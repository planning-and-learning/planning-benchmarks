#!/usr/bin/env python3
"""Visitall on a full rectangular grid (both sides at least 2), visiting every cell.

The start is a random cell, restricted to the majority colour of the chessboard
colouring (cells with x + y even) when the cell count is odd. From such a start a
Hamiltonian path exists (Itai, Papadimitriou and Szwarcfiter 1982), so the optimal
cost is the lower bound of one move per unvisited cell: width * height - 1.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(width: int, height: int, seed: int | None = None) -> str:
    if width < 2 or height < 2:
        raise ValueError("width and height must be at least 2")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for y in range(height) for x in range(width)]
    start = rng.choice([(x, y) for x, y in cells if (width * height) % 2 == 0 or (x + y) % 2 == 0])

    def name(x: int, y: int) -> str:
        return f"loc-x{x}-y{y}"

    connections = [
        f"(connected {name(x, y)} {name(nx, ny)})"
        for x, y in cells
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        if 0 <= nx < width and 0 <= ny < height
    ]
    return f"""; optimal plan cost: {width * height - 1}
(define (problem visitall-full-grid-{width}x{height})
  (:domain grid-visit-all)
  (:objects {' '.join(name(*cell) for cell in cells)} - place)
  (:init
    (at-robot {name(*start)})
    (visited {name(*start)})
{chr(10).join(f'    {fact}' for fact in connections)}
  )
  (:goal
    (and
{chr(10).join(f'      (visited {name(*cell)})' for cell in cells)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a full-grid Visitall task.")
    parser.add_argument("-x", "--width", type=int, required=True)
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
