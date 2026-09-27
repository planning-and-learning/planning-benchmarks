#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators mprime/mprime.c (FF domain collection). Distributed
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
"""Typed Mprime with speaking names, as in the Autoscale 21.11 tasks (`mprime -l -f -s -v -c`)."""

from __future__ import annotations

import argparse
import random
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    num_locations: int,
    max_fuel: int,
    max_space: int,
    num_vehicles: int,
    num_cargos: int,
    seed: int | None = None,
) -> str:
    """Generate a typed Mprime task.

    Locations form a ring. Every location gets fuel uniform in 0..max_fuel, every
    vehicle space uniform in 1..max_space; vehicles and cargos start at uniform
    locations and every cargo has a uniform destination (possibly its start).
    """
    for name, value, minimum in (
        ("num_locations", num_locations, 2),
        ("max_fuel", max_fuel, 1),
        ("max_space", max_space, 1),
        ("num_vehicles", num_vehicles, 1),
        ("num_cargos", num_cargos, 1),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    # upstream draw order: vehicle origins, cargo origins, cargo destinations, fuels, spaces
    vehicle_at = [rng.randrange(num_locations) for _ in range(num_vehicles)]
    cargo_at = [rng.randrange(num_locations) for _ in range(num_cargos)]
    cargo_to = [rng.randrange(num_locations) for _ in range(num_cargos)]
    fuel = [rng.randrange(max_fuel + 1) for _ in range(num_locations)]
    space = [rng.randrange(max_space) + 1 for _ in range(num_vehicles)]

    init = [f"(not-equal l{i} l{j})" for i in range(num_locations) for j in range(num_locations) if i != j]
    init += [f"(fuel-neighbor f{i} f{i + 1})" for i in range(max_fuel)]
    init += [f"(space-neighbor s{i} s{i + 1})" for i in range(max_space)]
    for i in range(num_locations - 1):
        init += [f"(conn l{i} l{i + 1})", f"(conn l{i + 1} l{i})"]
    init += [f"(conn l{num_locations - 1} l0)", f"(conn l0 l{num_locations - 1})"]
    init += [f"(has-fuel l{i} f{f})" for i, f in enumerate(fuel)]
    init += [f"(has-space v{i} s{s})" for i, s in enumerate(space)]
    init += [f"(at v{i} l{loc})" for i, loc in enumerate(vehicle_at)]
    init += [f"(at c{i} l{loc})" for i, loc in enumerate(cargo_at)]
    goal = [f"(at c{i} l{loc})" for i, loc in enumerate(cargo_to)]

    def names(prefix: str, count: int) -> str:
        return " ".join(f"{prefix}{i}" for i in range(count))

    return (f"""(define (problem strips-mprime-l{num_locations}-f{max_fuel}-s{max_space}-v{num_vehicles}-c{num_cargos})
(:domain mprime-strips)
(:objects {names("f", max_fuel + 1)} - fuel
          {names("s", max_space + 1)} - space
          {names("l", num_locations)} - location
          {names("v", num_vehicles)} - vehicle
          {names("c", num_cargos)} - cargo)
(:init
{chr(10).join(init)}
)
(:goal
(and
{chr(10).join(goal)}
)
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a typed Mprime PDDL problem (Autoscale 21.11 encoding).")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-f", "--max-fuel", type=int, required=True)
    parser.add_argument("-s", "--max-space", type=int, required=True)
    parser.add_argument("-v", "--num-vehicles", type=int, required=True)
    parser.add_argument("-c", "--num-cargos", type=int, required=True)
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
