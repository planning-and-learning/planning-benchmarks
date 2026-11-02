#!/usr/bin/env python3
"""TPP as generated for the IPC with one truck, every good sold at exactly one market, and roads between all places.

Supplies and demands are drawn as by the IPC generator (ipc/tpp): a good's total
supply is the capped sum of per-market lots (each market with probability 1/2, one
forced market always, lots of 1..ceil(max_level / (markets / 2)) until max_level), and
its demand is uniform in 1..supply; here the whole supply sits at one uniform random
market per good. num_depots depots as in the IPC, the truck at a random one. Every
place is connected to every other (the IPC's partial road graph would make the tour a
travelling salesman problem).

Each demanded unit costs buy + load + unload. Every market selling a demanded good
must be visited, one drive each from anywhere, plus the drive to a depot to unload:
cost 3 * (demanded units) + (markets visited) + 1. Choosing between markets selling
the same good would make it a set cover problem.
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from math import ceil


def make_problem(
    num_goods: int, num_markets: int, max_level: int, num_depots: int = 1, seed: int | None = None
) -> str:
    for name, value in (
        ("num_goods", num_goods), ("num_markets", num_markets), ("max_level", max_level), ("num_depots", num_depots)
    ):
        if value < 1:
            raise ValueError(f"{name} must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    goods = [f"goods{i}" for i in range(num_goods)]
    markets = [f"market{i}" for i in range(num_markets)]
    depots = [f"depot{i}" for i in range(num_depots)]
    # the IPC's supply draw: each market sells with probability 1/2 (one market sells every
    # good), lots of 1..max_forsale, until the good's total reaches max_level
    max_forsale = ceil(max_level / (num_markets // 2)) if num_markets > 2 else max_level
    forced_market = rng.randrange(num_markets)
    supply: list[int] = []
    for _ in goods:
        total = 0
        for market in range(num_markets):
            if total >= max_level:
                break
            if rng.randint(0, 1) or market == forced_market:
                total += min(rng.randint(1, max_forsale), max_level - total)
        supply.append(total)
    truck_depot = rng.randrange(num_depots)
    demand = [rng.randint(1, min(total, max_level)) for total in supply]
    seller = [rng.randrange(num_markets) for _ in goods]  # the one market selling the good's whole supply
    cost = 3 * sum(demand) + len(set(seller)) + 1
    places = [*depots, *markets]
    init = [
        *(f"(next level{i} level{i - 1})" for i in range(1, max_level + 1)),
        *(f"(connected {a} {b})" for a in places for b in places if a != b),
        f"(at truck0 depot{truck_depot})",
        *(f"(stored {g} level0)\n    (loaded {g} truck0 level0)" for g in goods),
        *(f"(ready-to-load {g} {m} level0)" for g in goods for m in markets),
        *(f"(on-sale {g} {markets[m]} level{s})" for g, m, s in zip(goods, seller, supply)),
        *(f"(on-sale {g} {m} level0)" for g, s in zip(goods, seller) for i, m in enumerate(markets) if i != s),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem tpp-exclusive-markets-g{num_goods}-m{num_markets}-d{num_depots}-l{max_level})
  (:domain tpp-propositional)
  (:objects
    {' '.join(markets)} - market
    {' '.join(depots)} - depot
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
    parser = argparse.ArgumentParser(description="Generate a TPP task where every good is sold at one market.")
    parser.add_argument("-g", "--num-goods", type=int, required=True)
    parser.add_argument("-m", "--num-markets", type=int, required=True)
    parser.add_argument("-l", "--max-level", type=int, required=True)
    parser.add_argument("-d", "--num-depots", type=int, default=1)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_goods, args.num_markets, args.max_level, args.num_depots, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
