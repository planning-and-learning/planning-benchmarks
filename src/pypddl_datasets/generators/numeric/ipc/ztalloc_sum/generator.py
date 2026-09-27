#!/usr/bin/env python3
# Reconstructed from the IPC 2026 ztalloc-sum tasks (data/numeric/ipc2026/ztalloc-sum);
# no generator was published. Domain by Christian Muise, IPC edit with several registers.

from __future__ import annotations

import argparse
import random
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    num_registers: int,
    target: int | None = None,
    min_target: int = 1,
    max_target: int = 1000,
    seed: int | None = None,
    name: str = "p1",
) -> str:
    """Generate a ztalloc-sum task: registers start at 1, their values must sum to ``target``.

    Without ``target`` it is drawn uniformly from ``[min_target, max_target]``.
    """
    for label, value, minimum in (("num_registers", num_registers, 1), ("min_target", min_target, 1)):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{label} must be an integer at least {minimum}")
    if max_target < min_target:
        raise ValueError("max_target must be at least min_target")
    if target is None:
        target = random.Random(seed).randint(min_target, max_target)
    if not _is_int(target) or target < 1:
        raise ValueError("target must be an integer at least 1")

    registers = [f"r{i}" for i in range(1, num_registers + 1)]
    init = ["        (free)"]
    goal: list[str] = []
    for r in registers:
        init += [f"        (normal {r})", f"        (= (value {r}) 1)", f"        (= (work-value {r}) 0)"]
        goal += [f"            (normal {r})", f"            (= (work-value {r}) 0)"]
    init.append("        (= (total-cost) 0)")
    total = f"(value {registers[0]})"
    for r in registers[1:]:
        total = f"(+ {total} (value {r}))"
    nl = "\n"
    return (f"""(define (problem {name})
    (:domain ztalloc-sum)

    (:objects
        {' '.join(registers)} - register
    )

    (:init
{nl.join(init)}
    )

    (:goal
        (and
            (= {total} {target})
            (free)
{nl.join(goal)}
        )
    )

    (:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a ztalloc-sum PDDL problem.")
    parser.add_argument("-r", "--num-registers", type=int, required=True)
    parser.add_argument("-t", "--target", type=int)
    parser.add_argument("--min-target", type=int, default=1)
    parser.add_argument("--max-target", type=int, default=1000)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--name", default="p1")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
