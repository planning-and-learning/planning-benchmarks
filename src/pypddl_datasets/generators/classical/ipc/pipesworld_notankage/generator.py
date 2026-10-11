#!/usr/bin/env python3
# IPC-2004 Pipesworld without tankage: the ipc/pipesworld_tankage distribution with
# tankage=None (no tank slots, no `normal` goals); the IPC notankage and tankage tasks share
# their initial states and goals.

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.pipesworld_tankage import generator as _tankage

make_problem = partial(_tankage.make_problem, tankage=None)


def main(argv: list[str] | None = None) -> int:
    return _tankage.main(argv, tankage=False)


if __name__ == "__main__":
    sys.exit(main())
