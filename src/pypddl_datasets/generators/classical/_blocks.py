"""Uniform labeled tower sampling shared by the two Blocksworld encodings."""

from __future__ import annotations

import argparse
from collections.abc import Callable

from pypddl_datasets.generators.runtime import Atom, RandomSource, atom


def completion_counts(num_blocks: int) -> list[list[int]]:
    """Count completions of floating towers with a given number of rooted towers."""
    counts = [[1] * (num_blocks + 1)]
    for num_floating in range(1, num_blocks + 1):
        previous = counts[-1]
        counts.append([
            previous[rooted] * (num_floating + rooted - 1) + previous[rooted + 1]
            for rooted in range(num_blocks - num_floating + 1)
        ])
    return counts


def make_stacks(
    blocks: list[str], rng: RandomSource, counts: list[list[int]],
) -> list[list[str]]:
    """Choose tower attachments in proportion to their numbers of completions."""
    floating = [[block] for block in blocks]
    rooted: list[list[str]] = []
    while floating:
        current = floating.pop()
        num_floating, num_rooted = len(floating), len(rooted)
        completions = counts[num_floating][num_rooted]
        table_completions = counts[num_floating][num_rooted + 1]
        choice = rng.randrange(counts[num_floating + 1][num_rooted])
        if choice < table_completions:
            rooted.append(current)
        else:
            destination = (choice - table_completions) // completions
            if destination < num_rooted:
                rooted[destination].extend(current)
            else:
                floating[destination - num_rooted].extend(current)
    return rooted


def arrangement(stacks: list[list[str]]) -> tuple[Atom, ...]:
    """Describe all tower boundaries and support relations."""
    facts: list[Atom] = []
    for stack in stacks:
        facts.append(atom("on-table", stack[0]))
        facts.extend(atom("on", upper, lower) for lower, upper in zip(stack, stack[1:]))
        facts.append(atom("clear", stack[-1]))
    return tuple(facts)


def run_cli(operators: int, make_problem: Callable[[int, int | None], str],
            argv: list[str] | None = None) -> int:
    """Share the command-line contract of the two operator encodings."""
    parser = argparse.ArgumentParser(description=f"Generate a {operators}-operator Blocksworld PDDL problem.")
    parser.add_argument("-b", "--num-blocks", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    if args.num_blocks < 1:
        parser.error("num_blocks must be at least 1")
    print(make_problem(args.num_blocks, args.seed), end="")
    return 0
