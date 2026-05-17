#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GENERATOR_DIR = ROOT_DIR / "generators" / "classical" / "hiking"
sys.path.insert(0, str(ROOT_DIR))

from generators.classical.hiking import make_problem  # noqa: E402


NUM_INSTANCES_PER_SPLIT = 30

TRAIN_SHAPES = [
    (1, 2, 2),
    (1, 2, 3),
    (1, 2, 4),
    (2, 3, 2),
    (2, 3, 3),
    (3, 4, 2),
    (3, 4, 3),
]

VALID_SHAPES = [
    (1, 2, 4),
    (1, 3, 4),
    (2, 3, 4),
    (2, 4, 4),
    (3, 4, 4),
    (3, 5, 4),
]

TEST_SHAPES = [
    (1, 2, 5),
    (1, 3, 5),
    (2, 3, 5),
    (2, 4, 5),
    (3, 4, 5),
    (3, 5, 5),
]


def with_seeds(shapes, seed_start):
    return [
        (*shapes[index % len(shapes)], seed_start + index)
        for index in range(NUM_INSTANCES_PER_SPLIT)
    ]


CONFIGS = {
    "train": with_seeds(TRAIN_SHAPES, 101),
    "valid": with_seeds(VALID_SHAPES, 201),
    "test": with_seeds(TEST_SHAPES, 301),
}


def main() -> int:
    output_dir = Path(__file__).resolve().parent
    shutil.copyfile(GENERATOR_DIR / "domain.pddl", output_dir / "domain.pddl")

    for split, configs in CONFIGS.items():
        split_dir = output_dir / split
        split_dir.mkdir(parents=True, exist_ok=True)
        for old_problem_path in split_dir.glob(f"{split}-*.pddl"):
            old_problem_path.unlink()

        for index, (num_couples, num_cars, num_places, seed) in enumerate(configs, start=1):
            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(
                make_problem(num_couples, num_cars, num_places, seed),
                encoding="utf-8",
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
