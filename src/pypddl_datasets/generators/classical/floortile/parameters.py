"""Validated structural parameters for floortile."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite floortile configuration."""

    num_rows: int
    num_columns: int
    num_robots: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_rows", self.num_rows, 1),
            ("num_columns", self.num_columns, 1),
            ("num_robots", self.num_robots, 1),
        ))
        if self.num_robots > self.num_columns:
            raise ValueError("num_robots must not exceed num_columns")
