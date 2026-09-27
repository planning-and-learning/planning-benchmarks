#!/usr/bin/env python3
# Port of pddl-generators pathways/main.c (Yannis Dimopoulos, Alfonso Gerevini and
# Alessandro Saetti, IPC 2006), Propositional track as run for IPC 5:
# `pathways --seed <s> -R <reactions> -G <goals> -L <substances>`, which always
# uses disjunctive goal pairs. reactions.txt / simple_substances.txt are the
# upstream Pathways-Reactions / Pathways-SimpleSubs data files. The domain is per
# task: goal molecules become constants and each goal is a dummy action with a
# disjunctive precondition, as in data/classical/downward-benchmarks/pathways.

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
import random

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
SIMPLE_SET = set(SIMPLE)


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


def make_task(
    min_reactions: int, num_goals: int, num_substances: int, seed: int | None = None, strips_wrapper: bool = False
) -> tuple[str, str]:
    """Generate a Pathways task; returns ``(domain, problem)``.

    Random simple substances are added until the relaxed reachable reactions
    number at least ``min_reactions``; those reactions form the network. Goal
    ``i`` asks for one of two molecules drawn from late reachability levels.
    At most ``num_substances`` substances may be chosen as initial ones.
    Upstream warns that the generator may produce unsolvable tasks.

    ``strips_wrapper`` gives the encoding of pddl-generators ``pathways/wrapper.py``
    (the Autoscale 21.11 optimal tasks): every molecule is a domain constant, each
    disjunctive goal action becomes two single-precondition STRIPS actions, and
    ``num_goals`` goal predicates are declared even when fewer goals are reachable.
    """
    checks: list[tuple[str, object]] = [
        ("min_reactions", min_reactions), ("num_goals", num_goals), ("num_substances", num_substances),
    ]
    for name, value in checks:
        if not isinstance(value, int) or isinstance(value, bool) or value < 1:
            raise ValueError(f"{name} must be an integer at least 1")
    applied, used, goals = _build(random.Random(seed), min_reactions, num_goals)
    if strips_wrapper:
        return _wrapper_task(applied, used, goals, num_goals, num_substances)
    if len(goals) < 2 * num_goals:
        raise ValueError(f"only {len(goals) // 2} goals are reachable; lower num_goals")
    order = {m: i for i, m in enumerate(SIMPLE + DASHED)}
    constants = sorted(set(goals), key=order.__getitem__)
    simple_used = [s for s in SIMPLE if s in used and s != EMPTY]
    objects = [f"\t{s} - simple" for s in simple_used if s not in constants]
    objects += [f"\t{d} - complex" for d in DASHED if d in used and d not in constants]
    objects += [f"\tl{i} - level" for i in range(num_substances + 1)]
    init = [f"\t(possible {s})" for s in simple_used]
    for i in sorted(applied):
        kind, s1, s2, s3 = REACTIONS[i]
        init.append(
            f"\t(synthesis-reaction {s1} {s3})" if kind == "synthesis" else f"\t({kind}-reaction {s1} {s2} {s3})"
        )
    init.append("\t(num-subs l0)")
    init += [f"\t(next l{i + 1} l{i})" for i in range(num_substances)]

    def typed(names: list[str], kind: str) -> str:
        return f"{' '.join(names)} - {kind}" if names else ""

    typed_constants = " ".join(
        part
        for part in (
            typed([c for c in constants if c in SIMPLE_SET], "simple"),
            typed([c for c in constants if c not in SIMPLE_SET], "complex"),
        )
        if part
    )
    goal_predicates = "\n".join(f"\t     (goal{g + 1})" for g in range(num_goals))
    dummies = "\n".join(
        f"""
(:action dummy-action-{g + 1}
 :parameters ()
 :precondition
\t(or (available {goals[2 * g]})
\t    (available {goals[2 * g + 1]}))
 :effect (and (goal{g + 1})))"""
        for g in range(num_goals)
    )
    domain = f"""; IPC5 Domain: Pathways Propositional
; Authors: Yannis Dimopoulos, Alfonso Gerevini and Alessandro Saetti

(define (domain pathways-propositional)
(:requirements :strips :disjunctive-preconditions :negative-preconditions :typing)

(:types level molecule - object
\tsimple complex - molecule)

(:constants {typed_constants})

(:predicates
\t     (association-reaction ?x1 ?x2 - molecule ?x3 - complex)
\t     (catalyzed-association-reaction ?x1 ?x2 - molecule ?x3 - complex)
\t     (synthesis-reaction ?x1 ?x2 - molecule)
\t     (possible ?x - molecule)
\t     (available ?x - molecule)
\t     (chosen ?s - simple)
\t     (next ?l1 ?l2 - level)
\t     (num-subs ?l - level)
{goal_predicates})


(:action choose
 :parameters (?x - simple ?l1 ?l2 - level)
 :precondition (and (possible ?x) (not (chosen ?x))
\t\t    (num-subs ?l2) (next ?l1 ?l2))
 :effect (and (chosen ?x) (not (num-subs ?l2)) (num-subs ?l1)))

(:action initialize
  :parameters (?x - simple)
  :precondition (and (chosen ?x))
  :effect (and (available ?x)))

(:action associate
 :parameters (?x1 ?x2 - molecule ?x3 - complex)
 :precondition (and (association-reaction ?x1  ?x2  ?x3)
\t\t    (available ?x1) (available ?x2))
 :effect (and  (not (available ?x1)) (not (available ?x2)) (available ?x3)))

(:action associate-with-catalyze
 :parameters (?x1 ?x2 - molecule ?x3 - complex)
 :precondition (and (catalyzed-association-reaction ?x1 ?x2 ?x3)
\t\t    (available ?x1) (available ?x2))
 :effect (and (not (available ?x1)) (available ?x3)))

(:action synthesize
 :parameters (?x1 ?x2 - molecule)
 :precondition (and (synthesis-reaction ?x1 ?x2) (available ?x1))
 :effect (and (available ?x2)))
{dummies}
)
"""
    nl = "\n"
    problem = f"""(define (problem pathways-r{min_reactions}-g{num_goals}-l{num_substances})
(:domain pathways-propositional)
(:objects
{nl.join(objects)})


(:init
{nl.join(init)})


(:goal
\t(and
{nl.join(f"{chr(9)}(goal{g + 1})" for g in range(num_goals))}))

)
"""
    return domain.lower(), problem.lower()


def _wrapper_task(
    applied: set[int], used: set[str], goals: list[str], num_goals: int, num_substances: int
) -> tuple[str, str]:
    """wrapper.py's rewrite of the IPC-style output (see make_task)."""
    if not goals:
        raise ValueError("no goal is reachable; raise min_reactions")
    simple_used = [s for s in SIMPLE if s in used and s != EMPTY]
    goal_set = set(goals)
    simple = [s for s in simple_used if s not in goal_set]
    complex_ = [d for d in DASHED if d in used and d not in goal_set]
    for molecule in goals:  # wrapper.py appends goal molecules missing from the problem objects
        target = simple if molecule in SIMPLE_SET else complex_
        if molecule not in target:
            target.append(molecule)
    init = [f"\t(possible {s})" for s in simple_used]
    for i in sorted(applied):
        kind, s1, s2, s3 = REACTIONS[i]
        init.append(
            f"\t(synthesis-reaction {s1} {s3})" if kind == "synthesis" else f"\t({kind}-reaction {s1} {s2} {s3})"
        )
    init.append("\t(num-subs l0)")
    init += [f"\t(next l{i + 1} l{i})" for i in range(num_substances)]
    goal_predicates = "\n".join(f"    (goal{g + 1})" for g in range(num_goals))
    dummies = "\n".join(
        f"""(:action dummy-strips-action-{i}
 :parameters ()
 :precondition (available {molecule})
 :effect (and (goal{i // 2 + 1})))
"""
        for i, molecule in enumerate(goals)
    )
    domain = f"""(define (domain pathways-propositional)
(:requirements :strips :negative-preconditions :typing)

(:types
    level molecule - object
    simple complex - molecule
)

(:constants
    {" ".join(simple)} - simple

    {" ".join(complex_)} - complex)

(:predicates
    (association-reaction ?x1 ?x2 - molecule ?x3 - complex)
    (catalyzed-association-reaction ?x1 ?x2 - molecule ?x3 - complex)
    (synthesis-reaction ?x1 ?x2 - molecule)
    (possible ?x - molecule)
    (available ?x - molecule)
    (chosen ?s - simple)
    (next ?l1 ?l2 - level)
    (num-subs ?l - level)
{goal_predicates}
)

(:action choose
 :parameters (?x - simple ?l1 ?l2 - level)
 :precondition (and (possible ?x) (not (chosen ?x))
                    (num-subs ?l2) (next ?l1 ?l2))
 :effect (and (chosen ?x) (not (num-subs ?l2)) (num-subs ?l1)))

(:action initialize
  :parameters (?x - simple)
  :precondition (and (chosen ?x))
  :effect (and (available ?x)))

(:action associate
 :parameters (?x1 ?x2 - molecule ?x3 - complex)
 :precondition (and (association-reaction ?x1  ?x2  ?x3)
                    (available ?x1) (available ?x2))
 :effect (and  (not (available ?x1)) (not (available ?x2)) (available ?x3)))

(:action associate-with-catalyze
 :parameters (?x1 ?x2 - molecule ?x3 - complex)
 :precondition (and (catalyzed-association-reaction ?x1 ?x2 ?x3)
                    (available ?x1) (available ?x2))
 :effect (and (not (available ?x1)) (available ?x3)))

(:action synthesize
 :parameters (?x1 ?x2 - molecule)
 :precondition (and (synthesis-reaction ?x1 ?x2) (available ?x1))
 :effect (and (available ?x2)))

{dummies}
)
"""
    nl = "\n"
    problem = f"""(define (problem pathways-problem)
(:domain pathways-propositional)
(:objects
{nl.join(f"{chr(9)}l{i} - level" for i in range(num_substances + 1))})


(:init
{nl.join(init)})


(:goal
\t(and
{nl.join(f"{chr(9)}(goal{g + 1})" for g in range(len(goals) // 2))}))

)
"""
    return domain.lower(), problem.lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Pathways (IPC 2006 Propositional) domain and problem.")
    parser.add_argument(
        "-R", "--min-reactions", type=int, required=True, help="minimum number of reactions (upstream -R)"
    )
    parser.add_argument("-G", "--num-goals", type=int, required=True, help="number of disjunctive goals (upstream -G)")
    parser.add_argument(
        "-L", "--num-substances", type=int, required=True, help="initial substances that may be chosen (upstream -L)"
    )
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--domain", default="domain.pddl", help="domain output file (default: domain.pddl)")
    parser.add_argument("--problem", default="problem.pddl", help="problem output file (default: problem.pddl)")
    parser.add_argument(
        "--strips-wrapper", action="store_true",
        help="encoding of pddl-generators pathways/wrapper.py (Autoscale optimal tasks)",
    )
    args = parser.parse_args(argv)
    try:
        domain, problem = make_task(
            args.min_reactions, args.num_goals, args.num_substances, args.seed, args.strips_wrapper
        )
    except ValueError as error:
        parser.error(str(error))
    Path(args.domain).write_text(domain, encoding="utf-8")
    Path(args.problem).write_text(problem, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
