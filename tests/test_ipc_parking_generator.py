import math
import re

import pytest

from pypddl_datasets.generators.classical.ipc.parking.generator import main, make_problem


def _layout(facts: str) -> tuple[dict[str, str], dict[str, str]]:
    return dict(re.findall(r"\(at-curb-num (\w+) (\w+)\)", facts)), dict(re.findall(r"\(behind-car (\w+) (\w+)\)", facts))


@pytest.mark.parametrize("curbs,cars", [(2, 1), (3, 4), (9, 16), (9, 14), (43, 84)])
def test_parking_initial_layout_is_valid_and_goal_is_canonical(curbs, cars):
    problem = make_problem(curbs, cars, seed=4)
    assert problem == make_problem(curbs, cars, seed=4)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    car_names = [f"car_{i:0{len(str(cars - 1))}d}" for i in range(cars)]
    curb_names = [f"curb_{i:0{len(str(curbs - 1))}d}" for i in range(curbs)]

    at_curb, behind = _layout(init)
    assert math.ceil(cars / 2) <= len(at_curb) <= min(curbs, cars)
    assert sorted([*at_curb, *behind]) == sorted(car_names)
    assert set(at_curb.values()) == set(curb_names[: len(at_curb)])
    assert set(behind.values()) <= set(at_curb) and len(set(behind.values())) == len(behind)
    assert set(re.findall(r"\(at-curb (\w+)\)", init)) == set(at_curb)
    assert set(re.findall(r"\(car-clear (\w+)\)", init)) == set(behind) | (set(at_curb) - set(behind.values()))
    assert set(re.findall(r"\(curb-clear (\w+)\)", init)) == set(curb_names[len(at_curb):])

    goal_curb, goal_behind = _layout(goal)
    front = min(curbs, cars)
    assert goal_curb == {car_names[i]: curb_names[i] for i in range(front)}
    assert goal_behind == {car_names[i]: car_names[i - front] for i in range(front, cars)}
    assert "(= (total-cost) 0)" in init and "(:metric minimize (total-cost))" in problem


def test_parking_cli_matches_make_problem(capsys):
    assert main(["-c", "5", "-n", "7", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(5, 7, seed=9)


@pytest.mark.parametrize("parameter,value", [("num_curbs", 1), ("num_cars", 0), ("num_cars", 9), ("num_cars", True)])
def test_parking_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_curbs=5, num_cars=4)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
