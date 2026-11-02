"""Validated structural parameters for blocks_3."""

from __future__ import annotations

from dataclasses import dataclass

from .._support import validate_counts


@dataclass(frozen=True)
class Parameters:
    """The supported finite blocks_3 configuration."""

    num_blocks: int

    def __post_init__(self) -> None:
        validate_counts((
            ("num_blocks", self.num_blocks, 1),
        ))
