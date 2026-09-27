#!/usr/bin/env python3
# Port of pddl-generators zenotravel/zenogenerator.cc, STRIPS mode. Defaults match the
# untyped IPC encoding (`ztravel -u ...`); Autoscale calls it typed without distance:
# `ztravel {seed} {cities} {planes} {people}`.

from __future__ import annotations

import argparse
import random
import sys

NUM_FUEL_LEVELS = 7


def make_problem(
    num_cities: int,
    num_planes: int,
    num_people: int,
    seed: int | None = None,
    distance: int = 0,
    typed: bool = False,
) -> str:
    """Generate a STRIPS Zenotravel task.

    Every plane and person starts in a uniformly random city and has a uniformly
    random destination (possibly its start). A plane gets a goal with
    probability 0.3, a person with probability 0.97. Without a distance bound,
    all planes start at the lowest fuel level ``fl0``; with one, a plane with
    burn rate ``b`` in 1..5 starts at ``fl(rnd(b * distance) % 7)``, as upstream.
    ``typed`` selects the typed encoding instead of the IPC's type predicates.
    """
    for name, value, minimum in (
        ("num_cities", num_cities, 1),
        ("num_planes", num_planes, 1),
        ("num_people", num_people, 1),
        ("distance", distance, 0),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    planes = [f"plane{i}" for i in range(1, num_planes + 1)]
    people = [f"person{i}" for i in range(1, num_people + 1)]
    cities = [f"city{i}" for i in range(num_cities)]
    levels = [f"fl{i}" for i in range(NUM_FUEL_LEVELS)]

    init_facts = []
    goals = []
    for plane in planes:
        location, destination = rng.choice(cities), rng.choice(cities)
        fuel = rng.randrange(rng.randint(1, 5) * distance) % NUM_FUEL_LEVELS if distance else 0
        init_facts.append(f"\t(at {plane} {location})")
        if not typed:
            init_facts.append(f"\t(aircraft {plane})")
        init_facts.append(f"\t(fuel-level {plane} fl{fuel})")
        if rng.random() >= 0.7:
            goals.append(f"\t(at {plane} {destination})")
    for person in people:
        location, destination = rng.choice(cities), rng.choice(cities)
        init_facts.append(f"\t(at {person} {location})")
        if not typed:
            init_facts.append(f"\t(person {person})")
        if rng.random() >= 0.03:
            goals.append(f"\t(at {person} {destination})")
    if not typed:
        init_facts.extend(f"\t(city {city})" for city in cities)
    init_facts.extend(f"\t(next {levels[i]} {levels[i + 1]})" for i in range(NUM_FUEL_LEVELS - 1))
    if not typed:
        init_facts.extend(f"\t(flevel {level})" for level in levels)

    def declare(names: list[str], type_name: str) -> list[str]:
        return [f"\t{name} - {type_name}" if typed else f"\t{name}" for name in names]

    objects = [
        *declare(planes, "aircraft"),
        *declare(people, "person"),
        *declare(cities, "city"),
        *declare(levels, "flevel"),
    ]
    return (f"""(define (problem ztravel-c{num_cities}-{num_planes}-{num_people})
(:domain zeno-travel)
(:objects
{chr(10).join(objects)}
\t)
(:init
{chr(10).join(init_facts)}
)
(:goal (and
{chr(10).join(goals)}
\t))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a STRIPS Zenotravel PDDL problem.")
    parser.add_argument("-c", "--num-cities", type=int, required=True)
    parser.add_argument("-a", "--num-planes", type=int, required=True)
    parser.add_argument("-p", "--num-people", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("-d", "--distance", type=int, default=0, help="distance bound; positive values randomize initial fuel (default: 0)")
    parser.add_argument("--typed", action="store_true", help="typed encoding instead of type predicates")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
