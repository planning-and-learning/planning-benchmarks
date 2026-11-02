"""Validated structural parameters for childsnack."""

from __future__ import annotations

from dataclasses import dataclass
import math

from .._support import validate_counts, validate_probabilities


@dataclass(frozen=True)
class Parameters:
    """The supported finite childsnack configuration."""

    num_children: int
    num_trays: int
    gluten_factor: float
    const_ratio: float = 1.2

    def __post_init__(self) -> None:
        validate_counts((
            ("num_children", self.num_children, 1),
            ("num_trays", self.num_trays, 1),
        ))
        validate_probabilities((
            ("gluten_factor", self.gluten_factor),
        ))
        if not math.isfinite(self.const_ratio) or self.const_ratio < 1:
            raise ValueError("const_ratio must be finite and at least 1")
