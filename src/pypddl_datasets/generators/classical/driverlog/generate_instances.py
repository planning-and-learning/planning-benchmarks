#!/usr/bin/env python3

from __future__ import annotations

from itertools import product
import shutil
from pathlib import Path

from .generator import make_problem


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


def with_goal_probabilities(configs, probabilities):
    if not probabilities:
        raise ValueError("Need at least one goal probability triple")
    return [(*config[:-1], *probabilities[index % len(probabilities)], config[-1]) for index, config in enumerate(configs)]


def assert_pairwise_disjoint(configs_by_split):
    seen = {}
    for split, configs in configs_by_split.items():
        for config in configs:
            previous = seen.setdefault(config, split)
            if previous != split:
                raise ValueError(f"Config {config} occurs in both {previous} and {split}")


GOAL_PROBABILITY_VALUES = (0.5, 0.75, 1.0)
GOAL_PROBABILITIES = tuple(product(GOAL_PROBABILITY_VALUES, repeat=3))

STRUCTURAL_SPACES = {
    "train": cartesian(range(4, 8), range(2, 5), range(2, 5), range(2, 5)),
    "valid": cartesian(range(9, 13), range(1, 3), range(1, 3), range(5, 8)),
    "test": cartesian(range(13, 19), range(2, 5), range(2, 5), range(8, 12)),
}

assert_pairwise_disjoint(STRUCTURAL_SPACES)

CONFIGS = {
    "train": with_goal_probabilities(with_instance_seeds(STRUCTURAL_SPACES["train"], 101), GOAL_PROBABILITIES),
    "valid": with_goal_probabilities(with_instance_seeds(STRUCTURAL_SPACES["valid"], 201), GOAL_PROBABILITIES),
    "test": with_goal_probabilities(with_instance_seeds(STRUCTURAL_SPACES["test"], 301), GOAL_PROBABILITIES),
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

        for index, (num_locations, num_drivers, num_trucks, num_packages, package_goal_probability, driver_goal_probability, truck_goal_probability, seed) in enumerate(configs, start=1):
            problem_path = split_dir / f"{split}-{index}.pddl"
            problem_path.write_text(
                make_problem(
                    num_locations,
                    num_drivers,
                    num_trucks,
                    num_packages,
                    seed=seed,
                    package_goal_probability=package_goal_probability,
                    driver_goal_probability=driver_goal_probability,
                    truck_goal_probability=truck_goal_probability,
                ),
                encoding="utf-8",
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
