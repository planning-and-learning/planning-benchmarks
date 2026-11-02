#!/usr/bin/env python3
"""Zenotravel as generated for the IPC with one plane and all people in one city.

The plane and the people's goals are drawn as by the IPC generator (ipc/zenotravel):
the plane starts in a uniform city with fuel level rnd(b * distance) mod 7 for a burn
rate b uniform in 1..5 (distance 1000 as in the IPC tasks; 0 gives fl0) and with
probability 0.3 must end in a uniform city; each person has a goal with probability
0.97, a uniform city (possibly the one it is in). A draw without any goal is repeated.

At unit cost a zoom (one action, two fuel levels) never beats a fly (one action, one
level), and refuelling adds one level per action anywhere. With m flights the optimal
cost is 2 per person to move (board + debark) + m + max(0, m - initial fuel), where m
is one flight to the origin unless the plane is there, one per destination city, and
one more to the plane's goal unless that is a destination (with nobody to move, one
flight to the plane's goal unless the plane is there).
"""

from __future__ import annotations

import argparse
import random
import sys
import time

NUM_FUEL_LEVELS = 7


def _problem(
    name: str, num_cities: int, plane: int, fuel: int, plane_goal: int | None,
    people: list[tuple[int, int | None]], cost: int,
) -> str:
    names = [f"person{i}" for i in range(len(people))]
    cities = [f"city{i}" for i in range(num_cities)]
    levels = [f"fl{i}" for i in range(NUM_FUEL_LEVELS)]
    init = [
        "(aircraft plane0)",
        f"(at plane0 city{plane})",
        f"(fuel-level plane0 fl{fuel})",
        *(f"(person {p})\n    (at {p} city{origin})" for p, (origin, _) in zip(names, people)),
        *(f"(city {city})" for city in cities),
        *(f"(next {a} {b})" for a, b in zip(levels, levels[1:])),
        *(f"(flevel {level})" for level in levels),
    ]
    goals = [f"(at {p} city{goal})" for p, (_, goal) in zip(names, people) if goal is not None]
    if plane_goal is not None:
        goals.append(f"(at plane0 city{plane_goal})")
    return f"""; optimal plan cost: {cost}
(define (problem {name}-c{num_cities}-p{len(people)})
  (:domain zeno-travel)
  (:objects plane0 {' '.join([*names, *cities, *levels])})
  (:init
{chr(10).join(f'    {fact}' for fact in init)}
  )
  (:goal
    (and
{chr(10).join(f'      {goal}' for goal in goals)}
    )
  )
)
"""


def make_problem(num_cities: int, num_people: int, distance: int = 1000, seed: int | None = None) -> str:
    if num_cities < 1:
        raise ValueError("num_cities must be at least 1")
    if num_people < 1:
        raise ValueError("num_people must be at least 1")
    if distance < 0:
        raise ValueError("distance must be non-negative")
    rng = random.Random(seed if seed is not None else int(time.time()))
    plane, plane_destination = rng.randrange(num_cities), rng.randrange(num_cities)
    fuel = rng.randrange(rng.randint(1, 5) * distance) % NUM_FUEL_LEVELS if distance else 0
    while True:  # a task without any goal (probability 0.7 * 0.03^people in the IPC) is redrawn
        plane_goal = plane_destination if rng.random() >= 0.7 else None
        origin = rng.randrange(num_cities)
        people: list[tuple[int, int | None]] = []
        for _ in range(num_people):
            destination = rng.randrange(num_cities)
            people.append((origin, destination if rng.random() >= 0.03 else None))
        destinations = {goal for _, goal in people if goal is not None and goal != origin}
        moved = sum(goal is not None and goal != origin for _, goal in people)
        if destinations:
            extra = plane_goal is not None and plane_goal not in destinations
            flights = (plane != origin) + len(destinations) + extra
        else:
            flights = int(plane_goal is not None and plane_goal != plane)
        if plane_goal is not None or any(goal is not None for _, goal in people):
            break
    cost = 2 * moved + flights + max(0, flights - fuel)
    return _problem("zenotravel-common-origin", num_cities, plane, fuel, plane_goal, people, cost)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Zenotravel task with all people in one city.")
    parser.add_argument("-c", "--num-cities", type=int, required=True)
    parser.add_argument("-p", "--num-people", type=int, required=True)
    parser.add_argument("-d", "--distance", type=int, default=1000,
                        help="distance bound randomising the fuel, 0 for no fuel (default: 1000, the IPC tasks')")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_cities, args.num_people, args.distance, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
