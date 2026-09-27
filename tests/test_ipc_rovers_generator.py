import re

import pytest

from pypddl_datasets.generators.classical.autoscale.rovers.generator import make_problem as make_autoscale
from pypddl_datasets.generators.classical.ipc.rovers.generator import main, make_problem


def visible_from(problem):
    sets = {}
    for objective, waypoint in re.findall(r"\(visible_from (\w+) waypoint(\d+)\)", problem):
        sets.setdefault(objective, set()).add(int(waypoint))
    return sets


def goal_types(problem):
    goal = problem.split("(:goal", 1)[1]
    return {kind for kind in ("soil", "rock", "image") if f"communicated_{kind}_data" in goal}


@pytest.mark.parametrize("seed", range(20))
def test_rovers_default_follows_ipc_tasks(seed):
    # All 40 IPC tasks: every goal type present, objectives visible from a prefix waypoint0..k-1.
    problem = make_problem(1, 4, 2, 1, 1, seed=seed)
    assert problem == make_problem(1, 4, 2, 1, 1, seed=seed)
    assert goal_types(problem) == {"soil", "rock", "image"}
    prefixes = sum(sets == set(range(len(sets))) for sets in visible_from(make_problem(6, 20, 8, 7, 5, seed=seed)).values())
    assert prefixes >= 7  # the calibration repair may extend one set


def test_rovers_autoscale_mode_draws_scattered_visibility():
    sets = [s for seed in range(10) for s in visible_from(make_autoscale(6, 20, 8, 7, 5, seed=seed)).values()]
    assert sum(s == set(range(len(s))) for s in sets) < len(sets) / 2
    assert any(goal_types(make_autoscale(1, 4, 2, 1, 1, seed=seed)) != {"soil", "rock", "image"} for seed in range(30))


def test_rovers_cli(capsys):
    assert main(["2", "6", "3", "2", "3", "-s", "4"]) == 0
    assert capsys.readouterr().out == make_problem(2, 6, 3, 2, 3, 4)
