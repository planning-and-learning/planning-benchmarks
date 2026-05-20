#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GENERATOR_DIR = ROOT_DIR / "generators" / "classical" / "childsnack"
sys.path.insert(0, str(ROOT_DIR))

from generators.classical.childsnack.generator import make_problem  # noqa: E402


NUM_INSTANCES_PER_SPLIT = 30

CONFIGS = {
    "train": [(2 + index % 4, 1 + index % 2, 0.25 + 0.25 * (index % 3), 1.2, 101 + index) for index in range(NUM_INSTANCES_PER_SPLIT)],
    "valid": [(6 + index % 4, 2 + index % 2, 0.25 + 0.25 * (index % 3), 1.2, 201 + index) for index in range(NUM_INSTANCES_PER_SPLIT)],
    "test": [(10 + index % 5, 3 + index % 2, 0.25 + 0.25 * (index % 3), 1.2, 301 + index) for index in range(NUM_INSTANCES_PER_SPLIT)],
}


def main() -> int:
    output_dir = Path(__file__).resolve().parent
    shutil.copyfile(GENERATOR_DIR / "domain.pddl", output_dir / "domain.pddl")

    for split, configs in CONFIGS.items():
        split_dir = output_dir / split
        split_dir.mkdir(parents=True, exist_ok=True)
        for old_problem_path in split_dir.glob(f"{split}-*.pddl"):
            old_problem_path.unlink()

        for index, (num_children, num_trays, gluten_factor, const_ratio, seed) in enumerate(configs, start=1):
            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(
                make_problem(num_children, num_trays, gluten_factor, const_ratio, seed),
                encoding="utf-8",
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
