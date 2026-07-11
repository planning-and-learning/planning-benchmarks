#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(
    num_cities: int,
    city_size: int,
    num_packages: int,
    num_airplanes: int,
    seed: int | None = None,
    goal_package_probability: float = 1.0,
) -> str:
    if not 0.0 <= goal_package_probability <= 1.0:
        raise ValueError("goal_package_probability must be in [0, 1]")

    rng = random.Random(seed if seed is not None else int(time.time()))
    num_trucks = num_cities

    airplanes = [f"a{i}" for i in range(num_airplanes)]
    cities = [f"c{i}" for i in range(num_cities)]
    trucks = [f"t{i}" for i in range(num_trucks)]
    locations = [f"l{c}-{l}" for c in range(num_cities) for l in range(city_size)]
    packages = [f"p{i}" for i in range(num_packages)]

    init_facts = []
    init_facts.extend(f"    (AIRPLANE {airplane})" for airplane in airplanes)
    init_facts.extend(f"    (CITY {city})" for city in cities)
    init_facts.extend(f"    (TRUCK {truck})" for truck in trucks)
    for c in range(num_cities):
        for l in range(city_size):
            init_facts.append(f"    (LOCATION l{c}-{l})")
            init_facts.append(f"    (in-city l{c}-{l} c{c})")
        init_facts.append(f"    (AIRPORT l{c}-0)")
    init_facts.extend(f"    (OBJ {package})" for package in packages)
    init_facts.extend(
        f"    (at t{c} l{c}-{rng.randrange(city_size)})" for c in range(num_cities)
    )
    init_facts.extend(
        f"    (at {airplane} l{rng.randrange(num_cities)}-0)"
        for airplane in airplanes
    )

    package_goals = []
    for package in packages:
        origin_city = rng.randrange(num_cities)
        origin_loc = rng.randrange(city_size)
        dest_city = rng.randrange(num_cities)
        dest_loc = rng.randrange(city_size)
        while dest_city == origin_city and dest_loc == origin_loc:
            dest_city = rng.randrange(num_cities)
            dest_loc = rng.randrange(city_size)
        init_facts.append(f"    (at {package} l{origin_city}-{origin_loc})")
        if rng.random() < goal_package_probability:
            package_goals.append((package, dest_city, dest_loc))

    if not package_goals and goal_package_probability > 0.0:
        package = rng.choice(packages)
        origin_fact_prefix = f"    (at {package} "
        origin = next(fact.removeprefix(origin_fact_prefix).removesuffix(")") for fact in init_facts if fact.startswith(origin_fact_prefix))
        origin_city, origin_loc = (int(part) for part in origin.removeprefix("l").split("-"))
        dest_city = rng.randrange(num_cities)
        dest_loc = rng.randrange(city_size)
        while dest_city == origin_city and dest_loc == origin_loc:
            dest_city = rng.randrange(num_cities)
            dest_loc = rng.randrange(city_size)
        package_goals.append((package, dest_city, dest_loc))

    goals = [f"      (at {package} l{dest_city}-{dest_loc})" for package, dest_city, dest_loc in package_goals]

    goal_probability_percent = round(goal_package_probability * 100)
    return f"""(define (problem logistics-c{num_cities}-s{city_size}-p{num_packages}-a{num_airplanes}-g{goal_probability_percent})
  (:domain logistics-strips)
  (:objects
    {" ".join(airplanes)}
    {" ".join(cities)}
    {" ".join(trucks)}
    {" ".join(locations)}
    {" ".join(packages)}
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
    parser = argparse.ArgumentParser(description="Generate a Logistics PDDL problem.")
    parser.add_argument("num_cities", type=int, help="number of cities")
    parser.add_argument("city_size", type=int, help="locations per city")
    parser.add_argument("num_packages", type=int, help="number of packages")
    parser.add_argument("num_airplanes", type=int, help="number of airplanes")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    parser.add_argument(
        "--goal-package-probability",
        type=float,
        default=1.0,
        help="probability that a package gets a goal atom",
    )
    args = parser.parse_args(argv)

    if args.num_cities < 1:
        parser.error("num_cities must be at least 1")
    if args.city_size < 2:
        parser.error("city_size must be at least 2")
    if args.num_packages < 1:
        parser.error("num_packages must be at least 1")
    if args.num_airplanes < 1:
        parser.error("num_airplanes must be at least 1")
    if not 0.0 <= args.goal_package_probability <= 1.0:
        parser.error("--goal-package-probability must be in [0, 1]")

    print(
        make_problem(
            args.num_cities,
            args.city_size,
            args.num_packages,
            args.num_airplanes,
            seed=args.seed,
            goal_package_probability=args.goal_package_probability,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
