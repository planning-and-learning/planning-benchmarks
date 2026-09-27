#!/usr/bin/env python3
# Numeric Settlers generator reconstructed from the IPC 2023 numeric tasks
# (data/numeric/ipc2023/settlersnumeric, the IPC 2002 numeric Settlers domain by
# Maria Fox and Derek Long). The IPC tasks were written by hand; no generator for
# this encoding is published (pddl-generators/settlers is a discretised STRIPS
# variant).

from __future__ import annotations

import argparse
import random
import sys

RESOURCES = ("wood", "timber", "ore", "stone", "iron", "coal")
SITES = (("woodland", 0.68), ("mountain", 0.38), ("metalliferous", 0.26))
# Goal kinds weighted by their frequency in the 20 IPC tasks.
GOAL_KINDS = (
    ("rail", 45), ("housing", 18), ("has-sawmill", 13), ("has-ironworks", 11), ("has-coal-stack", 11),
    ("available", 1), ("is-ship", 1),
)
P_COAST, P_EXTRA_SEA, P_HOUSING_ONE = 0.55, 0.1, 0.7


def make_problem(
    num_locations: int,
    num_vehicles: int,
    num_goals: int,
    seed: int | None = None,
    num_islands: int = 1,
) -> str:
    """Generate a numeric Settlers task.

    Locations are split into ``num_islands`` land-connected islands (random
    spanning tree plus extra roads, mean degree growing with the island size, as
    in the IPC tasks). Each location is coastal with probability 0.55; islands are
    chained by sea between coastal locations, plus extra sea routes between coastal
    locations with probability 0.1. Sites: woodland 0.68, mountain 0.38,
    metalliferous 0.26 per location, and island 0 has at least one of each, so all
    resources can be produced there and shipped anywhere. All numeric fluents start
    at 0, vehicles are only potential. ``num_goals`` distinct goals are drawn by
    kind with the IPC frequencies: rail along a road, housing >= 1 (p 0.7) or 2,
    sawmill / ironworks / coal stack at a location, timber at a location, a ship.
    The metric weighs pollution, resource use and labour with weights in 0..3.
    """
    for name, value, minimum in (
        ("num_locations", num_locations, 1),
        ("num_vehicles", num_vehicles, 1),
        ("num_goals", num_goals, 1),
        ("num_islands", num_islands, 1),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_islands > num_locations:
        raise ValueError("num_islands must not exceed num_locations")
    rng = random.Random(seed)
    locs = [f"location{i}" for i in range(num_locations)]
    order = list(range(num_locations))
    rng.shuffle(order)
    islands = [sorted(order[k::num_islands]) for k in range(num_islands)]

    land: set[tuple[int, int]] = set()
    for island in islands:
        n = len(island)
        if n < 2:
            continue
        nodes = island[:]
        rng.shuffle(nodes)
        for i in range(1, n):
            land.add(tuple(sorted((nodes[i], nodes[rng.randrange(i)]))))
        degree = 2.4 + 0.25 * n
        spare = n * (n - 1) // 2 - (n - 1)
        p_extra = min(1.0, max(0.0, (degree * n / 2 - (n - 1)) / spare)) if spare else 0.0
        for i, a in enumerate(island):
            for b in island[i + 1 :]:
                if (a, b) not in land and rng.random() < p_extra:
                    land.add((a, b))

    coast = {i for i in range(num_locations) if rng.random() < P_COAST}
    for island in islands[1:] if num_islands > 1 else []:
        if not coast & set(island):
            coast.add(rng.choice(island))
    if num_islands > 1 and not coast & set(islands[0]):
        coast.add(rng.choice(islands[0]))
    sea: set[tuple[int, int]] = set()
    for first, second in zip(islands, islands[1:]):
        a = rng.choice(sorted(coast & set(first)))
        b = rng.choice(sorted(coast & set(second)))
        sea.add(tuple(sorted((a, b))))
    coastal = sorted(coast)
    for i, a in enumerate(coastal):
        for b in coastal[i + 1 :]:
            if (a, b) not in land and rng.random() < P_EXTRA_SEA:
                sea.add((a, b))

    sites = {kind: {i for i in range(num_locations) if rng.random() < p} for kind, p in SITES}
    for kind, _ in SITES:
        if not sites[kind] & set(islands[0]):
            sites[kind].add(rng.choice(islands[0]))

    goals: list[str] = []
    seen: set[str] = set()
    kinds, weights = zip(*GOAL_KINDS)
    roads = sorted(land) + [(b, a) for a, b in sorted(land)]
    for _ in range(100 * num_goals):
        if len(goals) == num_goals:
            break
        kind = rng.choices(kinds, weights)[0]
        if kind == "rail":
            if not roads:
                continue
            a, b = rng.choice(roads)
            key, goal = f"rail {a} {b}", f"(connected-by-rail {locs[a]} {locs[b]})"
        elif kind == "housing":
            loc = rng.randrange(num_locations)
            key = goal = f"housing {loc}"
            goal = f"(>= (housing {locs[loc]}) {1 if rng.random() < P_HOUSING_ONE else 2})"
        elif kind == "available":
            loc = rng.randrange(num_locations)
            key, goal = f"available {loc}", f"(>= (available timber {locs[loc]}) 1)"
        elif kind == "is-ship":
            vehicle = rng.randrange(num_vehicles)
            key, goal = f"ship {vehicle}", f"(is-ship vehicle{vehicle})"
        else:
            loc = rng.randrange(num_locations)
            key, goal = f"{kind} {loc}", f"({kind} {locs[loc]})"
        if key not in seen:
            seen.add(key)
            goals.append(goal)
    if len(goals) < num_goals:
        raise ValueError(f"only {len(goals)} distinct goals exist for this map")

    init = ["(= (resource-use) 0)", "(= (labour) 0)", "(= (pollution) 0)"]
    for i in range(num_locations):
        init += [f"({kind} {locs[i]})" for kind, _ in SITES if i in sites[kind]]
        if i in coast:
            init.append(f"(by-coast {locs[i]})")
        init += [f"(= (housing {locs[i]}) 0)", f"(= (carts-at {locs[i]}) 0)"]
        init += [f"(= (available {r} {locs[i]}) 0)" for r in RESOURCES]
    for relation, edges in (("connected-by-land", land), ("connected-by-sea", sea)):
        for a, b in sorted(edges):
            init += [f"({relation} {locs[a]} {locs[b]})", f"({relation} {locs[b]} {locs[a]})"]
    init += [f"(potential vehicle{v})" for v in range(num_vehicles)]
    w = [rng.randrange(4) for _ in range(3)]
    objects = [f"\t{loc} - place" for loc in locs] + [f"\tvehicle{v} - vehicle" for v in range(num_vehicles)]
    nl, tab = "\n", "\n\t"
    return (f"""(define (problem settlers-l{num_locations}-v{num_vehicles}-g{num_goals}-i{num_islands})
(:domain civ)
(:objects
{nl.join(objects)}
)
(:init
\t{tab.join(init)}
)
(:goal (and
\t{tab.join(goals)}
\t)
)

(:metric minimize (+ (+ (* {w[0]} (pollution)) (* {w[1]} (resource-use))) (* {w[2]} (labour))))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Settlers PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-v", "--num-vehicles", type=int, required=True)
    parser.add_argument("-g", "--num-goals", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("-i", "--num-islands", type=int, default=1, help="land-connected islands (default: 1)")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
