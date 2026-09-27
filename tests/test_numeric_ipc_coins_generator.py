import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.coins import generator
from pypddl_datasets.generators.numeric.ipc.coins.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2026/coins"


def init_and_goal(text):
    text = text.lower()
    return sorted(re.findall(r"\([^()]*(?:\([^()]*\)[^()]*)*\)", text.split("(:init")[1].split("(:goal")[0])), text.split("(:goal")[1].split()


@pytest.mark.parametrize("path", sorted(REFERENCE.glob("pfile*.pddl")), ids=lambda p: p.name)
def test_every_reference_task_is_reproduced(path):
    reference = path.read_text()
    target = int(re.search(r"\(= \(current-value\) (\d+)\)", reference.split("(:goal")[1]).group(1))
    assert init_and_goal(make_problem(target)) == init_and_goal(reference)


def test_parses_strictly_and_cli(tmp_path, capsys):
    (tmp_path / "p.pddl").write_text(make_problem(100, (1, 4, 9)))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
    assert main(["-t", "100", "-d", "1", "4", "9"]) == 0
    assert capsys.readouterr().out == make_problem(100, (1, 4, 9))
    with pytest.raises(ValueError, match="denominations"):
        make_problem(10, (2, 3))
