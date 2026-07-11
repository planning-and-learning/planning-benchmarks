#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from itertools import cycle, product
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GENERATOR_DIR = ROOT_DIR / "generators" / "classical" / "satellite"
sys.path.insert(0, str(ROOT_DIR))

from generators.classical.satellite import make_problem  # noqa: E402


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


POINTING_GOAL_PROBABILITIES = [0.25, 0.5, 0.75]

STRUCTURAL_SPACES = {
    "train": cartesian(range(1, 3), range(1, 4), range(2, 4), range(1, 3), range(1, 4), POINTING_GOAL_PROBABILITIES),
    "valid": cartesian(range(3, 5), range(4, 6), range(3, 5), range(3, 5), range(4, 6), POINTING_GOAL_PROBABILITIES),
    "test": cartesian(range(5, 7), range(6, 9), range(4, 6), range(5, 7), range(6, 9), POINTING_GOAL_PROBABILITIES),
}

assert_pairwise_disjoint(STRUCTURAL_SPACES)

SEED_STARTS = {
    "train": 101,
    "valid": 201,
    "test": 301,
}


def main() -> int:
    output_dir = Path(__file__).resolve().parent
    shutil.copyfile(GENERATOR_DIR / "domain.pddl", output_dir / "domain.pddl")

    for split, configs in STRUCTURAL_SPACES.items():
        split_dir = output_dir / split
        split_dir.mkdir(parents=True, exist_ok=True)
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
