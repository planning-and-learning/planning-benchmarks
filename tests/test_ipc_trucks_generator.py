import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.trucks import generator
from pypddl_datasets.generators.classical.ipc.trucks.generator import main, make_problem

REFERENCE = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks/trucks"


def facts(text, section):
    part = text.split(f"(:{section}", 1)[1]
    part = part.split("(:goal", 1)[0] if section == "init" else part
    return set(re.findall(r"\([^()]+\)", part))


@pytest.mark.parametrize("pfile,args", [(1, (1, 3, 3, 2)), (7, (1, 4, 6, 3)), (19, (1, 6, 12, 5))])
def test_static_structure_matches_ipc_tasks(pfile, args):
    ref = (REFERENCE / f"p{pfile:02d}.pddl").read_text().lower()
    gen = make_problem(*args, seed=pfile, name=pfile)
    assert gen == make_problem(*args, seed=pfile, name=pfile)
    static = lambda fs: {f for f in fs if f.split()[0][1:] in ("free", "closer", "connected", "time-now", "le", "next")}
    assert static(facts(gen, "init")) == static(facts(ref, "init"))
    assert set(gen.split("(:objects")[1].split("(:init")[0].split()) == set(ref.split("(:objects")[1].split("(:init")[0].split())
    deadline = lambda text: {re.search(r"package(\d+)", g).group(1): g.split()[-1] for g in facts(text, "goal") if g.startswith("(delivered")}
    assert all(deadline(gen).get(p, t) == t for p, t in deadline(ref).items())


@pytest.mark.parametrize("seed", range(5))
def test_packages_come_in_area_groups_and_move(seed):
    problem = make_problem(2, 4, 7, 3, seed=seed)
    starts = dict(re.findall(r"\(at (package\d+) (l\d+)\)", facts(problem, "init").__str__()))
    by_location = [starts[f"package{i}"] for i in range(1, 8)]
    assert by_location[0:3].count(by_location[0]) == 3 and by_location[3:6].count(by_location[3]) == 3
    goals = facts(problem, "goal")
    assert len(goals) == 7
    for goal in goals:
        package, location = re.search(r"(package\d+) (l\d+)", goal).groups()
        assert starts[package] != location


def test_output_parses_strictly(tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(2, 5, 9, 4, seed=3))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_cli_matches_make_problem(capsys):
    assert main(["-t", "1", "-l", "3", "-p", "4", "-a", "2", "-n", "2", "-s", "5"]) == 0
    assert capsys.readouterr().out == make_problem(1, 3, 4, 2, seed=5, name=2)


@pytest.mark.parametrize("parameter,value", [("num_trucks", 0), ("num_locations", 1), ("num_packages", 0), ("num_areas", 0), ("num_areas", 1.5)])
def test_rejects_invalid_parameters(parameter, value):
    parameters = dict(num_trucks=1, num_locations=3, num_packages=3, num_areas=2)
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
