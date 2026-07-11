#!/usr/bin/env python3

from __future__ import annotations

import shutil
from itertools import cycle, product
from pathlib import Path

from .generator import make_problem


NUM_INSTANCES_PER_SPLIT = 100


def cartesian(*dimensions):
    return list(product(*dimensions))


def assert_pairwise_disjoint(configs_by_split):
    seen = {}
    for split, configs in configs_by_split.items():
        for config in configs:
            previous = seen.setdefault(config, split)
            if previous != split:
                raise ValueError(f"Config {config} occurs in both {previous} and {split}")


STRUCTURAL_SPACES = {
    "train": cartesian(range(3, 7), range(4, 8)),
    "valid": cartesian(range(7, 10), range(8, 11)),
    "test": cartesian(range(10, 14), range(11, 15)),
}

assert_pairwise_disjoint(STRUCTURAL_SPACES)

SEED_STARTS = {
    "train": 101,
    "valid": 201,
    "test": 301,
}


def main() -> int:
    here = Path(__file__).resolve()
    output_root = here.parents[5] / "data" / "classical" / "generated"

    for split, configs in STRUCTURAL_SPACES.items():
        split_dir = output_root / f"{here.parent.name}-{split}"
        split_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(here.parent / "domain.pddl", split_dir / "domain.pddl")
        for old_problem_path in split_dir.glob(f"{split}-*.pddl"):
            old_problem_path.unlink()

        index = 1
        seed = SEED_STARTS[split]
        attempts = 0
        max_attempts = NUM_INSTANCES_PER_SPLIT * len(configs)
        for config in cycle(configs):
            attempts += 1
            if attempts > max_attempts:
                raise ValueError(f"Could not generate {NUM_INSTANCES_PER_SPLIT} {split} instances")

            problem = make_problem(*config, seed)
            seed += 1
            if problem is None:
                continue

            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(problem, encoding="utf-8")
            index += 1
            if index > NUM_INSTANCES_PER_SPLIT:
                break

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
