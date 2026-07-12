import importlib
import importlib.util
import json
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path
from typing import cast

import pooch
import pytest

import pypddl_datasets
from pypddl_datasets.discovery import discover_domains
from pypddl_datasets.suites import SUITES

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "data"


def test_suite_entries_resolve():
    domains = {d.relative_to(DATA_ROOT).as_posix() for d in discover_domains(DATA_ROOT)}
    for suite, entries in SUITES.items():
        assert entries, suite
        for entry in entries:
            domain, _, instance = entry.partition(":")
            assert domain in domains, f"{suite}: {domain} is not a packagable domain dir"
            if instance:
                assert (DATA_ROOT / domain / instance).is_file(), f"{suite}: {entry}"


def test_test_suites_select_from_their_base_suite():
    # "generated-test" is the held-out split suite, not a fragment suite; it has no base.
    for suite in SUITES:
        base = SUITES.get(suite.removesuffix("-test"))
        if suite.endswith("-test") and base is not None:
            for entry in SUITES[suite]:
                assert entry.partition(":")[0] in set(base), f"{suite}: {entry}"


GENERATOR_DOMAINS = sorted(
    p.parent.name
    for p in (REPO_ROOT / "src/pypddl_datasets/generators/classical").glob("*/generate_instances.py")
)


@pytest.mark.parametrize("domain", GENERATOR_DOMAINS)
def test_split_configs_importable_and_disjoint(domain: str) -> None:
    # module import runs the assert_pairwise_disjoint checks on train/valid/test configs
    importlib.import_module(f"pypddl_datasets.generators.classical.{domain}.generate_instances")


def test_regenerated_instance_matches_committed_data():
    module = importlib.import_module("pypddl_datasets.generators.classical.childsnack.generate_instances")
    committed = (DATA_ROOT / "classical/generated/childsnack-train/train-1.pddl").read_text(encoding="utf-8")
    num_children, num_trays, gluten_factor, const_ratio, seed = module.CONFIGS["train"][0]
    assert module.make_problem(num_children, num_trays, gluten_factor, const_ratio, seed) == committed


def _package(data_root: Path, archive: Path) -> str:
    """Run package_data.py and return the printed sha256."""
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts/package_data.py"),
         "--data-root", str(data_root), "--output", str(archive)],
        check=True, capture_output=True, text=True,
    )
    return result.stdout.rsplit("sha256:", 1)[1].strip()


def test_package_and_fetch_round_trip(tmp_path: Path) -> None:
    archive = tmp_path / "assets" / "data.tar.gz"
    sha = _package(DATA_ROOT / "classical" / "tests", archive)
    # byte-reproducible: repackaging yields the identical hash
    assert _package(DATA_ROOT / "classical" / "tests", tmp_path / "again.tar.gz") == sha

    downloads = pooch.create(
        path=tmp_path / "cache",
        base_url="https://example.invalid/",
        registry={"data.tar.gz": f"sha256:{sha}"},
    )
    downloads.fetch(
        "data.tar.gz",
        processor=pooch.Untar(extract_dir="data"),
        downloader=lambda url, output, _: shutil.copy(archive, output),
    )

    fetched = tmp_path / "cache" / "data" / "gripper"
    original = DATA_ROOT / "classical/tests/gripper"
    assert {f.name for f in fetched.iterdir()} == {f.name for f in original.iterdir()}
    for f in original.iterdir():
        assert (fetched / f.name).read_bytes() == f.read_bytes()


@pytest.fixture
def local_data(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PYPDDL_DATASETS_DATA", str(DATA_ROOT))


def test_fetch_domain_rejects_unknown_name(local_data: None):
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_domain("classical/no-such-collection/no-such-domain")
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_suite("no-such-suite")


def test_fetch_domain_local_data_override(local_data: None):
    domain = pypddl_datasets.fetch_domain("classical/tests/gripper")
    assert domain.path == DATA_ROOT / "classical/tests/gripper"
    assert [t.task_path.name for t in domain.tasks] == ["test-1.pddl"]
    assert domain.tasks[0].domain_path == domain.path / "domain.pddl"
    assert domain.tasks[0].path == domain.path
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_domain("classical/tests/no-such-domain")


@pytest.mark.parametrize(
    ("domain", "task", "expected_domain_file"),
    [
        # shared domain.pddl
        ("classical/tests/gripper", "test-1.pddl", "domain.pddl"),
        # per-instance domain files, three naming conventions
        ("classical/downward-benchmarks/airport", "p01-airport1-p1.pddl", "p01-domain.pddl"),
        ("classical/downward-benchmarks/openstacks-strips", "p01.pddl", "domain_p01.pddl"),
        ("classical/htg-domains/genome-edit-distance", "d-1-2-original.pddl", "d-1-2-original-domain.pddl"),
        # tasks in an instances/ subdir, domain file at the domain root
        ("numeric/ipc2026/2048", "instances/pfile10.pddl", "domain.pddl"),
    ],
)
def test_task_pairing(local_data: None, domain: str, task: str, expected_domain_file: str) -> None:
    fetched = pypddl_datasets.fetch_task(f"{domain}/{task}")
    assert fetched.path == DATA_ROOT / domain
    assert fetched.task_path == DATA_ROOT / domain / task
    assert fetched.domain_path.name == expected_domain_file
    assert fetched.domain_path.is_file()


def test_fetch_task_accepts_bare_name_and_rejects_unknown(local_data: None):
    by_bare_name = pypddl_datasets.fetch_task("numeric/ipc2026/2048/pfile10.pddl")
    assert by_bare_name.task_path.name == "pfile10.pddl"
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_task("classical/tests/gripper/no-such-task.pddl")
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_task("classical/no-such-domain/task.pddl")


def test_fetch_suite_test_entries_are_single_task_domains(local_data: None):
    suite = pypddl_datasets.fetch_suite("pushworld-test")
    assert suite.path == DATA_ROOT
    assert len(suite.domains) == len(SUITES["pushworld-test"])
    for fetched in suite.domains:
        assert len(fetched.tasks) == 1
        assert fetched.tasks[0].domain_path.is_file()
        assert fetched.tasks[0].task_path.is_file()


def test_task_display_names(local_data: None):
    tasks = [t for d in pypddl_datasets.fetch_suite("htg-test").domains for t in d.tasks]
    assert len(tasks) == len(SUITES["htg-test"])
    labyrinth = next(t for t in tasks if t.domain == "classical-htg-domains-labyrinth")
    assert labyrinth.problem == labyrinth.task_path.name
    nested = pypddl_datasets.fetch_task("numeric/ipc2026/2048/pfile10.pddl")
    assert nested.domain == "numeric-ipc2026-2048"
    assert nested.problem == "instances/pfile10.pddl"


def test_task_domain_is_lab_safe_and_unique():
    # "/" would break lab run dirs/report keys; flattening with "-" must
    # remain collision-free across all domains.
    names = pypddl_datasets.list_domains()
    flattened = {name.replace("/", "-") for name in names}
    assert len(flattened) == len(names)
    assert all("/" not in flat for flat in flattened)


def test_export_suite_materializes_tree(local_data: None, tmp_path: Path):
    exported = pypddl_datasets.export_suite("tests-classical", tmp_path)
    assert (tmp_path / "classical/tests/gripper/domain.pddl").is_file()
    assert len(exported) == len(SUITES["tests-classical"])


def test_requirement_queries():
    R = pypddl_datasets.Requirement
    assert pypddl_datasets.domain_requirements("classical/tests/gripper") == {R.STRIPS}
    # the data is strict-clean: declarations are atomic and exact (no :adl anywhere)
    assert R.CONDITIONAL_EFFECTS in pypddl_datasets.domain_requirements("classical/downward-benchmarks/miconic-fulladl")

    # supported: capability ceiling over explicit requirements
    supported = [R.STRIPS, R.TYPING, R.NEGATIVE_PRECONDITIONS, R.DISJUNCTIVE_PRECONDITIONS,
                 R.EQUALITY, R.EXISTENTIAL_PRECONDITIONS, R.UNIVERSAL_PRECONDITIONS, R.CONDITIONAL_EFFECTS]
    assert "classical/downward-benchmarks/miconic-fulladl" in pypddl_datasets.find_domains(supported=supported)
    strips_only = pypddl_datasets.find_domains(supported=[R.STRIPS])
    assert "classical/tests/gripper" in strips_only
    assert "classical/downward-benchmarks/miconic-fulladl" not in strips_only

    # requires: feature floor
    assert "classical/downward-benchmarks/miconic-fulladl" in pypddl_datasets.find_domains(
        requires=[R.CONDITIONAL_EFFECTS])

    # suite scoping and find_suites
    scoped = pypddl_datasets.find_domains(suite="ipc-satisficing-adl", supported=supported)
    assert set(scoped) <= {e.partition(":")[0] for e in SUITES["ipc-satisficing-adl"]}
    assert "tests-classical" not in pypddl_datasets.find_suites(supported=[R.STRIPS])
    assert "cnot-synthesis" in pypddl_datasets.find_suites(requires=[R.TYPING])

    # strings are coerced; typos raise instead of silently filtering
    assert pypddl_datasets.find_domains(supported=[":strips"]) == strips_only
    with pytest.raises(ValueError):
        pypddl_datasets.find_domains(supported=[":stripss"])


def test_task_requirements():
    R = pypddl_datasets.Requirement
    assert pypddl_datasets.task_requirements("classical/tests/gripper/test-1.pddl") == {R.STRIPS}
    # per-task precision: the positional GED encoding needs conditional effects, original does not
    assert R.CONDITIONAL_EFFECTS in pypddl_datasets.task_requirements(
        "classical/htg-domains/genome-edit-distance/d-1-2-positional.pddl")
    assert R.CONDITIONAL_EFFECTS not in pypddl_datasets.task_requirements(
        "classical/htg-domains/genome-edit-distance/d-1-2-original.pddl")
    # bare-name lookup for nested layouts, KeyError on unknown
    assert pypddl_datasets.task_requirements("numeric/ipc2026/2048/pfile10.pddl")
    with pytest.raises(KeyError):
        pypddl_datasets.task_requirements("classical/tests/gripper/no-such.pddl")


def test_composites_resolve_to_explicit_requirements():
    # CompositeRequirements documents the aggregates; each must map to explicit
    # Requirements, and none may ever appear in the (strict-clean) metadata.
    from pypddl_datasets import COMPOSITE_TO_REQUIREMENTS, CompositeRequirements, Requirement

    for composite in CompositeRequirements:
        atoms = COMPOSITE_TO_REQUIREMENTS[composite]
        assert atoms and all(isinstance(atom, Requirement) for atom in atoms)

    composite_tokens = {c.value for c in CompositeRequirements}
    for filename in ("requirements.tasks.json", "requirements.domains.json", "requirements.suites.json"):
        text = (REPO_ROOT / "src/pypddl_datasets" / filename).read_text()
        assert not any(f'"{token}"' in text for token in composite_tokens), filename


def test_find_tasks_and_per_task_overrides():
    R = pypddl_datasets.Requirement
    # genome-edit-distance mixes encodings: only the positional tasks declare :adl
    tasks = pypddl_datasets.find_tasks(
        supported=[R.STRIPS, R.TYPING, R.EQUALITY, R.NEGATIVE_PRECONDITIONS, R.ACTION_COSTS])
    ged = [t for t in tasks if "genome-edit-distance" in t]
    assert ged and all("positional" not in t for t in ged)
    # suite-scoped -test entries yield one task per domain
    smoke = pypddl_datasets.find_tasks(suite="pushworld-test")
    assert len(smoke) == len(SUITES["pushworld-test"])


def test_fetch_suite_filters(local_data: None):
    R = pypddl_datasets.Requirement
    full = pypddl_datasets.fetch_suite("htg-test")
    strips_typed = pypddl_datasets.fetch_suite("htg-test", supported=[R.STRIPS, R.TYPING, R.ACTION_COSTS])
    assert 0 < len(strips_typed.domains) < len(full.domains)
    nothing = pypddl_datasets.fetch_suite("htg-test", requires=[R.DURATIVE_ACTIONS])
    assert nothing.domains == []


def test_requirements_metadata_is_fresh() -> None:
    pointer_probe = DATA_ROOT / "classical/pushworld/level1/Pulling.pddl"
    if pointer_probe.read_bytes().startswith(b"version https://git-lfs"):
        pytest.skip("LFS content not available; extraction would differ")
    pytest.importorskip("pypddl")

    # scripts/ is repo tooling, not an importable package: load by path
    spec = importlib.util.spec_from_file_location("extract_requirements", REPO_ROOT / "scripts" / "extract_requirements.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    generate = cast("Callable[[Path], dict[str, object]]", module.generate)

    for filename, generated in generate(DATA_ROOT).items():
        committed = cast("object", json.loads((REPO_ROOT / "src/pypddl_datasets" / filename).read_text()))
        assert generated == committed, f"{filename} is stale; regenerate with scripts/extract_requirements.py"


def test_pairing_tolerates_lfs_pointer_stubs(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    # A checkout without `git lfs pull` has pointer stubs instead of PDDL;
    # pairing must classify them by file name (as CI runners do).
    domain_dir = tmp_path / "classical" / "stub-domain"
    domain_dir.mkdir(parents=True)
    pointer = "version https://git-lfs.github.com/spec/v1\noid sha256:abc\nsize 1\n"
    (domain_dir / "domain_p28.pddl").write_text(pointer)
    (domain_dir / "p28.pddl").write_text("(define (problem p28) (:domain openstacks))")
    (domain_dir / "p29.pddl").write_text(pointer)
    monkeypatch.setenv("PYPDDL_DATASETS_DATA", str(tmp_path))
    domain = pypddl_datasets.fetch_domain("classical/stub-domain")
    by_problem = {t.problem: t for t in domain.tasks}
    assert by_problem["p28.pddl"].domain_path.name == "domain_p28.pddl"
    assert "p29.pddl" in by_problem
