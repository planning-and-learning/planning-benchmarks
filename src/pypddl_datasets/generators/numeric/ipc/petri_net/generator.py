#!/usr/bin/env python3
# Reconstructed from the IPC 2026 petri-net tasks (data/numeric/ipc2026/petri-net, anonymous
# author); no generator was published. The tasks use three hand-made net templates; this
# generator reproduces them (chain lengths as parameters) and draws their goal variants.

from __future__ import annotations

import argparse
import random
import sys

NETS = ("mesh", "pipeline", "merge")  # prob06/08, prob07, prob09/10
DEFAULT_CHAIN = {"mesh": 3, "merge": 2}
GOALS = {"mesh": ("hubs", "sum"), "pipeline": ("drain",), "merge": ("sum", "empty")}
GOAL_TOKENS = {"mesh": (2, 3), "pipeline": (1, 3), "merge": (2, 5)}


def _mesh(chain: int):
    branches, hub = "abc", chain + 1
    petals, end = [hub + 1, hub + 2, hub + 3], hub + 4
    places = ["s0"] + [f"{b}{i}" for b in branches for i in range(1, end + 1)] + ["g"]
    facts = ["(source s0)", ""] + [f"(one-to-one s0 {b}1)" for b in branches] + [""]
    for b in branches:
        facts += [f"(one-to-one {b}{i} {b}{i + 1})" for i in range(1, hub)] + [""]
        facts += [f"(one-to-one {b}{hub} {b}{p})" for p in petals] + [""]
        facts += [f"(one-to-two {b}{p} {b}{q} {b}{hub})" for p, q in zip(petals, petals[1:] + petals[:1])]
        facts += [f"(three-to-one {b}{petals[0]} {b}{petals[1]} {b}{petals[2]} {b}{end})", ""]
    facts += [f"(three-to-one a{petals[2]} b{petals[2]} c{petals[2]} g)", f"(three-to-one a{end} b{end} c{end} g)"]
    return places, facts, branches, hub, petals[2]


def _pipeline():
    branches = "pq"
    places = ["s0"] + [f"{b}{i}" for b in branches for i in range(1, 9)] + ["g"]
    facts = ["(source s0)"] + [f"(sink {b}2)" for b in branches] + [f"(one-to-one s0 {b}1)" for b in branches]
    for b in branches:
        facts += [
            f"(one-to-one {b}1 {b}2)", f"(one-to-one {b}1 {b}3)", f"(one-to-one {b}1 {b}4)",
            f"(one-to-two {b}1 {b}2 {b}4)", f"(one-to-two {b}1 {b}2 {b}3)",
            f"(two-to-one {b}1 {b}4 {b}5)", f"(two-to-one {b}1 {b}3 {b}5)",
            f"(one-to-one {b}5 {b}6)", f"(one-to-one {b}5 {b}7)", f"(one-to-one {b}6 {b}8)",
            f"(one-to-two {b}8 {b}8 {b}8)", "",
        ]
    facts.append("(two-to-one p8 q8 g)")
    return places, facts, branches


def _merge(chain: int):
    branches, last = "abc", chain + 1
    places = ["s0"] + [f"{b}{i}" for b in branches for i in range(1, last + 1)] + ["d1", "d2", "g"]
    facts = ["(source s0)", ""] + [f"(one-to-one s0 {b}1)" for b in branches]
    for i in range(1, last):
        facts += [f"(one-to-one {b}{i} {b}{i + 1})" for b in branches]
    facts += [f"(one-to-one {b}{last} d1)" for b in branches]
    facts += [f"(three-to-one a{last} b{last} c{last} d2)", "(two-to-one d1 d2 g)"]
    return places, facts, branches, last


def make_problem(
    net: str = "mesh",
    chain_length: int | None = None,
    goal: str | None = None,
    goal_tokens: int | None = None,
    seed: int | None = None,
    name: str = "prob",
) -> str:
    """Generate a petri-net task on one of the three IPC net templates.

    ``chain_length`` is the length of each branch's leading chain (IPC: mesh 3, merge 2;
    the pipeline net has none). ``goal`` picks the goal variant (mesh: ``hubs``/``sum``,
    pipeline: ``drain``, merge: ``sum``/``empty``), drawn uniformly if omitted, and
    ``goal_tokens`` the tokens required in ``g`` (drawn from the IPC range if omitted).
    """
    if net not in NETS:
        raise ValueError(f"net must be one of {', '.join(NETS)}")
    if goal is not None and goal not in GOALS[net]:
        raise ValueError(f"goal must be one of {', '.join(GOALS[net])} for net {net}")
    if chain_length is not None:
        if net == "pipeline":
            raise ValueError("chain_length does not apply to the pipeline net")
        if not isinstance(chain_length, int) or isinstance(chain_length, bool) or chain_length < 1:
            raise ValueError("chain_length must be an integer at least 1")
    if goal_tokens is not None and (not isinstance(goal_tokens, int) or isinstance(goal_tokens, bool) or goal_tokens < 1):
        raise ValueError("goal_tokens must be an integer at least 1")

    rng = random.Random(seed)
    goal = goal or rng.choice(GOALS[net])
    tokens = goal_tokens or rng.randint(*GOAL_TOKENS[net])
    goals = [f"(= {tokens} (value g))"]
    if net == "mesh":
        places, facts, branches, hub, outer = _mesh(chain_length or DEFAULT_CHAIN[net])
        if goal == "hubs":
            h = rng.randint(1, 2)
            goals += [f"(= (value {b}{hub}) {h})" for b in branches]
        else:
            goals.append(f"(<= {rng.randint(1, 3)} (+ (+ (value a{outer}) (value b{outer})) (value c{outer})))")
    elif net == "pipeline":
        places, facts, branches = _pipeline()
        h = rng.randint(1, 2)
        goals += [f"(= {h} (value {b}5))" for b in branches]
        goals += [f"(= (value {b}{i}) 0)" for b in branches for i in (2, 3, 4)]
    else:
        places, facts, branches, last = _merge(chain_length or DEFAULT_CHAIN[net])
        if goal == "sum":
            goals.append(f"(= 1 (+ (+ (value a{last}) (value b{last})) (value c{last})))")
        else:
            goals += [f"(= (value {b}{last}) 0)" for b in branches]
    facts += [""] + [f"(= (value {p}) 0)" for p in places] + ["(= (cost) 0)"]
    nl = "\n"
    return (f""";;anonymous
(define (problem {name})
  (:domain petri-net)
  (:objects
    {' '.join(places)} - place
  )

  (:init
{nl.join(f"    {f}" if f else "" for f in facts)}
  )

  (:goal (and
{nl.join(f"         {g}" for g in goals)}
         )
  )

  (:metric minimize (cost))
 )
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a petri-net PDDL problem.")
    parser.add_argument("-n", "--net", choices=NETS, default="mesh")
    parser.add_argument("-l", "--chain-length", type=int)
    parser.add_argument("-g", "--goal")
    parser.add_argument("-t", "--goal-tokens", type=int)
    parser.add_argument("-s", "--seed", type=int)
    parser.add_argument("--name", default="prob")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
