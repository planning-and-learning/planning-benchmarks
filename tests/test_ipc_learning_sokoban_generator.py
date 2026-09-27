from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.sokoban import generator
from pypddl_datasets.generators.classical.ipc_learning.sokoban.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/sokoban_ipc2023_learning/domain.pddl"


def test_domain_file_is_the_learning_track_file():
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed, tmp_path):
    problem = make_problem(*(8, 8, 20, 2), seed=seed)
    assert problem == make_problem(*(8, 8, 20, 2), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["-x", "8", "-y", "8", "-f", "20", "-b", "2", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(8, 8, 20, 2), seed=3)


def _solvable(text):
    import re
    from collections import deque

    init, goal = text.split("(:init")[1].split("(:goal")
    step = {(a, d): b for a, b, d in re.findall(r"\(adjacent (\S+) (\S+) (\w+)\)", init)}
    target = dict(re.findall(r"\(at (box\d+) (\S+)\)", goal))
    start = (re.search(r"\(at-robot (\S+)\)", init).group(1), tuple(sorted(re.findall(r"\(at (box\d+) (\S+)\)", init))))
    seen, queue = {start}, deque([start])
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
def test_every_box_reaches_its_own_goal(seed):
    # style="learning" names one goal cell per box; the tracked reverse pulls must solve it
    assert _solvable(make_problem(7, 7, 14, 2, seed=seed))
