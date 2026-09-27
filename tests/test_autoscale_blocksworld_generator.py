import re
from typing import Any

import pytest

from pypddl_datasets.generators.classical.autoscale.blocksworld.generator import main, make_problem


@pytest.mark.parametrize("num_blocks", [1, 2, 5, 12])
def test_blocks_goal_is_on_facts_of_a_valid_state(num_blocks: int) -> None:
    problem = make_problem(num_blocks, seed=3)
    assert problem == make_problem(num_blocks, seed=3)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    blocks = {f"b{i}" for i in range(1, num_blocks + 1)}

    below = dict(re.findall(r"\(on (\w+) (\w+)\)", init))
    on_table = set(re.findall(r"\(on-table (\w+)\)", init))
    assert set(below) | on_table == blocks and not set(below) & on_table
    assert set(re.findall(r"\(clear (\w+)\)", init)) == blocks - set(below.values())

    assert "on-table" not in goal and "clear" not in goal
    goal_below = dict(re.findall(r"\(on (\w+) (\w+)\)", goal))
    # A state: every block supports at most one block and stacks are acyclic.
    assert len(set(goal_below.values())) == len(goal_below)
    for block in goal_below:
        seen: set[str] = set()
        while block in goal_below:
            assert block not in seen
            seen.add(block)
            block = goal_below[block]


def test_blocks_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["7", "11"]) == 0
    assert capsys.readouterr().out == make_problem(7, 11)


@pytest.mark.parametrize("num_blocks", [0, True, 2.5])
def test_blocks_rejects_invalid_parameters(num_blocks: Any) -> None:
    with pytest.raises(ValueError, match="num_blocks"):
        make_problem(num_blocks)
