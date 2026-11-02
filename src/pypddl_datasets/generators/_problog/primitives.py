"""Deterministic finite-list and graph operations shared by declarative models.

The graph is a ground list of two-argument edge terms. Connectivity uses integer
vertices in range(NodeCount); incidence counting also accepts symbolic vertices.
These operations never sample, filter a proposed task, or know a planning domain.
"""
from __future__ import annotations

from typing import Any, cast

from problog.engine_builtin import check_mode
from problog.engine_unify import UnifyError, unify_value
from problog.logic import Constant, Term, term2list

from ..runtime import is_connected


def _edges(value: Term) -> list[tuple[Term, Term]]:
    result: list[tuple[Term, Term]] = []
    for edge in cast(list[Term], term2list(value, deep=False)):
        if len(edge.args) != 2:
            raise ValueError("graph edges must be two-argument terms")
        result.append((edge.args[0], edge.args[1]))
    return result


def connected_graph(count: Term, edges: Term, **context: Any) -> list[tuple[Term, Term]]:
    """Succeed exactly when the ground undirected graph is connected."""
    check_mode((count, edges), ["ig"], functor="connected_graph", **context)
    indexed: list[tuple[int, int]] = []
    for left, right in _edges(edges):
        if not isinstance(left, Constant) or not left.is_integer():
            raise ValueError("connectivity requires integer edge endpoints")
        if not isinstance(right, Constant) or not right.is_integer():
            raise ValueError("connectivity requires integer edge endpoints")
        indexed.append((left.value, right.value))
    return [(count, edges)] if is_connected(count.value, indexed) else []


def graph_incidence_count(edges: Term, vertices: Term, count: Any,
                          **context: Any) -> list[tuple[Term, Term, Term]]:
    """Count incident endpoints, retaining duplicate edges but treating vertices as a set."""
    check_mode((edges, vertices, count), ["ggv", "ggi"],
               functor="graph_incidence_count", **context)
    selected = set(cast(list[Term], term2list(vertices, deep=False)))
    value = Constant(sum(int(left in selected) + int(right in selected)
                         for left, right in _edges(edges)))
    try:
        unify_value(count, value, {})
    except UnifyError:
        return []
    return [(edges, vertices, value)]


def ground_member(value: Any, values: Term, **context: Any) -> list[tuple[Term, Term]]:
    """Enumerate matches in a ground list, retaining order and duplicate answers."""
    check_mode((value, values), ["*g"], functor="ground_member", **context)
    result: list[tuple[Term, Term]] = []
    for candidate in cast(list[Term], term2list(values, deep=False)):
        try:
            unified = unify_value(value, candidate, {})
        except UnifyError:
            continue
        result.append((unified, values))
    return result
