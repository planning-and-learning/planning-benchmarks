import re
from collections.abc import Callable
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.numeric.ipc.farmland.generator import main as farm_main, make_problem as farm
from pypddl_datasets.generators.numeric.ipc.fo_farmland.generator import main as fo_main, make_problem as fo_farm

GENERATORS = Path(__file__).resolve().parents[1] / "src/pypddl_datasets/generators/numeric/ipc"
IPC = Path(__file__).resolve().parents[1] / "data/numeric/ipc2023"


def structure(text: str) -> tuple[list[str], list[str], int, bool]:
    init = re.sub(r";[^\n]*", "", text.split("(:goal")[0]).lower()
    units = sorted(int(v) for v in re.findall(r"\(x farm\d+\) (\d+)\)", init))
    fluents = sorted(set(re.findall(r"\(= \((\S+?)[ )]", init)))
    return sorted(re.findall(r"\(adj \S+ \S+\)", init)), fluents, units[-1], set(units[:-1]) <= {0, 1}


# Upstream ran under Python 2, whose randint draws differ, so the source farm and the
# 0/1 allocations cannot be reproduced; the ladder, fluents and source size can.
@pytest.mark.parametrize("package,make", [("farmland", farm), ("fo-farmland", fo_farm)])
@pytest.mark.parametrize("index", range(1, 21))
def test_initial_states_match_ipc_structure(package: str, make: Callable[..., str], index: int) -> None:
    ipc = (IPC / package / f"pfile{index}.pddl").read_text()
    match = re.search(r"instance_(\d+)_(\d+)_(\d+)_ladder", ipc)
    assert match is not None
    farms, units, seed = map(int, match.groups())
    assert structure(make(farms, units, seed=seed)) == structure(ipc)


@pytest.mark.parametrize("package,make", [("farmland", farm), ("fo_farmland", fo_farm)])
def test_farmland_structure_and_strict_parse(package: str, make: Callable[..., str], tmp_path: Path) -> None:
    problem = make(6, 500, seed=4)
    assert problem == make(6, 500, seed=4)
    units = [int(v) for v in re.findall(r"\(x farm\d+\) (\d+)\)", problem.split("(:goal")[0])]
    assert sorted(units)[-1] == 500 and all(u in (0, 1) for u in sorted(units)[:-1])
    assert len(re.findall(r"\(adj ", problem)) == 2 * 7  # ladder of 3 rungs: 7 undirected edges
    weights = [float(w) for w in re.findall(r"\(\* ([\d.]+) \(x farm\d+\)\)", problem)]
    assert len(weights) == 6 and all(1.0 <= w <= 2.0 for w in weights) and "700.0)" in problem
    assert ("(cost))" in problem.split("(:goal")[1]) == (package == "fo_farmland")
    (tmp_path / "p.pddl").write_text(problem)
    options = ParserOptions()
    options.strict = True
    Parser(GENERATORS / package / "domain.pddl", options).parse_task(tmp_path / "p.pddl")


def test_farmland_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert farm_main(["-f", "4", "-u", "300", "-s", "1"]) == 0
    assert capsys.readouterr().out == farm(4, 300, seed=1)
    assert fo_main(["-f", "4", "-u", "300", "-s", "1"]) == 0
    assert capsys.readouterr().out == fo_farm(4, 300, seed=1)
    for num_farms, num_units in ((3, 10), (1, 10), (4, 0)):
        with pytest.raises(ValueError):
            farm(num_farms, num_units)
