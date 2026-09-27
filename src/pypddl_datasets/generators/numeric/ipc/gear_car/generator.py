#!/usr/bin/env python3
# Gear Car (IPC 2026 numeric). No generator was published; this reconstructs the
# 20 IPC tasks, whose gear tables are a fixed function of the number of gears and
# whose fuel budget and cost weights follow from the optimal plans (see README).

from __future__ import annotations

import argparse
import heapq
import math
import sys

MAX_ACCELERATION, MIN_ACCELERATION, ACC_STEP = 2, -1, 1


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def gear_table(num_gears: int) -> list[dict[str, int]]:
    """Per-gear speed band, acceleration band and fuel per drive, as in the IPC tasks."""
    over_first = 15 + num_gears
    return [
        {
            "v_min": 2 * (i - 1),
            "v_max": 2 * i,
            "min_acceleration": -1,
            "max_acceleration": 2 if i == 1 else (0 if i == num_gears else 1),
            "fuel_aligned": 11 if i == 1 else 11 - i,
            "fuel_under": 18 if i == 1 else 17,
            "fuel_over": over_first if i == 1 else over_first - 3 - 2 * (i - 2),
        }
        for i in range(1, num_gears + 1)
    ]


State = tuple[int, int, int, int]


def _optimum(num_gears: int, distance: int, fuel_first: bool) -> tuple[int, int]:
    """Lexicographic optimum over plans reaching d in [distance, distance+2], stopped in gear 1.

    Returns (fuel, drives) if ``fuel_first`` else (drives, fuel). Acceleration and gear
    changes are free; only drive actions move, cost time and fuel.
    """
    gears, max_speed = gear_table(num_gears), 2 * num_gears
    start: State = (0, 0, 0, 0)  # distance, speed, acceleration, gear index
    best: dict[State, tuple[int, int]] = {start: (0, 0)}
    queue: list[tuple[tuple[int, int], State]] = [((0, 0), start)]
    while queue:
        cost, state = heapq.heappop(queue)
        if best[state] != cost:
            continue
        d, v, a, g = state
        if distance <= d <= distance + 2 and v == 0 and a == 0 and g == 0:
            return cost
        gear = gears[g]
        moves: list[tuple[State, int, int]] = []  # next state, drives, fuel
        if a + ACC_STEP <= min(MAX_ACCELERATION, gear["max_acceleration"]):
            moves.append(((d, v, a + ACC_STEP, g), 0, 0))
        if a - ACC_STEP >= max(MIN_ACCELERATION, gear["min_acceleration"]):
            moves.append(((d, v, a - ACC_STEP, g), 0, 0))
        if a == 0:
            moves += [((d, v, a, h), 0, 0) for h in (g - 1, g + 1) if 0 <= h < num_gears]
        if 0 <= v + a <= max_speed and d + 2 * v + a <= distance + 2:
            if v < gear["v_min"]:
                fuel = gear["fuel_under"]
            elif v > gear["v_max"]:
                fuel = gear["fuel_over"]
            else:
                fuel = gear["fuel_aligned"]
            moves.append(((d + 2 * v + a, v + a, a, g), 1, fuel))
        for nxt, drives, fuel in moves:
            new = (cost[0] + fuel, cost[1] + drives) if fuel_first else (cost[0] + drives, cost[1] + fuel)
            if new < best.get(nxt, (math.inf, math.inf)):
                best[nxt] = new
                heapq.heappush(queue, (new, nxt))
    raise ValueError(f"distance {distance} cannot be reached with {num_gears} gears")


def make_problem(num_gears: int, distance: int) -> str:
    """Generate a Gear Car task: drive ``distance`` and stop in gear 1.

    Deterministic, like the IPC tasks: the fuel budget is ceil(1.2 * F) + 10 for the
    minimum fuel F of any plan, beta approximates ceil(1.2 * T) + 5 * num_gears - 6 for
    the minimum number of drive steps T (within 2 of every IPC task), and
    alpha = beta * (fuel + 1).
    """
    for name, value, minimum in (("num_gears", num_gears, 2), ("distance", distance, 1)):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    min_fuel = _optimum(num_gears, distance, fuel_first=True)[0]
    min_drives = _optimum(num_gears, distance, fuel_first=False)[0]
    fuel = math.ceil(1.2 * min_fuel) + 10
    beta = math.ceil(1.2 * min_drives) + 5 * num_gears - 6
    alpha = beta * (fuel + 1)

    names = [f"g{i}" for i in range(1, num_gears + 1)]
    gear_facts: list[str] = []
    for name, gear in zip(names, gear_table(num_gears)):
        gear_facts += [
            f"        (= (gear_v_min {name}) {gear['v_min']})",
            f"        (= (gear_v_max {name}) {gear['v_max']})",
            f"        (= (gear_min_acceleration {name}) {gear['min_acceleration']})",
            f"        (= (gear_max_acceleration {name}) {gear['max_acceleration']})",
            f"        (= (gear_fuel_aligned {name}) {gear['fuel_aligned']})",
            f"        (= (gear_fuel_under {name}) {gear['fuel_under']})",
            f"        (= (gear_fuel_over {name}) {gear['fuel_over']})",
        ]
    nexts = "\n".join(f"        (gear_next {a} {b})" for a, b in zip(names, names[1:]))
    return (f"""(define (problem car_linear_gears_g{num_gears}_d{distance})
    (:domain car_linear_gears_numeric)
    (:objects
        {' '.join(names)} - gear
    )
    (:init
        (current_gear g1)
{nexts}
        (= (d) 0)
        (= (v) 0)
        (= (a) 0)
        (= (max_acceleration) {MAX_ACCELERATION})
        (= (min_acceleration) {MIN_ACCELERATION})
        (= (max_speed) {2 * num_gears})
        (= (acc_step) {ACC_STEP})
        (= (fuel) {fuel})
        (= (fuel_used) 0)
        (= (elapsed_time) 0)
        (= (cost) 0)
        (= (alpha) {alpha})
        (= (beta) {beta})
        (= (shift_count) 0)
{chr(10).join(gear_facts)}
    )
    (:goal
        (and
            (>= (d) {distance})
            (<= (d) {distance + 2})
            (current_gear g1)
            (= (v) 0)
            (= (a) 0)
            (>= (fuel) 0)
            (> (fuel_used) 0)
        )
    )
    (:metric minimize (cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Gear Car PDDL problem.")
    parser.add_argument("-g", "--num-gears", type=int, required=True)
    parser.add_argument("-d", "--distance", type=int, required=True)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
