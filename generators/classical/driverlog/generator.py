#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def _connected_edges(num_locations: int, extra_edges: int, rng: random.Random) -> set[tuple[int, int]]:
    edges = {(index, index + 1) for index in range(num_locations - 1)}
    max_edges = num_locations * (num_locations - 1) // 2
    target_edges = min(max_edges, len(edges) + extra_edges)
    while len(edges) < target_edges:
        left, right = rng.sample(range(num_locations), 2)
        if left > right:
            left, right = right, left
        edges.add((left, right))
    return edges


def _bidirectional_facts(predicate: str, edges: set[tuple[int, int]], locations: list[str]) -> list[str]:
    facts = []
    for left, right in sorted(edges):
        facts.append(f"    ({predicate} {locations[left]} {locations[right]})")
        facts.append(f"    ({predicate} {locations[right]} {locations[left]})")
    return facts


def make_problem(num_locations: int, num_drivers: int, num_trucks: int, num_packages: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    locations = [f"s{i}" for i in range(num_locations)]
    drivers = [f"driver{i}" for i in range(1, num_drivers + 1)]
    trucks = [f"truck{i}" for i in range(1, num_trucks + 1)]
    packages = [f"package{i}" for i in range(1, num_packages + 1)]

    road_edges = _connected_edges(num_locations, num_locations, rng)
    path_edges = _connected_edges(num_locations, max(1, num_locations // 2), rng)

    init_facts = []
    init_facts.extend(_bidirectional_facts("link", road_edges, locations))
    init_facts.extend(_bidirectional_facts("path", path_edges, locations))
    init_facts.extend(f"    (at {driver} {rng.choice(locations)})" for driver in drivers)
    init_facts.extend(f"    (at {truck} {rng.choice(locations)})" for truck in trucks)
    init_facts.extend(f"    (empty {truck})" for truck in trucks)

    package_goals = []
    for package in packages:
        origin, destination = rng.sample(locations, 2)
        init_facts.append(f"    (at {package} {origin})")
        package_goals.append(f"      (at {package} {destination})")

    object_lines = [
        f"      {' '.join(locations)} - location",
        f"      {' '.join(drivers)} - driver",
        f"      {' '.join(trucks)} - truck",
        f"      {' '.join(packages)} - obj",
    ]

    return f"""(define (problem driverlog-l{num_locations}-d{num_drivers}-t{num_trucks}-p{num_packages})
  (:domain driverlog)
  (:objects
{chr(10).join(object_lines)}
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(package_goals)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Driverlog PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-d", "--num-drivers", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)

    if args.num_locations < 2:
        parser.error("num_locations must be at least 2")
    if args.num_drivers < 1:
        parser.error("num_drivers must be at least 1")
    if args.num_trucks < 1:
        parser.error("num_trucks must be at least 1")
    if args.num_packages < 1:
        parser.error("num_packages must be at least 1")

    print(make_problem(args.num_locations, args.num_drivers, args.num_trucks, args.num_packages, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
