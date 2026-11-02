"""Current Rovers graph-only sampler for the MiniZinc comparison.

This calls the existing accelerated ProbLog runtime and leaves the production
probability law intact. It does not sample equipment, positions or goals. Output
contains undirected zero-based edges, materialized just once for inspection.
MiniZinc solutions with matching legality constraints need not share this law.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from random import Random
import resource
from time import perf_counter
from typing import Any

from problog.logic import Term, term2list

from pypddl_datasets.generators._problog.engine import sample_source
from pypddl_datasets.generators.probabilistic import model_source

QUERIES = "\nquery(graphs(_,_)).\nquery(failure(_)).\n"
ROOT = Path(__file__).resolve().parents[2]


def source_hashes() -> dict[str, str]:
    """Record the helper and production dependencies used by the comparison."""
    generators = ROOT / "src/pypddl_datasets/generators"
    paths = [Path(__file__).resolve(), generators / "probabilistic.py",
             generators / "runtime.py", generators / "classical/rovers/parameters.py",
             generators / "classical/rovers/distribution.pl",
             *(generators / "_problog").glob("*.py"),
             *(generators / "_problog").glob("*.pl")]
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(paths)}


def _edges(value: Term) -> list[list[int]]:
    edges: list[list[int]] = []
    for item in term2list(value, deep=False):
        if item.functor != "e" or len(item.args) != 2:
            raise ValueError(f"unexpected graph edge: {item}")
        edges.append([int(item.args[0].value), int(item.args[1].value)])
    return edges


def _connected(node_count: int, edges: list[list[int]]) -> bool:
    adjacent: list[list[int]] = [[] for _ in range(node_count)]
    for left, right in edges:
        adjacent[left].append(right)
        adjacent[right].append(left)
    visited = {0}
    pending = [0]
    while pending:
        for neighbor in adjacent[pending.pop()]:
            if neighbor not in visited:
                visited.add(neighbor)
                pending.append(neighbor)
    return len(visited) == node_count


def _describe(node_count: int, visibility: list[list[int]],
              movement: list[list[list[int]]]) -> dict[str, Any]:
    maximum = node_count * (node_count - 1) // 2
    visible = {tuple(edge) for edge in visibility}
    traversable = [{tuple(edge) for edge in edges} for edges in movement]
    for edges, unique in zip([visibility, *movement], [visible, *traversable]):
        if len(edges) != len(unique) or any(not 0 <= left < right < node_count for left, right in edges):
            raise ValueError("graph contains duplicate, noncanonical or out-of-range edges")
    summary = {
        "visibility_edges": len(visibility), "movement_edges": [len(edges) for edges in movement],
        "visibility_density": len(visibility) / maximum if maximum else 0.0,
        "movement_density": [len(edges) / maximum if maximum else 0.0 for edges in movement],
        "visibility_connected": _connected(node_count, visibility),
        "movement_connected": [_connected(node_count, edges) for edges in movement],
        "movement_subset_visibility": [edges <= visible for edges in traversable],
    }
    if (not summary["visibility_connected"] or not all(summary["movement_connected"])
            or not all(summary["movement_subset_visibility"])):
        raise ValueError("sampled graph violates current Rovers graph constraints")
    return summary


def sample_graphs(num_waypoints: int, num_rovers: int, *, seed: int = 0,
                  edge_probability: float = 0.5, graph_budget: int | None = None) -> dict[str, Any]:
    """Sample and decode the current graph law; include source setup in total time.

    Other Rovers counts are fixed to valid minima and never queried. Validation,
    hashing and graph statistics run after the sampling/decode timer. Preparation
    is cold on the first call and reusable on later calls with the same parameters.
    Explicit graph exhaustion is returned as a failure; runtime exceptions propagate.
    """
    start = perf_counter()
    parameters: dict[str, int | float] = {
        "num_waypoints": num_waypoints, "num_rovers": num_rovers,
        "num_objectives": 1, "num_cameras": 0, "num_goals": 1,
        "edge_probability": edge_probability,
    }
    if graph_budget is not None:
        parameters["graph_budget"] = graph_budget
    program = model_source("rovers", parameters) + QUERIES
    assembled = perf_counter()
    world = sample_source(program, Random(seed), accelerated=True)
    sampled = perf_counter()
    failures = [str(term) for term, present in world.items() if present and term.functor == "failure"]
    graphs = [term for term, present in world.items() if present and term.functor == "graphs"]
    result: dict[str, Any] = {
        "backend": "problog", "num_waypoints": num_waypoints, "num_rovers": num_rovers,
        "edge_probability": edge_probability, "seed": seed,
        "source_seconds": assembled - start, "sampling_seconds": sampled - assembled,
    }
    if failures:
        if graphs:
            raise ValueError("world contains both graph failure and a successful graph")
        result.update(status="failure", failure=failures)
    else:
        if len(graphs) != 1:
            raise ValueError(f"expected one sampled graph world, got {len(graphs)}")
        visibility = _edges(graphs[0].args[0])
        indexed: dict[int, list[list[int]]] = {}
        for item in term2list(graphs[0].args[1], deep=False):
            if item.functor != "r" or len(item.args) != 2:
                raise ValueError(f"unexpected rover graph: {item}")
            rover = int(item.args[0].value)
            if rover in indexed:
                raise ValueError("duplicate rover graph")
            indexed[rover] = _edges(item.args[1])
        if set(indexed) != set(range(num_rovers)):
            raise ValueError("missing or out-of-range rover graph")
        movement = [indexed[index] for index in range(num_rovers)]
        result.update(status="success", visibility=visibility, movement=movement)
    decoded = perf_counter()
    result.update(decoding_seconds=decoded - sampled, seconds=decoded - start,
                  model_source_sha256=hashlib.sha256(program.encode()).hexdigest())
    if result["status"] == "success":
        result.update(_describe(num_waypoints, visibility, movement))
        semantic = {"visibility": visibility, "movement": movement}
        result["graph_sha256"] = hashlib.sha256(json.dumps(semantic, sort_keys=True).encode()).hexdigest()
    result["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--waypoints", type=int, required=True)
    parser.add_argument("--rovers", type=int, required=True)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--samples", type=int, default=1)
    parser.add_argument("--edge-probability", type=float, default=0.5)
    parser.add_argument("--graph-budget", type=int)
    parser.add_argument("--memory-mib", type=int, default=2048, help="process address-space cap; 0 disables")
    parser.add_argument("--summary-only", action="store_true", help="omit edge arrays after materializing and validating them")
    args = parser.parse_args()
    if args.samples < 1 or args.memory_mib < 0:
        parser.error("samples must be positive and memory-mib nonnegative")
    if args.memory_mib:
        resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib * 1024**2,) * 2)
    for seed in range(args.seed, args.seed + args.samples):
        result = sample_graphs(args.waypoints, args.rovers, seed=seed,
                               edge_probability=args.edge_probability, graph_budget=args.graph_budget)
        if args.summary_only:
            result.pop("visibility", None)
            result.pop("movement", None)
        print(json.dumps(result), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
