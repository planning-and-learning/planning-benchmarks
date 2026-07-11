#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time

SOFT = "soft"
HARD = "hard"
CLEAR = "clear"
ROBOT = "robot"
GOLD = "gold"
SUPPLY = "supply"


def loc(row: int, col: int) -> str:
    return f"f{row}-{col}f"


def make_problem(num_rows: int, num_cols: int, seed: int | None = None) -> str | None:
    if num_rows < 2 or num_cols < 3:
        return None

    rng = random.Random(seed if seed is not None else int(time.time()))
    grid = [[CLEAR for _ in range(num_cols)] for _ in range(num_rows)]

    robot_row = rng.randrange(num_rows)
    grid[robot_row][0] = ROBOT
    supply_row = rng.choice([row for row in range(num_rows) if grid[row][0] == CLEAR])
    grid[supply_row][0] = SUPPLY
    gold_row = rng.randrange(num_rows)
    grid[gold_row][num_cols - 1] = GOLD

    for row in range(num_rows):
        for col in range(1, num_cols):
            if grid[row][col] == CLEAR:
                grid[row][col] = SOFT if rng.randrange(2) == 0 else HARD

    current_row = gold_row
    current_col = num_cols - 1
    move = rng.randrange(3)
    while current_col > 1:
        if move == 0:
            steps = rng.randrange(current_row + 1) + 2
            while steps > 1 and current_row > 0:
                current_row -= 1
                grid[current_row][current_col] = SOFT
                steps -= 1
            move = 0 if rng.randrange(2) else 1
        elif move == 2:
            steps = rng.randrange(num_rows - current_row) + 2
            while steps > 1 and current_row < num_rows - 1:
                current_row += 1
                grid[current_row][current_col] = SOFT
                steps -= 1
            move = 2 if rng.randrange(2) else 1
        else:
            steps = 3
            while steps > 1 and current_col > 1:
                current_col -= 1
                grid[current_row][current_col] = SOFT
                steps -= 1
            move = rng.randrange(3)

    objects = [loc(row, col) for row in range(num_rows) for col in range(num_cols)]
    init_facts = ["    (arm-empty)"]
    for row in range(num_rows):
        for col in range(num_cols):
            here = loc(row, col)
            if col + 1 < num_cols:
                init_facts.append(f"    (connected {here} {loc(row, col + 1)})")
            if row + 1 < num_rows:
                init_facts.append(f"    (connected {here} {loc(row + 1, col)})")
            if col > 0:
                init_facts.append(f"    (connected {here} {loc(row, col - 1)})")
            if row > 0:
                init_facts.append(f"    (connected {here} {loc(row - 1, col)})")

    for row in range(num_rows):
        for col in range(num_cols):
            here = loc(row, col)
            value = grid[row][col]
            if value == ROBOT:
                init_facts.extend([f"    (robot-at {here})", f"    (clear {here})"])
            elif value == SUPPLY:
                init_facts.extend([f"    (bomb-at {here})", f"    (laser-at {here})", f"    (clear {here})"])
            elif value == GOLD:
                init_facts.extend([f"    (gold-at {here})", f"    (soft-rock-at {here})"])
            elif value == SOFT:
                init_facts.append(f"    (soft-rock-at {here})")
            elif value == HARD:
                init_facts.append(f"    (hard-rock-at {here})")
            else:
                init_facts.append(f"    (clear {here})")

    return f'''(define (problem goldminer-r{num_rows}-c{num_cols})
  (:domain gold-miner-typed)
  (:objects
    {' '.join(objects)} - LOC
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (holds-gold)
  )
)
'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Gold Miner PDDL problem.")
    parser.add_argument("num_rows", type=int)
    parser.add_argument("num_cols", type=int)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)

    problem = make_problem(args.num_rows, args.num_cols, args.seed)
    if problem is None:
        parser.error("expected num_rows >= 2 and num_cols >= 3")
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
