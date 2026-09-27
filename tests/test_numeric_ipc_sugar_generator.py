import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.sugar import generator
from pypddl_datasets.generators.numeric.ipc.sugar.generator import main, make_problem


@pytest.mark.parametrize("num_mills,num_goals", [(2, 1), (3, 1), (3, 5), (3, 10)])
@pytest.mark.parametrize("seed", range(3))
def test_goals_are_producible_and_fit_the_cane(num_mills, num_goals, seed):
    problem = make_problem(num_mills, num_goals, seed)
    assert problem == make_problem(num_mills, num_goals, seed)
    init, goal = problem.split("(:init")[1].split("(:goal")
    produce = set(re.findall(r"\(produce ([^\s)]+) ([^\s)]+)\)", init))
    stored = set(re.findall(r"\(=\(in-storage ([^\s)]+) ([^\s)]+)\)", init))
    producible = {b for m, b in produce if (m, b) in stored}
    goals = re.findall(r"\(>=\(in-storage ([^\s)]+) ([^\s)]+)\)(\d+)\)", goal)
    assert len(goals) == num_goals == len({(loc, b) for loc, b, _ in goals})
    assert all(b in producible and (loc, b) in stored for loc, b, _ in goals)
    cane = sum(int(x) for x in re.findall(r"\(=\(has-resource sugar-cane [^\s)]+\)(\d+)\)", init))
    harvest = int(re.search(r"\(=\(unharvest-field\)(\d+)\)", init).group(1))
    assert sum(int(a) for *_, a in goals) <= cane + 5 * harvest


def test_parses_strictly_and_cli(tmp_path, capsys):
    options = ParserOptions()
    options.strict = True
    for mills in (2, 3):
        (tmp_path / f"p{mills}.pddl").write_text(make_problem(mills, 3, 1))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / f"p{mills}.pddl")
    assert main(["-m", "3", "-g", "2", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem(3, 2, 4)
    with pytest.raises(ValueError, match="num_mills"):
        make_problem(4, 1)
