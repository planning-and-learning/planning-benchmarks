import re
from collections import defaultdict
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.settlersnumeric import generator
from pypddl_datasets.generators.numeric.ipc.settlersnumeric.generator import main, make_problem


def _component(start: str, edges: list[tuple[str, str]]) -> set[str]:
    adjacent: defaultdict[str, set[str]] = defaultdict(set)
    for a, b in edges:
        adjacent[a].add(b)
    seen, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(adjacent[node] - seen)
    return seen


@pytest.mark.parametrize("locations,vehicles,goals,islands", [(1, 1, 1, 1), (5, 5, 3, 1), (15, 10, 30, 1), (12, 15, 5, 3)])
def test_settlers_tasks_are_solvable_by_construction(locations, vehicles, goals, islands, tmp_path):
    problem = make_problem(locations, vehicles, goals, seed=8, num_islands=islands)
    assert problem == make_problem(locations, vehicles, goals, seed=8, num_islands=islands)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    land = re.findall(r"\(connected-by-land (\w+) (\w+)\)", init)
    sea = re.findall(r"\(connected-by-sea (\w+) (\w+)\)", init)
    coast = set(re.findall(r"\(by-coast (\w+)\)", init))
    everything = {f"location{i}" for i in range(locations)}
    assert _component("location0", land + sea) == everything
    assert all(a in coast and b in coast for a, b in sea)
    # some land component holds every site type
    assert any(
        all(set(re.findall(rf"\({k} (\w+)\)", init)) & _component(start, land) for k in ("woodland", "mountain", "metalliferous"))
        for start in everything
    )
    assert all(r in set(land) for r in re.findall(r"\(connected-by-rail (\w+) (\w+)\)", goal))
    assert len(re.findall(r"^\t\(", goal.split(":metric")[0], re.M)) == goals
    assert set(re.findall(r"\(= \([^)]*\) (\S+)\)", init)) == {"0"}
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_and_validation(capsys):
    assert main(["-l", "6", "-v", "4", "-g", "5", "-s", "2", "-i", "2"]) == 0
    assert capsys.readouterr().out == make_problem(6, 4, 5, seed=2, num_islands=2)
    with pytest.raises(ValueError, match="num_islands"):
        make_problem(2, 1, 1, num_islands=3)
