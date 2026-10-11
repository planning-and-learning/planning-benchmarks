import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.ged import generator
from pypddl_datasets.generators.classical.ipc.ged.generator import main, make_problem


def genome(part: str) -> list[int]:
    """Signed gene numbers of the cw cycle in ``part``, starting at g1."""
    nxt = dict(re.findall(r"\(cw g(\d+) g(\d+)\)", part))
    inverted = set(re.findall(r"\(inverted g(\d+)\)", part))
    order = ["1"]
    while nxt[order[-1]] != "1":
        order.append(nxt[order[-1]])
    assert len(order) == len(nxt)
    return [-int(g) if g in inverted else int(g) for g in order]


@pytest.mark.parametrize("num_genes", [4, 5, 20, 36])
def test_ged_structure(num_genes: int) -> None:
    problem = make_problem(num_genes, seed=4)
    assert problem == make_problem(num_genes, seed=4) == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    start, end = genome(init), genome(goal)
    assert sorted(map(abs, start)) == sorted(map(abs, end)) == list(range(1, num_genes + 1))
    assert len(re.findall(r"\((?:normal|inverted) ", goal)) == num_genes
    assert init.count("(present ") == num_genes and "(idle)" in init and "(= (total-cost) 0)" in init

    def adjacencies(g: list[int]) -> set[tuple[int, int]]:
        pairs = list(zip(g, g[1:]))
        return {*pairs, *((-b, -a) for a, b in pairs)}

    assert end[0] == 1 and end[-1] == start[-1]
    assert not adjacencies(start) & adjacencies(end)


def test_ged_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    for seed in range(3):
        (tmp_path / "p.pddl").write_text(make_problem(12, seed=seed))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_ged_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["8", "-s", "2", "--goal-inverted-probability", "0.5"]) == 0
    assert capsys.readouterr().out == make_problem(8, 2, goal_inverted_probability=0.5)
    with pytest.raises(ValueError, match="num_genes"):
        make_problem(3)
    with pytest.raises(ValueError, match="init_inverted_probability"):
        make_problem(5, init_inverted_probability=1.5)
