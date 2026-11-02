"""Public loading, parameter boundaries, and source diagnostics."""
from __future__ import annotations

from collections.abc import Mapping

import pytest

from pypddl_datasets.generators import SpecificationError, get_specification, load_specification
from pypddl_datasets.generators.classical.gripper.parameters import Parameters


def test_mapping_and_dataclass_produce_the_same_support() -> None:
    pytest.importorskip("z3")
    mapped = load_specification("gripper", {"num_balls": 2}).enumerate(limit=1)
    typed = load_specification("gripper", Parameters(2)).enumerate(limit=1)
    assert mapped.complete and typed.complete
    assert mapped.situations == typed.situations


@pytest.mark.parametrize("parameters,message", [
    ({}, "missing parameter"),
    ({"num_balls": 1, "extra": 2}, "unknown parameters"),
    ({"num_balls": True}, "integer"),
    ({"num_balls": 1.5}, "integer"),
    ({"num_balls": None}, "integer"),
    ({"num_balls": 0}, "constraint"),
])
def test_mapping_validation_is_independent_of_dataclasses(
    parameters: Mapping[str, object], message: str,
) -> None:
    pytest.importorskip("z3")
    with pytest.raises(SpecificationError, match=message):
        load_specification("gripper", parameters)


def test_parameter_error_and_named_rule_point_into_public_source() -> None:
    pytest.importorskip("z3")
    with pytest.raises(SpecificationError) as caught:
        load_specification("gripper", {"num_balls": 0})
    span = caught.value.span
    assert span is not None and span.source == "classical/gripper/distribution.spec"
    assert "require" in get_specification("gripper").source.splitlines()[span.line - 1]
    spec = load_specification("gripper", Parameters(1))
    rules = [rule for rule in spec.initial if rule.source is not None]
    assert rules
    for rule in rules:
        assert rule.source is not None
        assert "rule" in get_specification("gripper").source.splitlines()[rule.source.line - 1]


def test_grounding_budget_fails_without_poisoning_future_loads() -> None:
    pytest.importorskip("z3")
    with pytest.raises(SpecificationError, match="budget"):
        load_specification("gripper", Parameters(100_000), max_groundings=20)
    assert load_specification("gripper", Parameters(1)).enumerate(limit=1).complete


def test_independent_loads_do_not_share_mutable_constraints() -> None:
    z3 = pytest.importorskip("z3")
    first = load_specification("gripper", Parameters(1))
    second = load_specification("gripper", Parameters(1))
    first.add("initial", "reject", z3.BoolVal(False))
    assert not first.enumerate(limit=1).situations
    remaining = second.enumerate(limit=1)
    assert remaining.complete and len(remaining.situations) == 1
