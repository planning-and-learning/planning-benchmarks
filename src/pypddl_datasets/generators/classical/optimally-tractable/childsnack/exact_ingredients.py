#!/usr/bin/env python3
"""Childsnack as generated for the IPC, which is optimally tractable as a whole.

The IPC generator provides one bread and one content per child, exactly as many
gluten-free ones as allergic children, and at least as many sandwiches as children.
Every child needs its own sandwich (make, put on tray, serve: 3 actions) and every
table with waiting children needs a tray to arrive (1 move). One tray loaded with
all sandwiches, gluten-free ones made from the gluten-free ingredients, and touring
the occupied tables meets that bound.
"""

from __future__ import annotations

import argparse
import re
import sys

from pypddl_datasets.generators.classical.ipc.childsnack import generator as _ipc


def make_problem(
    num_children: int, num_trays: int, gluten_factor: float, const_ratio: float = 1.2, seed: int | None = None
) -> str:
    if num_children < 1:
        raise ValueError("num_children must be at least 1")
    if num_trays < 1:
        raise ValueError("num_trays must be at least 1")
    if not 0 <= gluten_factor <= 1:
        raise ValueError("gluten_factor must be between 0 and 1")
    if const_ratio < 1:
        raise ValueError("const_ratio must be at least 1")
    problem = _ipc.make_problem(num_children, num_trays, gluten_factor, const_ratio, seed)
    tables = set(re.findall(r"\(waiting \S+ (\S+)\)", problem))
    return f"; optimal plan cost: {3 * num_children + len(tables)}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Childsnack task.")
    parser.add_argument("-c", "--num-children", type=int, required=True)
    parser.add_argument("-t", "--num-trays", type=int, required=True)
    parser.add_argument("-g", "--gluten-factor", type=float, required=True)
    parser.add_argument("-r", "--const-ratio", type=float, default=1.2)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_children, args.num_trays, args.gluten_factor, args.const_ratio, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
