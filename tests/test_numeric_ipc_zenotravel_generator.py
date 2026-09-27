import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.zenotravel import generator
from pypddl_datasets.generators.numeric.ipc.zenotravel.generator import main, make_problem


@pytest.mark.parametrize("cities,planes,people,distance", [(1, 1, 1, 1000), (3, 2, 5, 1000), (25, 5, 40, 50)])
def test_zenotravel_numeric_values_follow_zenogenerator(cities: int, planes: int, people: int, distance: int) -> None:
    problem = make_problem(cities, planes, people, seed=4, distance=distance)
    assert problem == make_problem(cities, planes, people, seed=4, distance=distance)
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    distances = {(a, b): int(d) for a, b, d in re.findall(r"\(= \(distance (\w+) (\w+)\) (\d+)\)", init)}
    assert len(distances) == cities * cities
    assert all(
        d == 0 if a == b else distance // 2 <= d < distance and distances[b, a] == d for (a, b), d in distances.items()
    )
    for plane in range(1, planes + 1):
        value = {k: int(v) for k, v in re.findall(rf"\(= \(([a-z-]+) plane{plane}\) (\d+)\)", init)}
        assert 1 <= value["slow-burn"] <= 5 and 1 <= value["zoom-limit"] <= 10 and value["onboard"] == 0
        assert value["fuel"] < value["slow-burn"] * distance < value["capacity"]
        assert 2 * value["slow-burn"] <= value["fast-burn"] <= 4 * value["slow-burn"]
    assert "(= (total-fuel-used) 0)" in init and "(= (total-time) 0)" in init
    assert re.search(
        r"\(:metric minimize \(\+ \(\* [1-5] \(total-time\)\) \(\* [1-5] \(total-fuel-used\)\)\)\)", problem
    )


def test_fuel_metric_and_strict_parse(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    for metric in ("weighted", "fuel"):
        (tmp_path / "p.pddl").write_text(make_problem(4, 2, 5, seed=1, metric=metric))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
    assert "(:metric minimize (total-fuel-used))" in make_problem(2, 1, 1, seed=1, metric="fuel")


def test_goal_probabilities_follow_upstream() -> None:
    goals = [make_problem(5, 20, 20, seed=seed).split("(:goal", 1)[1] for seed in range(50)]
    assert 0.25 < sum(g.count("(located plane") for g in goals) / 1000 < 0.35
    assert sum(g.count("(located person") for g in goals) / 1000 > 0.94


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-c", "3", "-a", "2", "-p", "4", "-s", "5", "-m", "fuel"]) == 0
    assert capsys.readouterr().out == make_problem(3, 2, 4, seed=5, metric="fuel")
    with pytest.raises(ValueError, match="num_planes"):
        make_problem(3, 0, 1)
    with pytest.raises(ValueError, match="metric"):
        make_problem(3, 1, 1, metric="time")
