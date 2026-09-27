#!/usr/bin/env python3
# Reconstructed from the IPC 2026 settlers-snp tasks (data/numeric/ipc2026/settlers-snp; domain and
# tasks by Enrico Scala and Miquel Ramirez, after Patrik Haslum's IPC 2002 Settlers); no generator
# was published. Location properties, map density and goal kinds follow the measured tasks.

from __future__ import annotations

import argparse
import random
import sys

RESOURCES = ("wood", "timber", "ore", "stone", "iron", "coal")
VEHICLE_RESOURCES = ("timber", "wood", "coal", "stone", "iron", "ore")
# Per-location property rates measured over the 20 reference tasks.
PROPERTIES = (("mountain", 0.44), ("woodland", 0.74), ("by-coast", 0.52), ("metalliferous", 0.29))
# Goal kinds per draw, from the reference goals (106 rail, 46 housing, 32/31/26 buildings);
# a rail draw adds a walk of several links, so its weight is lowered to 50 (measured: 0.44 rail).
GOAL_KINDS = (("rail", 50), ("housing", 46), ("has-ironworks", 32), ("has-sawmill", 31), ("has-coal-stack", 26))


def make_problem(
    num_locations: int,
    num_vehicles: int | None = None,
    num_goals: int | None = None,
    land_density: float | None = None,
    seed: int | None = None,
) -> str:
    """Generate a Settlers task: an empty world, potential vehicles, building goals.

    Every location draws woodland/mountain/metalliferous/by-coast independently
    (each property present somewhere); roads form a connected random graph with
    ``land_density`` of all pairs (default decreases from 0.68 at 5 locations to
    0.43 at 15, as the reference tasks); sea links join coastal pairs. Goals mix
    housing (1 or 2), coal stacks, sawmills, ironworks and rail links, the rail
    links as short walks along roads.
    """
    if not isinstance(num_locations, int) or isinstance(num_locations, bool) or num_locations < 2:
        raise ValueError("num_locations must be an integer at least 2")
    rng = random.Random(seed)
    n = num_locations
    num_vehicles = min(n, 10) if num_vehicles is None else num_vehicles
    num_goals = rng.randint(max(1, n - 2), max(2, int(1.6 * n))) if num_goals is None else num_goals
    land_density = max(0.0, 0.8 - 0.025 * n) if land_density is None else land_density
    for label, value in (("num_vehicles", num_vehicles), ("num_goals", num_goals)):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{label} must be an integer at least 1")
    if not 0 <= land_density <= 1:
        raise ValueError("land_density must be in [0, 1]")

    locs = [f"location{i}" for i in range(n)]
    props = {p: {l for l in locs if rng.random() < rate} for p, rate in PROPERTIES}
    for p in props.values():  # every resource must be obtainable somewhere
        if not p:
            p.add(rng.choice(locs))
    # connected land graph: random spanning tree, then extra pairs up to the density
    order = rng.sample(range(n), n)
    edges = {frozenset((order[i], order[rng.randrange(i)])) for i in range(1, n)}
    pairs = [frozenset((a, b)) for a in range(n) for b in range(a + 1, n)]
    extra = [e for e in pairs if e not in edges]
    rng.shuffle(extra)
    edges |= set(extra[: max(0, round(land_density * len(pairs)) - len(edges))])
    coast = sorted(props["by-coast"], key=locs.index)
    sea_pairs = [(a, b) for i, a in enumerate(coast) for b in coast[i + 1:]]
    seas = rng.sample(sea_pairs, rng.randint(0, min(len(sea_pairs), len(coast)))) if sea_pairs else []

    init = ["(= (resource-use) 0) (= (labour) 0) (= (pollution) 0)"]
    for l in locs:
        init += [f"({p} {l})" for p, _ in PROPERTIES if l in props[p]]
        init += [f"(= (housing {l}) 0)"] + [f"(= (available {r} {l}) 0)" for r in RESOURCES]
    for e in sorted(edges, key=sorted):
        a, b = sorted(e)
        init += [f"(connected-by-land {locs[a]} {locs[b]})", f"(connected-by-land {locs[b]} {locs[a]})"]
    for a, b in seas:
        init += [f"(connected-by-sea {a} {b})", f"(connected-by-sea {b} {a})"]
    vehicles = [f"vehicle{i}" for i in range(num_vehicles)]
    for v in vehicles:
        init += [f";;{v}", f"(= (space-in {v}) 0)"] + [f"(= (available {r} {v}) 0)" for r in VEHICLE_RESOURCES]
    init += [f"(potential {v})" for v in vehicles]

    neighbours = {l: [locs[b] for e in edges for a, b in (sorted(e), sorted(e)[::-1]) if locs[a] == l] for l in locs}
    kinds, weights = zip(*GOAL_KINDS)
    goals: list[str] = []
    seen: set[str] = set()
    attempts = 0
    while len(goals) < num_goals and attempts < 100 * num_goals:
        attempts += 1
        kind = rng.choices(kinds, weights)[0]
        place = rng.choice(locs)
        if kind == "housing":
            new = [f"(>= (housing {place}) {rng.randint(1, 2)})"]
            key = [f"housing {place}"]
        elif kind == "rail":  # a walk of 1-5 roads, each road once as a goal
            new, key, current = [], [], place
            for _ in range(rng.randint(1, 5)):
                nxt = rng.choice(neighbours[current])
                new.append(f"(connected-by-rail {current} {nxt})")
                key.append(new[-1])
                current = nxt
        else:
            new, key = [f"({kind} {place})"], [f"({kind} {place})"]
        for g, k in zip(new, key):
            if k not in seen and len(goals) < num_goals:
                seen.add(k)
                goals.append(g)

    decl = " ".join(f"{v} - vehicle" for v in reversed(vehicles)) + " " + " ".join(f"{l} - place" for l in reversed(locs))
    nl = "\n"
    return (f""";; enrico scala (enricos83@gmail.com) and miquel ramirez (miquel.ramirez@gmail.com)
(define (problem settlers) (:domain civ)
 (:objects {decl})
 (:init
{nl.join(f"  {f}" for f in init)})
 (:goal
    (and {' '.join(goals)}))
(:metric minimize (+ (+ (* 1 (pollution)) (* 1 (resource-use))) (* 1 (labour))))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a settlers-snp PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-v", "--num-vehicles", type=int)
    parser.add_argument("-g", "--num-goals", type=int)
    parser.add_argument("-d", "--land-density", type=float)
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
