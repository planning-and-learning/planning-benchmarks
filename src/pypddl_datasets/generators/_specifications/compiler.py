"""Finite grounding of declarative contracts into the existing solver interface."""
from __future__ import annotations

from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from itertools import product
import math
import operator
import re
from typing import TypeAlias, Union, cast

try:
    import z3
except ImportError as error:
    raise ImportError("Executable specifications require pypddl-datasets[specs]") from error

from .core import Group, Specification
from .syntax import Definition, Node, Parameter, SpecificationError, string_value

Scalar: TypeAlias = str | int | float | bool | None
Value: TypeAlias = Union[Scalar, tuple["Value", ...], "Array", z3.BoolRef, z3.ArithRef]
Environment: TypeAlias = Mapping[str, Value]


@dataclass
class Array:
    entries: dict[tuple[Scalar, ...], Value]


@dataclass
class Relation:
    group: Group
    predicate: str
    arity: int
    numeric: bool
    slots: dict[tuple[str, ...], z3.BoolRef | z3.ArithRef]


class GroundingLimitError(SpecificationError):
    """The requested finite contract exceeded an explicit construction budget."""


def _scalar(value: Value) -> Scalar:
    if value is None or isinstance(value, (str, int, float)):
        return value
    raise ValueError("expected a ground scalar")


def _integer(value: Value) -> int:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    raise ValueError("expected a ground integer")


def _numeric(value: Value) -> int | float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    raise ValueError("expected a ground number")


def _sequence(value: Value) -> tuple[Value, ...]:
    if isinstance(value, tuple):
        return value
    raise ValueError("expected a finite list")


def _string(value: Value) -> str:
    if isinstance(value, str):
        return value
    raise ValueError("expected a ground string")


def _boolean(value: Value) -> bool | z3.BoolRef:
    if isinstance(value, (bool, z3.BoolRef)):
        return value
    raise ValueError("expected a Boolean expression")


def _arithmetic(value: Value) -> int | z3.ArithRef:
    if isinstance(value, z3.ArithRef):
        return value
    return _integer(value)


def _formula(value: Value) -> z3.BoolRef:
    checked = _boolean(value)
    return z3.BoolVal(checked) if isinstance(checked, bool) else checked


def _ground(value: Value) -> bool:
    if isinstance(value, (z3.BoolRef, z3.ArithRef)):
        return False
    if isinstance(value, Array):
        return all(_ground(item) for item in value.entries.values())
    return all(_ground(item) for item in value) if isinstance(value, tuple) else True


def _choose(condition: Value, yes: Value, no: Value) -> Value:
    checked = _boolean(condition)
    if isinstance(checked, bool):
        return yes if checked else no
    if isinstance(yes, (bool, z3.BoolRef)) and isinstance(no, (bool, z3.BoolRef)):
        return z3.If(checked, _formula(yes), _formula(no))
    return z3.If(checked, _arithmetic(yes), _arithmetic(no))


class Compiler:
    """Interpreter for the fixed language kernel; never imports domain code."""

    def __init__(self, definition: Definition, max_groundings: int | None) -> None:
        self.definition = definition
        self.spec = Specification(definition.distribution)
        self.environment: dict[str, Value] = {}
        self.relations: dict[tuple[str, str], Relation] = {}
        self.declared_objects: dict[str, str] = {}
        self.constants: dict[str, str] = {}
        self.optional_objects: set[str] = set()
        self.signatures: dict[tuple[str, str], int] = {}
        self.rule_names: set[tuple[str, str]] = set()
        self.semantic_names: set[tuple[str, str, str, tuple[str, ...]]] = set()
        self.remaining = max_groundings

    def charge(self, amount: int, node: Node) -> None:
        if self.remaining is not None:
            self.remaining -= amount
            if self.remaining < 0:
                raise GroundingLimitError("finite grounding budget exceeded", node.span)

    def evaluate(self, node: Node, environment: Environment) -> Value:
        self.charge(1, node)
        handlers: dict[str, Callable[[Node, Environment], Value]] = {
            "integer": self._literal, "floating": self._literal, "string": self._literal,
            "true": self._literal, "false": self._literal, "none": self._literal,
            "name": self._name, "list": self._list, "index": self._index,
            "call": self._call, "reference": self._reference, "binary": self._binary,
            "unary": self._unary, "conditional": self._conditional,
            "aggregate": self._aggregate, "quantifier": self._aggregate,
        }
        try:
            value = handlers[node.kind](node, environment)
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError("ground numeric result must be finite")
            return value
        except SpecificationError:
            raise
        except (ArithmeticError, ValueError, TypeError, KeyError, IndexError) as error:
            raise SpecificationError(str(error), node.span) from error

    def ground(self, node: Node, environment: Environment) -> Value:
        value = self.evaluate(node, environment)
        if not _ground(value):
            raise SpecificationError("this declaration requires a ground expression", node.span)
        return value

    @staticmethod
    def _literal(node: Node, _environment: Environment) -> Value:
        if node.kind in {"true", "false", "none"}:
            return {"true": True, "false": False, "none": None}[node.kind]
        token = node.children[0]
        if node.kind == "string":
            return string_value(token)
        return int(token.value) if node.kind == "integer" else float(token.value)

    @staticmethod
    def _name(node: Node, environment: Environment) -> Value:
        name = node.children[0].value
        if name not in environment:
            raise ValueError(f"unknown or forward-referenced name {name!r}")
        return environment[name]

    def _list(self, node: Node, environment: Environment) -> Value:
        arguments = node.children[0].children if node.children else ()
        return tuple(self.evaluate(argument, environment) for argument in arguments)

    def _arguments(self, node: Node, environment: Environment) -> tuple[Value, ...]:
        arguments = next((child.children for child in node.children if child.kind == "arguments"), ())
        return tuple(self.evaluate(argument, environment) for argument in arguments)

    def _index(self, node: Node, environment: Environment) -> Value:
        value = environment[node.children[0].value]
        indices = tuple(_scalar(value) for value in self._arguments(node, environment))
        if isinstance(value, Array):
            return value.entries[indices]
        if len(indices) != 1:
            raise ValueError("list indexing requires exactly one integer")
        return _sequence(value)[_integer(indices[0])]

    def _reference(self, node: Node, environment: Environment) -> Value:
        group, name = (child.value for child in node.children[:2])
        relation = self.relations.get((group, name))
        if relation is None:
            raise ValueError(f"undeclared relation {group}.{name}")
        arguments = tuple(_string(value).lower() for value in self._arguments(node, environment))
        if len(arguments) != relation.arity:
            raise ValueError(f"wrong arity for {group}.{name}")
        if arguments not in relation.slots:
            raise ValueError(f"arguments outside declared family for {group}.{name}: {arguments}")
        return relation.slots[arguments]

    def _conditional(self, node: Node, environment: Environment) -> Value:
        condition, yes, no = node.children
        value = _boolean(self.evaluate(condition, environment))
        if isinstance(value, bool):
            return self.evaluate(yes if value else no, environment)
        return _choose(value, self.evaluate(yes, environment), self.evaluate(no, environment))

    def _unary(self, node: Node, environment: Environment) -> Value:
        operation, expression = node.children
        value = self.evaluate(expression, environment)
        if operation.value == "not":
            checked = _boolean(value)
            return not checked if isinstance(checked, bool) else z3.Not(checked)
        numeric = _arithmetic(value) if isinstance(value, z3.ArithRef) else _numeric(value)
        return -1 * numeric if operation.value == "-" else numeric

    def _binary(self, node: Node, environment: Environment) -> Value:
        left, operation, right = node.children
        first = self.evaluate(left, environment)
        op = operation.value
        if op in {"and", "or", "implies", "iff"}:
            checked = _boolean(first)
            if isinstance(checked, bool):
                if op == "and" and not checked or op == "or" and checked:
                    return checked
                if op == "implies" and not checked:
                    return True
            return _logical(op, checked, _boolean(self.evaluate(right, environment)))
        second = self.evaluate(right, environment)
        if op in {"==", "!=", "<", "<=", ">", ">="}:
            return _compare(op, first, second)
        return _calculate(op, first, second)

    def environments(self, bindings: Node, environment: Environment) -> Iterator[dict[str, Value]]:
        if not bindings.children:
            yield dict(environment)
            return
        binding, *rest = bindings.children
        name, domain = binding.children
        if name.value in environment:
            raise SpecificationError(f"binding shadows existing name {name.value!r}", name.span)
        values = tuple(_scalar(value) for value in _sequence(self.ground(domain, environment)))
        if len(values) != len(set(values)):
            raise SpecificationError("duplicate finite domain value", domain.span)
        remainder = Node("bindings", tuple(rest), bindings.span)
        for value in values:
            self.charge(1, binding)
            nested = {**environment, name.value: value}
            yield from self.environments(remainder, nested)

    def _aggregate(self, node: Node, environment: Environment) -> Value:
        kind, bindings, *tail = node.children
        guard = tail[0].children[0] if len(tail) == 2 else None
        body = tail[-1]
        values: list[Value] = []
        for nested in self.environments(bindings, environment):
            condition = True if guard is None else _boolean(self.evaluate(guard, nested))
            if condition is False:
                continue
            value = self.evaluate(body, nested)
            if kind.value in {"forall", "exists"}:
                value = _logical("implies" if kind.value == "forall" else "and", condition, _boolean(value))
            elif kind.value == "count":
                value = _choose(_logical("and", condition, _boolean(value)), 1, 0)
            else:
                value = _choose(condition, _arithmetic(value), 0)
            values.append(value)
        return _reduce(kind.value, values)

    def _call(self, node: Node, environment: Environment) -> Value:
        name = node.children[0].value
        arguments = self._arguments(node, environment)
        if name == "present":
            if len(arguments) != 1:
                raise ValueError("present requires one object")
            return self.spec.present(_string(arguments[0]).lower())
        if not all(_ground(argument) for argument in arguments):
            raise ValueError(f"builtin {name!r} requires ground arguments")
        if name in {"range", "names"}:
            return self._finite_sequence(name, arguments, node)
        return _builtin(name, arguments)

    def _finite_sequence(self, name: str, arguments: tuple[Value, ...], node: Node) -> Value:
        if name == "range":
            if not 1 <= len(arguments) <= 3:
                raise ValueError("range requires one to three integers")
            sequence = range(*(_integer(argument) for argument in arguments))
            self.charge(len(sequence), node)
            return tuple(sequence)
        if len(arguments) not in {2, 3}:
            raise ValueError("names requires a prefix, count, and optional start")
        prefix, count = _string(arguments[0]), _integer(arguments[1])
        start = 0 if len(arguments) == 2 else _integer(arguments[2])
        if count < 0:
            raise ValueError("names count must be nonnegative")
        self.charge(count, node)
        return tuple(f"{prefix}{index}" for index in range(start, start + count))

    def parameters(self, supplied: Mapping[str, Scalar]) -> None:
        extra = supplied.keys() - {parameter.name for parameter in self.definition.parameters}
        if extra:
            span = self.definition.parameters[0].span if self.definition.parameters else None
            raise SpecificationError(f"unknown parameters: {sorted(extra)}", span)
        for parameter in self.definition.parameters:
            if parameter.name in supplied:
                value: Value = supplied[parameter.name]
            elif parameter.default is not None:
                self.validate(parameter.default, set(self.environment))
                value = self.ground(parameter.default, self.environment)
            else:
                raise SpecificationError(f"missing parameter {parameter.name!r}", parameter.span)
            try:
                self.environment[parameter.name] = _parameter_value(parameter, value)
            except (ValueError, OverflowError) as error:
                raise SpecificationError(str(error), parameter.span) from error

    def statement(self, node: Node) -> None:
        handlers: dict[str, Callable[[Node], None]] = {
            "let": self._let, "requirement": self._requirement,
            "objects": self._objects, "constants": self._objects,
            "relation": self._relation, "number": self._relation,
            "auxiliary": self._auxiliary, "group": self._group, "metric": self._metric,
        }
        try:
            scope = set(self.environment)
            dimensions = next((child for child in node.children if child.kind == "dimensions"), None)
            if dimensions:
                scope = self._binding_scope(dimensions.children[0], scope)
                if len(dimensions.children) == 2:
                    self.validate(dimensions.children[1], scope)
            for child in node.children:
                if child is not dimensions:
                    self.validate(child, scope)
            handlers[node.kind](node)
        except SpecificationError:
            raise
        except (ArithmeticError, ValueError, TypeError, KeyError, IndexError) as error:
            raise SpecificationError(str(error), node.span) from error

    def _binding_scope(self, bindings: Node, names: set[str]) -> set[str]:
        scope = set(names)
        for binding in bindings.children:
            name, domain = binding.children
            self.validate(domain, scope)
            if name.value in scope:
                raise SpecificationError(f"binding shadows existing name {name.value!r}", name.span)
            scope.add(name.value)
        return scope

    def validate(self, node: Node, names: set[str]) -> None:
        """Check names and arities even in branches that finite grounding skips."""
        if node.kind in {"quantifier", "aggregate"}:
            scope = self._binding_scope(node.children[1], names)
            for child in node.children[2:]:
                self.validate(child, scope)
            return
        if node.kind in {"name", "index"} and node.children[0].value not in names:
            raise SpecificationError(f"unknown or forward-referenced name {node.children[0].value!r}", node.span)
        if node.kind == "call":
            self._validate_call(node)
        if node.kind == "reference":
            self._validate_reference(node)
        for child in node.children:
            self.validate(child, names)

    def _validate_call(self, node: Node) -> None:
        name = node.children[0].value
        arities = {"range": (1, 3), "names": (2, 3), "min": (1, math.inf), "max": (1, math.inf)}
        unary = {"present", "len", "values", "str", "abs", "ceil", "floor", "trunc", "round", "int", "float"}
        if name not in arities and name not in unary:
            raise SpecificationError(f"unknown builtin {name!r}", node.span)
        minimum, maximum = arities.get(name, (1, 1))
        count = len(node.children[1].children) if len(node.children) == 2 else 0
        if not minimum <= count <= maximum:
            raise SpecificationError(f"wrong number of arguments for builtin {name!r}", node.span)

    def _validate_reference(self, node: Node) -> None:
        group, name = (child.value for child in node.children[:2])
        relation = self.relations.get((group, name))
        if relation is None:
            raise SpecificationError(f"undeclared relation {group}.{name}", node.span)
        count = len(node.children[2].children) if len(node.children) == 3 else 0
        if count != relation.arity:
            raise SpecificationError(f"wrong arity for {group}.{name}", node.span)

    def _requirement(self, node: Node) -> None:
        name, expression = node.children
        self._unique_rule("parameter", name)
        if self.ground(expression, self.environment) is not True:
            raise SpecificationError(f"parameter constraint {name.value!r} failed", expression.span)

    def _declare(self, name: Node, value: Value) -> None:
        if name.value in self.environment:
            raise SpecificationError(f"duplicate declaration {name.value!r}", name.span)
        self.environment[name.value] = value

    def _dimensions(self, dimensions: Node) -> Iterator[tuple[tuple[Scalar, ...], dict[str, Value]]]:
        bindings = dimensions.children[0]
        guard = dimensions.children[1].children[0] if len(dimensions.children) == 2 else None
        for environment in self.environments(bindings, self.environment):
            if guard is not None:
                value = self.ground(guard, environment)
                if not isinstance(value, bool):
                    raise SpecificationError("dimension guard must be Boolean", guard.span)
                if not value:
                    continue
            keys = tuple(_scalar(environment[binding.children[0].value]) for binding in bindings.children)
            yield keys, environment

    def _let(self, node: Node) -> None:
        name, *tail = node.children
        if len(tail) == 1:
            self._declare(name, self.ground(tail[0], self.environment))
            return
        dimensions, expression = tail
        entries = {indices: self.ground(expression, environment)
                   for indices, environment in self._dimensions(dimensions)}
        self._declare(name, Array(entries))

    def _objects(self, node: Node) -> None:
        expression, type_node, *optional = node.children
        names = tuple(_string(value).lower() for value in _sequence(self.ground(expression, self.environment)))
        kind = string_value(type_node) if type_node.value.startswith('"') else type_node.value
        _identifier(kind)
        target = self.constants if node.kind == "constants" else self.declared_objects
        for name in names:
            _identifier(name)
            if name in self.constants or name in self.declared_objects:
                raise ValueError(f"duplicate object or constant {name!r}")
            target[name] = kind.lower()
        self.charge(len(names), node)
        if node.kind == "objects":
            self.spec.objects(names, kind, optional=True)
            if optional:
                self.optional_objects.update(names)
            else:
                for name in names:
                    self.spec.add_declaration(f"object_{name}", self.spec.present(name), node.span)

    def _bounds(self, node: Node, environment: Environment) -> tuple[int, int]:
        lower, upper = (_integer(self.ground(child, environment)) for child in node.children)
        if lower > upper:
            raise SpecificationError("integer lower bound exceeds upper bound", node.span)
        return lower, upper

    def _auxiliary(self, node: Node) -> None:
        name, *tail = node.children
        dimensions = tail[0] if len(tail) == 2 else None
        kind = tail[-1]
        if kind.kind == "integer_type" and _referenced_names(kind) <= self.environment.keys():
            self._bounds(kind, self.environment)
        environments = self._dimensions(dimensions) if dimensions else iter([((), self.environment)])
        entries: dict[tuple[Scalar, ...], Value] = {}
        for index, (keys, environment) in enumerate(environments):
            self.charge(1, node)
            label = f"{name.value}_{index}"
            if kind.kind == "boolean_type":
                entries[keys] = self.spec.boolean_witness(label)
            else:
                lower, upper = self._bounds(kind, environment)
                value = self.spec.witness(label)
                self.spec.add_declaration(f"aux_bound_{label}", z3.And(value >= lower, value <= upper), node.span)
                entries[keys] = value
        self._declare(name, Array(entries) if dimensions else entries[()])

    def _relation_arguments(self, node: Node) -> Iterator[tuple[str, ...]]:
        dimensions = next((child for child in node.children if child.kind == "dimensions"), None)
        arguments = next((child.children for child in node.children if child.kind == "arguments"), ())
        if dimensions is not None:
            for _, environment in self._dimensions(dimensions):
                yield tuple(_string(self.ground(argument, environment)).lower() for argument in arguments)
            return
        families = [tuple(_string(value).lower() for value in _sequence(self.ground(argument, self.environment)))
                    for argument in arguments]
        for entry in product(*families):
            self.charge(1, node)
            yield entry

    def _new_relation(self, node: Node) -> Relation:
        group_node, name = node.children[:2]
        group = _group_name(group_node.value)
        if group == "joint" or node.kind == "number" and group != "initial":
            raise ValueError("semantic relations belong to initial/goal; numbers belong to initial")
        if (group, name.value) in self.relations:
            raise ValueError(f"duplicate relation {group}.{name.value}")
        alias = next((child for child in node.children if child.kind == "alias"), None)
        predicate = name.value if alias is None else string_value(alias.children[0])
        _identifier(predicate)
        arguments = next((child.children for child in node.children if child.kind == "arguments"), ())
        relation = Relation(group, predicate.lower(), len(arguments), node.kind == "number", {})
        signature = ("number" if relation.numeric else "atom", relation.predicate)
        arity = self.signatures.setdefault(signature, relation.arity)
        if arity != relation.arity:
            raise ValueError(f"inconsistent PDDL arity for {relation.predicate!r}")
        self.relations[group, name.value] = relation
        return relation

    def _relation(self, node: Node) -> None:
        relation = self._new_relation(node)
        name = node.children[1].value
        bounds = next((child for child in node.children if child.kind == "integer_type"), None)
        limits = None if bounds is None else self._bounds(bounds, self.environment)
        for entry in self._relation_arguments(node):
            if any(value not in self.declared_objects and value not in self.constants for value in entry):
                raise ValueError(f"relation references undeclared objects/constants: {entry}")
            semantic_name = (relation.group, "number" if relation.numeric else "atom", relation.predicate, entry)
            if semantic_name in self.semantic_names:
                raise ValueError(f"duplicate semantic declaration: {relation.predicate}{entry}")
            self.semantic_names.add(semantic_name)
            if limits is None:
                relation.slots[entry] = self.spec.atom(relation.group, relation.predicate, *entry)
            else:
                lower, upper = limits
                value = self.spec.number(relation.predicate, *entry)
                relation.slots[entry] = value
                self.spec.add_declaration(f"number_bound_{relation.group}_{name}_{len(relation.slots)}", z3.And(value >= lower, value <= upper), node.span)
            self._presence(relation, name, entry, node)

    def _presence(self, relation: Relation, name: str, arguments: tuple[str, ...], node: Node) -> None:
        optional = tuple(dict.fromkeys(value for value in arguments if value in self.optional_objects))
        if not optional:
            return
        present = z3.And(*(self.spec.present(value) for value in optional))
        formula = present if relation.numeric else z3.Implies(cast(z3.BoolRef, relation.slots[arguments]), present)
        self.spec.add_declaration(f"present_{relation.group}_{name}_{len(relation.slots)}", formula, node.span)

    def _unique_rule(self, group: str, name: Node) -> None:
        key = group, name.value
        if key in self.rule_names:
            raise SpecificationError(f"duplicate rule {group}.{name.value}", name.span)
        self.rule_names.add(key)

    def _group(self, node: Node) -> None:
        group_node, *rules = node.children
        group = _group_name(group_node.value)
        for rule in rules:
            name, expression = rule.children
            self._unique_rule(group, name)
            self.spec.add(group, name.value, _formula(self.evaluate(expression, self.environment)),
                          source=rule.span)

    def _metric(self, node: Node) -> None:
        direction, group, name, *arguments = node.children
        if self.spec.metric is not None:
            raise ValueError("duplicate metric")
        relation = self.relations.get((group.value, name.value))
        if relation is None or not relation.numeric or relation.arity or arguments:
            raise ValueError("metric requires a declared nullary initial numeric fluent")
        self.spec.metric = (direction.value, relation.predicate)


def _identifier(value: str) -> None:
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", value) is None:
        raise ValueError(f"invalid PDDL identifier {value!r}")


def _referenced_names(node: Node) -> set[str]:
    names: set[str] = {node.children[0].value} if node.kind in {"name", "index"} else set()
    for child in node.children:
        names.update(_referenced_names(child))
    return names


def _value_kind(value: Value) -> str:
    if isinstance(value, bool):
        return "Boolean"
    if isinstance(value, (int, float)):
        return "numeric"
    return type(value).__name__


def _group_name(value: str) -> Group:
    if value not in {"initial", "goal", "joint"}:
        raise ValueError(f"unknown constraint group {value!r}")
    return cast(Group, value)


def _parameter_value(parameter: Parameter, value: Value) -> Scalar:
    if value is None and parameter.nullable:
        return None
    if parameter.type_name == "int":
        result: Scalar = _integer(value)
    elif parameter.type_name == "float":
        result = float(_numeric(value))
        if not math.isfinite(result):
            raise SpecificationError("parameter must be finite", parameter.span)
    else:
        result = _string(value)
    return result


def _logical(operation: str, left: bool | z3.BoolRef, right: bool | z3.BoolRef) -> bool | z3.BoolRef:
    if isinstance(left, bool) and isinstance(right, bool):
        return {"and": left and right, "or": left or right, "implies": not left or right, "iff": left == right}[operation]
    a, b = _formula(left), _formula(right)
    return {"and": z3.And, "or": z3.Or, "implies": z3.Implies, "iff": operator.eq}[operation](a, b)


def _compare(operation: str, left: Value, right: Value) -> Value:
    if isinstance(left, (z3.BoolRef, z3.ArithRef)) or isinstance(right, (z3.BoolRef, z3.ArithRef)):
        if isinstance(left, (bool, z3.BoolRef)) or isinstance(right, (bool, z3.BoolRef)):
            if operation not in {"==", "!="}:
                raise ValueError("Booleans support equality only")
            a, b = _formula(left), _formula(right)
            return a == b if operation == "==" else a != b
        return _numeric_compare(operation, _arithmetic(left), _arithmetic(right))
    if operation in {"==", "!="}:
        if not _ground(left) or not _ground(right):
            raise ValueError("collection equality requires ground values")
        if left is not None and right is not None and _value_kind(left) != _value_kind(right):
            raise ValueError("equality operands have incompatible types")
        equal = left == right
        return equal if operation == "==" else not equal
    return _numeric_compare(operation, _numeric(left), _numeric(right))


def _numeric_compare(operation: str, left: int | float | z3.ArithRef,
                     right: int | float | z3.ArithRef) -> bool | z3.BoolRef:
    operators: dict[str, Callable[[int | float | z3.ArithRef, int | float | z3.ArithRef], bool | z3.BoolRef]] = {
        "==": operator.eq, "!=": operator.ne, "<": operator.lt, "<=": operator.le,
        ">": operator.gt, ">=": operator.ge,
    }
    return operators[operation](left, right)


def _calculate(operation: str, left: Value, right: Value) -> Value:
    if operation == "+" and isinstance(left, str) and isinstance(right, str):
        return left + right
    if operation == "+" and isinstance(left, tuple) and isinstance(right, tuple):
        return left + right
    if isinstance(left, z3.ArithRef) or isinstance(right, z3.ArithRef):
        a, b = _arithmetic(left), _arithmetic(right)
        if operation == "+":
            return a + b
        if operation == "-":
            return a + (-1 * b)
        if operation == "*" and (isinstance(a, int) or isinstance(b, int)):
            return a * b
        raise ValueError("symbolic arithmetic must be integer affine; division, powers and remainders must be ground")
    return _ground_calculate(operation, _numeric(left), _numeric(right))


def _ground_calculate(operation: str, left: int | float, right: int | float) -> int | float:
    if operation == "**":
        value: object = pow(left, right)
        if not isinstance(value, (int, float)):
            raise ValueError("numeric result must be real")
        return value
    operators: dict[str, Callable[[int | float, int | float], int | float]] = {
        "+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: a / b,
        "//": lambda a, b: a // b, "%": operator.mod,
    }
    return operators[operation](left, right)


def _reduce(kind: str, values: list[Value]) -> Value:
    if kind in {"forall", "exists"}:
        booleans = [_boolean(value) for value in values]
        if all(isinstance(value, bool) for value in booleans):
            return all(booleans) if kind == "forall" else any(booleans)
        operation = z3.And if kind == "forall" else z3.Or
        return operation(*(_formula(value) for value in booleans))
    terms = [_arithmetic(value) for value in values]
    if all(isinstance(value, int) for value in terms):
        return sum(terms)
    return z3.Sum(*terms)


def _builtin(name: str, arguments: tuple[Value, ...]) -> Value:
    if name in {"min", "max"}:
        values = _sequence(arguments[0]) if len(arguments) == 1 else arguments
        operation = min if name == "min" else max
        return operation(_numeric(value) for value in values)
    if len(arguments) != 1:
        raise ValueError(f"builtin {name!r} requires one argument")
    value = arguments[0]
    if name == "values":
        if not isinstance(value, Array):
            raise ValueError("values requires an indexed array")
        return tuple(value.entries.values())
    if name == "len":
        return len(value.entries) if isinstance(value, Array) else len(_sequence(value))
    if name == "str":
        return str(_scalar(value))
    operations: dict[str, Callable[[int | float], int | float]] = {
        "abs": abs, "ceil": math.ceil, "floor": math.floor, "trunc": math.trunc,
        "round": round, "int": int, "float": float,
    }
    if name not in operations:
        raise ValueError(f"unknown builtin {name!r}")
    return operations[name](_numeric(value))


def _grounding_budget(value: object) -> int | None:
    if value is None:
        return None
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise SpecificationError("max_groundings must be a positive integer")
    return value


def compile_definition(definition: Definition, parameters: Mapping[str, Scalar],
                       max_groundings: int | None = None) -> Specification:
    """Compile all finite declarations; an exhausted budget never returns a partial spec."""
    compiler = Compiler(definition, _grounding_budget(max_groundings))
    compiler.parameters(parameters)
    for node in definition.statements:
        compiler.statement(node)
    constraints = (*compiler.spec.declarations, *compiler.spec.initial, *compiler.spec.goal, *compiler.spec.joint)
    names: set[str] = set()
    for constraint in constraints:
        if constraint.name in names:
            raise SpecificationError("rule name collides with an implicit declaration constraint", constraint.source)
        names.add(constraint.name)
    return compiler.spec
