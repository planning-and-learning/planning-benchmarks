#!/usr/bin/env python3
"""Gripper with balls scattered over both rooms and a random goal room per ball.

With a balls to carry from rooma to roomb and b balls the other way, each needs one
pick and one drop. A move in either direction carries at most two balls, so the
robot needs x = ceil(a/2) moves to roomb and y = ceil(b/2) moves to rooma. The moves
alternate, so starting in rooma it needs max(2x - 1, 2y, 0) moves (symmetric when
starting in roomb), and full grippers on every needed crossing achieve this.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_balls: int, seed: int | None = None) -> str:
    if num_balls < 1:
        raise ValueError("num_balls must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    balls = [f"ball{i}" for i in range(1, num_balls + 1)]
    starts = [rng.choice(("rooma", "roomb")) for _ in balls]
    goals = [rng.choice(("rooma", "roomb")) for _ in balls]
    robot = rng.choice(("rooma", "roomb"))
    away = sum(start == robot != goal for start, goal in zip(starts, goals))
    back = sum(start != robot == goal for start, goal in zip(starts, goals))
    moves = max(2 * ((away + 1) // 2) - 1, 2 * ((back + 1) // 2), 0)
    cost = 2 * (away + back) + moves
    return f"""; optimal plan cost: {cost}
(define (problem gripper-two-way-{num_balls})
  (:domain gripper-strips)
  (:objects rooma roomb left right {" ".join(balls)})
  (:init
    (room rooma)
    (room roomb)
    (gripper left)
    (gripper right)
    (free left)
    (free right)
    (at-robby {robot})
{chr(10).join(f"    (ball {ball})" for ball in balls)}
{chr(10).join(f"    (at {ball} {start})" for ball, start in zip(balls, starts))}
  )
  (:goal
    (and
{chr(10).join(f"      (at {ball} {goal})" for ball, goal in zip(balls, goals))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a two-way Gripper task.")
    parser.add_argument("-n", "--num-balls", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_balls, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
