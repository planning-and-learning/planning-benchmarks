"""Balanced, reproducible learning splits with explicit proposal provenance."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, fields, is_dataclass
import hashlib
from importlib.metadata import version
import inspect
import json
from pathlib import Path
import platform
import random
import shutil
import tempfile
from typing import Generic, Literal, TypeVar

from pypddl_datasets import __version__
from .runtime import (DISTRIBUTION_REVISION, GenerationExhausted, Problem, RandomSource, Rejected,
                      render_problem, semantic_fingerprint)

P = TypeVar("P")
V = TypeVar("V")
Scalar = str | int | float | bool | None
Split = Literal["train", "valid", "test"]
SPLITS: tuple[Split, ...] = ("train", "valid", "test")


@dataclass(frozen=True)
class SplitRecipe(Generic[P]):
    """The finite parameter spaces and successful-instance quotas of a domain."""

    domain: str
    domain_path: Path
    spaces: Mapping[Split, Sequence[P]]
    counts: Mapping[Split, int]


@dataclass(frozen=True)
class SplitOptions:
    """Controls whose values are recorded in every output manifest."""

    output_root: Path
    master_seed: int = 0
    max_attempts: int = 10_000


@dataclass(frozen=True)
class InstanceRequest(Generic[P]):
    """A fixed structural request; retries never replace its parameters."""

    parameters: P
    split: Split
    index: int


def parameter_values(parameters: object) -> dict[str, Scalar]:
    """Expose scalar dataclass parameters without leaking dynamic typing."""
    if not is_dataclass(parameters) or isinstance(parameters, type):
        raise TypeError("split parameters must be a dataclass instance")
    result: dict[str, Scalar] = {}
    for field in fields(parameters):
        value: object = getattr(parameters, field.name)
        if value is not None and not isinstance(value, (str, int, float, bool)):
            raise TypeError(f"unsupported parameter value for {field.name}")
        result[field.name] = value
    return result


def valid_configurations(factory: Callable[[V], P], candidates: Iterable[V]) -> list[P]:
    """Filter invalid structural combinations before assigning sample quotas."""
    result: list[P] = []
    for candidate in candidates:
        try:
            result.append(factory(candidate))
        except ValueError:
            continue
    if not result:
        raise ValueError("the structural parameter space contains no valid configurations")
    return result


def make_recipe(
    module_file: str,
    spaces: Mapping[Split, Sequence[P]],
    counts: Mapping[Split, int] | None = None,
) -> SplitRecipe[P]:
    """Resolve a domain's conventional files and validate its split declarations."""
    directory = Path(module_file).resolve().parent
    assert_pairwise_disjoint(spaces)
    return SplitRecipe(directory.name, directory / "domain.pddl", spaces,
                       counts if counts is not None else {split: 100 for split in SPLITS})


def derive_seed(master_seed: int, *parts: str | int) -> int:
    """Stable streams, independent of process hash randomization and call order."""
    payload = json.dumps([master_seed, *parts], separators=(",", ":")).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def balanced_schedule(
    configurations: Sequence[P], count: int, seed: int
) -> list[P]:
    """Randomly order complete cycles and choose an unbiased partial last cycle."""
    if not configurations or count < 0:
        raise ValueError("need a nonempty parameter space and a nonnegative count")
    schedule: list[P] = []
    cycle_index = 0
    while len(schedule) < count:
        cycle = list(configurations)
        random.Random(derive_seed(seed, "cycle", cycle_index)).shuffle(cycle)
        schedule.extend(cycle[:count - len(schedule)])
        cycle_index += 1
    return schedule


def assert_pairwise_disjoint(spaces: Mapping[Split, Sequence[object]]) -> None:
    """Compare semantic parameters, including probabilities, across split spaces."""
    seen: dict[str, Split] = {}
    for split, configurations in spaces.items():
        for config in configurations:
            identity = json.dumps(parameter_values(config), sort_keys=True)
            previous = seen.setdefault(identity, split)
            if previous != split:
                raise ValueError(f"parameters occur in both {previous} and {split}: {identity}")


def _generate_request(
    sample: Callable[[P, RandomSource], Problem | Rejected],
    request: InstanceRequest[P],
    recipe: SplitRecipe[P],
    options: SplitOptions,
) -> tuple[Problem, int, dict[str, int]]:
    rejections: dict[str, int] = {}
    for attempt in range(options.max_attempts):
        seed = derive_seed(options.master_seed, recipe.domain, request.split,
                           "attempt", request.index, attempt)
        # Budget exhaustion is operational failure, not a request to redraw a
        # partially sampled hierarchy or choose different parameters.
        problem = sample(request.parameters, random.Random(seed))
        if isinstance(problem, Problem):
            return problem, seed, rejections
        rejections[problem.reason] = rejections.get(problem.reason, 0) + 1
    raise GenerationExhausted(
        f"{recipe.domain}/{request.split}-{request.index}: "
        f"rejected {options.max_attempts} attempts for {parameter_values(request.parameters)}"
    )


def _sampler_provenance(
    sample: Callable[[P, RandomSource], Problem | Rejected], recipe: SplitRecipe[P],
) -> dict[str, object]:
    """Distinguish the sampling implementation from its mathematical distribution."""
    result: dict[str, object] = {"entry_point": f"{sample.__module__}.{sample.__qualname__}"}
    source = inspect.getsourcefile(sample)
    if source is not None:
        result["source_sha256"] = hashlib.sha256(Path(source).read_bytes()).hexdigest()
    model = recipe.domain_path.with_name("distribution.pl")
    if model.exists():
        root = Path(__file__).parent
        resources = [root / "probabilistic.py",
                     *sorted((root / "_problog").glob("*.py")),
                     *sorted((root / "_problog").glob("*.pl"))]
        result.update({
            "model_sha256": hashlib.sha256(model.read_bytes()).hexdigest(),
            "problog_version": version("problog"),
            "backend_sha256": {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in resources},
        })
    return result


def _write_split(  # pylint: disable=too-many-arguments
    recipe: SplitRecipe[P],
    split: Split,
    sample: Callable[[P, RandomSource], Problem | Rejected],
    options: SplitOptions,
    directory: Path,
) -> None:
    directory.mkdir()
    shutil.copyfile(recipe.domain_path, directory / "domain.pddl")
    schedule = balanced_schedule(
        recipe.spaces[split], recipe.counts[split],
        derive_seed(options.master_seed, recipe.domain, split, "schedule"),
    )
    records: list[dict[str, object]] = []
    for index, parameters in enumerate(schedule, start=1):
        problem, seed, rejections = _generate_request(sample, InstanceRequest(parameters, split, index), recipe, options)
        content = render_problem(problem).encode("utf-8")
        filename = f"{split}-{index}.pddl"
        (directory / filename).write_bytes(content)
        records.append({
            "file": filename, "parameters": parameter_values(parameters),
            "seed": seed, "rejected_attempts": sum(rejections.values()),
            "rejection_reasons": rejections,
            "attempt_seeds": [derive_seed(options.master_seed, recipe.domain, split, "attempt", index, attempt)
                              for attempt in range(sum(rejections.values()) + 1)],
            "semantic_sha256": semantic_fingerprint(problem),
            "sha256": hashlib.sha256(content).hexdigest(),
        })
    manifest = {
        "schema_version": 1, "generator": f"classical/{recipe.domain}",
        "distribution_revision": DISTRIBUTION_REVISION, "split": split,
        "master_seed": options.master_seed, "python": platform.python_version(),
        "package_version": __version__, "sampler": _sampler_provenance(sample, recipe),
        "domain_sha256": hashlib.sha256(recipe.domain_path.read_bytes()).hexdigest(),
        "parameter_policy": "balanced-shuffled-cycles", "max_attempts": options.max_attempts,
        "valid_configurations": len(recipe.spaces[split]), "instances": records,
    }
    (directory / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def generate_splits(
    recipe: SplitRecipe[P],
    sample: Callable[[P, RandomSource], Problem | Rejected],
    options: SplitOptions,
) -> list[Path]:
    """Stage all outputs before replacing a domain's managed split files."""
    if options.max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    assert_pairwise_disjoint(recipe.spaces)
    options.output_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".generation-", dir=options.output_root) as temporary:
        staging = Path(temporary)
        for split in SPLITS:
            _write_split(recipe, split, sample, options, staging / split)
        paths: list[Path] = []
        for split in SPLITS:
            target = options.output_root / f"{recipe.domain}-{split}"
            target.mkdir(exist_ok=True)
            for old in target.glob(f"{split}-*.pddl"):
                old.unlink()
            for new in (staging / split).iterdir():
                shutil.copyfile(new, target / new.name)
            paths.append(target)
    return paths


def split_main(
    recipe: SplitRecipe[P],
    sample: Callable[[P, RandomSource], Problem | Rejected],
    argv: Sequence[str] | None = None,
) -> int:
    """Common CLI used by the historical per-domain module entry points."""
    parser = argparse.ArgumentParser(description=f"Generate {recipe.domain} learning splits.")
    default_root = Path(__file__).resolve().parents[3] / "data" / "classical" / "generated"
    parser.add_argument("--output-root", type=Path, default=default_root)
    parser.add_argument("--master-seed", type=int, default=0)
    parser.add_argument("--max-attempts", type=int, default=10_000)
    args = parser.parse_args(argv)
    generate_splits(recipe, sample, SplitOptions(args.output_root, args.master_seed, args.max_attempts))
    return 0
