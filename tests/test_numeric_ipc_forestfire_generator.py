import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.forestfire import generator
from pypddl_datasets.generators.numeric.ipc.forestfire.generator import main, make_problem


def parse(problem: str, tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


@pytest.mark.parametrize("width,height,bots,axes,extra_trees", [(3, 3, 1, 1, 0), (5, 6, 2, 2, 3), (9, 7, 3, 2, 10)])
def test_forestfire_layout(width, height, bots, axes, extra_trees, tmp_path):
    problem = make_problem(width, height, bots, axes, fire_rows=2 if height > 4 else 1, extra_trees=extra_trees, seed=7)
    assert problem == make_problem(width, height, bots, axes, fire_rows=2 if height > 4 else 1, extra_trees=extra_trees, seed=7)
    mid = (width + 1) // 2
    bushes = set(re.findall(r"\(= \(max-water (\S+)\) 1\)", problem))
    assert bushes == {f"bushes{x}_2" for x in range(1, width + 1) if x != mid}
    assert len(re.findall(r"\(connected ", problem)) == 2 * ((width - 1) * height + width * (height - 1))
    assert f"(= (tree grass{mid}_2) 6)" in problem
    fires = dict(re.findall(r"\(= \(fire (\S+)\) (\d+)\)", problem.split("(:goal")[0]))
    burning = {c for c, v in fires.items() if v != "0"}
    assert burning and burning == set(re.findall(r"\(= \(fire (\S+)\) 0\)", problem.split("(:goal")[1]))
    assert all(int(c.split("_")[1]) > height - (2 if height > 4 else 1) for c in burning)
    assert re.findall(r"\(pond (\S+)\)", problem) == ["grass1_1", f"grass{width}_1"]
    assert "(:metric minimize (cost))" in problem
    parse(problem, tmp_path)


def test_forestfire_cli_and_validation(capsys):
    assert main(["-x", "5", "-y", "4", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(5, 4, seed=3)
    for kwargs in (dict(width=4, height=4), dict(width=3, height=3, fire_rows=2), dict(width=3, height=3, num_bots=4)):
        with pytest.raises(ValueError):
            make_problem(**kwargs)
