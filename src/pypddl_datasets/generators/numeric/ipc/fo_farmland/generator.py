#!/usr/bin/env python3
# FO-Farmland (Scala and Li): the ipc/farmland generator with hireable cars
# ((= (num-of-cars) 0)) and the reward bound penalised by (cost), as in the IPC 2023 tasks.

from __future__ import annotations

import sys

from pypddl_datasets.generators.numeric.ipc.farmland import generator as _farmland


def make_problem(num_farms: int, num_units: int, seed: int | None = None) -> str:
    """Generate an FO-Farmland task; same farms, workers and weights as
    ``numeric/ipc/farmland``, goal reward minus cost at least 1.4 * num_units."""
    return _farmland._make(num_farms, num_units, seed, first_order=True)


def main(argv: list[str] | None = None) -> int:
    return _farmland.main(argv, first_order=True)


if __name__ == "__main__":
    sys.exit(main())
