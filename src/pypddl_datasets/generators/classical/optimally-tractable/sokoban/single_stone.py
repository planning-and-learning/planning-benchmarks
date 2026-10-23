#!/usr/bin/env python3
"""Sokoban with a single stone in a random room with scattered walls.

With one stone the state is just (stone cell, player cell), so the state space has
at most cells^2 states. Moves are free and pushes cost 1, so a 0-1 breadth-first
search over it gives the optimal cost. Rooms are resampled until the stone can
reach the goal.
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from collections import deque

Cell = tuple[int, int]
DIRECTIONS = {"dir-up": (0, -1), "dir-down": (0, 1), "dir-left": (-1, 0), "dir-right": (1, 0)}


def optimal_pushes(floor: set[Cell], stone: Cell, player: Cell, goal: Cell) -> int | None:
    best = {(stone, player): 0}
    queue = deque([(stone, player)])
    while queue:
        state = queue.popleft()
        stone, player = state
        if stone == goal:
            return best[state]
        for dx, dy in DIRECTIONS.values():
            step = (player[0] + dx, player[1] + dy)
            if step not in floor:
                continue
            if step != stone:
                successor, cost = (stone, step), best[state]
            elif (beyond := (stone[0] + dx, stone[1] + dy)) in floor:
                successor, cost = (beyond, stone), best[state] + 1
            else:
                continue
            if successor not in best or cost < best[successor]:
                best[successor] = cost
                if cost == best[state]:
                    queue.appendleft(successor)
                else:
                    queue.append(successor)
    return None


def make_problem(width: int, height: int, wall_ratio: float = 0.15, seed: int | None = None) -> str:
    if width < 3 or height < 3:
        raise ValueError("width and height must be at least 3")
    if not 0 <= wall_ratio < 0.7:
        raise ValueError("wall_ratio must be in [0, 0.7)")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for y in range(height) for x in range(width)]
    while True:
        floor = {cell for cell in cells if rng.random() >= wall_ratio}
        if len(floor) < 3:
            continue
        stone, player, goal = rng.sample(sorted(floor), 3)
        cost = optimal_pushes(floor, stone, player, goal)
        if cost is not None:
            break

    def name(cell: Cell) -> str:
        return f"pos-{cell[0] + 1:02d}-{cell[1] + 1:02d}"

    locations = sorted(floor)
    init = [
        "(= (total-cost) 0)",
        f"(at player-01 {name(player)})",
        f"(at stone-01 {name(stone)})",
        *(f"({'is-goal' if cell == goal else 'is-nongoal'} {name(cell)})" for cell in locations),
        *(f"(clear {name(cell)})" for cell in locations if cell not in (stone, player)),
        *(
            f"(move-dir {name(cell)} {name((cell[0] + dx, cell[1] + dy))} {direction})"
            for cell in locations
            for direction, (dx, dy) in DIRECTIONS.items()
            if (cell[0] + dx, cell[1] + dy) in floor
        ),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem sokoban-single-stone-{width}x{height})
  (:domain sokoban-sequential)
  (:objects
    {' '.join(DIRECTIONS)} - direction
    player-01 - player
    {' '.join(name(cell) for cell in locations)} - location
    stone-01 - stone
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
      (at-goal stone-01)
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a single-stone Sokoban task.")
    parser.add_argument("-x", "--width", type=int, required=True)
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-w", "--wall-ratio", type=float, default=0.15)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.wall_ratio, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
