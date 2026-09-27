import re
from pathlib import Path
from typing import Any

import pytest
from pypddl.formalism import Parser, ParserOptions

from pypddl_datasets.generators.classical.ipc.miconic_fulladl import generator
from pypddl_datasets.generators.classical.ipc.miconic_fulladl.generator import main, make_problem
from pypddl_datasets.generators.classical.ipc.miconic_simpleadl import generator as simple
from pypddl_datasets.generators.classical.ipc.miconic.generator import make_problem as make_strips


def kind(problem: str, name: str) -> list[str]:
    return re.findall(rf"\({name} (\w+)\)", problem)


@pytest.mark.parametrize("passengers,seed", [(1, 0), (5, 2), (18, 1), (30, 4)])
def test_kind_counts_and_journey_restrictions(passengers: int, seed: int) -> None:
    floors = 2 * passengers
    problem = make_problem(floors, passengers, seed=seed)
    assert problem == make_problem(floors, passengers, seed=seed)
    origin = dict(re.findall(r"\(origin (\w+) (\w+)\)", problem))
    destin = dict(re.findall(r"\(destin (\w+) (\w+)\)", problem))
    assert len(origin) == len(destin) == passengers and all(origin[p] != destin[p] for p in origin)
    ups, downs = kind(problem, "going_up"), kind(problem, "going_down")
    assert len(ups) + len(downs) == int(passengers * 0.2) and not (ups and downs)
    assert len(kind(problem, "conflict_a")) == int(passengers * 0.2)
    group_b = kind(problem, "conflict_b")
    assert len(group_b) == (int(passengers * 0.8) if kind(problem, "conflict_a") else 0)
    assert not set(group_b) & set(kind(problem, "conflict_a"))
    origins_a = {origin[p] for p in kind(problem, "conflict_a")}
    assert not origins_a & {origin[p] for p in group_b}
    alones = kind(problem, "never_alone")
    assert len(kind(problem, "attendant")) == (max(1, int(passengers * 0.6)) if alones else 0)
    for p, f in re.findall(r"\(no-access (\w+) (\w+)\)", problem):
        assert f not in (origin[p], destin[p])
    assert "(:goal (forall (?p - passenger) (served ?p)))" in problem


def test_output_parses_strictly(tmp_path: Path) -> None:
    options = ParserOptions()
    options.strict = True
    for i, (domain, problem) in enumerate(
        [
            (Path(generator.__file__).with_name("domain.pddl"), make_problem(60, 30, seed=3)),
            (Path(simple.__file__).with_name("domain.pddl"), simple.make_problem(20, 10, seed=3)),
        ]
    ):
        path = tmp_path / f"p{i}.pddl"
        path.write_text(problem)
        Parser(domain, options).parse_task(path)


def test_simpleadl_is_the_typed_strips_distribution() -> None:
    assert simple.make_problem(12, 6, seed=5) == make_strips(12, 6, seed=5, typed=True)


def test_cli_matches_make_problem(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["-f", "10", "-p", "5", "-r", "2"]) == 0
    assert capsys.readouterr().out == make_problem(10, 5, seed=2)


@pytest.mark.parametrize("parameter,value", [("num_floors", 1), ("num_passengers", 0), ("vip", 101), ("attendant", -1)])
def test_rejects_invalid_parameters(parameter: str, value: int) -> None:
    parameters: dict[str, Any] = {"num_floors": 4, "num_passengers": 2}
    parameters[parameter] = value
    with pytest.raises(ValueError, match=parameter):
        make_problem(**parameters)
