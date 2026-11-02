"""Parameters for the resource-constructed Woodworking family."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Parameters:
    """Parts, machines of each type, and available wood multiplier."""

    num_parts: int
    num_machines: int
    wood_factor: float = 1.0

    def __post_init__(self) -> None:
        if self.num_parts < 1 or self.num_machines < 1:
            raise ValueError("parts and machines must be positive")
        if not isfinite(self.wood_factor) or self.wood_factor < 1:
            raise ValueError("wood_factor must be finite and at least 1")
