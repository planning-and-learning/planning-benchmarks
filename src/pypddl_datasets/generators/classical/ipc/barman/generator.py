#!/usr/bin/env python3

# Port of pddl-generators/barman/barman-generator.py (the IPC 2011/2014 generator,
# also called by Autoscale 21.11): every cocktail is served exactly once, then
# each remaining shot but the last gets a random cocktail or ingredient with
# equal probability. Default encoding is IPC 2014 (no action costs);
# action_costs=True gives the IPC 2011 / Autoscale encoding.

from __future__ import annotations

import argparse
import random
import sys

MAX_LEVELS = 2


def make_problem(
    num_cocktails: int,
    num_ingredients: int,
    num_shots: int,
    seed: int | None = None,
    action_costs: bool = False,
) -> str:
    checks: list[tuple[str, object, int]] = [
        ("num_cocktails", num_cocktails, 1),
        ("num_ingredients", num_ingredients, 2),
        ("num_shots", num_shots, num_cocktails + 1),
    ]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")

    rng = random.Random(seed)
    cocktails = [f"cocktail{i}" for i in range(1, num_cocktails + 1)]
    ingredients = [f"ingredient{i}" for i in range(1, num_ingredients + 1)]
    shots = [f"shot{i}" for i in range(1, num_shots + 1)]
    dispensers = [f"dispenser{i}" for i in range(1, num_ingredients + 1)]
    levels = [f"l{i}" for i in range(MAX_LEVELS + 1)]

    init_facts = ["(= (total-cost) 0)"] if action_costs else []
    init_facts += [
        "(ontable shaker1)",
        "(clean shaker1)",
        "(empty shaker1)",
        "(handempty left)",
        "(handempty right)",
        "(shaker-empty-level shaker1 l0)",
        "(shaker-level shaker1 l0)",
    ]
    for shot in shots:
        init_facts.extend((f"(ontable {shot})", f"(clean {shot})", f"(empty {shot})"))
    init_facts.extend(f"(dispenses {d} {i})" for d, i in zip(dispensers, ingredients))
    init_facts.extend(f"(next {levels[i]} {levels[i + 1]})" for i in range(MAX_LEVELS))
    for cocktail in cocktails:
        part1, part2 = rng.sample(ingredients, 2)
        init_facts.extend((f"(cocktail-part1 {cocktail} {part1})", f"(cocktail-part2 {cocktail} {part2})"))

    served = rng.sample(cocktails, num_cocktails)
    for _ in range(num_cocktails, num_shots - 1):
        served.append(rng.choice(cocktails) if rng.randint(0, 1) else rng.choice(ingredients))
    goals = [f"(contains {shot} {beverage})" for shot, beverage in zip(shots, served)]

    metric = "\n  (:metric minimize (total-cost))" if action_costs else ""
    return (f"""(define (problem barman-c{num_cocktails}-i{num_ingredients}-s{num_shots})
  (:domain barman)
  (:objects
    shaker1 - shaker
    left right - hand
    {' '.join(shots)} - shot
    {' '.join(ingredients)} - ingredient
    {' '.join(cocktails)} - cocktail
    {' '.join(dispensers)} - dispenser
    {' '.join(levels)} - level
  )
  (:init
{chr(10).join(f"    {fact}" for fact in init_facts)}
  )
  (:goal
    (and
{chr(10).join(f"      {goal}" for goal in goals)}
    )
  ){metric}
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Barman PDDL problem.")
    parser.add_argument("--num-cocktails", type=int, required=True)
    parser.add_argument("--num-ingredients", type=int, required=True)
    parser.add_argument("--num-shots", type=int, required=True, help="at least num_cocktails + 1")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--action-costs", action="store_true", help="IPC 2011 / Autoscale encoding with total-cost")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
