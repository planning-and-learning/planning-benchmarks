#!/usr/bin/env python3
# Port of pddl-generators zenotravel/zenogenerator.cc in numeric mode
# (`ztravel -n <seed> <cities> <planes> <people> <distance>`), the generator of the
# IPC 2002 numeric tasks, written in the IPC 2023 encoding (`located`, domain
# `zenotravel`).

from __future__ import annotations

import argparse
import random
import sys

METRICS = ("weighted", "fuel")


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    num_cities: int,
    num_planes: int,
    num_people: int,
    seed: int | None = None,
    distance: int = 1000,
    metric: str = "weighted",
) -> str:
    """Generate a numeric Zenotravel task.

    Distances between distinct cities are uniform in ``[distance/2, distance)``.
    Each plane has slow burn 1..5, fuel uniform below ``slow_burn * distance``,
    capacity ``(2.1 + u) * slow_burn * distance``, fast burn ``(2 + 2u) * slow_burn``
    and zoom limit 1..10 (u uniform in [0, 1)). Planes keep a destination goal with
    probability 0.3, people with probability 0.97; destinations may equal the start.
    ``metric="weighted"`` gives upstream's ``w2 * total-time + w1 * total-fuel-used``
    with weights in 1..5, ``"fuel"`` minimises ``total-fuel-used`` (2 of the 20 IPC
    2023 tasks).
    """
    for name, value, minimum in (
        ("num_cities", num_cities, 1),
        ("num_planes", num_planes, 1),
        ("num_people", num_people, 1),
        ("distance", distance, 2),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if metric not in METRICS:
        raise ValueError(f"metric must be one of {', '.join(METRICS)}")

    rng = random.Random(seed)
    half = distance // 2
    path = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            path[i][j] = path[j][i] = rng.randrange(half) + half

    init: list[str] = []
    goals: list[str] = []
    for plane in range(1, num_planes + 1):
        location, destination = rng.randrange(num_cities), rng.randrange(num_cities)
        slow_burn = 1 + rng.randrange(5)
        rng.randrange(100)  # slow speed (temporal modes only)
        fuel = rng.randrange(slow_burn * distance)
        capacity = int((2.1 + rng.random()) * slow_burn * distance)
        rng.random()  # fast speed (temporal modes only)
        fast_burn = int((2.0 + rng.random() * 2.0) * slow_burn)
        rng.randrange(slow_burn * distance)  # refuel rate (complex mode only)
        zoom_limit = 1 + rng.randrange(10)
        interesting = rng.randrange(10) >= 7
        name = f"plane{plane}"
        init += [
            f"\t(located {name} city{location})",
            f"\t(= (capacity {name}) {capacity})",
            f"\t(= (fuel {name}) {fuel})",
            f"\t(= (slow-burn {name}) {slow_burn})",
            f"\t(= (fast-burn {name}) {fast_burn})",
            f"\t(= (onboard {name}) 0)",
            f"\t(= (zoom-limit {name}) {zoom_limit})",
        ]
        if interesting:
            goals.append(f"\t(located {name} city{destination})")
    for person in range(1, num_people + 1):
        location, destination = rng.randrange(num_cities), rng.randrange(num_cities)
        init.append(f"\t(located person{person} city{location})")
        if rng.randrange(100) >= 3:
            goals.append(f"\t(located person{person} city{destination})")
    init += [f"\t(= (distance city{i} city{j}) {path[i][j]})" for i in range(num_cities) for j in range(num_cities)]
    init.append("\t(= (total-fuel-used) 0)")
    if metric == "weighted":
        init.append("\t(= (total-time) 0)")
        w1, w2 = 1 + rng.randrange(5), 1 + rng.randrange(5)
        metric_text = f"(:metric minimize (+ (* {w2} (total-time)) (* {w1} (total-fuel-used))))"
    else:
        metric_text = "(:metric minimize (total-fuel-used))"

    objects = [f"\tplane{i} - aircraft" for i in range(1, num_planes + 1)]
    objects += [f"\tperson{i} - person" for i in range(1, num_people + 1)]
    objects += [f"\tcity{i} - city" for i in range(num_cities)]
    nl = "\n"
    return (f"""(define (problem ztravel-{num_cities}-{num_planes}-{num_people})
(:domain zenotravel)
(:objects
{nl.join(objects)}
\t)
(:init
{nl.join(init)}
)
(:goal (and
{nl.join(goals)}
\t))
{metric_text}
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Zenotravel PDDL problem.")
    parser.add_argument("-c", "--num-cities", type=int, required=True)
    parser.add_argument("-a", "--num-planes", type=int, required=True)
    parser.add_argument("-p", "--num-people", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("-d", "--distance", type=int, default=1000, help="distance bound (default: 1000)")
    parser.add_argument("-m", "--metric", choices=METRICS, default="weighted")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
