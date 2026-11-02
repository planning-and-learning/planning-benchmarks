#!/usr/bin/env python3
"""Grid as generated for the IPC with one key, which opens every lock, plus optional walls.

The map is drawn as by the IPC generator (ipc/grid): num_locks cells (default a quarter
of the grid) form one connected locked region of one shape, grown from a random cell,
the robot starts on a random open cell and the key, of that shape, lies on a random
open cell the robot can reach. wall_ratio (default 0, the IPC) additionally turns that
share of the other cells into walls, locks of a shape no key has. The goal is a random
cell the key can reach through the locks, as in the IPC possibly the key's own cell.

Without the key the robot cannot open anything, so it walks to the key through open
cells only. Carrying the key, entering a lock cell costs an unlock and a move, and an
opened lock stays open. Optimal cost: BFS(robot, key) + 1 + Dijkstra(key, goal) + 1,
where lock cells cost 2 on the second leg (0 if the key already lies on the goal).
"""

from __future__ import annotations

import argparse
import heapq
import random
import sys
import time

from pypddl_datasets.generators.classical.ipc.grid.generator import grow_region

Cell = tuple[int, int]


def make_problem(
    width: int, height: int, num_locks: int | None = None, wall_ratio: float = 0.0, seed: int | None = None
) -> str:
    if width < 2 or height < 2:
        raise ValueError("width and height must be at least 2")
    if num_locks is None:
        num_locks = width * height // 4
    if not 1 <= num_locks < width * height:
        raise ValueError("num_locks must be at least 1 and leave an open cell")
    if not 0 <= wall_ratio < 1:
        raise ValueError("wall_ratio must be in [0, 1)")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for x in range(width) for y in range(height)]

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
        locks = set(grow_region(cells, num_locks, rng))
        walls = {cell for cell in cells if cell not in locks and rng.random() < wall_ratio}
        open_cells = [cell for cell in cells if cell not in locks and cell not in walls]
        if open_cells:
            break
    robot = rng.choice(open_cells)
    to_key = distances(robot, {cell: 1 for cell in open_cells})
    key = rng.choice(sorted(to_key))
    to_goal = distances(key, {cell: 2 if cell in locks else 1 for cell in cells if cell not in walls})
    goal = rng.choice(sorted(to_goal))
    cost = 0 if goal == key else to_key[key] + 1 + to_goal[goal] + 1

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
        *(f"(locked {name(cell)})\n    (lock-shape {name(cell)} circle)" for cell in sorted(locks)),
        *(f"(locked {name(cell)})\n    (lock-shape {name(cell)} wall)" for cell in sorted(walls)),
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
    parser = argparse.ArgumentParser(description="Generate a Grid task with one key that opens every lock.")
    parser.add_argument("-x", "--width", type=int, required=True)
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-l", "--num-locks", type=int, help="locked cells the key opens (default: cells / 4)")
    parser.add_argument("-w", "--wall-ratio", type=float, default=0.0, help="share of the other cells that are walls")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.num_locks, args.wall_ratio, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
