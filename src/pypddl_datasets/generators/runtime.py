"""Typed values and random choices shared by the benchmark generators.

This module deliberately has no solver or parser dependency. Specifications
independently describe the semantic values produced by these constructors.
"""

from __future__ import annotations

from collections.abc import Iterable, MutableSequence, Sequence
from dataclasses import dataclass
from itertools import combinations
from fractions import Fraction
import hashlib
import json
import math
import random
import time
from typing import Literal, Protocol, TypeVar

T = TypeVar("T")
DISTRIBUTION_REVISION = "2"


class RandomSource(Protocol):
    """The random operations used by samplers and replayable test adapters."""

    def random(self) -> float: ...

    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int: ...

    def randint(self, a: int, b: int) -> int: ...

    def choice(self, seq: Sequence[T]) -> T: ...

    def sample(self, population: Sequence[T], k: int) -> list[T]: ...

    def shuffle(self, x: MutableSequence[T]) -> None: ...


def seeded_rng(seed: int | None = None) -> RandomSource:
    """Construct a local PRNG; omitted seeds retain the historical time default."""
    return random.Random(int(time.time()) if seed is None else seed)


@dataclass(frozen=True)
class Object:
    """An explicitly declared PDDL object."""

    name: str
    type_name: str | None = None


@dataclass(frozen=True)
class Atom:
    """A ground predicate or function application."""

    predicate: str
    arguments: tuple[str, ...] = ()


@dataclass(frozen=True)
class Assignment:
    """An initial numeric fluent value."""

    function: Atom
    value: int | float


@dataclass(frozen=True)
class Metric:
    """The optimization expression for a problem."""

    expression: Atom
    direction: Literal["minimize", "maximize"] = "minimize"


@dataclass(frozen=True)
class Problem:
    """A generated ground problem with a conjunctive positive goal."""

    name: str
    domain: str
    objects: tuple[Object, ...]
    initial: tuple[Atom | Assignment, ...]
    goal: tuple[Atom, ...]
    metric: Metric | None = None
    requirements: tuple[str, ...] = ()


def atom(predicate: str, *arguments: str) -> Atom:
    """Construct a ground atom without parsing PDDL text."""
    return Atom(predicate, arguments)


def objects(names: Iterable[str], type_name: str | None = None) -> tuple[Object, ...]:
    """Declare a group of objects of the same type."""
    return tuple(Object(name, type_name) for name in names)


def _render_atom(value: Atom) -> str:
    return "(" + " ".join((value.predicate, *value.arguments)) + ")"


def _render_initial(value: Atom | Assignment) -> str:
    if isinstance(value, Atom):
        return _render_atom(value)
    if not math.isfinite(value.value):
        raise ValueError("PDDL numeric values must be finite")
    return f"(= {_render_atom(value.function)} {value.value})"


def _object_lines(declarations: tuple[Object, ...]) -> list[str]:
    groups: dict[str | None, list[str]] = {}
    names: set[str] = set()
    for declaration in declarations:
        if declaration.name in names:
            raise ValueError(f"duplicate object {declaration.name!r}")
        names.add(declaration.name)
        groups.setdefault(declaration.type_name, []).append(declaration.name)
    return [
        "    " + " ".join(group) + (f" - {kind}" if kind is not None else "")
        for kind, group in groups.items()
    ]


def render_problem(problem: Problem) -> str:
    """Render semantic values deterministically; preserve atom order for review."""
    lines = [f"(define (problem {problem.name})", f"  (:domain {problem.domain})"]
    if problem.requirements:
        lines.append("  (:requirements " + " ".join(problem.requirements) + ")")
    lines.extend(["  (:objects", *_object_lines(problem.objects), "  )", "  (:init"])
    lines.extend("    " + _render_initial(value) for value in problem.initial)
    lines.extend(["  )", "  (:goal", "    (and"])
    lines.extend("      " + _render_atom(value) for value in problem.goal)
    lines.extend(["    )", "  )"])
    if problem.metric is not None:
        lines.append(
            f"  (:metric {problem.metric.direction} {_render_atom(problem.metric.expression)})"
        )
    return "\n".join([*lines, ")", ""])


@dataclass(frozen=True)
class Rejected:
    """A valid stochastic proposal rejected for an explicit reason."""

    reason: str


SampleResult = Problem | Rejected


class GenerationExhausted(RuntimeError):
    """A valid request exhausted its explicit proposal budget."""


def is_connected(num_nodes: int, edges: Iterable[tuple[int, int]]) -> bool:
    """Check connectivity of an undirected graph on range(num_nodes)."""
    if num_nodes < 1:
        return False
    neighbors: list[list[int]] = [[] for _ in range(num_nodes)]
    for left, right in edges:
        if not 0 <= left < num_nodes or not 0 <= right < num_nodes:
            raise ValueError("graph edge endpoint outside the object universe")
        neighbors[left].append(right)
        neighbors[right].append(left)
    reached = {0}
    frontier = [0]
    while frontier:
        for neighbor in neighbors[frontier.pop()]:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(neighbor)
    return len(reached) == num_nodes


def _graph_candidates(
    num_nodes: int, allowed_edges: Iterable[tuple[int, int]] | None
) -> tuple[tuple[int, int], ...]:
    if num_nodes < 1:
        raise ValueError("num_nodes must be positive")
    if allowed_edges is None:
        return tuple(combinations(range(num_nodes), 2))
    candidates = tuple(sorted({(min(left, right), max(left, right)) for left, right in allowed_edges}))
    if any(left == right for left, right in candidates):
        raise ValueError("self-loops are not permitted")
    if not is_connected(num_nodes, candidates):
        raise ValueError("the allowed edges cannot form a connected graph")
    return candidates


def connected_edges(  # pylint: disable=too-many-arguments
    num_nodes: int,
    rng: RandomSource,
    probability: float = 0.5,
    *,
    allowed_edges: Iterable[tuple[int, int]] | None = None,
    max_attempts: int = 10_000,
) -> set[tuple[int, int]]:
    """Independent undirected edges conditioned on connectivity.

    Every successful proposal has the Bernoulli law conditioned on being
    connected. Exhaustion is explicit: no backbone repair or fallback changes
    the measure. Restricting the candidate universe supports rover subgraphs.
    """
    if not math.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("edge probability must be finite and in [0, 1]")
    if max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    candidates = _graph_candidates(num_nodes, allowed_edges)
    if num_nodes > 1 and probability == 0:
        raise ValueError("a connected graph with multiple nodes needs positive probability")
    for _ in range(max_attempts):
        edges = {edge for edge in candidates if rng.random() < probability}
        if is_connected(num_nodes, edges):
            return edges
    raise GenerationExhausted(
        f"no connected graph in {max_attempts} proposals "
        f"(nodes={num_nodes}, edge_probability={probability})"
    )


def semantic_fingerprint(problem: Problem) -> str:
    """Hash labeled semantics, ignoring names, ordering and numeric spelling."""
    def fact_key(fact: Atom | Assignment) -> tuple[str, ...]:
        if isinstance(fact, Atom):
            return ("atom", fact.predicate, *fact.arguments)
        return ("number", fact.function.predicate, *fact.function.arguments,
                str(Fraction(str(fact.value))))
    payload = {
        "domain": problem.domain,
        "objects": sorted({(item.name, item.type_name or "object") for item in problem.objects}),
        "initial": sorted({fact_key(fact) for fact in problem.initial}),
        "goal": sorted({fact_key(fact) for fact in problem.goal}),
        "metric": None if problem.metric is None else (
            problem.metric.direction, problem.metric.expression.predicate,
            problem.metric.expression.arguments),
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
