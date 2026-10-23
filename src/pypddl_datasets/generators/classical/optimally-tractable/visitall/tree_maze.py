#!/usr/bin/env python3
"""Visitall in a maze whose passages form a random spanning tree of the grid.

Visiting every vertex of a tree with an open walk traverses every edge twice except
those on the path to where the walk ends, so the optimal cost is
2 * (cells - 1) - (largest tree distance from the start), ending at the farthest cell.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

Cell = tuple[int, int]


def make_problem(width: int, height: int, seed: int | None = None) -> str:
    if width < 1 or height < 1 or width * height < 2:
        raise ValueError("width and height must be at least 1 with at least 2 cells")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for y in range(height) for x in range(width)]

    def neighbours(cell: Cell) -> list[Cell]:
        x, y = cell
        candidates = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        return [(nx, ny) for nx, ny in candidates if 0 <= nx < width and 0 <= ny < height]

    # randomized Prim: grow the tree from a random cell
    tree: dict[Cell, list[Cell]] = {rng.choice(cells): []}
    while len(tree) < len(cells):
        cell, nxt = rng.choice([(cell, n) for cell in tree for n in neighbours(cell) if n not in tree])
        tree[cell].append(nxt)
        tree[nxt] = [cell]
    start = rng.choice(cells)
    depth = {start: 0}
    frontier = [start]
    while frontier:
        cell = frontier.pop()
        for n in tree[cell]:
            if n not in depth:
                depth[n] = depth[cell] + 1
                frontier.append(n)
    cost = 2 * (len(cells) - 1) - max(depth.values())

    def name(cell: Cell) -> str:
        return f"loc-x{cell[0]}-y{cell[1]}"

    connections = [f"(connected {name(cell)} {name(n)})" for cell in cells for n in tree[cell]]
    return f"""; optimal plan cost: {cost}
(define (problem visitall-tree-maze-{width}x{height})
  (:domain grid-visit-all)
  (:objects {' '.join(name(cell) for cell in cells)} - place)
  (:init
    (at-robot {name(start)})
    (visited {name(start)})
{chr(10).join(f'    {fact}' for fact in connections)}
  )
  (:goal
    (and
{chr(10).join(f'      (visited {name(cell)})' for cell in cells)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a tree-maze Visitall task.")
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
