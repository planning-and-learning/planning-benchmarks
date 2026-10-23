#!/usr/bin/env python3
"""3-operator Blocksworld: random initial towers, the goal is a single (on a b).

Optimal cost: every block above a or above b (other than a) is moved once,
then a is moved onto b. If a sits higher up in b's tower, a must first leave to
uncover the blocks between them: 1 more.
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


def optimal_moves(towers: list[list[str]], a: str, b: str) -> int:
    """Number of block moves (1 action each) to achieve (on a b)."""
    above = {block: set(tower[i + 1 :]) for tower in towers for i, block in enumerate(tower)}
    if any(lower == b and upper == a for tower in towers for lower, upper in zip(tower, tower[1:])):
        return 0
    return len((above[a] | above[b]) - {a}) + 1 + (a in above[b])


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    if num_blocks < 2:
        raise ValueError("num_blocks must be at least 2")
    rng = random.Random(seed if seed is not None else int(time.time()))
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    towers = _towers(blocks, rng)
    on = {(upper, lower) for tower in towers for lower, upper in zip(tower, tower[1:])}
    a, b = rng.choice([(a, b) for a in blocks for b in blocks if a != b and (a, b) not in on])
    return f"""; optimal plan cost: {optimal_moves(towers, a, b)}
(define (problem blocks-3-on-pair-{num_blocks})
  (:domain blocksworld-3ops)
  (:objects {' '.join(blocks)})
  (:init
{chr(10).join(f'    {fact}' for fact in _state(towers))}
  )
  (:goal
    (and
      (on {a} {b})
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Blocksworld task with a single (on a b) goal.")
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
