import re

import pytest

from pypddl_datasets.generators.classical.ipc.tidybot.generator import main, make_problem


def cells(pattern, text):
    return [(int(x), int(y)) for x, y in re.findall(pattern, text)]


@pytest.mark.parametrize("world_size,num_tables,num_cupboards", [(5, 0, 1), (9, 3, 1), (12, 5, 3), (12, 7, 2)])
def test_tidybot_objects_fill_cupboards_and_start_on_surfaces(world_size, num_tables, num_cupboards):
    problem = make_problem(world_size, num_tables, num_cupboards, 1, 2, 4, seed=3)
    assert problem == make_problem(world_size, num_tables, num_cupboards, 1, 2, 4, seed=3)
    assert problem == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    objects = re.findall(r"(object\d+) - object", problem)
    assert len(objects) == num_cupboards * 4 == len(re.findall(r"\(object-done", goal))
    assert len(re.findall(r" - xc", problem)) == len(re.findall(r" - yc", problem)) == world_size

    surfaces = set(cells(r"\(surface x(\d+) y(\d+)\)", init))
    table_cells = set(cells(r"\(base-obstacle x(\d+) y(\d+)\)\(surface", init))
    walls = set(cells(r"\(base-obstacle x(\d+) y(\d+)\)\(gripper-obstacle", init))
    inner = surfaces - table_cells
    assert len(walls) == num_cupboards * 10 and len(inner) == num_cupboards * 4
    starts = cells(r"\(object-pos \w+ x(\d+) y(\d+)\)", init)
    assert len(set(starts)) == len(objects) and set(starts) <= surfaces
    goals = {}
    for name, x, y in re.findall(r"\(object-goal (\w+) x(\d+) y(\d+)\)", init):
        goals.setdefault(name, []).append((int(x), int(y)))
    assert sorted(goals) == sorted(objects)
    # One cupboard cell per object, plus at most one extra goal on a table.
    assert sorted(g[0] for g in goals.values()) == sorted(inner)
    assert all(len(g) <= 2 and set(g[1:]) <= table_cells for g in goals.values())
    if not table_cells:
        assert all(len(g) == 1 for g in goals.values())
    assert (0, 0) not in surfaces | walls and (0, 1) not in surfaces | walls  # robot and cart start cells


def test_tidybot_cli_and_validation(capsys):
    assert main(["9", "3", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem(9, 3, seed=4)
    with pytest.raises(ValueError, match="cupboards do not fit"):
        make_problem(6, 0, 3)
    for parameter, value in (("world_size", 0), ("num_tables", -1), ("num_cupboards", 0), ("cupboard_size", 2)):
        arguments = dict(world_size=9, num_tables=1)
        arguments[parameter] = value
        with pytest.raises(ValueError, match=parameter):
            make_problem(**arguments)
