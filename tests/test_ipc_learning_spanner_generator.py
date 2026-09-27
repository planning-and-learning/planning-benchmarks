from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.spanner import generator
from pypddl_datasets.generators.classical.ipc_learning.spanner.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = (
    Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/spanner_ipc2023_learning/domain.pddl"
)


def test_domain_file_is_the_learning_track_file() -> None:
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed: int, tmp_path: Path) -> None:
    problem = make_problem(*(3, 2, 5), seed=seed)
    assert problem == make_problem(*(3, 2, 5), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["3", "2", "5", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(3, 2, 5), seed=3)
