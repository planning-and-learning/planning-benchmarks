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
# Two styles, following the IPC tasks in downward-benchmarks:
#   "98": logistics98 (AIPS-1998) structure and encoding (`obj`, domain.pddl).
#   "00": logistics00 (AIPS-2000 track 1) structure and encoding (`package`,
#         domain_logistics00.pddl): two locations per city, one truck per city.

from __future__ import annotations

import argparse
import random
import sys
import time

STYLES = ("98", "00")


def make_problem(
    num_cities: int,
    city_size: int,
    num_packages: int,
    num_airplanes: int,
    seed: int | None = None,
    num_trucks: int | None = None,
    num_goals: int | None = None,
    style: str = "98",
) -> str:
    """Generate a Logistics task.

    "98": truck i < num_cities starts in city i, further trucks in uniformly
    random cities, each at a uniformly random location of its city. Packages
    start and end at uniformly random locations (a goal may already hold);
    airplanes start at random airports (they may share one). ``num_goals``
    random packages get a goal (default: all). Airport of city c is its last
    location, as in the IPC tasks.

    "00": ``city_size`` must be 2 (pos, apt) and there is one truck per city
    at its pos. Packages are assigned to cities round-robin and start at the
    city's pos. Goals and airplanes as in "98".
    """
    if style not in STYLES:
        raise ValueError(f"style must be one of {STYLES}")
    if num_trucks is None:
        num_trucks = num_cities
    if num_goals is None:
        num_goals = num_packages
    checks: list[tuple[str, object, int]] = [
        ("num_cities", num_cities, 1),
        ("city_size", city_size, 1),
        ("num_packages", num_packages, 1),
        ("num_airplanes", num_airplanes, 1),
        ("num_trucks", num_trucks, num_cities),
        ("num_goals", num_goals, 0),
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_goals > num_packages:
        raise ValueError("num_goals must be at most num_packages")
    if style == "00" and (city_size != 2 or num_trucks != num_cities):
        raise ValueError("style 00 needs city_size 2 and one truck per city")

    rng = random.Random(seed if seed is not None else int(time.time()))
    cities = range(1, num_cities + 1)

    if style == "98":
        locations = {c: [f"city{c}-{l}" for l in range(1, city_size + 1)] for c in cities}
        airport = {c: locations[c][-1] for c in cities}
        truck_cities = [*cities, *(rng.choice(cities) for _ in range(num_trucks - num_cities))]
        trucks = [f"truck{t}" for t in range(1, num_trucks + 1)]
        truck_at = [rng.choice(locations[c]) for c in truck_cities]
        packages = [f"package{p}" for p in range(1, num_packages + 1)]
        all_locations = [loc for c in cities for loc in locations[c]]
        package_at = [rng.choice(all_locations) for _ in packages]
        planes = [f"plane{a}" for a in range(1, num_airplanes + 1)]
        package_type, city_name, domain = "obj", "city{}".format, "logistics-strips"
    else:
        locations = {c: [f"pos{c}", f"apt{c}"] for c in cities}
        airport = {c: f"apt{c}" for c in cities}
        trucks = [f"tru{c}" for c in cities]
        truck_at = [f"pos{c}" for c in cities]
        package_cities = [p % num_cities + 1 for p in range(num_packages)]
        packages = [f"obj{c}{p // num_cities + 1}" for p, c in enumerate(package_cities)]
        package_at = [f"pos{c}" for c in package_cities]
        all_locations = [loc for c in cities for loc in locations[c]]
        planes = [f"apn{a}" for a in range(1, num_airplanes + 1)]
        package_type, city_name, domain = "package", "cit{}".format, "logistics"

    plane_at = [airport[rng.choice(cities)] for _ in planes]
    goal_packages = sorted(rng.sample(range(num_packages), num_goals))
    goals = [f"      (at {packages[p]} {rng.choice(all_locations)})" for p in goal_packages]

    init_facts = [
        *(f"    ({package_type} {p})" for p in packages),
        *(f"    (city {city_name(c)})" for c in cities),
        *(f"    (truck {t})" for t in trucks),
        *(f"    (airplane {a})" for a in planes),
        *(f"    (location {loc})" for loc in all_locations),
        *(f"    (airport {airport[c]})" for c in cities),
        *(f"    (in-city {loc} {city_name(c)})" for c in cities for loc in locations[c]),
        *(f"    (at {a} {loc})" for a, loc in zip(planes, plane_at)),
        *(f"    (at {t} {loc})" for t, loc in zip(trucks, truck_at)),
        *(f"    (at {p} {loc})" for p, loc in zip(packages, package_at)),
    ]
    objects = [*packages, *(city_name(c) for c in cities), *trucks, *planes, *all_locations]

    name = f"logistics{style}-c{num_cities}-s{city_size}-p{num_packages}-a{num_airplanes}-t{num_trucks}-g{num_goals}"
    return (f"""(define (problem {name})
  (:domain {domain})
  (:objects {" ".join(objects)})
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
    parser = argparse.ArgumentParser(description="Generate a Logistics PDDL problem.")
    parser.add_argument("num_cities", type=int, help="number of cities")
    parser.add_argument("city_size", type=int, help="locations per city (style 00: 2)")
    parser.add_argument("num_packages", type=int, help="number of packages")
    parser.add_argument("num_airplanes", type=int, help="number of airplanes")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    parser.add_argument("-t", "--num-trucks", type=int, help="number of trucks (default: one per city)")
    parser.add_argument("-g", "--num-goals", type=int, help="packages with a goal (default: all)")
    parser.add_argument("--style", choices=STYLES, default="98", help="IPC 1998 or 2000 structure and encoding")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
