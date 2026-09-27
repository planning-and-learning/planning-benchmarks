#!/usr/bin/env python3
# Autoscale's sokoban tasks are IPC tasks; they follow the ipc/sokoban distribution.

from pypddl_datasets.generators.classical.ipc.sokoban.generator import main, make_problem

__all__ = ["main", "make_problem"]

if __name__ == "__main__":
    raise SystemExit(main())
