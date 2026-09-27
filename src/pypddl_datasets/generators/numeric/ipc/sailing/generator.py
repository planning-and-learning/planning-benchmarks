#!/usr/bin/env python3
# Port of hstairs/planning-numeric-domains-generators sailing/generate_saving.py
# (Enrico Scala). The IPC 2023 Sailing and FO-Sailing tasks draw person distances from
# -max..max (upstream's commented-out line; hence negative d values); the 5-boat
# FO-Sailing tasks use upstream's 0..max (nonnegative_distances). FO-Sailing adds (= (v b) 1).

from __future__ import annotations

import argparse
import random
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def build(
    num_boats: int,
    num_people: int,
    seed: int | None,
    max_distance: int,
    first_order: bool,
    nonnegative_distances: bool = False,
) -> str:
    for name, value, minimum in (
        ("num_boats", num_boats, 1), ("num_people", num_people, 1), ("max_distance", max_distance, 0)
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    people = [f"p{i}" for i in range(num_people)]
    distances = [rng.randint(0 if nonnegative_distances else -max_distance, max_distance) for _ in people]
    boats = [f"b{i}" for i in range(num_boats)]
    boat_facts: list[str] = []
    for boat in boats:
        boat_facts += [f"(= (x {boat}) {rng.randint(-10, 10)})", f"(= (y {boat}) 0)"]
        if first_order:
            boat_facts.append(f"(= (v {boat}) 1)")
    distance_facts = "\n".join(f"(= (d {p}) {d})" for p, d in zip(people, distances))
    goals = "\n".join(f"(saved {p})" for p in people)
    return (f"""(define (problem instance_{num_boats}_{num_people}_{seed})

\t(:domain {"sailing_ln" if first_order else "sailing"})

\t(:objects
\t\t{' '.join(boats)} - boat
\t\t{' '.join(people)} - person
\t)

  (:init
\t\t{chr(10).join(boat_facts)}

\t\t{distance_facts}
\t)

\t(:goal
\t\t(and
\t\t\t{goals}
\t\t)
\t)
)
""").lower()


def make_problem(
    num_boats: int,
    num_people: int,
    seed: int | None = None,
    max_distance: int = 500,
    nonnegative_distances: bool = False,
) -> str:
    """Generate a Sailing task: boats at x uniform in -10..10, y = 0; every person
    at a distance d uniform in -max_distance..max_distance (0..max_distance with
    ``nonnegative_distances``) must be saved."""
    return build(num_boats, num_people, seed, max_distance, False, nonnegative_distances)


def main(argv: list[str] | None = None, first_order: bool = False) -> int:
    prefix = "FO-" if first_order else ""
    parser = argparse.ArgumentParser(description=f"Generate a numeric {prefix}Sailing PDDL problem.")
    parser.add_argument("-b", "--num-boats", type=int, required=True)
    parser.add_argument("-p", "--num-people", type=int, required=True)
    parser.add_argument("-d", "--max-distance", type=int, default=500, help="maximum |d| of a person (default: 500)")
    parser.add_argument("--nonnegative-distances", action="store_true", help="draw d from 0..max-distance")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = build(
            args.num_boats, args.num_people, args.seed, args.max_distance, first_order, args.nonnegative_distances
        )
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
