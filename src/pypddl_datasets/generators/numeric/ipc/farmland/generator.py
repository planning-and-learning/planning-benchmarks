#!/usr/bin/env python3
# Port of hstairs/planning-numeric-domains-generators farmland/farmlandgenerator.py
# (Enrico Scala), ladder-graph mode as used for all IPC 2023 Farmland and FO-Farmland
# tasks, with the IPC additions: (= (cost) 0), and for FO-Farmland (= (num-of-cars) 0)
# and the cost-penalised reward bound.

from __future__ import annotations

import argparse
import random
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _ladder_edges(num_farms: int) -> list[tuple[int, int]]:
    """networkx.ladder_graph(num_farms // 2): two paths 0..k-1 and k..2k-1 plus rungs i -- i+k."""
    k = num_farms // 2
    rails = [(i, i + 1) for i in range(k - 1)] + [(k + i, k + i + 1) for i in range(k - 1)]
    edges = rails + [(i, i + k) for i in range(k)]
    return edges


def build(num_farms: int, num_units: int, seed: int | None, first_order: bool) -> str:
    for name, value, minimum in (("num_farms", num_farms, 2), ("num_units", num_units, 1)):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_farms % 2:
        raise ValueError("num_farms must be even (ladder graph)")

    rng = random.Random(seed)
    farms = [f"farm{i}" for i in range(num_farms)]
    source = rng.randint(0, num_farms - 1)
    units: list[int] = []
    weights: list[str] = []
    for i in range(num_farms):
        if i == source:
            units.append(num_units)
            weights.append("1.0")
        else:
            units.append(rng.randint(0, 1))
            weights.append(f"{rng.random() + 1.0:.1f}")
    neighbours: dict[int, list[int]] = {i: [] for i in range(num_farms)}
    for a, b in _ladder_edges(num_farms):
        neighbours[a].append(b)
        neighbours[b].append(a)

    init = [f"\t\t(= (x {f}) {u})" for f, u in zip(farms, units)]
    init.append("\t\t")
    init += [f"\t\t(adj {farms[i]} {farms[j]})" for i in range(num_farms) for j in sorted(neighbours[i])]
    init.append("\t\t")
    init.append("\t\t(= (cost) 0)")
    reward = "".join(f"(+ (* {w} (x {f}))" for w, f in zip(weights, farms)) + " 0" + ")" * num_farms
    if first_order:
        reward = f"(- {reward} (cost))"
    bound = f"{round(num_units * 1.4, 1)}"
    goals = "\n".join(f"\t\t\t(>= (x {f}) 1)" for f in farms)
    extra = "\t\t(= (num-of-cars) 0)\n" if first_order else ""
    return (f"""(define (problem instance_{num_farms}_{num_units}_{seed}_ladder)
\t(:domain {"farmland_ln" if first_order else "farmland"})
\t(:objects
\t\t{' '.join(farms)} - farm
\t)
  (:init
{extra}{chr(10).join(init)}
\t)
\t(:goal
\t\t(and
{goals}
\t\t\t(>= {reward} {bound})
\t\t)
\t)
)
""").lower()


def make_problem(num_farms: int, num_units: int, seed: int | None = None) -> str:
    """Generate a Farmland task on a ladder graph of ``num_farms`` farms.

    A uniformly chosen source farm holds ``num_units`` workers and weight 1.0;
    every other farm starts with 0 or 1 workers and a weight uniform in
    1.0..2.0 (one decimal). Goal: every farm has a worker and the weighted
    reward reaches 1.4 * num_units.
    """
    return build(num_farms, num_units, seed, first_order=False)


def main(argv: list[str] | None = None, first_order: bool = False) -> int:
    prefix = "FO-" if first_order else ""
    parser = argparse.ArgumentParser(description=f"Generate a numeric {prefix}Farmland PDDL problem.")
    parser.add_argument("-f", "--num-farms", type=int, required=True, help="number of farms (even)")
    parser.add_argument("-u", "--num-units", type=int, required=True, help="workers on the source farm")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = build(args.num_farms, args.num_units, args.seed, first_order)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
