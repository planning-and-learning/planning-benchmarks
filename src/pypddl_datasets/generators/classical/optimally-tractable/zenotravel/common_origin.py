#!/usr/bin/env python3
"""Zenotravel with one plane and all people starting in the same city.

At unit cost a zoom (one action, two fuel levels) never beats a fly (one action,
one level), and refuelling adds one level per action anywhere. With m flights, the
optimal cost is 2 per person (board + debark) + m + max(0, m - initial fuel), where
m is one flight to the origin unless the plane is there plus one per destination city.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

NUM_FUEL_LEVELS = 7


def _problem(name: str, num_cities: int, plane: int, fuel: int, trips: list[tuple[int, int]], flights: int) -> str:
    people = [f"person{i}" for i in range(len(trips))]
    cities = [f"city{i}" for i in range(num_cities)]
    levels = [f"fl{i}" for i in range(NUM_FUEL_LEVELS)]
    init = [
        "(aircraft plane0)",
        f"(at plane0 city{plane})",
        f"(fuel-level plane0 fl{fuel})",
        *(f"(person {p})\n    (at {p} city{origin})" for p, (origin, _) in zip(people, trips)),
        *(f"(city {city})" for city in cities),
        *(f"(next {a} {b})" for a, b in zip(levels, levels[1:])),
        *(f"(flevel {level})" for level in levels),
    ]
    cost = 2 * len(trips) + flights + max(0, flights - fuel)
    return f"""; optimal plan cost: {cost}
(define (problem {name}-c{num_cities}-p{len(trips)})
  (:domain zeno-travel)
  (:objects plane0 {' '.join([*people, *cities, *levels])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at {p} city{destination})' for p, (_, destination) in zip(people, trips))}
    )
  )
)
"""


def make_problem(num_cities: int, num_people: int, seed: int | None = None) -> str:
    if num_cities < 2:
        raise ValueError("num_cities must be at least 2")
    if num_people < 1:
        raise ValueError("num_people must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    origin, plane, fuel = rng.randrange(num_cities), rng.randrange(num_cities), rng.randrange(NUM_FUEL_LEVELS)
    trips = [(origin, rng.choice([c for c in range(num_cities) if c != origin])) for _ in range(num_people)]
    flights = (plane != origin) + len({d for _, d in trips})
    return _problem("zenotravel-common-origin", num_cities, plane, fuel, trips, flights)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Zenotravel task with all people in one city.")
    parser.add_argument("-c", "--num-cities", type=int, required=True)
    parser.add_argument("-p", "--num-people", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_cities, args.num_people, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
