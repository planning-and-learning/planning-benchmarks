"""Every generator's domain files and generated tasks parse strictly with pypddl.

Sample arguments come from tests/generator_samples.json: real calls recorded from
the generator tests (regenerate with tests/record_generator_samples.py). Re-export
and wrapper packages replay the samples of the module they delegate to.
"""

import functools
import importlib
import inspect
import json
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import pytest
from pypddl.formalism import Parser, ParserOptions

GENERATORS = Path(__file__).resolve().parents[1] / "src/pypddl_datasets/generators"
SAMPLES_FILE = Path(__file__).with_name("generator_samples.json")
SAMPLES = cast("dict[str, list[dict[str, Any]]]", json.loads(SAMPLES_FILE.read_text(encoding="utf-8")))
PACKAGES = sorted(
    p.relative_to(GENERATORS).as_posix()
    for p in [*GENERATORS.glob("classical/*/*"), *GENERATORS.glob("numeric/*/*")]
    if (p / "generator.py").is_file()
)
DOMAIN_NAME = re.compile(r"\(\s*define\s*\(\s*domain\s+([^\s()]+)", re.IGNORECASE)
PROBLEM_DOMAIN = re.compile(r"\(\s*:domain\s+([^\s()]+)", re.IGNORECASE)


def _options() -> ParserOptions:
    options = ParserOptions()
    options.strict = True
    return options


def _generator(package: str) -> tuple[Callable[..., str], str, dict[str, Any]]:
    """The package's make_problem, the sample key it replays, and its fixed keywords."""
    module = importlib.import_module(f"pypddl_datasets.generators.{package.replace('/', '.')}.generator")
    fn = cast("Callable[..., str]", module.make_problem)
    fixed: dict[str, Any] = {}
    target: Any = fn
    if isinstance(target, functools.partial):
        partial = cast("functools.partial[object]", target)
        fixed = dict(partial.keywords)
        target = partial.func
    implementation = cast("str", target.__module__)
    key = implementation.removeprefix("pypddl_datasets.generators.").removesuffix(".generator").replace(".", "/")
    return fn, key, fixed


def _domain_name(text: str) -> str:
    match = DOMAIN_NAME.search(re.sub(r";[^\n]*", "", text))
    assert match, "no (define (domain ...)) found"
    return match.group(1).lower()


@pytest.mark.parametrize("package", PACKAGES)
def test_domain_files_and_generated_tasks_parse(package: str, tmp_path: Path) -> None:
    assert (GENERATORS / package / "domain.pddl").is_file(), f"{package}: no fixed domain.pddl"
    domains = sorted((GENERATORS / package).glob("domain*.pddl"))
    for domain in domains:
        Parser(domain, _options())  # the domain file alone must parse strictly
    by_name: dict[str, list[Path]] = {}
    for domain in domains:
        by_name.setdefault(_domain_name(domain.read_text(encoding="utf-8")), []).append(domain)

    fn, key, fixed = _generator(package)
    defaults = {
        name: parameter.default
        for name, parameter in inspect.signature(fn).parameters.items()
        if parameter.default is not inspect.Parameter.empty
    }
    samples = SAMPLES.get(key, [])
    assert samples, f"no recorded samples for {key}; regenerate tests/generator_samples.json"
    used: set[Path] = set()
    parsed = 0
    for index, sample in enumerate(samples):
        kwargs = {name: value for name, value in sample.items() if name not in fixed}
        # a sample that sets an encoding/style flag away from this package's default may target
        # another package's domain (e.g. typed=True -> autoscale); that package replays it instead
        flagged = any(
            isinstance(value, (bool, str)) and name in defaults and value != defaults[name]
            for name, value in kwargs.items()
        )
        try:
            problem_text = fn(**kwargs)
        except ValueError:
            if fixed:  # the wrapper's fixed flags rule this sample out (e.g. hex levels in style="learning")
                continue
            raise
        match = PROBLEM_DOMAIN.search(problem_text)
        assert match, f"sample {sample} has no (:domain ...)"
        candidates = by_name.get(match.group(1).lower(), [])
        if not candidates:
            continue
        problem_path = tmp_path / f"p{index}.pddl"
        problem_path.write_text(problem_text, encoding="utf-8")
        errors: list[str] = []
        successes = 0
        for domain_path in candidates:
            try:
                Parser(domain_path, _options()).parse_task(problem_path)
            except Exception as error:  # pylint: disable=broad-exception-caught  # recorded, then judged below
                errors.append(f"{domain_path.name}: {error}")
            else:
                used.add(domain_path)
                successes += 1
        if successes:
            parsed += 1
        elif not flagged:
            pytest.fail(f"{package} sample {sample} does not parse: {errors}")
    assert parsed, f"{package}: no sample targets one of its domain files"
    assert used >= set(domains), f"{package}: no sample uses {sorted(p.name for p in set(domains) - used)}"
