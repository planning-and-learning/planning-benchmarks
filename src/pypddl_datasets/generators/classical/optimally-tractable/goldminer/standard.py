#!/usr/bin/env python3
"""Gold Miner as in the IPC 2023 learning track, which is optimally tractable as a whole.

The robot (row r) and the laser and bomb supply (row s) are in the free first column,
the gold (row g) is in the last column C - 1, and every other cell is rock. The
laser clears any rock but destroys gold, the bomb clears soft rock (the gold cell
is soft) and is used up, and the arm holds one item. So the robot fetches the
laser, walks the free column to row g, lasers and walks along row g up to column
C - 3, lasers column C - 2, drops the laser, fetches a bomb, walks back, bombs the
gold cell, steps in and picks the gold: |r - s| + 3 |s - g| + 4C - 4. If row g is
soft rock all the way, bombing it cell by cell (one supply trip per bomb) is the
alternative; it only wins on three columns.
"""

from __future__ import annotations

import argparse
import re
import sys

from pypddl_datasets.generators.classical.ipc.goldminer import generator as _ipc


def make_problem(num_rows: int, num_cols: int, seed: int | None = None) -> str:
    if num_rows < 2 or num_cols < 3:
        raise ValueError("num_rows must be at least 2 and num_cols at least 3")
    problem = _ipc.make_problem(num_rows, num_cols, seed)
    assert problem is not None

    def row(predicate: str) -> int:
        return int(re.findall(rf"\({predicate} f(\d+)-\d+f\)", problem)[0])

    robot, supply, gold = row("robot-at"), row("laser-at"), row("gold-at")
    walk, c = abs(supply - gold), num_cols
    cost = abs(robot - supply) + 3 * walk + 4 * c - 4
    if all(f"(soft-rock-at f{gold}-{col}f)" in problem for col in range(1, c - 1)):
        # bomb j (j = 1..c-1) clears column j: pick, walk walk + j - 1, detonate; walk back for all but the last
        bombs = sum(walk + j + 1 for j in range(1, c)) + sum(walk + j - 1 for j in range(1, c - 1)) + 2
        cost = min(cost, abs(robot - supply) + bombs)
    return f"; optimal plan cost: {cost}\n{problem}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Gold Miner task.")
    parser.add_argument("num_rows", type=int)
    parser.add_argument("num_cols", type=int)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        print(make_problem(args.num_rows, args.num_cols, args.seed), end="")
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    sys.exit(main())
