#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators miconic-fulladl/miconic.c (FF domain collection). Distributed
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
import sys

from pypddl_datasets.generators.classical.ipc.miconic_fulladl.generator import make_problem as make_ipc_problem


def make_problem(
    num_floors: int,
    num_passengers: int,
    seed: int | None = None,
    up_down: int = 20,
    vip: int = 5,
    going_nonstop: int = 5,
    attendant: int = 60,
    never_alone: int = 10,
    conflict_a: int = 20,
    conflict_b: int = 80,
    no_access: int = 50,
    no_access_floors: int = 5,
) -> str:
    """Generate the IPC distribution with the atomic goal ``(goal_satisfied)``."""
    problem = make_ipc_problem(
        num_floors, num_passengers, seed, up_down, vip, going_nonstop, attendant,
        never_alone, conflict_a, conflict_b, no_access, no_access_floors,
    )
    return problem.replace("(:domain miconic)", "(:domain miconic-fulladl-goal)").replace(
        "(:goal (forall (?p - passenger) (served ?p)))", "(:goal (goal_satisfied))"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Miconic-ADL problem with a derived goal predicate.")
    parser.add_argument("-f", "--num-floors", type=int, required=True)
    parser.add_argument("-p", "--num-passengers", type=int, required=True)
    for flag, dest, default in (("-u", "up_down", 20), ("-v", "vip", 5), ("-g", "going_nonstop", 5),
                                ("-a", "attendant", 60), ("-n", "never_alone", 10), ("-A", "conflict_a", 20),
                                ("-B", "conflict_b", 80), ("-N", "no_access", 50), ("-F", "no_access_floors", 5)):
        parser.add_argument(flag, dest=dest, type=int, default=default)
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
