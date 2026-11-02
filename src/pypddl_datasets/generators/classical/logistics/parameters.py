"""Validated structural parameters for logistics."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts, validate_probabilities


@dataclass(frozen=True)
class Parameters:
    """The supported finite logistics configuration."""

    num_cities: int
    city_size: int
    num_packages: int
    num_airplanes: int
    goal_package_probability: float = 1.0

    def __post_init__(self) -> None:
        validate_counts((
            ("num_cities", self.num_cities, 1),
            ("city_size", self.city_size, 2),
            ("num_packages", self.num_packages, 1),
            ("num_airplanes", self.num_airplanes, 1),
        ))
        validate_probabilities((
            ("goal_package_probability", self.goal_package_probability),
        ))
