#!/usr/bin/env python3
"""Logistics where all packages start at the same location, with random goal locations.

Every city has one truck and one airport (its first location). Each package needs one
load and one unload per vehicle it rides: the origin truck unless it starts at the
origin airport or stays in the origin city, a plane if its goal lies in another city,
and that city's truck unless the goal is the airport. Moves: the origin truck drives
to the origin (unless there) and once to each stop (local goals, plus the airport if
packages leave the city); one plane flies to the origin airport (the cheapest plane,
free if one is there) and once to each destination airport; each destination truck
drives to its airport (unless there) and once to each non-airport goal. Every drive
and flight in this count is one a plan cannot avoid.
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
    origin_city, origin = rng.choice(locations)
    goals = [rng.choice(locations) for _ in range(num_packages)]

    local = [goal for city, goal in goals if city == origin_city and goal != origin]
    foreign = [(city, goal) for city, goal in goals if city != origin_city]
    cost = 2 * len(local) + sum(2 + 2 * (origin != 0) + 2 * (goal != 0) for _, goal in foreign)
    stops = set(local) | ({0} if foreign and origin != 0 else set[int]())
    if stops:
        cost += (trucks[origin_city] != origin) + len(stops)
    if foreign:
        cost += min(plane != origin_city for plane in planes) + len({city for city, _ in foreign})
        for city in {city for city, _ in foreign}:
            far = {goal for c, goal in foreign if c == city and goal != 0}
            if far:
                cost += (trucks[city] != 0) + len(far)

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
        *(f"(obj {package})\n    (at {package} {loc(origin_city, origin)})" for package in packages),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem logistics-common-origin-c{num_cities}-s{city_size}-a{num_planes}-p{num_packages})
  (:domain logistics-strips)
  (:objects {' '.join(objects)})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at {package} {loc(*goal)})' for package, goal in zip(packages, goals))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Logistics task with all packages at one location.")
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
