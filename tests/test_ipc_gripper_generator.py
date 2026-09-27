import re
from pathlib import Path

import pytest

from pypddl_datasets.generators.classical.ipc.gripper import generator
from pypddl_datasets.generators.classical.ipc.gripper.generator import main, make_problem


@pytest.mark.parametrize("num_balls", [1, 20])
def test_gripper_declares_rooms_as_objects(num_balls):
    assert "(:constants" not in Path(generator.__file__).with_name("domain.pddl").read_text()
    problem = make_problem(num_balls)
    objects = problem.split("(:objects", 1)[1].split(")", 1)[0].split()
    assert objects[:4] == ["rooma", "roomb", "left", "right"] and len(objects) == 4 + num_balls
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    assert re.findall(r"\(at (\w+) rooma\)", init) == [f"ball{i}" for i in range(1, num_balls + 1)]
    assert re.findall(r"\(at (\w+) roomb\)", goal) == [f"ball{i}" for i in range(1, num_balls + 1)]


def test_gripper_cli(capsys):
    assert main(["-n", "3"]) == 0
    assert capsys.readouterr().out == make_problem(3)
    with pytest.raises(ValueError, match="num_balls"):
        make_problem(0)
