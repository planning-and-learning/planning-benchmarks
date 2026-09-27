#!/usr/bin/env python3
# OnlyCraft (IPC 2026 numeric; domain after Benyamin, Mordoch, Shperberg, Piotrowski
# and Stern, "Crafting a Pogo Stick in Minecraft with Heuristic Search"). No
# generator was published; this reconstructs the 40 opt/sat IPC tasks.

from __future__ import annotations

import argparse
import math
import random
import sys


def make_problem(num_pogo_sticks: int, num_trees: int | None = None, grid_size: int | None = None,
                 seed: int | None = None) -> str:
    """Generate an OnlyCraft task: craft ``num_pogo_sticks`` pogo sticks.

    ``num_trees`` defaults to ceil(3.5 * sticks) and ``grid_size`` to
    floor(sqrt(trees)) + 1, as in the IPC tasks; the trees occupy random cells of
    the ``grid_size``^2 cells, the rest is air. Agent position and crafting table
    are uniformly random cells (the table may share a cell with a tree).
    """
    num_trees = math.ceil(3.5 * num_pogo_sticks) if num_trees is None else num_trees
    grid_size = math.isqrt(num_trees) + 1 if grid_size is None else grid_size
    for name, value, minimum in (("num_pogo_sticks", num_pogo_sticks, 1), ("num_trees", num_trees, 1),
                                 ("grid_size", grid_size, 1)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_trees > grid_size * grid_size:
        raise ValueError(f"num_trees must be at most grid_size^2 = {grid_size * grid_size}")

    rng = random.Random(seed)
    cells = [f"cell{i}" for i in range(grid_size * grid_size)]
    trees = set(rng.sample(cells, num_trees))
    init = [f"(position {rng.choice(cells)})", f"(crafting_table_cell {rng.choice(cells)})", "(= (toxicity) 0)"]
    init += [f"({'tree' if c in trees else 'air'}_cell {c})" for c in cells]
    init += [f"(= ({f}) 0)" for f in ("count_log_in_inventory", "count_planks_in_inventory", "count_stick_in_inventory",
                                      "count_tree_tap_in_inventory", "count_sack_polyisoprene_pellets_in_inventory",
                                      "count_pogo_stick")]
    return (f"""(define (problem onlycraft-p{num_pogo_sticks}-t{num_trees}-g{grid_size})
(:domain polycraft)
(:objects
    {' '.join(cells)} - cell
)
(:init
{chr(10).join("    " + f for f in init)}
)
(:goal
  (and
    (>= (count_pogo_stick) {num_pogo_sticks})
  )
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an OnlyCraft PDDL problem.")
    parser.add_argument("-p", "--num-pogo-sticks", type=int, required=True)
    parser.add_argument("-t", "--num-trees", type=int)
    parser.add_argument("-g", "--grid-size", type=int)
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
