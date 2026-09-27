#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys


def make_problem(
    num_locations: int,
    num_trucks: int,
    num_packages: int,
    capacity: int = 2,
    extra_edges: int | None = None,
    seed: int | None = None,
    random_capacities: bool = True,
) -> str:
    """Generate a solvable Transport task with empty trucks and undirected roads.

    Roads form a random spanning tree plus ``extra_edges`` additional pairs;
    ``None`` (default) draws the edge count uniformly between a tree and the complete
    graph, like the learning track's ``random_connected_graph``. Every package must
    move to another location. With ``random_capacities`` (default) each truck gets a
    capacity uniform in 1..``capacity`` as in the learning track, otherwise all trucks
    have ``capacity``. No fuel constraints or action costs.
    """
    for name, value, minimum in (
        ("num_locations", num_locations, 2),
        ("num_trucks", num_trucks, 1),
        ("num_packages", num_packages, 1),
        ("capacity", capacity, 1),
        ("extra_edges", 0 if extra_edges is None else extra_edges, 0),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    max_extra_edges = (num_locations - 1) * (num_locations - 2) // 2
    if extra_edges is not None and extra_edges > max_extra_edges:
        raise ValueError(f"extra_edges must be at most {max_extra_edges} for {num_locations} locations")

    rng = random.Random(seed)
    if extra_edges is None:
        extra_edges = rng.randint(0, max_extra_edges)
    locations = [f"l{i}" for i in range(num_locations)]
    trucks = [f"t{i}" for i in range(num_trucks)]
    packages = [f"p{i}" for i in range(num_packages)]
    sizes = [f"capacity{i}" for i in range(capacity + 1)]

    order = list(range(num_locations))
    rng.shuffle(order)
    edges = set()
    for index in range(1, num_locations):
        left, right = order[index], order[rng.randrange(index)]
        edges.add((min(left, right), max(left, right)))
    if extra_edges:
        missing_edges = [
            (left, right)
            for left in range(num_locations)
            for right in range(left + 1, num_locations)
            if (left, right) not in edges
        ]
        edges.update(rng.sample(missing_edges, extra_edges))

    init_facts = []
    for left, right in sorted(edges):
        init_facts.append(f"    (road {locations[left]} {locations[right]})")
        init_facts.append(f"    (road {locations[right]} {locations[left]})")
    init_facts.extend(
        f"    (capacity-predecessor {sizes[index]} {sizes[index + 1]})"
        for index in range(capacity)
    )
    for truck in trucks:
        init_facts.append(f"    (at {truck} {rng.choice(locations)})")
        init_facts.append(f"    (capacity {truck} {sizes[rng.randint(1, capacity) if random_capacities else capacity]})")

    goals = []
    for package in packages:
        origin, destination = rng.sample(locations, 2)
        init_facts.append(f"    (at {package} {origin})")
        goals.append(f"      (at {package} {destination})")

    return f"""(define (problem transport-l{num_locations}-t{num_trucks}-p{num_packages}-c{capacity}-e{extra_edges})
  (:domain transport)
  (:objects
    {' '.join(locations)} - location
    {' '.join(trucks)} - vehicle
    {' '.join(packages)} - package
    {' '.join(sizes)} - size
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a cost-free Transport PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-c", "--capacity", type=int, default=2, help="maximum truck capacity (default: 2)")
    parser.add_argument("-e", "--extra-edges", type=int, help="roads beyond a spanning tree (default: random, as the learning track)")
    parser.add_argument("--equal-capacities", dest="random_capacities", action="store_false", help="every truck gets the maximum capacity")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
