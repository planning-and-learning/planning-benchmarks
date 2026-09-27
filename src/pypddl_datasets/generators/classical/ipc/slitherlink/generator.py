#!/usr/bin/env python3
# Port of ipc2023-classical/domain-slitherlink: the puzzle generator generate.hs
# (ctbo/slitherlink by Harald Bögeholz, BSD-2-Clause, notice below) and the PDDL
# writer generator-solver/generate-pddl.py `gen rows cols` (public domain), as used
# for the IPC 2023 grid tasks. The Haskell uniqueness solver is replaced by a
# pure-Python propagation + backtracking solver.
#
# Copyright (c) 2012, Harald Bögeholz (bo@ct.de)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.

from __future__ import annotations

import argparse
import random
import sys
from typing import cast

Cell = tuple[int, int]
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # right, down, left, up
# ponytail: search budget per uniqueness check; a clue whose removal cannot be proven
# safe within it is kept (upstream's Haskell solver always decides). Raise it for
# sparser puzzles at the cost of generation time.
MAX_SOLVER_NODES = 20000


def _grow_inside(rows: int, cols: int, rng: random.Random) -> set[Cell]:
    """generate.hs initialInside + addSquare: a random tree-like region."""
    def in_grid(cell: Cell) -> bool:
        return 0 <= cell[0] < rows and 0 <= cell[1] < cols

    start = (rng.randrange(rows), rng.randrange(cols))
    inside = {start}
    seeds = {((start[0] + d[0], start[1] + d[1]), d) for d in DIRECTIONS}
    seeds = {s for s in seeds if in_grid(s[0])}
    while seeds:
        (i, d) = sorted(seeds)[rng.randrange(len(seeds))]
        seeds.discard((i, d))
        left, right = (-d[1], d[0]), (d[1], -d[0])
        forward6 = [(i[0] + a[0] + b[0], i[1] + a[1] + b[1]) for b in ((0, 0), d) for a in ((0, 0), left, right)]
        if inside.isdisjoint(forward6):
            inside.add(i)
            seeds |= {s for s in (((i[0] + e[0], i[1] + e[1]), e) for e in (d, left, right)) if in_grid(s[0])}
    return inside


class _Grid:
    """Edges of a rows x cols Slitherlink grid, for solution counting."""

    def __init__(self, rows: int, cols: int):
        self.rows, self.cols = rows, cols
        self.edge_nodes: list[tuple[int, int]] = []
        index: dict[tuple[str, int, int], int] = {}

        def node(r: int, c: int) -> int:
            return r * (cols + 1) + c

        for r in range(rows + 1):
            for c in range(cols):
                index["h", r, c] = len(self.edge_nodes)
                self.edge_nodes.append((node(r, c), node(r, c + 1)))
        for r in range(rows):
            for c in range(cols + 1):
                index["v", r, c] = len(self.edge_nodes)
                self.edge_nodes.append((node(r, c), node(r + 1, c)))
        self.cell_edges = {
            (r, c): (index["h", r, c], index["h", r + 1, c], index["v", r, c], index["v", r, c + 1])
            for r in range(rows) for c in range(cols)
        }
        self.node_edges: list[list[int]] = [[] for _ in range((rows + 1) * (cols + 1))]
        for e, (a, b) in enumerate(self.edge_nodes):
            self.node_edges[a].append(e)
            self.node_edges[b].append(e)
        self.edge_cells: list[list[Cell]] = [[] for _ in self.edge_nodes]
        for cell, edges in self.cell_edges.items():
            for e in edges:
                self.edge_cells[e].append(cell)

    def count_solutions(self, clues: dict[Cell, int], limit: int = 2, max_nodes: int | None = None) -> int:
        """Solutions, counted up to ``limit``; returns ``limit`` once ``max_nodes`` search nodes are spent."""
        n_edges = len(self.edge_nodes)
        clue_cells = {e: [c for c in self.edge_cells[e] if c in clues] for e in range(n_edges)}

        def propagate(state: list[int], queue: list[int]) -> bool:
            while queue:
                e = queue.pop()
                for node in self.edge_nodes[e]:
                    edges = self.node_edges[node]
                    on = sum(state[x] == 1 for x in edges)
                    unknown = [x for x in edges if state[x] < 0]
                    if on > 2 or (on == 1 and not unknown):
                        return False
                    single = len(unknown) == 1
                    value = 0 if on == 2 or (on == 0 and single) else 1 if on == 1 and single else None
                    if value is not None:
                        for x in unknown:
                            state[x] = value
                            queue.append(x)
                for cell in clue_cells[e]:
                    edges = self.cell_edges[cell]
                    on = sum(state[x] == 1 for x in edges)
                    unknown = [x for x in edges if state[x] < 0]
                    if on > clues[cell] or on + len(unknown) < clues[cell]:
                        return False
                    value = 0 if on == clues[cell] else 1 if on + len(unknown) == clues[cell] else None
                    if value is not None and unknown:
                        for x in unknown:
                            state[x] = value
                            queue.append(x)
            return True

        def components(state: list[int]) -> tuple[list[int], dict[int, int]]:
            parent = list(range(len(self.node_edges)))

            def find(x: int) -> int:
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for e, (a, b) in enumerate(self.edge_nodes):
                if state[e] == 1:
                    parent[find(a)] = find(b)
            roots = [find(x) for x in range(len(parent))]
            sizes: dict[int, int] = {}
            for e, (a, _) in enumerate(self.edge_nodes):
                if state[e] == 1:
                    sizes[roots[a]] = sizes.get(roots[a], 0) + 1
            return roots, sizes

        def closed_is_solution(state: list[int]) -> bool:
            final = [1 if s == 1 else 0 for s in state]
            return all(sum(final[x] for x in self.cell_edges[c]) == v for c, v in clues.items())

        nodes = 0

        def search(state: list[int], queue: list[int]) -> int:
            nonlocal nodes
            nodes += 1
            if max_nodes is not None and nodes > max_nodes:
                return limit
            if not propagate(state, queue):
                return 0
            roots, sizes = components(state)
            on_total = sum(sizes.values())
            degree = [sum(state[x] == 1 for x in edges) for edges in self.node_edges]
            # a component without open ends is a closed loop
            open_roots = {roots[v] for v, d in enumerate(degree) if d == 1}
            closed = [r for r in sizes if r not in open_roots]
            if closed:
                if len(sizes) > 1:
                    return 0
                return int(closed_is_solution(state))
            # loop rule: an unknown edge joining both ends of one path closes it early
            for e, (a, b) in enumerate(self.edge_nodes):
                if state[e] < 0 and degree[a] == 1 and degree[b] == 1 and roots[a] == roots[b]:
                    trial = list(state)
                    trial[e] = 1
                    if sizes[roots[a]] + 1 == on_total + 1 and closed_is_solution(trial):
                        continue
                    state[e] = 0
                    return search(state, [e])
            unknown = [e for e in range(n_edges) if state[e] < 0]
            if not unknown:
                return 0  # no loop at all (empty, or open paths)
            ends = [e for e in unknown if degree[self.edge_nodes[e][0]] == 1 or degree[self.edge_nodes[e][1]] == 1]
            e = (ends or unknown)[0]
            count = 0
            for value in (1, 0):
                child = list(state)
                child[e] = value
                count += search(child, [e])
                if count >= limit:
                    break
            return count

        state = [-1] * n_edges
        # clues of 0 and full propagation from every clue cell
        return search(state, list(range(n_edges)))


def make_puzzle(rows: int, cols: int, seed: int | None = None) -> dict[Cell, int]:
    """generate.hs: clues of a random region, thinned while the solution stays unique."""
    rng = random.Random(seed)
    grid = _Grid(rows, cols)
    for _ in range(100):  # upstream keeps an ambiguous fully clued puzzle (tiny grids); we redraw
        inside = _grow_inside(rows, cols, rng)
        clues = {
            (r, c): sum(((r, c) in inside) != ((r + dr, c + dc) in inside) for dr, dc in DIRECTIONS)
            for r in range(rows) for c in range(cols)
        }
        if grid.count_solutions(clues) == 1:
            break
    else:
        raise ValueError(f"no uniquely solvable region on a {rows}x{cols} grid")
    order = list(clues)
    rng.shuffle(order)
    for cell in order:
        trial = dict(clues)
        del trial[cell]
        if grid.count_solutions(trial, max_nodes=MAX_SOLVER_NODES) == 1:
            clues = trial
    return clues


def make_problem(rows: int, cols: int, seed: int | None = None) -> str:
    """Generate a Slitherlink task on a rows x cols grid with a unique solution."""
    for name, value in (("rows", rows), ("cols", cols)):
        checked = cast(object, value)  # runtime check: callers may pass any type
        if not isinstance(checked, int) or isinstance(checked, bool) or checked < 1:
            raise ValueError(f"{name} must be an integer at least 1")
    if rows * cols < 2:
        raise ValueError("rows * cols must be at least 2")
    rng = random.Random(seed)
    return to_pddl(rows, cols, make_puzzle(rows, cols, rng.randrange(2**32)), f"slitherlink-{rows}x{cols}-{seed}")


def to_pddl(rows: int, cols: int, clues: dict[Cell, int], name: str) -> str:
    """generate-pddl.py's encoding of one puzzle (no start edge, as in `gen`)."""
    nodes = [f"n-{r}-{c}" for r in range(rows + 1) for c in range(cols + 1)]
    cells = [f"cell-{r}-{c}" for r in range(rows) for c in range(cols)]
    outside: list[str] = []
    for r in range(rows):
        outside += [f"cell-outside-{r}-left", f"cell-outside-{r}-right"]
    for c in range(cols):
        outside += [f"cell-outside-{c}-up", f"cell-outside-{c}-down"]

    cell_edges: list[str] = []
    for r in range(1, rows):
        for c in range(cols):
            cell_edges.append(f"(cell-edge cell-{r - 1}-{c} cell-{r}-{c} n-{r}-{c} n-{r}-{c + 1})")
    for c in range(cols):
        cell_edges.append(f"(cell-edge cell-outside-{c}-up cell-0-{c} n-0-{c} n-0-{c + 1})")
        cell_edges.append(f"(cell-edge cell-{rows - 1}-{c} cell-outside-{c}-down n-{rows}-{c} n-{rows}-{c + 1})")
    for c in range(1, cols):
        for r in range(rows):
            cell_edges.append(f"(cell-edge cell-{r}-{c - 1} cell-{r}-{c} n-{r}-{c} n-{r + 1}-{c})")
    for r in range(rows):
        cell_edges.append(f"(cell-edge cell-outside-{r}-left cell-{r}-0 n-{r}-0 n-{r + 1}-0)")
        cell_edges.append(f"(cell-edge cell-{r}-{cols - 1} cell-outside-{r}-right n-{r}-{cols} n-{r + 1}-{cols})")

    capacity = [f"(cell-capacity {cell} cap-1)" for cell in outside]
    capacity += [f"(cell-capacity cell-{r}-{c} cap-{clues.get((r, c), 4)})" for r in range(rows) for c in range(cols)]
    goal_caps = [f"(cell-capacity cell-{r}-{c} cap-0)" for r in range(rows) for c in range(cols) if (r, c) in clues]
    puzzle = [";;  " + "".join(str(clues[r, c]) if (r, c) in clues else "." for c in range(cols)) for r in range(rows)]

    nl = "\n    "
    return (f"""{chr(10).join(puzzle)}

(define (problem {name})
(:domain slitherlink)

(:objects
    cap-0 cap-1 cap-2 cap-3 cap-4 - cell-capacity-level
    {' '.join(nodes)} - node
    {' '.join(cells + outside)} - cell
)

(:init
    {nl.join(f"(cell-capacity-inc cap-{i} cap-{i + 1})" for i in range(4))}

    {nl.join(capacity)}

    {nl.join(f"(node-degree0 {n})" for n in nodes)}

    {nl.join(cell_edges)}
)
(:goal
    (and
        {(nl + '    ').join(sorted(f"(not (node-degree1 {n}))" for n in nodes))}

        {(nl + '    ').join(goal_caps)}
    )
)
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an IPC 2023 Slitherlink PDDL problem.")
    parser.add_argument("rows", type=int)
    parser.add_argument("cols", type=int)
    parser.add_argument("-s", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.rows, args.cols, seed=args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
