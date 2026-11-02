"""Native execution of the shared finite-choice rules, with identical draw identities."""
from __future__ import annotations

from collections.abc import Callable
from fractions import Fraction
from typing import Any

from problog.engine_builtin import check_mode
from problog.engine_unify import UnifyError, unify_value
from problog.logic import Constant, Term, list2term, term2list

from .numbers import rational, unrounded_constant


def _draw(target: Any, key: tuple[Any, ...], weight: Fraction) -> bool:
    choices: dict[tuple[Any, ...], bool] = target.world.primitives
    chosen = choices.get(key)
    if chosen is None:
        if not 0 <= weight <= 1:
            raise ValueError("choice weight must be within [0,1]")
        chosen = bool(weight) if weight in (0, 1) else (
            target.world.rng.randrange(weight.denominator) < weight.numerator)
        choices[key] = chosen
    return chosen


def uniform_head(identity: Term, count: Constant, value: Term, tail: Term, **context: Any) -> list[tuple[Term, ...]]:
    arguments = (identity, count, value, tail)
    check_mode(arguments, ["gggg"], **context)
    key = ("uniform", *arguments)
    chosen = context["target"].world.primitives.get(key)
    if chosen is None:
        chosen = _draw(context["target"], key, 1 / rational(count))
    return [arguments] if chosen else []


def weighted_head(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    identity: Term, weight: Term, total: Term, value: Term, tail: Term, **context: Any,
) -> list[tuple[Term, ...]]:
    arguments = (identity, weight, total, value, tail)
    check_mode(arguments, ["ggggg"], **context)
    key = ("weighted", *arguments)
    chosen = context["target"].world.primitives.get(key)
    if chosen is None:
        chosen = _draw(context["target"], key, rational(weight) / rational(total))
    return [arguments] if chosen else []


def _result(arguments: tuple[Any, ...], value: Term, remaining: Term) -> list[tuple[Term, ...]]:
    """Honor bound outputs and aliases using the same Prolog unifier."""
    substitutions: dict[Any, Any] = {}
    try:
        selected = unify_value(arguments[-2], value, substitutions)
        rest = unify_value(arguments[-1], remaining, substitutions)
    except UnifyError:
        return []
    return [(*arguments[:-2], selected, rest)]


def _cached_result(arguments: tuple[Any, ...], namespace: str, target: Any,
                   select: Callable[[], tuple[Term, Term] | None]) -> list[tuple[Term, ...]]:
    """Cache the draw before unification, so a failed output match cannot poison it."""
    choices: dict[tuple[Any, ...], tuple[Term, Term] | None] = target.world.selections
    key = (namespace, *arguments[:-2])
    if key not in choices:
        choices[key] = select()
    selection = choices[key]
    return _result(arguments, *selection) if selection is not None else []


def uniform_choice(identity: Term, values: Term, selected: Any, remaining: Any, **context: Any) -> list[tuple[Term, ...]]:
    arguments = (identity, values, selected, remaining)
    check_mode(arguments, ["gg**"], **context)
    return _cached_result(arguments, "uniform", context["target"],
                          lambda: _uniform_selection(identity, values, **context))


def _uniform_selection(identity: Term, values: Term, **context: Any) -> tuple[Term, Term] | None:
    items = term2list(values, deep=False)
    if not items:
        return None
    current = values
    for index, value in enumerate(items[:-1]):
        current = current.args[1]
        if uniform_head(identity, Constant(len(items) - index), value, current, **context):
            return value, list2term(items[:index] + items[index + 1:])
    return items[-1], list2term(items[:-1])


def _weight_total(weights: list[Term]) -> int | float:
    total: int | float = 0
    for weight in weights:
        number = weight.compute_value()
        if not isinstance(number, (int, float)) or number < 0:
            raise ValueError("weighted choices require nonnegative numeric weights")
        total += number  # Match sum_list's left fold, including binary64 arithmetic.
    return total


def weighted_choice(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    identity: Term, weights: Term, values: Term, selected: Any, remaining: Any, **context: Any,
) -> list[tuple[Term, ...]]:
    arguments = (identity, weights, values, selected, remaining)
    check_mode(arguments, ["ggg**"], **context)
    return _cached_result(arguments, "weighted", context["target"],
                          lambda: _weighted_selection(identity, weights, values, **context))


def _weighted_selection(identity: Term, weights: Term, values: Term,
                        **context: Any) -> tuple[Term, Term] | None:
    weights_list = term2list(weights, deep=False)
    items = term2list(values, deep=False)
    if len(weights_list) != len(items):
        raise ValueError("weighted choices require matching weight and value lists")
    total = _weight_total(weights_list)
    if total <= 0:
        return None
    current = values
    for index, (weight, value) in enumerate(zip(weights_list[:-1], items[:-1])):
        current = current.args[1]
        if weighted_head(identity, weight, unrounded_constant(total), value, current, **context):
            return value, list2term(items[:index] + items[index + 1:])
        total -= weight.compute_value()
    return (items[-1], list2term(items[:-1])) if weights_list[-1].compute_value() > 0 else None


def bernoulli_draw(identity: Term, probability: Term, value: Term, **context: Any) -> list[tuple[Term, ...]]:
    arguments = (identity, probability, value)
    check_mode(arguments, ["ggg"], **context)
    weight = rational(probability)
    if not 0 < weight < 1:
        return []
    target = context["target"]
    key = ("bernoulli", *arguments)
    if isinstance(probability, Constant) and probability.is_float():
        choices: dict[tuple[Any, ...], bool] = target.world.primitives
        if key not in choices:
            choices[key] = target.world.rng.random() < float(probability)
        selected = choices[key]
    else:
        selected = _draw(target, key, weight)
    return [arguments] if selected else []


def bernoulli_member(identity: Term, probability: Term, value: Term, **context: Any) -> list[tuple[Term, ...]]:
    check_mode((identity, probability, value), ["ggg"], **context)
    if rational(probability) == 1:
        return [(identity, probability, value)]
    return bernoulli_draw(identity, probability, value, **context)


def bernoulli_subset(identity: Term, probability: Term, values: Term, result: Any,
                     **context: Any) -> list[tuple[Term, ...]]:
    check_mode((identity, probability, values, result), ["ggg*"], **context)
    selected = list2term([value for value in term2list(values, deep=False)
                          if bernoulli_member(identity, probability, value, **context)])
    try:
        unified = unify_value(result, selected, {})
    except UnifyError:
        return []
    return [(identity, probability, values, unified)]
