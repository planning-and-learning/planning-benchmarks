"""Small validation and construction helpers shared by classical generators."""

from __future__ import annotations

from collections.abc import Iterable
import math

from pypddl_datasets.generators.runtime import Atom, RandomSource, atom


def validate_counts(values: Iterable[tuple[str, int, int]]) -> None:
    """Reject cardinalities below their domain-specific minima."""
    for name, value, minimum in values:
        if value < minimum:
            raise ValueError(f"{name} must be at least {minimum}")


def validate_probabilities(values: Iterable[tuple[str, float]]) -> None:
    """Require finite probabilities, including the explicitly supported endpoints."""
    for name, value in values:
        if not math.isfinite(value) or not 0 <= value <= 1:
            raise ValueError(f"{name} must be finite and in [0, 1]")


def placement_goals(
    positions: dict[str, str], locations: list[str], probability: float, rng: RandomSource,
) -> tuple[Atom, ...]:
    """Choose non-origin goals with the historical nonempty singleton repair."""
    selected = [name for name in positions if rng.random() < probability]
    if not selected and probability > 0:
        selected = [rng.choice(list(positions))]
    return tuple(atom("at", name, rng.choice([place for place in locations
                                             if place != positions[name]]))
                 for name in selected)
