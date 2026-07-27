#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time

DOMAIN_NAME = "blocksworld-3ops"


def _completion_counts(num_blocks: int) -> list[list[int]]:
    """Return g(n, k): completions of n floating and k rooted towers."""
    counts = [[1] * (num_blocks + 1)]
    for num_floating in range(1, num_blocks + 1):
        previous = counts[-1]
        counts.append(
            [
                previous[num_rooted] * (num_floating + num_rooted - 1)
                + previous[num_rooted + 1]
                for num_rooted in range(num_blocks - num_floating + 1)
            ]
        )
    return counts


def _make_stacks(
    blocks: list[str], rng: random.Random, counts: list[list[int]]
) -> list[list[str]]:
    floating = [[block] for block in blocks]
    rooted: list[list[str]] = []
    while floating:
        current = floating.pop()
        num_floating = len(floating)
        num_rooted = len(rooted)
        completions_per_destination = counts[num_floating][num_rooted]
        table_completions = counts[num_floating][num_rooted + 1]
        choice = rng.randrange(counts[num_floating + 1][num_rooted])
        if choice < table_completions:
            rooted.append(current)
            continue
        destination = (choice - table_completions) // completions_per_destination
        if destination < num_rooted:
            rooted[destination].extend(current)
        else:
            floating[destination - num_rooted].extend(current)
    return rooted


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
        facts.append(f"      (on-table {stack[0]})")
        for lower, upper in zip(stack, stack[1:]):
            facts.append(f"      (on {upper} {lower})")
        facts.append(f"      (clear {stack[-1]})")
    return facts


def make_problem(num_blocks: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))
    blocks = [f"b{i}" for i in range(1, num_blocks + 1)]
    counts = _completion_counts(num_blocks)
    initial_stacks = _make_stacks(blocks, rng, counts)
    goal_stacks = _make_stacks(blocks, rng, counts)
    goal_facts = _goal_facts(goal_stacks)

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
