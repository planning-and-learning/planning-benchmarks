#!/usr/bin/env python3

from __future__ import annotations

import argparse
from math import ceil
import random
import sys
import time


def _objects(names: list[str], type_name: str) -> str:
    return f"      {' '.join(names)} - {type_name}" if names else ""


def make_problem(num_children: int, num_trays: int, gluten_factor: float, const_ratio: float = 1.2, seed: int | None = None) -> str:
    rng = random.Random(seed if seed is not None else int(time.time()))

    num_sandwiches = int(ceil(num_children * const_ratio))
    num_allergic = min(num_children, int(num_children * gluten_factor))

    children = [f"child{i}" for i in range(1, num_children + 1)]
    trays = [f"tray{i}" for i in range(1, num_trays + 1)]
    sandwiches = [f"sandw{i}" for i in range(1, num_sandwiches + 1)]
    breads = [f"bread{i}" for i in range(1, num_children + 1)]
    contents = [f"content{i}" for i in range(1, num_children + 1)]
    tables = ["table1", "table2", "table3"]

    allergic_children = set(rng.sample(children, num_allergic))
    gluten_free_breads = set(rng.sample(breads, num_allergic))
    gluten_free_contents = set(rng.sample(contents, num_allergic))

    object_lines = [
        _objects(children, "child"),
        _objects(breads, "bread-portion"),
        _objects(contents, "content-portion"),
        _objects(sandwiches, "sandwich"),
        _objects(trays, "tray"),
        _objects(tables, "place"),
    ]

    init_facts = []
    init_facts.extend(f"    (at {tray} kitchen)" for tray in trays)
    init_facts.extend(f"    (at_kitchen_bread {bread})" for bread in breads)
    init_facts.extend(f"    (at_kitchen_content {content})" for content in contents)
    init_facts.extend(f"    (no_gluten_bread {bread})" for bread in sorted(gluten_free_breads))
    init_facts.extend(f"    (no_gluten_content {content})" for content in sorted(gluten_free_contents))
    init_facts.extend(f"    ({'allergic_gluten' if child in allergic_children else 'not_allergic_gluten'} {child})" for child in children)
    init_facts.extend(f"    (waiting {child} {rng.choice(tables)})" for child in children)
    init_facts.extend(f"    (notexist {sandwich})" for sandwich in sandwiches)

    objects = "\n".join(line for line in object_lines if line)
    init = "\n".join(init_facts)
    goal_facts = "\n".join(f"      (served {child})" for child in children)

    return f"""(define (problem childsnack-c{num_children}-t{num_trays})
  (:domain child-snack)
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
)
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Childsnack PDDL problem.")
    parser.add_argument("-c", "--num-children", type=int, required=True)
    parser.add_argument("-t", "--num-trays", type=int, required=True)
    parser.add_argument("-g", "--gluten-factor", type=float, required=True)
    parser.add_argument("-r", "--const-ratio", type=float, default=1.2)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)

    if args.num_children < 1:
        parser.error("num_children must be at least 1")
    if args.num_trays < 1:
        parser.error("num_trays must be at least 1")
    if not 0 <= args.gluten_factor <= 1:
        parser.error("gluten_factor must be between 0 and 1")
    if args.const_ratio < 1:
        parser.error("const_ratio must be at least 1")

    print(make_problem(args.num_children, args.num_trays, args.gluten_factor, args.const_ratio, args.seed), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
