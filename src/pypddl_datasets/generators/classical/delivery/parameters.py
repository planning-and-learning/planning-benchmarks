"""Validated structural parameters for delivery."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite delivery configuration."""

    grid_size: int
    num_packages: int

    def __post_init__(self) -> None:
        validate_counts((
            ("grid_size", self.grid_size, 2),
            ("num_packages", self.num_packages, 1),
        ))
