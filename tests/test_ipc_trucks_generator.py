import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.trucks import generator
from pypddl_datasets.generators.classical.ipc.trucks.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks/trucks"


def facts(text: str, section: str) -> set[str]:
    part = text.split(f"(:{section}", 1)[1]
    part = part.split("(:goal", 1)[0] if section == "init" else part
    return set(re.findall(r"\([^()]+\)", part))


def static(fs: set[str]) -> set[str]:
    return {f for f in fs if f.split()[0][1:] in ("free", "closer", "connected", "time-now", "le", "next")}


def deadline(text: str) -> dict[str, str]:
    goals = facts(text, "goal")
    return {g.split()[1].removeprefix("package"): g.split()[-1] for g in goals if g.startswith("(delivered")}


@pytest.mark.parametrize("pfile,args", [(1, (1, 3, 3, 2)), (7, (1, 4, 6, 3)), (19, (1, 6, 12, 5))])
def test_static_structure_matches_ipc_tasks(pfile: int, args: tuple[int, int, int, int]) -> None:
    ref = (REFERENCE / f"p{pfile:02d}.pddl").read_text().lower()
    gen = make_problem(*args, seed=pfile, name=pfile)
    assert gen == make_problem(*args, seed=pfile, name=pfile)
    assert static(facts(gen, "init")) == static(facts(ref, "init"))
    assert set(gen.split("(:objects")[1].split("(:init")[0].split()) == set(
        ref.split("(:objects")[1].split("(:init")[0].split()
    )
    assert all(deadline(gen).get(p, t) == t for p, t in deadline(ref).items())


@pytest.mark.parametrize("seed", range(5))
def test_packages_come_in_area_groups_and_move(seed: int) -> None:
    problem = make_problem(2, 4, 7, 3, seed=seed)
    starts = dict(re.findall(r"\(at (package\d+) (l\d+)\)", str(facts(problem, "init"))))
    by_location = [starts[f"package{i}"] for i in range(1, 8)]
    assert by_location[0:3].count(by_location[0]) == 3 and by_location[3:6].count(by_location[3]) == 3
    goals = facts(problem, "goal")
    assert len(goals) == 7
    for goal in goals:
        match = re.search(r"(package\d+) (l\d+)", goal)
        assert match is not None
        package, location = match.groups()
        assert starts[package] != location


def test_output_parses_strictly(tmp_path: Path) -> None:
    (tmp_path / "p.pddl").write_text(make_problem(2, 5, 9, 4, seed=3))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-t", "1", "-l", "3", "-p", "4", "-a", "2", "-n", "2", "-s", "5"]) == 0
    assert capsys.readouterr().out == make_problem(1, 3, 4, 2, seed=5, name=2)


@pytest.mark.parametrize(
    "parameter,value",
    [("num_trucks", 0), ("num_locations", 1), ("num_packages", 0), ("num_areas", 0), ("num_areas", 1.5)],
)
def test_rejects_invalid_parameters(parameter: str, value: float) -> None:
    parameters: dict[str, Any] = {"num_trucks": 1, "num_locations": 3, "num_packages": 3, "num_areas": 2}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
