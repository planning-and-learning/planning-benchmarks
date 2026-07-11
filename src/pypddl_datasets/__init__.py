"""Download and cache the planning-benchmarks PDDL suites.

Data is not shipped with this package: the first fetch downloads the pinned
data release (one archive) and unpacks it into the local cache; every later
call reuses that extraction. Override the cache location with the
PYPDDL_DATASETS_CACHE environment variable, or point PYPDDL_DATASETS_DATA at
a local checkout's data/ directory to use it directly (no download).
"""

from __future__ import annotations

import functools
import os
import re
import shutil
from pathlib import Path

import pooch

from .suites import SUITES

__version__ = "0.0.1"

# The pinned data release: updated when a new data-v* release is cut
# (its workflow prints the archive's sha256). Empty sha256 = development
# build without a pinned release; only PYPDDL_DATASETS_DATA works then.
DATA_VERSION = "data-v0.0.1"
DATA_SHA256 = "0df3275480778699e8f8d9dcedc9e0384b0cc1e9a235c87fa3794c2376fd9f16"

_ARCHIVE = "data.tar.gz"  # single asset on the data release

_CACHE = Path(os.environ.get("PYPDDL_DATASETS_CACHE", pooch.os_cache("pypddl-datasets"))) / DATA_VERSION

_POOCH = pooch.create(
    path=_CACHE,
    base_url=f"https://github.com/planning-and-learning/planning-benchmarks/releases/download/{DATA_VERSION}/",
    registry={_ARCHIVE: f"sha256:{DATA_SHA256}"},
)


class Task:
    """A single planning task of a domain: display names (domain, problem),
    the domain directory it belongs to, its domain file, and its problem
    file."""

    def __init__(self, domain: str, problem: str, path: Path, domain_path: Path, task_path: Path) -> None:
        self._domain = domain
        self._problem = problem
        self._path = path
        self._domain_path = domain_path
        self._task_path = task_path

    @property
    def domain(self) -> str:
        return self._domain

    @property
    def problem(self) -> str:
        return self._problem

    @property
    def path(self) -> Path:
        return self._path

    @property
    def domain_path(self) -> Path:
        return self._domain_path

    @property
    def task_path(self) -> Path:
        return self._task_path

    def __repr__(self) -> str:
        return f"Task(domain={self._domain!r}, problem={self._problem!r})"


class Domain:
    """A benchmark domain: its directory and all of its tasks, each paired
    with the correct domain file (which is per-instance in some collections,
    e.g. airport)."""

    def __init__(self, path: Path, tasks: list[Task]) -> None:
        self._path = path
        self._tasks = tasks

    @property
    def path(self) -> Path:
        return self._path

    @property
    def tasks(self) -> list[Task]:
        return self._tasks

    def __repr__(self) -> str:
        return f"Domain(path={self._path!r}, tasks={self._tasks!r})"


class Suite:
    """A named benchmark suite: the root directory its domains live under
    and the fetched domains themselves."""

    def __init__(self, path: Path, domains: list[Domain]) -> None:
        self._path = path
        self._domains = domains

    @property
    def path(self) -> Path:
        return self._path

    @property
    def domains(self) -> list[Domain]:
        return self._domains

    def __repr__(self) -> str:
        return f"Suite(path={self._path!r}, domains={self._domains!r})"


def list_suites() -> list[str]:
    """Names accepted by fetch_suite()."""
    return sorted(SUITES)


def list_domains() -> list[str]:
    """Domain names accepted by fetch_domain() and fetch_task(); triggers the
    one-time data download when no local data is configured. A domain is a
    maximal directory containing .pddl files directly."""
    root = _data_root()
    domains: list[str] = []

    def walk(directory: Path) -> None:
        if any(child.suffix == ".pddl" for child in directory.iterdir() if child.is_file()):
            domains.append(directory.relative_to(root).as_posix())
            return
        for child in directory.iterdir():
            if child.is_dir():
                walk(child)

    walk(root)
    return sorted(domains)


def fetch_domain(name: str) -> Domain:
    """Fetch a domain such as "classical/downward-benchmarks/gripper",
    downloading it if necessary."""
    directory = _fetch_directory(name)
    return Domain(directory, _pair_tasks(name, directory))


def fetch_task(name: str) -> Task:
    """Fetch one task by its full name, e.g.
    fetch_task("classical/tests/gripper/test-1.pddl"). The split between
    domain and task file is unambiguous because domains are never nested."""
    domain, task = _split_task_name(name)
    directory = _fetch_directory(domain)
    for candidate in _pair_tasks(domain, directory):
        if task in (candidate.problem, candidate.task_path.name):
            return candidate
    raise KeyError(f"no task {task!r} in domain {domain!r}")


def fetch_suite(suite: str) -> Suite:
    """Fetch all entries of a named suite; see list_suites(). A plain domain
    entry yields the whole domain; a "<domain>:<instance>" entry (as used by
    the "-test" suites) yields a Domain restricted to that single task."""
    if suite not in SUITES:
        raise KeyError(f"unknown suite {suite!r}; see list_suites()")
    domains = []
    for entry in SUITES[suite]:
        name, _, instance = entry.partition(":")
        if instance:
            task = fetch_task(f"{name}/{instance}")
            domains.append(Domain(task.path, [task]))
        else:
            domains.append(fetch_domain(name))
    return Suite(_data_root(), domains)


def export_suite(suite: str, dest: str | Path) -> list[Path]:
    """Copy all domains of a named suite into dest/<domain path>/, for tools
    that expect benchmark files in a fixed directory tree."""
    if suite not in SUITES:
        raise KeyError(f"unknown suite {suite!r}; see list_suites()")
    paths = []
    for entry in SUITES[suite]:
        name = entry.partition(":")[0]
        target = Path(dest) / name
        shutil.copytree(_fetch_directory(name), target, dirs_exist_ok=True)
        paths.append(target)
    return paths


def _data_root() -> Path:
    """The root directory the data lives under, downloading and unpacking the
    pinned data release once if necessary.

    If PYPDDL_DATASETS_DATA is set (e.g. to a local checkout's data/ dir on
    machines without internet access), it is used directly instead."""
    local_root = os.environ.get("PYPDDL_DATASETS_DATA")
    if local_root:
        return Path(local_root)
    return _fetched_data_root()


@functools.cache
def _fetched_data_root() -> Path:
    """Download and unpack the pinned data release; once per machine on disk,
    and the (re-)verification of the cached archive once per process."""
    if not DATA_SHA256:
        raise KeyError(
            "this pypddl-datasets build has no pinned data release (development "
            "build); set PYPDDL_DATASETS_DATA to a local checkout's data/ "
            "directory or install a released version"
        )
    _POOCH.fetch(_ARCHIVE, processor=pooch.Untar(extract_dir="data"))
    return _CACHE / "data"


def _split_task_name(name: str) -> tuple[str, str]:
    """Split "classical/tests/gripper/test-1.pddl" into domain and task part.
    Unique because domain directories are maximal (never nested)."""
    root = _data_root()
    parts = name.split("/")
    for index in range(1, len(parts)):
        domain = "/".join(parts[:index])
        directory = root / domain
        if directory.is_dir() and any(directory.glob("*.pddl")):
            return domain, "/".join(parts[index:])
    raise KeyError(f"no domain found in task name {name!r}; see list_domains()")


def _fetch_directory(name: str) -> Path:
    """The local directory of a domain, downloading the data if necessary."""
    path = _data_root() / name
    if not path.is_dir() or not any(path.glob("*.pddl")):
        raise KeyError(f"unknown domain {name!r}; see list_domains()")
    return path


# Domain/problem pairing, following the same rules as the repository's validate.py.

_DECLARATION = re.compile(r"\(\s*define\s*\(\s*(domain|problem)\s+([^\s()]+)", re.IGNORECASE)
_DOMAIN_REFERENCE = re.compile(r"\(\s*:domain\s+([^\s()]+)", re.IGNORECASE)
_HEAD_BYTES = 65536
_LFS_POINTER_PREFIX = "version https://git-lfs.github.com/spec/v1"


def _declaration(path: Path) -> tuple[str, str | None] | None:
    """("domain"|"problem", declared name), classified by file content."""
    with path.open("r", encoding="utf-8", errors="replace") as stream:
        head = stream.read(_HEAD_BYTES)
        if head.startswith(_LFS_POINTER_PREFIX):
            # LFS pointer stub (checkout without `git lfs pull`): classify by
            # file name so pairing matches a full checkout.
            return ("domain" if "domain" in path.name else "problem", None)
        text = re.sub(r";[^\n]*", "", head)
        match = _DECLARATION.search(text)
        if match is None and stream.read(1):
            text = re.sub(r";[^\n]*", "", text + stream.read())
            match = _DECLARATION.search(text)
    return (match.group(1).lower(), match.group(2)) if match else None


def _pair_tasks(domain: str, directory: Path) -> list[Task]:
    domain_files: dict[Path, str] = {}
    problem_files: list[Path] = []
    for path in sorted(directory.rglob("*.pddl")):
        declared = _declaration(path)
        if declared is None:
            continue
        kind, name = declared
        if kind == "domain":
            domain_files[path] = name.lower() if name else ""
        else:
            problem_files.append(path)
    return [
        Task(
            domain,
            problem.relative_to(directory).as_posix(),
            directory,
            _resolve_domain(problem, domain_files, directory),
            problem,
        )
        for problem in problem_files
    ]


def _resolve_domain(problem: Path, domain_files: dict[Path, str], root: Path) -> Path:
    stem = problem.stem
    candidates = (
        "domain.pddl",
        f"{stem}-domain{problem.suffix}",
        f"{stem[:3]}-domain.pddl",
        f"domain_{problem.name}",
        f"domain-{problem.name}",
    )
    directory = problem.parent
    while True:
        for candidate in candidates:
            if directory / candidate in domain_files:
                return directory / candidate
        if directory == root:
            break
        directory = directory.parent
    if len(domain_files) == 1:
        return next(iter(domain_files))
    reference = _DOMAIN_REFERENCE.search(problem.read_text(encoding="utf-8", errors="replace"))
    if reference:
        matches = [path for path, name in domain_files.items() if name == reference.group(1).lower()]
        if len(matches) == 1:
            return matches[0]
    raise ValueError(f"cannot resolve domain file for {problem}")
