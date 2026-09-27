#!/usr/bin/env python3
# Port of pddl-generators storage/main.cpp (Storage-Propositional, square depots),
# as called by Autoscale:
# `storage -p 01 -o {containers} -e {seed} -c {crates} -n {hoists} -s {store_areas} -d {depots}`.
# ponytail: the ASCII depot map comment upstream prints is omitted; depots are named
# depot0.. instead of upstream's char-code names (depot48..).

from __future__ import annotations

import argparse
import math
import random
import sys

SA_PER_CONTAINER = 4
SA_DEPOT_DEVIATION = 0.1


def _square_depot(num_areas: int, rng: random.Random) -> tuple[list[tuple[int, int]], tuple[int, int]]:
    """Cells (row-major) of a dimX x dimY depot with its door on the last row."""
    dim_x = math.isqrt(num_areas)
    dim_y = -(-num_areas // dim_x)
    door = (dim_x, rng.randrange(dim_y) + 1)
    cells = {door}
    for i in range(1, dim_x + 1):
        for j in range(1, dim_y + 1):
            if len(cells) < num_areas:
                cells.add((i, j))
    return sorted(cells), door


def make_problem(
    num_crates: int,
    num_hoists: int,
    num_store_areas: int,
    num_depots: int = 1,
    num_containers: int | None = None,
    seed: int | None = None,
) -> str:
    """Generate a Storage-Propositional task.

    Store areas are split roughly evenly over square depots (door on the last
    row, connected to the load area); adjacent depots are joined by a transit
    area with probability 1/2. Hoists start on distinct random store areas of
    random depots; crates start in containers (four per container, the last one
    takes the rest) and must end up in depots, spread with at least one crate
    per depot while crates remain. ``num_containers`` defaults to
    ``ceil(num_crates / 4)`` as in Autoscale.
    """
    if num_containers is None:
        num_containers = -(-num_crates // SA_PER_CONTAINER) if isinstance(num_crates, int) else 0
    for name, value in (
        ("num_crates", num_crates),
        ("num_hoists", num_hoists),
        ("num_store_areas", num_store_areas),
        ("num_depots", num_depots),
        ("num_containers", num_containers),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")
    for name, value in (("num_crates", num_crates), ("num_depots", num_depots), ("num_hoists", num_hoists)):
        if value > num_store_areas:
            raise ValueError(f"{name} must not exceed num_store_areas")

    rng = random.Random(seed)
    right_connected = [rng.randrange(2) == 1 for _ in range(num_depots - 1)] + [False]

    # Store areas per depot: a base share minus 10%, plus random extras.
    mean = num_store_areas // num_depots
    per_depot = max(mean - int(mean * SA_DEPOT_DEVIATION), 1)
    remaining = num_store_areas - per_depot * num_depots
    random_bound = max(2, int(mean * SA_DEPOT_DEVIATION * 2 + 1))
    areas_per_depot = []
    for _ in range(num_depots - 1):
        extra = rng.randrange(min(remaining + 1, random_bound)) if remaining else 0
        areas_per_depot.append(per_depot + extra)
        remaining -= extra
    areas_per_depot.append(per_depot + remaining)

    hoists_per_depot = [0] * num_depots
    for _ in range(num_hoists):
        depot = rng.choice([d for d in range(num_depots) if hoists_per_depot[d] < areas_per_depot[d]])
        hoists_per_depot[depot] += 1

    # Full containers of four when crates overflow the others, else one crate each.
    fill = SA_PER_CONTAINER if num_crates / max(num_containers - 1, 1) > SA_PER_CONTAINER else 1
    crates_per_container = []
    left = num_crates
    for _ in range(num_containers - 1):
        take = min(fill, left)
        crates_per_container.append(take)
        left -= take
    crates_per_container.append(left)

    crates = [f"crate{i}" for i in range(num_crates)]
    container_areas = []
    crate_facts = []
    crate_index = 0
    for container, count in enumerate(crates_per_container):
        for k in range(count):
            container_areas.append((f"container-{container}-{k}", f"container{container}", crates[crate_index]))
            crate_index += 1

    depots = [f"depot{i}" for i in range(num_depots)]
    depot_areas = []
    connections = []
    ins = []
    doors = []
    clears = []
    hoist_facts = []
    extremes = []
    hoist_count = 0
    for d, depot in enumerate(depots):
        cells, door = _square_depot(areas_per_depot[d], rng)
        cell_set = set(cells)
        names = [f"{depot}-{i}-{j}" for i, j in cells]
        for (i, j), name in zip(cells, names):
            ins.append(f"(in {name} {depot})")
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)):
                if (ni, nj) in cell_set:
                    connections.append(f"(connected {name} {depot}-{ni}-{nj})")
        depot_areas.extend(names)
        doors.append(f"(connected {depot}-{door[0]}-{door[1]} loadarea)\n\t(connected loadarea {depot}-{door[0]}-{door[1]})")
        # Leftmost / rightmost cell, first in row-major order, anchor transit areas.
        left_cell = min(cells, key=lambda cell: cell[1])
        right_cell = min(cells, key=lambda cell: -cell[1])
        extremes.append((f"{depot}-{left_cell[0]}-{left_cell[1]}", f"{depot}-{right_cell[0]}-{right_cell[1]}"))
        free = list(range(len(names)))
        for _ in range(hoists_per_depot[d]):
            pos = rng.randrange(len(free))
            hoist_facts.append(f"(at hoist{hoist_count} {names[free[pos]]})\n\t(available hoist{hoist_count})")
            hoist_count += 1
            free[pos] = free[-1]
            free.pop()
        clears.extend(f"(clear {names[index]})" for index in free)

    transits = []
    transit_facts = []
    for d in range(num_depots - 1):
        if right_connected[d]:
            transit = f"transit{len(transits)}"
            transits.append(transit)
            transit_facts.append(f"(connected {transit} {extremes[d][1]})\n\t(connected {transit} {extremes[d + 1][0]})")

    # Goal: crates in depot order, at least one per depot while crates remain,
    # capped by half the depot's store areas when crates <= store areas / 2.
    halve = num_crates <= num_store_areas // 2
    available = [(size + 1) // 2 if halve and size > 1 else size for size in areas_per_depot]
    goal_counts = [0] * num_depots
    left = num_crates
    for d in range(num_depots):
        if left > 0:
            bound = available[d] - (num_depots - d - 1)
            extra = rng.randrange(available[d] if bound <= 0 else bound)
            goal_counts[d] = min(1 + extra, left)
            left -= goal_counts[d]
            available[d] -= goal_counts[d]
    for d in range(num_depots):
        if left > 0:
            take = min(available[d], left)
            goal_counts[d] += take
            left -= take
    goal_depots = [depot for depot, count in zip(depots, goal_counts) for _ in range(count)]

    init_facts = [
        *connections,
        *transit_facts,
        *ins,
        *(f"(on {crate} {area})" for area, _, crate in container_areas),
        *(f"(in {crate} {container})" for _, container, crate in container_areas),
        *(f"(in {area} {container})" for area, container, _ in container_areas),
        *(f"(connected loadarea {area})\n\t(connected {area} loadarea)" for area, _, _ in container_areas),
        *doors,
        *clears,
        *hoist_facts,
    ]
    goals = [f"(in {crate} {depot})" for crate, depot in zip(crates, goal_depots)]
    storeareas = " ".join(depot_areas + [area for area, _, _ in container_areas])

    return (f"""(define (problem storage-c{num_crates}-h{num_hoists}-s{num_store_areas}-d{num_depots}-o{num_containers})
(:domain Storage-Propositional)
(:objects
\t{storeareas} - storearea
\t{" ".join(f"hoist{i}" for i in range(num_hoists))} - hoist
\t{" ".join(crates)} - crate
\t{" ".join(f"container{i}" for i in range(num_containers))} - container
\t{" ".join(depots)} - depot
\t{" ".join(["loadarea", *transits])} - transitarea)

(:init
{chr(10).join(f"{chr(9)}{fact}" for fact in init_facts)})

(:goal (and
{chr(10).join(f"{chr(9)}{goal}" for goal in goals)}))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Storage-Propositional PDDL problem.")
    parser.add_argument("-c", "--num-crates", type=int, required=True)
    parser.add_argument("-n", "--num-hoists", type=int, required=True)
    parser.add_argument("-s", "--num-store-areas", type=int, required=True)
    parser.add_argument("-d", "--num-depots", type=int, default=1)
    parser.add_argument("-o", "--num-containers", type=int, help="default: ceil(crates / 4)")
    parser.add_argument("-e", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
