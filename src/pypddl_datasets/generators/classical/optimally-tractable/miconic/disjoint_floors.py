#!/usr/bin/env python3
"""Miconic where no floor is both an origin and a destination.

The lift reaches any floor in one move. Each passenger costs board + depart, every
origin floor must be visited, and every destination floor must be visited after
some origin. So at least |origins| + |destinations| moves are needed, one less if
the lift starts at an origin floor; visiting all origins and then all
destinations meets that bound.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def _problem(name: str, num_floors: int, lift: int, trips: list[tuple[int, int]]) -> str:
    origins = {origin for origin, _ in trips}
    cost = 2 * len(trips) + len(origins) + len({destination for _, destination in trips}) - (lift in origins)
    passengers = [f"p{i}" for i in range(len(trips))]
    floors = [f"f{i}" for i in range(num_floors)]
    init = [
        *(f"(passenger {passenger})" for passenger in passengers),
        *(f"(floor {floor})" for floor in floors),
        *(f"(above f{i} f{j})" for i in range(num_floors) for j in range(i + 1, num_floors)),
        *(f"(origin {p} f{origin})\n    (destin {p} f{destin})" for p, (origin, destin) in zip(passengers, trips)),
        f"(lift-at f{lift})",
    ]
    return f"""; optimal plan cost: {cost}
(define (problem {name}-f{num_floors}-p{len(trips)})
  (:domain miconic)
  (:objects {' '.join([*passengers, *floors])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (served {passenger})' for passenger in passengers)}
    )
  )
)
"""


def make_problem(num_floors: int, num_passengers: int, seed: int | None = None) -> str:
    if num_floors < 2:
        raise ValueError("num_floors must be at least 2")
    if num_passengers < 1:
        raise ValueError("num_passengers must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    floors = rng.sample(range(num_floors), num_floors)
    split = rng.randint(1, num_floors - 1)
    origins, destinations = floors[:split], floors[split:]
    trips = [(rng.choice(origins), rng.choice(destinations)) for _ in range(num_passengers)]
    return _problem("miconic-disjoint", num_floors, rng.randrange(num_floors), trips)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Miconic task with disjoint origin and destination floors.")
    parser.add_argument("-f", "--num-floors", type=int, required=True)
    parser.add_argument("-p", "--num-passengers", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_floors, args.num_passengers, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
