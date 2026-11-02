"""Exact finite choice-tree enumeration, independent of ProbLog execution."""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, MutableSequence, Sequence
from fractions import Fraction
from typing import TypeVar

from pypddl_datasets.generators.runtime import Atom, Object, Problem

T = TypeVar("T")
TaskKey = tuple[frozenset[Object], frozenset[Atom], frozenset[Atom]]


def signature(problem: Problem) -> TaskKey:
    """Compare labeled tasks without serialization order or names."""
    assert all(isinstance(fact, Atom) for fact in problem.initial)
    return (frozenset(problem.objects),
            frozenset(fact for fact in problem.initial if isinstance(fact, Atom)),
            frozenset(problem.goal))


class NextChoice(Exception):
    """Suspend execution when the next ideal categorical draw is unknown."""
    def __init__(self, count: int) -> None:
        super().__init__(count)
        self.count = count


class Trace:
    """Replay categorical draws; real draws are valid only at Bernoulli endpoints."""
    def __init__(self, prefix: tuple[int, ...]) -> None:
        self.prefix = prefix
        self.index = 0

    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int:
        values = range(start) if stop is None else range(start, stop, step)
        if len(values) == 1:
            return values[0]
        if self.index == len(self.prefix):
            raise NextChoice(len(values))
        result = values[self.prefix[self.index]]
        self.index += 1
        return result

    def choice(self, seq: Sequence[T]) -> T:
        return seq[self.randrange(len(seq))]

    def random(self) -> float:
        return 0.5

    def randint(self, a: int, b: int) -> int:
        return self.randrange(a, b + 1)

    def sample(self, population: Sequence[T], k: int) -> list[T]:
        remaining = list(population)
        return [remaining.pop(self.randrange(len(remaining))) for _ in range(k)]

    def shuffle(self, x: MutableSequence[T]) -> None:
        for index in range(len(x) - 1, 0, -1):
            other = self.randrange(index + 1)
            x[index], x[other] = x[other], x[index]


def distribution(run: Callable[[Trace], Problem]) -> tuple[dict[TaskKey, Fraction], dict[TaskKey, Problem]]:
    """Sum exact categorical-history weights, including duplicate projections."""
    pending: list[tuple[tuple[int, ...], Fraction]] = [((), Fraction(1))]
    probabilities: defaultdict[TaskKey, Fraction] = defaultdict(Fraction)
    problems: dict[TaskKey, Problem] = {}
    explored = 0
    while pending:
        prefix, mass = pending.pop()
        explored += 1
        assert explored <= 2_000_000, "finite reference exceeded its exploration budget"
        try:
            problem = run(Trace(prefix))
        except NextChoice as decision:
            pending.extend(((*prefix, index), mass / decision.count)
                           for index in range(decision.count))
        else:
            key = signature(problem)
            probabilities[key] += mass
            problems[key] = problem
    assert sum(probabilities.values(), Fraction()) == 1
    return dict(probabilities), problems
