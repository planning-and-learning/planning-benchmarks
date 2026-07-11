import importlib
import shutil
import subprocess
import sys
from pathlib import Path

import pooch
import pytest

import pypddl_datasets
from pypddl_datasets.suites import SUITES, TEST_INSTANCES

from conftest import REPO_ROOT
from package_data import archive_name, discover_domains

DATA_ROOT = REPO_ROOT / "data"


def test_suite_entries_are_domain_dirs():
    domains = {d.relative_to(DATA_ROOT).as_posix() for d in discover_domains(DATA_ROOT)}
    for suite, entries in SUITES.items():
        assert entries, suite
        for entry in entries:
            assert entry in domains, f"{suite}: {entry} is not a packagable domain dir"


def test_archive_names_round_trip():
    for domain in discover_domains(DATA_ROOT):
        name = archive_name(domain, DATA_ROOT)
        relative = domain.relative_to(DATA_ROOT).as_posix()
        assert name[: -len(".tar.gz")].replace("--", "/") == relative
        assert "--" not in relative, f"'--' in {relative} breaks the / <-> -- mapping"


@pytest.mark.parametrize("suite", sorted(TEST_INSTANCES))
def test_test_instances_exist(suite):
    assert suite in SUITES
    entries = TEST_INSTANCES[suite]
    assert entries, suite
    for item in entries:
        domain, instance = item.split(":", 1)
        assert domain in SUITES[suite], f"{suite}: {domain} not in suite"
        assert (DATA_ROOT / domain / instance).is_file(), f"{domain}/{instance}"


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
