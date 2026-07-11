#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys


def make_problem(num_balls: int) -> str:
    balls = [f"ball{i}" for i in range(1, num_balls + 1)]
    objects = " ".join(["left", "right", *balls])
    ball_facts = "\n".join(f"    (ball {ball})" for ball in balls)
    initial_positions = "\n".join(f"    (at {ball} rooma)" for ball in balls)
    goals = "\n".join(f"      (at {ball} roomb)" for ball in balls)

    return f"""(define (problem gripper-{num_balls})
  (:domain gripper-strips)
  (:objects {objects})
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
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Gripper PDDL problem.")
    parser.add_argument("num_balls", type=int, help="number of balls")
    args = parser.parse_args(argv)

    if args.num_balls < 1:
        parser.error("num_balls must be at least 1")

    print(make_problem(args.num_balls), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
