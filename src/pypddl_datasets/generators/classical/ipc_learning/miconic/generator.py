#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators miconic/miconic.c (FF domain collection). Distributed
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

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_floors: int, num_passengers: int, seed: int | None = None, lift_start: str = "random") -> str:
    """``lift_start="random"`` (learning track) or ``"bottom"`` (lift at f0, the original)."""
    if lift_start not in ("random", "bottom"):
        raise ValueError("lift_start must be 'random' or 'bottom'")
    rng = random.Random(seed if seed is not None else int(time.time()))

    floors = [f"f{i}" for i in range(num_floors)]
    passengers = [f"p{i}" for i in range(num_passengers)]

    init_facts = [
        f"    (above f{i} f{j})"
        for i in range(num_floors - 1)
        for j in range(i + 1, num_floors)
    ]
    for passenger in passengers:
        origin = rng.randrange(num_floors)
        destin = origin
        while num_floors > 1 and destin == origin:
            destin = rng.randrange(num_floors)
        init_facts.append(f"    (origin {passenger} f{origin})")
        init_facts.append(f"    (destin {passenger} f{destin})")
    init_facts.append(f"    (lift-at f{rng.randrange(num_floors) if lift_start == 'random' else 0})")

    goals = [f"      (served {passenger})" for passenger in passengers]

    return f"""(define (problem miconic-f{num_floors}-p{num_passengers})
  (:domain miconic)
  (:objects
    {" ".join(passengers)} - passenger
    {" ".join(floors)} - floor
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
    parser = argparse.ArgumentParser(description="Generate a Miconic PDDL problem.")
    parser.add_argument("num_floors", type=int, help="number of floors")
    parser.add_argument("num_passengers", type=int, help="number of passengers")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    parser.add_argument("--lift-start", choices=("random", "bottom"), default="random", help="lift start floor (default: random)")
    args = parser.parse_args(argv)

    if args.num_floors < 1:
        parser.error("num_floors must be at least 1")
    if args.num_passengers < 1:
        parser.error("num_passengers must be at least 1")

    print(make_problem(args.num_floors, args.num_passengers, args.seed, args.lift_start), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
