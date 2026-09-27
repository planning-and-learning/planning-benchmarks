#!/usr/bin/env python3
# Port of ipc2023-classical/domain-rubiks-cube generator.py (Bharath Muppasani, Biplav
# Srivastava, Clemens Büchner, Patrick Ferber; public domain). Random draws happen in
# upstream's order, so a seed reproduces the IPC 2023 task of that seed exactly.

from __future__ import annotations

import argparse
import random
import sys
from typing import cast

# Stickers are indexed face * 9 + row * 3 + column, faces red, orange, white, green,
# blue, yellow as upstream. A move maps new[i] = old[MOVES[move][i]]; the tables are
# upstream's twelve hand-written quarter-turn functions applied to a labelled cube.
COLOURS = ("red", "orange", "white", "green", "blue", "yellow")
MOVES = {
    "B": (
        0, 1, 2, 3, 4, 5, 33, 34, 35, 42, 10, 11, 43, 13, 14, 44, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
        29, 30, 31, 32, 9, 12, 15, 36, 37, 38, 39, 40, 41, 6, 7, 8, 47, 50, 53, 46, 49, 52, 45, 48, 51,
    ),
    "Brev": (
        0, 1, 2, 3, 4, 5, 42, 43, 44, 33, 10, 11, 34, 13, 14, 35, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
        29, 30, 31, 32, 6, 7, 8, 36, 37, 38, 39, 40, 41, 9, 12, 15, 51, 48, 45, 52, 49, 46, 53, 50, 47,
    ),
    "D": (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 17, 10, 13, 16, 9, 12, 15, 18, 19, 42, 21, 22, 39, 24, 25, 36, 27, 28, 20,
        30, 31, 23, 33, 34, 26, 45, 37, 38, 48, 40, 41, 51, 43, 44, 35, 46, 47, 32, 49, 50, 29, 52, 53,
    ),
    "Drev": (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 12, 9, 16, 13, 10, 17, 14, 11, 18, 19, 29, 21, 22, 32, 24, 25, 35, 27, 28, 51,
        30, 31, 48, 33, 34, 45, 26, 37, 38, 23, 40, 41, 20, 43, 44, 36, 46, 47, 39, 49, 50, 42, 52, 53,
    ),
    "F": (
        36, 37, 38, 3, 4, 5, 6, 7, 8, 9, 10, 27, 12, 13, 28, 15, 16, 29, 20, 23, 26, 19, 22, 25, 18, 21, 24, 0, 1, 2,
        30, 31, 32, 33, 34, 35, 11, 14, 17, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
    ),
    "Frev": (
        27, 28, 29, 3, 4, 5, 6, 7, 8, 9, 10, 36, 12, 13, 37, 15, 16, 38, 24, 21, 18, 25, 22, 19, 26, 23, 20, 11, 14, 17,
        30, 31, 32, 33, 34, 35, 0, 1, 2, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
    ),
    "L": (
        47, 1, 2, 46, 4, 5, 45, 7, 8, 9, 10, 11, 12, 13, 14, 20, 19, 18, 6, 3, 0, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 38, 41, 44, 37, 40, 43, 36, 39, 42, 17, 16, 15, 48, 49, 50, 51, 52, 53,
    ),
    "Lrev": (
        20, 1, 2, 19, 4, 5, 18, 7, 8, 9, 10, 11, 12, 13, 14, 47, 46, 45, 17, 16, 15, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 42, 39, 36, 43, 40, 37, 44, 41, 38, 6, 3, 0, 48, 49, 50, 51, 52, 53,
    ),
    "R": (
        0, 1, 26, 3, 4, 25, 6, 7, 24, 53, 52, 51, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 11, 10, 9, 29, 32, 35,
        28, 31, 34, 27, 30, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 8, 5, 2,
    ),
    "Rrev": (
        0, 1, 53, 3, 4, 52, 6, 7, 51, 26, 25, 24, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 8, 5, 2, 33, 30, 27,
        34, 31, 28, 35, 32, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 11, 10, 9,
    ),
    "U": (
        2, 5, 8, 1, 4, 7, 0, 3, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 27, 19, 20, 30, 22, 23, 33, 25, 26, 53, 28, 29,
        50, 31, 32, 47, 34, 35, 36, 37, 24, 39, 40, 21, 42, 43, 18, 45, 46, 38, 48, 49, 41, 51, 52, 44,
    ),
    "Urev": (
        6, 3, 0, 7, 4, 1, 8, 5, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 44, 19, 20, 41, 22, 23, 38, 25, 26, 18, 28, 29,
        21, 31, 32, 24, 34, 35, 36, 37, 47, 39, 40, 50, 42, 43, 53, 45, 46, 33, 48, 49, 30, 51, 52, 27,
    ),
}
ACTIONS = sorted(MOVES)  # upstream draws from the sorted names, without double moves
# upstream toPddlState: the stickers of each corner cube and edge, in fact order
PIECES = (
    ("cube1", (0, 18, 38)), ("cube2", (17, 20, 36)), ("cube3", (6, 47, 44)), ("cube4", (15, 45, 42)),
    ("cube5", (2, 24, 27)), ("cube6", (11, 26, 29)), ("cube7", (8, 53, 33)), ("cube8", (9, 51, 35)),
    ("edge12", (19, 37)), ("edge24", (16, 39)), ("edge34", (46, 43)), ("edge13", (3, 41)),
    ("edge15", (1, 21)), ("edge26", (14, 23)), ("edge48", (12, 48)), ("edge37", (7, 50)),
    ("edge56", (25, 28)), ("edge68", (10, 32)), ("edge78", (52, 34)), ("edge57", (5, 30)),
)


def _redundant(face: str, last: str, second_to_last: str) -> bool:
    """Upstream check_not_optimal: same face twice, or X Y X on opposite faces."""
    if face == last:
        return True
    return face == second_to_last and any(face in pair and last in pair for pair in ("FB", "LR", "UD"))


def _pieces(stickers: list[str]) -> list[str]:
    return [f"({name} {' '.join(stickers[i] for i in indices)})" for name, indices in PIECES]


def make_problem(num_moves: int, seed: int | None = None) -> str:
    """Scramble the solved cube with ``num_moves`` random quarter turns.

    A move is redrawn while it turns the face of the last move, or the face two
    moves back with the last move on the opposite face (then again while it
    shares the last move's face letter), as upstream. The goal is the solved cube.
    """
    checked = cast(object, num_moves)  # runtime check: callers may pass any type
    if not isinstance(checked, int) or isinstance(checked, bool) or checked < 1:
        raise ValueError("num_moves must be an integer at least 1")
    rng = random.Random(seed)
    stickers = [colour for colour in COLOURS for _ in range(9)]
    solved = _pieces(stickers)
    moves: list[str] = []
    for i in range(num_moves):
        move = rng.choice(ACTIONS)
        if i > 1:
            while _redundant(move[0].upper(), moves[-1][0].upper(), moves[-2][0].upper()):
                move = rng.choice(ACTIONS)
        if i > 0:
            while move[0] == moves[-1][0]:
                move = rng.choice(ACTIONS)
        moves.append(move)
        stickers = [stickers[j] for j in MOVES[move]]

    init = "\n    ".join(_pieces(stickers))
    goal = [f"        {fact}" for fact in solved]
    for index in (16, 12, 8):  # blank lines between upstream's goal groups
        goal.insert(index, "")
    return (f"""(define
(problem rubiks-cube-shuffle-{num_moves})
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    {init}
)
(:goal
    (and
{chr(10).join(goal)}

    )
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Rubik's Cube PDDL problem (IPC 2023).")
    parser.add_argument("num_moves", type=int, help="random quarter turns applied to the solved cube")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_moves, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
