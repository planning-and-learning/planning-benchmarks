"""Parameters for the rectangular Visitall family."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Parameters:
    """Grid geometry, unavailable-cell count and legacy goal threshold."""

    width: int
    height: int | None = None
    goal_ratio: float = 1.0
    num_unavailable: int = 0

    @property
    def rows(self) -> int:
        """Resolve the square-grid shorthand without changing the parameters."""
        return self.width if self.height is None else self.height

    def __post_init__(self) -> None:
        if self.width < 1 or self.rows < 1:
            raise ValueError("grid dimensions must be positive")
        if not isfinite(self.goal_ratio) or not 0 <= self.goal_ratio <= 1:
            raise ValueError("goal_ratio must be finite and in [0, 1]")
        if not 0 <= self.num_unavailable < self.width * self.rows:
            raise ValueError("num_unavailable must be smaller than the grid")
