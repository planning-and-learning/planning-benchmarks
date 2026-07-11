"""Download and cache the planning-benchmarks PDDL suites.

Data is not shipped with this package; each domain is downloaded on first use
from the matching GitHub release and cached locally (override the cache
location with the PYPDDL_DATASETS_CACHE environment variable).
"""

from __future__ import annotations

import os
import re
import shutil
from importlib import resources
from pathlib import Path
from typing import NamedTuple

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


class Task:
    """A single planning task of a domain: the domain directory it belongs
    to, its domain file, and its problem file."""

    def __init__(self, path: Path, domain_path: Path, task_path: Path) -> None:
        self._path = path
        self._domain_path = domain_path
        self._task_path = task_path

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
        return f"Task(path={self._path!r}, domain_path={self._domain_path!r}, task_path={self._task_path!r})"


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


class LabTask(NamedTuple):
    """The attributes a downward-lab experiment reads off a task
    (lab itself is not a dependency)."""

    domain: str
    problem: str
    domain_file: Path
    problem_file: Path


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

    def lab(self) -> list[LabTask]:
        """This suite as a flat list of tasks the way a downward-lab
        experiment consumes them. Domain display names follow the suite
        entry layout, e.g. "classical/htg-domains/labyrinth"."""
        return [
            LabTask(
                domain=domain.path.relative_to(self._path).as_posix().replace("--", "/"),
                problem=task.task_path.relative_to(domain.path).as_posix(),
                domain_file=task.domain_path,
                problem_file=task.task_path,
            )
            for domain in self._domains
            for task in domain.tasks
        ]

    def __repr__(self) -> str:
        return f"Suite(path={self._path!r}, domains={self._domains!r})"


def list_suites() -> list[str]:
    """Names accepted by fetch_suite()."""
    return sorted(SUITES)


def list_domains() -> list[str]:
    """Domain names accepted by fetch_domain() and fetch_task()."""
    return sorted(name[: -len(_ARCHIVE_SUFFIX)].replace("--", "/") for name in _POOCH.registry)


def fetch_domain(name: str) -> Domain:
    """Fetch a domain such as "classical/downward-benchmarks/gripper",
    downloading it if necessary."""
    directory = _fetch_directory(name)
    return Domain(directory, _pair_tasks(directory))


def fetch_task(name: str) -> Task:
    """Fetch one task by its full name, e.g.
    fetch_task("classical/tests/gripper/test-1.pddl"). The split between
    domain and task file is unambiguous because domains are never nested."""
    domain, task = _split_task_name(name)
    directory = _fetch_directory(domain)
    for candidate in _pair_tasks(directory):
        relative = candidate.task_path.relative_to(directory).as_posix()
        if task in (relative, candidate.task_path.name):
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
    """The root directory fetched domains live under."""
    local_root = os.environ.get("PYPDDL_DATASETS_DATA")
    return Path(local_root) if local_root else Path(_POOCH.abspath)


def _split_task_name(name: str) -> tuple[str, str]:
    """Split "classical/tests/gripper/test-1.pddl" into domain and task part.
    Unique because domain directories are maximal (never nested)."""
    parts = name.split("/")
    local_root = os.environ.get("PYPDDL_DATASETS_DATA")
    for index in range(1, len(parts)):
        domain = "/".join(parts[:index])
        if local_root:
            directory = Path(local_root) / domain
            if directory.is_dir() and any(directory.glob("*.pddl")):
                return domain, "/".join(parts[index:])
        elif domain.replace("/", "--") + _ARCHIVE_SUFFIX in _POOCH.registry:
            return domain, "/".join(parts[index:])
    raise KeyError(f"no domain found in task name {name!r}; see list_domains()")


def _fetch_directory(name: str) -> Path:
    """The local directory of a domain, downloaded if necessary.

    If PYPDDL_DATASETS_DATA is set (e.g. to a local checkout's data/ dir on
    machines without internet access), domains are resolved there instead
    and nothing is downloaded."""
    local_root = os.environ.get("PYPDDL_DATASETS_DATA")
    if local_root:
        path = Path(local_root) / name
        if not path.is_dir():
            raise KeyError(f"domain {name!r} not found under PYPDDL_DATASETS_DATA={local_root}")
        return path
    stem = name.replace("/", "--")
    archive = stem + _ARCHIVE_SUFFIX
    if archive not in _POOCH.registry:
        raise KeyError(f"unknown domain {name!r}; see list_domains()")
    _POOCH.fetch(archive, processor=pooch.Untar(extract_dir=stem))
    return Path(_POOCH.abspath) / stem


# Domain/problem pairing, following the same rules as the repository's validate.py.

_DECLARATION = re.compile(r"\(\s*define\s*\(\s*(domain|problem)\s+([^\s()]+)", re.IGNORECASE)
_DOMAIN_REFERENCE = re.compile(r"\(\s*:domain\s+([^\s()]+)", re.IGNORECASE)
_HEAD_BYTES = 65536


def _declaration(path: Path) -> tuple[str, str] | None:
    """("domain"|"problem", declared name), classified by file content."""
    with path.open("r", encoding="utf-8", errors="replace") as stream:
        text = re.sub(r";[^\n]*", "", stream.read(_HEAD_BYTES))
        match = _DECLARATION.search(text)
        if match is None and stream.read(1):
            text = re.sub(r";[^\n]*", "", text + stream.read())
            match = _DECLARATION.search(text)
    return (match.group(1).lower(), match.group(2)) if match else None


def _pair_tasks(directory: Path) -> list[Task]:
    domain_files: dict[Path, str] = {}
    problem_files: list[Path] = []
    for path in sorted(directory.rglob("*.pddl")):
        declared = _declaration(path)
        if declared is None:
            continue
        kind, name = declared
        if kind == "domain":
            domain_files[path] = name.lower()
        else:
            problem_files.append(path)
    return [
        Task(directory, _resolve_domain(problem, domain_files, directory), problem)
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
