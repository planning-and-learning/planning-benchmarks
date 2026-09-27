#!/usr/bin/env python3
# Autoscale's pegsol tasks are IPC tasks; they follow the ipc/pegsol distribution.

from pypddl_datasets.generators.classical.ipc.pegsol.generator import main, make_problem

__all__ = ["main", "make_problem"]

if __name__ == "__main__":
    raise SystemExit(main())
