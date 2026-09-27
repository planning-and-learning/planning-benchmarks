#!/usr/bin/env python3
# Numeric Mystery-prime (IPC 2023 numeric track): the IPC 1998 mprime tasks with the
# fuel levels (`province`) and space levels (`planet`) replaced by the numeric
# fluents `locale` and `harmony`. The IPC 2023 tasks are exact translations of the
# IPC 1998 STRIPS tasks, so this translates classical/ipc/mprime, which is fitted
# to those tasks.

from __future__ import annotations

import argparse
import re
import sys

from pypddl_datasets.generators.classical.ipc.mprime.generator import make_problem as make_strips_problem


def _chain_index(pairs: list[tuple[str, str]], members: list[str]) -> dict[str, int]:
    """Position of every member along the successor chain (first element 0)."""
    successor = dict(pairs)
    first = next(m for m in members if m not in set(successor.values()))
    index: dict[str, int] = {}
    current: str | None = first
    while current is not None:
        index[current] = len(index)
        current = successor.get(current)
    return index


def make_problem(
    num_locations: int,
    num_vehicles: int,
    num_cargos: int,
    num_fuel_levels: int,
    num_space_levels: int,
    num_goals: int,
    seed: int | None = None,
) -> str:
    """Generate a numeric Mystery-prime task.

    Map, vehicles, cargos and goals follow classical/ipc/mprime. The fuel at a
    location is ``(locale food)`` = its fuel level's index, the space of a vehicle
    ``(harmony pleasure)`` = its space level's index; the level objects and their
    order facts disappear, objects become typed.
    """
    strips = make_strips_problem(
        num_locations, num_vehicles, num_cargos, num_fuel_levels, num_space_levels, num_goals, seed=seed
    )
    init, goal = strips.split("(:init", 1)[1].split("(:goal", 1)
    facts = re.findall(r"\(([a-z-]+) ([^()\s]+)(?: ([^()\s]+))?\)", init)
    kinds = {
        name: [a for p, a, b in facts if p == name and not b]
        for name in ("food", "pleasure", "pain", "province", "planet")
    }
    fuel = _chain_index([(a, b) for p, a, b in facts if p == "attacks"], kinds["province"])
    space = _chain_index([(a, b) for p, a, b in facts if p == "orbits"], kinds["planet"])

    lines: list[str] = []
    for p, a, b in facts:
        if p in ("eats", "craves", "fears"):
            lines.append(f"({p} {a} {b})")
        elif p == "locale":
            lines.append(f"(= (locale {a}) {fuel[b]})")
        elif p == "harmony":
            lines.append(f"(= (harmony {a}) {space[b]})")
    match = re.search(r"\(problem ([^)\s]+)", strips)
    assert match is not None  # the classical generator always names the problem
    name = match.group(1).replace("strips-", "")
    nl = "\n          "
    return (f"""(define (problem {name})
   (:domain mystery-prime-typed)
   (:objects {' '.join(kinds['food'])} - food
             {' '.join(kinds['pleasure'])} - pleasure
             {' '.join(kinds['pain'])} - pain
)
   (:init
          {nl.join(lines)})
   (:goal{goal.rstrip()[:-1].rstrip()}
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Mystery-prime PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-v", "--num-vehicles", type=int, required=True)
    parser.add_argument("-c", "--num-cargos", type=int, required=True)
    parser.add_argument("-f", "--num-fuel-levels", type=int, required=True)
    parser.add_argument("-p", "--num-space-levels", type=int, required=True)
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
