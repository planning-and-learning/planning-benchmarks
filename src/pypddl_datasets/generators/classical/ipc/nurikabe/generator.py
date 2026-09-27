#!/usr/bin/env python3
# Port of pddl-generators nurikabe/generate.py (Alvaro Torralba, Florian Pommerening), the
# `random` source used for the IPC 2018 tasks (`generate.py random -1 N N SEED pddl`), written
# in the IPC encoding (domain `nurikabe`, `n0` a domain constant). The IPC tasks were made
# under Python 2, so draws use Python 2's `randint`/`choice` and Python 2's iteration order
# of the two-element successor set; the seed in an IPC task name reproduces that task.

from __future__ import annotations

import argparse
import random
import sys
from collections import Counter
from itertools import product
from typing import TYPE_CHECKING, TypeVar

from typing_extensions import override

if TYPE_CHECKING:
    from _typeshed import SupportsLenAndGetItem

STOP_CHANCE = 0.01
BRANCH_CHANCE = 0.5
MAX_MAP_ATTEMPTS = 1000
_M64 = (1 << 64) - 1
_T = TypeVar("_T")


class _Py2Random(random.Random):
    """Python 2's randint/choice on top of the (unchanged) Mersenne Twister."""

    @override
    def randint(self, a: int, b: int) -> int:
        return a + int(self.random() * (b - a + 1))

    @override
    def choice(self, seq: SupportsLenAndGetItem[_T]) -> _T:
        return seq[int(self.random() * len(seq))]


def _py2_tuple_hash(t: tuple[int, int]) -> int:
    x, mult, n = 0x345678, 1000003, len(t)
    for item in t:
        n -= 1
        x = ((x ^ item) * mult) & _M64
        mult = (mult + 82520 + n + n) & _M64
    x = (x + 97531) & _M64
    return _M64 - 1 if x == _M64 else x


def _py2_set_order(items: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Iteration order of a small Python 2 set built by inserting items in order."""
    slots: dict[int, tuple[int, int]] = {}
    for item in items:
        if item in slots.values():
            continue
        h = _py2_tuple_hash(item)
        i, perturb = h & 7, h
        while i & 7 in slots:  # CPython 2 set_lookkey probing
            i = (i * 5 + perturb + 1) & _M64
            perturb >>= 5
        slots[i & 7] = item
    return [slots[k] for k in sorted(slots)]


def _adjacent(width: int, height: int, x: int, y: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    if x < width - 1:
        res.append((x + 1, y))
    if y < height - 1:
        res.append((x, y + 1))
    if x > 0:
        res.append((x - 1, y))
    if y > 0:
        res.append((x, y - 1))
    return res


def _is_number(cell: str) -> bool:
    return cell.isdigit()


def _reconstruct_islands(cmap: list[list[str]]) -> list[list[str]]:
    # pylint: disable=too-many-nested-blocks  # upstream's flood fill, kept as ported
    result = [list(row) for row in cmap]
    height, width = len(result), len(result[0])
    islands: list[tuple[tuple[int, int], list[tuple[int, int]]]] = []
    for y, row in enumerate(result):
        for x, cell in enumerate(row):
            if cell == " " or _is_number(cell):
                queue = [(x, y)]
                result[y][x] = "X"
                cells: list[tuple[int, int]] = []
                start = (x, y)
                while queue:
                    cx, cy = queue.pop()
                    cells.append((cx, cy))
                    for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                        if 0 <= ny < height and 0 <= nx < width:
                            if _is_number(result[ny][nx]):
                                start = (nx, ny)
                            if result[ny][nx] == " " or _is_number(result[ny][nx]):
                                queue.append((nx, ny))
                                result[ny][nx] = "X"
                islands.append((start, cells))
    for (sx, sy), cells in islands:
        for x, y in cells:
            result[y][x] = " "
        result[sy][sx] = str(len(cells))
    return result


def _random_map(rng: random.Random, width: int, height: int) -> list[list[str]]:
    # pylint: disable=too-many-nested-blocks  # upstream's walk, kept as ported
    cmap = [[" " for _ in range(width)] for _ in range(height)]
    ends = [(rng.randint(0, width - 1), rng.randint(0, height - 1))]
    cmap[ends[0][1]][ends[0][0]] = "#"
    next_ends: list[tuple[int, int]] = []
    while ends:
        for x, y in ends:
            if rng.random() < STOP_CHANCE:
                continue
            neighbors: list[tuple[int, int]] = []
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= ny < height and 0 <= nx < width and cmap[ny][nx] == " ":
                    for nnx, nny in [(nx + 1, ny), (nx - 1, ny), (nx, ny + 1), (nx, ny - 1)]:
                        if (nnx, nny) != (x, y) and 0 <= nny < height and 0 <= nnx < width and cmap[nny][nnx] == "#":
                            break
                    else:
                        neighbors.append((nx, ny))
            if neighbors:
                successors = [rng.choice(neighbors)]
                if rng.random() < BRANCH_CHANCE:
                    successors.append(rng.choice(neighbors))
                for nx, ny in _py2_set_order(successors):
                    cmap[ny][nx] = "#"
                    next_ends.append((nx, ny))
        ends = next_ends
        next_ends = []
    return _reconstruct_islands(cmap)


def _sources(cmap: list[list[str]]) -> list[tuple[int, int, int]]:
    return [(x, y, int(cell)) for y, row in enumerate(cmap) for x, cell in enumerate(row) if _is_number(cell)]


def make_problem(width: int, height: int | None = None, seed: int = 0) -> str:
    """Generate a Nurikabe task on a width x height grid (square by default).

    Walls grow from a random cell as a branching random walk that never touches
    itself; every remaining island gets its size written on one cell (the source).
    Maps are redrawn (upstream: up to 1000 times) until at most size/2 islands have
    size 1 and every island is smaller than max(width, height). The robot starts at
    pos-0-0; cells next to one source are `part-of` it, next to two `blocked`.
    """
    height = width if height is None else height
    checks: list[tuple[str, object]] = [("width", width), ("height", height), ("seed", seed)]
    for name, value in checks:
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"{name} must be an integer")
    if width < 2 or height < 2:
        raise ValueError("width and height must be at least 2")

    rng = _Py2Random(seed)
    size = max(width, height)
    for _ in range(MAX_MAP_ATTEMPTS):
        cmap = _random_map(rng, width, height)
        groups = Counter(n for _, _, n in _sources(cmap))
        if groups.get(1, 0) <= size / 2 and sorted(groups.items())[-1][0] < size:
            break
    else:
        raise ValueError(f"no reasonable {width}x{height} map within {MAX_MAP_ATTEMPTS} draws")
    s = _sources(cmap)

    available = list(product(range(width), range(height)))
    blocked: list[tuple[int, int]] = []
    part_of: list[tuple[int, int, int]] = []
    for i, (x, y, _) in enumerate(s):
        available.remove((x, y))
        adjacent = _adjacent(width, height, x, y)
        part_of += [(ax, ay, i) for ax, ay in adjacent]
        for p in adjacent:
            if p in available:
                available.remove(p)
            elif p not in blocked:
                blocked.append(p)
    part_of = [(x, y, i) for x, y, i in part_of if (x, y) not in blocked]

    def cell(x: int, y: int) -> str:
        return f"pos-{x}-{y}"

    max_number = max(n for _, _, n in s)
    connected: list[str] = []
    for x, y in product(range(width), range(height)):
        connected += [f"    (connected {cell(x, y)} {cell(ax, ay)})" for ax, ay in _adjacent(width, height, x, y)]
    init = [
        *(f"    (next n{n} n{n + 1})" for n in range(max_number)),
        *connected,
        "    (robot-pos pos-0-0)",
        "    (moving)",
        *(f"    (source {cell(x, y)} g{i})" for i, (x, y, _) in enumerate(s)),
        *(f"    (available {cell(x, y)})" for x, y in available),
        *(f"    (blocked {cell(x, y)})" for x, y in blocked),
        *(f"    (part-of {cell(x, y)} g{i})" for x, y, i in part_of),
        *(f"    (remaining-cells g{i} n{n})" for i, (_, _, n) in enumerate(s)),
    ]
    cells = " ".join(cell(x, y) for x, y in product(range(width), range(height)))
    numbers = " ".join(f"n{n}" for n in range(1, max_number + 1))
    groups_objects = " ".join(f"g{i}" for i in range(len(s)))
    goals = "\n".join(f"    (group-painted g{i})" for i in range(len(s)))
    return (f"""(define (problem random-{width}x{height}-{seed})
(:domain nurikabe)
(:objects
    {cells} - cell
    {numbers} - num
    {groups_objects} - group
)
(:init
{chr(10).join(init)}
)
(:goal
(and
{goals}
)
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC 2018 Nurikabe PDDL problem.")
    parser.add_argument("width", type=int)
    parser.add_argument("height", type=int, nargs="?")
    parser.add_argument("-s", "--seed", type=int, default=0)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.width, args.height, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
