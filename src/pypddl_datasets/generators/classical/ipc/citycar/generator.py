#!/usr/bin/env python3
# Port of pddl-generators citycar/generator.py (Mauro Vallati, IPC 2014; modified by
# Masataro Asai): `generator.py rows columns cars garages [--density D] [--seed S]`.
# domain.pddl is the IPC 2014 satisficing file; domain_citycar14opt.pddl the optimal
# one (no `(not (= ...))` preconditions). Both accept the same problems.

from __future__ import annotations

import argparse
import random
import sys


def make_problem(
    num_rows: int,
    num_columns: int,
    num_cars: int,
    num_garages: int,
    density: float = 1.0,
    seed: int | None = None,
) -> str:
    """Generate a Citycar task on a ``num_rows`` x ``num_columns`` junction grid.

    Straight and diagonal neighbours are listed both ways; ``num_rows + 2``
    roads are available. Each car starts in a uniform garage, garages sit at
    uniform junctions of row 0, goals at uniform junctions of the last row.
    With ``density < 1`` each interior junction is clear only with that
    probability (upstream's sparsity); the IPC tasks use density 1.
    """
    for name, value, minimum in (
        ("num_rows", num_rows, 2),
        ("num_columns", num_columns, 2),
        ("num_cars", num_cars, 1),
        ("num_garages", num_garages, 1),
    ):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if not 0.0 <= density <= 1.0:
        raise ValueError("density must be in [0, 1]")

    rng = random.Random(seed)
    starts = [rng.randint(0, num_garages - 1) for _ in range(num_cars)]

    def j(row: int, column: int) -> str:
        return f"junction{row}-{column}"

    init = []
    for row in range(num_rows):
        for column in range(num_columns - 1):
            init += [f"(same_line {j(row, column)} {j(row, column + 1)})", f"(same_line {j(row, column + 1)} {j(row, column)})"]
    for column in range(num_columns):
        for row in range(num_rows - 1):
            init += [f"(same_line {j(row, column)} {j(row + 1, column)})", f"(same_line {j(row + 1, column)} {j(row, column)})"]
    for row in range(num_rows - 1):
        for column in range(num_columns - 1):
            init += [
                f"(diagonal {j(row, column)} {j(row + 1, column + 1)})",
                f"(diagonal {j(row + 1, column + 1)} {j(row, column)})",
                f"(diagonal {j(row, column + 1)} {j(row + 1, column)})",
                f"(diagonal {j(row + 1, column)} {j(row, column + 1)})",
            ]
    for row in range(num_rows):
        for column in range(num_columns):
            interior = 0 < row < num_rows - 1 and 0 < column < num_columns - 1
            if density == 1.0 or not interior or density > rng.random():
                init.append(f"(clear {j(row, column)})")
    init += [f"(at_garage garage{g} {j(0, rng.randint(0, num_columns - 1))})" for g in range(num_garages)]
    init += [f"(starting car{c} garage{g})" for c, g in enumerate(starts)]
    init.append("(= (total-cost) 0)")
    goals = [f"(arrived car{c} {j(num_rows - 1, rng.randint(0, num_columns - 1))})" for c in range(num_cars)]

    junction_lines = "\n".join(" ".join(j(row, column) for column in range(num_columns)) for row in range(num_rows))
    return (f"""(define (problem citycar-{num_rows}-{num_columns}-{num_cars})
(:domain citycar)
(:objects
{junction_lines} - junction
{' '.join(f'car{c}' for c in range(num_cars))} - car
{' '.join(f'garage{g}' for g in range(num_garages))} - garage
{' '.join(f'road{r}' for r in range(num_rows + 2))} - road
)
(:init
{chr(10).join(init)}
)
(:goal
(and
{chr(10).join(goals)}
)
)
(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Citycar PDDL problem.")
    parser.add_argument("num_rows", type=int)
    parser.add_argument("num_columns", type=int)
    parser.add_argument("num_cars", type=int)
    parser.add_argument("num_garages", type=int)
    parser.add_argument("--density", type=float, default=1.0, help="probability that an interior junction is usable (default: 1.0)")
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
