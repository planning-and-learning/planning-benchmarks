#!/usr/bin/env python3
# Autoscale uses the ipc/grid generator with style="autoscale" (upstream generate.py);
# only domain.pddl is Autoscale's.

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.grid import generator as _ipc

make_problem = partial(_ipc.make_problem, style="autoscale")


def main(argv: list[str] | None = None) -> int:
    return _ipc.main([*(sys.argv[1:] if argv is None else argv), "--style", "autoscale"])


if __name__ == "__main__":
    raise SystemExit(main())
