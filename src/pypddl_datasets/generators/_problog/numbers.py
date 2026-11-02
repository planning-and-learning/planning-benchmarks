"""Unrounded arithmetic and exact finite probability weights.

Only our parser/engine is configured; the installed ProbLog classes and global
random module remain unchanged. Rational annotation expressions retain their
integer arithmetic. Float annotations denote the decimal value of their Python
repr; direct Bernoulli sampling still uses the legacy binary64 threshold.
"""
from __future__ import annotations

from fractions import Fraction
from collections.abc import Callable
from typing import Any

from problog.engine_builtin import check_mode
from problog.engine_unify import UnifyError, unify_value
from problog.evaluator import Semiring
from problog.logic import Constant, Term, unquote
from problog.program import ExtendedPrologFactory
from typing_extensions import override


def unrounded_constant(value: Any, **options: Any) -> Constant:
    """Keep ProbLog's exact Constant type: nested term equality checks types."""
    result = object.__new__(Constant)
    result.FLOAT_PRECISION = None
    Constant.__init__(result, value, **options)
    return result


class NumericFactory(ExtendedPrologFactory):
    """Preserve positive and negative numeric literals in this model only."""
    @override
    def build_constant(self, value: Any, location: Any = None) -> Constant:
        return unrounded_constant(value, location=(self.loc_id, location))

    @override
    def build_unop(self, functor: str, operand: Term, location: Any = None, **extra: Any) -> Term:
        if functor == "-" and isinstance(operand, Constant) and (operand.is_float() or operand.is_integer()):
            return unrounded_constant(-operand.value)
        return self.build_function(f"'{functor}'", (operand,), location=location, **extra)


def unrounded_is(left: Any, right: Term, engine: Any = None, **context: Any) -> list[tuple[Term, Term]]:
    """Instance-local implementation of ordinary Prolog arithmetic evaluation."""
    check_mode((left, right), ["*g"], functor="is", **context)
    value = right.compute_value(engine.functions)
    if value is None:
        return []
    result = unrounded_constant(value)
    try:
        unify_value(left, result, {})
    except UnifyError:
        return []
    return [(result, right)]


def rational(value: Any) -> Fraction:
    """Evaluate integer probability expressions without a float conversion."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, (int, float)):
        return Fraction(str(value))
    if not isinstance(value, Term):
        raise TypeError(f"unsupported probability weight {value!r}")
    operation = unquote(str(value.functor))
    if operation == "-" and len(value.args) == 1:
        return -rational(value.args[0])
    operations: dict[str, Callable[[Fraction, Fraction], Fraction]] = {
        "+": lambda a, b: a + b, "-": lambda a, b: a - b,
        "*": lambda a, b: a * b, "/": lambda a, b: a / b,
    }
    if operation in operations and len(value.args) == 2:
        return operations[operation](rational(value.args[0]), rational(value.args[1]))
    if operation == "**" and len(value.args) == 2:
        exponent = rational(value.args[1])
        if exponent.denominator != 1:
            raise ValueError("probability exponents must be integers")
        return rational(value.args[0]) ** exponent.numerator
    return Fraction(str(value.compute_value()))


# Semiring.create is an unused CLI factory; programmatic evaluation takes an instance.
class RationalSemiring(Semiring):  # pylint: disable=abstract-method
    """No epsilon thresholds or underflow in finite reference inference."""
    @override
    def one(self) -> Fraction:
        return Fraction(1)

    @override
    def zero(self) -> Fraction:
        return Fraction(0)

    @override
    def is_one(self, value: Fraction) -> bool:
        return value == 1

    @override
    def is_zero(self, value: Fraction) -> bool:
        return value == 0

    @override
    def plus(self, a: Fraction, b: Fraction) -> Fraction:
        return a + b

    @override
    def times(self, a: Fraction, b: Fraction) -> Fraction:
        return a * b

    @override
    def negate(self, a: Fraction) -> Fraction:
        return 1 - a

    @override
    def normalize(self, a: Fraction, z: Fraction) -> Fraction:
        return a / z

    @override
    def value(self, a: Any) -> Fraction:
        result = rational(a)
        if not 0 <= result <= 1:
            raise ValueError(f"probability outside [0,1]: {result}")
        return result

    @override
    def is_dsp(self) -> bool:
        return True

    @override
    def in_domain(self, a: Fraction) -> bool:
        return 0 <= a <= 1

    @override
    def result_in_domain(self, a: Fraction) -> bool:
        return self.in_domain(a)
