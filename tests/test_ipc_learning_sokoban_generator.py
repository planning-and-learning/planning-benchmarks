import re
from collections import deque
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.sokoban import generator
from pypddl_datasets.generators.classical.ipc_learning.sokoban.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = (
    Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/sokoban_ipc2023_learning/domain.pddl"
)


def test_domain_file_is_the_learning_track_file() -> None:
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed: int, tmp_path: Path) -> None:
    problem = make_problem(*(8, 8, 20, 2), seed=seed)
    assert problem == make_problem(*(8, 8, 20, 2), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-x", "8", "-y", "8", "-f", "20", "-b", "2", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(8, 8, 20, 2), seed=3)


State = tuple[str, tuple[tuple[str, str], ...]]


def _solvable(text: str) -> bool:
    init, goal = text.split("(:init")[1].split("(:goal")
    step: dict[tuple[str, str], str] = {(a, d): b for a, b, d in re.findall(r"\(adjacent (\S+) (\S+) (\w+)\)", init)}
    target: dict[str, str] = dict(re.findall(r"\(at (box\d+) (\S+)\)", goal))
    robot_match = re.search(r"\(at-robot (\S+)\)", init)
    assert robot_match is not None
    start: State = (robot_match.group(1), tuple(sorted(re.findall(r"\(at (box\d+) (\S+)\)", init))))
    seen: set[State] = {start}
    queue: deque[State] = deque([start])
    while queue:
        robot, boxes = queue.popleft()
        where = dict(boxes)
        if where == target:
            return True
        at = {cell: box for box, cell in where.items()}
        for direction in ("up", "down", "left", "right"):
            nxt = step.get((robot, direction))
            if nxt is None:
                continue
            if nxt in at:
                beyond = step.get((nxt, direction))
                if beyond is None or beyond in at:
                    continue
                boxes = tuple(sorted({**where, at[nxt]: beyond}.items()))
            state = (nxt, boxes if nxt in at else tuple(sorted(where.items())))
            if state not in seen:
                seen.add(state)
                queue.append(state)
    return False


@pytest.mark.parametrize("seed", range(5))
def test_every_box_reaches_its_own_goal(seed: int) -> None:
    # style="learning" names one goal cell per box; the tracked reverse pulls must solve it
    assert _solvable(make_problem(7, 7, 14, 2, seed=seed))
