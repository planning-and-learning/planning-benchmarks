#!/usr/bin/env python3

from __future__ import annotations

import argparse
import random
import sys
import time

MAX_LEVELS = 2


def _typed_objects(names: list[str], type_name: str) -> str:
    return f"      {' '.join(names)} - {type_name}" if names else ""


def make_problem(num_cocktails: int, num_ingredients: int, num_shots: int, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    cocktails = [f"cocktail{i}" for i in range(1, num_cocktails + 1)]
    ingredients = [f"ingredient{i}" for i in range(1, num_ingredients + 1)]
    shots = [f"shot{i}" for i in range(1, num_shots + 1)]
    dispensers = [f"dispenser{i}" for i in range(1, num_ingredients + 1)]
    levels = [f"l{i}" for i in range(MAX_LEVELS + 1)]

    object_lines = [
        _typed_objects(["left", "right"], "hand"),
        _typed_objects(["shaker1"], "shaker"),
        _typed_objects(shots, "shot"),
        _typed_objects(ingredients, "ingredient"),
        _typed_objects(cocktails, "cocktail"),
        _typed_objects(dispensers, "dispenser"),
        _typed_objects(levels, "level"),
    ]

    init_facts = [
        "    (= (total-cost) 0)",
        "    (handempty left)",
        "    (handempty right)",
        "    (ontable shaker1)",
        "    (clean shaker1)",
        "    (empty shaker1)",
        "    (shaker-empty-level shaker1 l0)",
        "    (shaker-level shaker1 l0)",
    ]
    init_facts.extend(f"    (ontable {shot})" for shot in shots)
    init_facts.extend(f"    (clean {shot})" for shot in shots)
    init_facts.extend(f"    (empty {shot})" for shot in shots)
    init_facts.extend(f"    (dispenses {dispenser} {ingredient})" for dispenser, ingredient in zip(dispensers, ingredients))
    init_facts.extend(f"    (next {levels[index]} {levels[index + 1]})" for index in range(len(levels) - 1))

    cocktail_parts = []
    for cocktail in cocktails:
        part1, part2 = rng.sample(ingredients, 2)
        cocktail_parts.append((cocktail, part1, part2))
        init_facts.append(f"    (cocktail-part1 {cocktail} {part1})")
        init_facts.append(f"    (cocktail-part2 {cocktail} {part2})")

    objects = "\n".join(line for line in object_lines if line)
    init = "\n".join(init_facts)
    goal_facts = "\n".join(f"      (contains {shot} {cocktail})" for shot, (cocktail, _, _) in zip(shots, cocktail_parts))

    return f"""(define (problem barman-c{num_cocktails}-i{num_ingredients}-s{num_shots})
  (:domain barman)
  (:objects
{objects}
  )
  (:init
{init}
  )
  (:goal
    (and
{goal_facts}
    )
  )
  (:metric minimize (total-cost))
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Barman PDDL problem.")
    parser.add_argument("-c", "--num-cocktails", type=int, required=True)
    parser.add_argument("-i", "--num-ingredients", type=int, required=True)
    parser.add_argument("-s", "--num-shots", type=int, required=True)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args(argv)

    if args.num_cocktails < 1:
        parser.error("num_cocktails must be at least 1")
    if args.num_ingredients < 2:
        parser.error("num_ingredients must be at least 2")
    if args.num_shots < args.num_cocktails:
        parser.error("num_shots must be at least num_cocktails")

    print(make_problem(args.num_cocktails, args.num_ingredients, args.num_shots, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
