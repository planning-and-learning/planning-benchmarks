#!/usr/bin/env python3
"""Movie as in the IPC, which is optimally tractable as a whole.

Every task has the same optimal cost 7: rewind-movie (the counter is not at two
hours), then reset-counter (rewinding deletes counter-at-zero), and one get action
per snack kind. The snack objects only add choices, never cheaper plans.
"""

from __future__ import annotations

import argparse
import sys

from pypddl_datasets.generators.classical.ipc.movie import generator as _ipc


def make_problem(num_snacks: int) -> str:
    return f"; optimal plan cost: 7\n{_ipc.make_problem(num_snacks)}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC Movie task.")
    parser.add_argument("-n", "--num-snacks", type=int, required=True)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_snacks), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
