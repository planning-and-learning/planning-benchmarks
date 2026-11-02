"""Compare declarative Rovers graph models in bounded isolated workers.

The sparse model is a shared-backbone structural proxy, not the classic IPC law.
The ipc2023 model changes the graph law only; other Rovers choices stay unchanged.
Full-task timing includes source assembly, sampling, decoding and PDDL rendering.
Graph-only timing instead produces compact edge counts, omitting task output.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import platform
from random import Random
import resource
import statistics
import subprocess
import sys
from time import perf_counter
from typing import Any

from benchmark import Case, cases, peak_rss

ROOT = Path(__file__).resolve().parents[2]
VARIANTS = ("current", "sparse", "ipc2023")
DEFAULT_CASES = ("rovers-downward-medium", "rovers-downward-large")
TASK_QUERIES = "\n".join(f"query({term})." for term in (
    "object(_,_)", "initial(_)", "goal(_)", "domain(_)", "problem_name(_)", "failure(_)"))
GRAPH_QUERIES = """
experiment_graph_counts(Visibility,Movement) :- graphs(V,Gs),length(V,Visibility),
    findall(count(R,N),(ground_member(r(R,Es),Gs),length(Es,N)),Movement).
query(experiment_graph_counts(_,_)).
query(failure(_)).
"""


def source_hashes() -> dict[str, str]:
    """Record the experiment, graph definitions and their production dependencies."""
    generators = ROOT / "src/pypddl_datasets/generators"
    experiment = Path(__file__).resolve().parent
    sources = [Path(__file__), experiment / "benchmark.py", experiment / "graph_models.py",
               generators / "runtime.py", generators / "probabilistic.py",
               generators / "classical/rovers/parameters.py",
               generators / "classical/rovers/distribution.pl",
               *experiment.rglob("*.pl"), *(generators / "_problog").glob("*.py"),
               *(generators / "_problog").glob("*.pl")]
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(set(sources)) if path.is_file()}


def emit(event: dict[str, Any]) -> None:
    print(json.dumps(event), flush=True)


def graph_counts(world: Any) -> dict[str, Any]:
    """Read the compact query without enumerating every edge into Python output."""
    from problog.logic import term2list
    failures = [str(term) for term, present in world.items() if present and term.functor == "failure"]
    if failures:
        raise RuntimeError("; ".join(failures))
    summaries = [term for term, present in world.items()
                 if present and term.functor == "experiment_graph_counts"]
    if len(summaries) != 1:
        raise ValueError(f"expected one graph count summary, got {len(summaries)}")
    count = summaries[0]
    return {"visibility_edges": int(count.args[0].value),
            "movement_edges": {str(item.args[0]): int(item.args[1].value)
                               for item in term2list(count.args[1], deep=False)}}


def task_graph_counts(problem: Any) -> dict[str, Any]:
    """Count undirected edges from the emitted symmetric PDDL predicates."""
    from pypddl_datasets.generators.runtime import Atom
    visibility = 0
    movement: Counter[str] = Counter()
    for fact in problem.initial:
        if isinstance(fact, Atom) and fact.predicate == "visible":
            visibility += 1
        elif isinstance(fact, Atom) and fact.predicate == "can_traverse":
            movement[fact.arguments[0]] += 1
    if visibility % 2 or any(count % 2 for count in movement.values()):
        raise ValueError("graph output does not have paired directed edges")
    return {"visibility_edges": visibility // 2,
            "movement_edges": {obj.name: movement[obj.name] // 2 for obj in problem.objects
                               if obj.type_name == "rover"}}


def worker(case: Case, variant: str, args: argparse.Namespace) -> None:
    if args.memory_mib:
        limit = args.memory_mib * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    start = perf_counter()
    from graph_models import source
    from pypddl_datasets.generators._problog.engine import sample_source
    from pypddl_datasets.generators._problog.output import decode_world
    from pypddl_datasets.generators.runtime import render_problem
    emit({"event": "ready", "setup_seconds": perf_counter() - start})
    queries = GRAPH_QUERIES if args.graph_only else TASK_QUERIES
    for seed in range(args.samples):
        start = perf_counter()
        try:
            program = source(variant, case.parameters) + "\n" + queries
            world = sample_source(program, Random(seed))
            if args.graph_only:
                counts = graph_counts(world)
                elapsed = perf_counter() - start
                result = {"event": "sample", "seed": seed, "status": "success", **counts}
            else:
                problem = decode_world(world)
                pddl = render_problem(problem)
                elapsed = perf_counter() - start
                result = {"event": "sample", "seed": seed, "status": "success",
                          "objects": len(problem.objects), "initial": len(problem.initial),
                          "goals": len(problem.goal), "pddl_bytes": len(pddl.encode()),
                          "sha256": hashlib.sha256(pddl.encode()).hexdigest(),
                          **task_graph_counts(problem)}
            result["model_source_sha256"] = hashlib.sha256(program.encode()).hexdigest()
        except Exception as error:  # Preserve failures instead of silently dropping samples.
            elapsed = perf_counter() - start
            result = {"event": "sample", "seed": seed, "status": "failure",
                      "error_type": type(error).__name__, "error": str(error)}
        result["seconds"] = elapsed
        result["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        emit(result)
        if result.get("error_type") in {"MemoryError", "RecursionError"}:
            return


def measure(case: Case, variant: str, args: argparse.Namespace) -> dict[str, Any]:
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", case.name,
               "--variant", variant, "--samples", str(args.samples),
               "--memory-mib", str(args.memory_mib)]
    if args.graph_only:
        command.append("--graph-only")
    before = source_hashes()
    load_before = os.getloadavg()
    start = perf_counter()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, cwd=ROOT)
    high_water = 0.0
    timed_out = False
    try:
        while True:
            high_water = max(high_water, peak_rss(process.pid))
            try:
                stdout, stderr = process.communicate(timeout=0.1)
                break
            except subprocess.TimeoutExpired:
                if perf_counter() - start >= args.timeout:
                    timed_out = True
                    process.kill()
                    stdout, stderr = process.communicate()
                    break
    except BaseException:
        process.kill()
        process.communicate()
        raise
    events = [json.loads(line) for line in stdout.splitlines() if line.startswith("{")]
    high_water = max([high_water, *(event.get("peak_rss_mib", 0) for event in events)])
    samples = [event for event in events if event["event"] == "sample"]
    successes = [event for event in samples if event["status"] == "success"]
    times = [event["seconds"] for event in successes]
    after = source_hashes()
    return {**asdict(case), "variant": variant, "graph_only": args.graph_only,
            "samples_requested": args.samples, "completed_tasks": len(successes),
            "generation_failures": len(samples) - len(successes),
            "status": "timeout" if timed_out else "completed" if process.returncode == 0 else "crashed",
            "exit_code": process.returncode, "wall_seconds": perf_counter() - start,
            "first_task_seconds": samples[0]["seconds"] if samples else None,
            "mean_seconds": statistics.mean(times) if times else None,
            "warm_seconds": [event["seconds"] for event in successes if event["seed"] > 0],
            "peak_rss_mib": high_water, "load_average_at_start": load_before,
            "load_average_at_end": os.getloadavg(), "source_sha256": before,
            "source_sha256_after": after, "sources_changed_during_measurement": before != after,
            "events": events, "stderr": stderr}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", help="repeatable case name; see --list")
    parser.add_argument("--variant", action="append", choices=VARIANTS, help="repeatable; default all three")
    parser.add_argument("--list", action="store_true", help="show available Rovers cases and provenance")
    parser.add_argument("--graph-only", action="store_true", help="sample graph counts without constructing a task")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=75, help="total seconds per isolated case/variant worker")
    parser.add_argument("--memory-mib", type=int, default=2048, help="address-space cap per worker; 0 disables")
    parser.add_argument("--output", type=Path, default=Path("/tmp/problog-graph-models.json"))
    parser.add_argument("--context", default="", help="concurrent work or other measurement conditions")
    parser.add_argument("--worker", help=argparse.SUPPRESS)
    args = parser.parse_args()
    available = {case.name: case for case in cases() if case.domain == "rovers"}
    if args.samples < 1 or args.timeout <= 0 or args.memory_mib < 0:
        parser.error("samples and timeout must be positive; memory-mib must be nonnegative")
    selected = args.case or DEFAULT_CASES
    if any(name not in available for name in selected) or (args.worker and args.worker not in available):
        parser.error("unknown Rovers case; use --list")
    if args.list:
        print(json.dumps([asdict(available[name]) for name in args.case or available], indent=2))
        return 0
    if args.worker:
        if not args.variant or len(args.variant) != 1:
            parser.error("workers require exactly one --variant")
        worker(available[args.worker], args.variant[0], args)
        return 0
    report: dict[str, Any] = {
        "recorded_at": datetime.now(timezone.utc).isoformat(), "python": sys.version,
        "platform": platform.platform(), "cpu_count": os.cpu_count(), "problog_version": version("problog"),
        "measurement_context": args.context, "source_sha256": source_hashes(),
        "samples_requested": args.samples, "timeout_seconds": args.timeout,
        "memory_limit_mib": args.memory_mib, "graph_only": args.graph_only,
        "timing_policy": "Fresh process per case/variant. Imports are separate setup. First draw is cold; later draws reuse prepared model. Full tasks include model assembly, sampling, decoding and rendering; graph-only queries produce compact counts. Full-task graph diagnostics and hashes are computed after timing. Timeouts retain completed seeds.",
        "distribution_scope": "Only graph definitions change. Sparse is a shared-backbone linear-edge-budget proxy; ipc2023 is the IPC2023 graph law with this repository's remaining Rovers choices.",
        "cases": [],
    }
    for name in selected:
        for variant in args.variant or VARIANTS:
            result = measure(available[name], variant, args)
            report["cases"].append(result)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, indent=2) + "\n")
            print(f"{name} / {variant}: {result['status']}, {result['completed_tasks']}/{args.samples} samples, "
                  f"{result['wall_seconds']:.3f}s wall, {result['peak_rss_mib']:.1f} MiB", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
