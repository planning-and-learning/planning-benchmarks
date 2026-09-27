import re
from pathlib import Path
from typing import Any
import importlib

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.barman.generator import main, make_problem
from pypddl_datasets.generators.classical.ipc.barman import generator


def _search(pattern: str, text: str) -> re.Match[str]:
    match = re.search(pattern, text)
    assert match is not None, pattern
    return match


@pytest.mark.parametrize("num_cocktails,num_ingredients,num_shots", [(1, 2, 2), (3, 4, 5), (5, 6, 10)])
def test_each_cocktail_served_once_then_random_extras(num_cocktails: int, num_ingredients: int, num_shots: int) -> None:
    problem = make_problem(num_cocktails, num_ingredients, num_shots, seed=3)
    assert problem == make_problem(num_cocktails, num_ingredients, num_shots, seed=3)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    served = re.findall(r"\(contains shot(\d+) (\w+)\)", goal)
    assert [int(shot) for shot, _ in served] == list(range(1, num_shots))
    first = [beverage for _, beverage in served[:num_cocktails]]
    assert sorted(first) == sorted(f"cocktail{i}" for i in range(1, num_cocktails + 1))
    beverages = {f"cocktail{i}" for i in range(1, num_cocktails + 1)} | {
        f"ingredient{i}" for i in range(1, num_ingredients + 1)
    }
    assert {beverage for _, beverage in served} <= beverages
    for cocktail in range(1, num_cocktails + 1):
        part1 = _search(rf"\(cocktail-part1 cocktail{cocktail} (\w+)\)", init).group(1)
        part2 = _search(rf"\(cocktail-part2 cocktail{cocktail} (\w+)\)", init).group(1)
        assert part1 != part2
    assert "total-cost" not in problem  # IPC 2014 encoding


def test_extra_shots_mix_cocktails_and_ingredients() -> None:
    extras = [
        beverage
        for seed in range(20)
        for beverage in re.findall(r"\(contains shot(?:[4-9]|1\d) (\w+)\)", make_problem(3, 4, 12, seed=seed))
    ]
    assert any(b.startswith("cocktail") for b in extras) and any(b.startswith("ingredient") for b in extras)


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--num-cocktails", "2", "--num-ingredients", "3", "--num-shots", "4", "--seed", "5"]) == 0
    assert capsys.readouterr().out == make_problem(2, 3, 4, seed=5)


@pytest.mark.parametrize(
    "parameter,value", [("num_cocktails", 0), ("num_ingredients", 1), ("num_shots", 2), ("num_shots", True)]
)
def test_rejects_invalid_parameters(parameter: str, value: int | bool) -> None:
    parameters: dict[str, Any] = {"num_cocktails": 2, "num_ingredients": 3, "num_shots": 4}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


@pytest.mark.parametrize("tree", ["ipc", "autoscale"])
def test_output_parses_against_package_domain(tree: str, tmp_path: Path) -> None:
    module = importlib.import_module(f"pypddl_datasets.generators.classical.{tree}.barman.generator")
    problem = module.make_problem(3, 4, 6, seed=1)
    assert ("(:metric minimize (total-cost))" in problem) == (tree == "autoscale")
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    assert module.__file__ is not None
    Parser(Path(module.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_action_costs_output_parses_against_ipc_2011_domain(tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(3, 4, 6, seed=1, action_costs=True))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain_barman11.pddl"), options).parse_task(tmp_path / "p.pddl")
