"""Independent graph-law checks and finite dataset-selection guarantees."""

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import random
from typing import cast

import pytest
from typing_extensions import override

from pypddl_datasets.generators.runtime import (
    GenerationExhausted, Problem, RandomSource, Rejected, atom, connected_edges,
    objects, render_problem,
)
from pypddl_datasets.generators.splits import (
    SPLITS, SplitOptions, SplitRecipe, assert_pairwise_disjoint, balanced_schedule,
    derive_seed, generate_splits, valid_configurations,
)


class Decisions(random.Random):
    """Replay the primitive Bernoulli decisions of one graph proposal."""

    def __init__(self, decisions: tuple[int, ...]) -> None:
        super().__init__(0)
        self.decisions = iter(decisions)

    @override
    def random(self) -> float:
        return 0.0 if next(self.decisions) else 0.999999


def _connected_by_cuts(size: int, edges: set[tuple[int, int]]) -> bool:
    """Independent finite oracle: every nontrivial cut must have a crossing."""
    for count in range(1, size):
        for subset in combinations(range(size), count):
            if not any((a in subset) != (b in subset) for a, b in edges):
                return False
    return True


@pytest.mark.parametrize("probability", [Fraction(1, 2), Fraction(1, 3)])
def test_connected_graph_support_and_exact_proposal_weights(probability: Fraction) -> None:
    universe = tuple(combinations(range(4), 2))
    weights: dict[frozenset[tuple[int, int]], Fraction] = {}
    for decisions in product((0, 1), repeat=len(universe)):
        expected = {edge for edge, include in zip(universe, decisions) if include}
        source = Decisions(decisions)
        if not _connected_by_cuts(4, expected):
            with pytest.raises(GenerationExhausted):
                connected_edges(4, source, float(probability), max_attempts=1)
            continue
        actual = connected_edges(4, source, float(probability), max_attempts=1)
        assert actual == expected
        edges = len(actual)
        weights[frozenset(actual)] = probability ** edges * (1 - probability) ** (6 - edges)
    assert len(weights) == 38
    assert frozenset({(0, 1), (0, 2), (0, 3)}) in weights
    assert frozenset(universe) in weights
    if probability == Fraction(1, 2):
        total = sum(weights.values(), Fraction())
        assert {weight / total for weight in weights.values()} == {Fraction(1, 38)}


def test_graph_boundaries_and_allowed_universe() -> None:
    assert connected_edges(1, random.Random(0), 0) == set()
    allowed = {(0, 1), (1, 2)}
    assert connected_edges(3, random.Random(0), 1, allowed_edges=allowed) == allowed
    for probability in (0.0, -0.1, 1.1, float("nan"), float("inf")):
        with pytest.raises(ValueError):
            connected_edges(3, random.Random(0), probability)
    with pytest.raises(ValueError, match="cannot form a connected graph"):
        connected_edges(3, random.Random(0), allowed_edges={(0, 1)})


@pytest.mark.parametrize("count", [2, 7, 20])
def test_balanced_cycles_and_prefix_coverage(count: int) -> None:
    configurations = tuple(range(7))
    first = balanced_schedule(configurations, count, 0)
    assert first == balanced_schedule(configurations, count, 0)
    frequencies = Counter(first)
    assert len(first) == count
    assert all(count // 7 <= frequencies[value] <= (count + 6) // 7 for value in configurations)
    if count < 7:
        observed = {value for seed in range(32) for value in balanced_schedule(configurations, count, seed)}
        assert observed == set(configurations)


def test_stable_independent_seed_streams() -> None:
    assert derive_seed(0, "grid", "train", 1) == derive_seed(0, "grid", "train", 1)
    streams = {derive_seed(0, domain, split, attempt)
               for domain in ("grid", "ferry") for split in SPLITS for attempt in range(10)}
    assert len(streams) == 60


@dataclass(frozen=True)
class ToyParameters:
    """A tiny generator whose structural support is independently transparent."""

    size: int

    def __post_init__(self) -> None:
        if self.size < 1:
            raise ValueError("size must be positive")


def _toy(parameters: ToyParameters, _rng: RandomSource) -> Problem:
    names = tuple(f"o{i}" for i in range(parameters.size))
    return Problem("toy", "toy", objects(names),
                   tuple(atom("ready", name) for name in names), (atom("ready", names[0]),))


def _recipe(root: Path) -> SplitRecipe[ToyParameters]:
    domain = root / "domain.pddl"
    domain.write_text("(define (domain toy) (:requirements :strips) (:predicates (ready ?x)))\n")
    return SplitRecipe("toy", domain,
                       {split: [ToyParameters(index + 1)] for index, split in enumerate(SPLITS)},
                       {split: 2 for split in SPLITS})


def test_rejected_samples_keep_their_configuration_and_manifest(tmp_path: Path) -> None:
    recipe = _recipe(tmp_path)
    visits: Counter[int] = Counter()

    def rejecting(parameters: ToyParameters, rng: RandomSource) -> Problem | Rejected:
        visits[parameters.size] += 1
        return Rejected("first proposal") if visits[parameters.size] == 1 else _toy(parameters, rng)

    paths = generate_splits(recipe, rejecting, SplitOptions(tmp_path / "generated"))
    assert visits == {1: 3, 2: 3, 3: 3}
    for directory in paths:
        manifest = cast("dict[str, object]", json.loads((directory / "manifest.json").read_text()))
        provenance = cast("dict[str, object]", manifest["sampler"])
        assert provenance["entry_point"] == f"{rejecting.__module__}.{rejecting.__qualname__}"
        assert provenance["source_sha256"] == hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        instances = cast("list[dict[str, object]]", manifest["instances"])
        assert instances[0]["rejection_reasons"] == {"first proposal": 1}
        assert instances[1]["rejected_attempts"] == 0


def test_generation_is_reproducible_and_failure_preserves_existing_data(tmp_path: Path) -> None:
    recipe = _recipe(tmp_path)
    options = SplitOptions(tmp_path / "generated", max_attempts=2)
    generate_splits(recipe, _toy, options)
    before = {path.relative_to(options.output_root): path.read_bytes()
              for path in options.output_root.rglob("*") if path.is_file()}
    generate_splits(recipe, _toy, options)
    assert before == {path.relative_to(options.output_root): path.read_bytes()
                      for path in options.output_root.rglob("*") if path.is_file()}
    with pytest.raises(GenerationExhausted):
        generate_splits(recipe, lambda _parameters, _rng: Rejected("never"), options)
    assert before == {path.relative_to(options.output_root): path.read_bytes()
                      for path in options.output_root.rglob("*") if path.is_file()}


def test_parameter_spaces_exclude_invalid_requests_and_overlap() -> None:
    assert valid_configurations(ToyParameters, [-1, 0, 1]) == [ToyParameters(1)]
    with pytest.raises(ValueError, match="no valid configurations"):
        valid_configurations(ToyParameters, [-1, 0])
    with pytest.raises(ValueError, match="both"):
        assert_pairwise_disjoint({"train": [ToyParameters(1)], "test": [ToyParameters(1)]})


def test_renderer_rejects_duplicate_objects() -> None:
    problem = Problem("bad", "toy", objects(["x", "x"]), (), ())
    with pytest.raises(ValueError, match="duplicate object"):
        render_problem(problem)


def test_probabilistic_split_records_model_and_backend_provenance(tmp_path: Path) -> None:
    from pypddl_datasets.generators.classical.ferry import generator

    root = Path(generator.__file__).parent
    recipe = SplitRecipe("ferry", root / "domain.pddl",
                         {split: [generator.Parameters(index, 1)] for index, split in enumerate(SPLITS)},
                         {split: 1 for split in SPLITS})
    paths = generate_splits(recipe, generator.sample, SplitOptions(tmp_path / "generated"))
    manifest = cast("dict[str, object]", json.loads((paths[0] / "manifest.json").read_text()))
    provenance = cast("dict[str, object]", manifest["sampler"])
    assert provenance["problog_version"] == "2.3.0"
    assert provenance["model_sha256"] == hashlib.sha256((root / "distribution.pl").read_bytes()).hexdigest()
    resources = cast("dict[str, str]", provenance["backend_sha256"])
    assert "probabilistic.py" in resources and "_problog/library.pl" in resources
    assert all(value == hashlib.sha256((root.parents[1] / path).read_bytes()).hexdigest()
               for path, value in resources.items())
