import importlib
import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.tpp.generator import main, make_problem


@pytest.mark.parametrize("args", [(1, 1, 1, 1, 1), (2, 3, 2, 1, 7), (5, 8, 3, 4, 10)])
@pytest.mark.parametrize("seed", range(4))
def test_markets_connected_and_supply_covers_goals(args: tuple[int, int, int, int, int], seed: int) -> None:
    num_products, num_markets, num_trucks, num_depots, max_level = args
    problem = make_problem(*args, seed=seed)
    assert problem == make_problem(*args, seed=seed)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)

    roads = set(re.findall(r"\(connected (\w+) (\w+)\)", init))
    assert all((right, left) in roads for left, right in roads)
    reached, frontier = {"market1"}, ["market1"]
    while frontier:
        current = frontier.pop()
        for left, right in roads:
            if left == current and right not in reached:
                reached.add(right)
                frontier.append(right)
    assert reached == {f"market{i}" for i in range(1, num_markets + 1)} | {
        f"depot{i}" for i in range(1, num_depots + 1)
    }

    supply: dict[str, int] = {}
    for product, _, level in re.findall(r"\(on-sale (\w+) (\w+) level(\d+)\)", init):
        supply[product] = supply.get(product, 0) + int(level)
    goals = dict(re.findall(r"\(stored (\w+) level(\d+)\)", goal))
    assert set(goals) == {f"goods{i}" for i in range(1, num_products + 1)}
    assert all(1 <= int(level) <= min(supply[product], max_level) for product, level in goals.items())
    assert all(total <= max_level for total in supply.values())
    assert len(re.findall(r"\(at truck\d+ depot\d+\)", init)) == num_trucks


def test_some_roads_get_cut() -> None:
    assert any(
        len(re.findall(r"\(connected market", make_problem(1, 6, 1, 1, 3, seed=seed))) < 6 * 5 + 1 for seed in range(10)
    )


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-p", "2", "-m", "4", "-t", "2", "-d", "1", "-l", "5", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(2, 4, 2, 1, 5, seed=3)


@pytest.mark.parametrize("parameter", ["num_products", "num_markets", "num_trucks", "num_depots", "max_level"])
def test_rejects_invalid_parameters(parameter: str) -> None:
    parameters: dict[str, Any] = {"num_products": 1, "num_markets": 1, "num_trucks": 1, "num_depots": 1, "max_level": 1}
    parameters[parameter] = 0
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


@pytest.mark.parametrize("tree", ["ipc", "autoscale"])
def test_output_parses_against_package_domain(tree: str, tmp_path: Path) -> None:
    module = importlib.import_module(f"pypddl_datasets.generators.classical.{tree}.tpp.generator")
    (tmp_path / "p.pddl").write_text(module.make_problem(3, 4, 2, 1, 5, seed=1))
    options = ParserOptions()
    options.strict = True
    assert module.__file__ is not None
    Parser(Path(module.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
