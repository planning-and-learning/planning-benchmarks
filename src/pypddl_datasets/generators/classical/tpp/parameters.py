"""Validated structural parameters for tpp."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite tpp configuration."""

    num_goods: int
    num_trucks: int
    num_markets: int
    num_depots: int
    max_level: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_goods", self.num_goods, 1),
            ("num_trucks", self.num_trucks, 1),
            ("num_markets", self.num_markets, 1),
            ("num_depots", self.num_depots, 1),
            ("max_level", self.max_level, 1),
        ))
