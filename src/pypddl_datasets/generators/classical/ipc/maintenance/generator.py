#!/usr/bin/env python3
# Port of pddl-generators maintenance/maintenance.c (Jussi Rintanen, IPC 2014):
# `maintenance <days> <planes> <mechanics> <cities> <visits> [<seed>]`.

from __future__ import annotations

import argparse
import random
import sys

AIRPORTS = ("fra", "ber", "ham")


def make_problem(num_days: int, num_planes: int, num_visits: int, seed: int | None = None) -> str:
    """Generate a maintenance-scheduling task.

    Every plane makes ``num_visits`` visits, each on a uniform day at a uniform
    one of the three airports; repeated (plane, day, airport) draws stay
    duplicated, as upstream and in the IPC tasks. Objects include one day more
    than ``today`` facts (upstream's ``d<days+1>``). Every plane must be done.
    """
    checks: list[tuple[str, object]] = [("num_days", num_days), ("num_planes", num_planes), ("num_visits", num_visits)]
    for name, value in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")

    rng = random.Random(seed)
    visits = [[rng.randrange(num_days), rng.randrange(len(AIRPORTS))] for _ in range(num_planes * num_visits)]
    by_plane: list[list[tuple[int, int]]] = [[] for _ in range(num_planes)]
    for index, (day, airport) in enumerate(visits):
        by_plane[index // num_visits].append((airport, day))

    init = [f"  (today d{day + 1})" for day in range(num_days)]
    for plane, plane_visits in enumerate(by_plane):
        # upstream prints per plane, then airport index, then day
        init.extend(f"  (at ap{plane + 1} d{day + 1} {AIRPORTS[airport]})" for airport, day in sorted(plane_visits))
    goals = "\n".join(f"      (done ap{plane + 1})" for plane in range(num_planes))

    return (f"""(define (problem maintenance-scheduling-1-3-{num_days}-{num_planes}-{num_visits}-{seed})
 (:domain maintenance-scheduling-domain)
 (:objects
   {' '.join(f'd{day + 1}' for day in range(num_days + 1))} - day
   {' '.join(AIRPORTS)} - airport
   {' '.join(f'ap{plane + 1}' for plane in range(num_planes))} - plane)
 (:init
{chr(10).join(init)}
 )
 (:goal
    (and
{goals}
    )
 )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a maintenance-scheduling PDDL problem.")
    parser.add_argument("num_days", type=int)
    parser.add_argument("num_planes", type=int)
    parser.add_argument("num_visits", type=int, help="visits per plane")
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
