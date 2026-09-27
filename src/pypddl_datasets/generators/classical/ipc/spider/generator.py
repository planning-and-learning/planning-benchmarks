#!/usr/bin/env python3
# Port of pddl-generators spider/generate.py (IPC 2018). The IPC tasks were additionally
# filtered with an external spider solver (generate-and-solve.sh retried seed + 1 until
# solvable); that filter is not reproduced.

from __future__ import annotations

import argparse
import random
import sys
from itertools import product

Card = tuple[int, int, int]


def _name(card: Card) -> str:
    return "card-d%s-s%s-v%s" % card


def _movable_top(pile: list[Card]) -> list[Card]:
    """The maximal same-suit descending run on top of the pile."""
    top = [pile[-1]]
    for below in reversed(pile[:-1]):
        (_, suit, value), (_, next_suit, next_value) = below, top[0]
        if suit != next_suit or value != next_value + 1:
            break
        top.insert(0, below)
    return top


def make_problem(
    num_decks: int,
    num_suits: int,
    num_values: int,
    num_piles: int,
    num_deals: int = 2,
    seed: int | None = None,
) -> str:
    """Generate a Spider task.

    All ``num_decks * num_suits * num_values`` cards are shuffled; the first
    ``num_deals * num_piles`` form the deals (one card per pile each), the rest go
    to the piles as evenly as possible, the first piles getting the leftovers. The
    goal is every card on the discard pile with all piles and deals empty.
    """
    for name, value in (
        ("num_decks", num_decks),
        ("num_suits", num_suits),
        ("num_values", num_values),
        ("num_piles", num_piles),
        ("num_deals", num_deals),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < (0 if name == "num_deals" else 1):
            raise ValueError(f"{name} must be an integer at least {0 if name == 'num_deals' else 1}")
    num_cards = num_decks * num_suits * num_values
    if num_cards < (num_deals + 1) * num_piles:
        raise ValueError("num_piles too large: every pile needs a card besides the deals")

    rng = random.Random(seed)
    cards: list[Card] = list(product(range(num_decks), range(num_suits), range(num_values)))
    rng.shuffle(cards)
    deals = [cards[i * num_piles : (i + 1) * num_piles] for i in range(num_deals)]
    rest = cards[num_deals * num_piles :]
    per_pile = len(rest) // num_piles
    piles = [rest[i * per_pile : (i + 1) * per_pile] for i in range(num_piles)]
    for pile, card in zip(piles, rest[num_piles * per_pile :]):
        pile.append(card)

    comments = [f"using {num_decks} decks of cards with {num_suits} suits per deck and {num_values} values per suit", "", "deals"]
    comments += [f"deal {i}: " + " ".join("d%s-s%s-v%s" % c for c in deal) for i, deal in enumerate(deals)]
    comments += ["", "initial configuration of piles"]
    comments += [f"pile {i}: " + " ".join("d%s-s%s-v%s" % c for c in pile) for i, pile in enumerate(piles)]

    objects = [f"{_name(card)} - card" for card in product(range(num_decks), range(num_suits), range(num_values))]
    objects += [f"pile-{i} - tableau" for i in range(num_piles)]
    objects += [f"deal-{i} - deal" for i in range(num_deals + 1)]

    facts = []
    for i, pile in enumerate(piles):
        facts += [f"(on {_name(upper)} {_name(lower)})" for upper, lower in zip(pile[1:], pile)]
        facts += [f"(on {_name(pile[0])} pile-{i})", f"(clear {_name(pile[-1])})", f"(part-of-tableau pile-{i} pile-{i})"]
        facts += [f"(part-of-tableau {_name(card)} pile-{i})" for card in pile]
        facts += [f"(movable {_name(card)})" for card in _movable_top(pile)]
        facts += [f"(in-play {_name(card)})" for card in pile]
    for i, deal in enumerate(deals):
        stack = deal[::-1]
        facts.append(f"(on {_name(stack[-1])} deal-{i})")
        facts += [f"(on {_name(upper)} {_name(lower)})" for lower, upper in zip(stack[1:], stack)][::-1]
        facts.append(f"(clear {_name(stack[0])})")
    facts.append("(current-deal deal-0)")
    decks, suits = range(num_decks), range(num_suits)
    facts += [
        f"(can-continue-group {_name((d1, s, v))} {_name((d2, s, v + 1))})"
        for d1 in decks for d2 in decks for s in suits for v in range(num_values - 1)
    ]
    facts += [
        f"(can-be-placed-on {_name((d1, s1, v))} {_name((d2, s2, v + 1))})"
        for d1 in decks for d2 in decks for s1 in suits for s2 in suits for v in range(num_values - 1)
    ]
    facts += [f"(is-ace {_name((d, s, 0))})" for d in decks for s in suits]
    facts += [f"(is-king {_name((d, s, num_values - 1))})" for d in decks for s in suits]
    facts += [f"(next-deal deal-{i} deal-{i + 1})" for i in range(num_deals)]
    for i, deal in enumerate(deals):
        stack = deal[::-1]
        facts.append(f"(to-deal {_name(stack[-1])} pile-{len(deal) - 1} deal-{i} deal-{i})")
        facts += [
            f"(to-deal {_name(following)} pile-{p} deal-{i} {_name(card)})"
            for p, (card, following) in enumerate(zip(stack[1:], stack))
        ]
    facts.append("(= (total-cost) 0)")

    goals = [f"(clear pile-{i})" for i in range(num_piles)] + [f"(clear deal-{i})" for i in range(num_deals)]
    goals += [f"(on {_name(card)} discard)" for card in product(decks, suits, range(num_values))]

    name = f"spider-{num_decks}-{num_suits}-{num_values}-{num_piles}-{num_deals}" + (f"-{seed}" if seed is not None else "")
    lines = [f"(define (problem {name})", "(:domain spider)", *(f"; {c}".rstrip() for c in comments), "(:objects"]
    lines += [f"    {o}" for o in objects] + [")", "(:init"] + [f"    {f}" for f in facts]
    lines += [")", "(:goal (and"] + [f"    {g}" for g in goals] + ["))", "(:metric minimize (total-cost))", ")"]
    return ("\n".join(lines) + "\n").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Spider solitaire PDDL problem.")
    parser.add_argument("-d", "--num-decks", type=int, required=True)
    parser.add_argument("-u", "--num-suits", type=int, required=True, help="suits per deck")
    parser.add_argument("-v", "--num-values", type=int, required=True, help="values per suit")
    parser.add_argument("-p", "--num-piles", type=int, required=True)
    parser.add_argument("-e", "--num-deals", type=int, default=2, help="deals (default: 2)")
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
