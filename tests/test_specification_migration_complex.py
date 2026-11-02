"""Exact hard-family support and sparse grounding after migration to .spec files."""
from __future__ import annotations

from dataclasses import replace
from itertools import product
from random import Random

import pytest

from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators.classical.nomystery.parameters import Parameters as TransportParameters
from pypddl_datasets.generators.classical.rovers.generator import Parameters as RoverParameters, sample as sample_rovers
from pypddl_datasets.generators.classical.woodworking.parameters import Parameters as WoodParameters
from pypddl_datasets.generators.runtime import Atom, atom, render_problem

pytest.importorskip("z3")
pytest.importorskip("pypddl")


@pytest.mark.parametrize("requested_cameras,expected_count", [(0, 31), (1, 28)])
def test_rover_singleton_complete_task_support(requested_cameras: int, expected_count: int) -> None:
    specification = load_specification("rovers", RoverParameters(1, 1, 1, requested_cameras, 1))
    result = specification.enumerate(limit=expected_count, timeout_ms=10_000)
    assert result.complete and len(result.situations) == expected_count
    actual: set[tuple[bool, bool, bool, frozenset[str]]] = set()
    for situation in result.situations:
        true_atoms = {(key.predicate, key.arguments) for key, value in situation.values if key.kind == "atom" and value}
        equipment = tuple((f"equipped_for_{kind}", ("rover0",)) in true_atoms
                          for kind in ("soil_analysis", "rock_analysis", "imaging"))
        modes = frozenset(args[1] for predicate, args in true_atoms if predicate == "supports")
        actual.add((equipment[0], equipment[1], equipment[2], modes))
    nonempty_modes = [frozenset(mode for mode, chosen in zip(("colour", "high_res", "low_res"), flags) if chosen)
                      for flags in product((False, True), repeat=3) if any(flags)]
    expected = {(soil, rock, True, modes) for soil, rock in product((False, True), repeat=2) for modes in nonempty_modes}
    if requested_cameras == 0:
        expected.update((soil, rock, False, frozenset()) for soil, rock in product((False, True), repeat=2) if soil or rock)
    assert actual == expected


@pytest.mark.parametrize("factor", [1.0, 2.0])
def test_woodworking_resource_projection_is_exact(factor: float) -> None:
    """Only unused/size/board-size coordinates are claimed exhaustive here."""
    specification = load_specification("woodworking", WoodParameters(1, 1, factor))
    projection = [key for key in specification.semantic_variables if key.predicate in {"unused", "goalsize", "boardsize"}]
    result = specification.enumerate(limit=6, timeout_ms=10_000, projection=projection)
    assert result.complete and len(result.situations) == 6
    actual: set[frozenset[tuple[str, tuple[str, ...]]]] = set()
    for situation in result.situations:
        actual.add(frozenset((key.predicate, key.arguments) for key, value in situation.values if value))
    expected: set[frozenset[tuple[str, tuple[str, ...]]]] = set()
    for size, label in enumerate(("small", "medium", "large"), 1):
        size_fact = ("goalsize", ("p0", label))
        expected.add(frozenset((size_fact,)))
        expected.add(frozenset((size_fact, ("unused", ("p0",)), ("boardsize", ("b0", f"s{int(size * factor)}")))))
    assert actual == expected


def test_nomystery_addition_relation_is_sparse_and_complete() -> None:
    parameters = TransportParameters(3, 1, max_edge_cost=2)
    specification = load_specification("nomystery", parameters)
    # The safe fuel bound is 2P(N-1)C = 8; the table contains only arithmetically
    # valid triples, even when a particular model omits some unused costs.
    bound = 8
    actual = {key.arguments for key in specification.semantic_variables if key.predicate == "sum"}
    expected = {(f"level{after}", f"level{cost}", f"level{after + cost}")
                for cost in (1, 2) for after in range(bound - cost + 1)}
    assert actual == expected
    assert len(actual) == 15


@pytest.mark.parametrize("mutation", ["self_visibility", "self_traversal", "missing_lander", "missing_camera_modes", "impossible_soil_goal"])
def test_rover_declarative_contract_rejects_semantic_counterexamples(mutation: str) -> None:
    parameters = RoverParameters(1, 2, 1, 1, 1)
    specification = load_specification("rovers", parameters)
    problem = sample_rovers(parameters, Random(4))
    assert specification.check_pddl(render_problem(problem)).is_member
    if mutation == "self_visibility":
        problem = replace(problem, initial=(*problem.initial, atom("visible", "waypoint0", "waypoint0")))
    elif mutation == "self_traversal":
        problem = replace(problem, initial=(*problem.initial, atom("can_traverse", "rover0", "waypoint0", "waypoint0")))
    elif mutation == "missing_lander":
        problem = replace(problem, initial=tuple(fact for fact in problem.initial
                          if not isinstance(fact, Atom) or fact.predicate != "at_lander"))
    elif mutation == "missing_camera_modes":
        problem = replace(problem, initial=tuple(fact for fact in problem.initial
                          if not isinstance(fact, Atom) or fact.predicate != "supports"))
    else:
        problem = replace(problem, initial=tuple(fact for fact in problem.initial if fact != atom("at_soil_sample", "waypoint0")),
                          goal=(atom("communicated_soil_data", "waypoint0"),))
    result = specification.check_pddl(render_problem(problem))
    assert result.status == "nonmember", result
    assert result.violations != ("pddl.syntax_or_semantics",), result
