import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.ztalloc_sum import generator
from pypddl_datasets.generators.numeric.ipc.ztalloc_sum.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2026/ztalloc-sum"


def _match(pattern: str, text: str, flags: int = 0) -> re.Match[str]:
    match = re.search(pattern, text, flags)
    assert match is not None, pattern
    return match


def _norm(text: str):
    return re.sub(r"\s+", " ", text).strip().lower()


@pytest.mark.parametrize("index", range(1, 21))
def test_reproduces_reference_task(index: int) -> None:
    reference = (REFERENCE / f"pfile{index}.pddl").read_text()
    registers = len(re.findall(r"\br\d+\b", reference.split(":objects")[1].split(")")[0]))
    target = int(_match(r"\) (\d+)\)\s*\(free\)", reference).group(1))
    assert _norm(make_problem(registers, target, name=f"p{index}")) == _norm(reference)


def test_random_target_is_deterministic_and_in_range() -> None:
    problem = make_problem(4, min_target=10, max_target=20, seed=3)
    assert problem == make_problem(4, min_target=10, max_target=20, seed=3)
    assert 10 <= int(_match(r"\(value r4\)\) (\d+)\)", problem).group(1)) <= 20


def test_parses_strictly(tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(5, seed=1))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-r", "3", "-t", "187"]) == 0
    assert capsys.readouterr().out == make_problem(3, 187)
    kwargs: dict[str, Any]
    for kwargs in (
        {"num_registers": 0},
        {"num_registers": 2, "target": 0},
        {"num_registers": 2, "min_target": 5, "max_target": 4},
    ):
        with pytest.raises(ValueError):
            make_problem(**kwargs)
