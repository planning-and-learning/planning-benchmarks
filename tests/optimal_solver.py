"""A blind optimal planner over pypddl tasks, to check generators' stated optimal costs.

It grounds every action over the typed objects (joining static preconditions against
the initial state), then runs uniform-cost search over sets of ground atoms. It
supports typing, conjunctions of positive and negative literals, equality, and action
costs that increase ``total-cost`` by a number or a static function value. That covers
every domain of the optimally-tractable fragments; anything else raises.
"""

from __future__ import annotations

import heapq
import itertools
import tempfile
from pathlib import Path
from typing import Any

from pypddl.formalism import Parser, ParserOptions

Atom = tuple[str, ...]  # predicate name followed by object names
Literal = tuple[bool, str, tuple[str, ...]]  # polarity, predicate, variable or object names
# positive and negative dynamic preconditions, add and delete effects, cost
GroundAction = tuple[frozenset[Atom], frozenset[Atom], frozenset[Atom], frozenset[Atom], float]


class SearchBudgetExceeded(RuntimeError):
    """The search expanded more states than allowed."""


def _variant(node: Any) -> Any:
    return node.get_variant()


def _term(term: Any) -> str:
    return _variant(term).get_name()


def _atom(atom: Any) -> tuple[str, tuple[str, ...]]:
    return atom.get_predicate().get_name(), tuple(_term(t) for t in atom.get_terms())


def _literals(condition: Any) -> list[Literal]:
    node = _variant(condition)
    kind = type(node).__name__
    if kind == "ConditionAnd":
        return [literal for sub in node.get_conditions() for literal in _literals(sub)]
    if kind == "ConditionLiteral":
        literal = node.get_literal()
        predicate, args = _atom(literal.get_atom())
        return [(literal.get_polarity(), predicate, args)]
    if kind == "ConditionNot":
        inner = _literals(node.get_condition())
        if len(inner) != 1:
            raise NotImplementedError("negated conjunction")
        polarity, predicate, args = inner[0]
        return [(not polarity, predicate, args)]
    raise NotImplementedError(kind)


def _effects(effect: Any) -> tuple[list[Literal], list[tuple[str, Any]]]:
    """Literal effects and (function name, expression) increases."""
    node = _variant(effect)
    kind = type(node).__name__
    if kind == "EffectAnd":
        literals: list[Literal] = []
        increases: list[tuple[str, Any]] = []
        for sub in node.get_effects():
            sub_literals, sub_increases = _effects(sub)
            literals.extend(sub_literals)
            increases.extend(sub_increases)
        return literals, increases
    if kind == "EffectLiteral":
        literal = node.get_literal()
        predicate, args = _atom(literal.get_atom())
        return [(literal.get_polarity(), predicate, args)], []
    if kind == "EffectNumeric":
        if "Increase" not in str(node.get_operator()):
            raise NotImplementedError(str(node.get_operator()))
        return [], [(node.get_function().get_function().get_name(), node.get_expression())]
    raise NotImplementedError(kind)


def _evaluate(expression: Any, binding: dict[str, str], values: dict[Atom, float]) -> float:
    node = _variant(expression)
    kind = type(node).__name__
    if kind == "FunctionExpressionNumber":
        return float(node.get_value())
    if kind == "FunctionTerm":
        key = (node.get_function().get_name(), *(binding.get(_term(t), _term(t)) for t in node.get_terms()))
        return values[key]
    raise NotImplementedError(kind)


def _unify(binding: dict[str, str], args: tuple[str, ...], objects: tuple[str, ...]) -> dict[str, str] | None:
    """Extend ``binding`` so that ``args`` (variables or objects) match ``objects``, or None."""
    extended = dict(binding)
    for name, obj in zip(args, objects):
        if name.startswith("?"):
            if extended.setdefault(name, obj) != obj:
                return None
        elif name != obj:
            return None
    return extended


class GroundTask:
    """A grounded task: dynamic atoms, ground actions and the goal."""

    def __init__(self, task: Any) -> None:
        domain = task.get_domain()
        bases = {t.get_name(): [b.get_name() for b in t.get_bases()] for t in domain.get_types()}

        def ancestors(name: str) -> set[str]:
            result, frontier = {name}, [name]
            while frontier:
                for base in bases.get(frontier.pop(), []):
                    if base not in result:
                        result.add(base)
                        frontier.append(base)
            return result

        self.objects: dict[str, set[str]] = {}
        for obj in [*domain.get_constants(), *task.get_objects()]:
            types = [t.get_name() for t in obj.get_types()] or ["object"]
            self.objects[obj.get_name()] = set().union(*(ancestors(t) for t in types))
        self.init: set[Atom] = set()
        for literal in task.get_initial_literals():
            if literal.get_polarity():
                predicate, args = _atom(literal.get_atom())
                self.init.add((predicate, *args))
        self.values: dict[Atom, float] = {}
        for value in task.get_initial_function_values():
            term = value.get_function()
            key = (term.get_function().get_name(), *(_term(t) for t in term.get_terms()))
            self.values[key] = float(_variant(value.get_value()).get_value())
        self.unit_cost = task.get_metric() is None
        actions = domain.get_actions()
        self.dynamic = {predicate for action in actions for _, predicate, _ in _effects(action.get_effect())[0]}
        self.goal = _literals(task.get_goal())
        self.actions = [ground for action in actions for ground in self._ground(action)]

    def _objects_of(self, types: list[str]) -> list[str]:
        if not types:
            return sorted(self.objects)
        return sorted(name for name, kinds in self.objects.items() if any(t in kinds for t in types))

    def holds_static(self, polarity: bool, predicate: str, args: tuple[str, ...]) -> bool:
        if predicate == "=":
            return (args[0] == args[1]) == polarity
        return ((predicate, *args) in self.init) == polarity

    def _bindings(self, preconditions: list[Literal]) -> list[dict[str, str]]:
        """Partial bindings that satisfy the static positive preconditions, joined against the initial state."""
        by_predicate: dict[str, list[Atom]] = {}
        for atom in self.init:
            by_predicate.setdefault(atom[0], []).append(atom)
        static = [
            (predicate, args) for polarity, predicate, args in preconditions
            if polarity and predicate != "=" and predicate not in self.dynamic
        ]
        bindings: list[dict[str, str]] = [{}]
        for predicate, args in sorted(static, key=lambda item: -len(item[1])):
            bindings = [
                extended
                for binding in bindings
                for atom in by_predicate.get(predicate, [])
                if (extended := _unify(binding, args, atom[1:])) is not None
            ]
        return bindings

    def _instantiate(
        self, binding: dict[str, str], preconditions: list[Literal], literals: list[Literal],
        increases: list[tuple[str, Any]],
    ) -> GroundAction | None:
        positive: set[Atom] = set()
        negative: set[Atom] = set()
        for polarity, predicate, args in preconditions:
            bound = tuple(binding.get(a, a) for a in args)
            if predicate == "=" or predicate not in self.dynamic:
                if not self.holds_static(polarity, predicate, bound):
                    return None
            elif polarity:
                positive.add((predicate, *bound))
            else:
                negative.add((predicate, *bound))
        adds = {(p, *(binding.get(a, a) for a in args)) for polarity, p, args in literals if polarity}
        dels = {(p, *(binding.get(a, a) for a in args)) for polarity, p, args in literals if not polarity}
        cost = 1.0 if self.unit_cost else sum(
            _evaluate(expression, binding, self.values) for name, expression in increases if name == "total-cost"
        )
        return frozenset(positive), frozenset(negative), frozenset(adds), frozenset(dels), cost

    def _ground(self, action: Any) -> list[GroundAction]:
        parameters = [
            (p.get_variable().get_name(), [t.get_name() for t in p.get_types()]) for p in action.get_parameters()
        ]
        candidates = {name: self._objects_of(types) for name, types in parameters}
        preconditions = _literals(action.get_precondition())
        literals, increases = _effects(action.get_effect())
        ground: list[GroundAction] = []
        for binding in self._bindings(preconditions):
            free = [name for name, _ in parameters if name not in binding]
            for choice in itertools.product(*(candidates[name] for name in free)):
                full = {**binding, **dict(zip(free, choice))}
                if any(full[name] not in candidates[name] for name, _ in parameters):
                    continue
                instance = self._instantiate(full, preconditions, literals, increases)
                if instance is not None:
                    ground.append(instance)
        return ground

    def solve(self, max_states: int = 500_000) -> float | None:
        """Optimal plan cost by uniform-cost search, or None if unsolvable."""
        for polarity, predicate, args in self.goal:
            if (predicate == "=" or predicate not in self.dynamic) and not self.holds_static(polarity, predicate, args):
                return None
        goal_positive = {(p, *args) for polarity, p, args in self.goal if polarity and p in self.dynamic}
        goal_negative = {(p, *args) for polarity, p, args in self.goal if not polarity and p in self.dynamic}
        start = frozenset(atom for atom in self.init if atom[0] in self.dynamic)
        best: dict[frozenset[Atom], float] = {start: 0.0}
        queue: list[tuple[float, int, frozenset[Atom]]] = [(0.0, 0, start)]
        counter = itertools.count(1)
        expanded = 0
        while queue:
            cost, _, state = heapq.heappop(queue)
            if cost > best[state]:
                continue
            if goal_positive <= state and goal_negative.isdisjoint(state):
                return cost
            expanded += 1
            if expanded > max_states:
                raise SearchBudgetExceeded(f"more than {max_states} states expanded")
            for positive, negative, adds, dels, action_cost in self.actions:
                if positive <= state and negative.isdisjoint(state):
                    successor = (state - dels) | adds
                    total = cost + action_cost
                    if total < best.get(successor, float("inf")):
                        best[successor] = total
                        heapq.heappush(queue, (total, next(counter), successor))
        return None


def optimal_cost(domain_path: Path, problem_text: str, max_states: int = 500_000) -> int | None:
    """Parse the task strictly and return its optimal plan cost (None if unsolvable)."""
    options = ParserOptions()
    options.strict = True
    with tempfile.TemporaryDirectory() as directory:
        problem_path = Path(directory) / "problem.pddl"
        problem_path.write_text(problem_text, encoding="utf-8")
        task = Parser(domain_path, options).parse_task(problem_path)
    cost = GroundTask(task).solve(max_states)
    if cost is None:
        return None
    assert cost == int(cost), cost
    return int(cost)
