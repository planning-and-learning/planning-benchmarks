import re

import pytest

from pypddl_datasets.generators.classical.autoscale.grid.generator import make_problem as make_autoscale
from pypddl_datasets.generators.classical.ipc.grid.generator import main, make_problem


def init_goal(problem):
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    return init, goal


@pytest.mark.parametrize("size,seed", [(3, 1), (5, 2), (9, 3)])
def test_grid_ipc_default_has_one_connected_lock_region(size, seed):
    problem = make_problem(size, size, seed=seed)
    assert problem == make_problem(size, size, seed=seed)
    init, goal = init_goal(problem)
    assert set(re.findall(r"\(shape (\w+)\)", init)) == {"triangle", "diamond", "square", "circle"}
    assert len(set(re.findall(r"\(lock-shape \S+ (\w+)\)", init))) == 1
    assert len(re.findall(r"\(key (\w+)\)", init)) == size + 4
    locked = set(re.findall(r"\(locked (\S+)\)", init))
    assert len(locked) == size * size // 4
    # locks are one 4-connected region, as in the IPC tasks
    cells = {tuple(map(int, c[4:].split("-"))) for c in locked}
    seen, stack = set(), [next(iter(cells))]
    while stack:
        x, y = stack.pop()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        stack += [c for c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if c in cells]
    assert seen == cells
    robot = re.search(r"\(at-robot (\S+)\)", init).group(1)
    assert robot.startswith("node") and robot not in locked and re.findall(r"\(at key\d+ \S+\)", goal)


def test_grid_ipc_goals_may_equal_start_autoscale_never():
    def hits(make):
        count = 0
        for seed in range(100):
            init, goal = init_goal(make(3, 3, 1, 4, 1, 1.0, seed))
            start = dict(re.findall(r"\(at (key\d+) (\S+)\)", init))
            count += sum(start[k] == p for k, p in re.findall(r"\(at (key\d+) (\S+)\)", goal))
        return count

    assert hits(make_problem) > 0
    assert hits(make_autoscale) == 0


def test_grid_autoscale_keeps_upstream_shapes_and_names():
    init, _ = init_goal(make_autoscale(7, 7, 2, 3, 24, 1.0, 1))
    assert set(re.findall(r"\(lock-shape \S+ (\w+)\)", init)) == {"shape0", "shape1"}
    assert "(place pos0-0)" in init


def test_grid_cli_matches_make_problem(capsys):
    assert main(["4", "5", "--locks", "3", "-s", "7"]) == 0
    assert capsys.readouterr().out == make_problem(4, 5, num_locks=3, seed=7)
