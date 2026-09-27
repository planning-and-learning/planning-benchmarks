#!/usr/bin/env python3
# Reconstruction of the IPC 2023 numeric Market Trader tasks (no generator was
# published): 17 fixed goods, one camel, markets on a connected symmetric road map;
# per-good price and supply ranges measured from the reference tasks.

from __future__ import annotations

import argparse
import random
import sys

# (good, min price, max price, P(on-sale = 0), min on-sale, max on-sale), from the tasks.
GOODS = (
    ("Food", 2.0, 7.6, 0.0, 6, 20),
    ("ExpensiveRugs", 5.2, 8.0, 0.0, 10, 17),
    ("Coffee", 17.6, 26.0, 0.0, 2, 23),
    ("Cattle", 2.0, 16.0, 0.8, 5, 5),
    ("Water", 19.2, 33.2, 0.19, 5, 30),
    ("Cars", 78.3, 100.8, 0.2, 6, 54),
    ("GummyBears", 3.2, 94.0, 0.46, 8, 61),
    ("Computers", 61.6, 100.8, 0.56, 14, 56),
    ("LaminateFloor", 46.8, 63.6, 0.2, 4, 40),
    ("Copper", 31.2, 34.0, 0.0, 10, 17),
    ("Footballs", 49.6, 86.0, 0.73, 3, 29),
    ("Kittens", 45.2, 70.3, 0.57, 9, 27),
    ("Minerals", 10.0, 12.8, 0.0, 53, 60),
    ("Gold", 36.0, 38.8, 0.0, 2, 9),
    ("Platinum", 62.8, 68.3, 0.0, 1, 63),
    ("DVDs", 15.2, 18.0, 0.8, 1, 1),
    ("TuringMachines", 21.2, 63.2, 1.0, 0, 0),
)
MARKET_NAMES = (
    "Amsterdam", "Athens", "Berlin", "Bonn", "Brussels", "Cardiff", "Cesis", "Copenhagen", "Daugai",
    "Daugavpils", "Douglas", "Dublin", "Dusetos", "Edinburgh", "Gelgaudiskis", "Hamburg", "Jelgava",
    "Jieznas", "Jurmala", "Kadagopya", "Kaunas", "Kavarskas", "KudirkosNaumiestis", "Lisbon", "London",
    "Longyearbyen", "Madrid", "Mandres", "Mariehamn", "Moscow", "Narva", "Neringa", "Nice", "Obeliai",
    "Ogre", "Oslo", "Palanga", "Panemune", "Paris", "Rakvere", "Riga", "Rome", "Salaspils", "Seda",
    "Simnas", "Sough", "StPetersburg", "Stockholm", "Tallinn", "Tartu", "Thule", "Torshavn", "Tukums",
    "Valencia", "Valmiera", "Venice", "Vienna", "Viljandi", "Vilkija",
)
EXTRA_ROAD_PROBABILITY = 0.5
MISSING_GOODS_PROBABILITY = 0.1  # a market lacks Kittens and Gold (and sometimes Copper), as in 5 of 70
MAX_ATTEMPTS = 1000


def _profitable(markets, roads, prices, on_sale) -> bool:
    """Some good sells for more at a neighbour than it costs, with profit covering the round trip."""
    for (a, b), cost in roads.items():
        for good in on_sale:
            if (good, a) in prices and (good, b) in prices and on_sale[good].get(a, 0) > 0:
                buy, sell = prices[good, a], prices[good, b]
                if buy + 7 <= 100 and 20 * (sell - buy) > 2 * cost:
                    return True
    return False


def make_problem(num_markets: int, seed: int | None = None) -> str:
    """Generate a Market Trader task with ``num_markets`` markets.

    Roads form a random spanning tree plus every other pair with probability 0.5,
    symmetric, with drive costs uniform in 0.8..7.0 (one decimal). Prices are
    uniform per good over its reference range (one decimal); supply is 0 with the
    good's reference probability, else uniform over its reference range. The camel
    starts at the last market with cash 100, capacity 20 and fuel 7; the goal is
    cash 1000. Draws are repeated until a profitable trade exists, so buying low
    and selling high repeatedly reaches the goal.
    """
    if not isinstance(num_markets, int) or isinstance(num_markets, bool) or not 2 <= num_markets <= len(MARKET_NAMES):
        raise ValueError(f"num_markets must be an integer in 2..{len(MARKET_NAMES)}")
    rng = random.Random(seed)
    for _ in range(MAX_ATTEMPTS):
        markets = rng.sample(MARKET_NAMES, num_markets)
        order = markets[:]
        rng.shuffle(order)
        pairs = {tuple(sorted((order[i], order[rng.randrange(i)]))) for i in range(1, num_markets)}
        pairs |= {
            (a, b) for i, a in enumerate(sorted(markets)) for b in sorted(markets)[i + 1:]
            if (a, b) not in pairs and rng.random() < EXTRA_ROAD_PROBABILITY
        }
        roads = {}
        for a, b in sorted(pairs):
            roads[a, b] = roads[b, a] = rng.randint(8, 70) / 10
        prices, on_sale = {}, {}
        for market in markets:
            missing = set()
            if rng.random() < MISSING_GOODS_PROBABILITY:
                missing = {"Kittens", "Gold"} | ({"Copper"} if rng.random() < 1 / 3 else set())
            for good, low, high, zero, sale_low, sale_high in GOODS:
                if good in missing:
                    continue
                prices[good, market] = rng.randint(round(10 * low), round(10 * high)) / 10
                on_sale.setdefault(good, {})[market] = 0 if rng.random() < zero else rng.randint(sale_low, sale_high)
        if _profitable(markets, roads, prices, on_sale):
            break
    else:
        raise ValueError(f"no profitable market draw in {MAX_ATTEMPTS} attempts")

    init = []
    for market in markets:
        for good, *_ in GOODS:
            if (good, market) in prices:
                init.append(f"        (= (price {good} {market})    {prices[good, market]})")
                init.append(f"        (= (on-sale {good} {market})  {on_sale[good][market]})")
        init.append("")
    init += [f"        (= (bought {good}) 0)" for good, *_ in GOODS]
    for (a, b), cost in roads.items():
        init.append(f"        (= (drive-cost {a} {b}) {cost})")
        init.append(f"        (can-drive {a} {b})")
    init += [
        f"        (at camel0 {markets[-1]})",
        "        (= (cash) 100)",
        "        (= (capacity) 20)",
        "        (= (fuel-used) 0)",
        "        (= (fuel) 7.0)",
    ]
    return (f"""(define (problem marketcount{num_markets})
(:domain trader)
(:objects
        {' '.join(markets)} - market
        camel0 - camel
        {' '.join(good for good, *_ in GOODS)} - goods)
(:init
{chr(10).join(init)}
)
(:goal (and
        (>= (cash) 1000)
))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Market Trader PDDL problem.")
    parser.add_argument("-m", "--num-markets", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_markets, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
