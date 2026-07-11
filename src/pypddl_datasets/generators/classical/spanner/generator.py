#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(
    num_spanners: int,
    num_nuts: int,
    num_locations: int,
    seed: int | None = None,
    name: str = "prob",
) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    spanners = [f"spanner{i}" for i in range(1, num_spanners + 1)]
    nuts = [f"nut{i}" for i in range(1, num_nuts + 1)]
    locations = [f"location{i}" for i in range(1, num_locations + 1)]

    init_facts = ["    (at bob shed)"]
    for spanner in spanners:
        init_facts.append(f"    (at {spanner} {rng.choice(locations)})")
        init_facts.append(f"    (useable {spanner})")
    for nut in nuts:
        init_facts.append(f"    (loose {nut})")
        init_facts.append(f"    (at {nut} gate)")
    init_facts.append(f"    (link shed {locations[0]})")
    init_facts.extend(
        f"    (link {left} {right})" for left, right in zip(locations, locations[1:])
    )
    init_facts.append(f"    (link {locations[-1]} gate)")

    goals = "\n".join(f"      (tightened {nut})" for nut in nuts)

    return f"""(define (problem {name})
  (:domain spanner)
  (:objects
    bob - man
    {' '.join(spanners)} - spanner
    {' '.join(nuts)} - nut
    {' '.join(locations)} shed gate - location
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{goals}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Spanner PDDL problem.")
    parser.add_argument("num_spanners", type=int, help="number of spanners")
    parser.add_argument("num_nuts", type=int, help="number of nuts")
    parser.add_argument("num_locations", type=int, help="number of locations")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    parser.add_argument("-n", "--problem-name", default="prob")
    args = parser.parse_args(argv)

    if args.num_spanners < 1:
        parser.error("num_spanners must be at least 1")
    if args.num_nuts < 1:
        parser.error("num_nuts must be at least 1")
    if args.num_nuts > args.num_spanners:
        parser.error("num_nuts must not exceed num_spanners")
    if args.num_locations < 1:
        parser.error("num_locations must be at least 1")

    print(
        make_problem(
            args.num_spanners,
            args.num_nuts,
            args.num_locations,
            args.seed,
            args.problem_name,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
