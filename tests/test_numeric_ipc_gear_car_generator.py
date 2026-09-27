import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.gear_car import generator
from pypddl_datasets.generators.numeric.ipc.gear_car.generator import main, make_problem

DATA = Path(__file__).resolve().parents[1] / "data/numeric/ipc2026/gear-car"


def _match(pattern: str, text: str, flags: int = 0) -> re.Match[str]:
    match = re.search(pattern, text, flags)
    assert match is not None, pattern
    return match


def fluents(text: str) -> dict[str, str]:
    return dict(re.findall(r"\(= \(([\w ]+)\) (-?\d+)\)", text.lower().split("(:goal")[0]))


@pytest.mark.parametrize("task", ["p01", "p06", "p11", "p16"])
def test_gear_car_reproduces_ipc_gear_tables_and_fuel(task: str) -> None:
    ref = (DATA / f"{task}.pddl").read_text().lower()
    n = len(re.findall(r"\bg\d+\b", ref.split("(:init")[0]))
    distance = int(_match(r">= \(d\) (\d+)", ref).group(1))
    ours, theirs = fluents(make_problem(n, distance)), fluents(ref)
    assert {k: v for k, v in ours.items() if k not in ("alpha", "beta")} == {
        k: v for k, v in theirs.items() if k not in ("alpha", "beta")
    }
    assert abs(int(ours["beta"]) - int(theirs["beta"])) <= 2
    assert int(ours["alpha"]) == int(ours["beta"]) * (int(ours["fuel"]) + 1)


def test_gear_car_parses_and_cli(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    problem = make_problem(3, 100)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
    assert main(["-g", "3", "-d", "100"]) == 0
    assert capsys.readouterr().out == problem
    with pytest.raises(ValueError, match="num_gears"):
        make_problem(1, 100)
