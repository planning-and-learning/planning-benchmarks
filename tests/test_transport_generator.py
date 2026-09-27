import re

import pytest

from pypddl_datasets.generators.classical.transport.generator import main, make_problem


@pytest.mark.parametrize(
    "num_locations,num_trucks,num_packages,capacity,extra_edges",
    [(2, 1, 1, 1, 0), (6, 2, 5, 3, 4), (4, 1, 3, 2, 3)],
)
def test_transport_tasks_have_nontrivial_reachable_goals(
    num_locations, num_trucks, num_packages, capacity, extra_edges
):
    problem = make_problem(num_locations, num_trucks, num_packages, capacity, extra_edges, seed=17)
    assert problem == make_problem(num_locations, num_trucks, num_packages, capacity, extra_edges, seed=17)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    roads = re.findall(r"\(road (\w+) (\w+)\)", init)
    assert len(roads) == len(set(roads)) == 2 * (num_locations - 1 + extra_edges)
    assert all(left != right and (right, left) in roads for left, right in roads)

    # A connected reversible road graph and a truck with room suffice to deliver
    # every package separately, independently of package count and truck starts.
    reached = {"l0"}
    frontier = ["l0"]
    while frontier:
        current = frontier.pop()
        for left, right in roads:
            if left == current and right not in reached:
                reached.add(right)
                frontier.append(right)
    assert reached == {f"l{i}" for i in range(num_locations)}

    at_facts = re.findall(r"\(at (\w+) (\w+)\)", init)
    starts = dict(at_facts)
    assert len(starts) == len(at_facts) == num_trucks + num_packages
    assert set(starts.values()) <= reached
    goals = re.findall(r"\(at (\w+) (\w+)\)", goal)
    assert len(goals) == num_packages
    assert {package for package, _ in goals} == {f"p{i}" for i in range(num_packages)}
    assert all(destination in reached and destination != starts[package] for package, destination in goals)
    assert set(re.findall(r"\(capacity (\w+) (\w+)\)", init)) == {
        (f"t{i}", f"capacity{capacity}") for i in range(num_trucks)
    }
    assert set(re.findall(r"\(capacity-predecessor (\w+) (\w+)\)", init)) == {
        (f"capacity{i}", f"capacity{i + 1}") for i in range(capacity)
    }
    assert "(:metric" not in problem
    assert "(in " not in init


def test_transport_cli_matches_make_problem(capsys):
    assert main(["-l", "5", "-t", "2", "-p", "4", "-c", "3", "-e", "2", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(5, 2, 4, capacity=3, extra_edges=2, seed=9)


@pytest.mark.parametrize(
    "parameter,value",
    [
        ("num_locations", 1),
        ("num_trucks", 0),
        ("num_packages", 0),
        ("capacity", 0),
        ("extra_edges", -1),
        ("extra_edges", 4),
        ("num_packages", 1.5),
        ("capacity", True),
    ],
)
def test_transport_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_locations=4, num_trucks=1, num_packages=1, capacity=2, extra_edges=0)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
