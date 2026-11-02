#!/usr/bin/env python3
"""Transport (with road lengths) with one truck of capacity 1 and all packages going to
the same location g.

After the first delivery the truck is at g, so each later package p costs the round
trip 2 * dist(g, p) plus pick-up and drop. The first package p, reached from the
truck's start t, minimizes dist(t, p) - dist(p, g): the optimal cost is
sum_p (2 * dist(g, p) + 2) + min_p (dist(t, p) - dist(p, g)) over the packages not
at g, with shortest road distances on the IPC's Euclidean city (ipc/transport): num_nodes
random points in a size x size square at least min_distance apart, roads between
points within the degree-derived connect distance, lengths ceil(distance / 10).
"""

from __future__ import annotations

import argparse
import heapq
import random
import sys
import time

from pypddl_datasets.generators.classical.ipc.transport import generator as _ipc


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
    num_nodes: int,
    num_packages: int,
    degree: int = 3,
    size: int = 1000,
    min_distance: int = 100,
    seed: int | None = None,
) -> str:
    if num_nodes < 2:
        raise ValueError("num_nodes must be at least 2")
    if num_packages < 1:
        raise ValueError("num_packages must be at least 1")
    for name, value, minimum in (("degree", degree, 1), ("size", size, 1), ("min_distance", min_distance, 0)):
        if value < minimum:
            raise ValueError(f"{name} must be at least {minimum}")
    rng = random.Random(seed if seed is not None else int(time.time()))
    roads = _ipc.city_roads(rng, num_nodes, degree, size, min_distance)
    destination, truck = rng.randrange(num_nodes), rng.randrange(num_nodes)
    origins = [rng.choice([n for n in range(num_nodes) if n != destination]) for _ in range(num_packages)]
    to_goal, from_truck = _distances(num_nodes, roads, destination), _distances(num_nodes, roads, truck)
    cost = sum(2 * to_goal[o] + 2 for o in origins) + min(from_truck[o] - to_goal[o] for o in origins)

    capacities = [f"capacity-{i}" for i in range(_ipc.MAX_CAPACITY + 1)]  # the IPC's objects; the truck uses 0 and 1
    init = [
        "(= (total-cost) 0)",
        *(f"(capacity-predecessor {a} {b})" for a, b in zip(capacities, capacities[1:])),
        *(f"(road l{u} l{v})\n    (= (road-length l{u} l{v}) {length})" for (u, v), length in sorted(roads.items())),
        f"(at truck-0 l{truck})\n    (capacity truck-0 capacity-1)",
        *(f"(at package-{i} l{o})" for i, o in enumerate(origins)),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem transport-common-destination-n{num_nodes}-p{num_packages})
  (:domain transport)
  (:objects
    {' '.join(f'l{node}' for node in range(num_nodes))} - location
    truck-0 - vehicle
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
    parser = argparse.ArgumentParser(description="Generate a Transport task with one unit-capacity truck and one goal.")
    parser.add_argument("-n", "--num-nodes", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-d", "--degree", type=int, default=3, help="roads per location (default: 3)")
    parser.add_argument("--size", type=int, default=1000, help="side of the square city (default: 1000)")
    parser.add_argument("--min-distance", type=int, default=100, help="least distance between locations (default: 100)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_nodes, args.num_packages, args.degree, args.size, args.min_distance, args.seed)
        print(problem, end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
