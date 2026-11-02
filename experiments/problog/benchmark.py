"""Measure complete generator calls in bounded, isolated Linux processes.

Run from the checkout with the environment containing this package installed.
Cases use committed split extrema or the object/goal counts of named Rovers tasks;
those historical Rovers tasks do not record their original sampling parameters.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import hashlib
import importlib
from importlib.metadata import version
import json
import os
from pathlib import Path
import platform
import random
import resource
import subprocess
import sys
import time
from typing import Any


@dataclass(frozen=True)
class Case:
    """A parameter configuration with inspectable repository provenance."""

    name: str
    domain: str
    parameters: dict[str, int | float]
    source: str


def cases() -> list[Case]:
    result: list[Case] = []
    for domain, names, rows in (
        ("ferry", ("num_cars", "num_locations"), ((7, 5), (11, 8), (17, 12))),
        ("delivery", ("grid_size", "num_packages"), ((5, 4), (8, 7), (13, 12))),
    ):
        for split, row in zip(("train", "valid", "test"), rows):
            result.append(Case(f"{domain}-{split}-max", domain, dict(zip(names, row)),
                               f"src/pypddl_datasets/generators/classical/{domain}/generate_instances.py"))
    names = ("num_rovers", "num_waypoints", "num_objectives", "num_cameras", "num_goals")
    for name, row, source in (
        ("test", (1, 2, 1, 1, 1), "tests/rovers/test-1.pddl"),
        ("downward-small", (1, 4, 2, 1, 3), "downward-benchmarks/rovers/p01.pddl"),
        ("downward-10", (4, 10, 4, 5, 8), "downward-benchmarks/rovers/p14.pddl"),
        ("downward-15", (6, 15, 6, 7, 13), "downward-benchmarks/rovers/p17.pddl"),
        ("downward-medium", (10, 25, 6, 10, 10), "downward-benchmarks/rovers/p25.pddl"),
        ("downward-large", (14, 100, 11, 15, 69), "downward-benchmarks/rovers/p40.pddl"),
        ("ipc-medium", (8, 53, 53, 28, 66), "ipc2023-learning/rovers_ipc2023_learning/medium_p16.pddl"),
        ("ipc-large", (30, 197, 236, 99, 728), "ipc2023-learning/rovers_ipc2023_learning/hard_p30.pddl"),
        ("htg-small", (1, 1000, 1, 1, 2), "htg-domains/rovers-large/p-r1-w1000-o1-1-g2-goal-2.pddl"),
        ("htg-large", (1, 5500, 1, 1, 8), "htg-domains/rovers-large/p-r1-w5500-o1-1-g8-goal-8.pddl"),
    ):
        result.append(Case(f"rovers-{name}", "rovers", dict(zip(names, row)), f"data/classical/{source}"))
    return result


def worker(case: Case, samples: int, memory_mib: int) -> None:
    """Emit each result immediately so a later timeout retains completed samples."""
    if memory_mib:
        limit = memory_mib * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    start = time.perf_counter()
    module = importlib.import_module(f"pypddl_datasets.generators.classical.{case.domain}.generator")
    parameters = module.Parameters(**case.parameters)
    print(json.dumps({"event": "ready", "setup_seconds": time.perf_counter() - start}), flush=True)
    for seed in range(samples):
        start = time.perf_counter()
        try:
            problem = module.sample(parameters, random.Random(seed))
            pddl = module.render(problem)
            result = {"event": "sample", "seed": seed, "status": "success",
                      "objects": len(problem.objects), "initial": len(problem.initial),
                      "goals": len(problem.goal), "pddl_bytes": len(pddl.encode()),
                      "sha256": hashlib.sha256(pddl.encode()).hexdigest()}
        except Exception as error:  # Report generation failures without hiding the case.
            result = {"event": "sample", "seed": seed, "status": "failure",
                      "error_type": type(error).__name__, "error": str(error)}
        result["seconds"] = time.perf_counter() - start
        result["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        print(json.dumps(result), flush=True)
        if result.get("error_type") in {"MemoryError", "RecursionError"}:
            break


def peak_rss(pid: int) -> float:
    try:
        lines = Path(f"/proc/{pid}/status").read_text().splitlines()
        return next(float(line.split()[1]) / 1024 for line in lines if line.startswith("VmHWM:"))
    except (FileNotFoundError, ProcessLookupError, StopIteration):
        return 0.0


def measure(case: Case, samples: int, timeout: float, memory_mib: int) -> dict[str, Any]:
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", case.name,
               "--samples", str(samples), "--memory-mib", str(memory_mib)]
    hashes_before = source_hashes()
    start = time.perf_counter()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    high_water = 0.0
    timed_out = False
    while True:
        high_water = max(high_water, peak_rss(process.pid))
        try:
            stdout, stderr = process.communicate(timeout=0.1)
            break
        except subprocess.TimeoutExpired:
            if time.perf_counter() - start >= timeout:
                timed_out = True
                process.kill()
                stdout, stderr = process.communicate()
                break
    events = [json.loads(line) for line in stdout.splitlines() if line.startswith("{")]
    high_water = max([high_water, *(event.get("peak_rss_mib", 0) for event in events)])
    return {**asdict(case), "wall_seconds": time.perf_counter() - start,
            "source_sha256": hashes_before, "sources_changed_during_measurement": hashes_before != source_hashes(),
            "status": "timeout" if timed_out else "completed" if process.returncode == 0 else "crashed",
            "exit_code": process.returncode, "peak_rss_mib": high_water,
            "events": events, "stderr": stderr}


def source_hashes() -> dict[str, str]:
    sources = [Path(__file__), *Path("src/pypddl_datasets/generators").glob("*proba*"),
               *Path("src/pypddl_datasets/generators/classical").glob("*/distribution.pl"),
               *(Path(f"src/pypddl_datasets/generators/classical/{domain}/generator.py")
                 for domain in ("ferry", "delivery", "rovers")),
               *Path("src/pypddl_datasets/generators/_problog").glob("*.py"),
               *Path("src/pypddl_datasets/generators/_problog").glob("*.pl")]
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in sources if path.is_file()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", help="run only these named cases; repeatable")
    parser.add_argument("--list", action="store_true", help="show available cases and provenance")
    parser.add_argument("--samples", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=60, help="seconds per case, including imports")
    parser.add_argument("--memory-mib", type=int, default=2048, help="per-worker virtual memory cap; 0 disables")
    parser.add_argument("--output", type=Path, default=Path("/tmp/problog-benchmark.json"))
    parser.add_argument("--worker", help=argparse.SUPPRESS)
    args = parser.parse_args()
    all_cases = {case.name: case for case in cases()}
    if args.samples < 1 or args.timeout <= 0 or args.memory_mib < 0:
        parser.error("samples and timeout must be positive; memory-mib must be nonnegative")
    if args.worker:
        worker(all_cases[args.worker], args.samples, args.memory_mib)
        return 0
    selected = args.case or list(all_cases)
    if any(name not in all_cases for name in selected):
        parser.error("unknown case; use --list to see available names")
    if args.list:
        print(json.dumps([asdict(all_cases[name]) for name in selected], indent=2))
        return 0
    report: dict[str, Any] = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "platform": platform.platform(), "cpu_count": os.cpu_count(),
        "problog_version": version("problog"), "source_sha256": source_hashes(),
        "samples_requested": args.samples, "timeout_seconds": args.timeout,
        "memory_limit_mib": args.memory_mib, "cases": [],
    }
    for name in selected:
        result = measure(all_cases[name], args.samples, args.timeout, args.memory_mib)
        report["cases"].append(result)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
        completed = sum(event.get("status") == "success" for event in result["events"])
        print(f"{name}: {result['status']}, {completed}/{args.samples} tasks, "
              f"{result['wall_seconds']:.3f}s, {result['peak_rss_mib']:.1f} MiB", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
