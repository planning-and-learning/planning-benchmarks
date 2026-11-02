"""Validated structural parameters for ferry."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite ferry configuration."""

    num_cars: int
    num_locations: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_cars", self.num_cars, 0),
            ("num_locations", self.num_locations, 1),
        ))
