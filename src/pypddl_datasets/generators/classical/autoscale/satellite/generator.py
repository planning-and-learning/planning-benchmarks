#!/usr/bin/env python3
# Autoscale uses the ipc/satellite generator with typed=True, patched=True (Autoscale's domain.pddl).

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.satellite import generator as _ipc

make_problem = partial(_ipc.make_problem, typed=True, patched=True)


def main(argv: list[str] | None = None) -> int:
    return _ipc.main([*(sys.argv[1:] if argv is None else argv), "--typed", "--patched"])


if __name__ == "__main__":
    raise SystemExit(main())
