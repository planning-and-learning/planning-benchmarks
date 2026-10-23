#!/usr/bin/env python3
"""Ferry as in IPC: cars at random locations with random goal locations.

The ferry holds one car and sails between any two locations in one action. Every
misplaced car costs board + sail + debark; the remaining cost is empty sails. The
loaded sails form the edges o -> d of a directed multigraph, and an optimal plan
covers them with as few trails as possible, the first one starting at the ferry.
Adding a dummy edge X -> ferry, the minimum trail cover of each weakly connected
component C is max(1, sum over v in C of max(0, out(v) - in(v))), and the empty
sails number one less than the total. Unloading a car on the way never helps: it
costs a debark, a board and a sail, and saves at most one empty sail.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def optimal_cost(ferry: int, trips: list[tuple[int, int]]) -> int:
    """Optimal plan cost for the ferry at location ``ferry`` and cars to move origin -> destination."""
    trips = [(origin, destination) for origin, destination in trips if origin != destination]
    edges = [(-1, ferry), *trips]  # -1 is the dummy vertex X
    parent: dict[int, int] = {}

    def find(vertex: int) -> int:
        while parent.setdefault(vertex, vertex) != vertex:
            vertex = parent[vertex]
        return vertex

    balance: dict[int, int] = {}
    for origin, destination in edges:
        parent[find(origin)] = find(destination)
        balance[origin] = balance.get(origin, 0) + 1
        balance[destination] = balance.get(destination, 0) - 1
    surplus: dict[int, int] = {}
    for vertex, value in balance.items():
        surplus[find(vertex)] = surplus.get(find(vertex), 0) + max(0, value)
    trails = sum(max(1, value) for value in surplus.values())
    return 3 * len(trips) + trails - 1


def make_problem(num_cars: int, num_locations: int, seed: int | None = None) -> str:
    if num_cars < 1:
        raise ValueError("num_cars must be at least 1")
    if num_locations < 2:
        raise ValueError("num_locations must be at least 2")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cars = [f"c{i}" for i in range(num_cars)]
    locations = [f"l{i}" for i in range(num_locations)]
    trips = [(rng.randrange(num_locations), rng.randrange(num_locations)) for _ in cars]
    ferry = rng.randrange(num_locations)
    init = [
        *(f"(location {location})" for location in locations),
        *(f"(car {car})" for car in cars),
        *(f"(not-eq {left} {right})" for left in locations for right in locations if left != right),
        "(empty-ferry)",
        f"(at-ferry l{ferry})",
        *(f"(at {car} l{origin})" for car, (origin, _) in zip(cars, trips)),
    ]
    return f"""; optimal plan cost: {optimal_cost(ferry, trips)}
(define (problem ferry-unrestricted-l{num_locations}-c{num_cars})
  (:domain ferry)
  (:objects {' '.join([*locations, *cars])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at {car} l{destination})' for car, (_, destination) in zip(cars, trips))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Ferry task.")
    parser.add_argument("-c", "--num-cars", type=int, required=True)
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_cars, args.num_locations, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
