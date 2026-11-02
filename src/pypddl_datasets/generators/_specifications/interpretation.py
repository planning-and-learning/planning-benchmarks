"""Solver-independent semantic identities for distribution interpretations."""
from dataclasses import dataclass

Value = bool | int


@dataclass(frozen=True, order=True)
class SemanticKey:
    """An object declaration, ground atom, or initialized numeric fluent."""
    group: str
    kind: str
    predicate: str
    arguments: tuple[str, ...] = ()


@dataclass(frozen=True)
class Situation:
    """A canonical interpretation; labels matter, serialization order does not."""
    values: tuple[tuple[SemanticKey, Value], ...]

    @property
    def identity(self) -> frozenset[tuple[SemanticKey, Value]]:
        """Hashable identity excluding all auxiliary witnesses."""
        return frozenset(self.values)

    def project(self, group: str) -> "Situation":
        """Select initial or goal variables without changing labels."""
        return Situation(tuple((key, value) for key, value in self.values if key.group == group))
