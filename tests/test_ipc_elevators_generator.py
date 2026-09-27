import re

import pytest

from pypddl_datasets.generators.classical.ipc.elevators.generator import main, make_problem


@pytest.mark.parametrize(
    "num_areas,area_size,num_passengers,num_fast,num_slow",
    # (3, 6, 3, 1, 1) are the parameters of Autoscale 21.11 agile p01.
    [(3, 6, 3, 1, 1), (2, 2, 5, 0, 1), (4, 5, 10, 3, 2)],
)
def test_elevators_floors_connected_and_costs(num_areas, area_size, num_passengers, num_fast, num_slow):
    problem = make_problem(num_areas, area_size, num_passengers, num_fast, num_slow, seed=4)
    assert problem == make_problem(num_areas, area_size, num_passengers, num_fast, num_slow, seed=4)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    num_floors = num_areas * area_size + 1

    reachable: dict[str, set[int]] = {}
    for lift, floor in re.findall(r"\(reachable-floor (\S+) n(\d+)\)", init):
        reachable.setdefault(lift, set()).add(int(floor))
    assert len(reachable) == num_fast + num_areas * num_slow
    starts = dict(re.findall(r"\(lift-at (\S+) n(\d+)\)", init))
    assert all(int(starts[lift]) in floors for lift, floors in reachable.items())

    # Slow lifts of neighbouring areas share a floor, so any floor reaches any other.
    reached, frontier = {0}, [0]
    while frontier:
        floor = frontier.pop()
        for floors in reachable.values():
            if floor in floors:
                for other in floors - reached:
                    reached.add(other)
                    frontier.append(other)
    assert reached == set(range(num_floors))

    origins = dict(re.findall(r"\(passenger-at (\S+) n(\d+)\)", init))
    destinations = dict(re.findall(r"\(passenger-at (\S+) n(\d+)\)", goal))
    assert len(origins) == len(destinations) == num_passengers
    assert all(origins[p] != destinations[p] for p in origins)

    for kind, stop, per_floor in (("slow", 5, 1), ("fast", 1, 3)):
        costs = re.findall(rf"\(= \(travel-{kind} n(\d+) n(\d+)\) (\d+)\)", init)
        assert all(int(c) == stop + (int(j) - int(i)) * per_floor for i, j, c in costs)
    assert len(set(re.findall(r"\(can-hold fast\d+ (\S+)\)", init))) == (3 if num_fast else 0)
    assert set(re.findall(r"\(can-hold slow\S+ (\S+)\)", init)) == {"n1", "n2"}


def test_elevators_cli_matches_make_problem(capsys):
    assert main(["2", "4", "6", "2", "--slow-capacity", "3", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(2, 4, 6, 2, slow_capacity=3, seed=9)


@pytest.mark.parametrize(
    "parameter,value",
    [("num_areas", 0), ("area_size", 1), ("num_passengers", 0), ("num_fast_elevators", -1),
     ("num_slow_elevators", 0), ("fast_capacity", True)],
)
def test_elevators_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_areas=2, area_size=3, num_passengers=2, num_fast_elevators=1)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
