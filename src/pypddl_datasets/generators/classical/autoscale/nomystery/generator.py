#!/usr/bin/env python3
# Autoscale uses the ipc/nomystery generator with the sum table restricted to edge costs (Autoscale's domain.pddl).

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.nomystery import generator as _ipc

make_problem = partial(_ipc.make_problem, full_sum_table=False)


def main(argv: list[str] | None = None) -> int:
    return _ipc.main([*(sys.argv[1:] if argv is None else argv), "--restricted-sum-table"])


if __name__ == "__main__":
    raise SystemExit(main())
