#!/usr/bin/env python3
# Generator for the IPC-1998 Mystery encoding (Drew McDermott). pddl-generators'
# mystery/mystery.c is a typed, renamed adaptation with a ring road and a goal for every
# cargo; this generator instead follows the distribution measured on the IPC tasks
# (see README.md), including their obfuscated names.

from __future__ import annotations

import argparse
import random
import sys
from collections.abc import Sequence

# Names observed in the IPC-1998 mystery/mprime tasks, per role.
LOCATIONS = (
    "apple arugula bacon baguette beef broccoli cantelope cherry chicken chocolate cod cucumber endive "
    "flounder grapefruit guava ham hamburger haroset hotdog kale lamb lemon lettuce lobster marzipan melon "
    "muffin mutton okra onion orange papaya pea pear pepper pistachio popover pork potato rice scallion "
    "scallop shrimp snickers sweetroll tofu tomato tuna turkey wonderbread wurst yogurt"
).split()
VEHICLES = (
    "achievement aesthetics curiosity empathy entertainment excitement expectation intoxication learning "
    "love lubricity rest satiety satisfaction stimulation triumph understanding"
).split()
CARGOS = (
    "abrasion anger angina anxiety boils depression dread grief hangover jealousy laceration loneliness "
    "prostatitis sciatica"
).split()
FUELS = (
    "alsace arizona bavaria bosnia goias guanabara kentucky manitoba moravia oregon pennsylvania quebec surrey"
).split()
SPACES = "earth jupiter mars mercury neptune pluto saturn uranus venus vulcan".split()


def _pair(a: int, b: int) -> tuple[int, int]:
    """The undirected edge {a, b} as a sorted pair."""
    return (a, b) if a <= b else (b, a)


def _names(rng: random.Random, pool: Sequence[str], count: int) -> list[str]:
    """``count`` distinct names: a random sample of the pool, then ``<name>-<k>`` once it runs out."""
    names = rng.sample(pool, min(count, len(pool)))
    names += [f"{rng.choice(pool)}-{k}" for k in range(1, count - len(names) + 1)]
    rng.shuffle(names)
    return names


def _roads(rng: random.Random, n: int) -> set[tuple[int, int]]:
    """Every location links to one random other, components are joined, degree-1 nodes get a second road."""
    edges = {_pair(i, rng.choice([j for j in range(n) if j != i])) for i in range(n)}
    component = list(range(n))

    def find(x: int) -> int:
        while component[x] != x:
            component[x] = component[component[x]]
            x = component[x]
        return x

    for a, b in edges:
        component[find(a)] = find(b)
    while len({find(i) for i in range(n)}) > 1:
        a = rng.randrange(n)
        b = rng.choice([i for i in range(n) if find(i) != find(a)])
        edges.add(_pair(a, b))
        component[find(a)] = find(b)
    while True:
        degree = [0] * n
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        low = [i for i in range(n) if degree[i] < 2]
        if not low or n < 3:
            return edges
        a = rng.choice(low)
        b = rng.choice([i for i in range(n) if i != a and _pair(a, i) not in edges])
        edges.add(_pair(a, b))


def make_problem(
    num_locations: int,
    num_vehicles: int,
    num_cargos: int,
    num_fuel_levels: int,
    num_space_levels: int,
    num_goals: int,
    seed: int | None = None,
    prime: bool = False,
) -> str:
    """Generate an IPC-1998 Mystery task (``prime`` for the Mystery Prime domain).

    Fuel at each location is uniform over the ``num_fuel_levels`` levels; each
    vehicle's free space is uniform over 1..``num_space_levels - 1``. Vehicles start
    at pairwise distinct uniform locations, cargos at uniform locations; ``num_goals`` distinct random cargos get a
    uniform destination (possibly their start). Solvability is not guaranteed,
    as in the IPC set.
    """
    checks: list[tuple[str, object, int]] = [
        ("num_locations", num_locations, 2),
        ("num_vehicles", num_vehicles, 1),
        ("num_cargos", num_cargos, 1),
        ("num_fuel_levels", num_fuel_levels, 2),
        ("num_space_levels", num_space_levels, 2),
        ("num_goals", num_goals, 1),
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_goals > num_cargos:
        raise ValueError("num_goals must not exceed num_cargos")
    if num_vehicles > num_locations:
        raise ValueError("num_vehicles must not exceed num_locations")

    rng = random.Random(seed)
    locations = _names(rng, LOCATIONS, num_locations)
    vehicles = _names(rng, VEHICLES, num_vehicles)
    cargos = _names(rng, CARGOS, num_cargos)
    fuels = _names(rng, FUELS, num_fuel_levels)
    spaces = _names(rng, SPACES, num_space_levels)

    relations: list[str] = []
    for a, b in _roads(rng, num_locations):
        relations += [f"(eats {locations[a]} {locations[b]})", f"(eats {locations[b]} {locations[a]})"]
    relations += [f"(attacks {fuels[i]} {fuels[i + 1]})" for i in range(num_fuel_levels - 1)]
    relations += [f"(orbits {spaces[i]} {spaces[i + 1]})" for i in range(num_space_levels - 1)]
    relations += [f"(locale {location} {rng.choice(fuels)})" for location in locations]
    relations += [f"(harmony {vehicle} {spaces[rng.randint(1, num_space_levels - 1)]})" for vehicle in vehicles]
    starts = dict(zip(vehicles, rng.sample(locations, num_vehicles)))
    starts.update((cargo, rng.choice(locations)) for cargo in cargos)
    relations += [f"(craves {thing} {location})" for thing, location in starts.items()]
    rng.shuffle(relations)
    goals = [f"(craves {cargo} {rng.choice(locations)})" for cargo in rng.sample(cargos, num_goals)]

    kinds = [("food", locations), ("pleasure", vehicles), ("pain", cargos), ("province", fuels), ("planet", spaces)]
    objects = " ".join(name for _, names in kinds for name in names)
    init = [f"({kind} {name})" for kind, names in kinds for name in names] + relations
    tag = "mprime" if prime else "mysty"
    domain = "mystery-prime-strips" if prime else "mystery-strips"
    parameters = f"l{num_locations}-v{num_vehicles}-c{num_cargos}-f{num_fuel_levels}-s{num_space_levels}-g{num_goals}"
    return (f"""(define (problem strips-{tag}-{parameters})
   (:domain {domain})
   (:objects {objects})
   (:init
{chr(10).join("          " + fact for fact in init)})
   (:goal (and {" ".join(goals)})))
""").lower()


def main(argv: list[str] | None = None, prime: bool = False) -> int:
    title = "Mystery Prime" if prime else "Mystery"
    parser = argparse.ArgumentParser(description=f"Generate an IPC-1998 {title} PDDL problem.")
    parser.add_argument("-l", "--num-locations", type=int, required=True)
    parser.add_argument("-v", "--num-vehicles", type=int, required=True)
    parser.add_argument("-c", "--num-cargos", type=int, required=True)
    parser.add_argument("-f", "--num-fuel-levels", type=int, required=True)
    parser.add_argument("-s", "--num-space-levels", type=int, required=True)
    parser.add_argument("-g", "--num-goals", type=int, required=True)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args), prime=prime)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
