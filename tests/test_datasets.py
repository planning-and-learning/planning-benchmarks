import importlib
import shutil
import subprocess
import sys
from pathlib import Path

import pooch
import pytest

import pypddl_datasets
from pypddl_datasets.suites import SUITES

from conftest import REPO_ROOT
from package_data import archive_name, discover_domains

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


def test_archive_names_round_trip():
    for domain in discover_domains(DATA_ROOT):
        name = archive_name(domain, DATA_ROOT)
        relative = domain.relative_to(DATA_ROOT).as_posix()
        assert name[: -len(".tar.gz")].replace("--", "/") == relative
        assert "--" not in relative, f"'--' in {relative} breaks the / <-> -- mapping"


GENERATOR_DOMAINS = sorted(
    p.parent.name
    for p in (REPO_ROOT / "src/pypddl_datasets/generators/classical").glob("*/generate_instances.py")
)


@pytest.mark.parametrize("domain", GENERATOR_DOMAINS)
def test_split_configs_importable_and_disjoint(domain):
    # module import runs the assert_pairwise_disjoint checks on train/valid/test configs
    importlib.import_module(f"pypddl_datasets.generators.classical.{domain}.generate_instances")


def test_regenerated_instance_matches_committed_data():
    module = importlib.import_module("pypddl_datasets.generators.classical.childsnack.generate_instances")
    committed = (DATA_ROOT / "classical/generated/childsnack-train/train-1.pddl").read_text(encoding="utf-8")
    num_children, num_trays, gluten_factor, const_ratio, seed = module.CONFIGS["train"][0]
    assert module.make_problem(num_children, num_trays, gluten_factor, const_ratio, seed) == committed


def test_package_and_fetch_round_trip(tmp_path):
    assets = tmp_path / "assets"
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts/package_data.py"),
         "--only", "classical/tests/gripper", "--output", str(assets)],
        check=True,
    )

    downloads = pooch.create(path=tmp_path / "cache", base_url="https://example.invalid/", registry=None)
    downloads.load_registry(assets / "registry.txt")
    stem = "classical--tests--gripper"
    downloads.fetch(
        stem + ".tar.gz",
        processor=pooch.Untar(extract_dir=stem),
        downloader=lambda url, output, _: shutil.copy(assets / Path(url).name, output),
    )

    fetched = Path(downloads.abspath) / stem
    original = DATA_ROOT / "classical/tests/gripper"
    assert {f.name for f in fetched.iterdir()} == {f.name for f in original.iterdir()}
    for f in original.iterdir():
        assert (fetched / f.name).read_bytes() == f.read_bytes()


def test_fetch_domain_rejects_unknown_name():
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_domain("classical/no-such-collection/no-such-domain")
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_suite("no-such-suite")


@pytest.fixture
def local_data(monkeypatch):
    monkeypatch.setenv("PYPDDL_DATASETS_DATA", str(DATA_ROOT))


def test_fetch_domain_local_data_override(local_data):
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
def test_task_pairing(local_data, domain, task, expected_domain_file):
    fetched = pypddl_datasets.fetch_task(f"{domain}/{task}")
    assert fetched.path == DATA_ROOT / domain
    assert fetched.task_path == DATA_ROOT / domain / task
    assert fetched.domain_path.name == expected_domain_file
    assert fetched.domain_path.is_file()


def test_fetch_task_accepts_bare_name_and_rejects_unknown(local_data):
    by_bare_name = pypddl_datasets.fetch_task("numeric/ipc2026/2048/pfile10.pddl")
    assert by_bare_name.task_path.name == "pfile10.pddl"
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_task("classical/tests/gripper/no-such-task.pddl")
    with pytest.raises(KeyError):
        pypddl_datasets.fetch_task("classical/no-such-domain/task.pddl")


def test_fetch_suite_test_entries_are_single_task_domains(local_data):
    suite = pypddl_datasets.fetch_suite("pushworld-test")
    assert suite.path == DATA_ROOT
    assert len(suite.domains) == len(SUITES["pushworld-test"])
    for fetched in suite.domains:
        assert len(fetched.tasks) == 1
        assert fetched.tasks[0].domain_path.is_file()
        assert fetched.tasks[0].task_path.is_file()


def test_task_display_names(local_data):
    tasks = [t for d in pypddl_datasets.fetch_suite("htg-test").domains for t in d.tasks]
    assert len(tasks) == len(SUITES["htg-test"])
    labyrinth = next(t for t in tasks if t.domain == "classical/htg-domains/labyrinth")
    assert labyrinth.problem == labyrinth.task_path.name
    nested = pypddl_datasets.fetch_task("numeric/ipc2026/2048/pfile10.pddl")
    assert nested.domain == "numeric/ipc2026/2048"
    assert nested.problem == "instances/pfile10.pddl"


def test_export_suite_materializes_tree(local_data, tmp_path):
    exported = pypddl_datasets.export_suite("tests-classical", tmp_path)
    assert (tmp_path / "classical/tests/gripper/domain.pddl").is_file()
    assert len(exported) == len(SUITES["tests-classical"])
