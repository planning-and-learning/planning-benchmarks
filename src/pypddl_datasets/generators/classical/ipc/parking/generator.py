#!/usr/bin/env python3
# Port of pddl-generators parking/parking-generator.pl (seq mode), as called by
# Autoscale: `parking-generator.pl prob {curbs} {cars} seq` with
# cars = 2 * (curbs - 1) + {0, -1, -2}. Adds the (total-cost) initialisation and
# metric that the Autoscale/IPC 2011 action-cost domain needs.

from __future__ import annotations

import argparse
import math
import random
import sys


def make_problem(num_curbs: int, num_cars: int, seed: int | None = None) -> str:
    """Generate a Parking task.

    Initially a uniformly random number of cars between ``ceil(cars / 2)`` and
    ``min(curbs, cars)`` stand directly at the first curbs in shuffled order; the
    remaining cars are parked behind them. The goal is the canonical layout:
    car i at curb i, and the remaining cars behind cars 0, 1, ...
    """
    checks: list[tuple[str, object, int]] = [("num_curbs", num_curbs, 2), ("num_cars", num_cars, 1)]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    max_cars = 2 * num_curbs - 2
    if num_cars > max_cars:
        raise ValueError(f"num_cars must be at most {max_cars} for {num_curbs} curbs")

    rng = random.Random(seed)
    curbs = [f"curb_{i:0{len(str(num_curbs - 1))}d}" for i in range(num_curbs)]
    cars = [f"car_{i:0{len(str(num_cars - 1))}d}" for i in range(num_cars)]

    def layout(order: list[str], num_against_curb: int) -> dict[str, str]:
        against = {curbs[i]: order[i] for i in range(num_against_curb)}
        against.update((order[i - num_against_curb], order[i]) for i in range(num_against_curb, num_cars))
        return against

    initial = layout(rng.sample(cars, num_cars), rng.randint(math.ceil(num_cars / 2), min(num_curbs, num_cars)))
    goal = layout(cars, min(num_curbs, num_cars))

    init_facts = ["    (= (total-cost) 0)"]
    goals: list[str] = []
    for curb in curbs:
        if curb not in initial:
            init_facts.append(f"    (curb-clear {curb})")
        else:
            car = initial[curb]
            init_facts.append(f"    (at-curb {car})")
            init_facts.append(f"    (at-curb-num {car} {curb})")
            if car in initial:
                init_facts.append(f"    (behind-car {initial[car]} {car})")
                init_facts.append(f"    (car-clear {initial[car]})")
            else:
                init_facts.append(f"    (car-clear {car})")
        if curb in goal:
            car = goal[curb]
            goals.append(f"      (at-curb-num {car} {curb})")
            if car in goal:
                goals.append(f"      (behind-car {goal[car]} {car})")

    return (f"""(define (problem parking-c{num_curbs}-n{num_cars})
  (:domain parking)
  (:objects
     {" ".join(cars)} - car
     {" ".join(curbs)} - curb
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
  (:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Parking PDDL problem.")
    parser.add_argument("-c", "--num-curbs", type=int, required=True)
    parser.add_argument("-n", "--num-cars", type=int, required=True)
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
