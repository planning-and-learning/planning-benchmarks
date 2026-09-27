#!/usr/bin/env python3

# Port of pddl-generators/tpp/tpp.c (gen-TPP, TPP-Propositional: no fuel, money
# or incompatibilities), the IPC 2006 generator, as also called by Autoscale 21.11:
# `tpp -s <seed> -m <markets> -p <products> -t <trucks> -d <depots> -l <goods>`.

from __future__ import annotations

import argparse
import random
import sys
from math import ceil


def _connected(edges: set[frozenset[int]], num_markets: int) -> bool:
    reached = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for other in range(num_markets):
            if other not in reached and frozenset((current, other)) in edges:
                reached.add(other)
                frontier.append(other)
    return len(reached) == num_markets


def make_problem(
    num_products: int,
    num_markets: int,
    num_trucks: int,
    num_depots: int,
    max_level: int,
    seed: int | None = None,
) -> str:
    for name, value in (
        ("num_products", num_products),
        ("num_markets", num_markets),
        ("num_trucks", num_trucks),
        ("num_depots", num_depots),
        ("max_level", max_level),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")

    rng = random.Random(seed)

    # Start from the complete market graph and try to cut a random number of
    # random roads, keeping only cuts that leave the markets connected.
    edges = {frozenset((i, j)) for i in range(num_markets) for j in range(i + 1, num_markets)}
    attempts = rng.randint(1, len(edges)) if num_markets > 2 else 0
    for _ in range(attempts):
        edge = frozenset(rng.sample(range(num_markets), 2))
        if edge in edges:
            edges.remove(edge)
            if not _connected(edges, num_markets):
                edges.add(edge)
    depot_markets = [rng.randrange(num_markets) for _ in range(num_depots)]

    # Each market sells a product with probability 1/2 (one market sells every
    # product), until the product's total supply reaches max_level.
    max_forsale = ceil(max_level / (num_markets // 2)) if num_markets > 2 else max_level
    forced_market = rng.randrange(num_markets)
    on_sale = [[0] * num_products for _ in range(num_markets)]
    totals = []
    for product in range(num_products):
        total = 0
        for market in range(num_markets):
            if total >= max_level:
                break
            if rng.randint(0, 1) or market == forced_market:
                level = min(rng.randint(1, max_forsale), max_level - total)
                total += level
                on_sale[market][product] = level
        totals.append(total)
    truck_depots = [rng.randrange(num_depots) for _ in range(num_trucks)]
    goals = [rng.randint(1, min(total, max_level)) for total in totals]

    goods = [f"goods{i}" for i in range(1, num_products + 1)]
    trucks = [f"truck{i}" for i in range(1, num_trucks + 1)]
    markets = [f"market{i}" for i in range(1, num_markets + 1)]
    depots = [f"depot{i}" for i in range(1, num_depots + 1)]

    init_facts = [f"(next level{i} level{i - 1})" for i in range(1, max_level + 1)]
    init_facts.extend(f"(ready-to-load {g} {m} level0)" for g in goods for m in markets)
    init_facts.extend(f"(stored {g} level0)" for g in goods)
    init_facts.extend(f"(loaded {g} {t} level0)" for g in goods for t in trucks)
    init_facts.extend(
        f"(connected {markets[i]} {markets[j]})"
        for i in range(num_markets)
        for j in range(num_markets)
        if i != j and frozenset((i, j)) in edges
    )
    for depot, market in zip(depots, depot_markets):
        init_facts.extend((f"(connected {depot} {markets[market]})", f"(connected {markets[market]} {depot})"))
    init_facts.extend(
        f"(on-sale {goods[p]} {markets[m]} level{on_sale[m][p]})" for m in range(num_markets) for p in range(num_products)
    )
    init_facts.extend(f"(at {truck} {depots[depot]})" for truck, depot in zip(trucks, truck_depots))
    goal_facts = [f"(stored {g} level{level})" for g, level in zip(goods, goals)]

    return (f"""(define (problem tpp-p{num_products}-m{num_markets}-t{num_trucks}-d{num_depots}-l{max_level})
  (:domain TPP-Propositional)
  (:objects
    {' '.join(goods)} - goods
    {' '.join(trucks)} - truck
    {' '.join(markets)} - market
    {' '.join(depots)} - depot
    {' '.join(f"level{i}" for i in range(max_level + 1))} - level
  )
  (:init
{chr(10).join(f"    {fact}" for fact in init_facts)}
  )
  (:goal
    (and
{chr(10).join(f"      {goal}" for goal in goal_facts)}
    )
  )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a TPP PDDL problem (gen-TPP distribution).")
    parser.add_argument("-p", "--num-products", type=int, required=True)
    parser.add_argument("-m", "--num-markets", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-d", "--num-depots", type=int, required=True)
    parser.add_argument("-l", "--max-level", type=int, required=True, help="maximum goods level")
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
