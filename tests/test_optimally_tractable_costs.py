"""The stated optimal costs of the optimally-tractable fragments are optimal and grow with size.

A blind uniform-cost search (``optimal_solver``) recomputes the optimal cost of small
tasks of every fragment. The fragments whose sampling moved to the package's standard
samplers in 0.0.19 also show a mean optimal cost that grows over 10, 100 and 1000
objects (Sokoban on 8, 16 and 32 cell wide grids, where level generation stays quick).
"""

from __future__ import annotations

import importlib.util
import math
import re
import statistics
from collections.abc import Callable
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest
from optimal_solver import optimal_cost

ROOT = Path(__file__).resolve().parents[1] / "src/pypddl_datasets/generators/classical/optimally-tractable"
SEEDS = (1, 2, 3)
NO_SEED = {"gripper/one_way.py", "movie/standard.py"}

SMALL: dict[str, dict[str, Any]] = {
    **{f"{encoding}/{fragment}.py": {"num_blocks": 5} for encoding in ("blocks_3", "blocks_4")
       for fragment in ("clear_block", "clear_blocks", "goal_on_table", "init_on_table", "on_pair", "table_blocks")},
    "childsnack/exact_ingredients.py": {"num_children": 2, "num_trays": 2, "gluten_factor": 0.5},
    "delivery/common_destination.py": {"grid_size": 3, "num_packages": 2},
    "delivery/common_route.py": {"grid_size": 3, "num_trucks": 2, "num_packages": 2},
    "elevators/common_destination.py": {"num_floors": 4, "num_passengers": 3},
    "elevators/common_origin.py": {"num_floors": 4, "num_passengers": 3, "kind": "fast"},
    "ferry/common_origin.py": {"num_cars": 3, "num_locations": 3},
    "ferry/unrestricted.py": {"num_cars": 3, "num_locations": 3},
    "floortile/single_column.py": {"num_rows": 3},
    "goldminer/standard.py": {"num_rows": 3, "num_cols": 4},
    "grid/single_key.py": {"width": 4, "height": 3},
    "grid/single_key_locks.py": {"width": 4, "height": 3},
    "gripper/one_way.py": {"num_balls": 3},
    "gripper/two_way.py": {"num_balls": 4},
    "logistics/common_destination.py": {"num_cities": 2, "city_size": 2, "num_planes": 1, "num_packages": 2},
    "logistics/common_origin.py": {"num_cities": 2, "city_size": 2, "num_planes": 1, "num_packages": 2},
    "miconic/common_destination.py": {"num_floors": 4, "num_passengers": 3},
    "miconic/common_origin.py": {"num_floors": 4, "num_passengers": 3},
    "miconic/disjoint_floors.py": {"num_floors": 4, "num_passengers": 3},
    "movie/standard.py": {"num_snacks": 2},
    "nomystery/single_package.py": {"num_locations": 4},
    "ricochet_robots/single_robot.py": {"board_size": 4},
    "satellite/single_instrument.py": {"num_targets": 2, "num_observations": 2, "num_modes": 2},
    "sokoban/single_box.py": {"grid_size": 7},
    "spanner/corridor.py": {"num_spanners": 3, "num_nuts": 2, "num_locations": 3},
    "tpp/exclusive_markets.py": {"num_goods": 2, "num_markets": 2, "max_level": 2},
    "transport/common_destination.py": {"num_nodes": 4, "num_packages": 2},
    "transport/common_route.py": {"num_nodes": 4, "num_trucks": 2, "num_packages": 2},
    "visitall/full_grid.py": {"width": 3, "height": 3},
    "visitall/row.py": {"num_cells": 5},
    "visitall/tree_maze.py": {"width": 3, "height": 3},
    "zenotravel/common_destination.py": {"num_cities": 3, "num_people": 2},
    "zenotravel/common_origin.py": {"num_cities": 3, "num_people": 2},
}


def _square(num_cells: int) -> int:
    return math.isqrt(num_cells)


SIZES = (10, 100, 1000)
GROWTH: dict[str, tuple[Callable[[int], dict[str, Any]], tuple[int, ...]]] = {
    **{f"{encoding}/{fragment}.py": (lambda n: {"num_blocks": n}, SIZES) for encoding in ("blocks_3", "blocks_4")
       for fragment in ("clear_block", "clear_blocks", "goal_on_table", "init_on_table", "on_pair", "table_blocks")},
    "nomystery/single_package.py": (lambda n: {"num_locations": n}, SIZES),
    "sokoban/single_box.py": (lambda n: {"grid_size": n}, (8, 16, 32)),
    "transport/common_destination.py": (lambda n: {"num_nodes": n, "num_packages": 3}, SIZES),
    "transport/common_route.py": (lambda n: {"num_nodes": n, "num_trucks": 2, "num_packages": 3}, SIZES),
    "ricochet_robots/single_robot.py": (lambda n: {"board_size": _square(n)}, SIZES),
    "grid/single_key_locks.py": (lambda n: {"width": _square(n), "height": _square(n)}, SIZES),
}


def _load(fragment: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(fragment.replace("/", "."), ROOT / fragment)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _stated_cost(problem: str) -> int:
    match = re.match(r"; optimal plan cost: (\d+)\n", problem)
    assert match is not None
    return int(match.group(1))


def test_every_fragment_is_checked() -> None:
    assert sorted(p.relative_to(ROOT).as_posix() for p in ROOT.glob("*/*.py")) == sorted(SMALL)


@pytest.mark.parametrize("fragment", sorted(SMALL))
def test_stated_cost_is_optimal(fragment: str) -> None:
    module = _load(fragment)
    domain = ROOT / fragment.split("/")[0] / "domain.pddl"
    for seed in SEEDS:
        problem: str = module.make_problem(**SMALL[fragment]) if fragment in NO_SEED else module.make_problem(
            **SMALL[fragment], seed=seed
        )
        assert optimal_cost(domain, problem) == _stated_cost(problem), (fragment, seed)
        if fragment in NO_SEED:
            break


@pytest.mark.parametrize("fragment", sorted(GROWTH))
def test_mean_cost_grows_with_size(fragment: str) -> None:
    module = _load(fragment)
    parameters, sizes = GROWTH[fragment]
    means = [
        statistics.mean(_stated_cost(module.make_problem(**parameters(size), seed=seed)) for seed in SEEDS)
        for size in sizes
    ]
    assert means == sorted(means) and len(set(means)) == len(means), (fragment, means)
