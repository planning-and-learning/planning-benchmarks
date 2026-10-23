#!/usr/bin/env python3
"""Nomystery with one truck and one package, on a random road network with fuel costs.

The state is the truck's location and fuel level and where the package is, so there
are at most locations * fuel levels * (locations + 1) states; a breadth-first search
over them (every action costs 1) gives the optimal cost. Tasks are resampled until
the fuel suffices.
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from collections import deque


def optimal_cost(
    roads: dict[tuple[int, int], int], truck: int, fuel: int, package: int, goal: int
) -> int | None:
    """Fewest actions to bring the package from ``package`` to ``goal``; -1 stands for "in the truck"."""
    start = (truck, fuel, package)
    seen = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        here, left, where = state
        if where == goal:
            return seen[state]
        successors = [(b, left - cost, where) for (a, b), cost in roads.items() if a == here and cost <= left]
        if where == here:
            successors.append((here, left, -1))
        if where == -1:
            successors.append((here, left, here))
        for successor in successors:
            if successor not in seen:
                seen[successor] = seen[state] + 1
                queue.append(successor)
    return None


def make_problem(num_locations: int, max_fuel: int, extra_roads: int = 2, seed: int | None = None) -> str:
    if num_locations < 2:
        raise ValueError("num_locations must be at least 2")
    if max_fuel < 1:
        raise ValueError("max_fuel must be at least 1")
    if extra_roads < 0:
        raise ValueError("extra_roads must be at least 0")
    rng = random.Random(seed if seed is not None else int(time.time()))
    while True:
        roads: dict[tuple[int, int], int] = {}
        pairs = [(rng.randrange(node), node) for node in range(1, num_locations)]
        for _ in range(extra_roads):
            u, v = rng.sample(range(num_locations), 2)
            pairs.append((u, v))
        for u, v in pairs:
            roads[u, v] = roads[v, u] = rng.randint(1, 3)
        truck, fuel = rng.randrange(num_locations), rng.randint(1, max_fuel)
        package, goal = rng.sample(range(num_locations), 2)
        cost = optimal_cost(roads, truck, fuel, package, goal)
        if cost is not None:
            break

    levels = [f"level{i}" for i in range(max_fuel + 1)]
    init = [
        "(= (total-cost) 0)",
        *(f"(sum level{a} level{b} level{a + b})" for a in range(max_fuel + 1) for b in range(max_fuel + 1 - a)),
        *(f"(connected l{u} l{v})\n    (fuelcost level{cost} l{u} l{v})" for (u, v), cost in sorted(roads.items())),
        f"(at t0 l{truck})",
        f"(fuel t0 level{fuel})",
        f"(at p0 l{package})",
    ]
    return f"""; optimal plan cost: {cost}
(define (problem nomystery-single-package-l{num_locations}-f{max_fuel})
  (:domain transport-strips)
  (:objects
    {' '.join(f'l{i}' for i in range(num_locations))} - location
    {' '.join(levels)} - fuellevel
    t0 - truck
    p0 - package
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
      (at p0 l{goal})
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a single-package Nomystery task.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-f", "--max-fuel", type=int, required=True)
    parser.add_argument("-e", "--extra-roads", type=int, default=2)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_locations, args.max_fuel, args.extra_roads, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
