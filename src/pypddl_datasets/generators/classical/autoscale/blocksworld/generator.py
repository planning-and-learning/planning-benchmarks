#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators blocksworld/4ops/2pddl/2pddl.c (FF domain collection). Distributed
# under the original notice, not GPL-3.0-or-later (see LICENSES/LicenseRef-Freiburg.txt):
#
# (C) Copyright 2001 Albert Ludwigs University Freiburg
#     Institute of Computer Science
#
# All rights reserved. Use of this software is permitted for
# non-commercial research purposes, and it may be copied only
# for that use.  All copies must include this copyright message.
# This software is made available AS IS, and neither the authors
# nor the  Albert Ludwigs University Freiburg make any warranty
# about the software or its performance.
# Port of pddl-generators/blocksworld (bwstates -s 2 + 4ops/2pddl) as called by
# Autoscale: blocksworld 4 {n} {seed}. Initial and goal state are independent
# uniformly random states (sampled like blocks_4); unlike blocks_4, the goal
# lists only the (on x y) facts of the goal state, as 2pddl does.

from __future__ import annotations

import argparse
import random
import sys

# autoscale/blocksworld reuses the uniform state sampler of ipc/blocks_4 (same distribution)
from pypddl_datasets.generators.classical.ipc.blocks_4.generator import (  # pylint: disable=protected-access
    _completion_counts,  # pyright: ignore[reportPrivateUsage]
    _make_stacks,  # pyright: ignore[reportPrivateUsage]
    _state_facts,  # pyright: ignore[reportPrivateUsage]
)


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    if not _is_int(num_blocks) or num_blocks < 1:
        raise ValueError("num_blocks must be an integer at least 1")
    rng = random.Random(seed)
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    counts = _completion_counts(num_blocks)
    initial_stacks = _make_stacks(blocks, rng, counts)
    goal_stacks = _make_stacks(blocks, rng, counts)
    goal_facts = [f"      (on {upper} {lower})" for stack in goal_stacks for lower, upper in zip(stack, stack[1:])]

    return (f"""(define (problem BW-rand-{num_blocks})
  (:domain blocksworld)
  (:objects {' '.join(blocks)})
  (:init
{chr(10).join(_state_facts(initial_stacks, "on-table", "arm-empty"))}
  )
  (:goal
    (and
{chr(10).join(goal_facts)}
    )
  )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a 4-operator Blocksworld PDDL problem (2pddl goals).")
    parser.add_argument("num_blocks", type=int)
    parser.add_argument("seed", type=int, nargs="?")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_blocks, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
