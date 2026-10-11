#!/usr/bin/env python3
# Autoscale uses the IPC pipesworld-notankage tasks (no generator); only domain.pddl is Autoscale's.

from pypddl_datasets.generators.classical.ipc.pipesworld_notankage.generator import main, make_problem

__all__ = ["main", "make_problem"]

if __name__ == "__main__":
    raise SystemExit(main())
