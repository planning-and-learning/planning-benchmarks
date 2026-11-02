"""Instance-local ProbLog sampling, including choices inside nested findall."""
from __future__ import annotations

from contextvars import ContextVar
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any

from problog import get_evaluatable
from problog.logic import Constant, Term
from problog.tasks.sample import SampledFormula
from typing_extensions import override

from ..runtime import RandomSource
from .numbers import RationalSemiring, rational
from .programs import new_engine, program
from .reference import conditioned_formula
from .prepared import prepared_program


@dataclass
class WorldChoices:
    """One draw cache shared by every nested formula in one sampled world."""
    rng: RandomSource
    facts: dict[Any, int | None] = field(default_factory=lambda: {})
    primitives: dict[tuple[Any, ...], bool] = field(default_factory=lambda: {})
    selections: dict[tuple[Any, ...], tuple[Term, Term] | None] = field(default_factory=lambda: {})
    groups: dict[Any, Fraction | None] = field(default_factory=lambda: {})


_WORLD: ContextVar[WorldChoices] = ContextVar("pypddl_problog_world")


class SampleFormula(SampledFormula):
    """ProbLog calls this constructor again for nested aggregation targets."""
    def __init__(self, **options: Any) -> None:
        super().__init__(**options)
        self.world = _WORLD.get()
        self.facts = self.world.facts
        self.groups = self.world.groups

    def _choose(self, weight: Fraction, probability: Term, categorical: bool) -> bool:
        if weight in (0, 1):
            return bool(weight)
        if not categorical and isinstance(probability, Constant) and probability.is_float():
            return self.world.rng.random() < float(probability)
        return self.world.rng.randrange(weight.denominator) < weight.numerator

    @override
    def add_atom(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self, identifier: Any, probability: Term | None, group: Any = None,
        name: Any = None, source: Any = None, cr_extra: bool = True, is_extra: bool = False,
    ) -> int | None:
        del name, source, cr_extra, is_extra
        if probability is None:
            return self.TRUE
        if identifier in self.facts:
            return self.facts[identifier]
        weight = rational(probability)
        if not 0 <= weight <= 1:
            raise ValueError(f"probability outside [0,1]: {weight}")
        if group is None:
            chosen = self._choose(weight, probability, False)
        else:
            chosen = self._group_choice(identifier, weight, probability)
        result = self.TRUE if chosen else self.FALSE
        self.facts[identifier] = result
        return result

    def _group_choice(self, identifier: Any, weight: Fraction, probability: Term) -> bool:
        origin = identifier[:-1]
        remaining = self.groups.get(origin, Fraction(1))
        if remaining is None:
            return False
        if weight > remaining:
            raise ValueError("categorical probabilities exceed one")
        chosen = remaining > 0 and self._choose(weight / remaining, probability, remaining != 1)
        self.groups[origin] = None if chosen else remaining - weight
        return chosen


def sample_source(source: str, rng: RandomSource, *, accelerated: bool = True) -> dict[Term, bool]:
    """Sample one world without ambient RNG or numeric configuration changes."""
    with prepared_program(source, accelerated=accelerated) as prepared:
        token = _WORLD.set(WorldChoices(rng))
        try:
            target = SampleFormula()
            prepared.engine.ground_queries(prepared.database, target, prepared.queries)
            result: dict[Term, bool] = {}
            for query, value in target.to_dict().items():
                if not isinstance(value, bool):
                    raise TypeError("the task backend requires Boolean query results")
                result[query] = value
            return result
        finally:
            _WORLD.reset(token)


def evaluate_source(source: str) -> dict[str, Fraction]:
    """Exact finite reference inference; callers must bound their problem size."""
    engine = new_engine()
    formula = conditioned_formula(engine, engine.prepare(program(source)))
    result = get_evaluatable().create_from(formula).evaluate(semiring=RationalSemiring())
    return {str(query): weight for query, weight in result.items()}
