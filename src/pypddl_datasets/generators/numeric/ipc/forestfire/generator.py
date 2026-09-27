#!/usr/bin/env python3
# Forest Fire (IPC 2026 numeric, domain by Alexander Shleyfman). No generator was
# published; this reconstructs the layout of the 20 IPC tasks.

from __future__ import annotations

import argparse
import heapq
import random
import sys


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _cell(x: int, y: int, mid: int) -> str:
    return f"bushes{x}_{y}" if y == 2 and x != mid else f"grass{x}_{y}"


def make_problem(
    width: int,
    height: int,
    num_bots: int = 1,
    num_axes: int = 2,
    water_capacity: int = 6,
    axe_durability: int = 3,
    gate_tree: int = 6,
    fire_rows: int = 1,
    fire_probability: float = 0.6,
    max_fire: int = 3,
    extra_trees: int = 0,
    max_tree: int = 3,
    seed: int | None = None,
) -> str:
    """Generate a Forest Fire task on a ``width`` x ``height`` grid (width odd).

    Row 1 holds the bots and axes (``grass1_1``, ``grass2_1``, ...) and two ponds
    at its ends; row 2 is bushes (``max-water`` 1) except the middle column,
    a grass gate with ``gate_tree`` trees. Fires burn on the top ``fire_rows``
    rows: each cell catches fire with ``fire_probability`` (at least one does),
    with 1..``max_fire`` units; every fire must be put out. ``extra_trees``
    grass cells between gate and fire rows get 1..``max_tree`` trees; a draw is
    kept only if the fire rows are reachable by chopping at most the total axe
    durability. All grid neighbours are connected.
    """
    for name, value, minimum in (
        ("width", width, 3), ("height", height, 3), ("num_bots", num_bots, 1), ("num_axes", num_axes, 1),
        ("water_capacity", water_capacity, 1), ("axe_durability", axe_durability, 1), ("gate_tree", gate_tree, 0),
        ("fire_rows", fire_rows, 1), ("max_fire", max_fire, 1), ("extra_trees", extra_trees, 0),
        ("max_tree", max_tree, 1),
    ):
        if not _is_int(value) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if width % 2 == 0:
        raise ValueError("width must be odd (the gate is the middle column)")
    if num_bots > width or num_axes > width:
        raise ValueError("num_bots and num_axes must not exceed width (they start on row 1)")
    if fire_rows > height - 2:
        raise ValueError(f"fire_rows must be at most height - 2 = {height - 2}")
    tree_cells = [(x, y) for y in range(3, height - fire_rows + 1) for x in range(1, width + 1)]
    if extra_trees > len(tree_cells):
        raise ValueError(f"extra_trees must be at most {len(tree_cells)}")
    if not 0.0 <= fire_probability <= 1.0:
        raise ValueError("fire_probability must be in [0, 1]")

    rng = random.Random(seed)
    mid = (width + 1) // 2
    cells = [(x, y) for y in range(1, height + 1) for x in range(1, width + 1)]
    fire_cells = [(x, y) for y in range(height - fire_rows + 1, height + 1) for x in range(1, width + 1)]
    for _ in range(1000):
        trees = {(mid, 2): gate_tree}
        trees.update({c: rng.randint(1, max_tree) for c in rng.sample(tree_cells, extra_trees)})
        fires = {c: rng.randint(1, max_fire) for c in fire_cells if rng.random() < fire_probability}
        if not fires:
            c = rng.choice(fire_cells)
            fires[c] = rng.randint(1, max_fire)
        if _chop_cost(trees, width, height, height - fire_rows + 1) <= num_axes * axe_durability:
            break
    else:
        raise ValueError("no draw with reachable fires; lower extra_trees or max_tree")

    def cell_name(c: tuple[int, int]) -> str:
        return _cell(c[0], c[1], mid)

    grass = [cell_name(c) for c in cells if cell_name(c).startswith("grass")]
    bushes = [cell_name(c) for c in cells if cell_name(c).startswith("bushes")]
    init: list[str] = []
    for x, y in cells:
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 1 <= nx <= width and 1 <= ny <= height:
                init.append(f"(connected {cell_name((x, y))} {cell_name((nx, ny))})")
    init += [f"(= (tree {cell_name(c)}) {trees.get(c, 0)})" for c in cells]
    init += [f"(= (fire {cell_name(c)}) {fires.get(c, 0)})" for c in cells]
    init += [f"(= (max-water {b}) 1)" for b in bushes]
    for i in range(1, num_bots + 1):
        init += [
            f"(at bot{i} grass{i}_1)", f"(= (water-capacity bot{i}) {water_capacity})", f"(= (has-water bot{i}) 0)"
        ]
    init += ["(pond grass1_1)", f"(pond grass{width}_1)"]
    for i in range(1, num_axes + 1):
        init += [f"(at axe{i} grass{i}_1)", f"(= (durability axe{i}) {axe_durability})"]
    init.append("(= (cost) 0)")
    goal = [f"(= (fire {cell_name(c)}) 0)" for c in sorted(fires, key=lambda c: (c[1], c[0]))]

    return (f"""(define (problem forestfire-w{width}-h{height}-b{num_bots}-a{num_axes})
(:domain forestfire)
(:objects {' '.join(f"bot{i}" for i in range(1, num_bots + 1))} - bot
          {' '.join(f"axe{i}" for i in range(1, num_axes + 1))} - axe
          {' '.join(grass)} - grass
          {' '.join(bushes)} - bushes
)
(:init
{chr(10).join("       " + fact for fact in init)}
)
(:goal (and {' '.join(goal)}))
(:metric minimize (cost))
)
""").lower()


def _chop_cost(trees: dict[tuple[int, int], int], width: int, height: int, fire_row: int) -> int:
    """Cheapest total chopping from row 1 to ``fire_row``; entering a tree cell costs its trees."""
    dist = {(x, 1): trees.get((x, 1), 0) for x in range(1, width + 1)}
    queue = [(d, c) for c, d in dist.items()]
    heapq.heapify(queue)
    while queue:
        d, (x, y) = heapq.heappop(queue)
        if y == fire_row:
            return d
        if d > dist[(x, y)]:
            continue
        for c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 1 <= c[0] <= width and 1 <= c[1] <= height and d + trees.get(c, 0) < dist.get(c, 1 << 30):
                dist[c] = d + trees.get(c, 0)
                heapq.heappush(queue, (dist[c], c))
    return 1 << 30


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Forest Fire PDDL problem.")
    parser.add_argument("-x", "--width", type=int, required=True, help="grid width (odd)")
    parser.add_argument("-y", "--height", type=int, required=True)
    parser.add_argument("-b", "--num-bots", type=int, default=1)
    parser.add_argument("-a", "--num-axes", type=int, default=2)
    parser.add_argument("--water-capacity", type=int, default=6)
    parser.add_argument("--axe-durability", type=int, default=3)
    parser.add_argument("--gate-tree", type=int, default=6)
    parser.add_argument("--fire-rows", type=int, default=1)
    parser.add_argument("--fire-probability", type=float, default=0.6)
    parser.add_argument("--max-fire", type=int, default=3)
    parser.add_argument("--extra-trees", type=int, default=0)
    parser.add_argument("--max-tree", type=int, default=3)
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
