#!/usr/bin/env python3
# Reconstruction of the IPC 2023 numeric Sugar (supply-chain) tasks (no generator was
# published). The reference tasks are hand-written from one template with 2 or 3 mills;
# only the resources, the harvest budget and the in-storage goals vary.

from __future__ import annotations

import argparse
import random
import sys

BRANDS = ("brand1", "brand2", "brand3", "brand4")
DEPOTS = ("depot1", "depot2", "depot3")
# Per mill: produced brands, current brand, brands with a declared in-storage fluent,
# cost-process, max-produce (from the reference template; 2-mill tasks use mills 1-2).
MILLS = (
    ("mill1", ("brand1", "brand3", "brand4"), "brand1", ("brand1", "brand3", "brand4"), 1, 5),
    ("mill2", ("brand2", "brand3", "brand4"), "brand3", ("brand1", "brand2", "brand3"), 3, 8),
    ("mill3", ("brand2", "brand1"), "brand1", ("brand1", "brand2", "brand4"), 6, 10),
)
MILL2_OF_TWO = ("mill2", ("brand2", "brand3"), "brand3", ("brand1", "brand2", "brand3"), 3, 8)
RESOURCES = (0, 3, 4, 5, 7, 8, 10, 15, 20, 25, 30)
MILL_GOAL_PROBABILITY = 0.15
# Goal amounts as observed in the reference tasks (amount: count).
GOAL_AMOUNTS = {1: 12, 2: 17, 3: 8, 4: 3, 5: 15, 7: 1, 10: 2}
LEFTOVER_PROBABILITY = 0.85  # mill3 starts with 2 units of brand4, as in 16 of 18 three-mill tasks
LABOUR_COST_PROBABILITY = 0.6
MAX_ATTEMPTS = 1000


def make_problem(num_mills: int, num_goals: int, seed: int | None = None) -> str:
    """Generate a Sugar task with 2 or 3 mills and ``num_goals`` in-storage goals.

    Structure (brands, trucks, depots, cranes, complete road map, production sets)
    is the reference template. Each mill's raw cane is drawn from the reference
    values, the unharvested fields from 3..4. Goals ask for amounts drawn from the reference tasks' amounts (1..10) of a brand
    some mill can produce (produce set and declared in-storage fluent) at a depot, or
    with probability 0.15 at a mill that declares it; draws repeat until the total
    goal amount fits the available cane (stock plus 5 per harvest).
    """
    if num_mills not in (2, 3) or isinstance(num_mills, bool):
        raise ValueError("num_mills must be 2 or 3")
    max_goals = (len(DEPOTS) + 1) * len(BRANDS)
    if not isinstance(num_goals, int) or isinstance(num_goals, bool) or not 1 <= num_goals <= max_goals:
        raise ValueError(f"num_goals must be an integer in 1..{max_goals}")
    rng = random.Random(seed)
    mills = [MILLS[0], MILL2_OF_TWO] if num_mills == 2 else list(MILLS)
    names = [m[0] for m in mills]
    producible = sorted({b for _, produce, _, stored, _, _ in mills for b in produce if b in stored})
    for _ in range(MAX_ATTEMPTS):
        unharvested = rng.randint(3, 4)
        resources = {m: rng.choice(RESOURCES) for m in names}
        leftover = num_mills == 3 and rng.random() < LEFTOVER_PROBABILITY
        goals: dict[tuple[str, str], int] = {}
        while len(goals) < num_goals:
            brand = rng.choice(producible)
            if rng.random() < MILL_GOAL_PROBABILITY:
                places = [m for m, _, _, stored, _, _ in mills if brand in stored]
            else:
                places = list(DEPOTS)
            goals.setdefault((rng.choice(places), brand), rng.choices(list(GOAL_AMOUNTS), list(GOAL_AMOUNTS.values()))[0])
        if sum(goals.values()) <= sum(resources.values()) + 5 * unharvested:
            break
    else:
        raise ValueError(f"no draw with enough cane for {num_goals} goals in {MAX_ATTEMPTS} attempts")

    locations = names + list(DEPOTS)
    crane_mills = names + [None] * (3 - num_mills)
    capacities = (3, 5, 5) if num_mills == 2 else (5, 5, 5)
    extra = "(=(labour-cost)0)" if rng.random() < LABOUR_COST_PROBABILITY else ""
    lines = [
        f"\t\t(=(unharvest-field){unharvested}) (=(mill-cost)0) (=(inventory-cost)0) (=(handling-cost)0){extra}",
        "\t\t" + " ".join(f"(=(cost-process {m[0]}){m[4]})" for m in mills),
        "\t\t" + " ".join(f"(=(has-resource sugar-cane {m})"f"{resources[m]})" for m in names),
        "\t\t" + " ".join(f"(=(max-changing {m})2)" for m in names),
        "\t\t" + " ".join(f"(=(max-produce {m[0]}){m[5]})" for m in mills),
        "\t\t" + " ".join(f"(available {m})" for m in names),
        "",
    ]
    for mill, produce, current, _, _, _ in mills:
        lines.append("\t\t" + " ".join(f"(produce {mill} {b})" for b in produce) + f" (current-process {mill} {current})")
    for mill, _, _, stored, _, _ in mills:
        lines.append("\t\t" + " ".join(
            f"(=(in-storage {mill} {b}){2 if leftover and (mill, b) == ('mill3', 'brand4') else 0})" for b in stored
        ))
    lines.append("")
    lines += ["\t\t" + " ".join(f"(change-process {a} {b})" for b in BRANDS if b != a) for a in BRANDS]
    lines += [
        "",
        "\t\t(at-location truck1 depot1) (at-location truck2 depot2)",
        "\t\t(=(truck-cap truck1)10) (=(truck-cap truck2)6)",
        "\t\t" + " ".join(f"(at-location crane{i + 1} {m})" for i, m in enumerate(crane_mills) if m),
        "\t\t" + " ".join(f"(ready-crane crane{i + 1})" for i, m in enumerate(crane_mills) if m),
        "\t\t" + " ".join(f"(=(capacity crane{i + 1}){c})" for i, (m, c) in enumerate(zip(crane_mills, capacities)) if m),
        "\t\t(=(service-time crane1)10) (=(service-time crane2)15) (=(service-time crane3)10)",
        "\t\t(=(max-service-time crane1)10) (=(max-service-time crane2)15) (=(max-service-time crane3)10)",
    ]
    lines += [f"\t\t(=(in-truck-sugar {b} {t})0)" for t in ("truck1", "truck2") for b in BRANDS]
    lines += ["\t\t" + " ".join(f"(=(in-storage {d} {b})0)" for b in BRANDS) for d in DEPOTS]
    lines.append("")
    lines += [
        f"\t\t(connected {a} {b}) (connected {b} {a})"
        for i, a in enumerate(locations) for b in locations[i + 1:]
    ]
    goal_lines = "\n".join(f"\t\t (>=(in-storage {loc} {brand}){amount})" for (loc, brand), amount in goals.items())
    return (f"""(define (problem sugar-m{num_mills}-g{num_goals})
\t(:domain supply-chain)

\t(:objects
\t\t{' '.join(BRANDS)} - brand
\t\tsugar-cane - raw-cane
\t\ttruck1 truck2 - truck
\t\t{' '.join(DEPOTS)} - depot
\t\t{' '.join(names)} - mill
\t\tcrane1 crane2 crane3 - crane
\t)

\t(:init
{chr(10).join(lines)}
\t)
\t(:goal (and
{goal_lines}
\t\t)
\t)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric Sugar (supply-chain) PDDL problem.")
    parser.add_argument("-m", "--num-mills", type=int, required=True, choices=(2, 3))
    parser.add_argument("-g", "--num-goals", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_mills, args.num_goals, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
