#!/usr/bin/env python3
"""Transport (with road lengths) where all packages share one origin and one destination.

Every truck can hold all packages (the IPC's capacity draw, 2..4, conditioned on
that). Each package costs a pick-up and a drop. Each
truck that is used drives to the origin and from there to the destination, so using
one truck, the one closest to the origin, is optimal: cost
min_t dist(t, origin) + dist(origin, destination) + 2 * num_packages, with shortest
road distances on the IPC's Euclidean city (ipc/transport): num_nodes random points in a
size x size square at least min_distance apart, roads between points within the
degree-derived connect distance, lengths ceil(distance / 10). One package is the
single-package special case.
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
    num_trucks: int,
    num_packages: int,
    degree: int = 3,
    size: int = 1000,
    min_distance: int = 100,
    seed: int | None = None,
) -> str:
    if num_nodes < 2:
        raise ValueError("num_nodes must be at least 2")
    if num_trucks < 1:
        raise ValueError("num_trucks must be at least 1")
    if num_packages < 1:
        raise ValueError("num_packages must be at least 1")
    for name, value, minimum in (("degree", degree, 1), ("size", size, 1), ("min_distance", min_distance, 0)):
        if value < minimum:
            raise ValueError(f"{name} must be at least {minimum}")
    rng = random.Random(seed if seed is not None else int(time.time()))
    roads = _ipc.city_roads(rng, num_nodes, degree, size, min_distance)
    origin, destination = rng.sample(range(num_nodes), 2)
    trucks = [rng.randrange(num_nodes) for _ in range(num_trucks)]
    # the IPC draws capacities in 2..4; conditioned on holding every package (its sole use here)
    capacities = [
        rng.randint(max(2, num_packages), _ipc.MAX_CAPACITY) if num_packages <= _ipc.MAX_CAPACITY else num_packages
        for _ in trucks
    ]
    from_origin = _distances(num_nodes, roads, origin)
    cost = min(from_origin[truck] for truck in trucks) + from_origin[destination] + 2 * num_packages

    numbers = [f"capacity-{i}" for i in range(max(_ipc.MAX_CAPACITY, num_packages) + 1)]  # at least the IPC's
    init = [
        "(= (total-cost) 0)",
        *(f"(capacity-predecessor {a} {b})" for a, b in zip(numbers, numbers[1:])),
        *(f"(road l{u} l{v})\n    (= (road-length l{u} l{v}) {length})" for (u, v), length in sorted(roads.items())),
        *(
            f"(at truck-{i} l{node})\n    (capacity truck-{i} capacity-{capacity})"
            for i, (node, capacity) in enumerate(zip(trucks, capacities))
        ),
        *(f"(at package-{i} l{origin})" for i in range(num_packages)),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem transport-common-route-n{num_nodes}-t{num_trucks}-p{num_packages})
  (:domain transport)
  (:objects
    {' '.join(f'l{node}' for node in range(num_nodes))} - location
    {' '.join(f'truck-{i}' for i in range(num_trucks))} - vehicle
    {' '.join(f'package-{i}' for i in range(num_packages))} - package
    {' '.join(numbers)} - capacity-number
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
    parser.add_argument("-d", "--degree", type=int, default=3, help="roads per location (default: 3)")
    parser.add_argument("--size", type=int, default=1000, help="side of the square city (default: 1000)")
    parser.add_argument("--min-distance", type=int, default=100, help="least distance between locations (default: 100)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(
            args.num_nodes, args.num_trucks, args.num_packages, args.degree, args.size, args.min_distance, args.seed
        )
        print(problem, end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
