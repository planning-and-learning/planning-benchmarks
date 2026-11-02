"""Immutable domain construction values for Woodworking."""
from dataclasses import dataclass
from pypddl_datasets.generators.runtime import Assignment, Atom, atom

COLOURS = ("black", "white", "red", "green", "blue", "mauve")
WOODS = ("oak", "pine", "cherry", "teak", "mahogany", "beech", "walnut")
MACHINES = ("highspeed-saw", "glazer", "grinder", "immersion-varnisher", "planer", "saw", "spray-varnisher")
PROPERTIES = ("treatment", "surface-condition", "colour", "wood")


@dataclass(frozen=True)
class Properties:
    """One value for each physical part attribute."""
    treatment: str
    surface: str
    colour: str
    wood: str

    def items(self) -> tuple[tuple[str, str], ...]:
        """Domain predicate names paired with their values."""
        return tuple(zip(PROPERTIES, (self.treatment, self.surface, self.colour, self.wood)))


@dataclass(frozen=True)
class Part:
    """A part's latent goal properties, projection and initial status."""
    name: str
    goal: Properties
    selection: frozenset[str]
    initial: Properties | None
    size: int

    def initial_facts(self) -> tuple[Atom | Assignment, ...]:
        """Attributes, status and size-dependent numeric costs."""
        status = "unused" if self.initial is None else "available"
        facts: list[Atom | Assignment] = [atom(status, self.name)]
        if self.initial is not None:
            facts.extend(atom(prop, self.name, value) for prop, value in self.initial.items())
        facts.append(atom("goalsize", self.name, ("small", "medium", "large")[self.size - 1]))
        facts.extend(Assignment(atom(function, self.name), multiplier * self.size + extra)
                     for function, multiplier, extra in (("spray-varnish-cost", 5, 0),
                                                        ("glaze-cost", 5, 5),
                                                        ("grind-cost", 15, 0), ("plane-cost", 10, 0)))
        return tuple(facts)

    def goal_facts(self) -> tuple[Atom, ...]:
        """Project selected properties, always requiring availability."""
        return (atom("available", self.name),
                *(atom(prop, self.name, value) for prop, value in sorted(self.goal.items())
                  if prop in self.selection))


@dataclass(frozen=True)
class Board:
    """One available board of a fixed wood, capacity and surface."""
    wood: str
    size: int
    surface: str

    def facts(self, name: str) -> tuple[Atom, ...]:
        """Initial board attributes."""
        return (atom("boardsize", name, f"s{self.size}"), atom("wood", name, self.wood),
                atom("surface-condition", name, self.surface), atom("available", name))


@dataclass(frozen=True)
class Machine:
    """One machine and its installed colours."""
    name: str
    kind: str
    colours: frozenset[str]

    def facts(self) -> tuple[Atom, ...]:
        """Initial machine state."""
        facts = [atom("has-colour", self.name, colour) for colour in sorted(self.colours)]
        if self.kind == "highspeed-saw":
            facts.insert(0, atom("empty", self.name))
        return tuple(facts)


@dataclass(frozen=True)
class Workshop:
    """Construction state before semantic PDDL projection."""
    colours: tuple[str, ...]
    woods: tuple[str, ...]
    parts: tuple[Part, ...]
    boards: tuple[Board, ...]
    machines: tuple[Machine, ...]

    @property
    def maximum_size(self) -> int:
        """Largest board size, or zero when all parts already exist."""
        return max((board.size for board in self.boards), default=0)
