#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def tile(row: int, col: int) -> str:
    return f"tile_{row}-{col}"


def make_problem(
    num_rows: int,
    num_columns: int,
    num_robots: int,
    seed: int | None = None,
    name: str | None = None,
) -> str | None:
    if num_rows < 1 or num_columns < 1 or num_robots < 1 or num_robots > num_columns:
        return None

    rng = random.Random(seed if seed is not None else int(time.time()))
    problem_name = name or f"floortile-r{num_rows}-c{num_columns}-rob{num_robots}"

    tiles = [tile(row, col) for row in range(num_rows + 1) for col in range(1, num_columns + 1)]
    robots = [f"robot{i}" for i in range(1, num_robots + 1)]

    used_cols = list(range(1, num_columns + 1))
    robot_locations: dict[str, str] = {}
    init_facts = ["    (= (total-cost) 0)"]
    for index, robot in enumerate(robots):
        row = rng.randint(0, num_rows)
        col = rng.choice(used_cols)
        used_cols.remove(col)
        location = tile(row, col)
        robot_locations[robot] = location
        color = "white" if index % 2 == 0 else "black"
        init_facts.append(f"    (robot-at {robot} {location})")
        init_facts.append(f"    (robot-has {robot} {color})")

    init_facts.extend(["    (available-color white)", "    (available-color black)"])
    occupied = set(robot_locations.values())
    init_facts.extend(f"    (clear {t})" for t in tiles if t not in occupied)

    for row in range(num_rows):
        for col in range(1, num_columns + 1):
            init_facts.append(f"    (up {tile(row + 1, col)} {tile(row, col)})")
            init_facts.append(f"    (down {tile(row, col)} {tile(row + 1, col)})")
    for row in range(num_rows + 1):
        for col in range(1, num_columns):
            init_facts.append(f"    (right {tile(row, col + 1)} {tile(row, col)})")
            init_facts.append(f"    (left {tile(row, col)} {tile(row, col + 1)})")

    goals = []
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            color = "white" if (row - 1 + col - 1) % 2 == 0 else "black"
            goals.append(f"      (painted {tile(row, col)} {color})")

    tile_lines = []
    for row in range(num_rows + 1):
        row_tiles = " ".join(tile(row, col) for col in range(1, num_columns + 1))
        tile_lines.append(f"    {row_tiles}")

    return f'''(define (problem {problem_name})
  (:domain floor-tile)
  (:objects
{chr(10).join(tile_lines)} - tile
    {' '.join(robots)} - robot
    white black - color
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
  (:metric minimize (total-cost))
)
'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Floortile PDDL problem.")
    parser.add_argument("num_rows", type=int)
    parser.add_argument("num_columns", type=int)
    parser.add_argument("num_robots", type=int)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("-n", "--name")
    args = parser.parse_args(argv)

    problem = make_problem(args.num_rows, args.num_columns, args.num_robots, args.seed, args.name)
    if problem is None:
        parser.error("expected num_rows >= 1, num_columns >= 1, and 1 <= num_robots <= num_columns")
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
