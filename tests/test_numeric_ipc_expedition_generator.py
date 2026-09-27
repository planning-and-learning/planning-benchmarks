import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.expedition import generator
from pypddl_datasets.generators.numeric.ipc.expedition.generator import main, make_problem

DATA = Path(__file__).resolve().parents[1] / "data/numeric"


def facts(text: str):
    text = re.sub(r"\s+", " ", re.sub(r";[^\n]*", "", text.lower()))
    init, goal = text.split("(:init", 1)[1].split("(:goal", 1)
    return sorted(re.findall(r"\(= \([^()]*\) \d+\)|\([^()=]*\)", init)), sorted(re.findall(r"\([^()]*\)", goal))


@pytest.mark.parametrize("year", ["ipc2023", "ipc2026"])
@pytest.mark.parametrize("index", range(1, 21))
def test_expedition_reproduces_ipc_task(year: str, index: int) -> None:
    task = (DATA / year / "expedition" / f"pfile{index}.pddl").read_text()
    num_waypoints = len(re.findall(r"\bwa\d+\b", task.split("(:init")[0]))
    assert facts(make_problem(num_waypoints, separate_tracks="wb0" in task)) == facts(task)


@pytest.mark.parametrize("separate", [False, True])
def test_expedition_parses_strictly(separate: bool, tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(4, 3, separate_tracks=separate))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_expedition_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["7", "--separate-tracks"]) == 0
    assert capsys.readouterr().out == make_problem(7, separate_tracks=True)
    parameters: tuple[Any, ...]
    for parameters, name in (((1,), "num_waypoints"), ((5, 0), "num_sleds")):
        with pytest.raises(ValueError, match=name):
            make_problem(*parameters)
    with pytest.raises(ValueError, match="initial_supplies"):
        make_problem(5, initial_supplies=5)
