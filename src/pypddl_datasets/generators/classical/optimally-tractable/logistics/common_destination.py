#!/usr/bin/env python3
"""Logistics where all packages go to the same location, from random origins.

Every city has one truck and one airport (its first location). Loads and unloads:
one pair per vehicle leg, as in common_origin. Moves: each source city's truck
visits its distinct non-airport origins (the one it starts at for free) and then the
airport; the planes visit every source airport and then the goal airport, which one
plane does in |source airports| + 1 flights, one less if some plane starts at a
source airport (several planes never do better); the goal city's truck visits the
local origins and, if packages arrive by plane and the goal is not the airport, the
airport (the one it starts at for free), and then the goal.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_cities: int, city_size: int, num_planes: int, num_packages: int, seed: int | None = None) -> str:
    for name, value in (("num_cities", num_cities), ("city_size", city_size), ("num_planes", num_planes)):
        if value < 1:
            raise ValueError(f"{name} must be at least 1")
    if num_packages < 1:
        raise ValueError("num_packages must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    locations = [(city, i) for city in range(num_cities) for i in range(city_size)]
    trucks = [rng.randrange(city_size) for _ in range(num_cities)]
    planes = [rng.randrange(num_cities) for _ in range(num_planes)]
    goal_city, goal = rng.choice(locations)
    origins = [rng.choice(locations) for _ in range(num_packages)]

    local = [origin for city, origin in origins if city == goal_city and origin != goal]
    foreign = [(city, origin) for city, origin in origins if city != goal_city]
    cost = 2 * len(local) + sum(2 + 2 * (origin != 0) + 2 * (goal != 0) for _, origin in foreign)
    for city in {city for city, _ in foreign}:
        pickups = {origin for c, origin in foreign if c == city and origin != 0}
        if pickups:
            cost += len(pickups) - (trucks[city] in pickups) + 1
    stops = set(local) | ({0} if foreign and goal != 0 else set[int]())
    if stops:
        cost += len(stops) - (trucks[goal_city] in stops) + 1
    if foreign:
        sources = {city for city, _ in foreign}
        cost += len(sources) + 1 - any(plane in sources for plane in planes)

    def loc(city: int, i: int) -> str:
        return f"c{city}-l{i}"

    packages = [f"p{i}" for i in range(num_packages)]
    objects = [
        *(f"c{city}" for city in range(num_cities)),
        *(loc(*location) for location in locations),
        *(f"t{city}" for city in range(num_cities)),
        *(f"a{i}" for i in range(num_planes)),
        *packages,
    ]
    init = [
        *(f"(city c{city})" for city in range(num_cities)),
        *(f"(location {loc(*location)})\n    (in-city {loc(*location)} c{location[0]})" for location in locations),
        *(f"(airport {loc(city, 0)})" for city in range(num_cities)),
        *(f"(truck t{city})\n    (at t{city} {loc(city, i)})" for city, i in enumerate(trucks)),
        *(f"(airplane a{i})\n    (at a{i} {loc(city, 0)})" for i, city in enumerate(planes)),
        *(f"(obj {package})\n    (at {package} {loc(*origin)})" for package, origin in zip(packages, origins)),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem logistics-common-destination-c{num_cities}-s{city_size}-a{num_planes}-p{num_packages})
  (:domain logistics-strips)
  (:objects {' '.join(objects)})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at {package} {loc(goal_city, goal)})' for package in packages)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Logistics task with all packages going to one location.")
    parser.add_argument("-c", "--num-cities", type=int, required=True)
    parser.add_argument("-s", "--city-size", type=int, required=True)
    parser.add_argument("-a", "--num-planes", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-r", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_cities, args.city_size, args.num_planes, args.num_packages, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
