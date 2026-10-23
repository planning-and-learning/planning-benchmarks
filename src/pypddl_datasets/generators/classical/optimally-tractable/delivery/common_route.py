#!/usr/bin/env python3
"""Delivery with several trucks and all packages sharing one origin o and one goal g.

Each truck holds one package. With D = dist(o, g) and d_t = dist(t, o), a truck's
first trip costs d_t + D and each further trip 2 * D (back to o and over again),
plus pick and drop per package. For k packages and the set S of trucks used, the
cost is 2k + 2kD + sum_{t in S} (d_t - D), so S is the closest truck plus every
other truck with d_t < D, at most k trucks in all.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def make_problem(grid_size: int, num_trucks: int, num_packages: int, seed: int | None = None) -> str:
    if grid_size < 2:
        raise ValueError("grid_size must be at least 2")
    if num_trucks < 1:
        raise ValueError("num_trucks must be at least 1")
    if num_packages < 1:
        raise ValueError("num_packages must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    cells = [(x, y) for x in range(grid_size) for y in range(grid_size)]
    origin, goal = rng.sample(cells, 2)
    trucks = [rng.choice(cells) for _ in range(num_trucks)]

    def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    route = dist(origin, goal)
    approaches = sorted(dist(truck, origin) for truck in trucks)
    used = [approaches[0], *(d for d in approaches[1:num_packages] if d < route)]
    cost = 2 * num_packages + 2 * num_packages * route + sum(d - route for d in used)

    def name(cell: tuple[int, int]) -> str:
        return f"c_{cell[0]}_{cell[1]}"

    adjacent = [
        f"(adjacent {name((x, y))} {name((nx, ny))})"
        for x, y in cells
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        if 0 <= nx < grid_size and 0 <= ny < grid_size
    ]
    init = [
        *adjacent,
        *(f"(at p{i} {name(origin)})" for i in range(num_packages)),
        *(f"(at t{i} {name(truck)})\n    (empty t{i})" for i, truck in enumerate(trucks)),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem delivery-common-route-g{grid_size}-t{num_trucks}-p{num_packages})
  (:domain delivery)
  (:objects
    {' '.join(name(cell) for cell in cells)} - cell
    {' '.join(f'p{i}' for i in range(num_packages))} - package
    {' '.join(f't{i}' for i in range(num_trucks))} - truck
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (at p{i} {name(goal)})' for i in range(num_packages))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a multi-truck Delivery task with one shared route.")
    parser.add_argument("-g", "--grid-size", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.grid_size, args.num_trucks, args.num_packages, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
