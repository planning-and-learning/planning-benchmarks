#!/usr/bin/env python3
# Reconstruction of the IPC 2023 numeric Hydropower tasks (no generator was published).
# All reference tasks share one half-hourly demand curve over t0000..t2500 (only
# t0000..t2400 are chained by `before`); they differ in the reservoir capacity and
# the funds goal.

from __future__ import annotations

import argparse
import random
import sys

# Demand (turnvalue index) at t0000, t0030, ..., t2500, as in every reference task.
DEMAND = (
    7, 7, 7, 6, 6, 6, 5, 4, 3, 3, 4, 5, 9, 13, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19,
    18, 18, 18, 18, 18, 19, 20, 23, 25, 26, 25, 24, 22, 21, 20, 19, 18, 16, 14, 12, 10, 6,
    3, 1, 1, 1,
)
NUM_REACHABLE = 49  # t0000..t2400; t2430 and t2500 exist but no `before` leads there
NUM_VALUES = 27
INITIAL_FUNDS = 1000


def _time(index: int) -> str:
    return f"t{index // 2:02d}{30 * (index % 2):02d}"


def make_problem(capacity: int, seed: int | None = None) -> str:
    """Generate a Hydropower task with reservoir capacity ``capacity``.

    Starts empty with funds 1000. The goal asks for a profit below the optimum
    (22.95 per stored unit): 50 * floor(20 * capacity / 50) for capacities of at
    least 10, else 10 * u with u uniform in {2 * capacity - 1, 2 * capacity}, the
    rule the reference tasks follow.
    """
    if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 1:
        raise ValueError("capacity must be an integer at least 1")
    rng = random.Random(seed)
    if capacity >= 10:
        profit = 50 * (20 * capacity // 50)
    else:
        profit = 10 * rng.randint(2 * capacity - 1, 2 * capacity)

    times = [_time(i) for i in range(len(DEMAND))]
    values = [f"n{i}" for i in range(NUM_VALUES)]
    init = [f"\t  (= (value {v}) {i})" for i, v in enumerate(values)]
    init += [f"\t(demand {t} n{d})" for t, d in zip(times, DEMAND)]
    init.append(f"\t(timenow {times[0]})")
    init += [f"\t(before {times[i]} {times[i + 1]})" for i in range(NUM_REACHABLE - 1)]
    init += ["\t(= (stored_units) 0)", f"\t(= (stored_capacity) {capacity})", f"\t(= (funds) {INITIAL_FUNDS})"]
    return (f"""(define (problem power{capacity})
  (:domain hydropower)
  (:objects
\t  {' '.join(values)} - turnvalue
\t  {' '.join(times)} - time
)
(:init
{chr(10).join(init)}
)
\t (:goal (and
\t (>= (funds) {INITIAL_FUNDS + profit})
\t)
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Hydropower PDDL problem.")
    parser.add_argument("-c", "--capacity", type=int, required=True, help="reservoir capacity in units")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.capacity, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
