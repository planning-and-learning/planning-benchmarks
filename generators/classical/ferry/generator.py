#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_cars: int, num_locations: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    cars = [f"c{i}" for i in range(num_cars)]
    locations = [f"l{i}" for i in range(num_locations)]

    car_origins = [rng.randrange(num_locations) for _ in cars]
    car_destinations = [rng.randrange(num_locations) for _ in cars]
    ferry_origin = rng.randrange(num_locations)

    objects = " ".join([*locations, *cars])
    location_facts = "\n".join(f"    (location {location})" for location in locations)
    car_facts = "\n".join(f"    (car {car})" for car in cars)
    not_eq_facts = "\n".join(
        f"    (not-eq {left} {right})\n    (not-eq {right} {left})"
        for i, left in enumerate(locations)
        for right in locations[i + 1 :]
    )
    origin_facts = "\n".join(
        f"    (at {car} l{origin})" for car, origin in zip(cars, car_origins)
    )
    goal_facts = "\n".join(
        f"      (at {car} l{destination})"
        for car, destination in zip(cars, car_destinations)
    )

    init_parts = [
        location_facts,
        car_facts,
        not_eq_facts,
        "    (empty-ferry)",
        origin_facts,
        f"    (at-ferry l{ferry_origin})",
    ]
    init = "\n".join(part for part in init_parts if part)

    return f"""(define (problem ferry-l{num_locations}-c{num_cars})
  (:domain ferry)
  (:objects {objects})
  (:init
{init}
  )
  (:goal
    (and
{goal_facts}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Ferry PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True, help="number of locations")
    parser.add_argument("-c", "--num-cars", type=int, required=True, help="number of cars")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.num_locations < 1:
        parser.error("num_locations must be at least 1")
    if args.num_cars < 0:
        parser.error("num_cars must be non-negative")

    print(make_problem(args.num_cars, args.num_locations, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
