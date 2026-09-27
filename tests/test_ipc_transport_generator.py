import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.transport.generator import make_problem as make_autoscale
from pypddl_datasets.generators.classical.ipc.transport import generator
from pypddl_datasets.generators.classical.ipc.transport.generator import main, make_problem

HERE = Path(generator.__file__).parent


@pytest.mark.parametrize(
    "kind,num_nodes,num_trucks,num_packages,degree",
    [("city", 2, 1, 1, 3), ("city", 20, 3, 6, 4), ("two-cities", 6, 2, 4, 5), ("three-cities", 8, 3, 5, 3)],
)
@pytest.mark.parametrize("seed", range(3))
def test_transport_tasks_are_connected_with_symmetric_costs(kind, num_nodes, num_trucks, num_packages, degree, seed):
    problem = make_problem(kind, num_nodes, num_trucks, num_packages, degree, seed=seed, action_costs=True)
    assert problem == make_problem(kind, num_nodes, num_trucks, num_packages, degree, seed=seed, action_costs=True)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    roads = re.findall(r"\(road (\S+) (\S+)\)", init)
    lengths = {(a, b): int(n) for a, b, n in re.findall(r"\(= \(road-length (\S+) (\S+)\) (\d+)\)", init)}
    assert set(roads) == set(lengths) and len(roads) == len(set(roads))
    assert all(lengths[b, a] == n and n >= 1 for (a, b), n in lengths.items())

    locations = problem.split("(:objects", 1)[1].split(" - location", 1)[0].split()
    num_cities = ("city", "two-cities", "three-cities").index(kind) + 1
    assert len(locations) == num_cities * num_nodes
    reached, frontier = {locations[0]}, [locations[0]]
    while frontier:
        current = frontier.pop()
        for a, b in roads:
            if a == current and b not in reached:
                reached.add(b)
                frontier.append(b)
    assert reached == set(locations)

    starts = dict(re.findall(r"\(at (\S+) (\S+)\)", init))
    assert len(starts) == num_trucks + num_packages
    goals = dict(re.findall(r"\(at (\S+) (\S+)\)", goal))
    assert sorted(goals) == sorted(f"package-{i + 1}" for i in range(num_packages))
    assert all(goals[p] != starts[p] for p in goals)
    if kind == "two-cities":
        assert all(starts[p].startswith("city-1-") and goals[p].startswith("city-2-") for p in goals)
        assert all(starts[f"truck-{i + 1}"].startswith("city-2-") for i in range(num_trucks))
    capacities = re.findall(r"\(capacity truck-\d+ capacity-(\d)\)", init)
    assert len(capacities) == num_trucks and all(2 <= int(c) <= 4 for c in capacities)
    assert "(:metric minimize (total-cost))" in problem


@pytest.mark.parametrize("kind", ["city", "two-cities", "three-cities"])
def test_cost_free_encoding_drops_only_costs(kind):
    with_costs = make_problem(kind, 6, 2, 3, seed=4, action_costs=True)
    cost_free = make_problem(kind, 6, 2, 3, seed=4)
    kept = [line for line in with_costs.splitlines() if "total-cost" not in line and "road-length" not in line]
    assert cost_free.splitlines() == kept
    assert make_autoscale(kind, 6, 2, 3, seed=4) == with_costs


@pytest.mark.parametrize(
    "action_costs,domain_path",
    [
        (False, HERE / "domain.pddl"),
        (True, HERE / "domain_action_costs.pddl"),
        (True, HERE.parents[1] / "autoscale/transport/domain.pddl"),
    ],
)
def test_transport_parses_strictly(action_costs, domain_path, tmp_path):
    options = ParserOptions()
    options.strict = True
    for kind in ("city", "two-cities", "three-cities"):
        problem = tmp_path / f"{kind}.pddl"
        problem.write_text(make_problem(kind, 5, 2, 3, seed=1, action_costs=action_costs))
        Parser(domain_path, options).parse_task(problem)  # pyright: ignore[reportUnknownMemberType]


def test_transport_cli_matches_make_problem(capsys):
    assert main(["three-cities", "5", "2", "3", "-d", "4", "-s", "7"]) == 0
    assert capsys.readouterr().out == make_problem("three-cities", 5, 2, 3, degree=4, seed=7)
    assert main(["city", "5", "2", "3", "-s", "7", "--action-costs"]) == 0
    assert capsys.readouterr().out == make_problem("city", 5, 2, 3, seed=7, action_costs=True)


@pytest.mark.parametrize(
    "parameter,value",
    [("kind", "four-cities"), ("num_nodes", 1), ("num_trucks", 0), ("num_packages", 0), ("degree", 0), ("num_nodes", 2.5)],
)
def test_transport_rejects_invalid_parameters(parameter, value):
    parameters = dict(kind="city", num_nodes=4, num_trucks=1, num_packages=1, degree=3)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
