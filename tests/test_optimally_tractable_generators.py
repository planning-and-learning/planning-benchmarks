"""Every optimally-tractable fragment generator yields strictly parsing tasks annotated with their optimal cost.

The closed-form costs were checked against A* with LM-cut on small tasks; this test
only guards the files and their output format. The fragment directory has a hyphen,
so modules are loaded by path.
"""

import importlib.util
import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

ROOT = Path(__file__).resolve().parents[1] / "src/pypddl_datasets/generators/classical/optimally-tractable"
SAMPLES: dict[str, dict[str, Any]] = {
    "blocks_3/clear_block.py": {"num_blocks": 6, "seed": 1},
    "blocks_3/clear_blocks.py": {"num_blocks": 6, "seed": 1},
    "blocks_3/goal_on_table.py": {"num_blocks": 6, "seed": 1},
    "blocks_3/init_on_table.py": {"num_blocks": 6, "seed": 1},
    "blocks_3/on_pair.py": {"num_blocks": 6, "seed": 1},
    "blocks_3/table_blocks.py": {"num_blocks": 6, "seed": 1},
    "blocks_4/clear_block.py": {"num_blocks": 6, "seed": 1},
    "blocks_4/clear_blocks.py": {"num_blocks": 6, "seed": 1},
    "blocks_4/goal_on_table.py": {"num_blocks": 6, "seed": 1},
    "blocks_4/init_on_table.py": {"num_blocks": 6, "seed": 1},
    "blocks_4/on_pair.py": {"num_blocks": 6, "seed": 1},
    "blocks_4/table_blocks.py": {"num_blocks": 6, "seed": 1},
    "childsnack/exact_ingredients.py": {"num_children": 4, "num_trays": 2, "gluten_factor": 0.5, "seed": 1},
    "delivery/common_destination.py": {"grid_size": 4, "num_packages": 3, "seed": 1},
    "delivery/common_route.py": {"grid_size": 4, "num_trucks": 2, "num_packages": 3, "seed": 1},
    "elevators/common_destination.py": {"num_floors": 6, "num_passengers": 3, "seed": 1},
    "elevators/common_origin.py": {"num_floors": 6, "num_passengers": 3, "kind": "fast", "seed": 1},
    "ferry/common_origin.py": {"num_cars": 4, "num_locations": 3, "seed": 1},
    "ferry/unrestricted.py": {"num_cars": 4, "num_locations": 3, "seed": 1},
    "floortile/single_column.py": {"num_rows": 4, "seed": 1},
    "goldminer/standard.py": {"num_rows": 3, "num_cols": 4, "seed": 1},
    "grid/single_key.py": {"width": 5, "height": 4, "seed": 1},
    "grid/single_key_locks.py": {"width": 5, "height": 4, "seed": 1},
    "gripper/one_way.py": {"num_balls": 5},
    "gripper/two_way.py": {"num_balls": 5, "seed": 1},
    "logistics/common_destination.py": {"num_cities": 3, "city_size": 3, "num_planes": 2, "num_packages": 4, "seed": 1},
    "logistics/common_origin.py": {"num_cities": 3, "city_size": 3, "num_planes": 2, "num_packages": 4, "seed": 1},
    "miconic/common_destination.py": {"num_floors": 5, "num_passengers": 4, "seed": 1},
    "miconic/common_origin.py": {"num_floors": 5, "num_passengers": 4, "seed": 1},
    "miconic/disjoint_floors.py": {"num_floors": 5, "num_passengers": 4, "seed": 1},
    "movie/standard.py": {"num_snacks": 3},
    "nomystery/single_package.py": {"num_locations": 5, "max_fuel": 4, "seed": 1},
    "ricochet_robots/single_robot.py": {"board_size": 5, "num_barriers": 6, "seed": 1},
    "satellite/single_instrument.py": {"num_directions": 4, "num_modes": 2, "num_images": 4, "seed": 1},
    "sokoban/single_stone.py": {"width": 5, "height": 4, "seed": 1},
    "spanner/corridor.py": {"num_spanners": 4, "num_nuts": 3, "num_locations": 4, "seed": 1},
    "tpp/exclusive_markets.py": {"num_goods": 3, "num_markets": 3, "max_level": 3, "seed": 1},
    "transport/common_destination.py": {"num_nodes": 6, "num_packages": 3, "seed": 1},
    "transport/common_route.py": {"num_nodes": 6, "num_trucks": 2, "num_packages": 3, "seed": 1},
    "visitall/full_grid.py": {"width": 4, "height": 3, "seed": 1},
    "visitall/row.py": {"num_cells": 6, "seed": 1},
    "visitall/tree_maze.py": {"width": 4, "height": 3, "seed": 1},
    "zenotravel/common_destination.py": {"num_cities": 4, "num_people": 3, "seed": 1},
    "zenotravel/common_origin.py": {"num_cities": 4, "num_people": 3, "seed": 1},
}


def test_every_fragment_has_a_sample() -> None:
    assert sorted(p.relative_to(ROOT).as_posix() for p in ROOT.glob("*/*.py")) == sorted(SAMPLES)


@pytest.mark.parametrize("fragment", sorted(SAMPLES))
def test_fragment_parses_with_cost(fragment: str, tmp_path: Path) -> None:
    spec = importlib.util.spec_from_file_location(fragment.replace("/", "."), ROOT / fragment)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    problem: str = module.make_problem(**SAMPLES[fragment])
    assert problem == module.make_problem(**SAMPLES[fragment])
    assert re.match(r"; optimal plan cost: \d+\n", problem)
    options = ParserOptions()
    options.strict = True
    path = tmp_path / "problem.pddl"
    path.write_text(problem, encoding="utf-8")
    Parser(ROOT / fragment.split("/")[0] / "domain.pddl", options).parse_task(path)
