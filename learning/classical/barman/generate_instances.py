#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GENERATOR_DIR = ROOT_DIR / "generators" / "classical" / "barman"
sys.path.insert(0, str(ROOT_DIR))

from generators.classical.barman.generator import make_problem  # noqa: E402


NUM_INSTANCES_PER_SPLIT = 30

CONFIGS = {
    "train": [(1 + index % 3, 2 + index % 3, 2 + index % 4, 101 + index) for index in range(NUM_INSTANCES_PER_SPLIT)],
    "valid": [(4 + index % 3, 4 + index % 3, 5 + index % 4, 201 + index) for index in range(NUM_INSTANCES_PER_SPLIT)],
    "test": [(7 + index % 3, 6 + index % 4, 8 + index % 4, 301 + index) for index in range(NUM_INSTANCES_PER_SPLIT)],
}


def main() -> int:
    output_dir = Path(__file__).resolve().parent
    shutil.copyfile(GENERATOR_DIR / "domain.pddl", output_dir / "domain.pddl")

    for split, configs in CONFIGS.items():
        split_dir = output_dir / split
        split_dir.mkdir(parents=True, exist_ok=True)
        for old_problem_path in split_dir.glob(f"{split}-*.pddl"):
            old_problem_path.unlink()

        for index, (num_cocktails, num_ingredients, num_shots, seed) in enumerate(configs, start=1):
            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(
                make_problem(num_cocktails, num_ingredients, num_shots, seed),
                encoding="utf-8",
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
