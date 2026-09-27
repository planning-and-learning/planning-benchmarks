import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.petri_net import generator
from pypddl_datasets.generators.numeric.ipc.petri_net.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2026/petri-net"
NET = {"06": "mesh", "07": "pipeline", "08": "mesh", "09": "merge", "10": "merge"}


def _init(text: str) -> set[str]:
    init = text.lower().split("(:init")[1].split("(:goal")[0]
    return {re.sub(r"\s+", " ", x) for x in re.findall(r"\((?:[a-z-]+ [^()]*|= \(\w+(?: \S+)?\) \d+)\)", init)}


def _goal(text: str) -> list[str]:
    goal = text.lower().split("(:goal")[1].split("(:metric")[0]
    return sorted(
        re.sub(r"\s+", " ", g).strip()
        for g in re.findall(r"\((?:=|<=) (?:[^()]|\([^()]*\)|\((?:[^()]|\([^()]*\))*\))*\)", goal)
    )


@pytest.mark.parametrize("path", sorted(REFERENCE.glob("prob*.pddl")), ids=lambda p: p.stem)
def test_reference_task_is_in_support(path: Path) -> None:
    reference = path.read_text()
    net = NET[path.stem[4:6]]
    assert _init(make_problem(net, seed=0)) == _init(reference)
    goals = {tuple(_goal(make_problem(net, seed=seed))) for seed in range(300)}
    assert tuple(_goal(reference)) in goals


def test_chain_length_scales_the_net() -> None:
    problem = make_problem("mesh", chain_length=5, goal="hubs", seed=1)
    assert "(one-to-one a5 a6)" in problem and "(three-to-one a7 a8 a9 a10)" in problem
    assert re.search(r"\(= \(value a6\) [12]\)", problem)


def test_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    cases: tuple[dict[str, Any], ...] = (
        {"net": "mesh", "chain_length": 6},
        {"net": "pipeline"},
        {"net": "merge", "chain_length": 1},
    )
    for i, kwargs in enumerate(cases):
        (tmp_path / f"p{i}.pddl").write_text(make_problem(seed=i, **kwargs))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / f"p{i}.pddl")


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-n", "merge", "-g", "empty", "-t", "4"]) == 0
    assert capsys.readouterr().out == make_problem("merge", goal="empty", goal_tokens=4)
    invalid: tuple[dict[str, Any], ...] = (
        {"net": "ring"},
        {"net": "pipeline", "chain_length": 2},
        {"net": "mesh", "goal": "drain"},
        {"goal_tokens": 0},
    )
    for kwargs in invalid:
        with pytest.raises(ValueError):
            make_problem(**kwargs)
