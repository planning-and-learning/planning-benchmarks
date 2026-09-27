#!/usr/bin/env python3
# IPC-1998 Mystery Prime tasks share the Mystery distribution (prob01-30 are the Mystery
# tasks); only the domain adds the fuel-passing action.

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.mystery import generator as _mystery

make_problem = partial(_mystery.make_problem, prime=True)


def main(argv: list[str] | None = None) -> int:
    return _mystery.main(argv, prime=True)


if __name__ == "__main__":
    sys.exit(main())
