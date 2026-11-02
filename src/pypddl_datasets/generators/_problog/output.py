"""Decode a model's generic output vocabulary into existing typed PDDL values."""
from __future__ import annotations

from collections.abc import Mapping

from problog.logic import Term, unquote

from ..runtime import Atom, GenerationExhausted, Object, Problem


def _name(value: Term) -> str:
    return unquote(str(value))


def _atom(value: Term) -> Atom:
    return Atom(unquote(str(value.functor)), tuple(_name(arg) for arg in value.args))


def decode_world(world: Mapping[Term, bool]) -> Problem:
    """Rendering contains no domain-specific construction or sampling logic."""
    declarations: list[Object] = []
    initial: list[Atom] = []
    goal: list[Atom] = []
    metadata: dict[str, str] = {}
    for term, present in world.items():
        if not present:
            continue
        kind = unquote(str(term.functor))
        if kind == "failure":
            raise GenerationExhausted(_name(term.args[0]))
        if kind == "object":
            name, type_name = map(_name, term.args)
            declarations.append(Object(name, None if type_name == "untyped" else type_name))
        elif kind in ("initial", "goal"):
            (initial if kind == "initial" else goal).append(_atom(term.args[0]))
        elif kind in ("domain", "problem_name"):
            if kind in metadata:
                raise ValueError(f"model emits multiple {kind} values")
            metadata[kind] = _name(term.args[0])
        else:
            raise ValueError(f"unexpected model output: {term}")
    if set(metadata) != {"domain", "problem_name"}:
        raise ValueError("model must emit one domain and one problem name")
    if len({item.name for item in declarations}) != len(declarations):
        raise ValueError("model emits conflicting object declarations")
    return Problem(metadata["problem_name"], metadata["domain"], tuple(declarations), tuple(initial), tuple(goal))
