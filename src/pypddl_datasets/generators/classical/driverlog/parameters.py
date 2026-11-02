"""Validated structural parameters for driverlog."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts, validate_probabilities


@dataclass(frozen=True)
class Parameters:
    """The supported finite driverlog configuration."""

    num_locations: int
    num_drivers: int
    num_trucks: int
    num_packages: int
    package_goal_probability: float = 1.0
    driver_goal_probability: float = 0.0
    truck_goal_probability: float = 0.0
    edge_probability: float = 0.5

    def __post_init__(self) -> None:
        validate_counts((
            ("num_locations", self.num_locations, 2),
            ("num_drivers", self.num_drivers, 1),
            ("num_trucks", self.num_trucks, 1),
            ("num_packages", self.num_packages, 1),
        ))
        validate_probabilities((
            ("package_goal_probability", self.package_goal_probability),
            ("driver_goal_probability", self.driver_goal_probability),
            ("truck_goal_probability", self.truck_goal_probability),
            ("edge_probability", self.edge_probability),
        ))
        if self.edge_probability == 0:
            raise ValueError("edge_probability must be positive for connected graphs")
