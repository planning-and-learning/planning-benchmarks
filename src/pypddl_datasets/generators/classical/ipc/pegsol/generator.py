#!/usr/bin/env python3
# Peg Solitaire in the IPC 2008/2011 sequential encoding, output format of
# pddl-generators pegsol/generator.rb (printProblemSequential). Upstream does not
# generate boards: it converts the fixed Solipeg 2.2 puzzle library. This module
# instead draws random end-game positions on the same English board by playing
# jumps backwards from the single goal peg, so every task is solvable.

from __future__ import annotations

import argparse
import random
import sys

SIZE = 7
TARGET = (3, 3)
CELLS = [(r, c) for r in range(SIZE) for c in range(SIZE) if 2 <= r <= 4 or 2 <= c <= 4]
CELL_SET = set(CELLS)
MAX_PEGS = len(CELLS) - 1  # 32: a single hole
FULL_BOARD_HOLES = [(0, 3), (3, 0), (3, 3), (3, 6), (6, 3)]


def _lines() -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    """(from, over, to) triples in upstream's IN-LINE order (both directions)."""
    lines = []
    for r, c in CELLS:
        for dr, dc in ((0, 1), (1, 0)):
            over, to = (r + dr, c + dc), (r + 2 * dr, c + 2 * dc)
            if over in CELL_SET and to in CELL_SET:
                lines += [((r, c), over, to), (to, over, (r, c))]
    return lines


LINES = _lines()


INDEX = {cell: i for i, cell in enumerate(CELLS)}
LINE_BITS = [(1 << INDEX[a], 1 << INDEX[b], 1 << INDEX[c]) for a, b, c in LINES]
# The 8 symmetries of the board all fix the centre; dead ends are shared among images.
SYMMETRIES = [
    [INDEX[f(r, c)] for r, c in CELLS]
    for f in (
        lambda r, c: (r, c), lambda r, c: (c, 6 - r), lambda r, c: (6 - r, 6 - c), lambda r, c: (6 - c, r),
        lambda r, c: (r, 6 - c), lambda r, c: (6 - r, c), lambda r, c: (c, r), lambda r, c: (6 - c, 6 - r),
    )
]


RESTART_BUDGET = 2000


def _canonical(bits: int) -> int:
    return min(sum(1 << image[i] for i in range(len(CELLS)) if bits >> i & 1) for image in SYMMETRIES)


def _backward_position(num_pegs: int, rng: random.Random) -> frozenset[tuple[int, int]]:
    """Random position with ``num_pegs`` pegs from which one peg can end on TARGET.

    Depth-first search over reverse jumps in random order: a reverse jump turns
    an occupied ``to`` with free ``over`` and ``from`` into pegs on ``from`` and
    ``over``. Dead ends are memoised up to symmetry; a search that exceeds its
    node budget restarts with fresh random move orders (near-full boards need it).
    """
    if num_pegs == MAX_PEGS:
        # Single-hole boards: by the position-class ("rule of three") invariant only
        # holes in the centre's class can end on the centre, and all five can.
        return frozenset(CELL_SET - {rng.choice(FULL_BOARD_HOLES)})
    dead: set[int] = set()
    budget = [0]

    def grow(pegs: int, count: int) -> int | None:
        if count == num_pegs:
            return pegs
        key = _canonical(pegs)
        if key in dead or budget[0] <= 0:
            return None
        budget[0] -= 1
        moves = [(frm, over, to) for frm, over, to in LINE_BITS if pegs & to and not pegs & (frm | over)]
        rng.shuffle(moves)
        for frm, over, to in moves:
            found = grow(pegs ^ to | frm | over, count + 1)
            if found is not None:
                return found
        if budget[0] > 0:
            dead.add(key)
        return None

    while True:
        budget[0] = RESTART_BUDGET
        position = grow(1 << INDEX[TARGET], 1)
        if position is not None:
            return frozenset(cell for cell in CELLS if position >> INDEX[cell] & 1)


def make_problem(num_pegs: int, seed: int | None = None) -> str:
    """Generate a Peg Solitaire task with ``num_pegs`` pegs, goal: one peg on the centre."""
    if not isinstance(num_pegs, int) or isinstance(num_pegs, bool) or not 1 <= num_pegs <= MAX_PEGS:
        raise ValueError(f"num_pegs must be an integer in 1..{MAX_PEGS}")
    pegs = _backward_position(num_pegs, random.Random(seed))

    def name(cell: tuple[int, int]) -> str:
        return f"pos-{cell[0]}-{cell[1]}"

    indent = "        "
    objects = [f"{indent}{name(cell)} - location" for cell in CELLS]
    init = [f"{indent}(= (total-cost) 0)", f"{indent}(move-ended)"]
    init += [f"{indent}(in-line {name(a)} {name(b)} {name(c)})" for a, b, c in LINES]
    init += [f"{indent}(free {name(cell)})" for cell in CELLS if cell not in pegs]
    init += [f"{indent}(occupied {name(cell)})" for cell in CELLS if cell in pegs]
    goal = [f"{indent}(free {name(cell)})" for cell in CELLS if cell != TARGET]
    goal.append(f"{indent}(occupied {name(TARGET)})")
    nl = "\n"
    return (f"""(define (problem pegsolitaire-sequential-{num_pegs}pegs)
    (:domain pegsolitaire-sequential)
    (:objects
{nl.join(objects)}
    )
    (:init
{nl.join(init)}
    )
    (:goal (and
{nl.join(goal)}
           )
    )
    (:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Peg Solitaire (IPC sequential) PDDL problem.")
    parser.add_argument("-n", "--num-pegs", type=int, required=True, help=f"pegs on the board, 1..{MAX_PEGS}")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_pegs, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
