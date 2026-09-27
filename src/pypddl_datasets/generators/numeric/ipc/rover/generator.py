#!/usr/bin/env python3
# Port of pddl-generators rovers/rovgen.cc in numeric mode (`rovgen -n`), the
# generator of the IPC 2002 numeric tasks: the STRIPS task of classical/ipc/rovers
# (same pre-2021 rovgen, IPC visibility) plus sunny waypoints, energy and the
# recharges metric, written in the IPC 2023 encoding (`in` for rover positions).

from __future__ import annotations

import argparse
import random
import re
import sys

from pypddl_datasets.generators.classical.ipc.rovers.generator import make_problem as make_strips_problem

ENERGY = 50


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    num_rovers: int,
    num_waypoints: int,
    num_objectives: int,
    num_cameras: int,
    num_goals: int,
    seed: int | None = None,
) -> str:
    """Generate a numeric Rovers task.

    Everything but energy follows the IPC STRIPS generator (classical/ipc/rovers).
    Each waypoint is in the sun with probability 0.3; like upstream
    ``makeChargeable``, a rover none of whose traversal sources is sunny gets the
    source of a random traversal made sunny. Every rover starts with 50 energy
    (navigating costs 8); the metric minimises ``recharges``.
    """
    for name, value, minimum in (
        ("num_rovers", num_rovers, 1),
        ("num_waypoints", num_waypoints, 2),
        ("num_objectives", num_objectives, 1),
        ("num_cameras", num_cameras, 1),
        ("num_goals", num_goals, 1),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    strips = make_strips_problem(num_rovers, num_waypoints, num_objectives, num_cameras, num_goals, seed=seed)
    rng = random.Random(seed)
    sunny = {w for w in range(num_waypoints) if rng.randrange(10) < 3}
    travs: dict[str, list[int]] = {}
    for rover, source in re.findall(r"\(can_traverse (rover\d+) waypoint(\d+) waypoint\d+\)", strips):
        travs.setdefault(rover, []).append(int(source))
    for rover in sorted(travs, key=lambda r: int(r[5:])):
        if not sunny & set(travs[rover]):
            sunny.add(rng.choice(travs[rover]))

    problem = re.sub(r"\(at (rover\d+) ", r"(in \1 ", strips)
    numeric = ["(= (recharges) 0)", *(f"(in_sun waypoint{w})" for w in sorted(sunny))]
    numeric += [f"(= (energy rover{r}) {ENERGY})" for r in range(num_rovers)]
    head, tail = problem.split("(:init", 1)
    problem = head + "(:init\n    " + "\n    ".join(numeric) + tail
    return problem.rstrip()[:-1].rstrip() + "\n  (:metric minimize (recharges))\n)\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Rovers PDDL problem.")
    parser.add_argument("-r", "--num-rovers", type=int, required=True)
    parser.add_argument("-w", "--num-waypoints", type=int, required=True)
    parser.add_argument("-o", "--num-objectives", type=int, required=True)
    parser.add_argument("-c", "--num-cameras", type=int, required=True)
    parser.add_argument("-g", "--num-goals", type=int, required=True)
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
