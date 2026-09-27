import re
from collections import Counter

import pytest

from pypddl_datasets.generators.classical.ipc.schedule.generator import main, make_problem, part_name


@pytest.mark.parametrize("num_parts", [1, 2, 10, 50])
def test_schedule_follows_ipc_task_structure(num_parts):
    problem = make_problem(num_parts, seed=3)
    assert problem == make_problem(num_parts, seed=3)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    parts = [part_name(i) for i in range(num_parts)]
    shape = dict(re.findall(r"\(shape (\w+) (\w+)\)", init))
    surface = dict(re.findall(r"\(surface-condition (\w+) (\w+)\)", init))
    paint = dict(re.findall(r"\(painted (\w+) (\w+)\)", init))
    holes = re.findall(r"\(has-hole (\w+) \w+ \w+\)", init)
    # IPC: every part is painted and has one hole initially.
    assert set(shape) == set(surface) == set(paint) == set(holes) == set(parts) and len(holes) == num_parts
    # IPC: exactly one goal fact per part, distinct (part, kind), never a hole goal, never already true.
    goals = re.findall(r"\((shape|surface-condition|painted|has-hole) (\w+) (\w+)\)", goal)
    assert len(goals) == num_parts and len({(kind, part) for kind, part, _ in goals}) == num_parts
    current = {"shape": shape, "surface-condition": surface, "painted": paint}
    assert all(kind != "has-hole" and current[kind][part] != value for kind, part, value in goals)
    assert all(value == "cylindrical" for kind, _, value in goals if kind == "shape")


def test_schedule_goal_kind_shares_match_ipc():
    # IPC 2000 (150 tasks): shape 0.256, surface 0.379, paint 0.366.
    kinds = Counter(kind for seed in range(40) for kind in re.findall(r"\((shape|surface-condition|painted) ", make_problem(30, seed=seed).split("(:goal")[1]))
    total = sum(kinds.values())
    assert abs(kinds["shape"] / total - 0.256) < 0.03
    assert abs(kinds["surface-condition"] / total - 0.379) < 0.03
    assert abs(kinds["painted"] / total - 0.366) < 0.03


def test_schedule_part_names_follow_ipc():
    assert [part_name(i) for i in (0, 14, 15, 16, 22, 23)] == ["a0", "o0", "q0", "p0", "z0", "a1"]


def test_schedule_cli(capsys):
    assert main(["-p", "4", "-r", "2"]) == 0
    assert capsys.readouterr().out == make_problem(4, seed=2)
    with pytest.raises(ValueError, match="num_parts"):
        make_problem(0)
