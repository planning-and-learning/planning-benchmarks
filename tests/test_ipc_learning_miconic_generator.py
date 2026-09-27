from pathlib import Path
import re

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.miconic import generator
from pypddl_datasets.generators.classical.ipc_learning.miconic.generator import main, make_problem


def _search(pattern: str, text: str) -> re.Match[str]:
    match = re.search(pattern, text)
    assert match is not None, pattern
    return match


DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = (
    Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/miconic_ipc2023_learning/domain.pddl"
)


def test_domain_file_is_the_learning_track_file() -> None:
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed: int, tmp_path: Path) -> None:
    problem = make_problem(*(5, 4), seed=seed)
    assert problem == make_problem(*(5, 4), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["5", "4", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(5, 4), seed=3)


@pytest.mark.parametrize("lift_start", ["random", "bottom"])
def test_lift_start_option(lift_start: str, tmp_path: Path) -> None:
    floors = {
        _search(r"\(lift-at (\S+)\)", make_problem(8, 3, seed=s, lift_start=lift_start)).group(1) for s in range(40)
    }
    assert floors == {"f0"} if lift_start == "bottom" else len(floors) > 3
    (tmp_path / "p.pddl").write_text(make_problem(8, 3, seed=1, lift_start=lift_start))
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")
