#!/usr/bin/env python3
# Reconstruction of the IPC 2023 numeric FO-Counters tasks (Scala and Li). No
# generator is published; every IPC task starts all values and rates at 0, so the
# task is determined by the number of counters.

from __future__ import annotations

import argparse
import sys


def make_problem(num_counters: int) -> str:
    """Generate an FO-Counters task: counters c0..c{n-1} with value and rate 0,
    max_int = 2n, goal value(c_i) + 1 <= value(c_{i+1}), minimising total cost."""
    if not isinstance(num_counters, int) or isinstance(num_counters, bool) or num_counters < 2:
        raise ValueError("num_counters must be an integer at least 2")

    counters = [f"c{i}" for i in range(num_counters)]
    values = "\n".join(f"        (= (value {c}) 0)" for c in counters)
    rates = "\n".join(f"        (= (rate_value {c}) 0)" for c in counters)
    goals = "\n".join(f"    (<= (+ (value {a}) 1) (value {b}))" for a, b in zip(counters, counters[1:]))
    return (f"""(define (problem instance_{num_counters})
  (:domain fn-counters)
  (:objects
    {' '.join(counters)} - counter
  )

  (:init
    (= (total-cost) 0)
    (= (max_int) {2 * num_counters})
{values}

{rates}
  )

  (:goal (and
{goals}
  ))
  (:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric FO-Counters PDDL problem.")
    parser.add_argument("-n", "--num-counters", type=int, required=True)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
