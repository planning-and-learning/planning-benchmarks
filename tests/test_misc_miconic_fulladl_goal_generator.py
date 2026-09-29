from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.miconic_fulladl import generator as original
from pypddl_datasets.generators.classical.misc.miconic_fulladl_goal import generator


def test_derived_goal_preserves_the_ipc_task(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    options = ParserOptions()
    options.strict = True
    original_path = tmp_path / "original.pddl"
    original_path.write_text(original.make_problem(10, 5, seed=2), encoding="utf-8")
    original_task = Parser(Path(original.__file__).with_name("domain.pddl"), options).parse_task(original_path)

    problem = generator.make_problem(10, 5, seed=2)
    path = tmp_path / "problem.pddl"
    path.write_text(problem, encoding="utf-8")
    task = Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(path)
    [axiom] = task.get_domain().get_axioms()
    assert str(axiom.get_head()) == "(goal_satisfied)"
    assert str(axiom.get_condition()) == str(original_task.get_goal())
    assert str(task.get_goal()) == "(goal_satisfied)"
    assert [str(action) for action in task.get_domain().get_actions()] == [
        str(action) for action in original_task.get_domain().get_actions()
    ]
    assert [str(fact) for fact in task.get_initial_literals()] == [
        str(fact) for fact in original_task.get_initial_literals()
    ]
    assert generator.main(["-f", "10", "-p", "5", "-r", "2"]) == 0
    assert capsys.readouterr().out == problem
