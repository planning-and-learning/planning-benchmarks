#!/usr/bin/env python3
# Reconstruction of the IPC 2023 numeric Counters tasks (Scala and Ramirez; F-Strips
# original by Frances and Geffner). The only published helper,
# hstairs/planning-numeric-domains-generators counters/make_int_goals.py, rewrites
# goals; the sampling below follows the 20 IPC tasks.

from __future__ import annotations

import argparse
import random
import sys

INITS = ("zero", "reverse", "random")


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(num_counters: int, init: str = "random", seed: int | None = None) -> str:
    """Generate a Counters task: counters c0..c{n-1}, max_int = 2n, goal
    value(c_i) + 1 <= value(c_{i+1}) for every i.

    ``init`` picks the initial values like the three IPC task families: all 0
    (``zero``), strictly decreasing 2(n-1-i) (``reverse``), or uniform in
    0..max_int-1 (``random``).
    """
    if not _is_int(num_counters) or num_counters < 2:
        raise ValueError("num_counters must be an integer at least 2")
    if init not in INITS:
        raise ValueError(f"init must be one of {', '.join(INITS)}")

    rng = random.Random(seed)
    max_int = 2 * num_counters
    if init == "zero":
        values = [0] * num_counters
    elif init == "reverse":
        values = [2 * (num_counters - 1 - i) for i in range(num_counters)]
    else:
        values = [rng.randrange(max_int) for _ in range(num_counters)]

    counters = [f"c{i}" for i in range(num_counters)]
    init_facts = "\n".join(f"\t(= (value {c}) {v})" for c, v in zip(counters, values))
    goals = "\n".join(f"(<= (+ (value {a}) 1) (value {b}))" for a, b in zip(counters, counters[1:]))
    return (f"""(define (problem instance_{num_counters}_{init})
  (:domain fn-counters)
  (:objects
    {' '.join(counters)} - counter
  )

  (:init
    (= (max_int) {max_int})
{init_facts}
  )

  (:goal (and
{goals}
  ))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Counters PDDL problem.")
    parser.add_argument("-n", "--num-counters", type=int, required=True)
    parser.add_argument("-i", "--init", choices=INITS, default="random", help="initial values (default: random)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
