import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.labyrinth import generator
from pypddl_datasets.generators.classical.ipc.labyrinth.generator import main, make_problem

IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def _norm(text):
    return re.sub(r"\s+", " ", text.lower()).strip()


@pytest.mark.parametrize("track", ["opt", "sat"])
def test_labyrinth_reproduces_every_ipc_task(track):
    for path in sorted((IPC / f"labyrinth-{track}23-adl").glob("p*.pddl")):
        text = path.read_text()
        size, rotations, seed = map(int, re.search(r"size-(\d+)-rotations-(\d+)-seed-(\d+)", text).groups())
        assert _norm(make_problem(size, rotations, seed)) == _norm(text), path.name


@pytest.mark.parametrize("size,rotations", [(3, 0), (4, 2), (7, 5)])
def test_labyrinth_structure(size, rotations):
    problem = make_problem(size, rotations, seed=11)
    assert problem == make_problem(size, rotations, seed=11) == problem.lower()
    cards = re.findall(r"\(card-at (card\d+) pos(\d+) pos(\d+)\)", problem)
    assert sorted(c for c, _, _ in cards) == sorted(f"card{i}" for i in range(size * size))
    assert ("card0", "0", "0") in cards and "(robot-at card0)" in problem
    walls = re.findall(r"\(blocked (card\d+) ([nesw])\)", problem)
    assert all(sum(c == card for c, _ in walls) <= 2 for card, _, _ in cards)


def test_labyrinth_parses_strictly(tmp_path):
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(make_problem(5, 3, seed=2))
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_labyrinth_cli_and_validation(capsys):
    assert main(["--size", "4", "--num-rotations", "2", "--seed", "5"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2, 5)
    for kwargs in (dict(size=2, num_rotations=0), dict(size=4, num_rotations=-1), dict(size=4, num_rotations=1, seed=-1)):
        with pytest.raises(ValueError):
            make_problem(**kwargs)
