#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators schedule/schedule.c (FF domain collection). Distributed
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

from __future__ import annotations

import argparse
import random
import sys
from typing import cast

SHAPES = ("cylindrical", "circular", "oblong")
SURFACES = ("polished", "rough", "smooth")
COLOURS = ("blue", "yellow", "red", "black")
WIDTHS = ("two", "three", "one")
ORIENTATIONS = ("back", "front")
# IPC part names cycle through these 23 letters (no t, x, y; q before p): a0..z0, a1, ...
LETTERS = "abcdefghijklmnoqprsuvwz"


def part_name(index: int) -> str:
    return f"{LETTERS[index % len(LETTERS)]}{index // len(LETTERS)}"


def make_problem(num_parts: int, seed: int | None = None) -> str:
    """Generate a Schedule task shaped like the IPC 2000 tasks.

    Every part gets a uniform shape, surface, paint colour and hole (width and
    orientation). The goal has exactly ``num_parts`` facts: distinct
    (part, kind) pairs drawn uniformly from all pairs whose goal is not yet
    true, where a kind is "make cylindrical" (only for non-cylindrical parts),
    "change the surface" or "repaint" (to a uniform different value). There
    are no hole goals.
    """
    checked = cast(object, num_parts)  # runtime check: callers may pass any type
    if not isinstance(checked, int) or isinstance(checked, bool) or checked < 1:
        raise ValueError("num_parts must be an integer at least 1")
    rng = random.Random(seed)
    parts = [part_name(i) for i in range(num_parts)]
    states = [
        (rng.choice(SHAPES), rng.choice(SURFACES), rng.choice(COLOURS), rng.choice(WIDTHS), rng.choice(ORIENTATIONS))
        for _ in parts
    ]

    candidates = [
        (i, kind)
        for i, state in enumerate(states)
        for kind in ("shape", "surface", "paint")
        if kind != "shape" or state[0] != "cylindrical"
    ]
    goals: list[str] = []
    for i, kind in rng.sample(candidates, num_parts):  # at least 2 candidates per part
        shape, surface, colour = states[i][:3]
        if kind == "shape":
            goals.append(f"(shape {parts[i]} cylindrical)")
        elif kind == "surface":
            goals.append(f"(surface-condition {parts[i]} {rng.choice([s for s in SURFACES if s != surface])})")
        else:
            goals.append(f"(painted {parts[i]} {rng.choice([c for c in COLOURS if c != colour])})")

    init: list[str] = []
    for part, (shape, surface, colour, width, orientation) in zip(parts, states):
        init += [
            f"(shape {part} {shape})",
            f"(surface-condition {part} {surface})",
            f"(painted {part} {colour})",
            f"(has-hole {part} {width} {orientation})",
            f"(temperature {part} cold)",
        ]
    for orientation in ORIENTATIONS:
        init += [f"(can-orient drill-press {orientation})", f"(can-orient punch {orientation})"]
    for colour in COLOURS:
        init += [f"(has-paint immersion-painter {colour})", f"(has-paint spray-painter {colour})"]
    for width in WIDTHS:
        init += [f"(has-bit drill-press {width})", f"(has-bit punch {width})"]

    objects = [f"{' '.join(reversed(parts))} - part", f"{' '.join(SHAPES[1:])} - ashape"]  # IPC lists both (149/150)
    objects += [f"{' '.join(COLOURS)} - colour", f"{' '.join(WIDTHS)} - width", f"{' '.join(ORIENTATIONS)} - anorient"]

    nl = "\n    "
    return (f"""(define (problem schedule-{num_parts})
(:domain schedule)
(:objects
    {nl.join(objects)}
)
(:init
    {nl.join(init)}
)
(:goal (and
    {nl.join(goals)}
)))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="generate an ipc-style schedule planning problem")
    parser.add_argument("-p", "--num-parts", type=int, required=True)
    parser.add_argument("-r", "--seed", type=int)
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_parts, args.seed)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
