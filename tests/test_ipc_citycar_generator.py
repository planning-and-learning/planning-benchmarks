import re
from collections import Counter
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.citycar import generator
from pypddl_datasets.generators.classical.ipc.citycar.generator import main, make_problem

HERE = Path(generator.__file__).parent
IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


def _kinds(text):
    return Counter(re.findall(r"\(([a-z_]+) ", re.sub(r";[^\n]*", "", text.lower()).split("(:init")[1]))


@pytest.mark.parametrize("rows,columns,cars,garages", [(2, 2, 1, 1), (3, 4, 3, 2), (4, 4, 5, 3)])
def test_citycar_structure(rows, columns, cars, garages):
    problem = make_problem(rows, columns, cars, garages, seed=5)
    assert problem == make_problem(rows, columns, cars, garages, seed=5) == problem.lower()
    assert len(re.findall(r"\(clear ", problem)) == rows * columns
    assert len(re.findall(r"\broad\d+\b", problem.split("(:init")[0])) == rows + 2
    assert {int(r) for r in re.findall(r"\(at_garage \S+ junction(\d+)-", problem)} == {0}
    assert {int(r) for r in re.findall(r"\(arrived \S+ junction(\d+)-", problem)} == {rows - 1}
    assert len(re.findall(r"\(starting ", problem)) == cars and "(:metric minimize (total-cost))" in problem


def test_citycar_matches_ipc_fact_counts():
    for track in ("opt", "sat"):
        for path in sorted((IPC / f"citycar-{track}14-adl").glob("p*.pddl")):
            a = list(map(int, path.stem[1:].split("-")))
            rows, columns, cars, garages, seed = a if track == "opt" else [a[0], a[0], a[1], a[2], a[4]]
            assert _kinds(make_problem(rows, columns, cars, garages, seed=seed)) == _kinds(path.read_text()), path.name


def test_density_only_blocks_interior_junctions():
    problem = make_problem(5, 5, 2, 2, density=0.0, seed=1)
    assert len(re.findall(r"\(clear ", problem)) == 25 - 9


@pytest.mark.parametrize("domain", ["domain.pddl", "domain_citycar14opt.pddl"])
def test_citycar_parses_strictly(domain, tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(4, 3, 3, 2, density=0.8, seed=2))
    options = ParserOptions()
    options.strict = True
    Parser(HERE / domain, options).parse_task(tmp_path / "p.pddl")


def test_citycar_cli_and_validation(capsys):
    assert main(["3", "3", "2", "2", "-s", "4", "--density", "0.5"]) == 0
    assert capsys.readouterr().out == make_problem(3, 3, 2, 2, density=0.5, seed=4)
    with pytest.raises(ValueError, match="num_rows"):
        make_problem(1, 3, 1, 1)
    with pytest.raises(ValueError, match="density"):
        make_problem(3, 3, 1, 1, density=1.5)
