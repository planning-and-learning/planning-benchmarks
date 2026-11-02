"""Independent decoding through pypddl's validated syntax tree."""
from __future__ import annotations

from pathlib import Path

from pypddl.formalism import (
    Atom, Condition, ConditionAnd, ConditionLiteral, FunctionExpressionNumber,
    FunctionTerm, Literal, Object, OptimizationDirection, Parser, ParserOptions,
    SemanticError, Term, InitialFunctionValue, Metric,
)

from .interpretation import SemanticKey, Situation, Value


def _arguments(terms: list[Term]) -> tuple[str, ...]:
    values = [term.get_value() for term in terms]
    if not all(isinstance(value, Object) for value in values):
        raise ValueError("A distribution situation must contain ground atoms")
    return tuple(value.get_name().lower() for value in values)


def _atom(atom: Atom, group: str) -> SemanticKey:
    return SemanticKey(group, "atom", atom.get_predicate().get_name().lower(), _arguments(atom.get_terms()))


def _literal(literal: Literal, group: str) -> tuple[SemanticKey, Value]:
    if not literal.get_polarity():
        raise ValueError("These distributions use positive literals only")
    return _atom(literal.get_atom(), group), True


def _goal(condition: Condition | None) -> list[tuple[SemanticKey, Value]]:
    if condition is None:
        raise ValueError("An explicit goal formula is required")
    value = condition.get_value()
    if isinstance(value, ConditionLiteral):
        return [_literal(value.get_literal(), "goal")]
    if isinstance(value, ConditionAnd):
        return [entry for child in value.get_conditions() for entry in _goal(child)]
    raise ValueError("These distributions use conjunctions of positive goal atoms")


def decode_pddl(domain_path: Path, source: str | Path) -> tuple[Situation, tuple[str, str] | None]:
    """Read complete objects, initial facts/numbers, goal atoms and metric.

    No task normalization or synthetic action costs are enabled. In particular,
    missing atoms are not filled in from generator code or a sampled reference.
    """
    options = ParserOptions()
    options.strict = True
    options.add_action_costs = False
    try:
        parser = Parser(domain_path, options)
        task = parser.parse_task(source)
    except SemanticError as error:
        raise ValueError(str(error)) from error
    values: list[tuple[SemanticKey, Value]] = []
    for obj in task.get_objects():
        types = obj.get_types()
        if len(types) != 1:
            raise ValueError("Generator object declarations must have exactly one type")
        values.append((SemanticKey("initial", "object", obj.get_name().lower(),
                                   (types[0].get_name().lower(),)), True))
    values.extend(_literal(literal, "initial") for literal in task.get_initial_literals())
    values.extend(_numbers(task.get_initial_function_values()))
    values.extend(_goal(task.get_goal()))
    return Situation(tuple(sorted(values))), _metric(task.get_metric())


def _metric(metric: Metric | None) -> tuple[str, str] | None:
    decoded_metric: tuple[str, str] | None = None
    if metric is not None:
        expression = metric.get_expression().get_value()
        if not isinstance(expression, FunctionTerm) or expression.get_terms():
            raise ValueError("Expected a nullary fluent as optimization metric")
        direction = "minimize" if metric.get_optimization_direction() == OptimizationDirection.Minimize else "maximize"
        decoded_metric = (direction, expression.get_function().get_name().lower())
    return decoded_metric


def _numbers(assignments: list[InitialFunctionValue]) -> list[tuple[SemanticKey, Value]]:
    values: list[tuple[SemanticKey, Value]] = []
    for assignment in assignments:
        value = assignment.get_value().get_value()
        if not isinstance(value, FunctionExpressionNumber):
            raise ValueError("Initialized numeric values must be constants")
        numeric = value.get_value()
        if int(numeric) != numeric:
            raise ValueError("These distributions initialize integral numeric values")
        function = assignment.get_function()
        values.append((SemanticKey("initial", "number", function.get_function().get_name().lower(),
                                   _arguments(function.get_terms())), int(numeric)))
    return values
