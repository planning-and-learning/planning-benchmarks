#!/usr/bin/env python3
# Port of autoscale/pddl-generators/snake/generate.py (empty boards, percentage
# spawn apples, as called by Autoscale 21.11).

from __future__ import annotations

import argparse
import random
import sys
from itertools import product
from typing import cast

Position = tuple[int, int]


def _pos(position: Position) -> str:
    return f"pos{position[0]}-{position[1]}"


def _adjacent_pairs(width: int, height: int) -> list[tuple[Position, Position]]:
    pairs: list[tuple[Position, Position]] = []
    for x in range(width):
        for y in range(height):
            if x < width - 1:
                pairs.append(((x, y), (x + 1, y)))
            if y < height - 1:
                pairs.append(((x, y), (x, y + 1)))
            if x > 0:
                pairs.append(((x, y), (x - 1, y)))
            if y > 0:
                pairs.append(((x, y), (x, y - 1)))
    return pairs


def make_problem(
    width: int,
    height: int,
    spawn_percentage: int,
    num_initial_apples: int = 5,
    snake_size: int = 1,
    seed: int | None = None,
) -> str:
    """Generate a Snake task on an empty ``width`` x ``height`` board.

    The snake has ``snake_size + 1`` cells. The number of spawning apples is
    ``spawn_percentage`` percent of the board minus the snake and the initial
    apples, with upstream's corrections for tiny boards and odd cell counts.
    """
    for name, value, minimum in (
        ("width", width, 1),
        ("height", height, 1),
        ("spawn_percentage", spawn_percentage, 1),
        ("num_initial_apples", num_initial_apples, 1),
        ("snake_size", snake_size, 1),
    ):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    if spawn_percentage > 100:
        raise ValueError("spawn_percentage must be at most 100")

    rng = random.Random(seed)
    board = [["_"] * height for _ in range(width)]
    num_cells = width * height

    requested_spawn = int(num_cells * spawn_percentage / 100.0) - 1 - snake_size - num_initial_apples
    num_apples = num_initial_apples
    num_spawn = requested_spawn
    if num_spawn < 1:  # at least one apple spawns
        num_apples += num_spawn - 1
        num_spawn = 1
    num_apples = max(num_apples, 1)
    if num_cells % 2 == 1 and num_spawn == requested_spawn:
        num_spawn -= 1
    if num_cells - snake_size - num_apples - num_spawn <= 0:
        raise ValueError(f"board {width}x{height} is too small for the snake and apples")

    def clear_positions() -> list[Position]:
        positions = [(x, y) for x, y in product(range(width), range(height)) if board[x][y] == "_"]
        rng.shuffle(positions)
        return positions

    def grow(x: int, y: int, remaining: int, snake: list[Position]) -> bool:
        if not (0 <= x < width and 0 <= y < height and board[x][y] == "_"):
            return False
        board[x][y] = "S"
        if remaining == 0:
            snake.append((x, y))
            return True
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        rng.shuffle(neighbors)
        for nx, ny in neighbors:
            if grow(nx, ny, remaining - 1, snake):
                snake.append((x, y))
                return True
        board[x][y] = "_"
        return False

    snake: list[Position] = []
    for x, y in clear_positions():
        if grow(x, y, snake_size, snake):
            board[x][y] = "H"
            break
    snake.reverse()  # head first
    if len(snake) != snake_size + 1:
        raise ValueError(f"no snake of size {snake_size} fits on the board")

    def place_apples(count: int, mark: str) -> list[Position]:
        apples = clear_positions()[:count]
        for x, y in apples:
            board[x][y] = mark
        return apples

    apples = place_apples(num_apples, "A")
    spawn = place_apples(num_spawn, "B")

    init = [f"    (isAdjacent {_pos(a)} {_pos(b)})" for a, b in _adjacent_pairs(width, height)]
    init.append(f"    (tailSnake {_pos(snake[-1])})")
    init.append(f"    (headSnake {_pos(snake[0])})")
    init.extend(f"    (nextSnake {_pos(a)} {_pos(b)})" for a, b in zip(snake, snake[1:]))
    init.extend(
        f"    (blocked {_pos((x, y))})"
        for x, y in product(range(width), range(height))
        if board[x][y] in "SH"
    )
    if spawn:
        init.append(f"    (spawn {_pos(spawn[0])})")
        init.append(f"    (nextSpawn {_pos(spawn[-1])} dummyPoint)")
        init.extend(f"    (nextSpawn {_pos(a)} {_pos(b)})" for a, b in zip(spawn, spawn[1:]))
    else:
        init.append("    (spawn dummyPoint)")
    init.extend(f"    (isPoint {_pos(apple)})" for apple in apples)
    goals = [f"      (not (isPoint {_pos(apple)}))" for apple in apples + spawn]

    positions = " ".join(_pos(p) for p in product(range(width), range(height)))
    name = f"snake-empty-{width}x{height}-{snake_size}-{num_apples}-{num_spawn}{'' if seed is None else f'-{seed}'}"
    return (f"""(define (problem {name})
  (:domain snake)
  (:objects
    {positions}
  )
  (:init
{chr(10).join(init)}
  )
  (:goal
    (and
{chr(10).join(goals)}
    )
  )
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Snake PDDL problem on an empty board.")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int)
    parser.add_argument("spawn_percentage", type=int, help="percentage of the board used by spawning apples")
    parser.add_argument("--num-initial-apples", type=int, default=5)
    parser.add_argument("--snake-size", type=int, default=1)
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
