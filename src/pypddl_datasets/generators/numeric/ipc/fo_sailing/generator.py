#!/usr/bin/env python3
# FO-Sailing (Scala and Li): the numeric/ipc/sailing generator with every boat at
# speed (v b) = 1, as in the IPC 2023 tasks.

from __future__ import annotations

import sys

from pypddl_datasets.generators.numeric.ipc.sailing import generator as _sailing


def make_problem(
    num_boats: int,
    num_people: int,
    seed: int | None = None,
    max_distance: int = 500,
    nonnegative_distances: bool = False,
) -> str:
    """Generate an FO-Sailing task; same boats and people as ``numeric/ipc/sailing``, plus v = 1."""
    return _sailing.build(num_boats, num_people, seed, max_distance, True, nonnegative_distances)


def main(argv: list[str] | None = None) -> int:
    return _sailing.main(argv, first_order=True)


if __name__ == "__main__":
    sys.exit(main())
