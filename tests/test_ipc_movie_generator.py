import re
from pathlib import Path

import pytest

from pypddl_datasets.generators.classical.ipc.movie.generator import main, make_problem

IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks/movie"


def _facts(problem: str):
    return sorted(re.findall(r"\([a-z-]+(?: [a-z0-9]+)?\)", problem.lower().split("(:init", 1)[1]))


@pytest.mark.parametrize("index", [1, 17, 30])
def test_movie_reproduces_ipc_tasks(index: int) -> None:
    assert _facts(make_problem(index + 4)) == _facts((IPC / f"prob{index:02d}.pddl").read_text())


def test_movie_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-n", "3"]) == 0
    assert capsys.readouterr().out == make_problem(3)
    with pytest.raises(ValueError, match="num_snacks"):
        make_problem(0)
