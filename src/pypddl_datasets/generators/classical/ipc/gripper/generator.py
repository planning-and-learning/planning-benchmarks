#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators gripper/gripper.c (FF domain collection). Distributed
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
"""Port of pddl-generators gripper/gripper.c (``gripper -n N``) as used by Autoscale 21.11."""

from __future__ import annotations

import argparse
import sys


def make_problem(num_balls: int) -> str:
    """All balls start in rooma and must reach roomb; rooms are objects, not constants."""
    if not isinstance(num_balls, int) or isinstance(num_balls, bool) or num_balls < 1:
        raise ValueError("num_balls must be an integer at least 1")
    balls = [f"ball{i}" for i in range(1, num_balls + 1)]
    ball_facts = "\n".join(f"    (ball {ball})" for ball in balls)
    initial_positions = "\n".join(f"    (at {ball} rooma)" for ball in balls)
    goals = "\n".join(f"      (at {ball} roomb)" for ball in balls)

    return (f"""(define (problem gripper-{num_balls})
  (:domain gripper-strips)
  (:objects rooma roomb left right {" ".join(balls)})
  (:init
    (room rooma)
    (room roomb)
    (gripper left)
    (gripper right)
{ball_facts}
    (free left)
    (free right)
{initial_positions}
    (at-robby rooma)
  )
  (:goal
    (and
{goals}
    )
  )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an Autoscale/IPC Gripper PDDL problem.")
    parser.add_argument("-n", "--num-balls", type=int, required=True)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_balls)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
