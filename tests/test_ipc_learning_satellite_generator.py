from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.satellite import generator
from pypddl_datasets.generators.classical.ipc_learning.satellite.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/satellite_ipc2023_learning/domain.pddl"


def test_domain_file_is_the_learning_track_file():
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed, tmp_path):
    problem = make_problem(*(2, 3, 3, 5, 4, 0.5), seed=seed)
    assert problem == make_problem(*(2, 3, 3, 5, 4, 0.5), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["2", "3", "3", "5", "4", "0.5", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(2, 3, 3, 5, 4, 0.5), seed=3)


@pytest.mark.parametrize("may_hold", [True, False])
def test_pointing_goal_option(may_hold, tmp_path):
    import re

    def holds(text):
        init, goal = text.split("(:init")[1].split("(:goal")
        return any(f"(pointing {s} {d})" in init for s, d in re.findall(r"\(pointing (\S+) (\S+)\)", goal))

    tasks = [make_problem(3, 3, 2, 2, 2, 1.0, seed=s, pointing_goal_may_hold=may_hold) for s in range(40)]
    assert any(map(holds, tasks)) == may_hold
    (tmp_path / "p.pddl").write_text(tasks[0])
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]
