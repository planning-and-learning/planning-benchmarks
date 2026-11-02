"""Preserve the public generator signatures, CLI behavior, and seed handling."""
from __future__ import annotations

from collections.abc import Callable
import importlib
import inspect
import json
from pathlib import Path
import random
from typing import Protocol, cast

import pytest

from pypddl_datasets.generators import list_specifications


class GeneratorModule(Protocol):
    make_problem: Callable[..., str | None]

    def main(self, argv: list[str] | None = None) -> int: ...


# CLI spellings deliberately differ across the historical public entry points.
CASES: dict[str, tuple[tuple[int | float, ...], str]] = {
    "barman": ((2, 3, 4), "-c 2 -i 3 -s 4 --seed 7"),
    "blocks_3": ((3,), "-b 3 -s 7"),
    "blocks_4": ((3,), "-b 3 -s 7"),
    "childsnack": ((3, 2, 0.5), "-c 3 -t 2 -g 0.5 -s 7"),
    "delivery": ((3, 2), "3 2 -s 7"),
    "driverlog": ((3, 1, 1, 2), "-l 3 -d 1 -t 1 -p 2 -s 7"),
    "ferry": ((2, 3), "-c 2 -l 3 -s 7"),
    "floortile": ((2, 3, 2), "2 3 2 -s 7"),
    "goldminer": ((3, 4), "3 4 -s 7"),
    "grid": ((2, 3), "2 3 -s 7"),
    "gripper": ((3,), "3"),
    "hiking": ((2, 3, 3), "2 3 3 -s 7"),
    "hiking_binary": ((2, 3, 3), "2 3 3 -s 7"),
    "logistics": ((2, 2, 2, 1), "2 2 2 1 -s 7"),
    "miconic": ((3, 2), "3 2 -s 7"),
    "nomystery": ((3, 1, 1.5, 2), "-l 3 -p 1 -n 1.5 -m 2 -s 7"),
    "rovers": ((2, 3, 2, 1, 2), "2 3 2 1 2 -s 7"),
    "satellite": ((2, 2, 2, 2, 2), "2 2 2 2 2 -s 7"),
    "schedule": ((2,), "-p 2 -r 7"),
    "spanner": ((2, 1, 2), "2 1 2 -s 7"),
    "tpp": ((2, 1, 2, 1, 3), "2 1 2 1 3 -s 7"),
    "visitall": ((2, 3), "-x 2 -y 3 -s 7"),
    "woodworking": ((3, 2), "1.0 3 2 -s 7"),
}
OPTIONAL_RESULT = {"floortile", "goldminer", "grid", "hiking_binary", "satellite"}


def _module(domain: str) -> GeneratorModule:
    return cast(GeneratorModule, importlib.import_module(
        f"pypddl_datasets.generators.classical.{domain}.generator"))


def _signature(function: Callable[..., object]) -> str:
    """Compare annotations independently of whether a module postpones them."""
    signature = inspect.signature(function)
    def annotation(value: object) -> str:
        return value if isinstance(value, str) else inspect.formatannotation(value)
    return str(signature.replace(
        parameters=[parameter.replace(annotation=annotation(parameter.annotation))
                    for parameter in signature.parameters.values()],
        return_annotation=annotation(signature.return_annotation),
    ))


def test_make_problem_signatures_are_preserved() -> None:
    fixture = Path(__file__).with_name("generator_signatures.json")
    expected = cast(dict[str, str], json.loads(fixture.read_text(encoding="utf-8")))
    assert set(expected) == set(CASES) == {item.domain for item in list_specifications()}
    assert {domain: _signature(_module(domain).make_problem) for domain in CASES} == expected


@pytest.mark.parametrize("domain", CASES)
def test_cli_and_wrapper_agree_without_mutating_global_rng(
    domain: str, capsys: pytest.CaptureFixture[str],
) -> None:
    module = _module(domain)
    arguments, command = CASES[domain]
    before = random.getstate()
    keywords = {} if domain == "gripper" else {"seed": 7}
    problem = module.make_problem(*arguments, **keywords)
    assert isinstance(problem, str)
    assert module.main(command.split()) == 0
    captured = capsys.readouterr()
    assert captured.out == problem
    assert captured.err == ""
    assert random.getstate() == before


@pytest.mark.parametrize("domain", CASES)
def test_invalid_wrapper_arguments_keep_their_return_convention(domain: str) -> None:
    module = _module(domain)
    arguments = (-1, *CASES[domain][0][1:])
    if domain in OPTIONAL_RESULT:
        assert module.make_problem(*arguments) is None
    else:
        with pytest.raises(ValueError):
            module.make_problem(*arguments)


@pytest.mark.parametrize("domain", ["floortile", "spanner"])
def test_custom_problem_name_is_preserved(domain: str) -> None:
    output = _module(domain).make_problem(*CASES[domain][0], seed=7, name="custom-task")
    assert output is not None and output.startswith("(define (problem custom-task)\n")


def test_rovers_seed_name_is_preserved() -> None:
    output = _module("rovers").make_problem(*CASES["rovers"][0], seed=7)
    assert output is not None and output.startswith("(define (problem roverprob7)\n")


def test_nomystery_density_alias_and_default_seed_are_preserved() -> None:
    make_problem = _module("nomystery").make_problem
    # For three locations edge_factor=1 means a complete graph, whereas the
    # Parameters class defaults to probability 0.5. The wrapper retains its alias.
    inferred = make_problem(3, 1, 1.0, 2, seed=7)
    assert inferred == make_problem(3, 1, 1.0, 2, seed=7, edge_probability=1.0)
    assert inferred != make_problem(3, 1, 1.0, 2, seed=7, edge_probability=0.5)
    assert inferred is not None and inferred.startswith(
        "(define (problem transport-l3-t1-p1---int100n100-m2---int100c100---s7---e0)\n")
    assert make_problem(3, 1, 1.0, 2) == make_problem(3, 1, 1.0, 2, seed=1)
