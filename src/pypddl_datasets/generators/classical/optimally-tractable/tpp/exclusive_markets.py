#!/usr/bin/env python3
"""TPP with one truck, every good sold at exactly one market, and roads between all places.

Each demanded unit costs buy + load + unload. Every market selling a demanded good
must be visited, one drive each from anywhere, plus the drive back to the depot:
cost 3 * (demanded units) + (markets visited) + 1. Choosing between markets selling
the same good would make it a set cover problem.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_goods: int, num_markets: int, max_level: int, seed: int | None = None) -> str:
    for name, value in (("num_goods", num_goods), ("num_markets", num_markets), ("max_level", max_level)):
        if value < 1:
            raise ValueError(f"{name} must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    goods = [f"goods{i}" for i in range(num_goods)]
    markets = [f"market{i}" for i in range(num_markets)]
    seller = [rng.randrange(num_markets) for _ in goods]
    supply = [rng.randint(1, max_level) for _ in goods]
    demand = [rng.randint(1, s) for s in supply]
    cost = 3 * sum(demand) + len(set(seller)) + 1
    places = ["depot0", *markets]
    init = [
        *(f"(next level{i} level{i - 1})" for i in range(1, max_level + 1)),
        *(f"(connected {a} {b})" for a in places for b in places if a != b),
        "(at truck0 depot0)",
        *(f"(stored {g} level0)\n    (loaded {g} truck0 level0)" for g in goods),
        *(f"(ready-to-load {g} {m} level0)" for g in goods for m in markets),
        *(f"(on-sale {g} {markets[m]} level{s})" for g, m, s in zip(goods, seller, supply)),
        *(f"(on-sale {g} {m} level0)" for g, s in zip(goods, seller) for i, m in enumerate(markets) if i != s),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem tpp-exclusive-markets-g{num_goods}-m{num_markets}-l{max_level})
  (:domain tpp-propositional)
  (:objects
    {' '.join(markets)} - market
    depot0 - depot
    truck0 - truck
    {' '.join(goods)} - goods
    {' '.join(f'level{i}' for i in range(max_level + 1))} - level
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (stored {g} level{d})' for g, d in zip(goods, demand))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a TPP task where each good has one seller.")
    parser.add_argument("-g", "--num-goods", type=int, required=True)
    parser.add_argument("-m", "--num-markets", type=int, required=True)
    parser.add_argument("-l", "--max-level", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_goods, args.num_markets, args.max_level, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
