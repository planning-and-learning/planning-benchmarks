"""Miconic as generated for the IPC, conditioned on no floor being both an origin and a destination.

Trips are the IPC generator's (ipc/miconic: origin uniform, destination uniform among the
other floors) conditioned on the origin floors and the destination floors being disjoint,
sampled exactly rather than by rejection: the number a of distinct origin floors has
conditional weight C(F, a) * surj(P, a) * (F - a)^P (surj counts the maps of the P
passengers onto a floors), the origin floors are a uniform a-subset, the passengers'
origins a uniformly random surjection onto them, and every destination is uniform over
the other floors. The lift starts at f0 as in the IPC tasks (lift_start="random" draws
it as the IPC 2023 learning track does).

The lift reaches any floor in one move. Each passenger costs board + depart, every
origin floor must be visited, and every destination floor must be visited after
some origin. So at least |origins| + |destinations| moves are needed, one less if
the lift starts at an origin floor; visiting all origins and then all
destinations meets that bound.
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time


def _problem(name: str, num_floors: int, lift: int, trips: list[tuple[int, int]]) -> str:
    origins = {origin for origin, _ in trips}
    cost = 2 * len(trips) + len(origins) + len({destination for _, destination in trips}) - (lift in origins)
    passengers = [f"p{i}" for i in range(len(trips))]
    floors = [f"f{i}" for i in range(num_floors)]
    init = [
        *(f"(passenger {passenger})" for passenger in passengers),
        *(f"(floor {floor})" for floor in floors),
        *(f"(above f{i} f{j})" for i in range(num_floors) for j in range(i + 1, num_floors)),
        *(f"(origin {p} f{origin})\n    (destin {p} f{destin})" for p, (origin, destin) in zip(passengers, trips)),
        f"(lift-at f{lift})",
    ]
    return f"""; optimal plan cost: {cost}
(define (problem {name}-f{num_floors}-p{len(trips)})
  (:domain miconic)
  (:objects {' '.join([*passengers, *floors])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      (served {passenger})' for passenger in passengers)}
    )
  )
)
"""


def _surjection_counts(num_items: int, max_blocks: int) -> list[list[int]]:
    """count[n][k]: maps of n labelled items onto k labelled targets (k! times a Stirling number)."""
    stirling = [[0] * (max_blocks + 1) for _ in range(num_items + 1)]
    stirling[0][0] = 1
    for n in range(1, num_items + 1):
        for k in range(1, min(n, max_blocks) + 1):
            stirling[n][k] = k * stirling[n - 1][k] + stirling[n - 1][k - 1]
    return [[math.factorial(k) * stirling[n][k] for k in range(max_blocks + 1)] for n in range(num_items + 1)]


def _weighted_index(rng: random.Random, weights: list[int]) -> int:
    """Index drawn with probability proportional to its (arbitrarily large integer) weight."""
    draw = rng.randrange(sum(weights))
    for index, weight in enumerate(weights):
        if draw < weight:
            return index
        draw -= weight
    raise ValueError("weights must be non-negative and not all zero")


def _random_surjection(rng: random.Random, num_items: int, targets: list[int]) -> list[int]:
    """A uniformly random map of range(num_items) onto all of ``targets``."""
    size = len(targets)
    # ways[r][k]: completions with r items left and k blocks started that end with exactly size blocks
    ways = [[0] * (size + 2) for _ in range(num_items + 1)]
    ways[0][size] = 1
    for r in range(1, num_items + 1):
        for k in range(size + 1):
            ways[r][k] = k * ways[r - 1][k] + ways[r - 1][k + 1]
    blocks: list[int] = []  # block index per item, blocks numbered by first appearance
    started = 0
    for item in range(num_items):
        left = num_items - item - 1
        joining = started * ways[left][started]  # join one of the started blocks, or start a new one
        draw = rng.randrange(joining + ways[left][started + 1])
        block = draw // ways[left][started] if draw < joining else started
        started += block == started
        blocks.append(block)
    labels = rng.sample(targets, size)  # a uniform labelling of the uniformly random partition
    return [labels[block] for block in blocks]


def make_problem(num_floors: int, num_passengers: int, seed: int | None = None, lift_start: str = "bottom") -> str:
    if num_floors < 2:
        raise ValueError("num_floors must be at least 2")
    if num_passengers < 1:
        raise ValueError("num_passengers must be at least 1")
    if lift_start not in ("bottom", "random"):
        raise ValueError("lift_start must be 'bottom' or 'random'")
    rng = random.Random(seed if seed is not None else int(time.time()))
    most = min(num_passengers, num_floors - 1)
    surjections = _surjection_counts(num_passengers, most)[num_passengers]
    weights = [math.comb(num_floors, a) * surjections[a] * (num_floors - a) ** num_passengers for a in range(most + 1)]
    num_origins = _weighted_index(rng, weights)
    origin_floors = rng.sample(range(num_floors), num_origins)
    others = [floor for floor in range(num_floors) if floor not in origin_floors]
    origins = _random_surjection(rng, num_passengers, origin_floors)
    trips = [(origin, rng.choice(others)) for origin in origins]
    lift = rng.randrange(num_floors) if lift_start == "random" else 0
    return _problem("miconic-disjoint", num_floors, lift, trips)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Miconic task with disjoint origin and destination floors.")
    parser.add_argument("-f", "--num-floors", type=int, required=True)
    parser.add_argument("-p", "--num-passengers", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--lift-start", choices=("bottom", "random"), default="bottom",
                        help="lift at f0 as in the IPC tasks, or on a random floor as in the IPC 2023 learning track")
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_floors, args.num_passengers, args.seed, args.lift_start), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
