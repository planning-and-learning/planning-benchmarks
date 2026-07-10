#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
from functools import cache
from heapq import heappop, heappush


def _shortest_paths(graph: list[list[int | None]]) -> list[list[int]]:
    num_locations = len(graph)
    infinity = 10**18
    distances = [
        [
            0 if source == target else graph[source][target] or infinity
            for target in range(num_locations)
        ]
        for source in range(num_locations)
    ]
    for middle in range(num_locations):
        for source in range(num_locations):
            through_middle = distances[source][middle]
            for target in range(num_locations):
                distances[source][target] = min(
                    distances[source][target],
                    through_middle + distances[middle][target],
                )
    return distances


def _minimum_fuel(
    distances: list[list[int]],
    truck_start: int,
    package_starts: list[int],
    package_goals: list[int],
) -> int:
    num_locations = len(distances)
    goals_per_start = [set() for _ in range(num_locations)]
    starts_per_goal = [set() for _ in range(num_locations)]
    for start, goal in zip(package_starts, package_goals):
        goals_per_start[start].add(goal)
        starts_per_goal[goal].add(start)

    load_mask = 0
    for start in package_starts:
        load_mask |= 1 << start

    deliveries = [
        len(starts) if starts else -1 for starts in starts_per_goal
    ]
    load_mask &= ~(1 << truck_start)
    for goal in goals_per_start[truck_start]:
        deliveries[goal] -= 1

    initial_state = (truck_start, load_mask, tuple(deliveries))

    @cache
    def heuristic(state: tuple[int, int, tuple[int, ...]]) -> int:
        truck, pending_loads, pending_deliveries = state
        active = [
            location
            for location in range(num_locations)
            if pending_loads & (1 << location)
            or pending_deliveries[location] >= 0
        ]
        minimum = {
            location: distances[truck][location] for location in active
        }
        value = 0
        while active:
            location = min(active, key=minimum.__getitem__)
            value += minimum.pop(location)
            active.remove(location)
            for other in active:
                minimum[other] = min(
                    minimum[other], distances[location][other]
                )
        return value

    initial_h = heuristic(initial_state)
    open_list = [(initial_h, initial_h, 0, initial_state)]
    best_cost = {initial_state: 0}

    while open_list:
        _, _, cost, state = heappop(open_list)
        if cost != best_cost.get(state):
            continue

        truck, pending_loads, pending_deliveries = state
        if all(value < 0 for value in pending_deliveries):
            return cost

        for location in range(num_locations):
            bit = 1 << location
            if not pending_loads & bit:
                continue

            new_deliveries = list(pending_deliveries)
            if new_deliveries[location] == 0:
                new_deliveries[location] = -1
            for goal in goals_per_start[location]:
                new_deliveries[goal] -= 1

            successor = (
                location,
                pending_loads & ~bit,
                tuple(new_deliveries),
            )
            successor_cost = cost + distances[truck][location]
            if successor_cost < best_cost.get(successor, 10**18):
                best_cost[successor] = successor_cost
                successor_h = heuristic(successor)
                heappush(
                    open_list,
                    (
                        successor_cost + successor_h,
                        successor_h,
                        successor_cost,
                        successor,
                    ),
                )

        for location, remaining in enumerate(pending_deliveries):
            if remaining != 0 or pending_loads & (1 << location):
                continue

            new_deliveries = list(pending_deliveries)
            new_deliveries[location] = -1
            successor = (
                location,
                pending_loads,
                tuple(new_deliveries),
            )
            successor_cost = cost + distances[truck][location]
            if successor_cost < best_cost.get(successor, 10**18):
                best_cost[successor] = successor_cost
                successor_h = heuristic(successor)
                heappush(
                    open_list,
                    (
                        successor_cost + successor_h,
                        successor_h,
                        successor_cost,
                        successor,
                    ),
                )

    raise RuntimeError("connected nomystery instance has no solution")


def make_problem(
    num_locations: int = 6,
    num_packages: int = 6,
    edge_factor: float = 1.5,
    max_edge_cost: int = 25,
    constrainedness: float = 1.0,
    seed: int = 1,
) -> str:
    rng = random.Random(seed)
    graph: list[list[int | None]] = [
        [None] * num_locations for _ in range(num_locations)
    ]

    connected = {rng.randrange(num_locations)}
    num_edges = 0
    while len(connected) < num_locations:
        source = rng.choice(sorted(connected))
        target = rng.choice(
            [
                location
                for location in range(num_locations)
                if location not in connected
            ]
        )
        edge_cost = rng.randint(1, max_edge_cost)
        graph[source][target] = graph[target][source] = edge_cost
        connected.add(target)
        num_edges += 1

    requested_edges = int(edge_factor * num_locations)
    missing_edges = [
        (source, target)
        for source in range(num_locations)
        for target in range(source + 1, num_locations)
        if graph[source][target] is None
    ]
    while num_edges < requested_edges and missing_edges:
        source, target = missing_edges.pop(rng.randrange(len(missing_edges)))
        edge_cost = rng.randint(1, max_edge_cost)
        graph[source][target] = graph[target][source] = edge_cost
        num_edges += 1

    truck_start = rng.randrange(num_locations)
    package_starts = []
    package_goals = []
    for _ in range(num_packages):
        start = rng.randrange(num_locations)
        goal = rng.randrange(num_locations)
        while goal == start:
            goal = rng.randrange(num_locations)
        package_starts.append(start)
        package_goals.append(goal)

    distances = _shortest_paths(graph)
    optimal_fuel = _minimum_fuel(
        distances,
        truck_start,
        package_starts,
        package_goals,
    )
    initial_fuel = int(constrainedness * optimal_fuel)
    max_fuel = max(initial_fuel, max_edge_cost)

    edge_costs = sorted(
        {
            cost
            for row in graph
            for cost in row
            if cost is not None
        }
    )
    sum_facts = [
        f"(sum level{post} level{delta} level{post + delta})"
        for post in range(max_fuel + 1)
        for delta in edge_costs
        if post + delta <= max_fuel
    ]
    road_facts = []
    for source in range(num_locations):
        for target in range(num_locations):
            edge_cost = graph[source][target]
            if edge_cost is not None:
                road_facts.append(f"(connected l{source} l{target})")
                road_facts.append(
                    f"(fuelcost level{edge_cost} l{source} l{target})"
                )

    problem_name = (
        f"transport-l{num_locations}-t1-p{num_packages}"
        f"---int100n{int(100 * edge_factor)}-m{max_edge_cost}"
        f"---int100c{int(100 * constrainedness)}---s{seed}---e0"
    )
    locations = " ".join(f"l{i}" for i in range(num_locations))
    packages = " ".join(f"p{i}" for i in range(num_packages))
    fuel_levels = " ".join(f"level{i}" for i in range(max_fuel + 1))
    init_facts = [
        *sum_facts,
        *road_facts,
        f"(at t0 l{truck_start})",
        f"(fuel t0 level{initial_fuel})",
        "(= (total-cost) 0)",
        *(
            f"(at p{package} l{location})"
            for package, location in enumerate(package_starts)
        ),
    ]
    goals = [
        f"(at p{package} l{location})"
        for package, location in enumerate(package_goals)
    ]
    init = "\n".join(f"    {fact}" for fact in init_facts)
    goal = "\n".join(f"      {fact}" for fact in goals)

    return f"""(define (problem {problem_name})
  (:domain transport-strips)
  (:objects
    {locations} - location
    t0 - truck
    {packages} - package
    {fuel_levels} - fuellevel
  )
  (:init
{init}
  )
  (:goal
    (and
{goal}
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="generate a nomystery pddl problem."
    )
    parser.add_argument(
        "-l", "--num-locations", type=int, default=6
    )
    parser.add_argument(
        "-p", "--num-packages", type=int, default=6
    )
    parser.add_argument(
        "-n", "--edge-factor", type=float, default=1.5
    )
    parser.add_argument(
        "-m", "--max-edge-cost", type=int, default=25
    )
    parser.add_argument(
        "-c", "--constrainedness", type=float, default=1.0
    )
    parser.add_argument("-s", "--seed", type=int, default=1)
    args = parser.parse_args(argv)

    if args.num_locations < 2:
        parser.error("--num-locations must be at least 2")
    if args.num_packages < 1:
        parser.error("--num-packages must be at least 1")
    if args.edge_factor < 1:
        parser.error("--edge-factor must be at least 1")
    if args.max_edge_cost < 1:
        parser.error("--max-edge-cost must be at least 1")
    if args.constrainedness < 1:
        parser.error("--constrainedness must be at least 1")
    if args.seed < 0:
        parser.error("--seed must be non-negative")

    print(
        make_problem(
            args.num_locations,
            args.num_packages,
            args.edge_factor,
            args.max_edge_cost,
            args.constrainedness,
            args.seed,
        ),
        end="",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
