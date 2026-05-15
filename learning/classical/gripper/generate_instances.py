#!/usr/bin/env python3

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
GENERATOR_DIR = ROOT_DIR / "generators" / "classical" / "gripper"
sys.path.insert(0, str(ROOT_DIR))

from generators.classical.gripper import make_problem  # noqa: E402


CONFIGS = {
    "train": [1, 2, 3, 4, 5],
    "valid": [6, 7, 8, 9, 10],
    "test": [11, 12, 13, 14, 15],
}


def main() -> int:
    output_dir = Path(__file__).resolve().parent
    shutil.copyfile(GENERATOR_DIR / "domain.pddl", output_dir / "domain.pddl")

    for split, num_balls_values in CONFIGS.items():
        split_dir = output_dir / split
        split_dir.mkdir(parents=True, exist_ok=True)

        for index, num_balls in enumerate(num_balls_values, start=1):
            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(make_problem(num_balls), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
