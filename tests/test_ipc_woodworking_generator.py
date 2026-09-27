import re
from pathlib import Path

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.woodworking import generator as autoscale_generator
from pypddl_datasets.generators.classical.ipc.woodworking import generator
from pypddl_datasets.generators.classical.ipc.woodworking.generator import main, make_problem


def test_woodworking_ipc_domain_keeps_board_size_on_cut():
    # IPC 2008/2011 cut-board adds the new size without deleting the old one; Autoscale's file deletes it.
    ipc = Path(generator.__file__).with_name("domain.pddl").read_text()
    autoscale = Path(autoscale_generator.__file__).with_name("domain.pddl").read_text()
    assert "(not (boardsize" not in ipc and "(not (boardsize" in autoscale


@pytest.mark.parametrize("module", [generator, autoscale_generator])
@pytest.mark.parametrize("num_parts,num_machines,wood_factor", [(3, 1, 1.0), (12, 2, 1.4)])
def test_woodworking_parses_against_package_domain(module, num_parts, num_machines, wood_factor, tmp_path: Path):
    problem = module.make_problem(num_parts, num_machines, wood_factor, seed=3)
    assert problem == module.make_problem(num_parts, num_machines, wood_factor, seed=3) == problem.lower()
    assert re.search(r"^\s*((?:p\d+ )+)- part$", problem, re.M).group(1).split() == [f"p{i}" for i in range(num_parts)]
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(problem)
    Parser(Path(module.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_woodworking_cli_matches_make_problem(capsys):
    assert main(["1.2", "4", "1", "-s", "2"]) == 0
    assert capsys.readouterr().out == make_problem(4, 1, 1.2, seed=2)
