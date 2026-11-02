"""Validated structural parameters for goldminer."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite goldminer configuration."""

    num_rows: int
    num_cols: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_rows", self.num_rows, 2),
            ("num_cols", self.num_cols, 3),
        ))
