"""Download and cache the planning-benchmarks PDDL suites.

Data is not shipped with this package: the first fetch downloads the pinned
data release (one archive) and unpacks it into the local cache; every later
call reuses that extraction. Override the cache location with the
PYPDDL_DATASETS_CACHE environment variable, or point PYPDDL_DATASETS_DATA at
a local checkout's data/ directory to use it directly (no download).
"""

from .fetching import (
    DATA_SHA256,
    DATA_VERSION,
    Domain,
    Suite,
    Task,
    export_suite,
    fetch_domain,
    fetch_suite,
    fetch_task,
    list_domains,
    list_suites,
)
from .requirements import (
    COMPOSITE_TO_REQUIREMENTS,
    CompositeRequirements,
    Requirement,
    Requirements,
    domain_requirements,
    find_domains,
    find_suites,
    find_tasks,
    task_requirements,
)

__all__ = [
    "COMPOSITE_TO_REQUIREMENTS",
    "DATA_SHA256",
    "DATA_VERSION",
    "CompositeRequirements",
    "Domain",
    "Requirement",
    "Requirements",
    "Suite",
    "Task",
    "domain_requirements",
    "export_suite",
    "fetch_domain",
    "fetch_suite",
    "fetch_task",
    "find_domains",
    "find_suites",
    "find_tasks",
    "list_domains",
    "list_suites",
    "task_requirements",
]

__version__ = "0.0.4"
