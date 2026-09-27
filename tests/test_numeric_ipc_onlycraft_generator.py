import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.onlycraft import generator
from pypddl_datasets.generators.numeric.ipc.onlycraft.generator import main, make_problem


@pytest.mark.parametrize("sticks,trees,grid", [(1, 4, 3), (10, 35, 6), (200, 700, 27)])
def test_onlycraft_defaults_follow_ipc(sticks: int, trees: int, grid: int, tmp_path: Path) -> None:
    problem = make_problem(sticks, seed=3)
    assert problem == make_problem(sticks, seed=3)
    assert problem.count("(tree_cell ") == trees and problem.count("(air_cell ") == grid * grid - trees
    assert len(re.findall(r"\(position ", problem)) == 1 and len(re.findall(r"\(crafting_table_cell ", problem)) == 1
    assert f"(>= (count_pogo_stick) {sticks})" in problem
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_onlycraft_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-p", "3", "-g", "5", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(3, grid_size=5, seed=1)
    with pytest.raises(ValueError, match="num_trees"):
        make_problem(10, grid_size=3)
