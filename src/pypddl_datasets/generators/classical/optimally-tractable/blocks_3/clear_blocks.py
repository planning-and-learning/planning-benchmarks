#!/usr/bin/env python3
"""3-operator Blocksworld: random initial towers, the goal clears a random set X of blocks.

Every block above some block of X must move, once each, and the table always takes
it. Optimal cost: u, the number of blocks above X.
"""

from __future__ import annotations

import argparse
import random
import sys
import time


def _towers(blocks: list[str], rng: random.Random) -> list[list[str]]:
    towers: list[list[str]] = []
    for block in rng.sample(blocks, len(blocks)):
        if towers and rng.random() < 0.5:
            towers[-1].append(block)
        else:
            towers.append([block])
    return towers


def _state(towers: list[list[str]]) -> list[str]:
    facts: list[str] = []
    for tower in towers:
        facts.append(f"(on-table {tower[0]})")
        facts.extend(f"(on {upper} {lower})" for lower, upper in zip(tower, tower[1:]))
        facts.append(f"(clear {tower[-1]})")
    return facts


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    if num_blocks < 2:
        raise ValueError("num_blocks must be at least 2")
    rng = random.Random(seed if seed is not None else int(time.time()))
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    towers: list[list[str]] = []
    while all(len(tower) == 1 for tower in towers):
        towers = _towers(blocks, rng)
    covered = [block for tower in towers for block in tower[:-1]]
    targets = rng.sample(covered, rng.randint(1, len(covered)))
    moved = {block for tower in towers for i, block in enumerate(tower) for lower in tower[:i] if lower in targets}
    return f"""; optimal plan cost: {len(moved)}
(define (problem blocks-3-clear-blocks-{num_blocks})
  (:domain blocksworld-3ops)
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
