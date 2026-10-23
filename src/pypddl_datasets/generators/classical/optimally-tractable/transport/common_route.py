#!/usr/bin/env python3
"""Transport (with road lengths) where all packages share one origin and one destination.

Every truck can hold all packages. Each package costs a pick-up and a drop. Each
truck that is used drives to the origin and from there to the destination, so using
one truck, the one closest to the origin, is optimal: cost
min_t dist(t, origin) + dist(origin, destination) + 2 * num_packages, with shortest
road distances. One package is the single-package special case.
"""

from __future__ import annotations

import argparse
import heapq
import random
import sys
import time


def _distances(num_nodes: int, roads: dict[tuple[int, int], int], source: int) -> list[int]:
    distances = [-1] * num_nodes
    queue = [(0, source)]
    while queue:
        distance, node = heapq.heappop(queue)
        if distances[node] >= 0:
            continue
        distances[node] = distance
        for (u, v), length in roads.items():
            if u == node and distances[v] < 0:
                heapq.heappush(queue, (distance + length, v))
    return distances


def make_problem(
    num_nodes: int, num_trucks: int, num_packages: int, extra_roads: int = 3, seed: int | None = None
) -> str:
    if num_nodes < 2:
        raise ValueError("num_nodes must be at least 2")
    if num_trucks < 1:
        raise ValueError("num_trucks must be at least 1")
    if num_packages < 1:
        raise ValueError("num_packages must be at least 1")
    if extra_roads < 0:
        raise ValueError("extra_roads must be at least 0")
    rng = random.Random(seed if seed is not None else int(time.time()))
    # a random spanning tree plus extra_roads random roads, both directions, lengths 1..10
    roads: dict[tuple[int, int], int] = {}
    pairs = [(rng.randrange(node), node) for node in range(1, num_nodes)]
    for _ in range(extra_roads):
        u, v = rng.sample(range(num_nodes), 2)
        pairs.append((u, v))
    for u, v in pairs:
        roads[u, v] = roads[v, u] = rng.randint(1, 10)
    origin, destination = rng.sample(range(num_nodes), 2)
    trucks = [rng.randrange(num_nodes) for _ in range(num_trucks)]
    from_origin = _distances(num_nodes, roads, origin)
    cost = min(from_origin[truck] for truck in trucks) + from_origin[destination] + 2 * num_packages

    capacities = [f"capacity-{i}" for i in range(num_packages + 1)]
    init = [
        "(= (total-cost) 0)",
        *(f"(capacity-predecessor {a} {b})" for a, b in zip(capacities, capacities[1:])),
        *(f"(road l{u} l{v})\n    (= (road-length l{u} l{v}) {length})" for (u, v), length in sorted(roads.items())),
        *(f"(at truck-{i} l{node})\n    (capacity truck-{i} {capacities[-1]})" for i, node in enumerate(trucks)),
        *(f"(at package-{i} l{origin})" for i in range(num_packages)),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem transport-common-route-n{num_nodes}-t{num_trucks}-p{num_packages})
  (:domain transport)
  (:objects
    {' '.join(f'l{node}' for node in range(num_nodes))} - location
    {' '.join(f'truck-{i}' for i in range(num_trucks))} - vehicle
    {' '.join(f'package-{i}' for i in range(num_packages))} - package
    {' '.join(capacities)} - capacity-number
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at package-{i} l{destination})' for i in range(num_packages))}
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Transport task where all packages share one route.")
    parser.add_argument("-n", "--num-nodes", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-e", "--extra-roads", type=int, default=3)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_nodes, args.num_trucks, args.num_packages, args.extra_roads, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
