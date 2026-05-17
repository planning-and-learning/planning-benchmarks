#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(
    num_couples: int,
    num_cars: int,
    num_places: int,
    seed: int | None = None,
) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    cars = [f"car{i}" for i in range(num_cars)]
    tents = [f"tent{i}" for i in range(num_couples)]
    couples = [f"couple{i}" for i in range(num_couples)]
    places = [f"place{i}" for i in range(num_places)]
    people = [name for i in range(num_couples) for name in (f"guy{i}", f"girl{i}")]

    init_facts = []
    for i in range(num_couples):
        tent_state = "up" if rng.randint(1, 2) == 2 else "down"
        init_facts.extend(
            [
                f"    (partner_of couple{i} guy{i})",
                f"    (partner_of couple{i} girl{i})",
                f"    (at_person guy{i} place0)",
                f"    (at_person girl{i} place0)",
                f"    (walked couple{i} place0)",
                f"    (at_tent tent{i} place0)",
                f"    ({tent_state} tent{i})",
            ]
        )

    init_facts.extend(f"    (at_car {car} place0)" for car in cars)
    init_facts.extend(
        f"    (next place{i} place{i + 1})" for i in range(num_places - 1)
    )
    goals = [
        f"      (walked couple{i} place{num_places - 1})"
        for i in range(num_couples)
    ]

    return f"""(define (problem hiking-binary-{num_couples}-{num_cars}-{num_places})
  (:domain hiking-binary)
  (:objects
    {" ".join(cars)} - car
    {" ".join(tents)} - tent
    {" ".join(couples)} - couple
    {" ".join(places)} - place
    {" ".join(people)} - person
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
    parser = argparse.ArgumentParser(description="Generate a Hiking Binary PDDL problem.")
    parser.add_argument("num_couples", type=int, help="number of couples")
    parser.add_argument("num_cars", type=int, help="number of cars")
    parser.add_argument("num_places", type=int, help="number of places")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.num_couples < 1:
        parser.error("num_couples must be at least 1")
    if args.num_cars < args.num_couples + 1:
        parser.error("num_cars must be at least num_couples + 1")
    if args.num_places < 2:
        parser.error("num_places must be at least 2")

    print(
        make_problem(args.num_couples, args.num_cars, args.num_places, args.seed),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
