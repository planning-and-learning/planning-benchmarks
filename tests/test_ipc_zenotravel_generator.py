import re
from typing import Any

import pytest

from pypddl_datasets.generators.classical.autoscale.zenotravel.generator import make_problem as make_typed
from pypddl_datasets.generators.classical.ipc.zenotravel.generator import main, make_problem


@pytest.mark.parametrize("num_cities,num_planes,num_people", [(1, 1, 1), (3, 2, 5), (17, 6, 5)])
def test_zenotravel_planes_can_always_refuel_and_reach_every_city(
    num_cities: int, num_planes: int, num_people: int
) -> None:
    problem = make_problem(num_cities, num_planes, num_people, seed=5)
    assert problem == make_problem(num_cities, num_planes, num_people, seed=5)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    cities = {f"city{i}" for i in range(num_cities)}
    planes = {f"plane{i}" for i in range(1, num_planes + 1)}
    people = {f"person{i}" for i in range(1, num_people + 1)}

    # Every plane starts empty-tanked on a full fuel chain; refuel works anywhere,
    # so any plane can fly any person anywhere.
    assert set(re.findall(r"\(fuel-level (\w+) (\w+)\)", init)) == {(plane, "fl0") for plane in planes}
    assert re.findall(r"\(next (\w+) (\w+)\)", init) == [(f"fl{i}", f"fl{i + 1}") for i in range(6)]
    starts = dict(re.findall(r"\(at (\w+) (\w+)\)", init))
    assert set(starts) == planes | people and set(starts.values()) <= cities
    goals = dict(re.findall(r"\(at (\w+) (\w+)\)", goal))
    assert set(goals) <= planes | people and set(goals.values()) <= cities


def test_zenotravel_goal_probabilities_follow_upstream() -> None:
    goals = [make_problem(5, 20, 20, seed=seed).split("(:goal", 1)[1] for seed in range(50)]
    plane_rate = sum(len(re.findall(r"\(at plane", goal)) for goal in goals) / 1000
    person_rate = sum(len(re.findall(r"\(at person", goal)) for goal in goals) / 1000
    assert 0.25 < plane_rate < 0.35
    assert person_rate > 0.94


def test_zenotravel_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-c", "4", "-a", "2", "-p", "3", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2, 3, seed=9)


@pytest.mark.parametrize(
    "parameter,value", [("num_cities", 0), ("num_planes", 0), ("num_people", 0), ("num_people", 1.5)]
)
def test_zenotravel_rejects_invalid_parameters(parameter: str, value: float) -> None:
    parameters: dict[str, Any] = {"num_cities": 3, "num_planes": 1, "num_people": 1}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


def test_zenotravel_encodings_and_distance_fuel() -> None:
    untyped, typed = make_problem(3, 2, 2, seed=1), make_typed(3, 2, 2, seed=1)
    assert "(aircraft plane1)" in untyped and "(flevel fl6)" in untyped and " - " not in untyped
    assert "plane1 - aircraft" in typed and "(aircraft " not in typed
    fuels = {
        level
        for seed in range(20)
        for level in re.findall(r"\(fuel-level \w+ (\w+)\)", make_problem(2, 5, 1, seed=seed, distance=100))
    }
    assert len(fuels) > 1 and fuels <= {f"fl{i}" for i in range(7)}
