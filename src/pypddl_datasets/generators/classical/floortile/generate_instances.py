#!/usr/bin/env python3

from __future__ import annotations

import shutil
from itertools import cycle, product
from pathlib import Path

from .generator import make_problem

from collections.abc import Iterable
from typing import Any

Config = tuple[int, int, int]


NUM_INSTANCES_PER_SPLIT = 100


def cartesian(*dimensions: Iterable[Any]) -> list[Config]:
    return list(product(*dimensions))


def assert_pairwise_disjoint(configs_by_split: dict[str, list[Config]]) -> None:
    seen: dict[Config, str] = {}
    for split, configs in configs_by_split.items():
        for config in configs:
            previous = seen.setdefault(config, split)
            if previous != split:
                raise ValueError(f"Config {config} occurs in both {previous} and {split}")


STRUCTURAL_SPACES: dict[str, list[Config]] = {
    "train": cartesian(range(2, 5), range(3, 6), range(1, 3)),
    "valid": cartesian(range(5, 7), range(6, 8), range(2, 4)),
    "test": cartesian(range(7, 10), range(8, 11), range(3, 5)),
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
