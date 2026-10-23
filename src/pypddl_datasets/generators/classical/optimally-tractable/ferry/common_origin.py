#!/usr/bin/env python3
"""Ferry where all cars start at the same location.

Optimal cost: each of the k cars costs board + sail + debark, plus k - 1 empty sails
back to the origin, plus one empty sail to the origin if the ferry starts elsewhere.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_cars: int, num_locations: int, seed: int | None = None) -> str:
    if num_cars < 1:
        raise ValueError("num_cars must be at least 1")
    if num_locations < 2:
        raise ValueError("num_locations must be at least 2")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cars = [f"c{i}" for i in range(num_cars)]
    locations = [f"l{i}" for i in range(num_locations)]
    origin = rng.randrange(num_locations)
    destinations = [rng.choice([i for i in range(num_locations) if i != origin]) for _ in cars]
    ferry = rng.randrange(num_locations)
    cost = 4 * num_cars - 1 + (ferry != origin)
    init = [
        *(f"(location {location})" for location in locations),
        *(f"(car {car})" for car in cars),
        *(f"(not-eq {left} {right})" for left in locations for right in locations if left != right),
        "(empty-ferry)",
        f"(at-ferry l{ferry})",
        *(f"(at {car} l{origin})" for car in cars),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem ferry-common-origin-l{num_locations}-c{num_cars})
  (:domain ferry)
  (:objects {' '.join([*locations, *cars])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at {car} l{destination})' for car, destination in zip(cars, destinations))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Ferry task with all cars at one location.")
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
