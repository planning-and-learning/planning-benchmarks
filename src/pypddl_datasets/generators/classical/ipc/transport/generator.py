#!/usr/bin/env python3
"""Port of pddl-generators transport/{city,two-cities,three-cities}-generator.py
and euclidean_graph.py, the generators behind the IPC 2008-2014 and Autoscale 21.11
tasks. Default: cost-free encoding (domain.pddl); ``action_costs=True``: the IPC
encoding with road lengths (domain_action_costs.pddl)."""

from __future__ import annotations

import argparse
import math
import random
import sys
from typing import cast

KINDS = ("city", "two-cities", "three-cities")
MAX_CAPACITY = 4
MAX_EPSILON_ATTEMPTS = 1000

Point = tuple[int, int]
City = tuple[list[Point], list[tuple[int, int]]]  # locations, directed roads
Connection = tuple[tuple[int, int], tuple[int, int], float]  # (city, node) pairs and road length


def _distance(a: Point, b: Point) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _round_distance(a: Point, b: Point) -> int:
    return int(round(_distance(a, b)))


def _generate(
    rng: random.Random, num_nodes: int, width: int, height: int, connect_distance: float, epsilon: int
) -> City:
    points: list[Point] = []
    edges: list[tuple[int, int]] = []
    for _ in range(num_nodes):
        for _ in range(MAX_EPSILON_ATTEMPTS):
            p = (rng.randrange(width), rng.randrange(height))
            if all(_round_distance(p, q) >= epsilon for q in points):
                break
        else:
            raise ValueError("failed to place vertex")
        points.append(p)
        index = len(points) - 1
        for other, q in enumerate(points):
            if 0 < _round_distance(p, q) <= connect_distance:
                edges.extend([(index, other), (other, index)])
    return points, edges


def _is_connected(num_nodes: int, edges: list[tuple[int, int]]) -> bool:
    reached, frontier = {0}, [0]
    while frontier:
        current = frontier.pop()
        for u, v in edges:
            if u == current and v not in reached:
                reached.add(v)
                frontier.append(v)
    return len(reached) == num_nodes


def _generate_city(rng: random.Random, num_nodes: int, size: int, connect_distance: float, epsilon: int) -> City:
    # generate_connected_safe: on placement failure enlarge the area by 1.5x.
    width = height = size
    while True:
        try:
            while True:
                # upstream's generate_connected bumps the distance once before each try
                connect_distance += 1
                points, edges = _generate(rng, num_nodes, width, height, connect_distance, epsilon)
                if _is_connected(num_nodes, edges):
                    return points, edges
                connect_distance += 1
        except ValueError:
            width = max(width + 1, int(width * 1.5))
            height = max(height + 1, int(height * 1.5))
            connect_distance *= 1.5


def _shortest_route(
    city_a: list[Point], city_b: list[Point], size: int, ox: int, oy: int
) -> tuple[tuple[int, int], float]:
    # Faithful to upstream three-cities-generator.py: always scans cities a x b, compares
    # at offset (ox, oy) but stores the distance at offset (2 * size, 0).
    best, best_distance = (0, 0), -1.0
    for i, v in enumerate(city_a):
        for j, u in enumerate(city_b):
            if best_distance == -1.0 or _distance(v, (u[0] + ox, u[1] + oy)) < best_distance:
                best, best_distance = (i, j), _distance(v, (u[0] + 2 * size, u[1]))
    return best, best_distance


def make_problem(
    kind: str,
    num_nodes: int,
    num_trucks: int,
    num_packages: int,
    degree: int = 3,
    size: int = 1000,
    min_distance: int = 100,
    seed: int | None = None,
    action_costs: bool = False,
) -> str:
    """Generate a Transport task on one, two or three Euclidean cities.

    ``num_nodes`` locations per city; roads connect locations within the
    degree-derived connect distance (retrying until connected), cities are
    joined by single roads. Road lengths are ceil(distance / 10); trucks get
    a random capacity in 2..4. Without ``action_costs`` the task has the same
    roads, objects and goals but no road lengths, total cost or metric.
    """
    if kind not in KINDS:
        raise ValueError(f"kind must be one of {', '.join(KINDS)}")
    for name, value, minimum in (
        ("num_nodes", num_nodes, 2),
        ("num_trucks", num_trucks, 1),
        ("num_packages", num_packages, 1),
        ("degree", degree, 1),
        ("size", size, 1),
        ("min_distance", min_distance, 0),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    num_cities = KINDS.index(kind) + 1
    connect_distance = math.sqrt((degree * size * size) / (num_nodes * math.pi * 0.694))
    cities = [_generate_city(rng, num_nodes, size, connect_distance, min_distance) for _ in range(num_cities)]

    def loc(city: int, node: int) -> str:
        return f"city-loc-{node + 1}" if kind == "city" else f"city-{city + 1}-loc-{node + 1}"

    init_facts = ["    (= (total-cost) 0)"] if action_costs else []
    init_facts.extend(
        f"    (capacity-predecessor capacity-{i} capacity-{i + 1})" for i in range(MAX_CAPACITY)
    )

    def road(a: str, b: str, length: float) -> None:
        init_facts.append(f"    (road {a} {b})")
        if action_costs:
            init_facts.append(f"    (= (road-length {a} {b}) {math.ceil(length / 10.0)})")

    for city, (points, edges) in enumerate(cities):
        for u, v in edges:
            road(loc(city, u), loc(city, v), _round_distance(points[u], points[v]))

    if kind == "two-cities":
        a, b = 0, 0
        length: float = 4 * size
        for i, v in enumerate(cities[0][0]):
            for j, u in enumerate(cities[1][0]):
                distance = _distance(v, (u[0] + 2 * size, u[1]))
                if distance < length:
                    (a, b), length = (i, j), distance
        connections: list[Connection] = [((0, a), (1, b), length)]
    elif kind == "three-cities":
        city_a, city_b = cities[0][0], cities[1][0]
        connections = []
        for first, second, ox, oy in ((0, 1, 2 * size, 0), (0, 2, size, 2 * size), (1, 2, size, -2 * size)):
            (a, b), length = _shortest_route(city_a, city_b, size, ox, oy)
            connections.append(((first, a), (second, b), length))
    else:
        connections = []
    for (c1, n1), (c2, n2), length in connections:
        road(loc(c1, n1), loc(c2, n2), length)
        road(loc(c2, n2), loc(c1, n1), length)

    # Vertex choices draw from city 1's node count; all cities have the same count.
    starts: list[tuple[int, int]] = []
    for package in range(num_packages):
        city = rng.randint(0, 2) if kind == "three-cities" else 0
        starts.append((city, rng.randrange(num_nodes)))
        init_facts.append(f"    (at package-{package + 1} {loc(*starts[-1])})")
    for truck in range(num_trucks):
        city = rng.randint(0, 2) if kind == "three-cities" else num_cities - 1
        init_facts.append(f"    (at truck-{truck + 1} {loc(city, rng.randrange(num_nodes))})")
        init_facts.append(f"    (capacity truck-{truck + 1} capacity-{rng.randint(2, MAX_CAPACITY)})")

    goals: list[str] = []
    for package, start in enumerate(starts):
        if kind == "two-cities":
            target = (1, rng.randrange(num_nodes))
        else:
            target = start
            while target == start:
                city = rng.randint(0, 2) if kind == "three-cities" else 0
                target = (city, rng.randrange(num_nodes))
        goals.append(f"      (at package-{package + 1} {loc(*target)})")

    name = (
        f"{kind}-sequential-{num_nodes}nodes-{size}size-{degree}degree-{min_distance}mindistance"
        f"-{num_trucks}trucks-{num_packages}packages-{seed}seed"
    )
    locations = [loc(city, node) for node in range(num_nodes) for city in range(num_cities)]
    return (f"""(define (problem transport-{name})
  (:domain transport)
  (:objects
    {' '.join(locations)} - location
    {' '.join(f"truck-{i + 1}" for i in range(num_trucks))} - vehicle
    {' '.join(f"package-{i + 1}" for i in range(num_packages))} - package
    {' '.join(f"capacity-{i}" for i in range(MAX_CAPACITY + 1))} - capacity-number
  )
  (:init
{chr(10).join(init_facts)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
{"  (:metric minimize (total-cost))" + chr(10) if action_costs else ""})
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC-style Transport PDDL problem.")
    parser.add_argument("kind", choices=KINDS)
    parser.add_argument("num_nodes", type=int, help="locations per city")
    parser.add_argument("num_trucks", type=int)
    parser.add_argument("num_packages", type=int)
    parser.add_argument("-d", "--degree", type=int, default=3, help="target average road degree (default: 3)")
    parser.add_argument("--size", type=int, default=1000, help="city side length (default: 1000)")
    parser.add_argument("--min-distance", type=int, default=100, help="minimum location distance (default: 100)")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument(
        "--action-costs", action="store_true", help="IPC encoding with road lengths and a total-cost metric"
    )
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
