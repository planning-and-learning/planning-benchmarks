#!/usr/bin/env python3
"""3-operator Blocksworld: every block starts on the table, the goal is a uniformly random state.

Optimal cost: 1 per goal (on x y), one move-t-to-b each, building every goal
tower bottom-up. No block is ever in the way, so the lower bound is met.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

from pypddl_datasets.generators.classical.ipc.blocks_3 import generator as _ipc


def _towers(blocks: list[str], rng: random.Random) -> list[list[str]]:
    """Uniformly random state over all labelled tower configurations, as bwstates in the IPC generator."""
    return _ipc.make_stacks(blocks, rng, _ipc.completion_counts(len(blocks)))


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    if num_blocks < 1:
        raise ValueError("num_blocks must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    goal: list[str] = []
    for tower in _towers(blocks, rng):  # the goal state in full, as the IPC generators emit it
        goal.append(f"(on-table {tower[0]})")
        goal.extend(f"(on {upper} {lower})" for lower, upper in zip(tower, tower[1:]))
        goal.append(f"(clear {tower[-1]})")
    stacked = sum(fact.startswith("(on ") for fact in goal)
    init = [*(f"(on-table {block})" for block in blocks), *(f"(clear {block})" for block in blocks)]
    return f"""; optimal plan cost: {stacked}
(define (problem blocks-3-init-on-table-{num_blocks})
  (:domain blocksworld-3ops)
  (:objects {' '.join(blocks)})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      {fact}' for fact in goal)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Blocksworld task with all blocks on the table.")
    parser.add_argument("-b", "--num-blocks", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_blocks, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
