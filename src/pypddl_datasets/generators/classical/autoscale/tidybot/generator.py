#!/usr/bin/env python3
# Autoscale's tidybot tasks are IPC tasks; they follow the ipc/tidybot distribution.

from pypddl_datasets.generators.classical.ipc.tidybot.generator import main, make_problem

__all__ = ["main", "make_problem"]

if __name__ == "__main__":
    raise SystemExit(main())
