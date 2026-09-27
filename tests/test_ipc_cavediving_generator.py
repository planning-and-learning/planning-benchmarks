import re
from collections import defaultdict
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.cavediving import generator
from pypddl_datasets.generators.classical.ipc.cavediving.generator import main, make_problem


def _depths(problem: str) -> tuple[defaultdict[str, set[str]], dict[str, int]]:
    adj: defaultdict[str, set[str]] = defaultdict(set)
    for a, b in re.findall(r"\(connected (l\d+) (l\d+)\)", problem):
        adj[a].add(b)
    depth, order = {"l0": 0}, ["l0"]
    index = 0
    while index < len(order):  # breadth-first: order grows while it is walked
        node = order[index]
        index += 1
        for nxt in adj[node]:
            if nxt not in depth:
                depth[nxt] = depth[node] + 1
                order.append(nxt)
    return adj, depth


@pytest.mark.parametrize("branches,objectives", [([2], [2]), ([3, 2, 2], [2, 2]), ([4, 3], [4, 3])])
@pytest.mark.parametrize("seed", range(3))
def test_cavediving_structure(branches: list[int], objectives: list[int], seed: int) -> None:
    problem = make_problem(branches, objectives, perturb_hiring_costs=0.1, seed=seed)
    assert problem == make_problem(branches, objectives, perturb_hiring_costs=0.1, seed=seed) == problem.lower()
    adj, depth = _depths(problem)
    locations = problem.split(" - location")[0].split()[-len(depth) :]
    assert set(depth) == set(locations)  # a connected tree
    assert sum(len(v) for v in adj.values()) == 2 * (len(depth) - 1)
    photos = [f"l{o}" for o in re.findall(r"\(have-photo l(\d+)\)", problem)]
    assert sorted(depth[p] for p in photos) == sorted(objectives) and all(len(adj[p]) == 1 for p in photos)
    tanks = re.findall(r"\(next-tank (\S+) \S+\)", problem)
    assert len(tanks) == sum(2 ** (d + 1) for d in objectives) - 1
    divers = set(re.findall(r"\(available (\S+)\)", problem))
    assert len(divers) == sum(2 ** (d - 1) for d in objectives)
    assert set(re.findall(r"\(decompressing (\S+)\)", problem)) == divers
    assert all(10 <= int(c) <= 100 for c in re.findall(r"\(hiring-cost \S+\) (\d+)\)", problem))


def test_cavediving_parses_strictly(tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(make_problem([3, 2, 2], [2, 2], perturb_hiring_costs=0.1, seed=1))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cavediving_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-b", "3:2", "-o", "3", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem([3, 2], [3], seed=4)
    with pytest.raises(ValueError, match="objectives"):
        make_problem([3], [2])
    with pytest.raises(ValueError, match="deepest"):
        make_problem([2, 3], [3])
