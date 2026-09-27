import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.pathwaysmetric import generator
from pypddl_datasets.generators.numeric.ipc.pathwaysmetric.generator import main, make_problem


@pytest.mark.parametrize("reactions,goals,seed", [(12, 1, 2004), (72, 6, 387462), (240, 20, 78854)])
def test_pathways_metric_quantities_and_goals(reactions: int, goals: int, seed: int, tmp_path: Path) -> None:
    problem = make_problem(reactions, goals, seed=seed)
    assert problem == make_problem(reactions, goals, seed=seed)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    for reaction in re.findall(r"\n\t\(((?:catalyzed-)?(?:self-)?association|synthesis)-reaction ([^)]*)\)", init):
        kind, args = reaction
        assert re.search(rf"\(= \(prod-by-{kind} {re.escape(args)}\) [1-4]\)", init)
        assert re.search(rf"\(= \(duration-{kind}-reaction {re.escape(args)}\) \d\.\d\)", init)
    needs = [
        int(v)
        for v in re.findall(r"\(= \(need-for-(?:association|catalyzed-association|synthesis) [^)]*\) (\d+)\)", init)
    ]
    assert needs and set(needs) <= {1, 2, 3, 4}
    thresholds = [int(k) for k in re.findall(r"\(>= \(\+ \(available \S+\) \(available \S+\)\) (\d+)\)", goal)]
    assert len(thresholds) == goals and all(2 <= k <= 8 for k in thresholds)
    assert "(= (num-subs) 0)" in init
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_self_catalysed_association_becomes_self_association() -> None:
    # reactions.txt has one "x [ x ]> y" reaction; some seed reaches it
    problems = [make_problem(300, 1, seed=s) for s in range(6)]
    assert any("(catalyzed-self-association-reaction cdk7-cych cdk7p1-cych)" in p for p in problems)
    for p in problems:
        for v in re.findall(r"\(= \(need-for-catalyzed-self-association [^)]*\) (\d+)\)", p):
            assert 2 <= int(v) <= 8


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-R", "24", "-G", "2", "-s", "1146"]) == 0
    assert capsys.readouterr().out == make_problem(24, 2, seed=1146)
    with pytest.raises(ValueError, match="num_goals"):
        make_problem(12, 0)
