import math
import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.sailing_wind import generator
from pypddl_datasets.generators.numeric.ipc.sailing_wind.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2026/sailing-wind-opt/problem_0.pddl"


def _fluents(problem: str):
    return {(f, o): float(v) for f, o, v in re.findall(r"\(= \((\S+) (\S+)\) (\S+)\)", problem)}


def test_boat_fluents_match_reference_polar() -> None:
    reference, generated = _fluents(REFERENCE.read_text().lower()), _fluents(make_problem(seed=1))
    assert {k: v for k, v in reference.items() if k[1] == "b0"} == {k: v for k, v in generated.items() if k[1] == "b0"}


@pytest.mark.parametrize("seed", range(5))
def test_persons_at_requested_distances(seed: int) -> None:
    problem = make_problem(3, 2, min_distance=20, max_distance=40, inertia=0.9, seed=seed)
    assert problem == make_problem(3, 2, min_distance=20, max_distance=40, inertia=0.9, seed=seed)
    f = _fluents(problem)
    for p in ("p0", "p1", "p2"):
        assert 19.9 <= math.hypot(f["x", p], f["y", p]) <= 40.1
    assert f["r", "b1"] == 0.9 and re.findall(r"\(saved (\S+)\)", problem) == ["p0", "p1", "p2"]


def test_angle_step_gives_compass_directions() -> None:
    f = _fluents(make_problem(4, min_distance=100, max_distance=100, angle_step=90, seed=2))
    assert all({abs(f["x", p]), abs(f["y", p])} == {0.0, 100.0} for p in ("p0", "p1", "p2", "p3"))


def test_parses_strictly(tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(2, 2, seed=3))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-p", "2", "-r", "0.9", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem(2, inertia=0.9, seed=4)
    kwargs: dict[str, Any]
    for kwargs in ({"num_persons": 0}, {"inertia": 1.0}, {"min_distance": 5, "max_distance": 1}, {"angle_step": 0}):
        with pytest.raises(ValueError):
            make_problem(**kwargs)
