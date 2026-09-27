import re
from collections import Counter
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.rubiks_cube import generator
from pypddl_datasets.generators.classical.ipc.rubiks_cube.generator import MOVES, main, make_problem


def _search(pattern: str, text: str) -> re.Match[str]:
    match = re.search(pattern, text)
    assert match is not None, pattern
    return match


IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def _norm(text: str):
    return re.sub(r"\s+", " ", re.sub(r";[^\n]*", "", text).lower()).strip()


@pytest.mark.parametrize("track", ["opt", "sat"])
def test_rubiks_cube_reproduces_every_ipc_task(track: str) -> None:
    for path in sorted((IPC / f"rubiks-cube-{track}23-adl").glob("p*.pddl")):
        text = path.read_text()
        seed, moves = map(int, _search(r"-s (\d+) .* (\d+)\s*$", text.splitlines()[0]).groups())
        assert _norm(make_problem(moves, seed)) == _norm(text), path.name


def test_moves_are_permutations_with_inverses() -> None:
    for name, perm in MOVES.items():
        assert sorted(perm) == list(range(54))
        if not name.endswith("rev"):
            inverse = MOVES[name + "rev"]
            assert [perm[i] for i in inverse] == list(range(54))


@pytest.mark.parametrize("num_moves", [1, 5, 20])
def test_rubiks_cube_structure(num_moves: int) -> None:
    problem = make_problem(num_moves, seed=3)
    assert problem == make_problem(num_moves, seed=3) == problem.lower()
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    facts = re.findall(r"\((cube\d|edge\d\d)((?: [a-z]+)+)\)", init)
    assert len(facts) == 20
    assert Counter(c for _, colours in facts for c in colours.split()) == Counter({c: 8 for c in generator.COLOURS})


def test_rubiks_cube_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(make_problem(7, seed=1))
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_rubiks_cube_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["6", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(6, 9)
    with pytest.raises(ValueError, match="num_moves"):
        make_problem(0)
