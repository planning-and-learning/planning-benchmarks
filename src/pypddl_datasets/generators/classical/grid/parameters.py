"""Validated structural parameters for grid."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts, validate_probabilities


@dataclass(frozen=True)
class Parameters:
    """The supported finite grid configuration."""

    width: int
    height: int
    num_shapes: int = 2
    num_keys: int = 2
    num_locks: int = 2
    goal_probability: float = 1.0

    def __post_init__(self) -> None:
        validate_counts((
            ("width", self.width, 2),
            ("height", self.height, 2),
            ("num_shapes", self.num_shapes, 1),
            ("num_keys", self.num_keys, 1),
            ("num_locks", self.num_locks, 1),
        ))
        validate_probabilities((
            ("goal_probability", self.goal_probability),
        ))
        if min(self.num_keys, self.num_locks) < self.num_shapes:
            raise ValueError("keys and locks must cover every shape")
        if self.num_locks >= self.width * self.height:
            raise ValueError("at least one position must be open")
        if self.goal_probability == 0:
            raise ValueError("goal_probability must be positive")
