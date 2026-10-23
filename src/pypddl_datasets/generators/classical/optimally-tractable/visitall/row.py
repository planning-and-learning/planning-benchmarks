#!/usr/bin/env python3
"""Visitall on a single row of cells, starting at a random cell.

Optimal cost: walk to the nearer end first, then to the other end:
(n - 1) + min(start, n - 1 - start).
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_cells: int, seed: int | None = None) -> str:
    if num_cells < 2:
        raise ValueError("num_cells must be at least 2")
    rng = random.Random(seed if seed is not None else int(time.time()))
    start = rng.randrange(num_cells)
    cells = [f"loc-x{x}-y0" for x in range(num_cells)]
    connections = [f"(connected {a} {b})\n    (connected {b} {a})" for a, b in zip(cells, cells[1:])]
    return f"""; optimal plan cost: {num_cells - 1 + min(start, num_cells - 1 - start)}
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
{chr(10).join(f'      (visited {cell})' for cell in cells)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a one-row Visitall task.")
    parser.add_argument("-n", "--num-cells", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_cells, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
