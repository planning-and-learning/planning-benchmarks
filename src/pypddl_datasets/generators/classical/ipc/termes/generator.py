#!/usr/bin/env python3
# Port of pddl-generators/termes/generate-autoscale.py (Alvaro Torralba, Florian
# Pommerening) as called by Autoscale:
#   generate-autoscale.py {seed} pddl --size_x {x} --size_y {y} --min_height {min}
#       --max_height {max} --num_towers {towers} --ensure_plan --dont_remove_slack
# The initial board is empty; the goal board has one tower of max_height and
# num_towers - 1 towers of uniform height in [min_height, max_height].
#
# --ensure_plan rejects boards for which upstream's z3 model (solve.py) has no
# scaffold, i.e. no intermediate board that the robot can build block by block
# from the depot, covering the goal, and then dismantle down to it. has_scaffold
# decides the same constraints without z3. After ENSURE_PLAN_TRIES rejected boards
# the grid grows by one row or column, alternating, as upstream does.

from __future__ import annotations

import argparse
import random
import sys
from collections.abc import Callable
from typing import cast

Cell = tuple[int, int]
ENSURE_PLAN_TRIES = 20


def _neighbors(cell: Cell, size_x: int, size_y: int) -> list[Cell]:
    x, y = cell
    return [
        (x + dx, y + dy)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
        if 0 <= x + dx < size_x and 0 <= y + dy < size_y
    ]


def has_scaffold(goal: list[list[int]], depot: Cell, max_height: int) -> bool:
    """Decide satisfiability of upstream solve.py's z3 constraints.

    The z3 model asks for a support tree rooted at the depot: each cell with
    intermediate height ``I > 0`` (and each supporter) has an adjacent supporter
    ``p`` with ``I(p) <= I(v) <= I(p) + 1`` and ``goal(p) <= goal(v)``, where
    ``goal <= I <= max_height``. Heights grow by at most one per tree edge, so
    ``I = min(depth, max_height)`` is optimal and a solution exists iff some tree
    over goal-monotone edges gives every tower cell depth >= its goal height.

    Cells up to depth ``top = max_height - 1`` keep their exact depth as label
    ("core"); anything deeper only has to be reachable, through non-core cells,
    from a core cell of depth ``top`` (an "entry"). Each tower gets a core path
    ending in it or is deferred to the entry region, whose entry paths are added
    at the end; minimal cores suffice, so the search is exact. It agrees with
    upstream's z3 model on ~1900 sampled boards.
    """
    size_y, size_x = len(goal), len(goal[0])
    top = max_height - 1

    def height(cell: Cell) -> int:
        return goal[cell[1]][cell[0]]

    def edge(a: Cell, b: Cell) -> bool:
        return b != depot and (a == depot or height(b) >= height(a))

    labels: dict[Cell, int] = {depot: 0}
    towers = sorted(
        ((x, y) for y in range(size_y) for x in range(size_x) if goal[y][x] > 0),
        key=lambda cell: -height(cell),
    )

    def core_paths(target: Cell | None) -> list[list[tuple[Cell, int]]]:
        """Newly labelled cells of the depot paths that consistently label target
        with a depth in [goal(target), top], or (target None) that reach depth top."""
        found: list[list[tuple[Cell, int]]] = []
        seen: set[frozenset[tuple[Cell, int]]] = set()
        on_path = {depot}
        new: list[tuple[Cell, int]] = []

        def record() -> None:
            key = frozenset(new)
            if key not in seen:
                seen.add(key)
                found.append(list(new))

        def extend(cell: Cell, depth: int) -> None:
            if target is None and depth == top:
                record()
                return
            if cell == target:
                record()
                return
            if depth == top:
                return
            if target is not None and abs(cell[0] - target[0]) + abs(cell[1] - target[1]) > top - depth:
                return
            for successor in _neighbors(cell, size_x, size_y):
                if successor in on_path or not edge(cell, successor):
                    continue
                label = labels.get(successor)
                if label is None:
                    # a core cell's label is its final height, so it must reach its goal
                    if height(successor) > depth + 1:
                        continue
                    new.append((successor, depth + 1))
                elif label != depth + 1:
                    continue
                on_path.add(successor)
                extend(successor, depth + 1)
                on_path.discard(successor)
                if label is None:
                    new.pop()

        extend(depot, 0)
        found.sort(key=len)
        return found

    def entry_region() -> set[Cell]:
        stack = [cell for cell, label in labels.items() if label == top]
        region = set(stack)
        while stack:
            cell = stack.pop()
            for successor in _neighbors(cell, size_x, size_y):
                if successor not in region and successor not in labels and edge(cell, successor):
                    region.add(successor)
                    stack.append(successor)
        return region

    failed: set[tuple[object, ...]] = set()

    def attempt(key: tuple[object, ...], new: list[tuple[Cell, int]], then: Callable[[], bool]) -> bool:
        labels.update(new)
        state = (key, frozenset(labels.items()))
        if state not in failed:
            if then():
                return True
            failed.add(state)
        for new_cell, _ in new:
            del labels[new_cell]
        return False

    def cover(deferred: frozenset[Cell]) -> bool:
        """Add entry paths until every deferred tower is labelled or in the entry region."""
        region = entry_region()
        missing = [cell for cell in deferred if cell not in labels and cell not in region]
        if not missing:
            return True
        # Any solution's entry for missing[0] covers it on top of the current core,
        # so only such entry paths need to be tried.
        tower = missing[0]
        for new in core_paths(None):
            labels.update(new)
            covers = tower in labels or tower in entry_region()
            for new_cell, _ in new:
                del labels[new_cell]
            if covers and new and attempt(("cover", deferred), new, lambda: cover(deferred)):
                return True
        return False

    def search(towers: list[Cell], index: int, deferred: frozenset[Cell]) -> bool:
        """Give each tower a core path or defer it to the entry region."""
        if index == len(towers):
            return cover(deferred)
        cell = towers[index]
        if cell in labels:
            return labels[cell] >= height(cell) and search(towers, index + 1, deferred)
        extended = deferred | {cell}
        if attempt(("search", len(towers), index, extended), [], lambda: search(towers, index + 1, extended)):
            return True
        if height(cell) <= top:
            for new in core_paths(cell):
                if attempt(("search", len(towers), index, deferred), new, lambda: search(towers, index + 1, deferred)):
                    return True
        return False

    # Each tower on its own is a cheap necessary condition that rejects most
    # boards before the joint search.
    def alone(tower: Cell) -> bool:
        feasible = search([tower], 0, frozenset())
        labels.clear()  # a successful search leaves its labels behind
        labels[depot] = 0
        failed.clear()  # memo keys do not name the tower list
        return feasible

    return all(alone(tower) for tower in towers) and search(towers, 0, frozenset())


def _goal_board(
    size_x: int, size_y: int, min_height: int, max_height: int, num_towers: int, rng: random.Random
) -> list[list[int]]:
    board = [[0] * size_x for _ in range(size_y)]
    cells = [(x, y) for x in range(size_x) for y in range(size_y)]
    for index, cell_index in enumerate(rng.sample(range(len(cells)), num_towers)):
        x, y = cells[cell_index]
        board[y][x] = max_height if index == 0 else rng.randint(min_height, max_height)
    return board


def _depot(size_x: int, size_y: int, goal: list[list[int]]) -> Cell | None:
    # upstream: the empty cell in the topmost row closest to the middle column
    candidates = [(y, abs(x - size_x / 2), x, y) for x in range(size_x) for y in range(size_y) if goal[y][x] == 0]
    if not candidates:
        return None
    _, _, x, y = min(candidates)
    return x, y


def make_problem(
    size_x: int,
    size_y: int,
    min_height: int,
    max_height: int,
    num_towers: int,
    seed: int = 0,
) -> str:
    """Generate a single-robot Termes task from an empty board.

    Boards are resampled until a scaffold exists (upstream ``--ensure_plan``);
    after ``ENSURE_PLAN_TRIES`` failures (or if the towers do not fit) the grid
    grows by one column or row, alternating and starting with the shorter side.
    """
    for name, value, minimum in (
        ("size_x", size_x, 1),
        ("size_y", size_y, 1),
        ("min_height", min_height, 1),
        ("max_height", max_height, 1),
        ("num_towers", num_towers, 1),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if min_height > max_height:
        raise ValueError("min_height must not exceed max_height")

    rng = random.Random(seed)
    increase_x = size_x < size_y
    tries = 0
    while True:
        tries += 1
        if tries > ENSURE_PLAN_TRIES or num_towers > size_x * size_y:
            tries = 0
            if increase_x:
                size_x += 1
            else:
                size_y += 1
            increase_x = not increase_x
            continue
        goal = _goal_board(size_x, size_y, min_height, max_height, num_towers, rng)
        depot = _depot(size_x, size_y, goal)
        if depot is not None and has_scaffold(goal, depot, max_height):
            break

    name = f"termes-{size_x * size_y * max_height:04d}-{size_x}x{size_y}x{max_height}"
    comments = [name, "Initial state:"]
    comments += [" ".join(("R0D" if (x, y) == depot else " 0 ") for x in range(size_x)) for y in range(size_y)]
    comments += ["Goal state:"]
    comments += [" ".join(f" {goal[y][x]} " for x in range(size_x)) for y in range(size_y)]
    comments += [f"Maximal height: {max_height}"]

    objects = [f"n{n} - numb" for n in range(max_height + 1)]
    objects += [f"pos-{x}-{y} - position" for x in range(size_x) for y in range(size_y)]
    facts = [f"(height pos-{x}-{y} n0)" for x in range(size_x) for y in range(size_y)]
    facts += [f"(at pos-{depot[0]}-{depot[1]})"]
    facts += [f"(SUCC n{n + 1} n{n})" for n in range(max_height)]
    facts += [
        f"(NEIGHBOR pos-{x}-{y} pos-{nx}-{ny})"
        for x in range(size_x)
        for y in range(size_y)
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if 0 <= nx < size_x and 0 <= ny < size_y
    ]
    facts += [f"(IS-DEPOT pos-{depot[0]}-{depot[1]})"]
    goals = [f"(height pos-{x}-{y} n{goal[y][x]})" for x in range(size_x) for y in range(size_y)]
    goals += ["(not (has-block))"]

    lines = [f"(define (problem {name})", "(:domain termes)"]
    lines += [f"; {comment}" for comment in comments]
    lines += ["(:objects"] + [f"    {o}" for o in objects] + [")", "(:init"]
    lines += [f"    {f}" for f in facts] + [")", "(:goal (and"]
    lines += [f"    {g}" for g in goals] + ["))", ")", ""]
    return ("\n".join(lines)).lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Termes PDDL problem.")
    parser.add_argument("seed", type=int)
    parser.add_argument("--size_x", type=int, default=4)
    parser.add_argument("--size_y", type=int, default=4)
    parser.add_argument("--min_height", type=int, default=1)
    parser.add_argument("--max_height", type=int, default=4)
    parser.add_argument("--num_towers", type=int, default=4)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.size_x, args.size_y, args.min_height, args.max_height, args.num_towers, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
