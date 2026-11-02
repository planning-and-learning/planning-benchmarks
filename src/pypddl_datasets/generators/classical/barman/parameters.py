"""Validated structural parameters for barman."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts, validate_probabilities


@dataclass(frozen=True)
class Parameters:
    """The supported finite barman configuration."""

    num_cocktails: int
    num_ingredients: int
    num_shots: int
    ingredient_goal_probability: float = 0.0
    num_goals: int | None = None

    def __post_init__(self) -> None:
        validate_counts((
            ("num_cocktails", self.num_cocktails, 1),
            ("num_ingredients", self.num_ingredients, 2),
            ("num_shots", self.num_shots, 2),
        ))
        validate_probabilities((
            ("ingredient_goal_probability", self.ingredient_goal_probability),
        ))
        count = self.num_shots - 1 if self.num_goals is None else self.num_goals
        if not 1 <= count <= self.num_shots:
            raise ValueError("num_goals must be between 1 and num_shots")
