import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.game_2048 import generator
from pypddl_datasets.generators.numeric.ipc.game_2048.generator import Board, main, make_problem, move

REFERENCE = Path(__file__).resolve().parents[1] / "data/numeric/ipc2026/2048"
MOVES = {"up": "u", "down": "d", "left": "l", "right": "r"}


def board_and_solution(text: str) -> tuple[Board, list[str], int]:
    init, goal = text.split("(:init")[1].split("(:goal")
    values: dict[str, str] = dict(re.findall(r"\(= \(value (p\d\d)\) (\d+)\)", init))
    board = tuple(tuple(int(values[f"p{r}{c}"]) for c in range(1, 5)) for r in range(1, 5))
    match = re.search(r"\(= \(value p11\) (\d+)\)", goal)
    assert match is not None
    target = int(match.group(1))
    return board, [MOVES[m] for m in text.splitlines()[0].split(":")[1].split()], target


def solved(board: Board, moves: list[str], target: int) -> bool:
    for m in moves:
        board = move(board, m)
    return board == tuple(tuple(target if (r, c) == (0, 0) else 0 for c in range(4)) for r in range(4))


@pytest.mark.parametrize("path", sorted(REFERENCE.glob("pfile*.pddl")), ids=lambda p: p.name)
def test_move_matches_the_domain_on_every_reference_solution(path: Path) -> None:
    assert solved(*board_and_solution(path.read_text()))


@pytest.mark.parametrize("target,num_moves", [(128, 8), (1024, 14), (8192, 20), (2048, 29)])
def test_recorded_solution_reaches_the_goal(target: int, num_moves: int) -> None:
    problem = make_problem(target, num_moves, seed=3)
    assert problem == make_problem(target, num_moves, seed=3)
    board, moves, goal = board_and_solution(problem)
    assert goal == target == sum(map(sum, board)) and len(moves) == num_moves
    assert solved(board, moves, target)


def test_parses_strictly_and_cli(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(512, 12, seed=1))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")
    assert main(["-t", "512", "-n", "12", "-s", "1"]) == 0
    assert capsys.readouterr().out == make_problem(512, 12, seed=1)
    with pytest.raises(ValueError, match="target"):
        make_problem(100, 5)
