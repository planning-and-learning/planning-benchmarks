#!/usr/bin/env python3
# Autoscale's pathways tasks are IPC tasks; they follow the ipc/pathways distribution.

from pypddl_datasets.generators.classical.ipc.pathways.generator import main, make_task

__all__ = ["main", "make_task"]

if __name__ == "__main__":
    raise SystemExit(main())
