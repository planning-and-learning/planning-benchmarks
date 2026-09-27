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


def make_problem(num_floors: int, num_passengers: int, seed: int | None = None, typed: bool = False) -> str:
    """Uniform origins, uniform destinations different from the origin, lift at f0.

    The default is the untyped IPC 2000 encoding with ``passenger``/``floor``
    type predicates; ``typed`` gives Autoscale's typed STRIPS encoding. The IPC
    tasks all use ``num_floors = 2 * num_passengers``.
    """
    for name, value, minimum in (("num_floors", num_floors, 2), ("num_passengers", num_passengers, 1)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    passengers = [f"p{i}" for i in range(num_passengers)]
    floors = [f"f{i}" for i in range(num_floors)]
    init_facts = [] if typed else [f"    (passenger {p})" for p in passengers] + [f"    (floor {f})" for f in floors]
    init_facts += [f"    (above f{i} f{j})" for i in range(num_floors - 1) for j in range(i + 1, num_floors)]
    for passenger in passengers:
        origin = rng.randrange(num_floors)
        destin = rng.randrange(num_floors)
        while destin == origin:
            destin = rng.randrange(num_floors)
        init_facts.append(f"    (origin {passenger} f{origin})")
        init_facts.append(f"    (destin {passenger} f{destin})")
    init_facts.append("    (lift-at f0)")
    goals = "\n".join(f"      (served {passenger})" for passenger in passengers)
    if typed:
        objects = f"    {' '.join(passengers)} - passenger\n    {' '.join(floors)} - floor"
    else:
        objects = f"    {' '.join(passengers)}\n    {' '.join(floors)}"

    return (f"""(define (problem mixed-f{num_floors}-p{num_passengers}-u0-v0-d0-a0-n0-A0-B0-N0-F0)
  (:domain miconic)
  (:objects
{objects}
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{goals}
    )
  )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Miconic PDDL problem.")
    parser.add_argument("-f", "--num-floors", type=int, required=True)
    parser.add_argument("-p", "--num-passengers", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--typed", action="store_true", help="typed encoding instead of type predicates")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_floors, args.num_passengers, args.seed, args.typed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
