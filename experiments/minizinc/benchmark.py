"""Bounded MiniZinc versus current ProbLog Rovers graph comparison.

MiniZinc searches for feasible assignments; it does NOT preserve the ProbLog law.
Every successful graph is materialized and independently checked before reporting.
"""
from __future__ import annotations

import argparse
from contextlib import suppress
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def limits(memory_mib: int) -> None:
    if memory_mib:
        resource.setrlimit(resource.RLIMIT_AS, (memory_mib * 1024**2,) * 2)


def process_birth(pid: int) -> str:
    """Linux process start ticks distinguish a tracked child from PID reuse."""
    return Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[19]


def terminate_tracked(processes: dict[int, str]) -> None:
    """Solvers can create their own process groups, so kill tracked PIDs too."""
    for pid, birth in reversed(list(processes.items())):
        with suppress(FileNotFoundError, ProcessLookupError):
            if process_birth(pid) == birth:
                os.kill(pid, signal.SIGKILL)


def memory_tree(pid: int, processes: dict[int, str]) -> float:
    """Sample aggregate resident bytes of a process and its descendants."""
    pending = [pid]
    rss = 0
    while pending:
        current = pending.pop()
        try:
            processes[current] = process_birth(current)
            rss += int(Path(f"/proc/{current}/statm").read_text().split()[1]) * os.sysconf("SC_PAGE_SIZE")
            pending.extend(map(int, Path(f"/proc/{current}/task/{current}/children").read_text().split()))
        except (FileNotFoundError, ProcessLookupError):
            pass
    return rss / 1024**2


def run(command: list[str], timeout: float, memory_mib: int) -> dict:
    start = perf_counter()
    process = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, start_new_session=True,
                               preexec_fn=lambda: limits(memory_mib))
    peak = 0.0
    tracked: dict[int, str] = {process.pid: process_birth(process.pid)}
    timed_out = False
    try:
        while True:
            peak = max(peak, memory_tree(process.pid, tracked))
            try:
                stdout, stderr = process.communicate(timeout=0.05)
                break
            except subprocess.TimeoutExpired:
                if perf_counter() - start >= timeout:
                    timed_out = True
                    terminate_tracked(tracked)
                    with suppress(ProcessLookupError):
                        os.killpg(process.pid, signal.SIGKILL)
                    stdout, stderr = process.communicate()
                    break
    except BaseException:
        terminate_tracked(tracked)
        with suppress(ProcessLookupError):
            os.killpg(process.pid, signal.SIGKILL)
        process.communicate()
        raise
    terminate_tracked(tracked)
    return {"status": "timeout" if timed_out else "completed" if process.returncode == 0 else "error",
            "wall_seconds": perf_counter() - start, "peak_tree_rss_mib": peak,
            "exit_code": process.returncode, "stdout": stdout, "stderr": stderr}


def connected(n: int, edges: list[tuple[int, int]]) -> bool:
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        if not 0 <= a < b < n:
            raise ValueError("invalid edge")
        adjacency[a].add(b)
        adjacency[b].add(a)
    visited = {0}
    frontier = [0]
    while frontier:
        for b in adjacency[frontier.pop()] - visited:
            visited.add(b)
            frontier.append(b)
    return len(visited) == n


def validate(solution: dict, goals: int) -> dict:
    n, nr = solution["n"], solution["nr"]
    if type(n) is not int or type(nr) is not int or n < 2 or nr < 1:
        raise ValueError("invalid dimensions")
    if len(solution["src"]) != len(solution["dst"]):
        raise ValueError("mismatched endpoint lengths")
    if any(type(value) is not int for value in solution["src"] + solution["dst"]):
        raise ValueError("invalid endpoint types")
    if type(solution["graph_only"]) is not bool:
        raise ValueError("invalid graph_only type")
    for key, length in [("visible", n*(n-1)//2), ("move", nr*n*(n-1)//2),
                        ("soil_sample", n), ("soil_goal", n), ("soil_capable", nr)]:
        if len(solution[key]) != length or any(type(value) is not bool for value in solution[key]):
            raise ValueError("invalid Boolean array: " + key)
    if solution["graph_only"] and any(solution["soil_sample"] + solution["soil_goal"] + solution["soil_capable"]):
        raise ValueError("graph-only output contains soil state")
    candidates = [(a - 1, b - 1) for a, b in zip(solution["src"], solution["dst"])]
    expected = [(a, b) for a in range(n) for b in range(a + 1, n)]
    if candidates != expected:
        raise ValueError("incomplete or unordered candidate edges")
    m = len(candidates)
    if len(solution["visible"]) != m or len(solution["move"]) != nr * m:
        raise ValueError("invalid graph array dimensions")
    visible = [edge for edge, flag in zip(candidates, solution["visible"]) if flag]
    moves = [[edge for edge, flag in zip(candidates, solution["move"][r*m:(r+1)*m]) if flag]
             for r in range(nr)]
    if not connected(n, visible) or not all(connected(n, move) for move in moves):
        raise ValueError("disconnected output")
    if not all(set(move) <= set(visible) for move in moves):
        raise ValueError("movement outside visibility")
    if len(solution["rover_at"]) != nr or any(type(w) is not int or not 1 <= w <= n for w in [*solution["rover_at"], solution["lander_at"]]):
        raise ValueError("invalid placement")
    if not solution["graph_only"]:
        if sum(solution["soil_goal"]) != goals or not any(solution["soil_capable"]):
            raise ValueError("invalid soil goal count or equipment")
        if any(g and not s for g, s in zip(solution["soil_goal"], solution["soil_sample"])):
            raise ValueError("goal has no soil sample")
    canonical = {"visibility": visible, "movement": moves}
    return {"validated": True, "visibility_edges": len(visible), "movement_edges": list(map(len, moves)),
            "visibility_density": len(visible)/m, "movement_density": [len(move)/m for move in moves],
            "graph_sha256": hashlib.sha256(json.dumps(canonical, sort_keys=True).encode()).hexdigest(),
            "soil_goals": sum(solution["soil_goal"])}


def parse_minizinc(result: dict, goals: int, n: int, nr: int, graph_only: bool) -> dict:
    stdout = result.pop("stdout")
    stats = {}
    for line in stdout.splitlines():
        if line.startswith("%%%mzn-stat: "):
            key, value = line.removeprefix("%%%mzn-stat: ").split("=", 1)
            try:
                stats[key] = json.loads(value)
            except json.JSONDecodeError:
                stats[key] = value
    result["statistics"] = stats
    solutions = []
    for line in stdout.splitlines():
        if line.startswith('{"n":'):
            try:
                solutions.append(json.loads(line))
            except json.JSONDecodeError:
                if result["status"] == "completed":
                    raise
                result["truncated_solution_output"] = True
    result["solutions"] = len(solutions)
    for solution in solutions:
        if (solution["n"], solution["nr"], solution["graph_only"]) != (n, nr, graph_only):
            raise ValueError("solver output does not match requested configuration")
        validate(solution, goals)
    if solutions:
        result.update(validate(solutions[0], goals))
        result["solution_sha256"] = hashlib.sha256(json.dumps(solutions[0], sort_keys=True).encode()).hexdigest()
    elif result["status"] == "completed":
        result["status"] = "unsatisfiable" if "=====UNSATISFIABLE=====" in stdout else "no_solution"
    result["stdout_tail"] = "\n".join(line for line in stdout.splitlines() if not line.startswith('{"n":'))[-4000:]
    return result


def hashes() -> dict:
    from problog_baseline import source_hashes
    result = source_hashes()
    for path in HERE.glob("*"):
        if path.suffix in {".py", ".mzn"}:
            result[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minizinc", type=Path, required=True)
    parser.add_argument("--case", action="append", required=True, help="waypoints,rovers; repeatable")
    parser.add_argument("--backend", action="append", choices=["gecode", "chuffed", "cp-sat", "problog"], required=True)
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--seed-start", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--memory-mib", type=int, default=2048)
    parser.add_argument("--soil", action="store_true", help="MiniZinc graph+soil fragment, not full Rovers")
    parser.add_argument("--search-mode", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.samples < 1 or args.timeout <= 0 or args.memory_mib < 0:
        parser.error("samples/timeout must be positive and memory-mib nonnegative")
    for case in args.case:
        try:
            n, nr = map(int, case.split(","))
            if n < 2 or nr < 1:
                raise ValueError()
        except ValueError:
            parser.error("case requires waypoints>=2,rovers>=1")
    if args.soil and "problog" in args.backend:
        parser.error("ProbLog baseline is graph-only; run soil fragment separately")
    report = {"recorded_at": datetime.now(timezone.utc).isoformat(), "python": sys.version,
              "platform": platform.platform(), "minizinc_version": subprocess.check_output([str(args.minizinc), "--version"], text=True),
              "solvers": subprocess.check_output([str(args.minizinc), "--solvers"], text=True),
              "timeout_seconds_per_minizinc_seed": args.timeout, "timeout_seconds_problog_batch": args.timeout * args.samples, "address_space_limit_mib_per_process": args.memory_mib,
              "scope": "graphs+soil" if args.soil else "graphs", "search_mode": args.search_mode,
              "seed_start": args.seed_start, "samples_requested": args.samples,
              "source_sha256": hashes(), "model_source": (HERE/"rovers.mzn").read_text(), "cases": []}
    for case in args.case:
        n, nr = map(int, case.split(","))
        goals = min(n, max(1, n//4))
        for backend in args.backend:
            seeds = [args.seed_start] if backend == "problog" else range(args.seed_start, args.seed_start + args.samples)
            for seed in seeds:
                before = hashes()
                if backend == "problog":
                    command = [sys.executable, str(HERE/"problog_baseline.py"), "--waypoints", str(n), "--rovers", str(nr),
                               "--samples", str(args.samples), "--seed", str(args.seed_start), "--summary-only", "--memory-mib", str(args.memory_mib)]
                else:
                    data = f"n={n}; nr={nr}; num_goals={goals}; graph_only={str(not args.soil).lower()}; search_mode={args.search_mode};"
                    command = [str(args.minizinc), "--solver", backend, "--statistics", "--output-time", "-r", str(seed),
                               "-D", data, str(HERE/"rovers.mzn")]
                load = os.getloadavg()
                result = run(command, args.timeout * (args.samples if backend == "problog" else 1), args.memory_mib)
                if backend == "problog":
                    stdout = result.pop("stdout")
                    result["samples"] = [json.loads(line) for line in stdout.splitlines() if line.startswith("{")]
                    result["solutions"] = sum(row["status"] == "success" for row in result["samples"])
                else:
                    result = parse_minizinc(result, goals, n, nr, not args.soil)
                result.update(n=n, nr=nr, backend=backend, seed=seed,
                              load_average_at_start=load, source_sha256=before,
                              sources_changed=before != hashes(), command=command)
                report["cases"].append(result)
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(json.dumps(report, indent=2)+"\n")
                print(f"{n}/{nr} {backend} seed{seed}: {result['status']} {result['wall_seconds']:.3f}s {result['peak_tree_rss_mib']:.1f}MiB {result['solutions']} solutions", flush=True)
                if result["status"] in {"timeout", "error"}:
                    break


if __name__ == "__main__":
    main()
