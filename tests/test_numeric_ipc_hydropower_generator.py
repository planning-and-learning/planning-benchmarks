import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.hydropower import generator
from pypddl_datasets.generators.numeric.ipc.hydropower.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023/hydropower"


def _match(pattern: str, text: str, flags: int = 0) -> re.Match[str]:
    match = re.search(pattern, text, flags)
    assert match is not None, pattern
    return match


def facts(text: str):
    text = re.sub(r";[^\n]*", "", text.lower())
    objects = text.split("(:objects")[1].split("(:init")[0].split()
    return objects, sorted(re.findall(r"\((?:[^()]|\([^()]*\))*\)", text.split("(:init")[1]))


@pytest.mark.parametrize("path", sorted(REFERENCE.glob("pfile*.pddl")), ids=lambda p: p.name)
def test_every_reference_task_is_reproduced_for_some_seed(path: Path) -> None:
    reference = path.read_text()
    capacity = int(_match(r"stored_capacity\) (\d+)", reference).group(1))
    assert any(facts(make_problem(capacity, seed)) == facts(reference) for seed in range(20))


@pytest.mark.parametrize("capacity", [1, 3, 9, 10, 13, 53])
def test_goal_profit_is_below_the_optimum(capacity: int) -> None:
    for seed in range(5):
        problem = make_problem(capacity, seed)
        assert problem == make_problem(capacity, seed)
        goal = int(_match(r">= \(funds\) (\d+)", problem).group(1))
        assert 1000 < goal < 1000 + 22.95 * capacity  # buy at 3 (t0400), sell at 26 (t1700)


def test_parses_strictly_and_cli(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(30, 1))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
    assert main(["-c", "30", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(30, 1)
    with pytest.raises(ValueError, match="capacity"):
        make_problem(0)
