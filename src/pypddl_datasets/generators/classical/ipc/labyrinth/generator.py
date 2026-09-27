#!/usr/bin/env python3
# Port of ipc2023-classical/domain-labyrinth instance_generator/{generator,labyrinth,to_pddl}.py
# (Rebecca Eifler, Daniel Fišer; public domain). Random draws happen in upstream's order,
# so a seed reproduces the IPC 2023 task of that seed exactly.

from __future__ import annotations

import argparse
import random
import sys
from collections import deque

DIRECTIONS = ("N", "E", "S", "W")
OPPOSITE = {"N": "S", "S": "N", "E": "W", "W": "E"}
STEP = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
MAX_SHIFT_ATTEMPTS = 100_000


def _neighbours(grid, paths, size, x, y):
    """Upstream get_reachable_positions: order W, E, N, S; both cards must be open."""
    out = []
    for d in ("W", "E", "N", "S"):
        nx, ny = x + STEP[d][0], y + STEP[d][1]
        if 0 <= nx < size and 0 <= ny < size and paths[grid[x][y]][d] and paths[grid[nx][ny]][OPPOSITE[d]]:
            out.append((d, (nx, ny)))
    return out


def _exit_reachable(grid, paths, size):
    seen, queue = {(0, 0)}, deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) == (size - 1, size - 1):
            return True
        for _, pos in _neighbours(grid, paths, size, x, y):
            if pos not in seen:
                seen.add(pos)
                queue.append(pos)
    return False


def _shift(grid, size, index, direction):
    """Upstream Board.rotate: push column (N/S) or row (E/W) ``index`` by one, wrapping around."""
    if direction in ("N", "S"):
        column = grid[index]
        grid[index] = column[1:] + column[:1] if direction == "N" else column[-1:] + column[:-1]
    else:
        row = [grid[x][index] for x in range(size)]
        row = row[1:] + row[:1] if direction == "W" else row[-1:] + row[:-1]
        for x in range(size):
            grid[x][index] = row[x]


def make_problem(size: int, num_rotations: int, seed: int = 0) -> str:
    """Generate a Labyrinth task on a ``size`` x ``size`` board.

    A random self-avoiding walk from the top-left to the bottom-right card is
    carved into an all-walls board, every card then loses walls at random until
    it has at most two, and ``num_rotations`` random row/column pushes (inner
    rows and columns only) are applied, each accepted only if the exit is then
    unreachable without pushing. The robot starts on card0 in the top-left
    corner and must leave through the bottom of the bottom-right card.
    """
    for name, value, minimum in (("size", size, 3), ("num_rotations", num_rotations, 0), ("seed", seed, 0)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    rng = random.Random(seed)

    # Random walk on the open board (upstream generate_random_labyrinth).
    open_paths = {c: dict.fromkeys(DIRECTIONS, True) for c in range(size * size)}
    grid = [[x + y * size for y in range(size)] for x in range(size)]
    pos, trace, sequence, tries = (0, 0), [], [(0, 0)], 0
    while pos != (size - 1, size - 1):
        tries += 1
        if tries >= 10000:
            raise ValueError("walk exceeded 10000 tries")
        options = _neighbours(grid, open_paths, size, *pos)
        direction, nxt = options[rng.randint(0, len(options) - 1)]
        if trace and trace[-1] == OPPOSITE[direction]:
            continue
        if nxt in sequence:
            index = sequence.index(nxt)
            sequence, trace = sequence[: index + 1], trace[:index]
        else:
            sequence.append(nxt)
            trace.append(direction)
        pos = nxt

    paths = {c: dict.fromkeys(DIRECTIONS, False) for c in range(size * size)}
    paths[grid[size - 1][size - 1]]["S"] = True
    for i, direction in enumerate(trace):
        (x, y), (nx, ny) = sequence[i], sequence[i + 1]
        paths[grid[x][y]][direction] = True
        paths[grid[nx][ny]][OPPOSITE[direction]] = True
    for x in range(size):
        for y in range(size):
            card = paths[grid[x][y]]
            order = list(DIRECTIONS)
            rng.shuffle(order)
            while True:
                for direction in order:
                    if rng.randint(0, 3) == 0:
                        card[direction] = True
                if sum(not v for v in card.values()) <= 2:
                    break

    # Pushes that make the exit unreachable without pushing (upstream mix_up_labyrinth).
    if num_rotations:
        accepted, previous, attempts = 0, None, 0
        while accepted < num_rotations:
            attempts += 1
            if attempts > MAX_SHIFT_ATTEMPTS:  # ponytail: upstream loops forever here; never hit at IPC sizes
                raise ValueError(f"no {num_rotations} disconnecting pushes found for size {size}")
            direction = DIRECTIONS[rng.randint(0, 3)]
            index = rng.randint(1, size - 2)
            if previous == (OPPOSITE[direction], index):
                continue
            trial = [column[:] for column in grid]
            _shift(trial, size, index, direction)
            if not _exit_reachable(trial, paths, size):
                grid, previous, accepted = trial, (direction, index), accepted + 1

    lines = [f";; Generated with seed: {seed}, size: {size}, num-rotations: {num_rotations}",
             f"(define (problem labyrinth-size-{size}-rotations-{num_rotations}-seed-{seed})", "(:domain labyrinth)",
             "(:objects", "\t" + " ".join(f"pos{i}" for i in range(size)) + "  - gridpos",
             "\t" + " ".join(f"card{i}" for i in range(size * size)) + "  - card", ")", "(:init",
             f"\t(max-pos pos{size - 1})", "\t(min-pos pos0)", ""]
    lines += [f"\t(next pos{i + 1} pos{i})" for i in range(size - 1)] + [""]
    lines += [f"\t(card-at card{grid[x][y]} pos{x} pos{y})" for y in range(size) for x in range(size)] + [""]
    for y in range(size):
        for x in range(size):
            lines += [f"\t(blocked card{grid[x][y]} {d})" for d in DIRECTIONS if not paths[grid[x][y]][d]] + [""]
    lines += ["", "\t(robot-at card0)", "", "\t(= (total-cost) 0)", "\t(= (move-robot-cost) 1)", "\t(= (move-card) 1)", ")",
              "(:goal", "\t(and", "\t\t(left)", "\t)", ")", "\t(:metric minimize (total-cost))", ")", ""]
    return ("\n".join(lines)).lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Labyrinth PDDL problem (IPC 2023).")
    parser.add_argument("--size", type=int, required=True, help="board side length")
    parser.add_argument("--num-rotations", type=int, required=True, help="disconnecting row/column pushes")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.size, args.num_rotations, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
