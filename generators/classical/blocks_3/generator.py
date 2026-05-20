#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time

DOMAIN_NAME = "blocksworld-3ops"


def _make_stacks(blocks: list[str], rng: random.Random) -> list[list[str]]:
    shuffled = blocks[:]
    rng.shuffle(shuffled)
    stacks: list[list[str]] = []
    for block in shuffled:
        if stacks and rng.random() < 0.65:
            rng.choice(stacks).append(block)
        else:
            stacks.append([block])
    return stacks


def _state_facts(stacks: list[list[str]]) -> list[str]:
    facts = []
    clear_blocks = set()
    for stack in stacks:
        facts.append(f"    (on-table {stack[0]})")
        for lower, upper in zip(stack, stack[1:]):
            facts.append(f"    (on {upper} {lower})")
        clear_blocks.add(stack[-1])
    facts.extend(f"    (clear {block})" for block in sorted(clear_blocks))
    return facts


def _goal_facts(stacks: list[list[str]]) -> list[str]:
    facts = []
    for stack in stacks:
        for lower, upper in zip(stack, stack[1:]):
            facts.append(f"      (on {upper} {lower})")
    return facts


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    initial_stacks = _make_stacks(blocks, rng)
    goal_stacks = _make_stacks(blocks, rng)
    goal_facts = _goal_facts(goal_stacks)
    if not goal_facts:
        goal_facts = ["      (clear b1)"]

    return f"""(define (problem blocks-3-{num_blocks})
  (:domain {DOMAIN_NAME})
  (:objects {' '.join(blocks)})
  (:init
{chr(10).join(_state_facts(initial_stacks))}
  )
  (:goal
    (and
{chr(10).join(goal_facts)}
    )
  )
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a 3-operator Blocksworld PDDL problem.")
    parser.add_argument("-b", "--num-blocks", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)

    if args.num_blocks < 1:
        parser.error("num_blocks must be at least 1")

    print(make_problem(args.num_blocks, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
