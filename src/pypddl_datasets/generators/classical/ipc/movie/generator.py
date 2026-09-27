#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-Freiburg
# Derived from pddl-generators movie/movie.c (FF domain collection). Distributed
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
# Port of pddl-generators movie/movie.c (FF domain collection), laid out like the IPC-1998 tasks.

from __future__ import annotations

import argparse
import sys
from typing import cast

SNACKS = (("chips", "c"), ("dip", "d"), ("pop", "p"), ("cheese", "z"), ("crackers", "k"))


def make_problem(num_snacks: int) -> str:
    """Deterministic: ``num_snacks`` objects of each of the five snack kinds.

    IPC-1998 task ``probNN`` uses ``num_snacks = NN + 4``. Objects are listed per
    kind in descending order, as in the IPC tasks.
    """
    checked = cast(object, num_snacks)  # runtime guard: callers may pass floats or bools
    if not isinstance(checked, int) or isinstance(checked, bool) or checked < 1:
        raise ValueError("num_snacks must be an integer at least 1")
    names = [(kind, [f"{prefix}{i}" for i in range(num_snacks, 0, -1)]) for kind, prefix in SNACKS]
    objects = " ".join(name for _, group in names for name in group)
    init = "\n".join(f"          ({kind} {name})" for kind, group in names for name in group)
    return (f"""(define (problem strips-movie-{num_snacks})
   (:domain movie-strips)
   (:objects {objects})
   (:init
{init}
          (counter-at-other-than-two-hours))
   (:goal (and (movie-rewound)
               (counter-at-zero)
               (have-chips)
               (have-dip)
               (have-pop)
               (have-cheese)
               (have-crackers))))
""").lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Movie PDDL problem.")
    parser.add_argument("-n", "--num-snacks", type=int, required=True, help="objects per snack kind")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(args.num_snacks)
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
