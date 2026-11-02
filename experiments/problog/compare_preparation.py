"""Compare complete imperative and ProbLog tasks in bounded fresh processes.

The interpreted and optimized-fresh modes prepare every task. Optimized-cached
uses the production preparation cache: its first task is cold, later tasks warm.
All task timers include model assembly, sampling, decoding and PDDL rendering.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
from importlib import import_module
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

from benchmark import Case, cases, peak_rss, source_hashes as backend_hashes

MODES = ("imperative", "interpreted", "optimized-fresh", "optimized-cached")
DEFAULT_CASES = ("ferry-test-max", "delivery-test-max", "rovers-downward-10",
                 "rovers-downward-15", "rovers-downward-medium", "rovers-downward-large")
QUERIES = "\n".join(f"query({term})." for term in (
    "object(_,_)", "initial(_)", "goal(_)", "domain(_)", "problem_name(_)", "failure(_)"))
ROOT = Path(__file__).resolve().parents[2]


def source_hashes() -> dict[str, str]:
    sources = [Path(__file__), ROOT / "src/pypddl_datasets/generators/runtime.py",
               *ROOT.glob("tests/reference_generators/*.py"),
               *(ROOT / f"src/pypddl_datasets/generators/classical/{domain}/parameters.py"
                 for domain in ("ferry", "delivery", "rovers"))]
    return {**backend_hashes(), **{str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                  for path in sources}}


def emit(event: dict[str, Any]) -> None:
    print(json.dumps(event), flush=True)


def source_for(case: Case) -> str:
    from pypddl_datasets.generators import model_source
    return model_source(case.domain, case.parameters) + "\n" + QUERIES


def prepare_sampler(case: Case, mode: str):
    """Load each implementation before starting its separately reported task timer."""
    from pypddl_datasets.generators.runtime import render_problem
    if mode == "imperative":
        sys.path.insert(0, str(ROOT / "tests"))
        reference = import_module(f"reference_generators.{case.domain}")
        parameters = reference.Parameters(**case.parameters)
        return lambda seed: (problem := reference.sample(parameters, Random(seed)), render_problem(problem))
    from pypddl_datasets.generators._problog.engine import sample_source
    from pypddl_datasets.generators._problog.output import decode_world

    def sample(seed: int):
        problem = decode_world(sample_source(source_for(case), Random(seed), accelerated=mode != "interpreted"))
        return problem, render_problem(problem)

    return sample


def preparation_cost(case: Case, mode: str) -> None:
    """Measure setup components after task timing, leaving the first task cold."""
    if mode == "imperative":
        return
    from pypddl_datasets.generators._problog.programs import create_sampling_program
    start = perf_counter()
    for _ in range(10):
        source = source_for(case)
    source_seconds = (perf_counter() - start) / 10
    start = perf_counter()
    create_sampling_program(source, accelerated=mode != "interpreted")
    emit({"event": "preparation", "source_seconds": source_seconds,
          "prepare_seconds": perf_counter() - start,
          "model_source_sha256": hashlib.sha256(source.encode()).hexdigest()})


def worker(case: Case, mode: str, samples: int, memory_mib: int) -> None:
    if memory_mib:
        limit = memory_mib * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    start = perf_counter()
    sample = prepare_sampler(case, mode)
    emit({"event": "ready", "setup_seconds": perf_counter() - start})
    for seed in range(samples):
        if mode in ("interpreted", "optimized-fresh"):
            from pypddl_datasets.generators._problog.prepared import clear_prepared_cache
            clear_prepared_cache()
        start = perf_counter()
        try:
            problem, pddl = sample(seed)
            result = {"event": "sample", "seed": seed, "status": "success",
                      "objects": len(problem.objects), "initial": len(problem.initial),
                      "goals": len(problem.goal), "pddl_bytes": len(pddl.encode()),
                      "sha256": hashlib.sha256(pddl.encode()).hexdigest()}
        except Exception as error:  # A model failure is an observation, not a hidden dropped sample.
            result = {"event": "sample", "seed": seed, "status": "failure",
                      "error_type": type(error).__name__, "error": str(error)}
        result["seconds"] = perf_counter() - start
        result["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        emit(result)
        if result.get("error_type") in {"MemoryError", "RecursionError"}:
            return
    preparation_cost(case, mode)


def summarize(events: list[dict[str, Any]]) -> dict[str, Any]:
    samples = [event for event in events if event["event"] == "sample"]
    success = [event for event in samples if event["status"] == "success"]
    times = [event["seconds"] for event in success]
    return {"completed_tasks": len(success), "generation_failures": len(samples) - len(success),
            "first_task_seconds": samples[0]["seconds"] if samples else None,
            "mean_seconds": statistics.mean(times) if times else None,
            "median_seconds": statistics.median(times) if times else None,
            "min_seconds": min(times) if times else None, "max_seconds": max(times) if times else None,
            "warm_seconds": [event["seconds"] for event in success if event["seed"] > 0]}


def measure(case: Case, mode: str, args: argparse.Namespace) -> dict[str, Any]:
    count = args.imperative_samples if mode == "imperative" else args.interpreted_samples if mode == "interpreted" else args.samples
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", case.name, "--mode", mode,
               "--samples", str(count), "--memory-mib", str(args.memory_mib)]
    hashes_before = source_hashes()
    load_before = os.getloadavg()
    start = perf_counter()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    high_water = 0.0
    timed_out = False
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
    events = [json.loads(line) for line in stdout.splitlines() if line.startswith("{")]
    high_water = max([high_water, *(event.get("peak_rss_mib", 0) for event in events)])
    hashes_after = source_hashes()
    return {**asdict(case), "mode": mode, "samples_requested": count, "wall_seconds": perf_counter() - start,
            "load_average_at_start": load_before, "load_average_at_end": os.getloadavg(),
            "source_sha256": hashes_before, "source_sha256_after": hashes_after,
            "sources_changed_during_measurement": hashes_before != hashes_after,
            "status": "timeout" if timed_out else "completed" if process.returncode == 0 else "crashed",
            "exit_code": process.returncode, "peak_rss_mib": high_water,
            **summarize(events), "events": events, "stderr": stderr}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", help="repeatable case name; see benchmark.py --list")
    parser.add_argument("--mode", action="append", choices=MODES, help="repeatable; default all four")
    parser.add_argument("--samples", type=int, default=3, help="optimized tasks per mode and case")
    parser.add_argument("--imperative-samples", type=int, default=100)
    parser.add_argument("--interpreted-samples", type=int, default=1)
    parser.add_argument("--timeout", type=float, default=75, help="total seconds per mode and case, including imports")
    parser.add_argument("--memory-mib", type=int, default=2048, help="per-process address-space cap; 0 disables")
    parser.add_argument("--output", type=Path, default=Path("/tmp/problog-runtime-comparison.json"))
    parser.add_argument("--context", default="", help="concurrent work or other measurement conditions")
    parser.add_argument("--worker", help=argparse.SUPPRESS)
    args = parser.parse_args()
    available = {case.name: case for case in cases()}
    if min(args.samples, args.imperative_samples, args.interpreted_samples) < 1 or args.timeout <= 0 or args.memory_mib < 0:
        parser.error("sample counts and timeout must be positive; memory-mib must be nonnegative")
    if args.worker:
        worker(available[args.worker], args.mode[0], args.samples, args.memory_mib)
        return 0
    selected = args.case or DEFAULT_CASES
    if any(name not in available for name in selected):
        parser.error("unknown case; use benchmark.py --list")
    report: dict[str, Any] = {
        "recorded_at": datetime.now(timezone.utc).isoformat(), "python": sys.version,
        "platform": platform.platform(), "cpu_count": os.cpu_count(), "problog_version": version("problog"),
        "load_average_at_start": os.getloadavg(), "measurement_context": args.context,
        "source_sha256": source_hashes(),
        "timeout_seconds": args.timeout, "memory_limit_mib": args.memory_mib,
        "timing_policy": "Fresh process per case/mode. Imports are separate setup. Each task includes model assembly, sampling, decoding and rendering. Interpreted and optimized-fresh clear preparation cache before each task. Optimized-cached first task is cold. Preparation component probes run after task timing.",
        "cases": [],
    }
    for name in selected:
        for mode in args.mode or MODES:
            result = measure(available[name], mode, args)
            report["cases"].append(result)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, indent=2) + "\n")
            print(f"{name} / {mode}: {result['status']}, {result['completed_tasks']}/{result['samples_requested']} tasks, "
                  f"{result['wall_seconds']:.3f}s wall, {result['peak_rss_mib']:.1f} MiB", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
