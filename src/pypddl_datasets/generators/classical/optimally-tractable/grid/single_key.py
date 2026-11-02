#!/usr/bin/env python3
"""Grid as generated for the IPC with one key whose shape no lock has, so every locked cell is a wall.

The map is drawn as by the IPC generator (ipc/grid): num_locks cells (default a quarter
of the grid) form one connected locked region grown from a random cell, the robot
starts on a random open cell, the key lies on a random open cell the robot can reach
and the goal is a random cell. Here no key opens the locks, so the goal is a random
cell of the robot's open region (any other cell is out of reach); as in the IPC it may
be the key's own cell.

Without usable locks the robot only walks, picks up and puts down. Optimal cost:
dist(robot, key) + 1 + dist(key, goal) + 1 with breadth-first distances around the
walls (0 if the key already lies on the goal).
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from collections import deque

from pypddl_datasets.generators.classical.ipc.grid.generator import grow_region

Cell = tuple[int, int]


def make_problem(width: int, height: int, num_locks: int | None = None, seed: int | None = None) -> str:
    if width < 2 or height < 2:
        raise ValueError("width and height must be at least 2")
    if num_locks is None:
        num_locks = width * height // 4
    if not 1 <= num_locks < width * height:
        raise ValueError("num_locks must be at least 1 and leave an open cell")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for x in range(width) for y in range(height)]

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

    walls = set(grow_region(cells, num_locks, rng))
    robot = rng.choice([cell for cell in cells if cell not in walls])
    from_robot = distances(robot, walls)
    reachable = sorted(from_robot)
    key = rng.choice(reachable)
    goal = rng.choice(reachable)
    cost = 0 if goal == key else from_robot[key] + 1 + distances(key, walls)[goal] + 1

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
    parser = argparse.ArgumentParser(description="Generate a Grid task with one key and walls only.")
    parser.add_argument("-x", "--width", type=int, required=True)
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-l", "--num-locks", type=int, help="locked (wall) cells, default: a quarter of the grid")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.num_locks, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
