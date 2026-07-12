#!/usr/bin/env python3

from __future__ import annotations

from itertools import product
import shutil
from pathlib import Path

from .generator import make_problem

from collections.abc import Callable, Iterable
from typing import Any

Config = tuple[Any, ...]


NUM_INSTANCES_PER_SPLIT = 100


def cartesian(*dimensions: Iterable[Any], predicate: Callable[..., bool] | None = None) -> list[Config]:
    configs: list[Config] = []
    for values in product(*dimensions):
        if predicate is None or predicate(*values):
            configs.append(values)
    return configs


def first_n(configs: list[Config], count: int = NUM_INSTANCES_PER_SPLIT) -> list[Config]:
    if len(configs) < count:
        raise ValueError(f"Need {count} configs, got {len(configs)}")
    return configs[:count]


def with_instance_seeds(configs: list[Config], seed_start: int, count: int = NUM_INSTANCES_PER_SPLIT) -> list[Config]:
    if not configs:
        raise ValueError("Need at least one structural config")
    return [(*configs[index % len(configs)], seed_start + index) for index in range(count)]


def assert_pairwise_disjoint(configs_by_split: dict[str, list[Config]]) -> None:
    seen: dict[Config, str] = {}
    for split, configs in configs_by_split.items():
        for config in configs:
            previous = seen.setdefault(config, split)
            if previous != split:
                raise ValueError(f"Config {config} occurs in both {previous} and {split}")


STRUCTURAL_SPACES: dict[str, list[Config]] = {
    "train": cartesian(range(2, 5), range(1, 3), [0.25, 0.5, 0.75], [1.2, 1.5]),
    "valid": cartesian(range(7, 11), range(1, 4), [0.25, 0.5, 0.75], [1.2, 1.5]),
    "test": cartesian(range(11, 17), range(2, 5), [0.25, 0.5, 0.75], [1.2, 1.5]),
}

assert_pairwise_disjoint(STRUCTURAL_SPACES)

CONFIGS: dict[str, list[Config]] = {
    "train": with_instance_seeds(STRUCTURAL_SPACES["train"], 101),
    "valid": with_instance_seeds(STRUCTURAL_SPACES["valid"], 201),
    "test": with_instance_seeds(STRUCTURAL_SPACES["test"], 301),
}

assert_pairwise_disjoint(CONFIGS)


def main() -> int:
    here = Path(__file__).resolve()
    output_root = here.parents[5] / "data" / "classical" / "generated"

    for split, configs in CONFIGS.items():
        split_dir = output_root / f"{here.parent.name}-{split}"
        split_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(here.parent / "domain.pddl", split_dir / "domain.pddl")
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
