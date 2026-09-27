#!/usr/bin/env python3
# Port of pddl-generators pathways/main.c (Yannis Dimopoulos, Alfonso Gerevini and
# Alessandro Saetti, IPC 2006) in its numeric mode (`-N`, random need/produce
# constants, disjunctive goals), in the atemporal Pathways-Metric encoding of the
# IPC 2023 numeric tasks (Coles, Fox and Long 2013): reaction durations stay in the
# init, goal pairs become `(>= (+ (available a) (available b)) k)`. Reaction
# selection and goal molecules come from the classical/ipc/pathways port.

from __future__ import annotations

import argparse
import random
import sys

from pypddl_datasets.generators.classical.ipc.pathways.generator import DASHED, EMPTY, REACTIONS, SIMPLE, _build


def _num(rng: random.Random) -> int:
    return rng.randrange(4) + 1  # upstream num_rand()


def _fnum(rng: random.Random) -> float:
    return 0.5 + 3.5 * rng.randrange(100) / 100  # upstream fnum_rand()


def make_problem(min_reactions: int, num_goals: int, seed: int | None = None) -> str:
    """Generate a Pathways-Metric task.

    The reaction network and goal molecule pairs are selected as in the
    propositional generator. Every needed and produced quantity is uniform in
    1..4; a catalysed association of a molecule with itself becomes a
    self-association needing the sum of both quantities. Goal ``i`` asks for at
    least ``k`` units of either of its two molecules, ``k`` the sum of two draws in
    1..4. Durations follow upstream's per-type formulas (one decimal).
    """
    for name, value in (("min_reactions", min_reactions), ("num_goals", num_goals)):
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")
    rng = random.Random(seed)
    applied, used, goals = _build(rng, min_reactions, num_goals)
    if len(goals) < 2 * num_goals:
        raise ValueError(f"only {len(goals) // 2} goals are reachable; lower num_goals")

    simple_used = [s for s in SIMPLE if s in used and s != EMPTY]
    complex_used = [d for d in DASHED if d in used]
    objects = [f"\t{s} - simple" for s in simple_used] + [f"\t{d} - complex" for d in complex_used]
    init = []
    for s in simple_used:
        init += [f"\t(possible {s})", f"\t(= (available {s}) 0)"]
    init += [f"\t(= (available {d}) 0)" for d in complex_used]
    durations = []
    for i in sorted(applied):
        kind, s1, s2, s3 = REACTIONS[i]
        if kind == "synthesis":
            init += [
                f"\t(synthesis-reaction {s1} {s3})",
                f"\t(= (need-for-synthesis {s1} {s3}) {_num(rng)})",
                f"\t(= (prod-by-synthesis {s1} {s3}) {_num(rng)})",
            ]
            durations.append(f"\t(= (duration-synthesis-reaction {s1} {s3}) {4 + (0.8 - _fnum(rng) / 2.5):.1f})")
        elif kind == "catalyzed-association" and s1 == s2:
            init += [
                f"\t(catalyzed-self-association-reaction {s1} {s3})",
                f"\t(= (need-for-catalyzed-self-association {s1} {s3}) {_num(rng) + _num(rng)})",
                f"\t(= (prod-by-catalyzed-self-association {s1} {s3}) {_num(rng)})",
            ]
            durations.append(f"\t(= (duration-catalyzed-self-association-reaction {s1} {s3}) {2 + (0.4 - _fnum(rng) / 5):.1f})")
        else:
            init += [
                f"\t({kind}-reaction {s1} {s2} {s3})",
                f"\t(= (need-for-{kind} {s1} {s2} {s3}) {_num(rng)})",
                f"\t(= (need-for-{kind} {s2} {s1} {s3}) {_num(rng)})",
                f"\t(= (prod-by-{kind} {s1} {s2} {s3}) {_num(rng)})",
            ]
            value = 2 + (0.4 - _fnum(rng) / 5) if kind == "catalyzed-association" else 1 + (0.2 - _fnum(rng) / 10)
            durations.append(f"\t(= (duration-{kind}-reaction {s1} {s2} {s3}) {value:.1f})")
    init += ["\t(= (num-subs) 0)", *durations]
    goal = [
        f"\t(>= (+ (available {goals[2 * g]}) (available {goals[2 * g + 1]})) {_num(rng) + _num(rng)})"
        for g in range(num_goals)
    ]
    nl = "\n"
    return (f"""(define (problem pathways-r{min_reactions}-g{num_goals})
(:domain pathways-metric)
(:objects
{nl.join(objects)})


(:init
{nl.join(init)})

(:goal
\t(and
{nl.join(goal)}))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Pathways-Metric PDDL problem.")
    parser.add_argument("-R", "--min-reactions", type=int, required=True, help="min number of reactions in the network")
    parser.add_argument("-G", "--num-goals", type=int, required=True)
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
