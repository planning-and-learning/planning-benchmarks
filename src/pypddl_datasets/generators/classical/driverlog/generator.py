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


def make_problem(
    num_locations: int,
    num_drivers: int,
    num_trucks: int,
    num_packages: int,
    seed: int | None = None,
    package_goal_probability: float = 1.0,
    driver_goal_probability: float = 0.0,
    truck_goal_probability: float = 0.0,
) -> str:
    if not 0.0 <= package_goal_probability <= 1.0:
        raise ValueError("package_goal_probability must be in [0, 1]")
    if not 0.0 <= driver_goal_probability <= 1.0:
        raise ValueError("driver_goal_probability must be in [0, 1]")
    if not 0.0 <= truck_goal_probability <= 1.0:
        raise ValueError("truck_goal_probability must be in [0, 1]")

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

    driver_locations = {driver: rng.choice(locations) for driver in drivers}
    truck_locations = {truck: rng.choice(locations) for truck in trucks}
    init_facts.extend(f"    (at {driver} {location})" for driver, location in driver_locations.items())
    init_facts.extend(f"    (at {truck} {location})" for truck, location in truck_locations.items())
    init_facts.extend(f"    (empty {truck})" for truck in trucks)

    package_locations = {}
    package_goals = []
    for package in packages:
        origin, destination = rng.sample(locations, 2)
        package_locations[package] = origin
        init_facts.append(f"    (at {package} {origin})")
        if rng.random() < package_goal_probability:
            package_goals.append(f"      (at {package} {destination})")
    if not package_goals and package_goal_probability > 0.0:
        package = rng.choice(packages)
        destination = rng.choice([location for location in locations if location != package_locations[package]])
        package_goals.append(f"      (at {package} {destination})")

    driver_goals = []
    for driver in drivers:
        if rng.random() < driver_goal_probability:
            destination = rng.choice([location for location in locations if location != driver_locations[driver]])
            driver_goals.append(f"      (at {driver} {destination})")
    if not driver_goals and driver_goal_probability > 0.0:
        driver = rng.choice(drivers)
        destination = rng.choice([location for location in locations if location != driver_locations[driver]])
        driver_goals.append(f"      (at {driver} {destination})")

    truck_goals = []
    for truck in trucks:
        if rng.random() < truck_goal_probability:
            destination = rng.choice([location for location in locations if location != truck_locations[truck]])
            truck_goals.append(f"      (at {truck} {destination})")
    if not truck_goals and truck_goal_probability > 0.0:
        truck = rng.choice(trucks)
        destination = rng.choice([location for location in locations if location != truck_locations[truck]])
        truck_goals.append(f"      (at {truck} {destination})")

    object_lines = [
        f"      {' '.join(locations)} - location",
        f"      {' '.join(drivers)} - driver",
        f"      {' '.join(trucks)} - truck",
        f"      {' '.join(packages)} - obj",
    ]

    package_goal_percent = round(package_goal_probability * 100)
    driver_goal_percent = round(driver_goal_probability * 100)
    truck_goal_percent = round(truck_goal_probability * 100)
    goals = [*package_goals, *driver_goals, *truck_goals]

    return f"""(define (problem driverlog-l{num_locations}-d{num_drivers}-t{num_trucks}-p{num_packages}-pg{package_goal_percent}-dg{driver_goal_percent}-tg{truck_goal_percent})
  (:domain driverlog)
  (:objects
{chr(10).join(object_lines)}
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
    parser = argparse.ArgumentParser(description="Generate a Driverlog PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-d", "--num-drivers", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument(
        "--package-goal-probability",
        type=float,
        default=1.0,
        help="probability that a package gets a goal atom",
    )
    parser.add_argument(
        "--driver-goal-probability",
        type=float,
        default=0.0,
        help="probability that a driver gets a goal atom",
    )
    parser.add_argument(
        "--truck-goal-probability",
        type=float,
        default=0.0,
        help="probability that a truck gets a goal atom",
    )
    args = parser.parse_args(argv)

    if args.num_locations < 2:
        parser.error("num_locations must be at least 2")
    if args.num_drivers < 1:
        parser.error("num_drivers must be at least 1")
    if args.num_trucks < 1:
        parser.error("num_trucks must be at least 1")
    if args.num_packages < 1:
        parser.error("num_packages must be at least 1")
    if not 0.0 <= args.package_goal_probability <= 1.0:
        parser.error("--package-goal-probability must be in [0, 1]")
    if not 0.0 <= args.driver_goal_probability <= 1.0:
        parser.error("--driver-goal-probability must be in [0, 1]")
    if not 0.0 <= args.truck_goal_probability <= 1.0:
        parser.error("--truck-goal-probability must be in [0, 1]")

    print(
        make_problem(
            args.num_locations,
            args.num_drivers,
            args.num_trucks,
            args.num_packages,
            seed=args.seed,
            package_goal_probability=args.package_goal_probability,
            driver_goal_probability=args.driver_goal_probability,
            truck_goal_probability=args.truck_goal_probability,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
