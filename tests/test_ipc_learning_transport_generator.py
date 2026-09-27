from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc_learning.transport import generator
from pypddl_datasets.generators.classical.ipc_learning.transport.generator import main, make_problem

DOMAIN = Path(generator.__file__).with_name("domain.pddl")
LEARNING_DOMAIN = Path(__file__).resolve().parents[1] / "data/classical/ipc2023-learning/transport_ipc2023_learning/domain.pddl"


def test_domain_file_is_the_learning_track_file():
    assert DOMAIN.read_bytes() == LEARNING_DOMAIN.read_bytes()


@pytest.mark.parametrize("seed", range(3))
def test_output_is_deterministic_and_parses_strictly(seed, tmp_path):
    problem = make_problem(*(6, 2, 4, 2, 1), seed=seed)
    assert problem == make_problem(*(6, 2, 4, 2, 1), seed=seed)
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["-l", "6", "-t", "2", "-p", "4", "-c", "2", "-e", "1", "-s", "3"]) == 0
    assert capsys.readouterr().out == make_problem(*(6, 2, 4, 2, 1), seed=3)


@pytest.mark.parametrize("learning", [True, False])
def test_density_and_capacity_options(learning, tmp_path):
    import re

    kwargs = {} if learning else dict(extra_edges=0, random_capacities=False)
    tasks = [make_problem(10, 4, 3, 4, seed=s, **kwargs) for s in range(20)]
    roads = [len(re.findall(r"\(road ", t)) for t in tasks]
    capacities = {c for t in tasks for c in re.findall(r"\(capacity t\d+ (\S+)\)", t)}
    if learning:
        assert max(roads) > 2 * 9 * 2 and len(capacities) > 1  # denser than a tree, mixed capacities
    else:
        assert set(roads) == {2 * 9} and capacities == {"capacity4"}
    (tmp_path / "p.pddl").write_text(tasks[0])
    options = ParserOptions()
    options.strict = True
    Parser(DOMAIN, options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]
