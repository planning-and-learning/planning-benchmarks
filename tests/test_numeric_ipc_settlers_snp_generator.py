import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.settlers_snp import generator
from pypddl_datasets.generators.numeric.ipc.settlers_snp.generator import main, make_problem


@pytest.mark.parametrize("num_locations,seed", [(2, 0), (5, 1), (9, 2), (15, 3)])
def test_world_is_connected_and_goals_are_buildable(num_locations, seed):
    problem = make_problem(num_locations, seed=seed)
    assert problem == make_problem(num_locations, seed=seed)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    land = set(re.findall(r"\(connected-by-land ([^\s)]+) ([^\s)]+)\)", init))
    assert all((b, a) in land for a, b in land)
    locations = {f"location{i}" for i in range(num_locations)}
    reached, frontier = {"location0"}, ["location0"]
    while frontier:
        current = frontier.pop()
        for a, b in land:
            if a == current and b not in reached:
                reached.add(b)
                frontier.append(b)
    assert reached == locations
    coast = set(re.findall(r"\(by-coast ([^\s)]+)\)", init))
    assert all(a in coast and b in coast for a, b in re.findall(r"\(connected-by-sea ([^\s)]+) ([^\s)]+)\)", init))
    for prop in ("woodland", "mountain", "metalliferous", "by-coast"):
        assert re.search(rf"\({prop} ", init)
    assert all(pair in land for pair in re.findall(r"\(connected-by-rail ([^\s)]+) ([^\s)]+)\)", goal))
    assert "(potential vehicle0)" in init and not re.search(r"\(= \([^)]*\) [1-9]", init)


def test_goal_count_and_vehicles():
    problem = make_problem(8, num_vehicles=3, num_goals=12, seed=5)
    goal = problem.split("(:goal")[1]
    assert len(re.findall(r"\((?:>= \(housing|has-|connected-by-rail)", goal)) == 12
    assert re.findall(r"\(potential ([^\s)]+)\)", problem) == ["vehicle0", "vehicle1", "vehicle2"]


def test_parses_strictly(tmp_path):
    options = ParserOptions()
    options.strict = True
    for n in (5, 15):
        (tmp_path / f"p{n}.pddl").write_text(make_problem(n, seed=n))
        Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / f"p{n}.pddl")


def test_cli_and_validation(capsys):
    assert main(["-l", "6", "-g", "5", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(6, num_goals=5, seed=2)
    for kwargs in (dict(num_locations=1), dict(num_locations=4, num_vehicles=0), dict(num_locations=4, land_density=2.0)):
        with pytest.raises(ValueError):
            make_problem(**kwargs)
