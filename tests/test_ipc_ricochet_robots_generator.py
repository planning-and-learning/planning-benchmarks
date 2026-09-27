import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.ricochet_robots import generator
from pypddl_datasets.generators.classical.ipc.ricochet_robots.generator import main, make_problem, optimal_moves

IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def parse(problem):
    init, goal = problem.split("(:goal", 1)
    size = int(re.search(r"ricochet-robots-(\d+)x", problem).group(1))
    blocked = {(int(x), int(y), d) for x, y, d in re.findall(r"\(blocked cell-(\d+)-(\d+) (\w+)\)", init)}
    at = dict(re.findall(r"\(at robot-(\d) cell-(\d+-\d+)\)", init))
    robots = [tuple(map(int, at[str(i)].split("-"))) for i in range(1, 5)]
    robot, cell = re.search(r"\(at robot-(\d) cell-(\d+-\d+)\)", goal).groups()
    return size, blocked, robots, int(robot) - 1, tuple(map(int, cell.split("-")))


@pytest.mark.parametrize("size", [3, 5, 8])
def test_tasks_are_solvable_and_need_a_move(size):
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


def test_asp2015_board_matches_the_ipc_board():
    ipc = (IPC / "ricochet-robots-opt23-adl/p01.pddl").read_text().lower()
    ours = make_problem(16, seed=1, board="asp2015", max_states=200_000)
    facts = lambda t, p: set(re.findall(rf"\({p} [^()]*\)", re.sub(r";[^\n]*", "", t.split("(:goal")[0])))
    for predicate in ("blocked", "next"):
        assert facts(ours, predicate) == facts(ipc, predicate)
    assert parse(ours)[2] == [(1, 1), (1, 16), (16, 1), (16, 16)]


@pytest.mark.parametrize("board", ["random", "asp2015"])
def test_output_parses_strictly(board, tmp_path):
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(make_problem(6 if board == "random" else 16, seed=2, board=board, max_states=200_000))
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["5", "-s", "4", "-b", "6"]) == 0
    assert capsys.readouterr().out == make_problem(5, num_barriers=6, seed=4)


@pytest.mark.parametrize(
    "kwargs",
    [dict(board_size=2), dict(board_size=4, num_barriers=25), dict(board_size=4, board="classic"), dict(board_size=10, board="asp2015")],
)
def test_rejects_invalid_parameters(kwargs):
    with pytest.raises(ValueError):
        make_problem(**kwargs)
