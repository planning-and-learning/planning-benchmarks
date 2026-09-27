import re
from collections import Counter
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.logistics import generator
from pypddl_datasets.generators.classical.ipc.logistics.generator import main, make_problem


def facts(problem, part):
    text = problem.split("(:init", 1)[1].split("(:goal", 1)[part]
    return [tuple(f.split()) for f in re.findall(r"\(([^()]+)\)", text)]


def parses(problem, domain, tmp_path):
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(problem)
    Parser(Path(generator.__file__).with_name(domain), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_logistics98_trucks_goals_and_starts(tmp_path):
    problem = make_problem(4, 3, 10, 2, seed=3, num_trucks=9, num_goals=6)
    assert problem == make_problem(4, 3, 10, 2, seed=3, num_trucks=9, num_goals=6)
    parses(problem, "domain.pddl", tmp_path)
    init, goal = facts(problem, 0), facts(problem, 1)
    in_city = {f[1]: f[2] for f in init if f[0] == "in-city"}
    at = {f[1]: f[2] for f in init if f[0] == "at"}
    trucks = [f[1] for f in init if f[0] == "truck"]
    per_city = Counter(in_city[at[t]] for t in trucks)
    assert len(trucks) == 9 and set(per_city) == {f"city{c}" for c in range(1, 5)}
    assert len(goal) == 6 and len({f[1] for f in goal}) == 6
    airports = {f[1] for f in init if f[0] == "airport"}
    assert airports == {f"city{c}-3" for c in range(1, 5)}
    assert all(at[f[1]] in airports for f in init if f[0] == "airplane")


def test_logistics98_goal_may_equal_start():
    # IPC logistics98: 3.6% of goals already hold; uniform destinations give 1/(C*L).
    hits = total = 0
    for seed in range(200):
        problem = make_problem(2, 2, 3, 1, seed=seed)
        at = {f[1]: f[2] for f in facts(problem, 0) if f[0] == "at"}
        goals = facts(problem, 1)
        hits += sum(at[f[1]] == f[2] for f in goals)
        total += len(goals)
    assert 0.15 < hits / total < 0.35


def test_logistics00_structure(tmp_path):
    problem = make_problem(3, 2, 9, 1, seed=1, num_goals=7, style="00")
    parses(problem, "domain_logistics00.pddl", tmp_path)
    init, goal = facts(problem, 0), facts(problem, 1)
    at = {f[1]: f[2] for f in init if f[0] == "at"}
    packages = [f[1] for f in init if f[0] == "package"]
    assert sorted(packages) == sorted(f"obj{c}{k}" for c in range(1, 4) for k in range(1, 4))
    assert all(at[p] == f"pos{p[3]}" for p in packages)  # packages start at their city's pos
    assert all(at[f"tru{c}"] == f"pos{c}" for c in range(1, 4))
    assert at["apn1"].startswith("apt") and len(goal) == 7
    with pytest.raises(ValueError, match="style 00"):
        make_problem(3, 3, 9, 1, style="00")


def test_logistics_cli_matches_make_problem(capsys):
    assert main(["3", "2", "6", "1", "-s", "4", "-t", "5", "-g", "4"]) == 0
    assert capsys.readouterr().out == make_problem(3, 2, 6, 1, seed=4, num_trucks=5, num_goals=4)
    assert main(["2", "2", "6", "1", "-s", "4", "--style", "00"]) == 0
    assert capsys.readouterr().out == make_problem(2, 2, 6, 1, seed=4, style="00")


@pytest.mark.parametrize("parameter,value", [("num_cities", 0), ("num_trucks", 1), ("num_goals", 7), ("style", "01")])
def test_logistics_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_cities=2, city_size=2, num_packages=6, num_airplanes=1)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter if parameter != "num_goals" else "num_goals"):
        make_problem(**parameters)
