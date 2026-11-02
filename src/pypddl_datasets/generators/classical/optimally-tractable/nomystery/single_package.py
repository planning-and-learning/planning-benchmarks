#!/usr/bin/env python3
"""Nomystery with one truck and one package on the IPC 2011 road network.

The roads are drawn as by the IPC generator (ipc/nomystery): a random spanning tree
plus random further roads up to edge_factor * num_locations, each with a fuel cost in
1..max_edge_cost. The truck starts with constrainedness times the cheapest fuel that
delivers the package, the IPC's rule, so every task is solvable without redrawing.

With one package the optimal plan drives to it, loads, drives to the goal and
unloads; unloading anywhere else costs two actions and changes nothing. So the
optimal cost is 2 + the fewest drives on a route truck -> package -> goal whose fuel
cost fits, found by breadth-first search over (location, fuel left, loaded) with
2 * locations * (fuel + 1) states: polynomial in the task, whose fuel levels are objects.
"""

from __future__ import annotations

import argparse
import heapq
import random
import sys
import time
from collections import deque

from pypddl_datasets.generators.classical.ipc.nomystery import generator as _ipc

Graph = list[list[int | None]]


def _fuel_distances(graph: Graph, source: int) -> list[int]:
    """Cheapest fuel from ``source`` to every location (Dijkstra)."""
    distances = [-1] * len(graph)
    queue = [(0, source)]
    while queue:
        distance, node = heapq.heappop(queue)
        if distances[node] >= 0:
            continue
        distances[node] = distance
        for other, cost in enumerate(graph[node]):
            if cost is not None and distances[other] < 0:
                heapq.heappush(queue, (distance + cost, other))
    return distances


def optimal_cost(graph: Graph, truck: int, fuel: int, package: int, goal: int) -> int | None:
    """Fewest actions to bring the package to ``goal`` with ``fuel``, or None if that is impossible."""
    start: tuple[int, int, bool] = (truck, fuel, False)
    seen: set[tuple[int, int, bool]] = {start}
    queue: deque[tuple[tuple[int, int, bool], int]] = deque([(start, 0)])
    while queue:
        (here, left, loaded), steps = queue.popleft()
        if loaded and here == goal:
            return steps + 1  # unload
        successors = [(here, left, True)] if not loaded and here == package else []
        successors += [
            (there, left - cost, loaded) for there, cost in enumerate(graph[here]) if cost is not None and cost <= left
        ]
        for successor in successors:
            if successor not in seen:
                seen.add(successor)
                queue.append((successor, steps + 1))
    return None


def make_problem(
    num_locations: int,
    edge_factor: float = 1.5,
    max_edge_cost: int = 25,
    constrainedness: float = 1.0,
    seed: int | None = None,
) -> str:
    if num_locations < 2:
        raise ValueError("num_locations must be at least 2")
    if edge_factor < 0:
        raise ValueError("edge_factor must be non-negative")
    if max_edge_cost < 1:
        raise ValueError("max_edge_cost must be at least 1")
    if constrainedness < 1:
        raise ValueError("constrainedness must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    graph = _ipc.road_graph(rng, num_locations, edge_factor, max_edge_cost)
    truck, package = rng.randrange(num_locations), rng.randrange(num_locations)
    goal = rng.choice([location for location in range(num_locations) if location != package])
    minimum = _fuel_distances(graph, truck)[package] + _fuel_distances(graph, package)[goal]
    fuel = int(constrainedness * minimum)
    max_fuel = max(fuel, max_edge_cost)
    cost = optimal_cost(graph, truck, fuel, package, goal)
    assert cost is not None  # the cheapest route fits the fuel

    init = [
        "(= (total-cost) 0)",
        *(f"(sum level{a} level{b} level{a + b})" for a in range(max_fuel + 1) for b in range(max_fuel + 1 - a)),
        *(
            f"(connected l{u} l{v})\n    (fuelcost level{cost} l{u} l{v})"
            for u, row in enumerate(graph)
            for v, cost in enumerate(row)
            if cost is not None
        ),
        f"(at t0 l{truck})",
        f"(fuel t0 level{fuel})",
        f"(at p0 l{package})",
    ]
    return f"""; optimal plan cost: {cost}
(define (problem nomystery-single-package-l{num_locations}-f{fuel})
  (:domain transport-strips)
  (:objects
    {' '.join(f'l{i}' for i in range(num_locations))} - location
    {' '.join(f'level{i}' for i in range(max_fuel + 1))} - fuellevel
    t0 - truck
    p0 - package
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
      (at p0 l{goal})
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Nomystery task with one truck and one package.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-e", "--edge-factor", type=float, default=1.5, help="roads per location (default: 1.5)")
    parser.add_argument("-m", "--max-edge-cost", type=int, default=25, help="largest road fuel cost (default: 25)")
    parser.add_argument("-c", "--constrainedness", type=float, default=1.0, help="fuel / cheapest fuel (default: 1)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(
            args.num_locations, args.edge_factor, args.max_edge_cost, args.constrainedness, args.seed
        )
        print(problem, end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
