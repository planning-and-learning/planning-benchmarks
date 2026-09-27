#!/usr/bin/env python3
# Reconstructed from the IPC 2023 numeric block-grouping tasks (Scala and Ramirez; no generator
# was published). Problem names follow the IPC tasks: instance_<size>_<blocks>_<colours>_<seed>.

from __future__ import annotations

import argparse
import random
import sys
from itertools import combinations


def make_problem(size: int, num_blocks: int, num_colours: int, seed: int | None = None) -> str:
    """Generate a Block Grouping task on a ``size x size`` grid (coordinates 1..size).

    Every block gets a uniformly random cell (blocks may share a cell) and a
    uniformly random colour (a colour may stay unused). The goal requires, for
    every pair of blocks, equal coordinates if they share a colour and different
    cells otherwise.
    """
    for name, value, minimum in (("size", size, 1), ("num_blocks", num_blocks, 1), ("num_colours", num_colours, 1)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if size * size < num_colours:
        raise ValueError("size * size must be at least num_colours so every colour fits its own cell")

    rng = random.Random(seed)
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    position = {b: (rng.randint(1, size), rng.randint(1, size)) for b in blocks}
    colour = {b: rng.randrange(num_colours) for b in blocks}

    init = [f"(= (x {b}) {x})\n\t(= (y {b}) {y})" for b, (x, y) in position.items()]
    init += [f"(= (max_x) {size} )", "(= (min_x) 1 )", f"(= (max_y) {size} )", "(= (min_y) 1 )"]
    goals = []
    for a, b in combinations(sorted(blocks), 2):  # name order, as in the IPC tasks
        if colour[a] == colour[b]:
            goals.append(f"(= (x {a}) (x {b}))\n(= (y {a}) (y {b}))")
        else:
            goals.append(f"(or (not (= (x {a}) (x {b}))) (not (= (y {a}) (y {b}))))")

    # Strict PDDL rejects unused requirements: single-colour tasks have no disjunction.
    uses_or = any(goal.startswith("(or") for goal in goals)
    requirements = "(:requirements :disjunctive-preconditions :negative-preconditions)\n" if uses_or else ""
    return (f""";; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem instance_{size}_{num_blocks}_{num_colours}_{seed})
  (:domain mt-block-grouping)
{requirements}  (:objects
    {" ".join(blocks)} - block
  )

  (:init
    {chr(10).join(chr(9) + fact for fact in init).lstrip()}
  )

  (:goal (and
    {chr(10).join(chr(9) + goal for goal in goals).lstrip()}
  ))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Block Grouping PDDL problem.")
    parser.add_argument("size", type=int, help="grid side length")
    parser.add_argument("num_blocks", type=int)
    parser.add_argument("num_colours", type=int)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.size, args.num_blocks, args.num_colours, seed=args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
