import re
from collections import Counter
from typing import Any

import pytest

from pypddl_datasets.generators.classical.ipc.storage.generator import main, make_problem


@pytest.mark.parametrize(
    "crates,hoists,store_areas,depots,containers",
    [(1, 1, 1, 1, None), (4, 6, 15, 2, None), (18, 27, 39, 4, None), (30, 5, 70, 36, None), (3, 2, 10, 3, 3)],
)
def test_storage_depots_are_connected_grids_with_doors(
    crates: int, hoists: int, store_areas: int, depots: int, containers: None | int
) -> None:
    problem = make_problem(crates, hoists, store_areas, depots, containers, seed=11)
    assert problem == make_problem(crates, hoists, store_areas, depots, containers, seed=11)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    depot_names = [f"depot{i}" for i in range(depots)]
    area_depot = dict(re.findall(r"\(in (depot\d+-\d+-\d+) (depot\d+)\)", init))
    assert len(area_depot) == store_areas and set(area_depot.values()) == set(depot_names)

    connected = set(re.findall(r"\(connected ([\w-]+) ([\w-]+)\)", init))
    doors = {area for area, other in connected if other == "loadarea" and area in area_depot}
    assert Counter(area_depot[door] for door in doors) == Counter(depot_names)
    # Every store area reaches its depot's door, so every crate can be stored.
    for door in doors:
        reached, frontier = {door}, [door]
        while frontier:
            current = frontier.pop()
            for left, right in connected:
                if left == current and right in area_depot and right not in reached:
                    reached.add(right)
                    frontier.append(right)
        assert reached == {area for area, depot in area_depot.items() if depot == area_depot[door]}

    hoist_at = dict(re.findall(r"\(at (hoist\d+) ([\w-]+)\)", init))
    assert len(hoist_at) == hoists and len(set(hoist_at.values())) == hoists
    assert set(re.findall(r"\(clear ([\w-]+)\)", init)) == set(area_depot) - set(hoist_at.values())

    crate_on = dict(re.findall(r"\(on (crate\d+) ([\w-]+)\)", init))
    assert len(crate_on) == crates and all(area.startswith("container-") for area in crate_on.values())
    assert all(("loadarea", area) in connected for area in crate_on.values())
    goal_in = dict(re.findall(r"\(in (crate\d+) (depot\d+)\)", goal))
    assert set(goal_in) == set(crate_on)
    goal_counts = Counter(goal_in.values())
    assert all(goal_counts[depot] <= Counter(area_depot.values())[depot] for depot in depot_names)


def test_storage_default_containers_hold_four_crates() -> None:
    init = make_problem(10, 2, 20, seed=1).split("(:init", 1)[1]
    assert Counter(re.findall(r"\(in crate\d+ (container\d+)\)", init)) == {
        "container0": 4,
        "container1": 4,
        "container2": 2,
    }


def test_storage_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-c", "4", "-n", "3", "-s", "12", "-d", "2", "-e", "9"]) == 0
    assert capsys.readouterr().out == make_problem(4, 3, 12, 2, seed=9)


@pytest.mark.parametrize(
    "parameter,value",
    [
        ("num_crates", 0),
        ("num_hoists", 0),
        ("num_store_areas", 0),
        ("num_depots", 0),
        ("num_containers", 0),
        ("num_crates", 13),
        ("num_hoists", 13),
        ("num_depots", 13),
    ],
)
def test_storage_rejects_invalid_parameters(parameter: str, value: int) -> None:
    parameters: dict[str, Any] = {"num_crates": 2, "num_hoists": 2, "num_store_areas": 12, "num_depots": 2}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
