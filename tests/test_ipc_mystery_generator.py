import collections
import re

import pytest

from pypddl_datasets.generators.classical.ipc.mprime.generator import make_problem as make_mprime
from pypddl_datasets.generators.classical.ipc.mystery.generator import main, make_problem


def _relations(problem):
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    by = collections.defaultdict(list)
    for fact in re.findall(r"\(([a-z][a-z0-9 -]*)\)", init):
        predicate, *arguments = fact.split()
        by[predicate].append(tuple(arguments))
    return by, re.findall(r"\(craves (\S+) (\S+)\)", goal)


@pytest.mark.parametrize("params", [(2, 1, 1, 2, 2, 1), (7, 4, 20, 5, 4, 2), (22, 16, 46, 13, 4, 3), (60, 20, 30, 15, 12, 3)])
def test_mystery_structure(params):
    num_locations, num_vehicles, num_cargos, num_fuels, num_spaces, num_goals = params
    problem = make_problem(*params, seed=3)
    assert problem == make_problem(*params, seed=3) == problem.lower()
    by, goals = _relations(problem)
    locations = [x for (x,) in by["food"]]
    vehicles = {x for (x,) in by["pleasure"]}
    cargos = {x for (x,) in by["pain"]}
    assert (len(locations), len(vehicles), len(cargos), len(by["province"]), len(by["planet"])) == params[:5]
    assert len(set(locations) | vehicles | cargos) == num_locations + num_vehicles + num_cargos

    # Roads are symmetric and connected; with 3+ locations every location has 2+ roads.
    roads = set(by["eats"])
    assert all((b, a) in roads for a, b in roads)
    adjacent = collections.defaultdict(set)
    for a, b in roads:
        adjacent[a].add(b)
    seen, stack = {locations[0]}, [locations[0]]
    while stack:
        for other in adjacent[stack.pop()] - seen:
            seen.add(other)
            stack.append(other)
    assert seen == set(locations)
    if num_locations > 2:
        assert min(len(adjacent[location]) for location in locations) >= 2

    # Fuel and space chains, one fuel level per location, positive space per vehicle.
    assert len(by["attacks"]) == num_fuels - 1 and len(by["orbits"]) == num_spaces - 1
    assert sorted(location for location, _ in by["locale"]) == sorted(locations)
    lowest_space = ({x for (x,) in by["planet"]} - {b for _, b in by["orbits"]}).pop()
    assert {v for v, _ in by["harmony"]} == vehicles and lowest_space not in {s for _, s in by["harmony"]}
    starts = dict(by["craves"])
    assert set(starts) == vehicles | cargos and len({starts[v] for v in vehicles}) == num_vehicles
    assert len(goals) == len({c for c, _ in goals}) == num_goals and {c for c, _ in goals} <= cargos


def test_mprime_shares_the_mystery_distribution():
    mystery, mprime = make_problem(8, 3, 6, 5, 4, 2, seed=1), make_mprime(8, 3, 6, 5, 4, 2, seed=1)
    assert "(:domain mystery-strips)" in mystery and "(:domain mystery-prime-strips)" in mprime
    assert _relations(mystery) == _relations(mprime)


def test_mystery_cli_and_validation(capsys):
    assert main(["-l", "5", "-v", "2", "-c", "3", "-f", "4", "-s", "3", "-g", "1", "--seed", "2"]) == 0
    assert capsys.readouterr().out == make_problem(5, 2, 3, 4, 3, 1, seed=2)
    for parameters, message in (((3, 4, 2, 3, 3, 1), "num_vehicles"), ((3, 1, 2, 3, 3, 3), "num_goals"), ((3, 1, 2, 1, 3, 1), "num_fuel_levels")):
        with pytest.raises(ValueError, match=message):
            make_problem(*parameters)
