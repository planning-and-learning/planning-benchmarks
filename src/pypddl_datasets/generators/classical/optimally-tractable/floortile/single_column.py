#!/usr/bin/env python3
"""Floortile with one robot and one column, painted in the IPC's alternating colours.

A painted tile cannot be entered, and the robot can never paint the tile it stands
on, so the column must be painted top-down from below: the robot climbs to row
R - 1 (3 per up, or 1 down from row R), then alternates paint-up (2) and down (1)
until it paints row 1 from row 0. Adjacent rows differ in colour, so it changes
colour (5) between every two paints, plus once at the start if it holds the wrong
colour for row R.
"""

from __future__ import annotations

import argparse
import re
import sys

from pypddl_datasets.generators.classical.ipc.floortile import generator as _ipc


def make_problem(num_rows: int, seed: int | None = None) -> str:
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1")
    problem = _ipc.make_problem(num_rows, 1, 1, seed, name=f"floortile-single-column-r{num_rows}")
    assert problem is not None
    start = int(re.findall(r"\(robot-at robot1 tile_(\d+)-1\)", problem)[0])
    color = re.findall(r"\(robot-has robot1 (\S+)\)", problem)[0]
    top = re.findall(rf"\(painted tile_{num_rows}-1 (\S+)\)", problem)[0]
    climb = 1 if start == num_rows else 3 * (num_rows - 1 - start)
    cost = climb + 2 * num_rows + (num_rows - 1) + 5 * (num_rows - 1 + (color != top))
    return f"; optimal plan cost: {cost}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a one-column Floortile task.")
    parser.add_argument("-r", "--num-rows", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_rows, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
