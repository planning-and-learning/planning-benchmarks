"""Prepare canonical ProbLog programs and specialize generic primitive calls."""
from __future__ import annotations

from functools import lru_cache
from importlib.resources import files
from threading import RLock
from typing import Any

from problog.engine import DefaultEngine
from problog.formula import LogicFormula
from problog.logic import Term, unquote
from problog.program import PrologString
from typing_extensions import override

from .numbers import NumericFactory, unrounded_is

_PREPARE_LOCK = RLock()
_NATIVE_PREDICATES = frozenset(("uniform_choice", "weighted_choice", "uniform_head", "weighted_head",
                                "connected_graph", "graph_incidence_count", "ground_member",
                                "bernoulli_draw", "bernoulli_member", "bernoulli_subset"))


class ModelEngine(DefaultEngine):
    """ProbLog's Python library registration uses a global database pointer."""
    @override
    def prepare(self, db: Any) -> Any:
        with _PREPARE_LOCK:
            return super().prepare(db)



def new_engine() -> DefaultEngine:
    engine = ModelEngine()
    engine.add_simple_builtin("is", 2, unrounded_is)
    return engine


def program(source: str) -> PrologString:
    return PrologString(source, factory=NumericFactory())


@lru_cache(maxsize=1)
def _native_library() -> tuple[str, str]:
    source = files("pypddl_datasets.generators").joinpath("_problog").joinpath("library.pl").read_text()
    statements: list[str] = []
    for statement in program(source):
        head = getattr(statement, "head", statement)
        if str(head.functor) not in _NATIVE_PREDICATES:
            statements.append(str(statement) + ".")
    return source, "\n".join(statements)


def _extends_primitives(source: str) -> bool:
    for statement in program(source):
        heads = getattr(statement, "heads", (getattr(statement, "head", statement),))
        if any(unquote(str(head.functor)) in _NATIVE_PREDICATES for head in heads):
            return True
    return False


def create_sampling_program(source: str, accelerated: bool = True) -> tuple[DefaultEngine, Any, list[tuple[str, Term]]]:
    """Specialize only our exact bundled primitive definitions; keep domain rules."""
    engine = new_engine()
    common, native_common = _native_library()
    if accelerated and source.startswith(common) and not _extends_primitives(source[len(common):]):
        from . import choices, primitives
        for module, signatures in (
            (choices, (("uniform_choice", 4), ("weighted_choice", 5), ("uniform_head", 4), ("weighted_head", 5),
                       ("bernoulli_draw", 3), ("bernoulli_member", 3), ("bernoulli_subset", 4))),
            (primitives, (("connected_graph", 2), ("graph_incidence_count", 3), ("ground_member", 2))),
        ):
            for name, arity in signatures:
                engine.add_simple_builtin(name, arity, getattr(module, name))
        source = native_common + source[len(common):]
    database = engine.prepare(program(source))
    if engine.query(database, Term("evidence", None)) or engine.query(database, Term("evidence", None, None)):
        raise ValueError("sampling requires explicit local retries; global evidence is inference-only")
    queries = [(LogicFormula.LABEL_QUERY, row[0]) for row in engine.query(database, Term("query", None))]
    return engine, database, queries
