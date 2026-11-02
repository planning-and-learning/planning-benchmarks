"""Common situation construction for the two Hiking relation encodings."""

from __future__ import annotations

from pypddl_datasets.generators.runtime import Atom, Problem, RandomSource, atom, objects


def _couple_initial(index: int, rng: RandomSource, binary: bool) -> tuple[Atom, ...]:
    couple, guy, girl = f"couple{index}", f"guy{index}", f"girl{index}"
    partners = ((atom("partner_of", couple, guy), atom("partner_of", couple, girl))
                if binary else (atom("partners", couple, guy, girl),))
    return partners + (
        atom("at_person", guy, "place0"), atom("at_person", girl, "place0"),
        atom("walked", couple, "place0"), atom("at_tent", f"tent{index}", "place0"),
        atom("up" if rng.randint(1, 2) == 2 else "down", f"tent{index}"),
    )


def hiking_problem(
    num_couples: int, num_cars: int, num_places: int, rng: RandomSource, *, binary: bool,
) -> Problem:
    """Build the fixed chain and indexed partners with random initial tent states."""
    cars = [f"car{i}" for i in range(num_cars)]
    couples = [f"couple{i}" for i in range(num_couples)]
    universe = objects(cars, "car") + objects(couples, "couple")
    universe += objects((f"tent{i}" for i in range(num_couples)), "tent")
    universe += objects((f"place{i}" for i in range(num_places)), "place")
    universe += objects((person for i in range(num_couples)
                         for person in (f"guy{i}", f"girl{i}")), "person")
    initial = tuple(fact for i in range(num_couples) for fact in _couple_initial(i, rng, binary))
    initial += tuple(atom("at_car", car, "place0") for car in cars)
    initial += tuple(atom("next", f"place{i}", f"place{i + 1}") for i in range(num_places - 1))
    domain = "hiking-binary" if binary else "hiking"
    return Problem(
        f"{domain}-{num_couples}-{num_cars}-{num_places}", domain, universe, initial,
        tuple(atom("walked", couple, f"place{num_places - 1}") for couple in couples),
    )
