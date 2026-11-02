#!/usr/bin/env python3
"""Ricochet Robots with a single robot on a random board with barriers.

Barriers are drawn as by the IPC generator (ipc/ricochet_robots): num_barriers random
walls between neighbouring cells, by default uniform in 5..5 + size^2 / 3 as upstream;
board="asp2015" is the fixed 16x16 board of the ASP competition with the robot in one
of its four corners.

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


def make_problem(
    board_size: int, num_barriers: int | None = None, seed: int | None = None, board: str = "random"
) -> str:
    if board not in _ipc.BOARDS:
        raise ValueError(f"board must be one of {', '.join(_ipc.BOARDS)}")
    if board == "asp2015" and (board_size != 16 or num_barriers is not None):
        raise ValueError("board='asp2015' is a fixed 16x16 board: use board_size=16 and no num_barriers")
    if board_size < 3:
        raise ValueError("board_size must be at least 3")
    max_barriers = 2 * board_size * (board_size - 1)  # interior walls
    if num_barriers is not None and not 0 <= num_barriers <= max_barriers:
        raise ValueError(f"num_barriers must be between 0 and {max_barriers}, the number of interior walls")
    rng = random.Random(seed if seed is not None else int(time.time()))
    n = board_size
    for _ in range(_ipc.MAX_TRIES):
        if board == "asp2015":
            barriers = list(_ipc.ASP_2015_BARRIERS)
        else:
            count = num_barriers if num_barriers is not None else min(rng.randint(5, 5 + n * n // 3), max_barriers)
            barriers = _ipc.random_barriers(rng, n, count)
        blocked = [(x, 1, "north") for x in range(1, n + 1)] + [(x, n, "south") for x in range(1, n + 1)]
        blocked += [(1, y, "west") for y in range(1, n + 1)] + [(n, y, "east") for y in range(1, n + 1)]
        for x, y, d in barriers:
            dx, dy = _ipc.MOVES[d]
            blocked += [(x, y, d), (x + dx, y + dy, _ipc.OPPOSITE[d])]
        cells_xy = [(x, y) for x in range(1, n + 1) for y in range(1, n + 1)]
        robot = rng.choice(_ipc.ASP_2015_ROBOTS) if board == "asp2015" else rng.choice(cells_xy)
        target = rng.choice([cell for cell in cells_xy if cell != robot])
        cost = _ipc.optimal_moves(n, set(blocked), [robot], 0, target, n * n + 1)
        if cost is not None and cost > 0:
            break
    else:
        raise ValueError(f"no solvable task found in {_ipc.MAX_TRIES} draws; use fewer barriers")

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
    parser.add_argument("-b", "--num-barriers", type=int, help="default: uniform in 5..5 + size^2/3")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--board", choices=_ipc.BOARDS, default="random", help="random barriers or the ASP 2015 board")
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.board_size, args.num_barriers, args.seed, args.board), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
