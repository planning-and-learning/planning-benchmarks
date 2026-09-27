#!/usr/bin/env python3
# The learning track's own sokoban generator has no license, so this uses ipc/sokoban's
# levels in the learning-track encoding (style="learning").

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.sokoban import generator as _ipc

make_problem = partial(_ipc.make_problem, style="learning")


def main(argv: list[str] | None = None) -> int:
    return _ipc.main([*(sys.argv[1:] if argv is None else argv), "--style", "learning"])


if __name__ == "__main__":
    raise SystemExit(main())
