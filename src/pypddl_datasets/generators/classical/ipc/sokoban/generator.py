#!/usr/bin/env python3
# Random Sokoban levels in the encoding of pddl-generators sokoban/build-problems.py, the
# converter behind the IPC 2008/2011 tasks and the Autoscale 21.11 tasks. The reference
# levels themselves are hand-made (Microban, Multiban, Hexoban); this generator draws
# random levels of similar size instead, on square or hexagonal grids and with one or
# more players. Levels are built by reverse play from the goal, so every task is solvable.

from __future__ import annotations

import argparse
import random
import sys
from typing import cast

Cell = tuple[int, int]  # (column, row)
Dirs = dict[str, tuple[int, int]]
DIRECTIONS: Dirs = {"dir-up": (0, -1), "dir-down": (0, 1), "dir-left": (-1, 0), "dir-right": (1, 0)}
# Hexoban as in build-problems.py: only cells with (column + row) even exist; east and
# west are two columns apart, the diagonals one column and one row.
HEX_DIRECTIONS: Dirs = {
    "dir-east": (2, 0), "dir-west": (-2, 0), "dir-northeast": (1, -1),
    "dir-northwest": (-1, -1), "dir-southeast": (1, 1), "dir-southwest": (-1, 1),
}
ATTEMPTS = 3


def _floor(rng: random.Random, width: int, height: int, num_floor: int, dirs: Dirs) -> set[Cell]:
    """A connected random region inside the border, grown from a random cell.

    A frontier cell is added with weight 1 / (its floor neighbours), which favours
    corridors and irregular rooms over round blobs (walls per floor cell ~1.13, the
    IPC Microban levels have 1.15).
    """

    def neighbours(cell: Cell) -> list[Cell]:
        return [
            (cell[0] + dx, cell[1] + dy)
            for dx, dy in dirs.values()
            if 1 <= cell[0] + dx < width - 1 and 1 <= cell[1] + dy < height - 1
        ]

    if dirs is DIRECTIONS:  # draw order of the original square generator
        start = (rng.randrange(1, width - 1), rng.randrange(1, height - 1))
    else:
        start = rng.choice(_interior(width, height, dirs))
    floor, frontier = {start}, set(neighbours(start))
    while len(floor) < num_floor:
        candidates = sorted(frontier)
        weights = [1 / sum(1 for other in neighbours(cell) if other in floor) for cell in candidates]
        cell = rng.choices(candidates, weights)[0]
        floor.add(cell)
        frontier.discard(cell)
        frontier.update(other for other in neighbours(cell) if other not in floor)
    return floor


def _interior(width: int, height: int, dirs: Dirs) -> list[Cell]:
    return [
        (x, y) for y in range(1, height - 1) for x in range(1, width - 1)
        if dirs is DIRECTIONS or (x + y) % 2 == 0
    ]


def _reachable(floor: set[Cell], stones: set[Cell], player: Cell, dirs: Dirs) -> set[Cell]:
    seen, stack = {player}, [player]
    while stack:
        x, y = stack.pop()
        for dx, dy in dirs.values():
            cell = (x + dx, y + dy)
            if cell in floor and cell not in stones and cell not in seen:
                seen.add(cell)
                stack.append(cell)
    return seen


def _pulls(floor: set[Cell], stones: set[Cell], player: Cell, dirs: Dirs) -> list[tuple[Cell, Cell]]:
    """Legal pulls as (player cell, direction): the player steps away from a stone and drags it."""
    return [
        (cell, (dx, dy))
        for cell in sorted(_reachable(floor, stones, player, dirs))
        for dx, dy in dirs.values()
        if (cell[0] - dx, cell[1] - dy) in stones
        and (cell[0] + dx, cell[1] + dy) in floor
        and (cell[0] + dx, cell[1] + dy) not in stones
    ]


def _pull(stones: set[Cell], pull: tuple[Cell, Cell]) -> tuple[set[Cell], Cell]:
    (x, y), (dx, dy) = pull
    return (stones - {(x - dx, y - dy)}) | {(x, y)}, (x + dx, y + dy)


def _scramble(
    rng: random.Random, floor: set[Cell], goals: set[Cell], player: Cell, num_pulls: int, dirs: Dirs
) -> tuple[set[Cell], Cell, dict[Cell, Cell]]:
    """Apply up to ``num_pulls`` random pulls, then move the player to a random reachable cell.

    Also returns where each goal's stone ended up (goal cell -> stone cell).

    A pull is a push played backwards, so reversing the sequence solves the level.
    Pulls are weighted by (cells the player can still reach)^3, which avoids pulling
    the player into dead ends, and by 4 for stones still on their goal.
    """
    stones = set(goals)
    where = {goal: goal for goal in goals}
    for _ in range(num_pulls):
        pulls = _pulls(floor, stones, player, dirs)
        if not pulls:
            break
        weights: list[int] = []
        for pull in pulls:
            after = _pull(stones, pull)
            (x, y), (dx, dy) = pull
            weights.append(len(_reachable(floor, *after, dirs)) ** 3 * (4 if (x - dx, y - dy) in goals else 1))
        pull = rng.choices(pulls, weights)[0]
        (x, y), (dx, dy) = pull
        where = {goal: (x, y) if cell == (x - dx, y - dy) else cell for goal, cell in where.items()}
        stones, player = _pull(stones, pull)
    return stones, rng.choice(sorted(_reachable(floor, stones, player, dirs))), where


def _scramble_players(
    rng: random.Random, floor: set[Cell], goals: set[Cell], players: list[Cell], num_pulls: int, dirs: Dirs,
    log: list[tuple[int, Cell, tuple[Cell, Cell]]] | None = None,
) -> tuple[set[Cell], list[Cell]]:
    """Multi-player scramble: each pull is made by a random player that can pull.

    A player walks only through free floor (stones and the other players block) and
    pulls as in ``_scramble``. Reversing the pulls (each player walking back and
    pushing) solves the level and may need several players. Players stay where their
    last pull leaves them, so they can end on goal cells. ``log`` records
    (player index, position before walking to the pull, pull) for each pull.
    """
    stones, players = set(goals), list(players)
    for _ in range(num_pulls):
        options: list[tuple[int, set[Cell], list[tuple[Cell, Cell]]]] = []
        for index, player in enumerate(players):
            own_floor = floor - {p for i, p in enumerate(players) if i != index}
            pulls = _pulls(own_floor, stones, player, dirs)
            if pulls:
                options.append((index, own_floor, pulls))
        if not options:
            break
        index, own_floor, pulls = rng.choice(options)
        weights: list[int] = []
        for pull in pulls:
            after = _pull(stones, pull)
            (x, y), (dx, dy) = pull
            weights.append(len(_reachable(own_floor, *after, dirs)) ** 3 * (4 if (x - dx, y - dy) in goals else 1))
        pull = rng.choices(pulls, weights)[0]
        if log is not None:
            log.append((index, players[index], pull))
        stones, players[index] = _pull(stones, pull)
    return stones, players


def make_problem(
    width: int,
    height: int,
    num_floor: int,
    num_stones: int,
    seed: int | None = None,
    num_pulls: int | None = None,
    grid: str = "square",
    num_players: int = 1,
    style: str = "ipc",
) -> str:
    """Generate a solvable Sokoban task.

    ``width`` x ``height`` bounds the level including its walls; ``num_floor``
    connected floor cells are grown inside, every non-floor cell touching the floor
    (8-neighbourhood) is a wall, the rest is empty outside space as in the IPC mazes.
    Goals are ``num_stones`` random floor cells a stone can be pulled away from; stones
    start on them and are scrambled by up to ``num_pulls`` random reverse pushes
    (default 20 * num_stones). Of ``ATTEMPTS`` scrambles the one leaving the fewest
    stones on goals is kept; a level with every stone still on its goal is redrawn.
    The bounding box is cropped to the walls.

    ``grid="hex"`` builds a Hexoban level (six directions, every second cell of
    the box, as the Autoscale hexoban tasks). ``num_players`` > 1 starts the players
    on random free floor cells and lets every player pull (``_scramble_players``),
    so undoing the pulls can need several players, as in the Autoscale
    multi-player levels.

    ``style="learning"`` (square grid, one player) writes the IPC 2023 learning-track
    encoding instead: every cell a ``loc_<row>_<col>`` location, ``adjacent`` facts
    with the constant directions down/left/up/right, and one goal cell per box.
    """
    if grid not in ("square", "hex"):
        raise ValueError("grid must be 'square' or 'hex'")
    if style not in ("ipc", "learning"):
        raise ValueError("style must be 'ipc' or 'learning'")
    if style == "learning" and (grid != "square" or num_players != 1):
        raise ValueError("style='learning' needs grid='square' and num_players=1")
    for name, value, minimum in (
        ("width", width, 3), ("height", height, 3), ("num_floor", num_floor, 2), ("num_stones", num_stones, 1),
        ("num_players", num_players, 1),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    dirs = HEX_DIRECTIONS if grid == "hex" else DIRECTIONS
    if num_floor > len(_interior(width, height, dirs)):
        raise ValueError(f"num_floor must fit inside the walls: at most {len(_interior(width, height, dirs))}")
    if num_stones + num_players > num_floor:
        raise ValueError("num_stones must leave num_floor room for the players")
    if num_pulls is None:
        num_pulls = 20 * num_stones

    rng = random.Random(seed)
    for _ in range(100):
        full_floor = _floor(rng, width, height, num_floor, dirs)
        cells = sorted(full_floor)
        # Goals where a stone can be pulled away at all (two free cells in a line).
        pullable = [
            cell
            for cell in cells
            if any(
                (cell[0] + dx, cell[1] + dy) in full_floor and (cell[0] + 2 * dx, cell[1] + 2 * dy) in full_floor
                for dx, dy in dirs.values()
            )
        ]
        goals = set(rng.sample(pullable if len(pullable) >= num_stones else cells, num_stones))
        free = [c for c in cells if c not in goals]
        # ponytail: best of ATTEMPTS scrambles (fewest stones left on goals); matches the
        # IPC's ~12% stones-on-goal, raise ATTEMPTS if larger levels need more mixing.
        if num_players == 1:
            stones, player, where = min(
                (_scramble(rng, full_floor, goals, rng.choice(free), num_pulls, dirs) for _ in range(ATTEMPTS)),
                key=lambda result: len(result[0] & goals),  # pylint: disable=cell-var-from-loop  # min() calls it now
            )
            placed = [player]
        else:
            stones, placed = min(
                (
                    _scramble_players(rng, full_floor, goals, rng.sample(free, num_players), num_pulls, dirs)
                    for _ in range(ATTEMPTS)
                ),
                key=lambda result: len(result[0] & goals),  # pylint: disable=cell-var-from-loop  # min() calls it now
            )
            where: dict[Cell, Cell] = {}  # only style="learning" uses it, which needs one player
        if stones != goals:
            break
    else:
        raise ValueError("could not move any stone off its goal; increase num_floor or num_pulls")

    floor = full_floor
    ring = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)] if dirs is DIRECTIONS else list(dirs.values())
    walls = {(x + dx, y + dy) for x, y in floor for dx, dy in ring if (x + dx, y + dy) not in floor}
    min_x, min_y = min(x for x, _ in walls), min(y for _, y in walls)
    if dirs is HEX_DIRECTIONS and (min_x + min_y) % 2:
        min_x -= 1  # keep (column + row) even for existing cells after cropping
    cols, rows = max(x for x, _ in walls) - min_x + 1, max(y for _, y in walls) - min_y + 1

    def shift(cells: set[Cell]) -> set[Cell]:
        return {(x - min_x, y - min_y) for x, y in cells}

    walls, floor, stones, goals = shift(walls), shift(floor), shift(stones), shift(goals)
    players = shift(set(placed))
    if style == "learning":
        return _learning_problem(cols, rows, floor, players, {
            (goal[0] - min_x, goal[1] - min_y): (cell[0] - min_x, cell[1] - min_y) for goal, cell in where.items()
        }, seed)
    digits = len(str(max(rows, cols)))

    def pos(cell: Cell) -> str:
        return f"pos-{cell[0] + 1:0{digits}d}-{cell[1] + 1:0{digits}d}"

    def symbol(cell: Cell) -> str:
        if cell in walls:
            return "#"
        if cell in players:
            return "+" if cell in goals else "@"
        if cell in stones:
            return "*" if cell in goals else "$"
        return "." if cell in goals else " "

    maze = ["".join(symbol((x, y)) for x in range(cols)).rstrip() for y in range(rows)]
    ordered = sorted(stones)
    stone_names = {cell: f"stone-{i + 1:02d}" for i, cell in enumerate(sorted(stones, key=lambda c: (c[1], c[0])))}
    player_names = {cell: f"player-{i + 1:02d}" for i, cell in enumerate(sorted(players, key=lambda c: (c[1], c[0])))}
    objects = [f"{d} - direction" for d in dirs] + [f"{name} - player" for name in player_names.values()]
    objects += [f"{name} - stone" for name in stone_names.values()]
    init: list[str] = []
    for y in range(rows):
        for x in range(cols):
            cell = (x, y)
            if dirs is HEX_DIRECTIONS and (x + y) % 2:
                continue
            objects.append(f"{pos(cell)} - location")
            init.append(f"({'is-goal' if cell in goals else 'is-nongoal'} {pos(cell)})")
            if cell in walls:
                continue
            if cell not in players and cell not in stones:
                init.append(f"(clear {pos(cell)})")
            for direction, (dx, dy) in dirs.items():
                other = (x + dx, y + dy)
                if 0 <= other[0] < cols and 0 <= other[1] < rows and other not in walls:
                    init.append(f"(move-dir {pos(cell)} {pos(other)} {direction})")
    init.extend(f"(at {name} {pos(cell)})" for cell, name in player_names.items())
    for cell in ordered:
        init.append(f"(at {stone_names[cell]} {pos(cell)})")
        if cell in goals:
            init.append(f"(at-goal {stone_names[cell]})")
    goal = sorted(f"(at-goal {name})" for name in stone_names.values())

    name = f"{'hexoban' if grid == 'hex' else 'sokoban'}-{cols}x{rows}-f{num_floor}-s{num_stones}"
    name += (f"-p{num_players}" if num_players > 1 else "") + (f"-{seed}" if seed is not None else "")
    lines = [*(f";; {line}" for line in maze), "", f"(define (problem {name})", "  (:domain sokoban-sequential)"]
    lines += ["  (:objects", *(f"    {o}" for o in sorted(objects)), "  )"]
    lines += ["  (:init", *(f"    {fact}" for fact in sorted(init)), "    (= (total-cost) 0)", "  )"]
    lines += ["  (:goal (and", *(f"    {g}" for g in goal), "  ))", "  (:metric minimize (total-cost))", ")"]
    return ("\n".join(lines) + "\n").lower()


LEARNING_DIRECTIONS = {(0, 1): "down", (-1, 0): "left", (0, -1): "up", (1, 0): "right"}


def _learning_problem(
    cols: int, rows: int, floor: set[Cell], players: set[Cell], where: dict[Cell, Cell], seed: int | None
) -> str:
    """IPC 2023 learning-track Sokoban encoding (typed, direction constants, box -> goal cell)."""
    def loc(cell: Cell) -> str:
        return f"loc_{cell[1] + 1}_{cell[0] + 1}"

    goal_of = dict(sorted(((cell, goal) for goal, cell in where.items()), key=lambda item: (item[0][1], item[0][0])))
    boxes = {cell: f"box{i + 1}" for i, cell in enumerate(goal_of)}
    (player,) = players
    init = [f"(at-robot {loc(player)})"] + [f"(at {boxes[cell]} {loc(cell)})" for cell in goal_of]
    init += [f"(clear {loc(cell)})" for cell in sorted(floor, key=lambda c: (c[1], c[0])) if cell not in boxes]
    for cell in sorted(floor, key=lambda c: (c[1], c[0])):
        for (dx, dy), direction in LEARNING_DIRECTIONS.items():
            if (cell[0] + dx, cell[1] + dy) in floor:
                init.append(f"(adjacent {loc(cell)} {loc((cell[0] + dx, cell[1] + dy))} {direction})")
    locations = " ".join(loc((x, y)) for y in range(rows) for x in range(cols))
    name = f"sokoban-{cols}x{rows}-b{len(boxes)}" + (f"-{seed}" if seed is not None else "")
    lines = [f"(define (problem {name})", " (:domain sokoban)", " (:objects", f"    {locations} - location"]
    lines += [f"    {' '.join(boxes.values())} - box", "    )", " (:init", *(f"    {fact}" for fact in init), "    )"]
    lines += [" (:goal (and", *(f"    (at {boxes[cell]} {loc(goal)})" for cell, goal in goal_of.items()), "    ))", ")"]
    return ("\n".join(lines) + "\n").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a solvable Sokoban PDDL problem (IPC encoding).")
    parser.add_argument("-x", "--width", type=int, required=True, help="level width including walls")
    parser.add_argument("-y", "--height", type=int, required=True, help="level height including walls")
    parser.add_argument("-f", "--num-floor", type=int, required=True, help="connected floor cells")
    parser.add_argument("-b", "--num-stones", type=int, required=True)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--num-pulls", type=int, help="random reverse pushes (default: 20 * num_stones)")
    parser.add_argument(
        "--grid", choices=("square", "hex"), default="square", help="square (IPC) or hexagonal (Hexoban) grid"
    )
    parser.add_argument("--num-players", type=int, default=1, help="players (default: 1)")
    parser.add_argument(
        "--style", choices=("ipc", "learning"), default="ipc", help="IPC or IPC 2023 learning-track encoding"
    )
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
