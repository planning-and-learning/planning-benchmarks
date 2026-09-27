from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.rovers import generator
from pypddl_datasets.generators.classical.ipc_learning.rovers.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/rovers_ipc2023_learning/domain.pddl"


def test_domain_file_is_the_learning_track_file():
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed, tmp_path):
    problem = make_problem(*(2, 6, 3, 2, 4), seed=seed)
    assert problem == make_problem(*(2, 6, 3, 2, 4), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["2", "6", "3", "2", "4", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(2, 6, 3, 2, 4), seed=3)


@pytest.mark.parametrize("learning", [True, False])
def test_graph_and_goal_options(learning, tmp_path):
    import re

    kwargs = {} if learning else dict(learning_graphs=False, learning_goals=False)
    dense = [make_problem(2, 40, 3, 2, 4, seed=s, **kwargs) for s in range(10)]
    visible_per_waypoint = sum(len(re.findall(r"\(visible ", t)) for t in dense) / (10 * 40)
    tasks = [make_problem(1, 4, 1, 1, 2, seed=s, **kwargs) for s in range(100)]
    no_image = sum("communicated_image" not in t.split("(:goal")[1] for t in tasks)
    assert all("communicated" in t.split("(:goal")[1] for t in tasks)
    if learning:
        assert visible_per_waypoint > 12 and no_image > 0
    else:
        assert visible_per_waypoint < 12 and no_image == 0
    (tmp_path / "p.pddl").write_text(tasks[0])
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]
