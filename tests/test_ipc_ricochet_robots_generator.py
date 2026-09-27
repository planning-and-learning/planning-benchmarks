import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.ricochet_robots import generator
from pypddl_datasets.generators.classical.ipc.ricochet_robots.generator import main, make_problem, optimal_moves

IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


Cell = tuple[int, int]
Parsed = tuple[int, set[tuple[int, int, str]], list[Cell], int, Cell]


def _cell(text: str) -> Cell:
    x, y = text.split("-")
    return int(x), int(y)


def parse(problem: str) -> Parsed:
    init, goal = problem.split("(:goal", 1)
    size_match = re.search(r"ricochet-robots-(\d+)x", problem)
    assert size_match is not None
    size = int(size_match.group(1))
    blocked = {(int(x), int(y), d) for x, y, d in re.findall(r"\(blocked cell-(\d+)-(\d+) (\w+)\)", init)}
    at: dict[str, str] = dict(re.findall(r"\(at robot-(\d) cell-(\d+-\d+)\)", init))
    robots = [_cell(at[str(i)]) for i in range(1, 5)]
    goal_match = re.search(r"\(at robot-(\d) cell-(\d+-\d+)\)", goal)
    assert goal_match is not None
    robot, cell = goal_match.groups()
    return size, blocked, robots, int(robot) - 1, _cell(cell)


@pytest.mark.parametrize("size", [3, 5, 8])
def test_tasks_are_solvable_and_need_a_move(size: int) -> None:
    problem = make_problem(size, seed=7, max_states=200_000)
    assert problem == make_problem(size, seed=7, max_states=200_000)
    n, blocked, robots, target_robot, target = parse(problem)
    assert len(set(robots)) == 4
    opposite = {"north": "south", "south": "north", "east": "west", "west": "east"}
    step = {"north": (0, -1), "south": (0, 1), "east": (1, 0), "west": (-1, 0)}
    for x, y, d in blocked:  # every inner barrier blocks both sides
        nx, ny = x + step[d][0], y + step[d][1]
        assert not (1 <= nx <= n and 1 <= ny <= n) or (nx, ny, opposite[d]) in blocked
    cost = optimal_moves(n, blocked, robots, target_robot, target, 200_000)
    assert cost is not None and cost > 0
    assert f"-{size}x{size}-{cost}-" in problem


def test_asp2015_board_matches_the_ipc_board() -> None:
    ipc = (IPC / "ricochet-robots-opt23-adl/p01.pddl").read_text().lower()
    ours = make_problem(16, seed=1, board="asp2015", max_states=200_000)

    def facts(text: str, predicate: str) -> set[str]:
        return set(re.findall(rf"\({predicate} [^()]*\)", re.sub(r";[^\n]*", "", text.split("(:goal")[0])))

    for predicate in ("blocked", "next"):
        assert facts(ours, predicate) == facts(ipc, predicate)
    assert parse(ours)[2] == [(1, 1), (1, 16), (16, 1), (16, 16)]


@pytest.mark.parametrize("board", ["random", "asp2015"])
def test_output_parses_strictly(board: str, tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(
        make_problem(6 if board == "random" else 16, seed=2, board=board, max_states=200_000)
    )
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["5", "-s", "4", "-b", "6"]) == 0
    assert capsys.readouterr().out == make_problem(5, num_barriers=6, seed=4)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"board_size": 2},
        {"board_size": 4, "num_barriers": 25},
        {"board_size": 4, "board": "classic"},
        {"board_size": 10, "board": "asp2015"},
    ],
)
def test_rejects_invalid_parameters(kwargs: dict[str, Any]) -> None:
    with pytest.raises(ValueError):
        make_problem(**kwargs)
