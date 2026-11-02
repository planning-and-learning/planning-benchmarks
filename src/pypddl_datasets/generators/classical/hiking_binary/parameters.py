"""Conservative Hiking Binary parameters."""

from __future__ import annotations

from dataclasses import dataclass

from ..hiking.parameters import Parameters as HikingParameters


@dataclass(frozen=True)
class Parameters(HikingParameters):
    """Retain the historical extra-car precondition of the binary generator."""

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.num_cars < self.num_couples + 1:
            raise ValueError("num_cars must be at least num_couples + 1")
