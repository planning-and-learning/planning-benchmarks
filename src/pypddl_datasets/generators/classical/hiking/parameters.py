"""Validated structural parameters for hiking."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite hiking configuration."""

    num_couples: int
    num_cars: int
    num_places: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_couples", self.num_couples, 1),
            ("num_cars", self.num_cars, 1),
            ("num_places", self.num_places, 2),
        ))
