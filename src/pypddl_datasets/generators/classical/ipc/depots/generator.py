#!/usr/bin/env python3
# Port of pddl-generators depots/depots.cc (STRIPS), as called by Autoscale:
# `depots -e {depots} -i {distributors} -t {trucks} -p {pallets} -h {hoists} -c {crates} -s {seed}`.

from __future__ import annotations

import argparse
import random
import sys


def make_problem(
    num_depots: int,
    num_distributors: int,
    num_trucks: int,
    num_pallets: int,
    num_hoists: int,
    num_crates: int,
    seed: int | None = None,
    typed: bool = False,
) -> str:
    """Generate a STRIPS Depots task.

    Places are the depots followed by the distributors. Pallets and hoists are
    raised to at least one per place: the first ``#places`` of each sit one per
    place, the rest at random places. Crates are stacked onto uniformly random
    pallets. Goals come from ``2 * num_crates`` draws of a random crate; a crate
    without a goal yet is stacked onto a random pallet's goal tower, so crates
    drawn only as repeats stay goal-free. ``typed`` selects the typed encoding
    Autoscale uses instead of the IPC's type predicates (domain ``depot``).
    """
    checks: list[tuple[str, object]] = [
        ("num_depots", num_depots),
        ("num_distributors", num_distributors),
        ("num_trucks", num_trucks),
        ("num_pallets", num_pallets),
        ("num_hoists", num_hoists),
        ("num_crates", num_crates),
    ]
    for name, value in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")

    rng = random.Random(seed)
    places = [f"depot{i}" for i in range(num_depots)] + [f"distributor{i}" for i in range(num_distributors)]
    num_places = len(places)
    num_pallets = max(num_pallets, num_places)
    num_hoists = max(num_hoists, num_places)

    truck_places = [rng.randrange(num_places) for _ in range(num_trucks)]
    hoist_places = [i if i < num_places else rng.randrange(num_places) for i in range(num_hoists)]
    pallet_places = [i if i < num_places else rng.randrange(num_places) for i in range(num_pallets)]

    # A surface is ("pallet", i) or ("crate", i); towers track the current top.
    top: list[tuple[str, int]] = [("pallet", i) for i in range(num_pallets)]
    crate_pallets: list[int] = []
    crate_surfaces: list[tuple[str, int]] = []
    for crate in range(num_crates):
        pallet = rng.randrange(num_pallets)
        crate_pallets.append(pallet)
        crate_surfaces.append(top[pallet])
        top[pallet] = ("crate", crate)

    goal_top: list[tuple[str, int]] = [("pallet", i) for i in range(num_pallets)]
    goal_surfaces: dict[int, tuple[str, int]] = {}
    for _ in range(2 * num_crates):
        crate = rng.randrange(num_crates)
        if crate in goal_surfaces:
            continue
        pallet = rng.randrange(num_pallets)
        goal_surfaces[crate] = goal_top[pallet]
        goal_top[pallet] = ("crate", crate)

    def kind(*predicates: str) -> list[str]:
        return [] if typed else [f"\t({predicate})" for predicate in predicates]

    init_facts: list[str] = []
    for pallet, place in enumerate(pallet_places):
        init_facts += kind(f"pallet pallet{pallet}", f"surface pallet{pallet}")
        init_facts.append(f"\t(at pallet{pallet} {places[place]})")
        init_facts.append(f"\t(clear {top[pallet][0]}{top[pallet][1]})")
    for truck, place in enumerate(truck_places):
        init_facts += kind(f"truck truck{truck}")
        init_facts.append(f"\t(at truck{truck} {places[place]})")
    for hoist, place in enumerate(hoist_places):
        init_facts += kind(f"hoist hoist{hoist}")
        init_facts.append(f"\t(at hoist{hoist} {places[place]})")
        init_facts.append(f"\t(available hoist{hoist})")
    for crate, (pallet, surface) in enumerate(zip(crate_pallets, crate_surfaces)):
        init_facts += kind(f"crate crate{crate}", f"surface crate{crate}")
        init_facts.append(f"\t(at crate{crate} {places[pallet_places[pallet]]})")
        init_facts.append(f"\t(on crate{crate} {surface[0]}{surface[1]})")
    init_facts += kind(*(f"place {place}" for place in places))
    goals = [f"\t\t(on crate{crate} {kind}{index})" for crate, (kind, index) in sorted(goal_surfaces.items())]

    def names(prefix: str, count: int) -> str:
        return " ".join(f"{prefix}{i}" for i in range(count))

    groups = [("depot", num_depots), ("distributor", num_distributors), ("truck", num_trucks),
              ("pallet", num_pallets), ("crate", num_crates), ("hoist", num_hoists)]
    if typed:
        objects = "\n".join(f"\t{names(prefix, count)} - {prefix}" for prefix, count in groups) + ")"
    else:
        objects = "\t" + " ".join(names(prefix, count) for prefix, count in groups) + " )"

    name = f"depot-{num_depots}-{num_distributors}-{num_trucks}-{num_pallets}-{num_hoists}-{num_crates}"
    return (f"""(define (problem {name}) (:domain {"depots" if typed else "depot"})
(:objects
{objects}
(:init
{chr(10).join(init_facts)}
)

(:goal (and
{chr(10).join(goals)}
\t)
))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a STRIPS Depots PDDL problem.")
    parser.add_argument("-e", "--num-depots", type=int, required=True)
    parser.add_argument("-i", "--num-distributors", type=int, required=True)
    parser.add_argument("-t", "--num-trucks", type=int, required=True)
    parser.add_argument("-p", "--num-pallets", type=int, required=True)
    parser.add_argument("-u", "--num-hoists", type=int, required=True, help="number of hoists (upstream -h)")
    parser.add_argument("-c", "--num-crates", type=int, required=True)
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
