import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.drone import generator
from pypddl_datasets.generators.numeric.ipc.drone.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023/drone"
norm = lambda text: re.sub(r"\s+", " ", re.sub(r";[^\n]*", "", text.lower())).strip()  # noqa: E731


@pytest.mark.parametrize("index", range(1, 21))
def test_drone_reproduces_ipc_task(index):
    task = (REFERENCE / f"pfile{index}.pddl").read_text()
    x, y, z = map(int, re.search(r"with (\d+)x(\d+)x(\d+)", task).groups())
    assert norm(make_problem(x, y, z)) == norm(task)


def test_drone_parses_strictly(tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(3, 2, 2))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_drone_cli_and_validation(capsys):
    assert main(["2", "3", "1"]) == 0
    assert capsys.readouterr().out == make_problem(2, 3, 1)
    with pytest.raises(ValueError, match="size_z"):
        make_problem(1, 1, 0)
