import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.mprime import generator
from pypddl_datasets.generators.classical.autoscale.mprime.generator import main, make_problem

AGILE = Path(__file__).resolve().parents[1] / "data/classical/autoscale-benchmarks-main/21.11-agile-strips/mprime"


@pytest.mark.parametrize("locations,fuel,space,vehicles,cargos", [(2, 1, 1, 1, 1), (10, 8, 3, 3, 6)])
def test_mprime_ring_fuel_space_and_goals(locations, fuel, space, vehicles, cargos, tmp_path):
    problem = make_problem(locations, fuel, space, vehicles, cargos, seed=2)
    assert problem == make_problem(locations, fuel, space, vehicles, cargos, seed=2) == problem.lower()
    init, goal = problem.split("(:init", 1)[1].split("(:goal", 1)
    conn = set(re.findall(r"\(conn l(\d+) l(\d+)\)", init))
    assert all((b, a) in conn for a, b in conn) and len({a for a, _ in conn}) == locations
    assert all(0 <= int(f) <= fuel for f in re.findall(r"\(has-fuel l\d+ f(\d+)\)", init))
    assert all(1 <= int(s) <= space for s in re.findall(r"\(has-space v\d+ s(\d+)\)", init))
    assert len(re.findall(r"\(at c\d+ l\d+\)", goal)) == cargos
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")  # pyright: ignore[reportUnknownMemberType]


def test_mprime_static_facts_match_agile_task():
    reference = re.sub(r"[ \t]+", " ", (AGILE / "p02.pddl").read_text().lower())  # l5-f15-s2-v8-c10
    problem = make_problem(5, 15, 2, 8, 10, seed=0)
    static = lambda text: sorted(re.findall(r"\((?:not-equal|fuel-neighbor|space-neighbor|conn) [^()]*\)", text))  # noqa: E731
    assert static(problem) == static(reference)


def test_mprime_cli_matches_make_problem(capsys):
    assert main(["-l", "5", "-f", "4", "-s", "2", "-v", "2", "-c", "3", "-r", "7"]) == 0
    assert capsys.readouterr().out == make_problem(5, 4, 2, 2, 3, seed=7)
    with pytest.raises(ValueError, match="num_locations"):
        make_problem(1, 1, 1, 1, 1)
