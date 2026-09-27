#!/usr/bin/env python3
# Miconic-SIMPLE tasks are the typed Miconic STRIPS tasks (uniform journeys, lift at f0);
# only the domain file (conditional-effect stop) differs, so this re-exports ipc/miconic typed.

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.miconic import generator as _ipc

make_problem = partial(_ipc.make_problem, typed=True)


def main(argv: list[str] | None = None) -> int:
    return _ipc.main([*(sys.argv[1:] if argv is None else argv), "--typed"])


if __name__ == "__main__":
    raise SystemExit(main())
