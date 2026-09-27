#!/usr/bin/env python3
# Port of autoscale/pddl-generators/elevators/generate.py (the Python generator
# Autoscale 21.11 calls; the C generate_data/generate_pddl pair is the older IPC
# generator and unused). Defaults are Autoscale's constant cost/capacity values.

from __future__ import annotations

import argparse
import random
import sys
from itertools import combinations


def make_problem(
    num_areas: int,
    area_size: int,
    num_passengers: int,
    num_fast_elevators: int,
    num_slow_elevators: int = 1,
    fast_cost: int = 3,
    stop_fast_cost: int = 1,
    fast_capacity: int = 3,
    slow_cost: int = 1,
    stop_slow_cost: int = 5,
    slow_capacity: int = 2,
    seed: int | None = None,
) -> str:
    """Generate an Elevators task with ``num_areas * area_size + 1`` floors.

    Fast elevators stop every ``area_size // 2`` floors of the building; each
    area gets ``num_slow_elevators`` slow elevators serving its floors and the
    first floor of the next area, so every floor is reachable. Moving from
    floor i to j costs ``stop_cost + |i - j| * cost`` for the elevator kind.
    Every passenger starts and ends on different uniformly drawn floors.
    """
    for name, value, minimum in (
        ("num_areas", num_areas, 1),
        ("area_size", area_size, 2),
        ("num_passengers", num_passengers, 1),
        ("num_fast_elevators", num_fast_elevators, 0),
        ("num_slow_elevators", num_slow_elevators, 1),
        ("fast_cost", fast_cost, 0),
        ("stop_fast_cost", stop_fast_cost, 0),
        ("fast_capacity", fast_capacity, 1),
        ("slow_cost", slow_cost, 0),
        ("stop_slow_cost", stop_slow_cost, 0),
        ("slow_capacity", slow_capacity, 1),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    num_floors = num_areas * area_size + 1
    fast_step = max(1, area_size // 2)

    # (name, kind, capacity, floors, initial floor), drawn in upstream order.
    elevators: list[tuple[str, str, int, range, int]] = []
    for i in range(num_fast_elevators):
        floors = range(0, num_floors, fast_step)
        elevators.append((f"fast{i}", "fast", fast_capacity, floors, rng.choice(floors)))
    for i in range(num_slow_elevators):
        for j in range(num_areas):
            floors = range(j * area_size, min(num_floors, (j + 1) * area_size + 1))
            elevators.append((f"slow{j}-{i}", "slow", slow_capacity, floors, rng.choice(floors)))

    passengers: list[tuple[int, int]] = []
    for _ in range(num_passengers):
        origin = rng.randint(0, num_floors - 1)
        destination = rng.randint(0, num_floors - 1)
        while destination == origin:
            destination = rng.randint(0, num_floors - 1)
        passengers.append((origin, destination))

    num_counts = max(num_floors, fast_capacity + 1 if num_fast_elevators else 0, slow_capacity + 1)
    init = [f"    (next n{i} n{i + 1})" for i in range(num_floors - 1)]
    init.extend(f"    (above n{i} n{j})" for i in range(num_floors - 1) for j in range(i + 1, num_floors))
    pairs: dict[str, set[tuple[int, int]]] = {"slow": set(), "fast": set()}
    for name, kind, capacity, floors, start in elevators:
        init.append(f"    (lift-at {name} n{start})")
        init.append(f"    (passengers {name} n0)")
        init.extend(f"    (can-hold {name} n{i + 1})" for i in range(capacity))
        init.extend(f"    (reachable-floor {name} n{i})" for i in floors)
        pairs[kind].update(combinations(floors, 2))
    init.extend(f"    (passenger-at p{index} n{origin})" for index, (origin, _) in enumerate(passengers))
    init.extend(
        f"    (= (travel-slow n{i} n{j}) {stop_slow_cost + (j - i) * slow_cost})" for i, j in sorted(pairs["slow"])
    )
    init.extend(
        f"    (= (travel-fast n{i} n{j}) {stop_fast_cost + (j - i) * fast_cost})" for i, j in sorted(pairs["fast"])
    )
    init.append("    (= (total-cost) 0)")
    goals = [f"      (passenger-at p{index} n{destination})" for index, (_, destination) in enumerate(passengers)]

    objects = [
        f"    {' '.join(f'n{i}' for i in range(num_counts))} - count",
        f"    {' '.join(f'p{i}' for i in range(num_passengers))} - passenger",
    ]
    for kind in ("fast", "slow"):
        names = [name for name, elevator_kind, *_ in elevators if elevator_kind == kind]
        if names:
            objects.append(f"    {' '.join(names)} - {kind}-elevator")

    return (f"""(define (problem elevators-a{num_areas}-s{area_size}-p{num_passengers}-f{num_fast_elevators}-l{num_slow_elevators})
  (:domain elevators-sequencedstrips)
  (:objects
{chr(10).join(objects)}
  )
  (:init
{chr(10).join(init)}
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
    parser = argparse.ArgumentParser(description="Generate an Elevators PDDL problem.")
    parser.add_argument("num_areas", type=int)
    parser.add_argument("area_size", type=int)
    parser.add_argument("num_passengers", type=int)
    parser.add_argument("num_fast_elevators", type=int)
    parser.add_argument("num_slow_elevators", type=int, nargs="?", default=1, help="per area (default: 1)")
    parser.add_argument("--fast-cost", type=int, default=3)
    parser.add_argument("--stop-fast-cost", type=int, default=1)
    parser.add_argument("--fast-capacity", type=int, default=3)
    parser.add_argument("--slow-cost", type=int, default=1)
    parser.add_argument("--stop-slow-cost", type=int, default=5)
    parser.add_argument("--slow-capacity", type=int, default=2)
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
