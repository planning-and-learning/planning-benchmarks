#!/usr/bin/env python3
"""Ricochet Robots with a single robot on a random board with barriers.

Other robots are what make Ricochet Robots hard: they serve as movable blockers.
Alone, the robot's position is the whole state, so a breadth-first search over the
board's cells gives the fewest moves (each move costs go-cost 1; steps and stops are
free).
"""

from __future__ import annotations

import argparse
import random
import sys
import time

from pypddl_datasets.generators.classical.ipc.ricochet_robots import generator as _ipc


def make_problem(board_size: int, num_barriers: int, seed: int | None = None) -> str:
    if board_size < 2:
        raise ValueError("board_size must be at least 2")
    if not 0 <= num_barriers <= 2 * board_size * (board_size - 1):
        raise ValueError("num_barriers must be between 0 and the number of interior walls")
    rng = random.Random(seed if seed is not None else int(time.time()))
    n = board_size
    walls = [
        (x, y, d)
        for x in range(1, n + 1)
        for y in range(1, n + 1)
        for d, (dx, dy) in (("east", (1, 0)), ("south", (0, 1)))
        if x + dx <= n and y + dy <= n
    ]
    while True:
        barriers = rng.sample(walls, num_barriers)
        blocked = [(x, 1, "north") for x in range(1, n + 1)] + [(x, n, "south") for x in range(1, n + 1)]
        blocked += [(1, y, "west") for y in range(1, n + 1)] + [(n, y, "east") for y in range(1, n + 1)]
        for x, y, d in barriers:
            dx, dy = _ipc.MOVES[d]
            blocked += [(x, y, d), (x + dx, y + dy, _ipc.OPPOSITE[d])]
        robot, target = rng.sample([(x, y) for x in range(1, n + 1) for y in range(1, n + 1)], 2)
        cost = _ipc.optimal_moves(n, set(blocked), [robot], 0, target, n * n + 1)
        if cost is not None and cost > 0:
            break

    cells = [f"cell-{x}-{y}" for x in range(1, n + 1) for y in range(1, n + 1)]
    init = [
        *(f"(next cell-{x}-{y} cell-{x}-{y + 1} south)" for x in range(1, n + 1) for y in range(1, n)),
        *(f"(next cell-{x}-{y} cell-{x}-{y - 1} north)" for x in range(1, n + 1) for y in range(2, n + 1)),
        *(f"(next cell-{x}-{y} cell-{x + 1}-{y} east)" for y in range(1, n + 1) for x in range(1, n)),
        *(f"(next cell-{x}-{y} cell-{x - 1}-{y} west)" for y in range(1, n + 1) for x in range(2, n + 1)),
        *(f"(blocked cell-{x}-{y} {d})" for x, y, d in sorted(set(blocked))),
        *(f"(free {cell})" for cell in cells if cell != f"cell-{robot[0]}-{robot[1]}"),
        f"(at robot-1 cell-{robot[0]}-{robot[1]})",
        "(nothing-is-moving)",
        "(= (total-cost) 0)",
        "(= (go-cost) 1)",
        "(= (step-cost) 0)",
        "(= (stop-cost) 0)",
    ]
    return f"""; optimal plan cost: {cost}
(define (problem ricochet-robots-single-robot-{n}x{n})
  (:domain ricochet-robots)
  (:objects
    {' '.join(cells)} - cell
    robot-1 - robot
    west east north south - direction
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
      (at robot-1 cell-{target[0]}-{target[1]})
      (nothing-is-moving)
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a single-robot Ricochet Robots task.")
    parser.add_argument("-n", "--board-size", type=int, required=True)
    parser.add_argument("-b", "--num-barriers", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.board_size, args.num_barriers, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
