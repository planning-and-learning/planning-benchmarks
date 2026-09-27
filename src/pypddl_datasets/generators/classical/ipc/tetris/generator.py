#!/usr/bin/env python3
# Port of pddl-generators tetris/generator.py (Mauro Vallati, IPC 2014). Block types:
# 1 = only 1x1, 2 = only 2x1, 3 = only L, 4 = mix (the only type of the IPC 2014 tasks;
# Autoscale 21.11 uses 1-4). Like the IPC and Autoscale tasks (unlike upstream),
# problems initialise total-cost and minimize it.

from __future__ import annotations

import argparse
import random
import sys
from typing import cast

COLUMNS = 4


# grid, squares, 2x1 pieces, L pieces, at-facts
Placement = tuple[list[list[str]], list[str], list[str], list[str], list[str]]


def _cell(row: int, column: int) -> str:
    return f"f{row}-{column}f"


def _place_squares_only(rng: random.Random, num_rows: int) -> Placement:
    """Type 1: 1..half*4 squares on uniform free cells of rows 0..num_rows/2 (upstream's inclusive bound)."""
    grid = [["free"] * COLUMNS for _ in range(num_rows)]
    free = [(x, y) for x in range(num_rows // 2 + 1) for y in range(COLUMNS)]
    squares: list[str] = []
    at_facts: list[str] = []
    for index in range(rng.randint(1, (num_rows // 2) * COLUMNS)):
        x, y = free.pop(rng.randrange(len(free)))
        name = f"square{index}"
        grid[x][y] = name
        squares.append(name)
        at_facts.append(f"(at_square {name} {_cell(x, y)})")
    return grid, squares, [], [], at_facts


def _place_straights_only(rng: random.Random, num_rows: int) -> Placement | None:
    """Type 2: 1..(num_rows/2)*2 2x1 pieces, each on a uniform free cell of rows 0..num_rows/2
    and upstream's direction rule (1 up, 2 right, 3 down, 4 left; up at row 0 falls through
    to right, right at the last column to left). None where upstream would loop forever."""
    grid = [["free"] * COLUMNS for _ in range(num_rows)]
    top = num_rows // 2
    straights: list[str] = []
    at_facts: list[str] = []
    target = rng.randint(1, (num_rows // 2) * (COLUMNS // 2))

    def free(x: int, y: int) -> bool:
        return 0 <= x < num_rows and 0 <= y < COLUMNS and grid[x][y] == "free"

    while len(straights) < target:
        if not any(
            free(x, y) and any(free(x + dx, y + dy) for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)))
            for x in range(top + 1)
            for y in range(COLUMNS)
        ):
            return None
        x, y = rng.randint(0, top), rng.randint(0, COLUMNS - 1)
        if not free(x, y):
            continue
        direction = rng.randint(1, 4)
        other = None
        if direction == 1:
            if x != 0:
                other = (x - 1, y) if free(x - 1, y) else None
            else:
                direction = 2
        if direction == 2:
            if y != COLUMNS - 1:
                other = (x, y + 1) if free(x, y + 1) else None
            else:
                direction = 4
        if direction == 3:
            other = (x + 1, y) if free(x + 1, y) else None
        if direction == 4 and y != 0:
            other = (x, y - 1) if free(x, y - 1) else None
        if other is None:
            continue
        name = f"straight{len(straights)}"
        grid[x][y] = grid[other[0]][other[1]] = name
        straights.append(name)
        at_facts.append(f"(at_two {name} {_cell(x, y)} {_cell(*other)})")
    return grid, [], straights, [], at_facts


def _place(rng: random.Random, num_rows: int, block_type: int = 4) -> Placement | None:
    """One upstream draw; None where upstream would loop forever (no room left for a piece)."""
    if block_type == 1:
        return _place_squares_only(rng, num_rows)
    if block_type == 2:
        return _place_straights_only(rng, num_rows)
    grid = [["free"] * COLUMNS for _ in range(num_rows)]
    half = num_rows // 2
    at_facts: list[str] = []
    right_ls: list[str] = []
    for index in range(rng.randint(1, (num_rows // 4) * (COLUMNS // 2))):
        anchors = [
            (x, y)
            for x in range(half)
            for y in range(COLUMNS - 1)
            if grid[x][y] == grid[x + 1][y] == grid[x + 1][y + 1] == "free"
        ]
        if not anchors:
            return None
        x, y = rng.choice(anchors)
        name = f"rightl{index}"
        for row, column in ((x, y), (x + 1, y), (x + 1, y + 1)):
            grid[row][column] = name
        right_ls.append(name)
        at_facts.append(f"(at_right_l {name} {_cell(x, y)} {_cell(x + 1, y)} {_cell(x + 1, y + 1)})")
    if block_type == 3:
        return grid, [], [], right_ls, at_facts
    straights: list[str] = []
    for row in range(1, half):
        for column in range(COLUMNS - 1):
            if grid[row][column] == grid[row - 1][column] == "free" and rng.randint(1, 4) > 2:
                name = f"straight{len(straights)}"
                grid[row][column] = grid[row - 1][column] = name
                straights.append(name)
                at_facts.append(f"(at_two {name} {_cell(row - 1, column)} {_cell(row, column)})")
    squares: list[str] = []
    for row in range(half):
        for column in range(COLUMNS - 1):
            if grid[row][column] == "free" and rng.randint(1, 4) > 2:
                name = f"square{len(squares)}"
                grid[row][column] = name
                squares.append(name)
                at_facts.append(f"(at_square {name} {_cell(row, column)})")
    return grid, squares, straights, right_ls, at_facts


def make_problem(num_rows: int, seed: int | None = None, block_type: int = 4) -> str:
    """Generate a Tetris task on a ``num_rows`` x 4 grid; the goal clears the upper half.

    ``block_type`` 1: only 1x1 pieces (1..num_rows*2, uniform free cells of rows
    0..num_rows/2); 2: only 2x1 pieces (1..num_rows, upstream's random direction
    rule); 3: only L-pieces (as in type 4); 4 (IPC): L-pieces (1..num_rows//4*2 of
    them) are dropped on uniform free anchors in the upper half; then each free
    vertical pair in rows 0..num_rows/2-1, columns 0-2,
    gets a 2x1 piece with probability 1/2, then each free cell there a 1x1 piece
    with probability 1/2. Draws where upstream would hang are redrawn. Solvability
    is not guaranteed, as upstream.
    """
    checked = cast(object, num_rows)  # runtime check: callers may pass any type
    if not isinstance(checked, int) or isinstance(checked, bool) or checked < 4 or checked % 2:
        raise ValueError("num_rows must be an even integer at least 4")
    kind = cast(object, block_type)  # runtime check: callers may pass any type
    if isinstance(kind, bool) or kind not in (1, 2, 3, 4):
        raise ValueError("block_type must be 1, 2, 3 or 4")
    rng = random.Random(seed)
    placed = None
    while placed is None:
        placed = _place(rng, num_rows, block_type)
    grid, squares, straights, right_ls, at_facts = placed

    positions = "\n".join(" ".join(_cell(row, column) for column in range(COLUMNS)) for row in range(num_rows))
    connected: list[str] = []
    for row in range(num_rows):
        for column in range(COLUMNS - 1):
            a, b = _cell(row, column), _cell(row, column + 1)
            connected += [f"(connected {a} {b})", f"(connected {b} {a})"]
    for row in range(num_rows - 1):
        for column in range(COLUMNS):
            a, b = _cell(row, column), _cell(row + 1, column)
            connected += [f"(connected {a} {b})", f"(connected {b} {a})"]
    clear = [
        f"(clear {_cell(row, column)})"
        for row in range(num_rows)
        for column in range(COLUMNS)
        if grid[row][column] == "free"
    ]
    goal = [f"(clear {_cell(row, column)})" for row in range(num_rows // 2) for column in range(COLUMNS)]
    return (f"""(define (problem tetris-{num_rows}-{block_type}-{rng.randint(0, 9875232)})
(:domain tetris)
(:objects
{positions} - position
{" ".join(squares) or "nothing"} - one_square
{" ".join(straights) or "nada"} - two_straight
{" ".join(right_ls) or "nisba"} - right_l
)
(:init
{chr(10).join(connected + clear + at_facts)}
(= (total-cost) 0)
)
(:goal
(and
{chr(10).join(goal)}
)
)
(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Tetris PDDL problem (IPC 2014 / Autoscale).")
    parser.add_argument("-r", "--num-rows", type=int, required=True, help="even number of grid rows; 4 columns")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument(
        "-b", "--block-type", type=int, default=4, help="1 = 1x1, 2 = 2x1, 3 = L, 4 = mix (IPC, default)"
    )
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_rows, args.seed, args.block_type)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
