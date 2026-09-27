#!/usr/bin/env python3
# Line Exchange SNP (IPC 2026 numeric). No generator was published; this
# reconstructs the 20 IPC tasks, named <robots>_<mean load>_<spread>_<segment>.

from __future__ import annotations

import argparse
import random
import sys


def make_problem(num_robots: int, mean_load: int, spread: int, segment: int, seed: int | None = None) -> str:
    """Generate a Line Exchange task.

    Robot i patrols [segment*i, segment*(i+1)] and starts, and must end, at its
    midpoint; neighbours exchange load units when they meet on the shared border.
    Loads start at ``mean_load`` each, then every unit moves with probability
    ``spread``% to a robot drawn by random weights Exp(1)^(0.8 * spread / 100), so
    high spreads give very unbalanced lines, as in the IPC tasks; draws that are
    already balanced are redrawn. The goal balances all loads (chain of equalities).
    """
    for name, value, minimum in (("num_robots", num_robots, 2), ("mean_load", mean_load, 1),
                                 ("spread", spread, 1), ("segment", segment, 2)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if spread > 100:
        raise ValueError("spread must be at most 100 (a percentage)")
    if segment % 2:
        raise ValueError("segment must be even (robots step by 1 from the midpoint to the border)")

    rng = random.Random(seed)
    while True:
        loads = [mean_load] * num_robots
        # ponytail: weight exponent fitted to the IPC max deviations (0.26/0.39/0.84 vs ours 0.31/0.42/0.72 at spread 25/50/90)
        weights = [rng.expovariate(1) ** (0.8 * spread / 100) for _ in range(num_robots)]
        for owner in range(num_robots):
            for _ in range(mean_load):
                if rng.random() < spread / 100:
                    loads[owner] -= 1
                    loads[rng.choices(range(num_robots), weights)[0]] += 1
        if len(set(loads)) > 1:
            break

    robots = [f"r{i}" for i in range(num_robots)]
    x = [f"(= (x {r}) {segment * i + segment / 2})" for i, r in enumerate(robots)]
    init = [f"(= (d) {segment})", *(f"(= (i {r}) {i})" for i, r in enumerate(robots)), *x,
            *(f"(= (q {r}) {q})" for r, q in zip(robots, loads)),
            *(f"(next {a} {b})" for a, b in zip(robots, robots[1:]))]
    goal = [*x, *(f"(= (q {a}) (q {b}))" for a, b in zip(robots, robots[1:]))]
    return (f"""(define (problem line-exchange-{num_robots}-{mean_load}-{spread}-{segment})
    (:domain line-exchange)
    (:objects
        {' '.join(robots)} - robot
    )
    (:init
{chr(10).join("        " + f for f in init)}
    )
    (:goal
        (and
{chr(10).join("            " + g for g in goal)}
        )
    )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Line Exchange PDDL problem.")
    parser.add_argument("num_robots", type=int)
    parser.add_argument("mean_load", type=int)
    parser.add_argument("spread", type=int, help="percentage of load units moved to a random robot")
    parser.add_argument("segment", type=int, help="segment length per robot (even)")
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
