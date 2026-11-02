"""Validated structural parameters for gripper."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite gripper configuration."""

    num_balls: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_balls", self.num_balls, 1),
        ))
