#!/usr/bin/env python3
# Port of pddl-generators trucks/trucks.c (gen-Trucks, Yannis Dimopoulos, Alfonso Gerevini and
# Alessandro Saetti), propositional mode, written against the lifted ADL IPC 2006 domain
# (downward-benchmarks/trucks). The STRIPS grounding (trucks-strips.sh) is not applied.

from __future__ import annotations

import argparse
import random
import sys


def make_problem(
    num_trucks: int,
    num_locations: int,
    num_packages: int,
    num_areas: int,
    seed: int | None = None,
    name: int | None = None,
) -> str:
    """Generate a Trucks task.

    Trucks start at uniform locations with all areas free; packages come in
    groups of ``num_areas`` at a uniform location; locations are completely
    connected. Every package must reach a uniform other location. With
    probability 1 - 1/num_areas it must be delivered by a deadline
    ``(delivered p l t)``, otherwise just ``(at-destination p l)``. The
    number of time steps is num_locations * (ceil(num_packages/num_areas)) + 1.
    """
    for label, value, minimum in (
        ("num_trucks", num_trucks, 1),
        ("num_locations", num_locations, 2),
        ("num_packages", num_packages, 1),
        ("num_areas", num_areas, 1),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{label} must be an integer at least {minimum}")

    rng = random.Random(seed)
    num_times = num_locations * ((num_packages - 1) // num_areas + 1) + 1

    init = []
    for truck in range(1, num_trucks + 1):
        init.append(f"(at truck{truck} l{rng.randrange(num_locations) + 1})")
    for truck in range(1, num_trucks + 1):
        init.extend(f"(free a{area} truck{truck})" for area in range(1, num_areas + 1))
    init.extend(f"(closer a{i} a{j})" for i in range(1, num_areas + 1) for j in range(i + 1, num_areas + 1))

    starts: list[int] = []
    while len(starts) < num_packages:
        location = rng.randrange(num_locations) + 1
        for _ in range(num_areas):
            starts.append(location)
            init.append(f"(at package{len(starts)} l{location})")
            if len(starts) == num_packages:
                break
    init.extend(
        f"(connected l{i} l{j})" for i in range(1, num_locations + 1) for j in range(1, num_locations + 1) if i != j
    )
    init.append("(time-now t0)")
    init.extend(f"(le t{i + 1} t{j + 1})" for i in range(num_times - 1) for j in range(i, num_times - 1))

    destinations = []
    for start in starts:
        destination = start
        while destination == start:
            destination = rng.randrange(num_locations) + 1
        destinations.append(destination)
    deadlines = [rng.randrange(num_areas) != 0 for _ in starts]
    init.extend(f"(next t{i} t{i + 1})" for i in range(num_times - 1))

    goals = []
    for i, (destination, deadline) in enumerate(zip(destinations, deadlines)):
        wave = i // num_areas + 1
        time = num_locations * wave if num_locations <= num_areas else (num_areas + 1) * wave
        goals.append(
            f"(delivered package{i + 1} l{destination} t{time})" if deadline else f"(at-destination package{i + 1} l{destination})"
        )

    objects = [
        *(f"truck{i} - truck" for i in range(1, num_trucks + 1)),
        *(f"package{i} - package" for i in range(1, num_packages + 1)),
        *(f"l{i} - location" for i in range(1, num_locations + 1)),
        *(f"t{i} - time" for i in range(num_times)),
        *(f"a{i} - truckarea" for i in range(1, num_areas + 1)),
    ]
    problem = f"truck-{name}" if name is not None else f"truck-t{num_trucks}-l{num_locations}-p{num_packages}-a{num_areas}"
    nl = "\n\t"
    return f"""(define (problem {problem})
(:domain trucks)
(:objects
\t{nl.join(objects)})

(:init
\t{nl.join(init)})

(:goal (and
\t{nl.join(goals)}))
)
""".lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a lifted ADL Trucks PDDL problem.")
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-a", "--num-areas", type=int, required=True)
    parser.add_argument("-n", "--name", type=int, help="problem number (name truck-<n>, as upstream -n)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
