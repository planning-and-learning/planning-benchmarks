#!/usr/bin/env python3
"""Gripper as in the IPC: all balls start in rooma and must reach roomb.

Optimal cost: one pick and one drop per ball, and with two grippers ceil(n/2) moves
to roomb with ceil(n/2) - 1 moves back in between: 2n + 2 * ceil(n/2) - 1.
"""

from __future__ import annotations

import argparse
import sys

from pypddl_datasets.generators.classical.ipc.gripper import generator as _ipc


def make_problem(num_balls: int) -> str:
    return f"; optimal plan cost: {2 * num_balls + 2 * ((num_balls + 1) // 2) - 1}\n{_ipc.make_problem(num_balls)}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC Gripper task.")
    parser.add_argument("-n", "--num-balls", type=int, required=True)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_balls), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
