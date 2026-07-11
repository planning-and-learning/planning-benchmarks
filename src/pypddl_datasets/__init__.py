"""Download and cache the planning-benchmarks PDDL suites.

Data is not shipped with this package; each domain is downloaded on first use
from the matching GitHub release and cached locally (override the cache
location with the PYPDDL_DATASETS_CACHE environment variable).
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path

import pooch

from .suites import SUITES

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
    """Return the local paths of all entries of a named suite, downloading
    them if necessary; see list_suites(). A plain domain entry resolves to
    the fetched directory; a "<domain>:<instance>" entry (as used by the
    "-test" suites) resolves to that problem file within it."""
    if suite not in SUITES:
        raise KeyError(f"unknown suite {suite!r}; see list_suites()")
    paths = []
    for entry in SUITES[suite]:
        domain, _, instance = entry.partition(":")
        directory = fetch_domain(domain)
        paths.append(directory / instance if instance else directory)
    return paths
