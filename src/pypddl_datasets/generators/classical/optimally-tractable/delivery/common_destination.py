#!/usr/bin/env python3
"""Delivery as in the IPC, which is optimally tractable as a whole.

One truck holding one package at a time, a 4-connected grid, and every package goes
to the same goal cell g. After the first delivery the truck is at g, so each later
package p costs a round trip 2 * dist(g, p) plus pick and drop. With truck start t,
the first package p minimizes dist(t, p) + dist(p, g) - 2 * dist(g, p), so the optimal
cost is sum_p (2 * dist(g, p) + 2) + min_p (dist(t, p) - dist(p, g)) over the
packages not already at g. Dropping a package on the way never helps (triangle
inequality, two extra actions).
"""

from __future__ import annotations

import argparse
import re
import sys

from pypddl_datasets.generators.classical.ipc.delivery import generator as _ipc


def make_problem(grid_size: int, num_packages: int, seed: int | None = None) -> str:
    if grid_size < 2:
        raise ValueError("grid_size must be at least 2")
    if num_packages < 1:
        raise ValueError("num_packages must be at least 1")
    problem = _ipc.make_problem(grid_size, num_packages, seed)
    init, goal = problem.split("(:goal", 1)

    def cell(name: str) -> tuple[int, int]:
        x, y = name.split("_")[1:]
        return int(x), int(y)

    def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    target = cell(re.findall(r"\(at \S+ (\S+)\)", goal)[0])
    truck = cell(re.findall(r"\(at t1 (\S+)\)", init)[0])
    packages = [cell(c) for p, c in re.findall(r"\(at (\S+) (\S+)\)", init) if p != "t1"]
    packages = [p for p in packages if p != target]
    cost = 0
    if packages:
        cost = sum(2 * dist(target, p) + 2 for p in packages) + min(dist(truck, p) - dist(p, target) for p in packages)
    return f"; optimal plan cost: {cost}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC Delivery task.")
    parser.add_argument("-g", "--grid-size", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.grid_size, args.num_packages, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
