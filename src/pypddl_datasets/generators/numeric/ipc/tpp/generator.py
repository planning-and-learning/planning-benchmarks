#!/usr/bin/env python3
# TPP-Metric generator reconstructed from the IPC 2023 numeric tasks
# (data/numeric/ipc2023/tpp, by Enrico Scala and Miquel Ramirez; the domain is the
# IPC 2006 TPP Metric domain by Alfonso Gerevini and Alessandro Saetti). No
# generator for this encoding is published.

from __future__ import annotations

import argparse
import math
import random
import sys

SIZE = 1000  # ponytail: side of the square the places lie in; IPC's map spans ~900-1000
MAX_PRICE, MAX_SALE, P_ON_SALE = 50, 20, 0.525


def make_problem(num_markets: int, num_goods: int, seed: int | None = None, num_depots: int = 1, num_trucks: int = 1) -> str:
    """Generate a TPP-Metric task.

    Places lie uniformly in a 1000 x 1000 square; every ordered pair of places is
    connected, with the Euclidean distance (2 decimals) as drive cost. Each good
    is on sale at each market with probability 0.525, in a quantity uniform in
    1..20 at a price uniform in 1..50 (redrawn until some market sells it); its
    request is uniform in 1..total supply. Trucks start at the first depot and must
    return there after buying every request.
    """
    for name, value in (("num_markets", num_markets), ("num_goods", num_goods), ("num_depots", num_depots), ("num_trucks", num_trucks)):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")
    rng = random.Random(seed)
    markets = [f"market{i + 1}" for i in range(num_markets)]
    depots = [f"depot{i}" for i in range(num_depots)]
    trucks = [f"truck{i}" for i in range(num_trucks)]
    goods = [f"goods{i}" for i in range(num_goods)]

    sale = {}
    for g in goods:
        while True:
            sale[g] = {m: (rng.randint(1, MAX_SALE), rng.randint(1, MAX_PRICE)) for m in markets if rng.random() < P_ON_SALE}
            if sale[g]:
                break
    init = []
    for m in markets:
        for g in goods:
            if m in sale[g]:
                quantity, price = sale[g][m]
                init += [f"\t(= (price {g} {m}) {price})", f"\t(= (on-sale {g} {m}) {quantity})"]
            else:
                init.append(f"\t(= (on-sale {g} {m}) 0)")
    init += [f"\t(loc {t} {depots[0]})" for t in trucks]
    places = depots + markets
    points = {p: (rng.uniform(0, SIZE), rng.uniform(0, SIZE)) for p in places}
    for i, a in enumerate(places):
        for b in places[i + 1 :]:
            cost = f"{math.dist(points[a], points[b]):.2f}"
            init += [f"\t(= (drive-cost {a} {b}) {cost})", f"\t(= (drive-cost {b} {a}) {cost})"]
    for g in goods:
        supply = sum(quantity for quantity, _ in sale[g].values())
        init += [f"\t(= (bought {g}) 0)", f"\t(= (request {g}) {rng.randint(1, supply)})"]
    init.append("\t(= (total-cost) 0)")
    goal = [f"\t(>= (bought {g}) (request {g}))" for g in goods] + [f"\t(loc {t} {depots[0]})" for t in trucks]
    nl = "\n"
    return (f"""(define (problem tpp-m{num_markets}-g{num_goods}-d{num_depots}-t{num_trucks})
(:domain tpp-metric)
(:objects
\t{' '.join(markets)} - market
\t{' '.join(depots)} - depot
\t{' '.join(trucks)} - truck
\t{' '.join(goods)} - goods)
(:init
{nl.join(init)}
\t)

(:goal (and
{nl.join(goal)}))

(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a TPP-Metric PDDL problem.")
    parser.add_argument("-m", "--num-markets", type=int, required=True)
    parser.add_argument("-g", "--num-goods", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("-d", "--num-depots", type=int, default=1)
    parser.add_argument("-t", "--num-trucks", type=int, default=1)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
