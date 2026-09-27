import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.line_exchange_snp import generator
from pypddl_datasets.generators.numeric.ipc.line_exchange_snp.generator import main, make_problem


@pytest.mark.parametrize("robots,mean,spread,segment", [(3, 5, 25, 10), (4, 10, 50, 50), (5, 15, 90, 100)])
def test_line_exchange_loads_and_positions(robots: int, mean: int, spread: int, segment: int, tmp_path: Path) -> None:
    problem = make_problem(robots, mean, spread, segment, seed=2)
    assert problem == make_problem(robots, mean, spread, segment, seed=2)
    init, goal = problem.split("(:goal")
    loads = [int(q) for q in re.findall(r"\(= \(q r\d+\) (\d+)\)", init)]
    assert sum(loads) == robots * mean and len(set(loads)) > 1
    xs = [float(x) for x in re.findall(r"\(= \(x r\d+\) ([\d.]+)\)", init)]
    assert (
        xs
        == [segment * i + segment / 2 for i in range(robots)]
        == [float(x) for x in re.findall(r"\(= \(x r\d+\) ([\d.]+)\)", goal)]
    )
    assert len(re.findall(r"\(= \(q r\d+\) \(q r\d+\)\)", goal)) == robots - 1
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_line_exchange_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["3", "5", "50", "50", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(3, 5, 50, 50, seed=1)
    with pytest.raises(ValueError, match="segment"):
        make_problem(3, 5, 50, 51)
