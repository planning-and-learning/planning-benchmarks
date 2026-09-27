#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators freecell/freecell.c (FF domain collection). Distributed
# under the original notice, not GPL-3.0-or-later (see LICENSES/LicenseRef-Freiburg.txt):
#
# (C) Copyright 2001 Albert Ludwigs University Freiburg
#     Institute of Computer Science
#
# All rights reserved. Use of this software is permitted for
# non-commercial research purposes, and it may be copied only
# for that use.  All copies must include this copyright message.
# This software is made available AS IS, and neither the authors
# nor the  Albert Ludwigs University Freiburg make any warranty
# about the software or its performance.
"""Typed Freecell, as in the Autoscale 21.11 tasks (`freecell -f -c -s -0..-3 -i`)."""

from __future__ import annotations

import argparse
import random
import sys

SUITS = "chsd"
# CANSTACK partners per suit, in upstream's output order
PARTNERS = {0: (1, 3), 1: (0, 2), 2: (1, 3), 3: (0, 2)}


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _card(suit: int, index: int) -> str:
    return f"{SUITS[suit]}{'a' if index == 0 else index + 1}"


def make_problem(
    num_cells: int,
    num_columns: int,
    num_stacks: int,
    suit_size: int,
    num_suits: int = 4,
    seed: int | None = None,
) -> str:
    """Generate a typed Freecell task.

    Cards are dealt one at a time: a uniform suit among those with undealt cards,
    a uniform undealt card of it, onto a uniform one of ``num_stacks`` initial
    stacks (a stack may stay empty). ``COLSPACE`` is ``num_columns - num_stacks``
    either way, as upstream. The goal puts every suit's top card home.
    """
    for name, value, minimum in (
        ("num_cells", num_cells, 0),
        ("num_columns", num_columns, 1),
        ("num_stacks", num_stacks, 1),
        ("suit_size", suit_size, 1),
        ("num_suits", num_suits, 1),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_suits > 4:
        raise ValueError("num_suits must be at most 4")
    if num_stacks > num_columns:
        raise ValueError("num_stacks must not exceed num_columns")
    # ponytail: all suits share one size (as in every Autoscale task); upstream allows one per suit.

    rng = random.Random(seed)
    undealt = [list(range(suit_size)) for _ in range(num_suits)]
    stacks: list[list[tuple[int, int]]] = [[] for _ in range(num_stacks)]
    while any(undealt):
        suit = rng.choice([s for s in range(num_suits) if undealt[s]])
        index = undealt[suit].pop(rng.randrange(len(undealt[suit])))
        stacks[rng.randrange(num_stacks)].append((suit, index))

    suits = range(num_suits)
    init: list[str] = []
    for s in suits:
        init.append(f"(value {SUITS[s]}0 n0)")
        init += [f"(value {_card(s, j)} n{j + 1})" for j in range(suit_size)]
    init += [f"(cellsuccessor celln{i + 1} celln{i})" for i in range(num_cells)]
    init += [f"(colsuccessor coln{i + 1} coln{i})" for i in range(num_columns)]
    init += [f"(successor n{i + 1} n{i})" for i in range(suit_size)]
    for s in suits:
        init.append(f"(hassuit {SUITS[s]}0 {SUITS[s]})")
        init += [f"(hassuit {_card(s, j)} {SUITS[s]})" for j in range(suit_size)]
    for s in suits:
        for i in range(1, suit_size - 1):  # card i onto a partner's card i + 1
            init += [f"(canstack {_card(s, i)} {_card(p, i + 1)})" for p in PARTNERS[s] if p < num_suits]
    init += [f"(home {SUITS[s]}0)" for s in suits]
    init += [f"(cellspace celln{num_cells})", f"(colspace coln{num_columns - num_stacks})"]
    for stack in stacks:
        if not stack:
            continue
        init.append(f"(bottomcol {_card(*stack[0])})")
        init += [f"(on {_card(*upper)} {_card(*lower)})" for lower, upper in zip(stack, stack[1:])]
        init.append(f"(clear {_card(*stack[-1])})")
    goal = [f"(home {_card(s, suit_size - 1)})" for s in suits]

    cards = "\n".join(f"          {SUITS[s]}0 " + " ".join(_card(s, j) for j in range(suit_size)) for s in suits)
    sizes = "".join(f"-{s}{suit_size}" for s in suits)
    return (f"""(define (problem freecell-f{num_cells}-c{num_columns}-s{num_suits}-i{num_stacks}{sizes})
(:domain freecell)
(:objects
{cards}
 - card
          {" ".join(f"celln{i}" for i in range(num_cells + 1))}
 - cellnum
          {" ".join(f"coln{i}" for i in range(num_columns + 1))}
 - colnum
          {" ".join(f"n{i}" for i in range(suit_size + 1))}
 - num
          {" ".join(SUITS[s] for s in suits)}
 - suit
)
(:init
{chr(10).join(init)}
)
(:goal
(and
{chr(10).join(goal)}
)
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a typed Freecell PDDL problem (Autoscale 21.11 encoding).")
    parser.add_argument("-f", "--num-cells", type=int, required=True)
    parser.add_argument("-c", "--num-columns", type=int, required=True)
    parser.add_argument("-i", "--num-stacks", type=int, required=True)
    parser.add_argument("-n", "--suit-size", type=int, required=True, help="cards per suit")
    parser.add_argument("-s", "--num-suits", type=int, default=4)
    parser.add_argument("-r", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
