import re

import pytest

from pypddl_datasets.generators.classical.ipc.snake.generator import main, make_problem


@pytest.mark.parametrize(
    "width,height,spawn_percentage,name",
    # Parameters and resulting apple counts of Autoscale 21.11 agile p01, p02, p30.
    [(5, 5, 40, "snake-empty-5x5-1-5-2-2019"), (5, 6, 40, "snake-empty-5x6-1-5-5-2020"),
     (13, 14, 40, "snake-empty-13x14-1-5-65-2048")],
)
def test_snake_matches_autoscale_counts_and_is_consistent(width, height, spawn_percentage, name):
    seed = int(name.rsplit("-", 1)[1])
    problem = make_problem(width, height, spawn_percentage, seed=seed)
    assert problem == make_problem(width, height, spawn_percentage, seed=seed)
    assert f"(problem {name})" in problem
    _, snake_size, num_apples, num_spawn, _ = map(int, re.findall(r"\d+", name.split("x", 1)[1]))
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)

    head = re.findall(r"\(headsnake (\S+)\)", init)
    tail = re.findall(r"\(tailsnake (\S+)\)", init)
    body = re.findall(r"\(nextsnake (\S+) (\S+)\)", init)
    blocked = set(re.findall(r"\(blocked (\S+)\)", init))
    assert len(head) == len(tail) == 1 and len(body) == snake_size
    assert body[0][0] == head[0] and body[-1][1] == tail[0]
    assert blocked == {head[0], tail[0]} | {cell for pair in body for cell in pair}

    apples = re.findall(r"\(ispoint (\S+)\)", init)
    spawn_chain = dict(re.findall(r"\(nextspawn (\S+) (\S+)\)", init))
    first = re.findall(r"\(spawn (\S+)\)", init)
    spawned, current = [], first[0]
    while current != "dummypoint":
        spawned.append(current)
        current = spawn_chain[current]
    assert len(apples) == num_apples and len(spawned) == num_spawn == len(spawn_chain)
    assert len(set(apples) | set(spawned) | blocked) == num_apples + num_spawn + snake_size + 1
    assert sorted(re.findall(r"\(not \(ispoint (\S+)\)\)", goal)) == sorted(apples + spawned)
    assert len(re.findall(r"\(isadjacent ", init)) == 2 * ((width - 1) * height + width * (height - 1))


def test_snake_cli_matches_make_problem(capsys):
    assert main(["6", "7", "70", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(6, 7, 70, seed=3)


@pytest.mark.parametrize(
    "parameter,value",
    [("width", 0), ("height", 1.5), ("spawn_percentage", 0), ("spawn_percentage", 101), ("snake_size", True)],
)
def test_snake_rejects_invalid_parameters(parameter, value):
    parameters = dict(width=5, height=5, spawn_percentage=40)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)


def test_snake_rejects_overfull_board():
    with pytest.raises(ValueError, match="too small"):
        make_problem(2, 2, 100, snake_size=3)
