#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(num_floors: int, num_passengers: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    floors = [f"f{i}" for i in range(num_floors)]
    passengers = [f"p{i}" for i in range(num_passengers)]

    init_facts = [
        f"    (above f{i} f{j})"
        for i in range(num_floors - 1)
        for j in range(i + 1, num_floors)
    ]
    for passenger in passengers:
        origin = rng.randrange(num_floors)
        destin = origin
        while num_floors > 1 and destin == origin:
            destin = rng.randrange(num_floors)
        init_facts.append(f"    (origin {passenger} f{origin})")
        init_facts.append(f"    (destin {passenger} f{destin})")
    init_facts.append("    (lift-at f0)")

    goals = [f"      (served {passenger})" for passenger in passengers]

    return f"""(define (problem miconic-f{num_floors}-p{num_passengers})
  (:domain miconic)
  (:objects
    {" ".join(passengers)} - passenger
    {" ".join(floors)} - floor
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Miconic PDDL problem.")
    parser.add_argument("num_floors", type=int, help="number of floors")
    parser.add_argument("num_passengers", type=int, help="number of passengers")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.num_floors < 1:
        parser.error("num_floors must be at least 1")
    if args.num_passengers < 1:
        parser.error("num_passengers must be at least 1")

    print(make_problem(args.num_floors, args.num_passengers, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
