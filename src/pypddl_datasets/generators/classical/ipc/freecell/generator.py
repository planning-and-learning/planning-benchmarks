#!/usr/bin/env python3
# FreeCell in the untyped STRIPS encoding of the IPC 2000/2002 tasks (Fahiem Bacchus).
# The original IPC generator is not public; the deal is reconstructed from the tasks in
# downward-benchmarks/freecell (pddl-generators' freecell.c uses a different encoding).

from __future__ import annotations

import argparse
import random
import sys

SUITS = {"ipc2000": ("c", "d", "h", "s"), "ipc2002": ("club", "diamond", "heart", "spade")}
RED = {1, 2}  # diamonds and hearts; clubs and spades are black
RANKS = ["0", "a", *map(str, range(2, 11)), "j", "q", "k"]
FULL_DECK = 13


def make_problem(
    num_cards: int,
    num_cells: int = 4,
    num_columns: int = 8,
    seed: int | None = None,
    style: str = "ipc2000",
) -> str:
    """Generate a FreeCell task with 4 suits of ``num_cards`` cards (ace upwards).

    ``ipc2000``: a shuffled 52-card deck is dealt round-robin onto the columns and every
    card above ``num_cards`` is removed, so columns are uneven and may end up empty;
    numbers n0..n13 always exist. ``ipc2002``: only the 4 * ``num_cards`` cards are
    shuffled and dealt round-robin, so column heights differ by at most one; numbers
    run up to max(num_cards, num_cells, num_columns). All cells start empty; the goal
    is every suit's top card at home.
    """
    checks: list[tuple[str, object, int, int]] = [
        ("num_cards", num_cards, 1, FULL_DECK),
        ("num_cells", num_cells, 0, FULL_DECK),
        ("num_columns", num_columns, 1, FULL_DECK),
    ]
    for name, value, minimum, maximum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or not minimum <= value <= maximum:
            raise ValueError(f"{name} must be an integer in [{minimum}, {maximum}]")
    if style not in SUITS:
        raise ValueError(f"style must be one of {sorted(SUITS)}")

    rng = random.Random(seed)
    suits = SUITS[style]
    full_deck = style == "ipc2000"

    def card(suit: int, rank: int) -> str:
        return f"{suits[suit]}{RANKS[rank]}"

    deck = [(suit, rank) for suit in range(4) for rank in range(1, (FULL_DECK if full_deck else num_cards) + 1)]
    rng.shuffle(deck)
    columns: list[list[tuple[int, int]]] = [[] for _ in range(num_columns)]
    for index, dealt in enumerate(deck):
        columns[index % num_columns].append(dealt)
    columns = [[c for c in column if c[1] <= num_cards] for column in columns]
    stacks = [column for column in columns if column]

    max_number = max(FULL_DECK if full_deck else num_cards, num_cells, num_columns)
    cards = [(suit, rank) for suit in range(4) for rank in range(num_cards + 1)]
    init = [f"(value {card(s, r)} n{r})" for s, r in cards]
    init += [f"(suit {card(s, r)} {suits[s]})" for s, r in cards]
    init += [f"(successor n{i + 1} n{i})" for i in range(max_number)]
    init += [
        f"(canstack {card(s, r)} {card(t, r + 1)})"
        for s, r in cards
        for t in range(4)
        if 1 <= r < num_cards and (s in RED) != (t in RED)
    ]
    init += [f"(home {card(s, 0)})" for s in range(4)]
    init += [f"(cellspace n{num_cells})", f"(colspace n{num_columns - len(stacks)})"]
    for stack in stacks:
        init.append(f"(bottomcol {card(*stack[0])})")
        init += [f"(on {card(*upper)} {card(*lower)})" for lower, upper in zip(stack, stack[1:])]
        init.append(f"(clear {card(*stack[-1])})")

    objects = [*suits, *(f"n{i}" for i in range(max_number + 1)), *(card(s, r) for s, r in cards)]
    name = f"freecell-{num_cards}" + (f"-{seed}" if seed is not None else "") if full_deck else f"freecell{num_cards}-4"
    return (f"""(define (problem {name})
(:domain freecell)
(:objects
{chr(10).join("    " + o for o in objects)}
)
(:init
{chr(10).join("    " + fact for fact in init)}
)
(:goal (and
{chr(10).join(f"    (home {card(s, num_cards)})" for s in range(4))}
)))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a STRIPS FreeCell PDDL problem (IPC encoding).")
    parser.add_argument("-n", "--num-cards", type=int, required=True, help="cards per suit (ace upwards)")
    parser.add_argument("-f", "--num-cells", type=int, default=4, help="free cells (default: 4)")
    parser.add_argument("-c", "--num-columns", type=int, default=8, help="tableau columns (default: 8)")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument(
        "--style", choices=sorted(SUITS), default="ipc2000", help="deal and naming of the IPC 2000 or 2002 tasks"
    )
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
