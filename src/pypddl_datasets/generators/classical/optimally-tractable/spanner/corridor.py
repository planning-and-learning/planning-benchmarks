#!/usr/bin/env python3
"""Spanner as in the IPC 2023 learning track, which is optimally tractable as a whole.

The man walks one way along the corridor shed -> location1 -> ... -> gate, so every
plan walks num_locations + 1 times. Each nut needs one tighten and its own spanner
(a spanner is used up), so num_nuts pickups; picking up the first spanners met on
the way meets that bound.
"""

from __future__ import annotations

import argparse
import sys

from pypddl_datasets.generators.classical.ipc_learning.spanner import generator as _ipc


def make_problem(num_spanners: int, num_nuts: int, num_locations: int, seed: int | None = None) -> str:
    if num_nuts < 1:
        raise ValueError("num_nuts must be at least 1")
    if num_spanners < num_nuts:
        raise ValueError("num_spanners must be at least num_nuts")
    if num_locations < 1:
        raise ValueError("num_locations must be at least 1")
    cost = num_locations + 1 + 2 * num_nuts
    problem = _ipc.make_problem(num_spanners, num_nuts, num_locations, seed, name="spanner-corridor")
    return f"; optimal plan cost: {cost}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Spanner task.")
    parser.add_argument("-s", "--num-spanners", type=int, required=True)
    parser.add_argument("-n", "--num-nuts", type=int, required=True)
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_spanners, args.num_nuts, args.num_locations, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
