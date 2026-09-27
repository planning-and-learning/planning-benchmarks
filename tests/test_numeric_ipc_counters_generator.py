import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.counters import generator
from pypddl_datasets.generators.numeric.ipc.counters.generator import main, make_problem

IPC = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023/counters"


def body(text: str):
    return re.sub(r"\s+", " ", re.sub(r";[^\n]*", "", text).lower().split("(:objects", 1)[1]).strip()


@pytest.mark.parametrize("init", ["zero", "reverse", "random"])
def test_counters_structure_and_strict_parse(init: str, tmp_path: Path) -> None:
    problem = make_problem(6, init, seed=3)
    assert problem == make_problem(6, init, seed=3)
    values = [int(v) for v in re.findall(r"\(value c\d+\) (\d+)\)", problem.split("(:goal", maxsplit=1)[0])]
    assert len(values) == 6 and all(0 <= v < 12 for v in values) and "(= (max_int) 12)" in problem
    assert len(re.findall(r"\(<= \(\+ \(value c(\d+)\) 1\) \(value c(\d+)\)\)", problem)) == 5
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(Path(generator.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


@pytest.mark.parametrize("index,init", [(1, "reverse"), (3, "zero"), (8, "zero"), (15, "reverse")])
def test_counters_reproduce_ipc_zero_and_reverse_tasks(index: int, init: str) -> None:
    ipc = (IPC / f"pfile{index}.pddl").read_text()
    n = len(re.findall(r"\(value c\d+\)", ipc.split("(:goal")[0]))
    assert body(make_problem(n, init)).split(")", 1)[1] == body(ipc).split(")", 1)[1]


def test_counters_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-n", "4", "-i", "random", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(4, "random", seed=2)
    bad: dict[str, Any]
    for bad in ({"num_counters": 1}, {"num_counters": 4, "init": "up"}):
        with pytest.raises(ValueError):
            make_problem(**bad)
