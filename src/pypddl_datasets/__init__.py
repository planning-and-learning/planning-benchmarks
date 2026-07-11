"""Download and cache the planning-benchmarks PDDL suites.

Data is not shipped with this package; each domain is downloaded on first use
from the matching GitHub release and cached locally (override the cache
location with the PYPDDL_DATASETS_CACHE environment variable).
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

import pooch

from .suites import SUITES, TEST_INSTANCES

__version__ = "0.1.0"

_ARCHIVE_SUFFIX = ".tar.gz"

_POOCH = pooch.create(
    path=pooch.os_cache("pypddl-datasets"),
    base_url="https://github.com/planning-and-learning/planning-benchmarks/releases/download/v{version}/",
    version=__version__,
    registry=None,
    env="PYPDDL_DATASETS_CACHE",
)
with resources.as_file(resources.files(__package__) / "registry.txt") as _registry:
    _POOCH.load_registry(_registry)


def list_suites() -> list[str]:
    """Names accepted by fetch_suite()."""
    return sorted(SUITES)


def list_domains() -> list[str]:
    """Domain names accepted by fetch_domain()."""
    return sorted(name[: -len(_ARCHIVE_SUFFIX)].replace("--", "/") for name in _POOCH.registry)


def fetch_domain(name: str) -> Path:
    """Return the local directory of a domain such as
    "classical/downward-benchmarks/gripper", downloading it if necessary."""
    stem = name.replace("/", "--")
    archive = stem + _ARCHIVE_SUFFIX
    if archive not in _POOCH.registry:
        raise KeyError(f"unknown domain {name!r}; see list_domains()")
    _POOCH.fetch(archive, processor=pooch.Untar(extract_dir=stem))
    return Path(_POOCH.abspath) / stem


def fetch_suite(suite: str) -> list[Path]:
    """Return the local directories of all domains in a named suite,
    downloading them if necessary; see list_suites()."""
    if suite not in SUITES:
        raise KeyError(f"unknown suite {suite!r}; see list_suites()")
    return [fetch_domain(name) for name in SUITES[suite]]


def fetch_test_suite(suite: str) -> list[Path]:
    """Return one representative problem file per domain of a named suite,
    for quick planner smoke runs. The domain files sit in the returned
    paths' parent directories."""
    if suite not in TEST_INSTANCES:
        raise KeyError(f"no test instances for suite {suite!r}; available: {sorted(TEST_INSTANCES)}")
    paths = []
    for entry in TEST_INSTANCES[suite]:
        domain, instance = entry.split(":", 1)
        paths.append(fetch_domain(domain) / instance)
    return paths
