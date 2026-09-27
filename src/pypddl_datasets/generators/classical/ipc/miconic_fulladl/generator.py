#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators miconic-fulladl/miconic.c (FF domain collection). Distributed
# under the original notice, not GPL-3.0-or-later (see LICENSES/LicenseRef-Freiburg.txt):
#
# (C) Copyright 2001 Albert Ludwigs University Freiburg
#     Institute of Computer Science
#
# All rights reserved. Use of this software is permitted for
# non-commercial research purposes, and it may be copied only
# for that use.  All copies must include this copyright message.
# This software is made available AS IS, and neither the authors
# nor the  Albert Ludwigs University Freiburg make any warranty
# about the software or its performance.
#
# Port of the AIPS-2000 Miconic-ADL generator, printed like the IPC tasks
# (passenger kinds as unary predicates, universally quantified goal).

from __future__ import annotations

import argparse
import random
import sys

MAX_ATTEMPTS = 1000


def make_problem(
    num_floors: int,
    num_passengers: int,
    seed: int | None = None,
    up_down: int = 20,
    vip: int = 5,
    going_nonstop: int = 5,
    attendant: int = 60,
    never_alone: int = 10,
    conflict_a: int = 20,
    conflict_b: int = 80,
    no_access: int = 50,
    no_access_floors: int = 5,
) -> str:
    """Generate a Miconic-ADL task; percentages as in miconic.c (IPC used the defaults).

    Passenger kinds are drawn as fixed-size random subsets (``int(p * pct / 100)``
    passengers each; attendants only with a never-alone passenger, at least one;
    conflict-B only with a conflict-A passenger, disjoint from it). Journeys and
    no-access floors follow upstream's solvability heuristics: no A and B with
    the same origin, conflict passengers away from vip floors, all up/down
    passengers in one direction, going-nonstop passengers share the first
    one's destination, never-alone and conflict passengers not at vip
    destinations, no-access never at a passenger's own floors, vip
    destinations or (for attendants) never-alone origins. The IPC tasks use
    ``num_floors = 2 * num_passengers``.
    """
    for name, value, minimum in (("num_floors", num_floors, 2), ("num_passengers", num_passengers, 1)):
        if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
            raise ValueError(f"{name} must be an integer at least {minimum}")
    percentages = dict(up_down=up_down, vip=vip, going_nonstop=going_nonstop, attendant=attendant, never_alone=never_alone,
                       conflict_a=conflict_a, conflict_b=conflict_b, no_access=no_access, no_access_floors=no_access_floors)
    for name, value in percentages.items():
        if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= 100:
            raise ValueError(f"{name} must be an integer percentage in [0, 100]")

    rng = random.Random(seed)
    p, f = num_passengers, num_floors

    def count(pct: int) -> int:
        return int(p * (pct / 100.0))

    def draw(n: int, excluded: set[int]) -> list[int]:
        if n > p - len(excluded):
            raise ValueError("percentages ask for more distinct passengers than exist")
        chosen: list[int] = []
        for _ in range(n):
            while (x := rng.randrange(p)) in excluded or x in chosen:
                pass
            chosen.append(x)
        return chosen

    ups = draw(count(up_down), set())
    vips = draw(count(vip), set())
    nonstops = draw(count(going_nonstop), set())
    alones = draw(count(never_alone), set())
    attendants = draw(max(1, count(attendant)), set(alones)) if alones else []
    group_a = draw(count(conflict_a), set())
    group_b = draw(count(conflict_b), set(group_a)) if group_a else []
    ups_s, vips_s, nonstops_s, alones_s, a_s, b_s = map(set, (ups, vips, nonstops, alones, group_a, group_b))

    def journeys() -> tuple[list[int], list[int]] | None:
        origin = [0] * p
        destin = [0] * p
        for i in range(p):
            for _ in range(MAX_ATTEMPTS):
                o = rng.randrange(f)
                if i in a_s and any(origin[j] == o and j in b_s for j in range(i)):
                    continue
                if i in b_s and any(origin[j] == o and j in a_s for j in range(i)):
                    continue
                if (i in a_s or i in b_s) and any((origin[j] == o or destin[j] == o) and j in vips_s for j in range(i)):
                    continue
                break
            else:
                return None
            origin[i] = o
            for _ in range(MAX_ATTEMPTS):
                d = rng.randrange(f)
                if d == o:
                    continue
                if i in ups_s and any(j in ups_s and ((origin[j] < destin[j] and o > d) or (origin[j] > destin[j] and o < d)) for j in range(i)):
                    continue
                if i in vips_s and any(origin[j] == d and j in alones_s for j in range(i)):
                    continue
                if i in vips_s and any(origin[j] == d and (j in a_s or j in b_s) for j in range(i)):
                    continue
                if i in nonstops_s:
                    first = next((j for j in range(i) if j in nonstops_s), None)
                    if first is not None:
                        d = destin[first]  # upstream copies without re-checking, even onto the origin
                break
            else:
                return None
            destin[i] = d

        return origin, destin

    # ponytail: upstream loops forever on a dead end (e.g. an up/down passenger on the top
    # floor when all must go up); such seeds never produced a task, so redraw the journeys.
    for _ in range(1000):
        if (drawn := journeys()) is not None:
            origin, destin = drawn
            break
    else:
        raise ValueError("no admissible journeys found; use more floors")

    no_access_facts = []
    for x in draw(count(no_access), set()):
        for floor in range(f):
            if rng.randrange(100) >= no_access_floors or floor in (origin[x], destin[x]):
                continue
            near_vip = any(k != x and k in vips_s and origin[x] in (origin[k], destin[k]) for k in range(p))
            if near_vip and any(k != x and k in vips_s and destin[k] == floor for k in range(p)):
                continue
            if x in attendants and any(k in alones_s and origin[k] == floor for k in range(p)):
                continue
            no_access_facts.append(f"(no-access p{x} f{floor})")

    kinds = [f"(going_up p{x})" for x in ups if origin[x] < destin[x]]
    kinds += [f"(going_down p{x})" for x in ups if origin[x] > destin[x]]
    kinds += [f"({kind} p{x})" for kind, group in (("vip", vips), ("going_nonstop", nonstops), ("attendant", attendants),
                                                  ("never_alone", alones), ("conflict_a", group_a), ("conflict_b", group_b))
              for x in group]
    init = kinds + [f"(above f{i} f{j})" for i in range(f - 1) for j in range(i + 1, f)]
    for i in range(p):
        init += [f"(origin p{i} f{origin[i]})", f"(destin p{i} f{destin[i]})"]
    init += no_access_facts + ["(lift-at f0)"]
    name = (f"mixed-f{f}-p{p}-u{up_down}-v{vip}-g{going_nonstop}-a{attendant}-n{never_alone}"
            f"-a{conflict_a}-b{conflict_b}-n{no_access}-f{no_access_floors}-r{seed}")
    return (f"""(define (problem {name})
   (:domain miconic)
   (:objects {' '.join(f'p{i}' for i in range(p))} - passenger
             {' '.join(f'f{i}' for i in range(f))} - floor)
   (:init
{chr(10).join(init)}
   )
   (:goal (forall (?p - passenger) (served ?p)))
)
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Miconic-ADL PDDL problem (miconic.c options).")
    parser.add_argument("-f", "--num-floors", type=int, required=True)
    parser.add_argument("-p", "--num-passengers", type=int, required=True)
    for flag, dest, default in (("-u", "up_down", 20), ("-v", "vip", 5), ("-g", "going_nonstop", 5), ("-a", "attendant", 60),
                                ("-n", "never_alone", 10), ("-A", "conflict_a", 20), ("-B", "conflict_b", 80),
                                ("-N", "no_access", 50), ("-F", "no_access_floors", 5)):
        parser.add_argument(flag, dest=dest, type=int, default=default)
    parser.add_argument("-r", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
