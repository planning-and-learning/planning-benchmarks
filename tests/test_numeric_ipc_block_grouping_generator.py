import re
from itertools import combinations
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.block_grouping import generator
from pypddl_datasets.generators.numeric.ipc.block_grouping.generator import main, make_problem


@pytest.mark.parametrize("size,blocks,colours", [(1, 3, 1), (5, 10, 2), (20, 15, 3), (11, 40, 10)])
def test_block_grouping_goal_encodes_a_colouring(size, blocks, colours):
    problem = make_problem(size, blocks, colours, seed=7)
    assert problem == make_problem(size, blocks, colours, seed=7)
    init, goal = problem.split("(:goal", 1)
    xs = dict(re.findall(r"\(= \(x (\w+)\) (\d+)\)", init))
    ys = dict(re.findall(r"\(= \(y (\w+)\) (\d+)\)", init))
    assert len(xs) == len(ys) == blocks and all(1 <= int(v) <= size for v in [*xs.values(), *ys.values()])
    same = set(re.findall(r"(?<!\(not )\(= \(x (\w+)\) \(x (\w+)\)\)", goal))
    apart = set(re.findall(r"\(or \(not \(= \(x (\w+)\) \(x (\w+)\)\)\)", goal))
    pairs = set(combinations(sorted(xs), 2))
    assert same | apart == pairs and not same & apart
    # "same colour" must be an equivalence relation with at most `colours` classes
    group = {b: {b} for b in xs}
    for a, b in same:
        merged = group[a] | group[b]
        for c in merged:
            group[c] = merged
    assert all((a, b) in same for g in map(frozenset, group.values()) for a, b in combinations(sorted(g), 2))
    assert len(set(map(frozenset, group.values()))) <= colours
    assert ("(:requirements" in problem) == bool(apart)


@pytest.mark.parametrize("colours", [1, 3])
def test_block_grouping_parses_strictly(colours, tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(6, 8, colours, seed=1))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_block_grouping_cli_and_validation(capsys):
    assert main(["7", "5", "2", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(7, 5, 2, seed=3)
    with pytest.raises(ValueError, match="num_colours"):
        make_problem(1, 3, 2)
    with pytest.raises(ValueError, match="num_blocks"):
        make_problem(5, 0, 1)
