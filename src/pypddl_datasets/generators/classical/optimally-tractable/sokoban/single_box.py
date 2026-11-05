#!/usr/bin/env python3
"""Sokoban with a single box on a level drawn by the IPC 2023 learning-track generator.

The level comes from ipc_learning/sokoban with boxes = 1: the box starts in the inner
(grid_size - 4) square, the generator walks the robot to it and pushes it along up to
three straight runs of random length (turning 90 degrees in between), the box's end
cell is the goal, and 30-80% of the cells off that route become walls.

With one box the state is (box cell, robot cell), at most cells^2 states. The domain
has no action costs, so moves and pushes cost 1 each and a breadth-first search over
these states gives the optimal plan length.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from collections import deque

from pypddl_datasets.generators.classical.ipc_learning.sokoban import generator as _ipc

Moves = dict[tuple[str, str], str]  # (cell, direction) -> neighbouring cell


def optimal_cost(moves: Moves, box: str, robot: str, goal: str) -> int | None:
    """Fewest moves and pushes to get the box onto ``goal``, or None if it cannot be done."""
    directions = sorted({direction for _, direction in moves})
    steps = {(box, robot): 0}
    queue = deque([(box, robot)])
    while queue:
        state = queue.popleft()
        box, robot = state
        if box == goal:
            return steps[state]
        for direction in directions:
            step = moves.get((robot, direction))
            if step is None:
                continue
            if step != box:
                successor = (box, step)
            elif (beyond := moves.get((box, direction))) is not None:
                successor = (beyond, box)
            else:
                continue
            if successor not in steps:
                steps[successor] = steps[state] + 1
                queue.append(successor)
    return None


def make_problem(grid_size: int, seed: int | None = None) -> str:
    problem = _ipc.make_problem(grid_size, 1, seed if seed is not None else int(time.time()))
    moves: Moves = {(a, direction): b for a, b, direction in re.findall(r"\(adjacent (\S+) (\S+) ([^\s)]+)\)", problem)}
    robot = re.findall(r"\(at-robot ([^\s)]+)\)", problem)[0]
    box = re.findall(r"\(at box1 ([^\s)]+)\)", problem)[0]
    goal = re.findall(r"\(at box1 ([^\s)]+)\)", problem.split("(:goal")[1])[0]
    cost = optimal_cost(moves, box, robot, goal)
    assert cost is not None  # the generator plants a solution
    return f"; optimal plan cost: {cost}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Sokoban task with a single box.")
    parser.add_argument("-g", "--grid-size", type=int, required=True, help="square grid side including the walls")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.grid_size, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
