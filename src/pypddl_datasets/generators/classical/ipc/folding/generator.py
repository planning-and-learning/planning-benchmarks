#!/usr/bin/env python3
"""Port of ipc2023-classical/domain-folding generate.py (Daniel Fišer, public domain).

Same random draws in the same order as upstream, so ``make_problem(scenario,
length, folds, seed)`` reproduces the IPC 2023 task generated with
``./generate.py seed scenario length folds``.
"""

from __future__ import annotations

import argparse
import random
import sys

SCENARIOS = ("zigzag", "spiral", "bias-spiral")
MAX_TRIES = 10000
NEXT_DIRECTION = {
    ("up", "clockwise"): "right",
    ("up", "counterclockwise"): "left",
    ("down", "clockwise"): "left",
    ("down", "counterclockwise"): "right",
    ("left", "clockwise"): "up",
    ("left", "counterclockwise"): "down",
    ("right", "clockwise"): "down",
    ("right", "counterclockwise"): "up",
}
STEP = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}


def _rotate(directions: list[str], node: int, rotation: str) -> tuple[list[tuple[int, int]], list[str]] | None:
    """Rotate the string after ``node``; None if it would intersect itself."""
    directions = directions[: node - 1] + [NEXT_DIRECTION[d, rotation] for d in directions[node - 1 :]]
    num_nodes = len(directions) + 1
    positions = [(num_nodes, num_nodes)]
    for direction in directions:
        dx, dy = STEP[direction]
        nxt = (positions[-1][0] + dx, positions[-1][1] + dy)
        if nxt in positions:
            return None
        positions.append(nxt)
    return positions, directions


def _goal_positions(rng: random.Random, scenario: str, num_nodes: int, num_folds: int) -> list[tuple[int, int]]:
    for _ in range(MAX_TRIES):
        directions = ["up"] * (num_nodes - 1)
        nodes = list(range(1, num_nodes))
        rng.shuffle(nodes)
        nodes = nodes[:num_folds]
        folds: dict[int, str] = {}
        for node in nodes:
            if scenario == "zigzag":
                folds[node] = rng.choice(["clockwise", "counterclockwise"])
            elif scenario == "spiral":
                folds[node] = "clockwise"
            else:
                folds[node] = rng.choice(["clockwise", "clockwise", "clockwise", "counterclockwise"])
        positions: list[tuple[int, int]] | None = None
        for node in nodes:
            rotated = _rotate(directions, node, folds[node])
            if rotated is None:
                positions = None
                break
            positions, directions = rotated
        if positions is not None:
            return positions
    raise ValueError(f"no self-avoiding fold sequence found in {MAX_TRIES} tries")


def make_problem(scenario: str, num_nodes: int, num_folds: int, seed: int | None = None) -> str:
    """Generate a Folding task.

    A string of ``num_nodes`` nodes starts as a vertical line at
    ``(num_nodes, num_nodes)``. The goal is the shape reached by rotating
    ``num_folds`` distinct random nodes (shuffled order, at most one rotation
    per node): clockwise or counterclockwise uniformly (``zigzag``), always
    clockwise (``spiral``), or clockwise with probability 3/4
    (``bias-spiral``). Draws that make the string intersect itself are
    redrawn. Every node's goal position is given, plus ``(not (rotating))``.
    """
    if scenario not in SCENARIOS:
        raise ValueError(f"scenario must be one of {', '.join(SCENARIOS)}")
    checks: list[tuple[str, object, int]] = [("num_nodes", num_nodes, 2), ("num_folds", num_folds, 1)]
    for name, value, minimum in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if num_folds > num_nodes - 1:
        raise ValueError("num_folds must be at most num_nodes - 1")

    rng = random.Random(seed)
    goal = _goal_positions(rng, scenario, num_nodes, num_folds)
    rand = int(1000000 * rng.random())

    coords = [f"c{i}" for i in range(1, 2 * num_nodes)]
    start = [(num_nodes, num_nodes + i) for i in range(num_nodes)]
    occupied = {(f"c{x}", f"c{y}") for x, y in start}
    init = [
        *(f"    (next-direction {d} {r} {n})" for (d, r), n in NEXT_DIRECTION.items()),
        "",
        *(f"    (coord-inc c{i} c{i + 1})" for i in range(1, 2 * num_nodes - 1)),
        "",
        *(f"    (connected n{i} n{i + 1})" for i in range(1, num_nodes)),
        f"    (end-node n{num_nodes})",
        "",
        *(f"    (at n{i + 1} c{x} c{y})" for i, (x, y) in enumerate(start)),
        *(f"    (heading n{i} up)" for i in range(1, num_nodes)),
        *(f"    (free {x} {y})" for x in coords for y in coords if (x, y) not in occupied),
        "",
        "    (= (total-cost) 0)",
        "    (= (rotate-cost) 1)",
        "    (= (update-cost) 0)",
    ]
    goals = [f"        (at n{i + 1} c{x} c{y})" for i, (x, y) in enumerate(goal)]
    return (f"""(define (problem folding-{scenario}-{num_nodes}-{num_folds}-{rand})
(:domain folding)

(:objects
    {' '.join(f"n{i}" for i in range(1, num_nodes + 1))} - node
    {' '.join(coords)} - coord
)
(:init
{chr(10).join(init)}
)
(:goal
    (and
{chr(10).join(goals)}
        (not (rotating))
    )
)
(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Folding PDDL problem (IPC 2023).")
    parser.add_argument("scenario", choices=SCENARIOS)
    parser.add_argument("num_nodes", type=int, help="length of the string")
    parser.add_argument("num_folds", type=int, help="number of rotations")
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
