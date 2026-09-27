import re

import pytest

from pypddl_datasets.generators.classical.ipc.scanalyzer.generator import main, make_problem


@pytest.mark.parametrize("segment_type", ["empty", "ab"])
@pytest.mark.parametrize("inout", ["none", "in", "both"])
@pytest.mark.parametrize("size", [1, 3])
def test_scanalyzer_structure(size, segment_type, inout):
    problem = make_problem(size, segment_type, inout)
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    halves = ["a", "b"] if segment_type == "ab" else [""]
    cars = {f"car-{d}-{s}{h}" for d in ("in", "out") for s in range(1, size + 1) for h in halves}
    on = dict(re.findall(r"\(on (\S+) (\S+)\)", init))
    assert set(on) == cars and len(set(on.values())) == len(cars)
    assert set(re.findall(r"\(analyzed (\S+)\)", goal)) == cars

    # Every car has one goal segment and together they are a permutation of the
    # segments, so the goal is a rearrangement of the initial occupancy.
    goal_on = dict(re.findall(r"\(on (\S+) (\S+)\)", goal))
    assert set(goal_on) == cars and set(goal_on.values()) == set(on.values())

    cycle = "cycle-4" if segment_type == "ab" else "cycle-2"
    assert len(re.findall(rf"\({cycle} ", init)) == size * size
    num_in, num_out = {"none": (1, 1), "in": (size, 1), "both": (size, size)}[inout]
    assert len(re.findall(rf"\({cycle}-with-analysis ", init)) == num_in * num_out
    assert "(:metric minimize (total-cost))" in problem


def test_scanalyzer_cli_matches_make_problem(capsys):
    assert main(["4", "ab", "both"]) == 0
    assert capsys.readouterr().out == make_problem(4, "ab", "both")


@pytest.mark.parametrize("parameter,value", [("size", 0), ("size", True), ("segment_type", "a"), ("inout", "out")])
def test_scanalyzer_rejects_invalid_parameters(parameter, value):
    parameters = dict(size=2, segment_type="empty", inout="in")
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
