"""Parameters for the Rovers family."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Parameters:
    """Counts and probability of an edge in a connected movement graph."""

    num_rovers: int
    num_waypoints: int
    num_objectives: int
    num_cameras: int
    num_goals: int
    edge_probability: float = 0.5

    def __post_init__(self) -> None:
        if min(self.num_rovers, self.num_waypoints, self.num_objectives, self.num_goals) < 1:
            raise ValueError("rovers, waypoints, objectives and goal density must be positive")
        if self.num_cameras < 0:
            raise ValueError("num_cameras must be non-negative")
        if not isfinite(self.edge_probability) or not 0 <= self.edge_probability <= 1:
            raise ValueError("edge_probability must be finite and in [0, 1]")
        if self.num_waypoints > 1 and self.edge_probability == 0:
            raise ValueError("a nontrivial connected graph needs positive edge probability")
