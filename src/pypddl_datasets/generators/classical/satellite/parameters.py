"""Validated structural parameters for satellite."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts, validate_probabilities


@dataclass(frozen=True)
class Parameters:
    """The supported finite satellite configuration."""

    num_satellites: int
    num_instruments: int
    num_modes: int
    num_targets: int
    num_observations: int
    pointing_goal_probability: float = 0.0

    def __post_init__(self) -> None:
        validate_counts((
            ("num_satellites", self.num_satellites, 1),
            ("num_instruments", self.num_instruments, 1),
            ("num_modes", self.num_modes, 1),
            ("num_targets", self.num_targets, 1),
            ("num_observations", self.num_observations, 1),
        ))
        validate_probabilities((
            ("pointing_goal_probability", self.pointing_goal_probability),
        ))
