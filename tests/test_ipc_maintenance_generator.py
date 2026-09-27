import re
from collections import Counter
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.maintenance import generator
from pypddl_datasets.generators.classical.ipc.maintenance.generator import main, make_problem

IPC = Path(__file__).resolve().parents[1] / "data/classical/downward-benchmarks"


@pytest.mark.parametrize("days,planes,visits", [(1, 1, 1), (10, 10, 2), (60, 180, 5)])
def test_maintenance_structure(days, planes, visits):
    problem = make_problem(days, planes, visits, seed=3)
    assert problem == make_problem(days, planes, visits, seed=3) == problem.lower()
    at = re.findall(r"\(at (ap\d+) d(\d+) (\w+)\)", problem)
    assert Counter(p for p, _, _ in at) == {f"ap{i + 1}": visits for i in range(planes)}
    assert all(1 <= int(d) <= days for _, d, _ in at) and {a for _, _, a in at} <= {"fra", "ber", "ham"}
    assert len(re.findall(r"\(today ", problem)) == days and f"d{days + 1} - day" in problem
    assert re.findall(r"\(done (\S+)\)", problem) == [f"ap{i + 1}" for i in range(planes)]


def test_maintenance_matches_ipc_fact_counts():
    for path in sorted(IPC.glob("maintenance-*14-adl/maintenance-*.pddl")):
        days, planes, visits, index = map(int, path.stem.split("-")[3:])
        count = lambda text: Counter(re.findall(r"\((today|at|done) ", text.lower()))  # noqa: E731
        assert count(make_problem(days, planes, visits, seed=index)) == count(path.read_text()), path.name


def test_maintenance_parses_strictly(tmp_path):
    (tmp_path / "p.pddl").write_text(make_problem(8, 12, 3, seed=1))
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_maintenance_cli_and_validation(capsys):
    assert main(["5", "4", "2", "-s", "9"]) == 0
    assert capsys.readouterr().out == make_problem(5, 4, 2, seed=9)
    with pytest.raises(ValueError, match="num_visits"):
        make_problem(5, 4, 0)
