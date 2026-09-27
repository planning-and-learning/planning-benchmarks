import random
import re
from collections import deque
from typing import Any

import pytest

from pypddl_datasets.generators.classical.ipc.termes.generator import (  # pylint: disable=protected-access
    _depot,  # pyright: ignore[reportPrivateUsage]  # the solvability test samples boards like the generator
    _goal_board,  # pyright: ignore[reportPrivateUsage]
    has_scaffold,
    main,
    make_problem,
)

State = tuple[tuple[int, ...], int, bool]


def _plan_exists(goal: list[list[int]], depot: tuple[int, int], max_height: int) -> bool:
    """Breadth-first search over the Termes state space (heights, robot, block)."""
    size_y, size_x = len(goal), len(goal[0])
    cells = [(x, y) for y in range(size_y) for x in range(size_x)]
    index = {cell: i for i, cell in enumerate(cells)}
    target = tuple(goal[y][x] for x, y in cells)
    neighbors = {
        cell: [
            index[(cell[0] + dx, cell[1] + dy)]
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if (cell[0] + dx, cell[1] + dy) in index
        ]
        for cell in cells
    }
    start: State = ((0,) * len(cells), index[depot], False)
    seen: set[State] = {start}
    queue: deque[State] = deque([start])
    while queue:
        heights, robot, block = queue.popleft()
        if heights == target and not block:
            return True
        successors: list[State] = []
        if robot == index[depot]:
            successors.append((heights, robot, not block))  # create-block / destroy-block
        for other in neighbors[cells[robot]]:
            if abs(heights[other] - heights[robot]) <= 1:
                successors.append((heights, other, block))  # move, move-up, move-down
            if block and other != index[depot] and heights[other] == heights[robot] < max_height:
                successors.append((heights[:other] + (heights[other] + 1,) + heights[other + 1 :], robot, False))
            if not block and heights[other] == heights[robot] + 1:
                successors.append((heights[:other] + (heights[other] - 1,) + heights[other + 1 :], robot, True))
        for state in successors:
            if state not in seen:
                seen.add(state)
                queue.append(state)
    return False


@pytest.mark.parametrize(
    "goal,depot,max_height",
    [
        # Boards where upstream z3 finds no scaffold although each tower alone has a ramp.
        ([[0, 0, 5], [5, 0, 0], [0, 0, 0], [0, 4, 0]], (1, 0), 5),
        ([[0, 7, 6], [0, 0, 0], [5, 0, 0]], (0, 0), 7),
        ([[4, 0, 4, 0], [0, 0, 0, 2], [0, 4, 0, 0], [0, 0, 0, 0]], (1, 0), 4),
        # A cell of height 2 whose neighbours are all taller has no supporter.
        ([[0, 0, 4, 2], [0, 0, 0, 4]], (1, 0), 4),
    ],
)
def test_termes_rejects_boards_without_scaffold(goal: list[list[int]], depot: tuple[int, int], max_height: int) -> None:
    assert not has_scaffold(goal, depot, max_height)


def test_termes_accepted_tiny_boards_are_solvable() -> None:
    rng = random.Random(0)
    accepted = 0
    for _ in range(60):
        size_x, size_y = rng.choice([(2, 3), (3, 2), (3, 3)])
        max_height = rng.randint(1, 3 if size_x * size_y < 9 else 2)
        goal = _goal_board(size_x, size_y, 1, max_height, rng.randint(1, 3), rng)
        depot = _depot(size_x, size_y, goal)
        if depot is not None and has_scaffold(goal, depot, max_height):
            accepted += 1
            assert _plan_exists(goal, depot, max_height), goal
    assert accepted >= 20


@pytest.mark.parametrize(
    "size_x,size_y,min_height,max_height,num_towers",
    [(3, 3, 1, 1, 1), (4, 4, 1, 4, 4), (6, 6, 3, 5, 6), (3, 3, 2, 3, 12)],
)
def test_termes_tasks_are_well_formed(
    size_x: int, size_y: int, min_height: int, max_height: int, num_towers: int
) -> None:
    problem = make_problem(size_x, size_y, min_height, max_height, num_towers, seed=5)
    assert problem == make_problem(size_x, size_y, min_height, max_height, num_towers, seed=5)
    name = re.search(r"termes-\d+-(\d+)x(\d+)x(\d+)", problem)
    assert name is not None
    width, depth, top = map(int, name.groups())
    assert top == max_height and width >= size_x and depth >= size_y  # the grid only grows
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    assert set(re.findall(r"\(height \S+ (n\d+)\)", init)) == {"n0"}
    goal_heights = {cell: int(h) for cell, h in re.findall(r"\(height (\S+) n(\d+)\)", goal)}
    assert len(goal_heights) == width * depth
    towers = [h for h in goal_heights.values() if h > 0]
    assert len(towers) == num_towers and max(towers) == max_height and min(towers) >= min(min_height, max_height)
    depot_fact = re.search(r"\(is-depot (\S+)\)", init)
    assert depot_fact is not None
    depot = depot_fact.group(1)
    assert f"(at {depot})" in init and goal_heights[depot] == 0
    assert "(not (has-block))" in goal


def test_termes_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    arguments = ["7", "--size_x", "5", "--size_y", "6", "--min_height", "2", "--max_height", "4", "--num_towers", "3"]
    assert main(arguments) == 0
    assert capsys.readouterr().out == make_problem(5, 6, 2, 4, 3, seed=7)


@pytest.mark.parametrize(
    "parameter,value",
    [("size_x", 0), ("num_towers", 0), ("min_height", 0), ("max_height", True), ("min_height", 5)],
)
def test_termes_rejects_invalid_parameters(parameter: str, value: bool | int) -> None:
    parameters: dict[str, Any] = {"size_x": 4, "size_y": 4, "min_height": 1, "max_height": 4, "num_towers": 2}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter if value != 5 else "min_height"):
        make_problem(**parameters)
