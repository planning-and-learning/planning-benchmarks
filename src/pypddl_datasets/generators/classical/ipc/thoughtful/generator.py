#!/usr/bin/env python3
# Thoughtful Solitaire (IPC 2008 learning track, reused in IPC 2014), typed STRIPS encoding.
# No original generator is public; the deal is reconstructed from the IPC tasks: a uniform
# shuffle dealt Klondike-style onto num_columns columns (1, 2, ... cards), the rest is the talon.

from __future__ import annotations

import argparse
import random
import sys

SUITS = ("c", "d", "h", "s")
BLACK = ("c", "s")
RANKS = "0a23456789tjqk"
MAX_CARDS = 13
PLAYABLE = 2  # the third talon card from the bottom is playable initially, as in every IPC task


def make_problem(num_cards: int, num_columns: int, seed: int | None = None) -> str:
    """Generate a Thoughtful task with 4 suits of ``num_cards`` cards and ``num_columns`` columns.

    Column i (1-based) gets i cards with only its top card face up; the remaining
    4 * num_cards - num_columns * (num_columns + 1) / 2 cards form the talon (at least 3).
    The goal is every suit's top card (the "king", rank ``num_cards``) at home.
    """
    checks: list[tuple[str, object, int]] = [
        ("num_cards", num_cards, MAX_CARDS),
        ("num_columns", num_columns, MAX_CARDS),
    ]
    for name, value, maximum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or not 1 <= value <= maximum:
            raise ValueError(f"{name} must be an integer in [1, {maximum}]")
    tableau = num_columns * (num_columns + 1) // 2
    if 4 * num_cards - tableau < PLAYABLE + 1:
        raise ValueError("num_columns too large: the talon needs at least 3 cards")

    ranks = range(num_cards + 1)
    deck = [f"{s}{RANKS[r]}" for s in SUITS for r in range(1, num_cards + 1)]
    random.Random(seed).shuffle(deck)

    init = [f"(value {s}{RANKS[r]} n{r})" for r in ranks for s in SUITS]
    init += [f"(colsuccessor coln{i + 1} coln{i})" for i in range(num_columns)]
    init += [f"(successor n{r + 1} n{r})" for r in range(num_cards)]
    init += [f"(suit {s}{RANKS[r]} {s})" for r in ranks for s in SUITS]
    init += [f"(king {s}{RANKS[num_cards]})" for s in SUITS]
    init += [
        f"(canstack {low}{RANKS[r]} {high}{RANKS[r + 1]})"
        for r in range(2, num_cards)
        for low in ("c", "s", "d", "h")
        for high in SUITS
        if (low in BLACK) != (high in BLACK)
    ]
    init.append("(colspace coln0)")
    start = 0
    for height in range(1, num_columns + 1):
        column = deck[start : start + height]
        start += height
        init.append(f"(bottomcol {column[0]})")
        init += [f"(on {upper} {lower})" for lower, upper in zip(column, column[1:])]
        init += [f"(clear {column[-1]})", f"(faceup {column[-1]})"]
    talon = deck[tableau:]
    init.append(f"(bottomtalon {talon[0]})")
    init += [f"(ontalon {upper} {lower})" for lower, upper in zip(talon, talon[1:])]
    init += [f"(toptalon {talon[-1]})", f"(talonplayable {talon[PLAYABLE]})"]
    init += [f"(home {s}0)" for s in SUITS]

    cards = "\n".join("    " + " ".join(f"{s}{RANKS[r]}" for r in ranks) for s in SUITS)
    return f"""(define (problem thoughtful-s{num_cards}-t{num_columns})
(:domain thoughtful-typed)
(:objects
{cards}
 - card
    {" ".join(f"coln{i}" for i in range(num_columns + 1))}
 - colnum
    {" ".join(f"n{r}" for r in ranks)}
 - num
    {" ".join(SUITS)}
 - suittype
)
(:init
{chr(10).join(init)}
)
(:goal
(and
{chr(10).join(f"(home {s}{RANKS[num_cards]})" for s in SUITS)}
)
)
)
""".lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Thoughtful Solitaire PDDL problem (IPC encoding).")
    parser.add_argument("-n", "--num-cards", type=int, required=True, help="cards per suit, ace upwards")
    parser.add_argument("-c", "--num-columns", type=int, required=True, help="tableau columns")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
