"""Parameters for the fuel-constrained transport family."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Parameters:
    """A connected Bernoulli road graph and independently placed packages."""

    num_locations: int = 6
    num_packages: int = 6
    edge_factor: float = 1.5
    max_edge_cost: int = 25
    constrainedness: float = 1.0
    edge_probability: float | None = 0.5

    @property
    def probability(self) -> float:
        """Translate the historical density parameter unless overridden."""
        if self.edge_probability is not None:
            return self.edge_probability
        return min(1.0, 2 * self.edge_factor / (self.num_locations - 1))

    def __post_init__(self) -> None:
        if self.num_locations < 2 or self.num_packages < 1 or self.max_edge_cost < 1:
            raise ValueError("need at least two locations, one package and positive costs")
        if not isfinite(self.edge_factor) or self.edge_factor < 1:
            raise ValueError("edge_factor must be finite and at least 1")
        if not isfinite(self.constrainedness) or self.constrainedness < 1:
            raise ValueError("constrainedness must be finite and at least 1")
        if not isfinite(self.probability) or not 0 < self.probability <= 1:
            raise ValueError("edge_probability must be finite and in (0, 1]")
