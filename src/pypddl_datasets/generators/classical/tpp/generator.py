#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(
    num_goods: int,
    num_trucks: int,
    num_markets: int,
    num_depots: int,
    max_level: int,
    seed: int | None = None,
) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    goods = [f"goods{i}" for i in range(num_goods)]
    trucks = [f"truck{i}" for i in range(num_trucks)]
    markets = [f"market{i}" for i in range(num_markets)]
    depots = [f"depot{i}" for i in range(num_depots)]
    levels = [f"level{i}" for i in range(max_level + 1)]

    init_facts = []
    init_facts.extend(
        f"    (next level{i + 1} level{i})" for i in range(max_level)
    )
    places = [*depots, *markets]
    for left in places:
        for right in places:
            if left != right:
                init_facts.append(f"    (connected {left} {right})")
    init_facts.extend(f"    (at {truck} {rng.choice(depots)})" for truck in trucks)

    for item in goods:
        init_facts.append(f"    (stored {item} level0)")
        for truck in trucks:
            init_facts.append(f"    (loaded {item} {truck} level0)")
        for market in markets:
            sale_level = rng.randint(1, max_level)
            init_facts.append(f"    (on-sale {item} {market} level{sale_level})")
            init_facts.append(f"    (ready-to-load {item} {market} level0)")

    goals = [f"      (stored {item} level{max_level})" for item in goods]

    return f"""(define (problem tpp-g{num_goods}-t{num_trucks}-m{num_markets}-d{num_depots}-l{max_level})
  (:domain TPP-Propositional)
  (:objects
    {" ".join(markets)} - market
    {" ".join(depots)} - depot
    {" ".join(trucks)} - truck
    {" ".join(goods)} - goods
    {" ".join(levels)} - level
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a TPP PDDL problem.")
    parser.add_argument("num_goods", type=int, help="number of goods")
    parser.add_argument("num_trucks", type=int, help="number of trucks")
    parser.add_argument("num_markets", type=int, help="number of markets")
    parser.add_argument("num_depots", type=int, help="number of depots")
    parser.add_argument("max_level", type=int, help="maximum quantity level")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.num_goods < 1:
        parser.error("num_goods must be at least 1")
    if args.num_trucks < 1:
        parser.error("num_trucks must be at least 1")
    if args.num_markets < 1:
        parser.error("num_markets must be at least 1")
    if args.num_depots < 1:
        parser.error("num_depots must be at least 1")
    if args.max_level < 1:
        parser.error("max_level must be at least 1")

    print(
        make_problem(
            args.num_goods,
            args.num_trucks,
            args.num_markets,
            args.num_depots,
            args.max_level,
            args.seed,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
