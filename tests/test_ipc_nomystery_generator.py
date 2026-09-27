import re

import pytest

from pypddl_datasets.generators.classical.autoscale.nomystery.generator import make_problem as make_autoscale
from pypddl_datasets.generators.classical.ipc.nomystery.generator import main, make_problem


def sum_table(problem):
    sums = {tuple(map(int, fact)) for fact in re.findall(r"\(sum level(\d+) level(\d+) level(\d+)\)", problem)}
    max_level = max(int(level) for level in re.findall(r"\blevel(\d+)\b", problem.split("(:init")[0]))
    costs = {int(cost) for cost in re.findall(r"\(fuelcost level(\d+)", problem)}
    return sums, max_level, costs


@pytest.mark.parametrize("seed", range(5))
def test_nomystery_default_lists_full_sum_table_like_ipc(seed):
    # All 40 IPC 2011 tasks list sum for every a + b <= max level, including b = 0.
    problem = make_problem(4, 3, 1.5, 25, 1.5, seed)
    sums, top, _ = sum_table(problem)
    assert sums == {(a, b, a + b) for a in range(top + 1) for b in range(top + 1) if a + b <= top}


def test_nomystery_autoscale_restricts_sum_table_to_edge_costs():
    # All 30 agile tasks list sum only for the edge costs.
    sums, top, costs = sum_table(make_autoscale(4, 3, 1.5, 25, 1.5, 2))
    assert sums == {(a, b, a + b) for a in range(top + 1) for b in costs if a + b <= top}


def test_nomystery_cli(capsys):
    assert main(["-l", "4", "-p", "2", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2, seed=3)
    assert main(["-l", "4", "-p", "2", "-s", "3", "--restricted-sum-table"]) == 0
    assert capsys.readouterr().out == make_autoscale(4, 2, seed=3)
