"""Shared structural learning ranges for the two Blocksworld encodings."""

from collections.abc import Callable
from typing import TypeVar

from ..splits import Split

P = TypeVar("P")


def blocks_spaces(factory: Callable[[int], P]) -> dict[Split, list[P]]:
    """Use disjoint block counts while keeping the encodings directly comparable."""
    ranges: dict[Split, range] = {
        "train": range(4, 11), "valid": range(11, 16), "test": range(16, 25),
    }
    return {split: [factory(size) for size in sizes] for split, sizes in ranges.items()}
