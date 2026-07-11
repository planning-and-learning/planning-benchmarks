import importlib
import shutil
import subprocess
import sys
from pathlib import Path

import pooch
import pytest

import pypddl_datasets
from pypddl_datasets import suites
from pypddl_datasets.suites import SUITES

import _smoke_instances_classical
import _smoke_instances_numeric
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


# Old suite_test.py smoke lists: one representative instance per domain,
# resolved by directory basename within the matching suite.
SMOKE_LISTS = {
    "SUITE_CNOT_SYNTHESIS": _smoke_instances_classical.SUITE_CNOT_SYNTHESIS_TEST,
    "SUITE_IPC_OPTIMAL_STRIPS": _smoke_instances_classical.SUITE_IPC_OPTIMAL_STRIPS_TEST,
    "SUITE_IPC_OPTIMAL_ADL": _smoke_instances_classical.SUITE_IPC_OPTIMAL_ADL_TEST,
    "SUITE_IPC_SATISFICING_STRIPS": _smoke_instances_classical.SUITE_IPC_SATISFICING_STRIPS_TEST,
    "SUITE_IPC_SATISFICING_ADL": _smoke_instances_classical.SUITE_IPC_SATISFICING_ADL_TEST,
    "SUITE_IPC2023_LEARNING": _smoke_instances_classical.SUITE_IPC_LEARNING_TEST,
    "SUITE_AUTOSCALE_OPTIMAL_STRIPS": _smoke_instances_classical.SUITE_AUTOSCALE_OPTIMAL_STRIPS_TEST,
    "SUITE_AUTOSCALE_AGILE_STRIPS": _smoke_instances_classical.SUITE_AUTOSCALE_AGILE_STRIPS_TEST,
    "SUITE_HTG": _smoke_instances_classical.SUITE_HTG_TEST,
    "SUITE_PUSHWORLD": _smoke_instances_classical.SUITE_PUSHWORLD_TEST,
    "SUITE_BELUGA2025_SCALABILITY_DETERMINISTIC": _smoke_instances_classical.SUITE_BELUGA2025_SCALABILITY_DETERMINISTIC_TEST,
    "SUITE_MINEPDDL_CLASSICAL": _smoke_instances_classical.SUITE_MINEPDDL_TEST,
    "SUITE_IPC2023_NUMERIC": _smoke_instances_numeric.SUITE_IPC2023_NUMERIC_TEST,
    "SUITE_MINEPDDL_NUMERIC": _smoke_instances_numeric.SUITE_MINEPDDL_TEST,
}


@pytest.mark.parametrize("suite_const", sorted(SMOKE_LISTS))
def test_smoke_instances_exist(suite_const):
    entries = getattr(suites, suite_const)
    by_basename = {entry.rsplit("/", 1)[-1]: entry for entry in entries}
    for item in SMOKE_LISTS[suite_const]:
        domain, instance = item.split(":", 1)
        assert domain in by_basename, f"{suite_const}: no suite entry named {domain}"
        assert (DATA_ROOT / by_basename[domain] / instance).is_file(), f"{by_basename[domain]}/{instance}"


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
