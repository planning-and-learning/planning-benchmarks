#!/usr/bin/env python3
# Reconstructed from the IPC 2026 sailing-wind tasks (data/numeric/ipc2026/sailing-wind-{opt,sat});
# no generator was published. Domain by Luigi Bonassi and Carl Hentges.

from __future__ import annotations

import argparse
import math
import random
import sys

# Polar diagram shared by every reference task: speed for angles 0, 15, ..., 180 to the wind.
VMAX = (0, 0.17, 0.3, 0.45, 0.65, 1, 1.49, 1.44, 1.37, 1.26, 1.12, 0.96, 0.8)


def make_problem(
    num_persons: int = 1,
    num_boats: int = 1,
    min_distance: float = 15.0,
    max_distance: float = 100.0,
    inertia: float = 0.5,
    angle_step: int | None = None,
    seed: int | None = None,
    name: str = "test",
) -> str:
    """Generate a sailing-wind task: boats start at the origin at rest, persons must be saved.

    Every person sits at a uniform distance in ``[min_distance, max_distance]`` from the
    origin, in a uniform direction (a multiple of ``angle_step`` degrees if given, like the
    sat tasks' 45). ``inertia`` is the boats' ``r`` (opt tasks 0.5, sat tasks 0.9).
    """
    for label, value in (("num_persons", num_persons), ("num_boats", num_boats)):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{label} must be an integer at least 1")
    if not 0 <= min_distance <= max_distance:
        raise ValueError("need 0 <= min_distance <= max_distance")
    if not 0 <= inertia < 1:
        raise ValueError("inertia must be in [0, 1)")
    if angle_step is not None and not (isinstance(angle_step, int) and 1 <= angle_step <= 360):
        raise ValueError("angle_step must be an integer in [1, 360]")

    rng = random.Random(seed)
    boats = [f"b{i}" for i in range(num_boats)]
    persons = [f"p{i}" for i in range(num_persons)]
    init = []
    for b in boats:
        init += [f"\t(= (vmax_{15 * i} {b}) {v})" for i, v in enumerate(VMAX)]
        init += [f"\t(= (x {b}) 0)", f"\t(= (y {b}) 0)", f"\t(= (r {b}) {inertia})", f"\t(= (v {b}) 0)", f"\t(= (sailing-angle {b}) 0)"]
    for p in persons:
        distance = rng.uniform(min_distance, max_distance)
        angle = rng.randrange(0, 360, angle_step) if angle_step else rng.uniform(0, 360)
        # heading measured from north (+y) clockwise, as the domain's move actions
        x, y = distance * math.sin(math.radians(angle)), distance * math.cos(math.radians(angle))
        init += [f"\t(= (x {p}) {round(x, 1) + 0.0:g})", f"\t(= (y {p}) {round(y, 1) + 0.0:g})"]  # + 0.0: no "-0"
    nl = "\n"
    return (f"""(define (problem {name}) (:domain sailing-wind)
(:objects
    {' '.join(boats)} - boat
    {' '.join(persons)} - person
)

(:init
{nl.join(init)}
)

(:goal (and
{nl.join(f"    (saved {p})" for p in persons)}
))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a sailing-wind PDDL problem.")
    parser.add_argument("-p", "--num-persons", type=int, default=1)
    parser.add_argument("-b", "--num-boats", type=int, default=1)
    parser.add_argument("--min-distance", type=float, default=15.0)
    parser.add_argument("--max-distance", type=float, default=100.0)
    parser.add_argument("-r", "--inertia", type=float, default=0.5)
    parser.add_argument("--angle-step", type=int)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--name", default="test")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
