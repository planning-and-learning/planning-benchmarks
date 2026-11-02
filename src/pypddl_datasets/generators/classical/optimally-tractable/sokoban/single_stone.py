#!/usr/bin/env python3
"""Sokoban with a single stone on a level drawn by the IPC level generator.

The level comes from ipc/sokoban with num_stones = 1 and its parameters unchanged: a
connected room of num_floor cells grown inside a width x height box, the goal on a
random floor cell a stone can be pulled away from, the stone scrambled off it by
num_pulls random reverse pushes (the IPC default is 20 per stone; scale it with the
room for longer solutions), and the player on a random cell it can reach; grid="hex"
builds a Hexoban level.

With one stone the state is (stone cell, player cell), so the state space has at
most floor^2 states. Moves are free and pushes cost 1, so a 0-1 breadth-first search
over it gives the optimal cost, read off the generated level.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque

from pypddl_datasets.generators.classical.ipc.sokoban import generator as _ipc

Moves = dict[tuple[str, str], str]  # (cell, direction) -> neighbouring cell


def optimal_pushes(moves: Moves, stone: str, player: str, goals: set[str]) -> int | None:
    """Fewest pushes to get the stone onto a goal cell, or None if it cannot be done."""
    directions = sorted({direction for _, direction in moves})
    best = {(stone, player): 0}
    queue = deque([(stone, player)])
    while queue:
        state = queue.popleft()
        stone, player = state
        if stone in goals:
            return best[state]
        for direction in directions:
            step = moves.get((player, direction))
            if step is None:
                continue
            if step != stone:
                successor, cost = (stone, step), best[state]
            elif (beyond := moves.get((stone, direction))) is not None:
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


def make_problem(
    width: int, height: int, num_floor: int, num_pulls: int | None = None, seed: int | None = None,
    grid: str = "square",
) -> str:
    problem = _ipc.make_problem(width, height, num_floor, 1, seed=seed, num_pulls=num_pulls, grid=grid)
    moves: Moves = {(a, direction): b for a, b, direction in re.findall(r"\(move-dir (\S+) (\S+) (\S+)\)", problem)}
    player = re.findall(r"\(at player-01 (\S+)\)", problem)[0]
    stone = re.findall(r"\(at stone-01 (\S+)\)", problem)[0]
    goals = set(re.findall(r"\(is-goal (\S+)\)", problem))
    cost = optimal_pushes(moves, stone, player, goals)
    assert cost is not None  # levels are built by reverse play from the goal
    return f"; optimal plan cost: {cost}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Sokoban task with a single stone.")
    parser.add_argument("-x", "--width", type=int, required=True, help="level width including walls")
    parser.add_argument("-y", "--height", type=int, required=True, help="level height including walls")
    parser.add_argument("-f", "--num-floor", type=int, required=True, help="connected floor cells")
    parser.add_argument("--num-pulls", type=int, help="random reverse pushes (default: 20, as the IPC generator)")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--grid", choices=("square", "hex"), default="square", help="square (IPC) or hexagonal")
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.width, args.height, args.num_floor, args.num_pulls, args.seed, args.grid), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
