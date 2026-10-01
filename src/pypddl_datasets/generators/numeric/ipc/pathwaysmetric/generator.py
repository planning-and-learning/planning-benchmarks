#!/usr/bin/env python3
# Port of pddl-generators pathways/main.c (Yannis Dimopoulos, Alfonso Gerevini and
# Alessandro Saetti, IPC 2006) in its numeric mode (`-N`, random need/produce
# constants, disjunctive goals), in the atemporal Pathways-Metric encoding of the
# IPC 2023 numeric tasks (Coles, Fox and Long 2013): reaction durations stay in the
# init, goal pairs become `(>= (+ (available a) (available b)) k)`. Reaction
# selection and goal molecules follow the same upstream sampler. The original
# Pathways-Reactions and Pathways-SimpleSubs data are shipped beside this module
# as reactions.txt and simple_substances.txt.

from __future__ import annotations

import argparse
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EMPTY = "_"
GOAL_P, GOAL_Q = 40, 20  # upstream INITIAL_PROB_P / INITIAL_PROB_Q (percent)


def _lines(path: Path) -> list[str]:
    """Upstream parsing: drop '%' comments and all spaces, skip empty lines."""
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("%", 1)[0].replace(" ", "").strip()
        if line:
            lines.append(line)
    return lines


def _load() -> tuple[list[str], list[str], list[tuple[str, str, str, str]]]:
    # Upstream prepends while reading, so arrays hold the files in reverse order;
    # the empty substance "_" is the last simple substance.
    simple = [*reversed(_lines(HERE / "simple_substances.txt")), EMPTY]
    simple_set = set(simple)
    reaction_lines = _lines(HERE / "reactions.txt")
    dashed: list[str] = []
    for line in reversed(reaction_lines):
        for token in re.split(r"[+=\[\]>]", line):
            if token and token not in simple_set and token not in dashed:
                dashed.append(token)
    dashed.reverse()
    reactions: list[tuple[str, str, str, str]] = []
    for line in reaction_lines:  # prepended twice: file order
        tokens = [t for t in re.split(r"[>\[\]+]", line) if t]
        if tokens[0] == EMPTY:  # "_ [ c ]> y": synthesis catalysed by c
            reactions.append(("synthesis", tokens[1], tokens[2], tokens[2]))
        elif "[" in line:  # "a [ c ]> b": catalysed association
            product = tokens[1] if tokens[2] == EMPTY else tokens[2]
            reactions.append(("catalyzed-association", tokens[0], tokens[1], product))
        elif "+" in line and line.index("+") < line.index(">"):  # "a + b > ab"
            reactions.append(("association", tokens[0], tokens[1], tokens[2]))
        else:
            raise ValueError(f"unsupported reaction {line!r}")  # no decompositions in the data
    return simple, dashed, reactions


SIMPLE, DASHED, REACTIONS = _load()


def _enabled(reaction: tuple[str, str, str, str], available: set[str]) -> bool:
    kind, s1, s2, _ = reaction
    return s1 in available and (kind == "synthesis" or s2 in available)


def _reach(available: set[str], applied: set[int], used: set[str]) -> list[str]:
    """One upstream "flip": apply every enabled, not yet applied reaction."""
    fired = [i for i, r in enumerate(REACTIONS) if i not in applied and _enabled(r, available)]
    new: list[str] = []
    for i in fired:
        applied.add(i)
        used.update(REACTIONS[i][1:])
        product = REACTIONS[i][3]
        if product not in available:
            available.add(product)
            new.append(product)
    return new


def _build(rng: random.Random, min_reactions: int, num_goals: int) -> tuple[set[int], set[str], list[str]]:
    # Incremental phase: add random simple substances until a fix point uses
    # at least min_reactions reactions.
    available: set[str] = set()
    applied: set[int] = set()
    used: set[str] = set()
    pool = list(SIMPLE)
    initial: list[str] = []
    changed = True
    while True:
        if not changed:
            if len(applied) >= min_reactions or not pool:
                break
            index = rng.randrange(len(pool))
            substance = pool[index]
            pool[index] = pool[-1]  # upstream swap-remove
            pool.pop()
            initial.append(substance)
            available.add(substance)
        changed = bool(_reach(available, applied, used))

    # Fix-point phase from the chosen substances, recording each flip's new molecules.
    available, applied, used = set(initial), set(), set()
    levels: list[list[str]] = []
    while True:
        new = _reach(available, applied, used)
        if not new:
            break
        levels.insert(0, new)  # levels[0] is the last flip
    return applied, used, _pick_goals(rng, levels, 2 * num_goals)


def _pick_goals(rng: random.Random, levels: list[list[str]], count: int) -> list[str]:
    """Upstream build_goals with disjunctive goals: pairs of molecules drawn from
    the last level (p = 40%), the second-to-last (q = 20%) or a random level;
    every odd draw mirrors the probability. Exhausted levels are removed."""
    goals: list[str] = []
    while len(goals) < count and any(levels):
        r = rng.randrange(100)
        if len(goals) % 2:
            r = 100 - r
        if r < GOAL_P:
            index = 0
        elif r < GOAL_P + GOAL_Q:
            index = 1 if len(levels) > 1 else 0
        else:
            index = max(rng.randrange(len(levels)) - 1, 0)
        while not levels[index]:
            if index == len(levels) - 1:
                break
            levels.pop(index)
        if not levels[index]:
            continue  # upstream retries the draw
        level = levels[index]
        pick = rng.randrange(len(level))
        goals.append(level[pick])
        level[pick] = level[-1]  # upstream swap-remove
        level.pop()
    return goals[: len(goals) // 2 * 2]


def _is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


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
        if not _is_int(value) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")
    rng = random.Random(seed)
    applied, used, goals = _build(rng, min_reactions, num_goals)
    if len(goals) < 2 * num_goals:
        raise ValueError(f"only {len(goals) // 2} goals are reachable; lower num_goals")

    simple_used = [s for s in SIMPLE if s in used and s != EMPTY]
    complex_used = [d for d in DASHED if d in used]
    objects = [f"\t{s} - simple" for s in simple_used] + [f"\t{d} - complex" for d in complex_used]
    init: list[str] = []
    for s in simple_used:
        init += [f"\t(possible {s})", f"\t(= (available {s}) 0)"]
    init += [f"\t(= (available {d}) 0)" for d in complex_used]
    durations: list[str] = []
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
            duration = 2 + (0.4 - _fnum(rng) / 5)
            durations.append(f"\t(= (duration-catalyzed-self-association-reaction {s1} {s3}) {duration:.1f})")
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
