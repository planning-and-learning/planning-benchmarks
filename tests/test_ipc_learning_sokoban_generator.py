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
    problem = make_problem(grid_size=8, boxes=1, seed=seed)
    assert problem == make_problem(grid_size=8, boxes=1, seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-g", "8", "-b", "1", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(grid_size=8, boxes=1, seed=3)


@pytest.mark.parametrize("name", ["easy_p01", "easy_p10", "medium_p01"])
def test_matches_learning_reference_tasks(name: str) -> None:
    reference = LEARNING_DOMAIN.with_name(f"{name}.pddl").read_text()
    parameters = {key: int(value) for key, value in re.findall(
        r"(grid_size|boxes|seed)=(\d+)", reference.splitlines()[0]
    )}
    generated = make_problem(**parameters)
    reference_init, reference_goal = reference.split("(:init")[1].split("(:goal")
    generated_init, generated_goal = generated.split("(:init")[1].split("(:goal")
    # Ignore serialization order; preserve every initial fact and goal assignment.
    assert set(re.findall(r"\([^()]+\)", generated_init)) == set(re.findall(r"\([^()]+\)", reference_init))
    assert set(re.findall(r"\([^()]+\)", generated_goal)) == set(re.findall(r"\([^()]+\)", reference_goal))


@pytest.mark.parametrize("grid_size,boxes", [(4, 1), (8, 0), (8, 17)])
def test_rejects_invalid_parameters(grid_size: int, boxes: int) -> None:
    with pytest.raises(ValueError):
        make_problem(grid_size, boxes)


def test_sampling_failure_is_reported_without_retrying() -> None:
    with pytest.raises(ValueError, match="upstream Sokoban sampling failed"):
        make_problem(grid_size=6, boxes=2, seed=0)


State = tuple[str, tuple[tuple[str, str], ...]]


def _solvable(text: str) -> bool:
    init, goal = text.split("(:init")[1].split("(:goal")
    step: dict[tuple[str, str], str] = {
        (a, d): b for a, b, d in re.findall(r"\(adjacent ([^()\s]+) ([^()\s]+) (\w+)\)", init)
    }
    target: dict[str, str] = dict(re.findall(r"\(at (box\d+) ([^()\s]+)\)", goal))
    robot_match = re.search(r"\(at-robot ([^()\s]+)\)", init)
    assert robot_match is not None
    start: State = (robot_match.group(1), tuple(sorted(re.findall(r"\(at (box\d+) ([^()\s]+)\)", init))))
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
    assert _solvable(make_problem(grid_size=7, boxes=2, seed=seed))
