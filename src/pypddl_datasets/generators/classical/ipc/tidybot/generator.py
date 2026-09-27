#!/usr/bin/env python3
# Port of pddl-generators tidybot/src/tidybot/core.clj (Bhaskara Marthi), the IPC 2011
# generator: `java -jar tidybot.jar world-size n-tables n-cupboards min-size max-size
# cupboard-size [seed]`. The IPC tasks all use table sides 1..2 and cupboard size 4.

from __future__ import annotations

import argparse
import random
import sys
from collections.abc import Callable, Iterator
from itertools import product
from typing import cast

GRIPPER_RADIUS = 1
ORIENTATIONS = ("u", "d", "l", "r")
PLACEMENT_TRIES = 100
WORLD_ATTEMPTS = 1000

Cell = tuple[int, int]
Box = tuple[Cell, Cell, str]  # (min corner, max corner, "table" or cupboard orientation)


def make_problem(
    world_size: int,
    num_tables: int,
    num_cupboards: int = 1,
    min_table_size: int = 1,
    max_table_size: int = 2,
    cupboard_size: int = 4,
    seed: int | None = None,
) -> str:
    """Generate a Tidybot task on a ``world_size`` x ``world_size`` grid.

    Cupboards (U-shaped, random opening side) are placed first, then tables with
    random side lengths in ``min_table_size..max_table_size``; each placement is
    retried up to 100 times against a one-cell clearance and silently dropped
    if it never fits, as upstream; the whole world is redrawn until every
    cupboard fits (as in all IPC tasks), tables may still be dropped. There is one object per inner cupboard cell,
    whose goal is that cell; its start is a distinct random surface cell, and
    with probability 1/2 it gets a second acceptable goal on a random table cell.
    """
    for name, value, minimum in (
        ("world_size", world_size, 1),
        ("num_tables", num_tables, 0),
        ("num_cupboards", num_cupboards, 1),
        ("min_table_size", min_table_size, 1),
        ("max_table_size", max_table_size, min_table_size),
        ("cupboard_size", cupboard_size, 3),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if cupboard_size + 1 > world_size:
        raise ValueError("cupboard_size must be smaller than world_size")

    rng = random.Random(seed)

    def rand_int(n: int) -> int:
        # Clojure's (rand-int n) truncates toward zero, so non-positive n gives 0.
        return int(rng.random() * n)

    def clamp(x: int) -> int:
        return max(0, min(world_size - 1, x))

    def sample_box(low: int, high: int, kind: str) -> Box:
        x_size, y_size = low + rand_int(high + 1 - low), low + rand_int(high + 1 - low)
        min_x, min_y = 1 + rand_int(world_size - x_size - 2), 1 + rand_int(world_size - y_size - 2)
        return (min_x, min_y), (clamp(min_x + x_size - 1), clamp(min_y + y_size - 1)), kind

    def too_close(box: Box, cell: Cell) -> bool:
        (x_min, y_min), (x_max, y_max), _ = box
        return x_min - 1 <= cell[0] <= x_max + 1 and y_min - 1 <= cell[1] <= y_max + 1

    def collide(a: Box, b: Box) -> bool:
        # ponytail: upstream only tests corners, so long thin boxes may still cross.
        def corners(box: Box) -> Iterator[Cell]:
            return product((box[0][0], box[1][0]), (box[0][1], box[1][1]))

        return any(too_close(b, c) for c in corners(a)) or any(too_close(a, c) for c in corners(b))

    def place(surfaces: list[Box], count: int, cupboards: bool) -> list[Box]:
        for _ in range(count):
            rng.random()  # upstream draws (rand) < cupboard-prob for every surface
            kind = rng.choice(ORIENTATIONS) if cupboards else "table"
            low, high = (cupboard_size, cupboard_size) if cupboards else (min_table_size, max_table_size)
            for _ in range(PLACEMENT_TRIES + 1):
                box = sample_box(low, high, kind)
                if not any(collide(box, other) for other in surfaces):
                    surfaces = [box, *surfaces]
                    break
        return surfaces

    def cells(box: Box) -> list[Cell]:
        (x_min, y_min), (x_max, y_max), _ = box
        return list(product(range(x_min, x_max + 1), range(y_min, y_max + 1)))

    def object_locations(box: Box) -> list[Cell]:
        (x_min, y_min), (x_max, y_max), kind = box
        inside = [(x, y) for x, y in cells(box) if x_min < x < x_max and y_min < y < y_max]
        return [c for c in cells(box) if c not in inside] if kind == "table" else inside

    def walls(box: Box) -> list[Cell]:
        (x_min, y_min), (x_max, y_max), kind = box
        openings: dict[str, Callable[[int, int], bool]] = {
            "u": lambda x, y: y == y_min and x_min < x < x_max,
            "d": lambda x, y: y == y_max and x_min < x < x_max,
            "l": lambda x, y: x == x_min and y_min < y < y_max,
            "r": lambda x, y: x == x_max and y_min < y < y_max,
        }
        opening = openings[kind]
        return [
            (x, y) for x, y in cells(box)
            if (x in (x_min, x_max) or y in (y_min, y_max)) and not opening(x, y)
        ]

    # Upstream silently drops surfaces that never fit; every IPC task has all its
    # cupboards (objects = cupboards * (cupboard_size - 2)^2), so redraw until they fit.
    for _ in range(WORLD_ATTEMPTS):
        surfaces = place(place([], num_cupboards, cupboards=True), num_tables, cupboards=False)
        if sum(box[2] != "table" for box in surfaces) == num_cupboards:
            break
    else:
        raise ValueError(f"num_cupboards={num_cupboards} cupboards do not fit into world_size={world_size}")
    tables = [box for box in surfaces if box[2] == "table"]
    cupboards = [box for box in surfaces if box[2] != "table"]
    locations = [c for box in surfaces for c in object_locations(box)]
    table_locations = [c for box in tables for c in object_locations(box)]
    goal_cells = [c for box in cupboards for c in object_locations(box)]
    starts: list[Cell] = []
    while len(starts) < len(goal_cells):
        cell = rng.choice(locations)
        if cell not in starts:
            starts.append(cell)
    objects: list[tuple[str, Cell, list[Cell]]] = []  # name, start, goal cells
    for index, (goal, start) in enumerate(zip(goal_cells, starts)):
        # Upstream crashes when it wants an extra table goal but there are no tables;
        # the IPC tasks are the runs that succeeded, i.e. no extra goal then.
        extra = rand_int(2) if table_locations else 0
        objects.append((f"object{index}", start, [goal, *(rng.choice(table_locations) for _ in range(extra))]))

    def xc(x: int) -> str:
        return f"x{x}"

    def yc(y: int) -> str:
        return f"y{y}"

    radius = range(-GRIPPER_RADIUS, GRIPPER_RADIUS + 1)
    object_lines = [
        "pr2 - robot", "cart - cart",
        *(f"{name} - object" for name, _, _ in objects),
        *(f"{xc(x)} - xc" for x in range(world_size)),
        *(f"{yc(y)} - yc" for y in range(world_size)),
        *(f"xrel{r} - xrel" for r in radius),
        *(f"yrel{r} - yrel" for r in radius),
    ]
    constants = [
        *(f"(leftof {xc(x)} {xc(x + 1)})" for x in range(world_size - 1)),
        *(f"(above {yc(y)} {yc(y + 1)})" for y in range(world_size - 1)),
        *(f"(leftof-rel xrel{r} xrel{r + 1})" for r in radius[:-1]),
        *(f"(above-rel yrel{r} yrel{r + 1})" for r in radius[:-1]),
        *(f"(sum-x {xc(x)} xrel{r} {xc(x + r)})" for x in range(world_size) for r in radius if 0 <= x + r < world_size),
        *(f"(sum-y {yc(y)} yrel{r} {yc(y + r)})" for y in range(world_size) for r in radius if 0 <= y + r < world_size),
        "(zerox-rel xrel0) ", "(zeroy-rel yrel0) ",
        *(f"(object-goal {name} {xc(x)} {yc(y)})" for name, _, goals in objects for x, y in goals),
    ]
    base = [
        "(parked pr2)", "(not-pushing pr2)", "(base-pos pr2 x0 y0)", "(base-obstacle x0 y0)",
        *(f"(base-obstacle {xc(x)} {yc(y)})(surface {xc(x)} {yc(y)})" for box in tables for x, y in cells(box)),
        *(
            f"(base-obstacle {xc(x)} {yc(y)})(gripper-obstacle {xc(x)} {yc(y)})"
            for box in cupboards
            for x, y in walls(box)
        ),
        *(f"(surface {xc(x)} {yc(y)})" for box in cupboards for x, y in object_locations(box)),
    ]
    cart = ["(cart-pos cart x0 y1)", "(not-pushed cart)", "(base-obstacle x0 y1)"]
    object_positions = [f"(object-pos {name} {xc(x)} {yc(y)})" for name, (x, y), _ in objects]
    gripper = [
        "(gripper-empty pr2)", "(gripper-rel pr2 xrel0 yrel0)",
        *(f"(gripper-obstacle {xc(x)} {yc(y)})" for _, (x, y), _ in objects),
    ]
    init = "\n   \n   ".join("\n   ".join(group) for group in (constants, base, cart, object_positions, gripper))
    goals = "\n   ".join(f"(object-done {name})" for name, _, _ in objects)
    return (f"""(define
  (problem test)
  (:domain tidybot)

  (:objects
   {" ".join(f"{line} {chr(10)}  " for line in object_lines)})

  (:init
   {init}
  )

  (:goal
   (and
   {goals}
  )))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Tidybot PDDL problem.")
    parser.add_argument("world_size", type=int)
    parser.add_argument("num_tables", type=int)
    parser.add_argument("num_cupboards", type=int, nargs="?", default=1)
    parser.add_argument("min_table_size", type=int, nargs="?", default=1)
    parser.add_argument("max_table_size", type=int, nargs="?", default=2)
    parser.add_argument("cupboard_size", type=int, nargs="?", default=4)
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
