import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.nurikabe import generator
from pypddl_datasets.generators.classical.ipc.nurikabe.generator import main, make_problem

DATA = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def normalize(text: str) -> str:
    return " ".join(re.sub(r";[^\n]*", "", text).lower().split())


@pytest.mark.parametrize(
    "path", sorted(DATA.glob("nurikabe-*18-adl/p*.pddl")), ids=lambda p: f"{p.parent.name}/{p.name}"
)
def test_reproduces_ipc_task_from_its_name(path: Path) -> None:
    text = path.read_text()
    name = re.search(r"problem random-(\d+)x(\d+)-(\d+)", text)
    assert name is not None
    width, height, seed = map(int, name.groups())
    assert normalize(make_problem(width, height, seed)) == normalize(text)


@pytest.mark.parametrize("size,seed", [(3, 1), (6, 4), (10, 9)])
def test_islands_and_neighbours_are_consistent(size: int, seed: int) -> None:
    problem = make_problem(size, seed=seed)
    assert problem == make_problem(size, seed=seed) and problem == problem.lower()
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    sources = re.findall(r"\(source (\S+) (g\d+)\)", init)
    remaining = dict(re.findall(r"\(remaining-cells (g\d+) n(\d+)\)", init))
    assert {g for _, g in sources} == set(remaining) and all(int(n) < size for n in remaining.values())
    available = set(re.findall(r"\(available (\S+)\)", init))
    blocked = set(re.findall(r"\(blocked (\S+)\)", init))
    part_of = {c for c, _ in re.findall(r"\(part-of (\S+) (g\d+)\)", init)}
    cells = {c for c, _ in sources}
    assert not available & blocked and not available & part_of and not blocked & part_of
    assert not cells & (available | blocked | part_of)


def test_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(make_problem(7, seed=3))
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["5", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(5, seed=2)
    with pytest.raises(ValueError, match="width"):
        make_problem(1)
