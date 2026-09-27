#!/usr/bin/env python3
# Autoscale uses the ipc/barman generator in its action-cost encoding (Autoscale's domain.pddl).

from __future__ import annotations

import sys
from functools import partial

from pypddl_datasets.generators.classical.ipc.barman import generator as _ipc

make_problem = partial(_ipc.make_problem, action_costs=True)


def main(argv: list[str] | None = None) -> int:
    return _ipc.main([*(sys.argv[1:] if argv is None else argv), "--action-costs"])


if __name__ == "__main__":
    raise SystemExit(main())
