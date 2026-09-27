#!/usr/bin/env python3
# Reconstructed from the IPC 2023 numeric ext-plant-watering tasks (Espasa Arxer; no generator
# was published). Problem names follow the IPC tasks: instance_<size>_<plants>_<agents>_<seed>.

from __future__ import annotations

import argparse
import random
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def make_problem(
    size: int,
    num_plants: int,
    num_agents: int = 2,
    num_taps: int = 1,
    max_carry: int = 5,
    max_poured: int = 10,
    seed: int | None = None,
) -> str:
    """Generate an Extended Plant Watering task on a ``size x size`` grid (1..size).

    Plants, taps and agents occupy distinct uniformly random cells. Each plant
    must receive exactly a uniform amount in 1..``max_poured``; the water reserve
    is the total demand plus 10% (rounded down), and every agent carries at most
    ``max_carry`` units. The goal also requires ``total_poured = total_loaded``.
    """
    for name, value, minimum in (
        ("size", size, 1),
        ("num_plants", num_plants, 1),
        ("num_agents", num_agents, 1),
        ("num_taps", num_taps, 1),
        ("max_carry", max_carry, 1),
        ("max_poured", max_poured, 1),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    things = (
        [f"plant{i}" for i in range(1, num_plants + 1)]
        + [f"tap{i}" for i in range(1, num_taps + 1)]
        + [f"agent{i}" for i in range(1, num_agents + 1)]
    )
    if len(things) > size * size:
        raise ValueError(f"size is too small for {len(things)} distinct cells")

    rng = random.Random(seed)
    cells = rng.sample([(x, y) for x in range(1, size + 1) for y in range(1, size + 1)], len(things))
    plants = things[:num_plants]
    demand = {plant: rng.randint(1, max_poured) for plant in plants}
    total = sum(demand.values())
    agents = things[num_plants + num_taps:]

    init = [f"(= (maxx) {size})", "(= (minx) 1)", f"(= (maxy) {size})", "(= (miny) 1)",
            "(= (total_poured) 0)", "(= (total_loaded) 0)", f"(= (water_reserve) {total + total // 10})"]
    for agent in agents:
        init += [f"(= (carrying {agent}) 0)", f"(= (max_carry {agent}) {max_carry})"]
    init += [f"(= (poured {plant}) 0)" for plant in plants]
    for thing, (x, y) in zip(things, cells):
        init += [f"(= (x {thing}) {x})", f"(= (y {thing}) {y})"]
    goals = [f"(= (poured {plant}) {demand[plant]})" for plant in plants] + ["(= (total_poured) (total_loaded))"]
    types = [(t, "plant" if t.startswith("plant") else "tap" if t.startswith("tap") else "agent") for t in things]

    return (f"""(define (problem instance_{size}_{num_plants}_{num_agents}_{seed})
(:domain ext-plant-watering)
(:objects
{chr(10).join(f"{chr(9)}{t} - {ty}" for t, ty in types)}
)
(:init
{chr(10).join(chr(9) + fact for fact in init)}
)
(:goal
(and
{chr(10).join(chr(9) + goal for goal in goals)}
)))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an Extended Plant Watering PDDL problem.")
    parser.add_argument("size", type=int, help="grid side length")
    parser.add_argument("num_plants", type=int)
    parser.add_argument("-a", "--num-agents", type=int, default=2)
    parser.add_argument("-t", "--num-taps", type=int, default=1)
    parser.add_argument("--max-carry", type=int, default=5)
    parser.add_argument("--max-poured", type=int, default=10)
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
