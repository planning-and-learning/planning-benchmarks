import re
from collections.abc import Callable
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.fo_sailing.generator import main as fo_main, make_problem as fo_sail
from pypddl_datasets.generators.numeric.ipc.sailing.generator import main as sail_main, make_problem as sail

GENERATORS = Path(__file__).resolve().parents[1] / "src/pypddl_datasets/generators/numeric/ipc"
IPC = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023"


def facts(text: str) -> tuple[list[str], list[str]]:
    text = re.sub(r";[^\n]*", "", text).lower()
    return sorted(re.findall(r"\(= \([^()]*\) -?\d+\)", text)), sorted(re.findall(r"\(saved \S+\)", text))


@pytest.mark.parametrize("package,make", [("sailing", sail), ("fo-sailing", fo_sail)])
@pytest.mark.parametrize("index", range(1, 21))
def test_reproduces_ipc_tasks(package: str, make: Callable[..., str], index: int) -> None:
    ipc = (IPC / package / f"pfile{index}.pddl").read_text()
    match = re.search(r"instance_(\d+)_(\d+)_(\d+)", ipc)
    assert match is not None
    boats, people, seed = map(int, match.groups())
    distances = [int(d) for d in re.findall(r"\(d p\d+\) (-?\d+)\)", ipc)]
    if min(distances) >= 0 and package == "fo-sailing":  # the 5-boat tasks: 0..500, seeds not recoverable
        problem = make(boats, people, seed=seed, nonnegative_distances=True)
        assert all(0 <= int(d) <= 500 for d in re.findall(r"\(d p\d+\) (-?\d+)\)", problem))
        assert len(facts(problem)[0]) == len(facts(ipc)[0])
    else:
        assert facts(make(boats, people, seed=seed)) == facts(ipc)


@pytest.mark.parametrize("package,make", [("sailing", sail), ("fo_sailing", fo_sail)])
def test_sailing_structure_and_strict_parse(package: str, make: Callable[..., str], tmp_path: Path) -> None:
    problem = make(3, 6, seed=5)
    assert problem == make(3, 6, seed=5)
    xs = [int(x) for x in re.findall(r"\(x b\d+\) (-?\d+)\)", problem)]
    assert len(xs) == 3 and all(-10 <= x <= 10 for x in xs)
    assert len(re.findall(r"\(saved p\d+\)", problem)) == 6
    assert (len(re.findall(r"\(= \(v b\d+\) 1\)", problem)) == 3) == (package == "fo_sailing")
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(GENERATORS / package / "domain.pddl", options).parse_task(tmp_path / "p.pddl")


def test_sailing_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert sail_main(["-b", "2", "-p", "3", "-s", "1"]) == 0
    assert capsys.readouterr().out == sail(2, 3, seed=1)
    assert fo_main(["-b", "2", "-p", "3", "-s", "1", "--nonnegative-distances"]) == 0
    assert capsys.readouterr().out == fo_sail(2, 3, seed=1, nonnegative_distances=True)
    for num_boats, num_people in ((0, 1), (1, 0)):
        with pytest.raises(ValueError):
            sail(num_boats, num_people)
