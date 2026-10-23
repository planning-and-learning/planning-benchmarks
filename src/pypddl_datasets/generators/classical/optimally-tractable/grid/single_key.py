#!/usr/bin/env python3
"""Grid with one key to deliver and locks that no key opens (walls).

Without usable locks the robot only walks, picks up and puts down. Optimal cost:
dist(robot, key) + 1 + dist(key, goal) + 1, with breadth-first distances around the
walls.
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from collections import deque

Cell = tuple[int, int]


def make_problem(width: int, height: int, wall_ratio: float = 0.2, seed: int | None = None) -> str:
    if width < 1 or height < 1 or width * height < 2:
        raise ValueError("width and height must be at least 1 with at least 2 cells")
    if not 0 <= wall_ratio < 1:
        raise ValueError("wall_ratio must be in [0, 1)")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for y in range(height) for x in range(width)]

    def neighbours(cell: Cell) -> list[Cell]:
        x, y = cell
        candidates = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        return [(nx, ny) for nx, ny in candidates if 0 <= nx < width and 0 <= ny < height]

    def distances(source: Cell, walls: set[Cell]) -> dict[Cell, int]:
        found, frontier = {source: 0}, deque([source])
        while frontier:
            cell = frontier.popleft()
            for n in neighbours(cell):
                if n not in walls and n not in found:
                    found[n] = found[cell] + 1
                    frontier.append(n)
        return found

    reachable: dict[Cell, int] = {}
    walls: set[Cell] = set()
    while len(reachable) < 2:
        walls = {cell for cell in cells if rng.random() < wall_ratio}
        open_cells = [cell for cell in cells if cell not in walls]
        if len(open_cells) >= 2:
            reachable = distances(rng.choice(open_cells), walls)
    robot, key, goal = rng.choice(list(reachable)), *rng.sample(list(reachable), 2)
    cost = distances(robot, walls)[key] + 1 + distances(key, walls)[goal] + 1

    def name(cell: Cell) -> str:
        return f"pos-{cell[0]}-{cell[1]}"

    init = [
        "(arm-empty)",
        "(shape circle)",
        "(shape wall)",
        "(key key0)",
        "(key-shape key0 circle)",
        f"(at key0 {name(key)})",
        f"(at-robot {name(robot)})",
        *(f"(place {name(cell)})" for cell in cells),
        *(f"(conn {name(cell)} {name(n)})" for cell in cells for n in neighbours(cell)),
        *(f"(open {name(cell)})" for cell in cells if cell not in walls),
        *(f"(locked {name(cell)})\n    (lock-shape {name(cell)} wall)" for cell in sorted(walls)),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem grid-single-key-{width}x{height})
  (:domain grid)
  (:objects {' '.join(name(cell) for cell in cells)} circle wall key0)
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
      (at key0 {name(goal)})
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Grid task with one key and walls.")
    parser.add_argument("-x", "--width", type=int, required=True)
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-w", "--wall-ratio", type=float, default=0.2)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.wall_ratio, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
