#!/usr/bin/env python3
"""Elevators with one elevator serving every floor, big enough for everyone, and all
passengers travelling to the same floor d.

Only moves cost: stop + rate * distance (IPC defaults: fast 1 + 3d, slow 5 + d).
The elevator stops once on each origin floor (except the one it starts on) and then
on d. With L and R the lowest and highest origin, it covers [L, R] from its start s
and ends at d: rate * (R - L + min(|s - L| + |R - d|, |s - R| + |L - d|)).
"""

from __future__ import annotations

import argparse
import random
import sys
import time

COSTS = {"fast": (1, 3), "slow": (5, 1)}  # (stop cost, cost per floor)


def make_problem(num_floors: int, num_passengers: int, kind: str = "slow", seed: int | None = None) -> str:
    if num_floors < 2:
        raise ValueError("num_floors must be at least 2")
    if num_passengers < 1:
        raise ValueError("num_passengers must be at least 1")
    if kind not in COSTS:
        raise ValueError("kind must be 'fast' or 'slow'")
    rng = random.Random(seed if seed is not None else int(time.time()))
    stop, rate = COSTS[kind]
    destination, lift = rng.randrange(num_floors), rng.randrange(num_floors)
    origins = [rng.choice([f for f in range(num_floors) if f != destination]) for _ in range(num_passengers)]
    low, high = min(origins), max(origins)
    sweep = high - low + min(abs(lift - low) + abs(high - destination), abs(lift - high) + abs(low - destination))
    cost = stop * (len(set(origins)) - (lift in origins) + 1) + rate * sweep

    counts = [f"n{i}" for i in range(max(num_floors, num_passengers + 1))]
    init = [
        "(= (total-cost) 0)",
        *(f"(next {a} {b})" for a, b in zip(counts, counts[1:])),
        *(f"(above n{i} n{j})" for i in range(num_floors) for j in range(i + 1, num_floors)),
        *(f"(reachable-floor e0 n{i})" for i in range(num_floors)),
        *(f"(can-hold e0 n{i})" for i in range(1, num_passengers + 1)),
        "(passengers e0 n0)",
        f"(lift-at e0 n{lift})",
        *(f"(passenger-at p{i} n{o})" for i, o in enumerate(origins)),
        *(
            f"(= (travel-{kind} n{i} n{j}) {stop + (j - i) * rate})"
            for i in range(num_floors)
            for j in range(i + 1, num_floors)
        ),
    ]
    return f"""; optimal plan cost: {cost}
(define (problem elevators-common-destination-{kind}-f{num_floors}-p{num_passengers})
  (:domain elevators-sequencedstrips)
  (:objects
    {' '.join(counts)} - count
    e0 - {kind}-elevator
    {' '.join(f'p{i}' for i in range(num_passengers))} - passenger
  )
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (passenger-at p{i} n{destination})' for i in range(num_passengers))}
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an Elevators task with all passengers going to one floor.")
    parser.add_argument("-f", "--num-floors", type=int, required=True)
    parser.add_argument("-p", "--num-passengers", type=int, required=True)
    parser.add_argument("-k", "--kind", choices=sorted(COSTS), default="slow")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_floors, args.num_passengers, args.kind, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
