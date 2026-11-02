"""Finite labeled interpretations, named formulas, and projected model enumeration."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from time import monotonic
from types import MappingProxyType
from typing import TYPE_CHECKING, Literal, cast

from .interpretation import SemanticKey, Situation, Value

if TYPE_CHECKING:
    from .syntax import SourceSpan

try:
    import z3
except ImportError as error:
    raise ImportError("Executable specifications require pypddl-datasets[specs]") from error

Group = Literal["initial", "goal", "joint"]
Status = Literal["complete", "limit", "timeout", "unknown"]


@dataclass(frozen=True)
class NamedConstraint:
    """A readable identifier and its executable logical formula."""
    name: str
    description: str
    formula: z3.BoolRef
    source: SourceSpan | None = None


@dataclass(frozen=True)
class MembershipResult:
    """Membership status; ``unknown`` must never be treated as acceptance."""
    status: Literal["member", "nonmember", "unknown", "timeout"]
    violations: tuple[str, ...] = ()
    detail: str = ""

    @property
    def is_member(self) -> bool:
        """Whether the solver established membership."""
        return self.status == "member"


@dataclass(frozen=True)
class EnumerationResult:
    """Bounded enumeration, with explicit evidence of whether it was exhausted."""
    situations: tuple[Situation, ...]
    status: Status
    detail: str = ""

    @property
    def complete(self) -> bool:
        """True only after the remaining model space was proved empty."""
        return self.status == "complete"


class Specification:
    """An executable finite-domain distribution contract.

    Every declared semantic variable is bound during membership checks, including
    absent initial/goal atoms. Enumeration blocks only the requested semantic
    projection, so different witnesses cannot duplicate a situation.
    """

    def __init__(self, domain: str) -> None:
        self.domain = domain
        self._semantic: dict[SemanticKey, z3.BoolRef | z3.ArithRef] = {}
        self._auxiliary: list[z3.ExprRef] = []
        self._declarations: list[NamedConstraint] = []
        self._constraints: dict[Group, list[NamedConstraint]] = {
            "initial": [], "goal": [], "joint": [],
        }
        self._objects: dict[str, str] = {}
        self.metric: tuple[str, str] | None = None

    @property
    def semantic_variables(self) -> Mapping[SemanticKey, z3.BoolRef | z3.ArithRef]:
        """Read-only semantic symbols, excluding proof witnesses."""
        return MappingProxyType(self._semantic)

    @property
    def auxiliary_variables(self) -> tuple[z3.ExprRef, ...]:
        """Witnesses excluded from situation identity."""
        return tuple(self._auxiliary)

    @property
    def object_universe(self) -> Mapping[str, str]:
        """Finite possible object names and declared types (constants excluded)."""
        return MappingProxyType(self._objects)

    @property
    def declarations(self) -> tuple[NamedConstraint, ...]:
        """Finite variable-domain constraints, active for every rule projection."""
        return tuple(self._declarations)

    def add_declaration(self, name: str, formula: z3.BoolRef,
                        source: SourceSpan | None = None) -> None:
        """Retain declared variable domains independently of selected rule groups."""
        self._declarations.append(NamedConstraint(f"declaration.{name}", name, formula, source))

    @property
    def initial(self) -> tuple[NamedConstraint, ...]:
        """Named constraints on initial facts and static structure."""
        return tuple(self._constraints["initial"])

    @property
    def goal(self) -> tuple[NamedConstraint, ...]:
        """Named constraints on goal-atom membership, not initial truth."""
        return tuple(self._constraints["goal"])

    @property
    def joint(self) -> tuple[NamedConstraint, ...]:
        """Named relationships between the initial and goal interpretations."""
        return tuple(self._constraints["joint"])

    def add(self, group: Group, name: str, formula: z3.BoolRef, description: str = "",
            *, source: SourceSpan | None = None) -> None:  # pylint: disable=too-many-arguments
        """Add an independently readable rule."""
        identifier = f"{group}.{name}"
        self._constraints[group].append(NamedConstraint(identifier, description or name.replace("_", " "), formula, source))

    def atom(self, group: Group, predicate: str, *arguments: str) -> z3.BoolRef:
        """Declare a possible atom; undeclared atoms are outside the contract."""
        key = SemanticKey(group, "atom", predicate.lower(), tuple(arg.lower() for arg in arguments))
        if key not in self._semantic:
            self._semantic[key] = z3.Bool(f"{group}:{predicate}:{':'.join(arguments)}")
        return cast(z3.BoolRef, self._semantic[key])

    def objects(self, names: Sequence[str], type_name: str = "object", optional: bool = False) -> None:
        """Declare a finite typed universe, optionally allowing absent objects."""
        for name in names:
            self._objects[name] = type_name.lower()
            key = SemanticKey("initial", "object", name, (type_name.lower(),))
            self._semantic[key] = z3.Bool(f"object:{name}")
            if not optional:
                self.add("initial", f"object_{name}", cast(z3.BoolRef, self._semantic[key]))

    def present(self, name: str) -> z3.BoolRef:
        """Object-declaration membership for variable-size universes."""
        return cast(z3.BoolRef, self._semantic[SemanticKey("initial", "object", name, (self._objects[name],))])

    def number(self, predicate: str, *arguments: str) -> z3.ArithRef:
        """Declare an integer-valued initialized fluent."""
        key = SemanticKey("initial", "number", predicate, tuple(arguments))
        if key not in self._semantic:
            self._semantic[key] = z3.Int(f"number:{predicate}:{':'.join(arguments)}")
        return cast(z3.ArithRef, self._semantic[key])

    def witness(self, name: str) -> z3.ArithRef:
        """Create an auxiliary integer witness, excluded from model blocking."""
        result = z3.Int(f"witness:{name}")
        self._auxiliary.append(result)
        return result

    def boolean_witness(self, name: str) -> z3.BoolRef:
        """Create an auxiliary Boolean witness excluded from model blocking."""
        result = z3.Bool(f"witness:{name}")
        self._auxiliary.append(result)
        return result

    def solver(self, groups: Sequence[Group] = ("initial", "goal", "joint")) -> z3.Solver:
        """Create a fresh solver; callers may add corner-case predicates."""
        solver = z3.Solver()
        for declaration in self._declarations:
            solver.assert_and_track(declaration.formula, declaration.name)
        for group in groups:
            for constraint in self._constraints[group]:
                solver.assert_and_track(constraint.formula, constraint.name)
        return solver

    def check(self, situation: Situation, timeout_ms: int | None = None) -> MembershipResult:
        """Bind every semantic variable to an interpretation and check all rules."""
        errors = _value_errors(situation)
        if errors:
            return MembershipResult("nonmember", ("interpretation.values",), errors)
        values = dict(situation.values)
        extra = values.keys() - self._semantic.keys()
        missing_numbers = [key for key in self._semantic if key.kind == "number" and key not in values]
        if extra or missing_numbers:
            return MembershipResult("nonmember", ("initial_or_goal.vocabulary",),
                                    f"Unexpected symbols: {sorted(extra)}; missing numbers: {missing_numbers}")
        solver = self.solver()
        if timeout_ms is not None:
            if timeout_ms < 1:
                raise ValueError("timeout_ms must be positive")
            solver.set(timeout=timeout_ms)
        for key, variable in self._semantic.items():
            solver.add(variable == values.get(key, False))
        result = solver.check()
        if result == z3.sat:
            return MembershipResult("member")
        if result == z3.unsat:
            return MembershipResult("nonmember", tuple(str(rule) for rule in solver.unsat_core()))
        reason = solver.reason_unknown()
        return MembershipResult("timeout" if "timeout" in reason else "unknown", detail=reason)

    def check_pddl(self, source: str | Path, timeout_ms: int | None = None) -> MembershipResult:
        """Parse PDDL independently using strict pypddl and check membership."""
        from .decoding import decode_pddl  # pylint: disable=import-outside-toplevel
        domain_path = Path(__file__).parents[1] / "classical" / self.domain / "domain.pddl"
        try:
            situation, metric = decode_pddl(domain_path, source)
        except (ValueError, RuntimeError) as error:
            return MembershipResult("nonmember", ("pddl.syntax_or_semantics",), str(error))
        if metric != self.metric:
            return MembershipResult("nonmember", ("joint.metric",), f"Expected {self.metric}, got {metric}")
        return self.check(situation, timeout_ms)

    def enumerate(self, limit: int = 1000, timeout_ms: int | None = None,
                  projection: Sequence[SemanticKey] | None = None,
                  groups: Sequence[Group] = ("initial", "goal", "joint")) -> EnumerationResult:
        """Enumerate projected interpretations under a total wall-clock budget."""
        if limit < 0 or (timeout_ms is not None and timeout_ms < 1):
            raise ValueError("limit must be nonnegative and timeout_ms must be positive")
        keys = tuple(self._semantic) if projection is None else tuple(projection)
        if any(key not in self._semantic for key in keys):
            raise ValueError("projection contains an undeclared semantic variable")
        solver = self.solver(groups)
        situations: list[Situation] = []
        deadline = None if timeout_ms is None else monotonic() + timeout_ms / 1000
        while True:
            if deadline is not None:
                remaining = int((deadline - monotonic()) * 1000)
                if remaining <= 0:
                    return EnumerationResult(tuple(situations), "timeout", "total enumeration budget exhausted")
                solver.set(timeout=remaining)
            result = solver.check()
            if result == z3.unsat:
                return EnumerationResult(tuple(situations), "complete")
            if result != z3.sat:
                reason = solver.reason_unknown()
                return EnumerationResult(tuple(situations), "timeout" if "timeout" in reason else "unknown", reason)
            if len(situations) == limit:
                return EnumerationResult(tuple(situations), "limit")
            model = solver.model()
            values = tuple((key, _model_value(model.eval(self._semantic[key], model_completion=True))) for key in keys)
            situations.append(Situation(values))
            solver.add(z3.Or(*(self._semantic[key] != value for key, value in values)))


def _model_value(value: z3.ExprRef) -> Value:
    if z3.is_int_value(value):
        return cast(z3.IntNumRef, value).as_long()
    return z3.is_true(value)


def _value_errors(situation: Situation) -> str:
    seen: dict[SemanticKey, Value] = {}
    for key, value in situation.values:
        if not _valid_value(value, numeric=key.kind == "number"):
            return f"Invalid value type for {key}: {type(value).__name__}"
        if key in seen and seen[key] != value:
            return f"Conflicting values for {key}"
        seen[key] = value
    return ""


def _valid_value(value: object, numeric: bool) -> bool:
    if numeric:
        return isinstance(value, int) and not isinstance(value, bool)
    return isinstance(value, bool)
