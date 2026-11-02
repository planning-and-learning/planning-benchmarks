#!/usr/bin/env python3
"""4-operator Blocksworld: random initial towers, the goal clears a uniformly random non-empty set X of blocks.

Every block above some block of X must move, once each, and the table always takes
it. Optimal cost: 2u for the u blocks above X (unstack and put down), minus 1 if the
last one can stay in the hand: the last block moved from a tower is the one right
above its lowest target, and a held block is not clear, so it must not be in X.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

from pypddl_datasets.generators.classical.ipc.blocks_4 import generator as _ipc


def _towers(blocks: list[str], rng: random.Random) -> list[list[str]]:
    """Uniformly random state over all labelled tower configurations, as bwstates in the IPC generator."""
    return _ipc.make_stacks(blocks, rng, _ipc.completion_counts(len(blocks)))


def _state(towers: list[list[str]]) -> list[str]:
    facts = ["(handempty)"]
    for tower in towers:
        facts.append(f"(ontable {tower[0]})")
        facts.extend(f"(on {upper} {lower})" for lower, upper in zip(tower, tower[1:]))
        facts.append(f"(clear {tower[-1]})")
    return facts


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    if num_blocks < 1:
        raise ValueError("num_blocks must be at least 1")
    rng = random.Random(seed if seed is not None else int(time.time()))
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    towers = _towers(blocks, rng)
    targets: list[str] = []
    while not targets:  # a uniformly random non-empty set of blocks
        targets = [block for block in blocks if rng.random() < 0.5]
    moved = {block for tower in towers for i, block in enumerate(tower) for lower in tower[:i] if lower in targets}
    lowest = [tower[min(i for i, b in enumerate(tower[:-1]) if b in targets) + 1] for tower in towers
              if any(b in targets for b in tower[:-1])]
    cost = 2 * len(moved) - any(block not in targets for block in lowest)
    return f"""; optimal plan cost: {cost}
(define (problem blocks-clear-blocks-{num_blocks})
  (:domain blocks)
  (:objects {' '.join(blocks)})
  (:init
{chr(10).join(f'    {fact}' for fact in _state(towers))}
  )
  (:goal
    (and
{chr(10).join(f'      (clear {block})' for block in sorted(targets))}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Blocksworld task that clears several blocks.")
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
