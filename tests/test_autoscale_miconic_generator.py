import re

import pytest

from pypddl_datasets.generators.classical.autoscale.miconic.generator import main, make_problem


@pytest.mark.parametrize("num_floors,num_passengers", [(2, 1), (11, 19)])
@pytest.mark.parametrize("seed", range(3))
def test_miconic_autoscale_journeys_change_floor(num_floors: int, num_passengers: int, seed: int) -> None:
    problem = make_problem(num_floors, num_passengers, seed=seed)
    assert problem == make_problem(num_floors, num_passengers, seed=seed)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    assert len(re.findall(r"\(above ", init)) == num_floors * (num_floors - 1) // 2
    origins = dict(re.findall(r"\(origin (\w+) (\w+)\)", init))
    destins = dict(re.findall(r"\(destin (\w+) (\w+)\)", init))
    floors = {f"f{i}" for i in range(num_floors)}
    assert origins.keys() == destins.keys() == {f"p{i}" for i in range(num_passengers)}
    assert all(origins[p] != destins[p] and {origins[p], destins[p]} <= floors for p in origins)
    assert re.findall(r"\(served (\w+)\)", goal) == [f"p{i}" for i in range(num_passengers)]
    assert "(lift-at f0)" in init and "not-" not in problem


def test_miconic_autoscale_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-f", "5", "-p", "4", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(5, 4, seed=9)
    for parameters, name in (((1, 1), "num_floors"), ((2, 0), "num_passengers")):
        with pytest.raises(ValueError, match=name):
            make_problem(*parameters)
