#!/usr/bin/env python3
# Port of pddl-generators driverlog/generator.cc (dlgen, STRIPS, no distances). The
# default is the untyped IPC 2002 encoding; Autoscale calls it typed:
# `dlgen {seed} {roadjunctions} {drivers} {packages} {trucks}`.

from __future__ import annotations

import argparse
import random
import sys
from collections import deque


def _undirected_edges(graph: dict[int, set[int]]) -> list[tuple[int, int]]:
    """Edges as upstream prints them: non-loops, skipping the later copy of a two-way pair."""
    return [
        (source, target)
        for source in sorted(graph)
        for target in sorted(graph[source])
        if source != target and not (source in graph[target] and target < source)
    ]


def make_problem(
    num_locations: int,
    num_drivers: int,
    num_packages: int,
    num_trucks: int,
    seed: int | None = None,
    typed: bool = False,
) -> str:
    """Generate a STRIPS Driverlog task.

    Two random connected graphs over the road junctions: foot paths (via one
    intermediate path location per edge, two attempts per junction) and roads
    (four attempts per junction). Drivers, trucks and packages start at random
    junctions and get a random destination, possibly their start; drivers and
    trucks keep it as a goal with probability 0.7, packages with probability 0.95.
    ``typed`` selects Autoscale's typed encoding instead of the IPC's type predicates.
    """
    for name, value in (
        ("num_locations", num_locations),
        ("num_drivers", num_drivers),
        ("num_packages", num_packages),
        ("num_trucks", num_trucks),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")

    rng = random.Random(seed)
    # Upstream draws path and road attempts interleaved per junction.
    path: dict[int, set[int]] = {i: set() for i in range(num_locations)}
    road: dict[int, set[int]] = {i: set() for i in range(num_locations)}
    for _ in range(num_locations):
        for graph, attempts in ((path, 2), (road, 4)):
            for _ in range(attempts):
                source, target = rng.randrange(num_locations), rng.randrange(num_locations)
                if source not in graph[target]:
                    graph[source].add(target)
    path = _connect(path, rng)
    road = _connect(road, rng)

    def placed(prefix: str, count: int, goal_probability: float) -> list[tuple[str, int, int | None]]:
        entities = []
        for i in range(1, count + 1):
            location, destination = rng.randrange(num_locations), rng.randrange(num_locations)
            entities.append((f"{prefix}{i}", location, destination if rng.random() < goal_probability else None))
        return entities

    drivers = placed("driver", num_drivers, 0.7)
    trucks = placed("truck", num_trucks, 0.7)
    packages = placed("package", num_packages, 0.95)

    def kind(fact: str) -> list[str]:
        return [] if typed else [f"\t({fact})"]

    # Every directed non-loop path edge names a location, even the unused reverse of a two-way pair.
    path_locations = [f"p{source}-{target}" for source in sorted(path) for target in sorted(path[source]) if source != target]
    locations = [f"s{i}" for i in range(num_locations)] + path_locations

    init_facts = []
    for driver, location, _ in drivers:
        init_facts += [f"\t(at {driver} s{location})", *kind(f"driver {driver}")]
    for truck, location, _ in trucks:
        init_facts += [f"\t(at {truck} s{location})", f"\t(empty {truck})", *kind(f"truck {truck}")]
    for package, location, _ in packages:
        init_facts += [f"\t(at {package} s{location})", *kind(f"obj {package}")]
    for location in locations:
        init_facts += kind(f"location {location}")
    for source, target in _undirected_edges(path):
        middle = f"p{source}-{target}"
        init_facts.extend(
            f"\t(path {a} {b})"
            for a, b in ((f"s{source}", middle), (middle, f"s{source}"), (f"s{target}", middle), (middle, f"s{target}"))
        )
    for source, target in _undirected_edges(road):
        init_facts.append(f"\t(link s{source} s{target})")
        init_facts.append(f"\t(link s{target} s{source})")

    goals = [
        f"\t(at {name} s{destination})"
        for name, _, destination in [*drivers, *trucks, *packages]
        if destination is not None
    ]
    def declare(names: list[str], type_name: str) -> list[str]:
        return [f"\t{name} - {type_name}" if typed else f"\t{name}" for name in names]

    objects = [
        *declare([driver for driver, _, _ in drivers], "driver"),
        *declare([truck for truck, _, _ in trucks], "truck"),
        *declare([package for package, _, _ in packages], "obj"),
        *declare(locations, "location"),
    ]
    return (f"""(define (problem DLOG-l{num_locations}-{num_drivers}-{num_trucks}-{num_packages})
\t(:domain driverlog)
\t(:objects
{chr(10).join(objects)}
\t)
\t(:init
{chr(10).join(init_facts)}
)
\t(:goal (and
{chr(10).join(goals)}
\t))

)
""").lower()


def _connect(graph: dict[int, set[int]], rng: random.Random) -> dict[int, set[int]]:
    """Chain unreached junctions until everything is reachable from a random start."""
    num_locations = len(graph)
    reached: set[int] = set()

    def explore(start: int) -> None:
        queue = deque([start])
        reached.add(start)
        while queue:
            for neighbour in graph[queue.popleft()]:
                if neighbour not in reached:
                    reached.add(neighbour)
                    queue.append(neighbour)

    start = rng.randrange(num_locations)
    explore(start)
    while len(reached) != num_locations:
        following = min(set(range(num_locations)) - reached)
        graph[start].add(following)
        start = following
        explore(start)
    return graph


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a STRIPS Driverlog PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True, help="number of road junctions")
    parser.add_argument("-d", "--num-drivers", type=int, required=True)
    parser.add_argument("-p", "--num-packages", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--typed", action="store_true", help="typed encoding instead of type predicates")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
