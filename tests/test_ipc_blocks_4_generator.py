import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.blocks_4 import generator
from pypddl_datasets.generators.classical.ipc.blocks_4.generator import main, make_problem


@pytest.mark.parametrize("num_blocks", [1, 2, 6, 17])
def test_blocks_4_default_goal_is_one_ipc_tower(num_blocks: int) -> None:
    problem = make_problem(num_blocks, seed=3)
    assert problem == make_problem(num_blocks, seed=3) == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    on = re.findall(r"\(on (\w+) (\w+)\)", goal)
    # n - 1 `on` facts over n blocks leave exactly one tower; nothing else is required.
    assert len(on) == num_blocks - 1
    assert len({upper for upper, _ in on}) == len({lower for _, lower in on}) == num_blocks - 1
    assert "(ontable" not in goal and "(clear" not in goal
    assert "(handempty)" in init and len(re.findall(r"\(ontable ", init)) >= 1


def test_blocks_4_full_goal_variant() -> None:
    goal = make_problem(5, seed=1, goal="full").split("(:goal", 1)[1]
    assert "(ontable " in goal and "(clear " in goal


def test_blocks_4_parses_against_ipc_domain(tmp_path: Path) -> None:
    domain = Path(generator.__file__).with_name("domain.pddl")
    options = ParserOptions()
    options.strict = True
    for goal in ("tower", "full"):
        (tmp_path / "p.pddl").write_text(make_problem(8, seed=2, goal=goal))
        Parser(domain, options).parse_task(tmp_path / "p.pddl")


def test_blocks_4_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-b", "4", "-s", "7", "-g", "full"]) == 0
    assert capsys.readouterr().out == make_problem(4, 7, "full")
    with pytest.raises(ValueError, match="goal"):
        make_problem(3, goal="partial")
