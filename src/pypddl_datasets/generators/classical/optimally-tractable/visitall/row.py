#!/usr/bin/env python3
"""Visitall as generated for the IPC on a single row of cells (height 1).

The start is a random cell and, as in the IPC generator (ipc/visitall), each cell is a
goal with probability goal_ratio (default 1, every cell) and the start always is.
Optimal cost: walk to the nearer end of the goal span [L, R] first, then to the other:
(R - L) + min(start - L, R - start).
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_cells: int, goal_ratio: float = 1.0, seed: int | None = None) -> str:
    if num_cells < 1:
        raise ValueError("num_cells must be at least 1")
    if not 0 <= goal_ratio <= 1:
        raise ValueError("goal_ratio must be in [0, 1]")
    rng = random.Random(seed if seed is not None else int(time.time()))
    start = rng.randrange(num_cells)
    # the IPC's goal draw: each cell with probability goal_ratio, plus the start
    goals = [x for x in range(num_cells) if rng.randrange(num_cells) < goal_ratio * num_cells or x == start]
    left, right = goals[0], goals[-1]
    cells = [f"loc-x{x}-y0" for x in range(num_cells)]
    connections = [f"(connected {a} {b})\n    (connected {b} {a})" for a, b in zip(cells, cells[1:])]
    return f"""; optimal plan cost: {right - left + min(start - left, right - start)}
(define (problem visitall-row-{num_cells})
  (:domain grid-visit-all)
  (:objects {' '.join(cells)} - place)
  (:init
    (at-robot {cells[start]})
    (visited {cells[start]})
{chr(10).join(f'    {fact}' for fact in connections)}
  )
  (:goal
    (and
{chr(10).join(f'      (visited {cells[x]})' for x in goals)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Visitall task on a single row.")
    parser.add_argument("-n", "--num-cells", type=int, required=True)
    parser.add_argument("-r", "--goal-ratio", type=float, default=1.0, help="share of cells to visit (default: 1)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_cells, args.goal_ratio, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
