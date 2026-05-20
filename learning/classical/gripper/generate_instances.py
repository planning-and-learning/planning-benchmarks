#!/usr/bin/env python3

from __future__ import annotations

from itertools import product
import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GENERATOR_DIR = ROOT_DIR / "generators" / "classical" / "gripper"
sys.path.insert(0, str(ROOT_DIR))

from generators.classical.gripper import make_problem  # noqa: E402


NUM_INSTANCES_PER_SPLIT = 100


def cartesian(*dimensions, predicate=None):
    configs = []
    for values in product(*dimensions):
        if predicate is None or predicate(*values):
            configs.append(values)
    return configs


def first_n(configs, count: int = NUM_INSTANCES_PER_SPLIT):
    if len(configs) < count:
        raise ValueError(f"Need {count} configs, got {len(configs)}")
    return configs[:count]


def with_instance_seeds(configs, seed_start: int, count: int = NUM_INSTANCES_PER_SPLIT):
    if not configs:
        raise ValueError("Need at least one structural config")
    return [(*configs[index % len(configs)], seed_start + index) for index in range(count)]


def assert_pairwise_disjoint(configs_by_split):
    seen = {}
    for split, configs in configs_by_split.items():
        for config in configs:
            previous = seen.setdefault(config, split)
            if previous != split:
                raise ValueError(f"Config {config} occurs in both {previous} and {split}")


STRUCTURAL_SPACES = {
    "train": [(num_balls,) for num_balls in range(1, 6)],
    "valid": [(num_balls,) for num_balls in range(6, 11)],
    "test": [(num_balls,) for num_balls in range(11, 21)],
}

assert_pairwise_disjoint(STRUCTURAL_SPACES)

CONFIGS = {
    "train": STRUCTURAL_SPACES["train"],
    "valid": STRUCTURAL_SPACES["valid"],
    "test": STRUCTURAL_SPACES["test"],
}

assert_pairwise_disjoint(CONFIGS)


def main() -> int:
    output_dir = Path(__file__).resolve().parent
    shutil.copyfile(GENERATOR_DIR / "domain.pddl", output_dir / "domain.pddl")

    for split, configs in CONFIGS.items():
        split_dir = output_dir / split
        split_dir.mkdir(parents=True, exist_ok=True)
        for old_problem_path in split_dir.glob(f"{split}-*.pddl"):
            old_problem_path.unlink()

        for index, (num_balls,) in enumerate(configs, start=1):
            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(
                make_problem(num_balls),
                encoding="utf-8",
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
