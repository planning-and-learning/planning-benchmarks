"""Parameters for independent Schedule part attributes."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    """Attribute-domain sizes and inclusion probabilities in percent."""

    num_parts: int
    num_shapes: int = 0
    num_colours: int = 2
    num_widths: int = 2
    num_orientations: int = 2
    cylindrical_goal_probability: int = 80
    initial_colour_probability: int = 50
    goal_colour_probability: int = 80
    initial_hole_probability: int = 50
    goal_hole_probability: int = 80
    goal_surface_probability: int = 50

    def __post_init__(self) -> None:
        if self.num_parts < 1 or not 0 <= self.num_shapes <= 2:
            raise ValueError("parts must be positive and num_shapes must be in [0, 2]")
        if not (1 <= self.num_colours <= 4 and 1 <= self.num_widths <= 3
                and 1 <= self.num_orientations <= 2):
            raise ValueError("attribute counts exceed their available domains")
        probabilities = (
            self.cylindrical_goal_probability, self.initial_colour_probability,
            self.goal_colour_probability, self.initial_hole_probability,
            self.goal_hole_probability, self.goal_surface_probability,
        )
        if any(not 0 <= probability <= 100 for probability in probabilities):
            raise ValueError("probabilities must be integer percentages in [0, 100]")
