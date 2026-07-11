#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(
    width: int,
    height: int | None = None,
    goal_ratio: float = 1.0,
    num_unavailable: int = 0,
    seed: int | None = None,
) -> str:
    height = width if height is None else height
    rng = random.Random(seed if seed is not None else int(time.time()))
    area = width * height

    protected = (width + 1) * height // 2
    candidates = [cell for cell in range(area) if cell != protected]
    unavailable = set(rng.sample(candidates, num_unavailable))
    locations = [
        (x, y)
        for x in range(width)
        for y in range(height)
        if x * height + y not in unavailable
    ]
    initial = rng.choice(locations)

    connections = []
    for x, y in locations:
        for next_x, next_y in (
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ):
            if (next_x, next_y) in locations:
                connections.append(
                    f"(connected loc-x{x}-y{y} loc-x{next_x}-y{next_y})"
                )

    goals = []
    for x, y in locations:
        selected = rng.randrange(area) < goal_ratio * area
        if selected or (x, y) == initial:
            goals.append(f"(visited loc-x{x}-y{y})")

    problem_name = (
        f"grid-{width}"
        if width == height
        else f"grid-{width}x{height}"
    )
    objects = "\n".join(
        f"    loc-x{x}-y{y}" for x, y in locations
    )
    init = "\n".join(
        (
            f"    (at-robot loc-x{initial[0]}-y{initial[1]})",
            f"    (visited loc-x{initial[0]}-y{initial[1]})",
            *(f"    {fact}" for fact in connections),
        )
    )
    goal = "\n".join(f"      {fact}" for fact in goals)

    return f"""(define (problem {problem_name})
  (:domain grid-visit-all)
  (:objects
{objects}
    - place
  )
  (:init
{init}
  )
  (:goal
    (and
{goal}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="generate a visitall pddl problem.")
    dimensions = parser.add_mutually_exclusive_group(required=True)
    dimensions.add_argument("-n", "--size", type=int, help="square grid size")
    dimensions.add_argument("-x", "--width", type=int, help="grid width")
    parser.add_argument("-y", "--height", type=int, help="grid height")
    parser.add_argument(
        "-r",
        "--goal-ratio",
        type=float,
        default=1.0,
        help="ratio of available cells required in the goal",
    )
    parser.add_argument(
        "-u",
        "--num-unavailable",
        type=int,
        default=0,
        help="number of unavailable cells",
    )
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.size is not None:
        if args.height is not None:
            parser.error("--height cannot be combined with --size")
        width = height = args.size
    else:
        if args.height is None:
            parser.error("--height is required with --width")
        width, height = args.width, args.height

    if width < 1 or height < 1:
        parser.error("grid dimensions must be at least 1")
    if not 0.0 <= args.goal_ratio <= 1.0:
        parser.error("--goal-ratio must be between 0 and 1")
    if not 0 <= args.num_unavailable < width * height:
        parser.error(
            "--num-unavailable must be non-negative and smaller than the grid"
        )

    print(
        make_problem(
            width,
            height,
            args.goal_ratio,
            args.num_unavailable,
            args.seed,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
