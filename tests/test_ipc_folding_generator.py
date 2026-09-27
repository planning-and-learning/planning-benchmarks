import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.folding import generator
from pypddl_datasets.generators.classical.ipc.folding.generator import main, make_problem


def _search(pattern: str, text: str) -> re.Match[str]:
    match = re.search(pattern, text)
    assert match is not None, pattern
    return match


IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def facts(text: str):
    text = re.sub(r";[^\n]*", "", text).lower()
    return set(re.findall(r"\((?:[^()]|\([^()]*\))*\)", text))


@pytest.mark.parametrize(
    "task", ["folding-opt23-adl/p01.pddl", "folding-sat23-adl/p08.pddl", "folding-opt23-adl/p20.pddl"]
)
def test_reproduces_ipc_task_from_its_generator_call(task: str) -> None:
    text = (IPC / task).read_text()
    seed, scenario, length, folds = _search(r"generate\.py (\d+) (\S+) (\d+) (\d+)", text).groups()
    assert facts(make_problem(scenario, int(length), int(folds), seed=int(seed))) == facts(text)


@pytest.mark.parametrize("scenario", ["zigzag", "spiral", "bias-spiral"])
def test_goal_is_a_self_avoiding_string(scenario: str) -> None:
    problem = make_problem(scenario, 12, 7, seed=5)
    assert problem == make_problem(scenario, 12, 7, seed=5)
    goal = problem.split("(:goal", 1)[1]
    at = [
        (int(x), int(y))
        for _, x, y in sorted(re.findall(r"\(at n(\d+) c(\d+) c(\d+)\)", goal), key=lambda f: int(f[0]))
    ]
    assert len(at) == 12 and len(set(at)) == 12
    assert all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(at, at[1:]))
    assert "(not (rotating))" in goal


def test_output_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(make_problem("bias-spiral", 10, 6, seed=2))
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["spiral", "8", "4", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem("spiral", 8, 4, seed=3)


@pytest.mark.parametrize("args", [("loop", 8, 4), ("zigzag", 1, 1), ("zigzag", 8, 0), ("zigzag", 8, 8)])
def test_rejects_invalid_parameters(args: tuple[str, int, int]) -> None:
    with pytest.raises(ValueError):
        make_problem(*args)
