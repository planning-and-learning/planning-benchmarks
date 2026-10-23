#!/usr/bin/env python3
"""Grid with one key to deliver, locks that this key opens, and locks no key opens (walls).

Without the key the robot cannot open anything, so it walks to the key through open
cells only. Carrying the key, entering a lock cell costs an unlock and a move, and an
opened lock stays open. Optimal cost: BFS(robot, key) + 1 + Dijkstra(key, goal) + 1,
where lock cells cost 2 on the second leg.
"""

from __future__ import annotations

import argparse
import heapq
import random
import sys
import time

Cell = tuple[int, int]


def make_problem(
    width: int, height: int, wall_ratio: float = 0.15, lock_ratio: float = 0.2, seed: int | None = None
) -> str:
    if width < 1 or height < 1 or width * height < 3:
        raise ValueError("width and height must be at least 1 with at least 3 cells")
    if not (0 <= wall_ratio and 0 <= lock_ratio and wall_ratio + lock_ratio < 1):
        raise ValueError("wall_ratio and lock_ratio must be non-negative with sum below 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for y in range(height) for x in range(width)]

    def neighbours(cell: Cell) -> list[Cell]:
        x, y = cell
        candidates = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        return [(nx, ny) for nx, ny in candidates if 0 <= nx < width and 0 <= ny < height]

    def distances(source: Cell, step: dict[Cell, int]) -> dict[Cell, int]:
        """Dijkstra where entering a cell costs step[cell]; cells missing from step are blocked."""
        found: dict[Cell, int] = {}
        queue = [(0, source)]
        while queue:
            distance, cell = heapq.heappop(queue)
            if cell in found:
                continue
            found[cell] = distance
            for n in neighbours(cell):
                if n in step and n not in found:
                    heapq.heappush(queue, (distance + step[n], n))
        return found

    while True:
        kinds = {cell: rng.choices(("wall", "lock", "open"), (wall_ratio, lock_ratio, 1 - wall_ratio - lock_ratio))[0]
                 for cell in cells}
        open_cells = sorted(cell for cell, kind in kinds.items() if kind == "open")
        if len(open_cells) < 3:
            continue
        robot, key, goal = rng.sample(open_cells, 3)
        to_key = distances(robot, {cell: 1 for cell in open_cells})
        to_goal = distances(key, {cell: 1 if kind == "open" else 2 for cell, kind in kinds.items() if kind != "wall"})
        if key in to_key and goal in to_goal:
            break
    cost = to_key[key] + 1 + to_goal[goal] + 1

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
        *(f"(open {name(cell)})" for cell in open_cells),
        *(
            f"(locked {name(cell)})\n    (lock-shape {name(cell)} {'circle' if kind == 'lock' else 'wall'})"
            for cell, kind in sorted(kinds.items())
            if kind != "open"
        ),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem grid-single-key-locks-{width}x{height})
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
    parser = argparse.ArgumentParser(description="Generate a Grid task with one key and locks it opens.")
    parser.add_argument("-x", "--width", type=int, required=True)
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-w", "--wall-ratio", type=float, default=0.15)
    parser.add_argument("-l", "--lock-ratio", type=float, default=0.2)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.wall_ratio, args.lock_ratio, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
