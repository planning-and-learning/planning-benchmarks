#!/usr/bin/env python3
# Reconstruction of the IPC 2026 numeric 2048 tasks (no generator was published). The
# game has no random tile spawns: every reference task is a 4x4 board whose tiles sum
# to T, with the goal "single tile T at p11" reachable in exactly the number of moves
# recorded in its solution comment. We build such boards backwards from the goal.

from __future__ import annotations

import argparse
import random
import sys

SIZE = 4
DIRECTIONS = {"u": "up", "d": "down", "l": "left", "r": "right"}
ROW_STATUS = ("top", "midtop", "midbot", "bot")
COL_STATUS = ("left", "midleft", "midright", "right")
ATTEMPTS_PER_NODE = 30
MAX_NODES = 20_000
MAX_RESTARTS = 20

Board = tuple[tuple[int, ...], ...]


def _line_cells(direction: str, k: int) -> list[tuple[int, int]]:
    """Cells of line k in order i1..i4 (i1 closest to the target edge)."""
    if direction == "l":
        return [(k, c) for c in range(SIZE)]
    if direction == "r":
        return [(k, c) for c in reversed(range(SIZE))]
    if direction == "u":
        return [(r, k) for r in range(SIZE)]
    return [(r, k) for r in reversed(range(SIZE))]


def _slide(line: list[int]) -> list[int]:
    tiles, out, j = [v for v in line if v], [], 0
    while j < len(tiles):
        if j + 1 < len(tiles) and tiles[j] == tiles[j + 1]:
            out.append(2 * tiles[j])
            j += 2
        else:
            out.append(tiles[j])
            j += 1
    return out + [0] * (SIZE - len(out))


def move(board: Board, direction: str) -> Board:
    """The domain's move: shift toward the edge, merge equal pairs from the edge once, shift."""
    cells = [list(row) for row in board]
    for k in range(SIZE):
        line = _line_cells(direction, k)
        for (r, c), v in zip(line, _slide([board[r][c] for r, c in line])):
            cells[r][c] = v
    return tuple(tuple(row) for row in cells)


OPPOSITE = {"u": "d", "d": "u", "l": "r", "r": "l"}


def _unmove(rng: random.Random, board: Board, direction: str, previous: str | None, num_splits: int) -> Board | None:
    """A random board that ``direction`` turns into ``board``, or None.

    Unless ``previous`` is None (the initial board), the pre-image must itself be the
    result of a ``previous`` move, i.e. packed toward that edge: tiles form a prefix
    (same edge) or suffix (opposite edge) of each line, or nested occupied index sets
    along ``previous`` (perpendicular edge).
    """
    lines = [_line_cells(direction, k) for k in range(SIZE)]
    pres = []
    for line in lines:
        values = [board[r][c] for r, c in line]
        tiles = [v for v in values if v]
        if values[: len(tiles)] != tiles:
            return None  # not packed toward the edge: no pre-image for this direction
        pres.append(tiles)
    splittable = [(k, i) for k, pre in enumerate(pres) for i, v in enumerate(pre) if v >= 4]
    chosen = set(rng.sample(splittable, min(num_splits, len(splittable))))  # undo these merges
    for k in range(SIZE):
        pres[k] = [x for i, v in enumerate(pres[k]) for x in ([v // 2] * 2 if (k, i) in chosen else [v])]
        if len(pres[k]) > SIZE:
            return None
    slots: list[list[int]] = [[] for _ in range(SIZE)]
    if previous is None:
        slots = [sorted(rng.sample(range(SIZE), len(pre))) for pre in pres]
    elif previous == direction:
        slots = [list(range(len(pre))) for pre in pres]
    elif previous == OPPOSITE[direction]:
        slots = [list(range(SIZE - len(pre), SIZE)) for pre in pres]
    else:
        order = range(SIZE) if previous in "ul" else reversed(range(SIZE))
        allowed = list(range(SIZE))
        for k in order:
            if len(pres[k]) > len(allowed):
                return None
            slots[k] = allowed = sorted(rng.sample(allowed, len(pres[k])))
    cells = [list(row) for row in board]
    for line, pre, slot in zip(lines, pres, slots):
        new = [0] * SIZE
        for i, v in zip(slot, pre):
            new[i] = v
        for (r, c), v in zip(line, new):
            cells[r][c] = v
    before = tuple(tuple(row) for row in cells)
    return before if before != board and move(before, direction) == board else None


def _scramble(rng: random.Random, target: int, num_moves: int, num_tiles: int):
    """Depth-first search for ``num_moves`` inverse moves from the goal board that undo
    ``num_tiles - 1`` merges in total, backtracking out of boards no move can produce."""
    budget = [MAX_NODES]

    def search(board: Board, direction: str, steps_left: int):
        tiles = sum(v > 0 for row in board for v in row)
        remaining = max(0, num_tiles - tiles)
        for _ in range(ATTEMPTS_PER_NODE):
            if budget[0] <= 0:
                return None
            budget[0] -= 1
            share = remaining / steps_left
            splits = int(share) + (rng.random() < share - int(share))
            previous = None if steps_left == 1 else rng.choice("udlr")
            before = _unmove(rng, board, direction, previous, splits)
            if before is None:
                continue
            if steps_left == 1:
                return before, [direction]
            rest = search(before, previous, steps_left - 1)
            if rest is not None:
                return rest[0], rest[1] + [direction]
        return None

    goal: Board = tuple(tuple(target if (r, c) == (0, 0) else 0 for c in range(SIZE)) for r in range(SIZE))
    return search(goal, rng.choice("ul"), num_moves)  # the last move packs the target into p11


def make_problem(target: int, num_moves: int, num_tiles: int | None = None, seed: int | None = None) -> str:
    """Generate a 2048 task: reach a single ``target`` tile at p11 in ``num_moves`` moves.

    Starting from the goal board, ``num_moves`` random inverse moves are applied: a
    direction is drawn, some tiles of at least 4 split into two halves (undoing
    merges, spread so that the initial board has about ``num_tiles`` tiles; default
    uniform in 9..16 as in the reference tasks), and each line's tiles are spread over
    its cells in order, packed toward the edge of the move before (free for the
    initial board). An inverse move is kept only if the forward move reproduces
    the board, so the recorded moves always solve the task.
    """
    if not isinstance(target, int) or isinstance(target, bool) or target < 4 or target & (target - 1):
        raise ValueError("target must be a power of two of at least 4")
    if not isinstance(num_moves, int) or isinstance(num_moves, bool) or num_moves < 1:
        raise ValueError("num_moves must be an integer at least 1")
    rng = random.Random(seed)
    if num_tiles is None:
        num_tiles = rng.randint(9, 16)
    if not isinstance(num_tiles, int) or isinstance(num_tiles, bool) or not 1 <= num_tiles <= SIZE * SIZE:
        raise ValueError("num_tiles must be an integer in 1..16")
    for _ in range(MAX_RESTARTS):
        result = _scramble(rng, target, num_moves, num_tiles)
        if result is not None:
            break
        num_tiles = max(1, num_tiles - 1)  # ponytail: dense boards dead-end often; settle for one tile fewer
    else:
        raise ValueError(f"no scramble of {num_moves} moves found in {MAX_RESTARTS} restarts")
    board, moves = result

    def picture(b: Board) -> str:
        return "\n".join(f"    ;   {' | '.join(str(v) for v in row)}" for row in b)

    pos = [[f"p{r + 1}{c + 1}" for c in range(SIZE)] for r in range(SIZE)]
    init = []
    for d, statuses, name in (("l", ROW_STATUS, "L"), ("r", ROW_STATUS, "R"), ("u", COL_STATUS, "U"), ("d", COL_STATUS, "D")):
        for k, status in enumerate(statuses):
            init.append("        " + " ".join(
                f"(pos-at {name} {status} i{i + 1} {pos[r][c]})" for i, (r, c) in enumerate(_line_cells(d, k))
            ))
    for name, statuses in (("L", ROW_STATUS), ("R", ROW_STATUS), ("U", COL_STATUS), ("D", COL_STATUS)):
        chain = list(statuses) + ["done"]
        init.append("        " + " ".join(f"(next {name} {a} {b})" for a, b in zip(chain, chain[1:])))
    init += [f"        (start-status {name} {s})" for name, s in (("L", "top"), ("R", "top"), ("U", "left"), ("D", "left"))]
    init.append("        (next-idx i1 i2) (next-idx i2 i3) (next-idx i3 i4)")
    init.append("        (free-to-play)")
    init += ["        " + " ".join(f"(= (value {pos[r][c]}) {board[r][c]})" for c in range(SIZE)) for r in range(SIZE)]
    goal = "\n".join(
        "        " + " ".join(f"(= (value {pos[r][c]}) {target if (r, c) == (0, 0) else 0})" for c in range(SIZE))
        for r in range(SIZE)
    )
    goal_board = tuple(tuple(target if (r, c) == (0, 0) else 0 for c in range(SIZE)) for r in range(SIZE))
    return (f"""; solution sequence: {' '.join(DIRECTIONS[m] for m in moves)}
(define (problem game-2048-t{target}-n{num_moves})
    (:domain twenty-forty-eight)

    ; initial board (0 = empty):
    ;
{picture(board)}

    ; goal:
    ;
{picture(goal_board)}

    (:init
{chr(10).join(init)}
    )

    (:goal (and
{goal}
    ))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a numeric 2048 PDDL problem.")
    parser.add_argument("-t", "--target", type=int, required=True, help="goal tile at p11 (power of two)")
    parser.add_argument("-n", "--num-moves", type=int, required=True, help="length of the known solution")
    parser.add_argument("-k", "--num-tiles", type=int, help="tiles on the initial board (default: uniform in 9..16)")
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.target, args.num_moves, args.num_tiles, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
