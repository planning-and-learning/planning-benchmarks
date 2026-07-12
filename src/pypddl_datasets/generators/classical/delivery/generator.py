#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(grid_size: int, num_packages: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    cells = [f"c_{x}_{y}" for x in range(grid_size) for y in range(grid_size)]
    packages = [f"p{i}" for i in range(1, num_packages + 1)]
    truck = "t1"

    adjacent_facts = []
    for x in range(grid_size):
        for y in range(grid_size):
            current = f"c_{x}_{y}"
            if x > 0:
                adjacent_facts.append(f"        (adjacent {current} c_{x - 1}_{y})")
            if x < grid_size - 1:
                adjacent_facts.append(f"        (adjacent {current} c_{x + 1}_{y})")
            if y > 0:
                adjacent_facts.append(f"        (adjacent {current} c_{x}_{y - 1})")
            if y < grid_size - 1:
                adjacent_facts.append(f"        (adjacent {current} c_{x}_{y + 1})")

    package_locations = [rng.choice(cells) for _ in packages]
    package_facts = [
        f"        (at {package} {cell})"
        for package, cell in zip(packages, package_locations)
    ]
    truck_location = rng.choice(cells)

    goal_cell = rng.choice(cells)
    if len(set(package_locations)) == 1:
        while goal_cell == package_locations[0]:
            goal_cell = rng.choice(cells)

    goal_facts = [f"        (at {package} {goal_cell})" for package in packages]
    objects_cells = " ".join(cells)
    objects_packages = " ".join(packages)
    init_facts = "\n".join(
        [
            *adjacent_facts,
            *package_facts,
            f"        (at {truck} {truck_location})",
            f"        (empty {truck})",
        ]
    )
    goals = "\n".join(goal_facts)

    return f"""(define (problem delivery-{grid_size}x{grid_size}-{num_packages})
    (:domain delivery)
    (:objects
        {objects_cells} - cell
        {objects_packages} - package
        {truck} - truck
    )

    (:init
{init_facts}
    )

    (:goal
      (and
{goals}
      )
    )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Delivery PDDL problem.")
    parser.add_argument("grid_size", type=int, help="width and height of the square grid")
    parser.add_argument("num_packages", type=int, help="number of packages")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args(argv)

    if args.grid_size < 2:
        parser.error("grid_size must be at least 2")
    if args.num_packages < 1:
        parser.error("num_packages must be at least 1")

    print(make_problem(args.grid_size, args.num_packages, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
