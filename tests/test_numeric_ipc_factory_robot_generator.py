import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.factory_robot import generator
from pypddl_datasets.generators.numeric.ipc.factory_robot.generator import main, make_problem


@pytest.mark.parametrize("robots,stations,workload,max_temp", [(2, 5, 40, 20), (6, 9, 70, 30), (12, 14, 130, 50)])
def test_factory_robot_structure(robots, stations, workload, max_temp, tmp_path):
    problem = make_problem(robots, stations, workload, max_temp, seed=5)
    assert problem == make_problem(robots, stations, workload, max_temp, seed=5)
    at = dict(re.findall(r"\(at (r\d+) (\S+)\)", problem))
    assert len(at) == robots and len(set(at.values())) == robots
    assert len(re.findall(r"\(connected ", problem)) == stations * (stations - 1)
    assert len(re.findall(r"\(free ", problem)) == stations - robots
    caps = [int(v) for v in re.findall(r"\(= \(capacity r\d+\) (\d+)\)", problem)]
    energy = [int(v) for v in re.findall(r"\(= \(energy r\d+\) (\d+)\)", problem)]
    assert all(c - 20 <= e <= c for c, e in zip(caps, energy))
    targets = [int(v) for v in re.findall(r"\(>= \(workload r\d+\) (\d+)\)", problem)]
    assert len(targets) == robots and all(abs(t - workload) <= 2 for t in targets)
    assert f"(<= (temperature r0) {max_temp})" in problem
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_factory_robot_cli_and_validation(capsys):
    assert main(["--robots", "3", "--stations", "6", "--workload", "45", "--max-temp", "20", "--seed", "42"]) == 0
    assert capsys.readouterr().out == make_problem(3, 6, 45, 20, seed=42)
    with pytest.raises(ValueError, match="num_stations"):
        make_problem(4, 5)
