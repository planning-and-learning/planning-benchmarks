"""Validated structural parameters for miconic."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite miconic configuration."""

    num_floors: int
    num_passengers: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_floors", self.num_floors, 1),
            ("num_passengers", self.num_passengers, 1),
        ))
