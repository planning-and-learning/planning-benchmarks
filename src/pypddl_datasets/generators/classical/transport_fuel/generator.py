#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
from collections import deque


def _distance(neighbors: dict[str, list[str]], source: str, target: str) -> int:
    frontier = deque([(source, 0)])
    reached = {source}
    while frontier:
        current, distance = frontier.popleft()
        if current == target:
            return distance
        for neighbor in neighbors[current]:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append((neighbor, distance + 1))
    raise ValueError("road graph must be connected")


def make_problem(
    num_locations: int,
    num_trucks: int,
    num_packages: int,
    capacity: int = 2,
    extra_edges: int = 0,
    fuel: int | None = None,
    seed: int | None = None,
) -> str:
    """Generate a fuel-limited Transport task with empty trucks and no refuelling.

    Roads form a random spanning tree plus ``extra_edges`` additional pairs.
    Every package must move to another location. All trucks have the same
    positive cargo capacity and initial fuel; each drive consumes one unit.
    With ``fuel=None``, the budget is a constructive upper bound: enough for
    the first truck to deliver packages one at a time in generated order,
    following shortest road paths. This guarantees solvability, without
    computing an optimal plan. Smaller explicit budgets permit tight training
    instances but may be unsolvable. There are no action costs.
    """
    for name, value, minimum in (
        ("num_locations", num_locations, 2),
        ("num_trucks", num_trucks, 1),
        ("num_packages", num_packages, 1),
        ("capacity", capacity, 1),
        ("extra_edges", extra_edges, 0),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    max_extra_edges = (num_locations - 1) * (num_locations - 2) // 2
    if extra_edges > max_extra_edges:
        raise ValueError(f"extra_edges must be at most {max_extra_edges} for {num_locations} locations")
    if fuel is not None and (not isinstance(fuel, int) or isinstance(fuel, bool) or fuel < 0):
        raise ValueError("fuel must be None or an integer at least 0")

    rng = random.Random(seed)
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
    truck_locations = [rng.choice(locations) for _ in trucks]
    for truck, location in zip(trucks, truck_locations):
        init_facts.append(f"    (at {truck} {location})")
        init_facts.append(f"    (capacity {truck} {sizes[-1]})")

    goals = []
    route = [truck_locations[0]]
    for package in packages:
        origin, destination = rng.sample(locations, 2)
        init_facts.append(f"    (at {package} {origin})")
        goals.append(f"      (at {package} {destination})")
        route.extend((origin, destination))

    if fuel is None:
        neighbors = {location: [] for location in locations}
        for left, right in sorted(edges):
            neighbors[locations[left]].append(locations[right])
            neighbors[locations[right]].append(locations[left])
        fuel = sum(_distance(neighbors, source, target) for source, target in zip(route, route[1:]))
    fuel_levels = [f"fuel{i}" for i in range(fuel + 1)]
    init_facts.extend(f"    (fuel {truck} {fuel_levels[-1]})" for truck in trucks)
    init_facts.extend(
        f"    (fuel-predecessor {fuel_levels[index]} {fuel_levels[index + 1]})"
        for index in range(fuel)
    )

    return f"""(define (problem transport-fuel-l{num_locations}-t{num_trucks}-p{num_packages}-c{capacity}-e{extra_edges}-f{fuel})
  (:domain transport-fuel)
  (:objects
    {' '.join(locations)} - location
    {' '.join(trucks)} - vehicle
    {' '.join(packages)} - package
    {' '.join(sizes)} - size
    {' '.join(fuel_levels)} - fuellevel
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
    parser = argparse.ArgumentParser(description="Generate a fuel-limited Transport PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-c", "--capacity", type=int, default=2, help="capacity of each initially empty truck (default: 2)")
    parser.add_argument("-e", "--extra-edges", type=int, default=0, help="additional undirected roads beyond a spanning tree (default: 0)")
    parser.add_argument("-f", "--fuel", type=int, help="initial fuel per truck; default covers a constructive delivery route, lower budgets may be unsolvable")
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
