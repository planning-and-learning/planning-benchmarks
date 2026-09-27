#!/usr/bin/env python3
"""Port of ipc2023-classical/domain-ricochet-robots generate.py + asp-to-pddl.py
(Daniel Fišer, IPC 2023). Upstream's Rust solver filter is replaced by an exact
breadth-first search over robot configurations (``max_states`` bounds it, like
upstream's solver time limit)."""

from __future__ import annotations

import argparse
import random
import sys
from collections import deque
from collections.abc import Collection, Sequence
from typing import cast

ROBOTS = ("red", "blue", "green", "yellow")
MOVES = {"north": (0, -1), "south": (0, 1), "east": (1, 0), "west": (-1, 0)}
OPPOSITE = {"north": "south", "south": "north", "east": "west", "west": "east"}
MAX_TRIES = 1000
BOARDS = ("random", "asp2015")
# The single 16x16 board of all ASP competition 2015 instances (27 of the 40 IPC
# 2023 tasks); robots start in the corners there (red, blue, green, yellow).
ASP_2015_BARRIERS = (
    (1, 6, "south"), (1, 12, "south"), (2, 1, "east"), (2, 2, "south"), (2, 3, "east"), (2, 10, "south"),
    (2, 11, "east"), (3, 7, "east"), (3, 15, "east"), (3, 15, "south"), (4, 2, "east"), (4, 7, "south"),
    (4, 10, "east"), (4, 16, "east"), (5, 1, "south"), (5, 10, "south"), (6, 14, "east"), (7, 4, "east"),
    (7, 4, "south"), (7, 8, "east"), (7, 9, "east"), (7, 13, "south"), (8, 7, "south"), (8, 10, "north"),
    (8, 11, "east"), (9, 7, "south"), (9, 10, "north"), (9, 10, "south"), (10, 1, "east"), (10, 8, "west"),
    (10, 9, "west"), (10, 14, "south"), (10, 15, "east"), (11, 3, "east"), (11, 7, "south"), (11, 8, "east"),
    (11, 12, "east"), (11, 12, "south"), (12, 3, "south"), (12, 16, "east"), (13, 11, "east"), (14, 2, "east"),
    (14, 7, "east"), (14, 7, "south"), (14, 10, "south"), (14, 13, "east"), (15, 1, "south"), (15, 13, "south"),
    (16, 4, "south"), (16, 9, "south"),
)
ASP_2015_ROBOTS = ((1, 1), (1, 16), (16, 1), (16, 16))


def _barriers(rng: random.Random, size: int, num_barriers: int) -> list[tuple[int, int, str]]:
    barriers: list[tuple[int, int, str]] = []
    seen: set[tuple[int, int, str]] = set()
    while len(barriers) < num_barriers:
        x, y = rng.randint(1, size), rng.randint(1, size)
        direction = rng.choice(["north", "south", "east", "west"])
        dx, dy = MOVES[direction]
        if not (1 <= x + dx <= size and 1 <= y + dy <= size):
            continue
        other = (x + dx, y + dy, OPPOSITE[direction])
        if (x, y, direction) not in seen and other not in seen:
            seen.add((x, y, direction))
            barriers.append((x, y, direction))
    return barriers


def optimal_moves(  # pylint: disable=unused-argument  # size: kept for callers; the border is in `blocked`
    size: int,
    blocked: Collection[tuple[int, int, str]],
    robots: Sequence[tuple[int, int]],
    target_robot: int,
    target: tuple[int, int],
    max_states: int,
) -> int | None:
    """Fewest robot moves to bring ``target_robot`` to ``target``; -1 if
    impossible, None if more than ``max_states`` configurations are needed."""
    start: tuple[tuple[int, int], ...] = tuple(robots)
    if start[target_robot] == target:
        return 0
    seen = {start}
    queue = deque([(start, 0)])
    while queue:
        state, depth = queue.popleft()
        occupied = set(state)
        for i, (x0, y0) in enumerate(state):
            for direction, (dx, dy) in MOVES.items():
                x, y = x0, y0
                while (x, y, direction) not in blocked and (x + dx, y + dy) not in occupied:
                    x, y = x + dx, y + dy
                nxt = state[:i] + ((x, y),) + state[i + 1 :]
                if nxt in seen:
                    continue
                if i == target_robot and (x, y) == target:
                    return depth + 1
                seen.add(nxt)
                if len(seen) > max_states:
                    return None
                queue.append((nxt, depth + 1))
    return -1


def make_problem(
    board_size: int,
    num_barriers: int | None = None,
    seed: int | None = None,
    max_states: int = 1_000_000,
    board: str = "random",
) -> str:
    """Generate a Ricochet Robots task on a square board.

    Barriers: ``num_barriers`` (default uniform in 5..5 + size²/3, as
    upstream) random walls between neighbouring cells, each blocking both
    sides. Four robots on distinct uniform cells; the goal puts one uniform
    robot on a uniform cell. ``board="asp2015"`` instead uses the fixed
    16x16 board of the ASP competition 2015 instances with the robots in the
    corners. As upstream, only tasks that need at least one move and are
    provably solvable are kept (else redrawn).
    """
    if board not in BOARDS:
        raise ValueError(f"board must be one of {', '.join(BOARDS)}")
    if board == "asp2015" and (board_size != 16 or num_barriers is not None):
        raise ValueError("board='asp2015' is a fixed 16x16 board: use board_size=16 and no num_barriers")
    # four robots need at least one free cell to move
    for name, value, minimum in (("board_size", board_size, 3), ("max_states", max_states, 1)):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    barriers = cast(object, num_barriers)  # runtime check: callers may pass any type
    if barriers is not None and (not isinstance(barriers, int) or isinstance(barriers, bool) or barriers < 0):
        raise ValueError("num_barriers must be a non-negative integer")
    max_barriers = 2 * board_size * (board_size - 1)  # interior walls
    if num_barriers is not None and num_barriers > max_barriers:
        raise ValueError(f"num_barriers must be at most {max_barriers} on a {board_size}x{board_size} board")

    rng = random.Random(seed)
    n = board_size
    border = [(x, 1, "north") for x in range(1, n + 1)] + [(x, n, "south") for x in range(1, n + 1)]
    border += [(1, y, "west") for y in range(1, n + 1)] + [(n, y, "east") for y in range(1, n + 1)]
    for _ in range(MAX_TRIES):
        # ponytail: capped at the interior wall count; upstream loops forever on tiny boards
        if board == "asp2015":
            barriers, robots = list(ASP_2015_BARRIERS), list(ASP_2015_ROBOTS)
        else:
            count = num_barriers if num_barriers is not None else min(rng.randint(5, 5 + n * n // 3), max_barriers)
            barriers, robots = _barriers(rng, n, count), []
        while len(robots) < len(ROBOTS):
            cell = (rng.randint(1, n), rng.randint(1, n))
            if cell not in robots:
                robots.append(cell)
        target_robot = rng.randrange(len(ROBOTS))
        target = (rng.randint(1, n), rng.randint(1, n))
        blocked = list(border)
        for x, y, direction in barriers:
            dx, dy = MOVES[direction]
            blocked += [(x, y, direction), (x + dx, y + dy, OPPOSITE[direction])]
        cost = optimal_moves(n, set(blocked), robots, target_robot, target, max_states)
        if cost is not None and cost > 0:
            break
    else:
        raise ValueError(f"no solvable task found in {MAX_TRIES} draws; raise max_states or change the board")

    cells = [f"cell-{x}-{y}" for x in range(1, n + 1) for y in range(1, n + 1)]
    nxt = [f"(next cell-{x}-{y} cell-{x}-{y + 1} south)" for x in range(1, n + 1) for y in range(1, n)]
    nxt += [f"(next cell-{x}-{y} cell-{x}-{y - 1} north)" for x in range(1, n + 1) for y in range(n, 1, -1)]
    nxt += [f"(next cell-{x}-{y} cell-{x + 1}-{y} east)" for y in range(1, n + 1) for x in range(1, n)]
    nxt += [f"(next cell-{x}-{y} cell-{x - 1}-{y} west)" for y in range(1, n + 1) for x in range(n, 1, -1)]
    free = [f"(free cell-{x}-{y})" for x in range(1, n + 1) for y in range(1, n + 1) if (x, y) not in robots]
    at = sorted(f"(at robot-{i + 1} cell-{x}-{y})" for i, (x, y) in enumerate(robots))
    init = [*nxt, "", *(f"(blocked cell-{x}-{y} {d})" for x, y, d in blocked), "", *free, "", *at, ""]
    init += ["(nothing-is-moving)", "", "(= (total-cost) 0)", "(= (go-cost) 1)"]
    init += ["(= (step-cost) 0)", "(= (stop-cost) 0)"]
    rand = int(1000000 * rng.random())
    return (f"""(define (problem ricochet-robots-{n}x{n}-{cost}-{rand})
(:domain ricochet-robots)

(:objects
    {' '.join(cells)} - cell
    {' '.join(f"robot-{i + 1}" for i in range(len(ROBOTS)))} - robot
    west east north south - direction
)

(:init
{chr(10).join(f"    {fact}" if fact else "" for fact in init)}
)
(:goal
    (and
        (at robot-{target_robot + 1} cell-{target[0]}-{target[1]})
        (nothing-is-moving)
    )
)
(:metric minimize (total-cost))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Ricochet Robots PDDL problem (IPC 2023).")
    parser.add_argument("board_size", type=int)
    parser.add_argument("-b", "--num-barriers", type=int, help="default: uniform in 5..5 + size^2/3")
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--board", choices=BOARDS, default="random", help="asp2015: the fixed ASP competition board")
    parser.add_argument("--max-states", type=int, default=1_000_000, help="search bound of the solvability check")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
