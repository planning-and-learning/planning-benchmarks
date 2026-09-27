#!/usr/bin/env python3
# Autoscale's tetris tasks are IPC tasks; they follow the ipc/tetris distribution.

from pypddl_datasets.generators.classical.ipc.tetris.generator import main, make_problem

__all__ = ["main", "make_problem"]

if __name__ == "__main__":
    raise SystemExit(main())
