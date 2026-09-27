#!/usr/bin/env python3
# Port of pddl-generators openstacks/generator.py (matrix sampling after Ioannis Refanidis's
# generate_problems), written for the lifted ADL IPC encodings: IPC 2008 `openstacks-{opt,sat}08-adl`
# (domain.pddl, default) and IPC 2006 `openstacks` (domain_openstacks06.pddl, ``style="06"``).

from __future__ import annotations

import argparse
import math
import random
import sys

STYLES = ("08", "06")
MODELS = ("clustered", "uniform")


def _includes(product: int, order: int, num_products: int, density: int, rng: random.Random) -> bool:
    # Upstream's inclusion test: a normal-density weight around the diagonal. randrange(100)
    # may be 0, so every pair has probability >= 1/100 and any matrix can occur.
    d = abs(product - order)
    s = num_products / 6.0
    p = (1 / (s * (2 * math.pi) ** 0.5)) * math.exp(-(d * d) / (2 * s * s))
    chance = p * density * num_products / (2.7 * (num_products / 5.0) ** 0.5)
    return rng.randrange(100) <= chance


def make_problem(
    num_products: int,
    num_orders: int,
    density: int,
    seed: int | None = None,
    style: str = "08",
    shuffle: bool = True,
    model: str = "clustered",
) -> str:
    """Generate an Openstacks task.

    The order/product matrix follows upstream (diagonal-clustered inclusion, every
    order and product used at least once). ``shuffle`` permutes orders and products,
    which upstream only does on copies: the IPC matrices are shuffled. ``density``
    is upstream's density parameter (not a percentage of ones). ``model="uniform"``
    instead includes each product in each order independently with probability
    density/100, which reaches the dense IPC 2006 Challenge matrices (up to 0.54).
    """
    if style not in STYLES:
        raise ValueError(f"style must be one of {', '.join(STYLES)}")
    checks: list[tuple[str, object, int]] = [
        ("num_products", num_products, 1), ("num_orders", num_orders, 1), ("density", density, 0),
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if model not in MODELS:
        raise ValueError(f"model must be one of {', '.join(MODELS)}")
    if density > 100:
        raise ValueError("density must be at most 100")

    rng = random.Random(seed)
    products, orders = range(num_products), range(num_orders)
    if model == "uniform":
        matrix = [[rng.randrange(100) < density for _ in products] for _ in orders]
    else:
        matrix = [[_includes(p, o, num_products, density, rng) for p in products] for o in orders]
    for o in orders:
        if not any(matrix[o]):
            matrix[o][rng.choice(products)] = True
    for p in products:
        if not any(matrix[o][p] for o in orders):
            matrix[rng.choice(orders)][p] = True
    order_ids, product_ids = list(range(1, num_orders + 1)), list(range(1, num_products + 1))
    if shuffle:
        rng.shuffle(order_ids)
        rng.shuffle(product_ids)

    counts = max(num_orders, num_products)
    init = [" ".join(f"(next-count n{i} n{i + 1})" for i in range(counts)), "(stacks-avail n0)"]
    if style == "06":
        init.insert(0, "(machine-available)")
    for o in sorted(orders, key=lambda o: order_ids[o]):
        included = sorted(product_ids[p] for p in products if matrix[o][p])
        init.append(f"(waiting o{order_ids[o]})")
        init.append("".join(f"(includes o{order_ids[o]} p{p})" for p in included))
    if style == "08":
        init.append("(= (total-cost) 0)")

    domain = "openstacks-sequencedstrips" + ("-adl" if style == "08" else "")
    nl = "\n"
    return f"""(define (problem os-sequencedstrips-p{num_products}-o{num_orders}-d{density})
(:domain {domain})
(:objects
{" ".join(f"n{i}" for i in range(counts + 1))} - count
{" ".join(f"o{i}" for i in range(1, num_orders + 1))} - order
{" ".join(f"p{i}" for i in range(1, num_products + 1))} - product
)
(:init
{nl.join(init)}
)
(:goal (and
{nl.join(f"(shipped o{i})" for i in range(1, num_orders + 1))}
))
{"(:metric minimize (total-cost))" + nl if style == "08" else ""})
""".lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a lifted ADL Openstacks PDDL problem.")
    parser.add_argument("num_products", type=int)
    parser.add_argument("num_orders", type=int)
    parser.add_argument("density", type=int, help="upstream density parameter (0-100)")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument(
        "--style", choices=STYLES, default="08",
        help="08: IPC 2008 ADL (domain.pddl), 06: IPC 2006 (domain_openstacks06.pddl)",
    )
    parser.add_argument(
        "--model", choices=MODELS, default="clustered",
        help="clustered: upstream's diagonal model; uniform: iid with probability density/100",
    )
    parser.add_argument(
        "--no-shuffle", dest="shuffle", action="store_false", help="keep upstream's diagonal-clustered order"
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
