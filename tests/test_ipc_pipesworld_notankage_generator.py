import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.pipesworld_notankage.generator import make_problem as make_autoscale
from pypddl_datasets.generators.classical.ipc.pipesworld_notankage import generator
from pypddl_datasets.generators.classical.ipc.pipesworld_notankage.generator import main, make_problem


@pytest.mark.parametrize("network,num_batches,num_goals", [(1, 3, 1), (1, 14, 8), (3, 20, 8), (5, 30, 8)])
def test_pipesworld_notankage_structure(network: int, num_batches: int, num_goals: int, tmp_path: Path) -> None:
    problem = make_problem(network, num_batches, num_goals, seed=7)
    assert problem == make_problem(network, num_batches, num_goals, seed=7) == make_autoscale(
        network, num_batches, num_goals, seed=7
    )
    assert "tank-slot" not in problem and "occupied" not in problem
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    starts = dict(re.findall(r"\(on (\S+) (\S+)\)", init))
    goals = dict(re.findall(r"\(on (\S+) (\S+)\)", goal))
    assert len(re.findall(r"\(is-product ", init)) == num_batches
    assert len(goals) == num_goals and all(starts.get(b) != a for b, a in goals.items())
    assert "(normal" not in goal

    path = tmp_path / "p.pddl"
    path.write_text(problem, encoding="utf-8")
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(path)


def test_pipesworld_notankage_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-n", "2", "-b", "10", "-g", "2", "--seed", "1"]) == 0
    assert capsys.readouterr().out == make_problem(2, 10, 2, seed=1)
    with pytest.raises(SystemExit):
        main(["-n", "2", "-b", "10", "-g", "2", "-t", "50"])  # no tankage option
    with pytest.raises(ValueError, match="network"):
        make_problem(0, 10, 2)
