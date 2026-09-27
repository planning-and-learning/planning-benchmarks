#!/usr/bin/env python3
# Port of pddl-generators cavediving/generator/generator.py (ADL, ordered tanks), IPC 2014.
#
# Copyright (c) Year 2013, Nathan Robinson <nathan.m.robinson@gmail.com>
#                          Christian Muise <christian.muise@gmail.com>
#                          Charles Gretton <charles.gretto@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from __future__ import annotations

import argparse
import itertools
import random
import sys


def make_problem(
    cave_branches: list[int],
    objectives: list[int],
    neg_link_prob: float = 0.5,
    perturb_hiring_costs: float = 0.0,
    min_hiring_cost: int = 10,
    max_hiring_cost: int = 100,
    other_action_cost: int = 1,
    seed: int | None = None,
    name: str | None = None,
) -> str:
    """Generate a Cave Diving (ADL) task.

    ``cave_branches`` are the depths of the cave's branches (the first starts
    at the entrance, the others branch off a random shallower node);
    ``objectives`` the depths of the photographed leaves. There are exactly
    the required 2^(d+1) - 1 tanks per objective at depth d (ordered, plus
    ``dummy``) and 2^(d-1) divers; each diver pair outside the helper chain
    precludes each other with ``neg_link_prob``. Hiring costs fall with the
    number of precludes, perturbed by ``perturb_hiring_costs``.
    """
    branches: list[object] = [*cave_branches]  # runtime guard: callers may pass non-ints
    if not branches or any(not isinstance(b, int) or b < 1 for b in branches):
        raise ValueError("cave_branches must be positive integers")
    goal_depths: list[object] = [*objectives]
    if not goal_depths or any(not isinstance(o, int) or o < 1 for o in goal_depths):
        raise ValueError("objectives must be positive integers")
    if cave_branches[0] < max(cave_branches):
        raise ValueError("cave_branches must start with the deepest branch")
    if not 0.0 <= neg_link_prob <= 1.0:
        raise ValueError("neg_link_prob must be in [0, 1]")
    if not 0.0 <= perturb_hiring_costs <= 1.0:
        raise ValueError("perturb_hiring_costs must be in [0, 1]")
    if not 0 <= min_hiring_cost <= max_hiring_cost:
        raise ValueError("min_hiring_cost must be in [0, max_hiring_cost]")

    rng = random.Random(seed)
    # caves: a random tree with the given branch depths
    edges = [(x, x + 1) for x in range(cave_branches[0])]
    depths = list(range(cave_branches[0] + 1))
    leaves = [len(depths) - 1]
    for branch in cave_branches[1:]:
        junction = rng.choice([x for x in range(len(depths)) if depths[x] < branch])
        first = len(depths)
        edges.append((junction, first))
        for step in range(branch - depths[junction]):
            if step:
                edges.append((first + step - 1, first + step))
            depths.append(depths[junction] + 1 + step)
        leaves.append(len(depths) - 1)

    goals: list[int] = []
    for depth in objectives:
        candidates = [n for n in leaves if depths[n] == depth and n not in goals]
        if not candidates:
            raise ValueError(f"objectives: not enough leaves at depth {depth}")
        goals.append(rng.choice(candidates))

    tanks = [f"t{x}" for x in range(sum(2 ** (depths[o] + 1) for o in goals) - 1)] + ["dummy"]
    num_divers = sum(2 ** (depths[o] - 1) for o in goals)

    # helper chain: divers that must bring tanks to the diver behind them
    positive: set[tuple[int, int]] = set()
    current = 0
    for obj in goals:
        chain = [current]
        current += 1
        for _ in range(depths[obj] - 1):
            new = list(range(current, current + len(chain)))
            positive.update((n, d) for d in chain for n in new)
            chain.extend(new)
            current += len(new)

    precludes: dict[int, list[int]] = {d: [] for d in range(num_divers)}
    for d1, d2 in itertools.combinations(range(num_divers), 2):
        if (d1, d2) not in positive and rng.random() < neg_link_prob:
            precludes[d1].append(d2)

    costs = _hiring_costs(rng, precludes, min_hiring_cost, max_hiring_cost, perturb_hiring_costs)
    divers = [f"d{x}" for x in range(num_divers)]
    rng.shuffle(divers)  # upstream: the relations are written through a shuffled name list

    def chunks(names: list[str], kind: str) -> list[str]:
        return [f"    {' '.join(names[i:i + 20])} - {kind}" for i in range(0, len(names), 20)]

    ordered = [f"d{x}" for x in range(num_divers)]
    init = [f"    (available {d})" for d in ordered] + [f"    (capacity {d} four)" for d in ordered]
    init.append(f"    (in-storage {tanks[0]})")
    init += [f"    (next-tank {a} {b})" for a, b in zip(tanks, tanks[1:])]
    init.append("    (cave-entrance l0)")
    for a, b in edges:
        init += [f"    (connected l{a} l{b})", f"    (connected l{b} l{a})"]
    init += [f"    (next-quantity {a} {b})" for a, b in itertools.pairwise(("zero", "one", "two", "three", "four"))]
    init += [f"    (precludes {divers[d1]} {divers[d2]})" for d1 in range(num_divers) for d2 in precludes[d1]]
    init += [f"    (= (hiring-cost {divers[d]}) {costs[d]})" for d in range(num_divers)]
    init += [f"    (= (other-cost ) {other_action_cost})", "    (= (total-cost) 0)"]
    goal = [f"      (have-photo l{o})" for o in goals] + [f"      (decompressing {d})" for d in divers]

    name = name or f"b{'-'.join(map(str, cave_branches))}-o{'-'.join(map(str, objectives))}-s{seed}"
    return (f"""(define (problem cave-diving-adl-{name})
  (:domain cave-diving-adl)
  (:objects
    {' '.join(f'l{x}' for x in range(len(depths)))} - location
{chr(10).join(chunks(ordered, 'diver'))}
{chr(10).join(chunks(tanks, 'tank'))}
    zero one two three four - quantity
  )

  (:init
{chr(10).join(init)}
  )

  (:goal
    (and
{chr(10).join(goal)}
    )
  )

  (:metric minimize (total-cost))
)
""").lower()


def _hiring_costs(
    rng: random.Random, precludes: dict[int, list[int]], low: int, high: int, perturb: float
) -> dict[int, int]:
    """Upstream make_hiring_costs: fewer precludes, higher cost."""
    counts = {d: len(v) for d, v in precludes.items()}
    if high == low:
        return {d: low for d in counts}
    if len(set(counts.values())) == 1:
        return {d: int(low + (high - low) / 2.0) for d in counts}
    groups: dict[int, list[int]] = {}
    for d, n in counts.items():
        groups.setdefault(n, []).append(d)
    costs: dict[int, int] = {}
    step = (high - low) / float(len(groups))
    for rank, n in enumerate(sorted(groups, reverse=True)):
        for d in groups[n]:
            base = low + step * rank
            base += rng.random() * 2 * perturb * base - perturb * base
            costs[d] = max(low, min(high, int(base)))
    return costs


def _depths(text: str) -> list[int]:
    return [int(x) for x in text.split(":")]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Cave Diving (ADL) PDDL problem.")
    parser.add_argument(
        "-b", "--cave-branches", type=_depths, default=[3], help="branch depths, e.g. 3:2:2 (default: 3)"
    )
    parser.add_argument("-o", "--objectives", type=_depths, default=[3], help="objective depths, e.g. 2:2 (default: 3)")
    parser.add_argument("--neg-link-prob", type=float, default=0.5)
    parser.add_argument("--perturb-hiring-costs", type=float, default=0.0)
    parser.add_argument("--min-hiring-cost", type=int, default=10)
    parser.add_argument("--max-hiring-cost", type=int, default=100)
    parser.add_argument("--other-action-cost", type=int, default=1)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--name")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
