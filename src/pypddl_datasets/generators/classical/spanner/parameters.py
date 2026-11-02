"""Parameters for the fixed-chain Spanner family."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    """The number of labeled resources and internal chain locations."""

    num_spanners: int
    num_nuts: int
    num_locations: int

    def __post_init__(self) -> None:
        if min(self.num_spanners, self.num_nuts, self.num_locations) < 1:
            raise ValueError("spanners, nuts and locations must be positive")
        if self.num_nuts > self.num_spanners:
            raise ValueError("num_nuts must not exceed num_spanners")
