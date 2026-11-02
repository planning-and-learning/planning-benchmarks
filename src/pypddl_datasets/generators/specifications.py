"""Public discovery and loading of self-contained distribution contracts."""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, fields, is_dataclass
from functools import lru_cache
from importlib import resources
from typing import TYPE_CHECKING, cast

from ._specifications.syntax import Definition, SpecificationError, parse_definition

if TYPE_CHECKING:
    from ._specifications.core import Specification

Scalar = str | int | float | bool | None


@dataclass(frozen=True)
class Evidence:
    """Verification scope, never an implicit general completeness claim."""
    scope: str
    cases: tuple[str, ...]
    limitations: tuple[str, ...] = ()


@dataclass(frozen=True)
class SpecificationDescription:
    """Immutable distribution documentation, available without solver imports."""
    domain: str
    distribution_revision: str
    parameters: tuple[str, ...]
    probability_law: str
    solvability: str
    evidence: Evidence
    parameter_constraints: tuple[str, ...] = ()

    @property
    def source(self) -> str:
        """The complete declarative contract, including its logical rules."""
        return _definition(self.domain).source_text


def _domains() -> tuple[str, ...]:
    root = resources.files("pypddl_datasets.generators").joinpath("classical")
    return tuple(sorted(child.name for child in root.iterdir()
                        if child.is_dir() and child.joinpath("distribution.spec").is_file()))


@lru_cache(maxsize=None)
def _definition(domain: str) -> Definition:
    if domain not in _domains():
        raise KeyError(f"Unknown generator specification: {domain!r}")
    name = f"classical/{domain}/distribution.spec"
    source = resources.files("pypddl_datasets.generators").joinpath(name).read_text(encoding="utf-8")
    definition = parse_definition(source, name)
    if definition.distribution != domain:
        raise SpecificationError(f"{name}: distribution identifier must be {domain!r}")
    return definition


def _text(definition: Definition, field: str) -> str:
    value = definition.metadata.get(field)
    if not isinstance(value, str):
        raise SpecificationError(f"{definition.source_name}: metadata {field!r} must be a string")
    return value


def _texts(definition: Definition, field: str) -> tuple[str, ...]:
    value = definition.metadata.get(field)
    if not isinstance(value, tuple):
        raise SpecificationError(f"{definition.source_name}: metadata {field!r} must be a string list")
    return value


def get_specification(domain: str) -> SpecificationDescription:
    """Read a domain's parameter, probability, evidence, and source descriptions."""
    definition = _definition(domain)
    return SpecificationDescription(
        domain, definition.revision, tuple(parameter.name for parameter in definition.parameters),
        _text(definition, "probability"), _text(definition, "solvability"),
        Evidence(_text(definition, "scope"), _texts(definition, "cases"), _texts(definition, "limitations")),
        definition.constraint_sources,
    )


def list_specifications() -> tuple[SpecificationDescription, ...]:
    """List all shipped contracts without importing Z3 or the PDDL parser."""
    return tuple(get_specification(domain) for domain in _domains())


def discover_specifications() -> tuple[SpecificationDescription, ...]:
    """Alias for :func:`list_specifications`."""
    return list_specifications()


def _parameter_values(parameters: object) -> dict[str, Scalar]:
    if is_dataclass(parameters) and not isinstance(parameters, type):
        supplied: Mapping[object, object] = {field.name: getattr(parameters, field.name) for field in fields(parameters)}
    elif isinstance(parameters, Mapping):
        supplied = cast(Mapping[object, object], parameters)
    else:
        raise SpecificationError("parameters must be a dataclass instance or a mapping")
    result: dict[str, Scalar] = {}
    for name, value in supplied.items():
        if not isinstance(name, str) or (value is not None and not isinstance(value, (str, int, float, bool))):
            raise SpecificationError("parameters must map string names to scalar values")
        result[name] = value
    return result


def load_specification(domain: str, parameters: object, *, max_groundings: int | None = None) -> Specification:
    """Compile a contract for typed parameters or a mapping; requires ``[specs]``.

    Only parsed definitions are cached. Every call constructs a fresh Specification and constraints;
    its solver methods create fresh solvers. A supplied grounding budget raises SpecificationError on
    exhaustion; it never silently truncates the permitted distribution.
    """
    definition = _definition(domain)
    from ._specifications.compiler import compile_definition
    return compile_definition(definition, _parameter_values(parameters), max_groundings)
