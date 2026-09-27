#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators logistics/logistics.c (FF domain collection). Distributed
# under the original notice, not GPL-3.0-or-later (see LICENSES/LicenseRef-Freiburg.txt):
#
# (C) Copyright 2001 Albert Ludwigs University Freiburg
#     Institute of Computer Science
#
# All rights reserved. Use of this software is permitted for
# non-commercial research purposes, and it may be copied only
# for that use.  All copies must include this copyright message.
# This software is made available AS IS, and neither the authors
# nor the  Albert Ludwigs University Freiburg make any warranty
# about the software or its performance.
# Port of pddl-generators logistics/logistics.c, as called by Autoscale:
# `logistics -r {seed} -a {airplanes} -c {cities} -s {city_size} -p {packages} -t {cities}`.

from __future__ import annotations

import argparse
import random
import sys


def make_problem(
    num_cities: int,
    city_size: int,
    num_packages: int,
    num_airplanes: int,
    num_trucks: int | None = None,
    seed: int | None = None,
) -> str:
    """Generate a STRIPS Logistics task.

    Truck i < num_cities starts in city i, further trucks in random cities, all
    at random locations. Packages start and end at uniformly random locations
    (a goal may already hold, as upstream); airplanes start at random airports
    (location 0 of each city). ``num_trucks`` defaults to one per city.
    """
    if num_trucks is None:
        num_trucks = num_cities
    for name, value, minimum in (
        ("num_cities", num_cities, 1),
        ("city_size", city_size, 1),
        ("num_packages", num_packages, 1),
        ("num_airplanes", num_airplanes, 0),
        ("num_trucks", num_trucks, 1),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_trucks < num_cities:
        raise ValueError("num_trucks must be at least num_cities")

    rng = random.Random(seed)

    def location(city: int | None = None) -> str:
        if city is None:
            city = rng.randrange(num_cities)
        return f"l{city}-{rng.randrange(city_size)}"

    truck_origins = [location(i if i < num_cities else None) for i in range(num_trucks)]
    package_origins = [location() for _ in range(num_packages)]
    package_destinations = [location() for _ in range(num_packages)]
    airplane_origins = [f"l{rng.randrange(num_cities)}-0" for _ in range(num_airplanes)]

    locations = [f"l{c}-{l}" for c in range(num_cities) for l in range(city_size)]
    init_facts = [
        *(f"    (AIRPLANE a{i})" for i in range(num_airplanes)),
        *(f"    (CITY c{i})" for i in range(num_cities)),
        *(f"    (TRUCK t{i})" for i in range(num_trucks)),
    ]
    for c in range(num_cities):
        for l in range(city_size):
            init_facts.append(f"    (LOCATION l{c}-{l})")
            init_facts.append(f"    (in-city l{c}-{l} c{c})")
    init_facts.extend(f"    (AIRPORT l{i}-0)" for i in range(num_cities))
    init_facts.extend(f"    (OBJ p{i})" for i in range(num_packages))
    init_facts.extend(f"    (at t{i} {origin})" for i, origin in enumerate(truck_origins))
    init_facts.extend(f"    (at p{i} {origin})" for i, origin in enumerate(package_origins))
    init_facts.extend(f"    (at a{i} {origin})" for i, origin in enumerate(airplane_origins))
    goals = [f"        (at p{i} {destination})" for i, destination in enumerate(package_destinations)]

    return (f"""(define (problem logistics-c{num_cities}-s{city_size}-p{num_packages}-a{num_airplanes}-t{num_trucks})
(:domain logistics-strips)
(:objects {" ".join([*(f"a{i}" for i in range(num_airplanes)), *(f"c{i}" for i in range(num_cities)), *(f"t{i}" for i in range(num_trucks)), *locations, *(f"p{i}" for i in range(num_packages))])}
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
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a STRIPS Logistics PDDL problem (Autoscale generator).")
    parser.add_argument("-c", "--num-cities", type=int, required=True)
    parser.add_argument("-s", "--city-size", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-a", "--num-airplanes", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, help="default: one per city")
    parser.add_argument("-r", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
