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
    "train": cartesian(range(1, 4), range(2, 5), range(2, 4)),
    "valid": cartesian(range(4, 5), range(5, 6), range(4, 6)),
    "test": cartesian(range(5, 6), range(6, 8), range(5, 7)),
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

    for split, shapes in STRUCTURAL_SPACES.items():
        split_dir = output_root / f"{here.parent.name}-{split}"
        split_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(here.parent / "domain.pddl", split_dir / "domain.pddl")
        for old_problem_path in split_dir.glob(f"{split}-*.pddl"):
            old_problem_path.unlink()

        index = 1
        seed = SEED_STARTS[split]
        attempts = 0
        max_attempts = NUM_INSTANCES_PER_SPLIT * len(shapes)
        for num_couples, num_cars, num_places in cycle(shapes):
            attempts += 1
            if attempts > max_attempts:
                raise ValueError(f"Could not generate {NUM_INSTANCES_PER_SPLIT} {split} instances")

            problem = make_problem(num_couples, num_cars, num_places, seed)
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
