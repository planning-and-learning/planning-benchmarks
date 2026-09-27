import re
from pathlib import Path

import pytest

from pypddl_datasets.generators.classical.autoscale.driverlog.generator import make_problem as make_typed
from pypddl_datasets.generators.classical.ipc.driverlog import generator as ipc_generator
from pypddl_datasets.generators.classical.ipc.driverlog.generator import main, make_problem


GENERATORS = Path(ipc_generator.__file__).parents[2]


def _parse(problem: str, domain_file: Path, tmp_path: Path) -> None:
    from pypddl.formalism import Parser, ParserOptions

    (tmp_path / "p.pddl").write_text(problem, encoding="utf-8")
    options = ParserOptions()
    options.strict = True
    Parser(domain_file, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def _facts(problem: str) -> set[str]:
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    return set(re.findall(r"\([^()]+\)", init))


def _reachable(edges, start):
    reached, frontier = {start}, [start]
    while frontier:
        current = frontier.pop()
        for left, right in edges:
            if left == current and right not in reached:
                reached.add(right)
                frontier.append(right)
    return reached


@pytest.mark.parametrize("locations,drivers,packages,trucks", [(1, 1, 1, 1), (3, 1, 2, 1), (10, 4, 12, 4)])
def test_driverlog_road_and_foot_networks_are_connected(locations, drivers, packages, trucks):
    problem = make_typed(locations, drivers, packages, trucks, seed=6)
    assert problem == make_typed(locations, drivers, packages, trucks, seed=6)
    objects, rest = problem.split("(:init", 1)
    init, goal = rest.split("(:goal", 1)
    junctions = {f"s{i}" for i in range(locations)}
    declared = set(re.findall(r"(\S+) - location", objects))

    links = re.findall(r"\(link (\w+) (\w+)\)", init)
    assert all((right, left) in links for left, right in links)
    assert _reachable(links, "s0") == junctions
    paths = re.findall(r"\(path ([\w-]+) ([\w-]+)\)", init)
    assert all((right, left) in paths for left, right in paths)
    # Foot paths go junction -> p{a}-{b} -> junction.
    assert all((left in junctions) != (right in junctions) for left, right in paths)
    assert {name for pair in paths for name in pair} <= declared
    assert _reachable(paths, "s0") >= junctions

    at = dict(re.findall(r"\(at (\w+) (\w+)\)", init))
    assert len(at) == drivers + trucks + packages and set(at.values()) <= junctions
    assert set(re.findall(r"\(empty (\w+)\)", init)) == {f"truck{i}" for i in range(1, trucks + 1)}
    goals = dict(re.findall(r"\(at (\w+) (\w+)\)", goal))
    assert set(goals) <= set(at) and set(goals.values()) <= junctions


def test_driverlog_goal_probabilities_follow_upstream():
    goals = [make_problem(4, 20, 20, 20, seed=seed).split("(:goal", 1)[1] for seed in range(50)]
    for prefix, low, high in (("driver", 0.65, 0.75), ("truck", 0.65, 0.75), ("package", 0.92, 0.98)):
        rate = sum(len(re.findall(rf"\(at {prefix}\d", goal)) for goal in goals) / 1000
        assert low < rate < high, prefix


def test_driverlog_cli_matches_make_problem(capsys):
    assert main(["-l", "5", "-d", "2", "-p", "4", "-t", "3", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(5, 2, 4, 3, seed=9)


@pytest.mark.parametrize("parameter", ["num_locations", "num_drivers", "num_packages", "num_trucks"])
def test_driverlog_rejects_invalid_parameters(parameter):
    parameters = dict(num_locations=3, num_drivers=1, num_packages=1, num_trucks=1)
    parameters[parameter] = 0
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


@pytest.mark.parametrize("seed", range(3))
def test_driverlog_encodings_differ_only_in_type_predicates(seed, tmp_path):
    untyped, typed = make_problem(4, 2, 5, 2, seed=seed), make_typed(4, 2, 5, 2, seed=seed)
    kinds = {fact for fact in _facts(untyped) if re.fullmatch(r"\((driver|truck|obj|location) [\w-]+\)", fact)}
    assert _facts(untyped) - kinds == _facts(typed)
    assert untyped.split("(:goal", 1)[1] == typed.split("(:goal", 1)[1]
    assert {fact.split()[0][1:] for fact in kinds} == {"driver", "truck", "obj", "location"} and " - " not in untyped
    _parse(untyped, GENERATORS / "ipc/driverlog/domain.pddl", tmp_path)
    _parse(typed, GENERATORS / "autoscale/driverlog/domain.pddl", tmp_path)
