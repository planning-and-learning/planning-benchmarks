import re
from pathlib import Path
from types import ModuleType

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.autoscale.miconic import generator as autoscale_generator
from pypddl_datasets.generators.classical.ipc.miconic import generator
from pypddl_datasets.generators.classical.ipc.miconic.generator import main, make_problem


@pytest.mark.parametrize("num_floors,num_passengers", [(2, 1), (20, 10)])
def test_miconic_ipc_encoding_uses_type_predicates(num_floors: int, num_passengers: int) -> None:
    problem = make_problem(num_floors, num_passengers, seed=4)
    assert problem == make_problem(num_floors, num_passengers, seed=4) == problem.lower()
    init = problem.split("(:init", 1)[1].split("(:goal", 1)[0]
    assert set(re.findall(r"\(passenger (\w+)\)", init)) == {f"p{i}" for i in range(num_passengers)}
    assert set(re.findall(r"\(floor (\w+)\)", init)) == {f"f{i}" for i in range(num_floors)}
    assert " - " not in problem


def facts(problem: str, name: str) -> list[str]:
    return re.findall(rf"\({name} \w+ \w+\)", problem)


def test_miconic_ipc_and_autoscale_share_the_distribution() -> None:
    untyped, typed = make_problem(8, 4, seed=1), autoscale_generator.make_problem(8, 4, seed=1)
    assert facts(untyped, "origin") == facts(typed, "origin") and facts(untyped, "destin") == facts(typed, "destin")
    assert "p0 p1 p2 p3 - passenger" in typed


@pytest.mark.parametrize("module", [generator, autoscale_generator])
def test_miconic_parses_against_package_domain(module: ModuleType, tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    (tmp_path / "p.pddl").write_text(module.make_problem(6, 3, seed=2))
    assert module.__file__ is not None
    Parser(Path(module.__file__).with_name("domain.pddl"), options).parse_task(tmp_path / "p.pddl")


def test_miconic_ipc_cli_and_validation(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-f", "4", "-p", "2", "-s", "5"]) == 0
    assert capsys.readouterr().out == make_problem(4, 2, seed=5)
    with pytest.raises(ValueError, match="num_floors"):
        make_problem(1, 1)
