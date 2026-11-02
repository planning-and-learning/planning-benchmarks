"""Propagate evidence into nested aggregation without discarding its weights."""
from __future__ import annotations

from contextvars import ContextVar
from typing import Any

from problog.engine import DefaultEngine
from problog.formula import LogicFormula, atom
from problog.logic import Term
from typing_extensions import override

_FORCED: ContextVar[dict[Any, int | None]] = ContextVar("pypddl_problog_evidence")


class ConditionedFormula(LogicFormula):
    """Nested findall formulas inherit the root evidence's forced choices."""
    @override
    def add_atom(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self, identifier: Any, probability: Any, group: Any = None,
        name: Any = None, source: Any = None, cr_extra: bool = True, is_extra: bool = False,
    ) -> int | None:
        forced = _FORCED.get({})
        if identifier in forced:
            return forced[identifier]
        return super().add_atom(identifier, probability, group, name, source, cr_extra, is_extra)


def conditioned_formula(engine: DefaultEngine, database: Any) -> LogicFormula:
    """Keep evidence factors for normalization, simplify subsequent query work.

    Merely replacing forced atoms with Boolean constants and rebuilding the
    formula would lose categorical normalization. The original evidence nodes
    stay in this root formula with their original weights and constraints.
    """
    token = _FORCED.set({})
    try:
        target = ConditionedFormula()
        engine.ground_all(database, target=target, queries=[], propagate_evidence=True)
        forced: dict[Any, int | None] = {}
        for index, value in target.lookup_evidence.items():
            node = target.get_node(index)
            if isinstance(node, atom) and (target.is_true(value) or target.is_false(value)):
                forced[node.identifier] = value
        _FORCED.set(forced)
        queries = [(target.LABEL_QUERY, row[0]) for row in engine.query(database, Term("query", None))]
        engine.ground_queries(database, target, queries)
        return target
    finally:
        _FORCED.reset(token)
