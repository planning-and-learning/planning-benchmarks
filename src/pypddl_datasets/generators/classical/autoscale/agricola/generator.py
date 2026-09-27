#!/usr/bin/env python3
# Autoscale's agricola tasks are IPC tasks; they follow the ipc/agricola distribution.

from pypddl_datasets.generators.classical.ipc.agricola.generator import main, make_problem

__all__ = ["main", "make_problem"]

if __name__ == "__main__":
    raise SystemExit(main())
