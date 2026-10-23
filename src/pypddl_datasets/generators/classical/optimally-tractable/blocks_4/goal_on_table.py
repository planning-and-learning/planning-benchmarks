#!/usr/bin/env python3
"""4-operator Blocksworld: random initial towers, the goal puts every block on the table.

Optimal cost: 2 per block not on the table, one unstack and one put-down each,
dismantling every tower top-down.
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
    cost = 2 * sum(len(tower) - 1 for tower in towers)
    return f"""; optimal plan cost: {cost}
(define (problem blocks-goal-on-table-{num_blocks})
  (:domain blocks)
  (:objects {' '.join(blocks)})
  (:init
{chr(10).join(f'    {fact}' for fact in _state(towers))}
  )
  (:goal
    (and
{chr(10).join(f'      (ontable {block})' for block in blocks)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Blocksworld task that puts every block on the table.")
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
