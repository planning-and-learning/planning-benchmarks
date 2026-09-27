import re
from typing import Any

import pytest

from pypddl_datasets.generators.classical.autoscale.logistics.generator import main, make_problem


def _search(pattern: str, text: str) -> re.Match[str]:
    match = re.search(pattern, text)
    assert match is not None, pattern
    return match


@pytest.mark.parametrize(
    "cities,city_size,packages,airplanes,trucks",
    [(1, 1, 1, 0, None), (2, 3, 4, 1, None), (8, 15, 3, 5, None), (3, 2, 5, 2, 7)],
)
def test_logistics_trucks_cover_every_city_and_planes_start_at_airports(
    cities: int, city_size: int, packages: int, airplanes: int, trucks: None | int
) -> None:
    problem = make_problem(cities, city_size, packages, airplanes, trucks, seed=8)
    assert problem == make_problem(cities, city_size, packages, airplanes, trucks, seed=8)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    num_trucks = cities if trucks is None else trucks
    in_city = dict(re.findall(r"\(in-city ([\w-]+) (\w+)\)", init))
    assert len(in_city) == cities * city_size
    airports = set(re.findall(r"\(airport ([\w-]+)\)", init))
    assert airports == {f"l{c}-0" for c in range(cities)}

    at = dict(re.findall(r"\(at (\w+) ([\w-]+)\)", init))
    assert [in_city[at[f"t{i}"]] for i in range(cities)] == [f"c{i}" for i in range(cities)]
    assert len([name for name in at if name.startswith("t")]) == num_trucks
    assert all(at[f"a{i}"] in airports for i in range(airplanes))
    goals = dict(re.findall(r"\(at (p\d+) ([\w-]+)\)", goal))
    assert set(goals) == {f"p{i}" for i in range(packages)} and set(goals.values()) <= set(in_city)


def test_logistics_goals_may_already_hold_as_upstream() -> None:
    # 1 city x 2 locations: upstream draws destinations independently of origins.
    problems = [make_problem(1, 2, 1, 0, seed=seed) for seed in range(40)]
    held = [
        _search(r"\(at p0 ([\w-]+)\)", p.split("(:goal")[0]).group(1)
        == _search(r"\(at p0 ([\w-]+)\)", p.split("(:goal")[1]).group(1)
        for p in problems
    ]
    assert any(held) and not all(held)


def test_logistics_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-c", "3", "-s", "2", "-p", "4", "-a", "1", "-t", "4", "-r", "9"]) == 0
    assert capsys.readouterr().out == make_problem(3, 2, 4, 1, num_trucks=4, seed=9)


@pytest.mark.parametrize(
    "parameter,value",
    [("num_cities", 0), ("city_size", 0), ("num_packages", 0), ("num_airplanes", -1), ("num_trucks", 1)],
)
def test_logistics_rejects_invalid_parameters(parameter: str, value: int) -> None:
    parameters: dict[str, Any] = {"num_cities": 2, "city_size": 2, "num_packages": 1, "num_airplanes": 1}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
