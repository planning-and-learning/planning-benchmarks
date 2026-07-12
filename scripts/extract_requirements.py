#!/usr/bin/env python3
"""Regenerate the committed requirement metadata from data/:

- requirements.tasks.json:   {domain: {task: [declared requirements]}}
  (a task's requirements = its own declarations plus its domain file's)
- requirements.domains.json: {domain: [union of declared requirements]}
- requirements.suites.json:  {suite: {"union": [...], "intersection": [...]}}
  over the EXPANDED domain requirements, so find_suites answers both filter
  directions with one subset test each.
"""

from __future__ import annotations

import argparse
import functools
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_REQUIREMENTS = re.compile(r"\(\s*:requirements([^)]*)\)", re.IGNORECASE)
_HEAD_BYTES = 262144  # declarations live in the define header


def generate(data_root: Path) -> dict[str, dict]:
    os.environ["PYPDDL_DATASETS_DATA"] = str(data_root)
    sys.path.insert(0, str(ROOT / "src"))
    import pypddl_datasets
    from pypddl_datasets.requirements import Requirement, _expand
    from pypddl_datasets.suites import SUITES

    from package_data import discover_domains

    @functools.cache
    def declared(path: Path) -> frozenset[str]:
        text = re.sub(r";[^\n]*", "", path.read_text(encoding="utf-8", errors="replace")[:_HEAD_BYTES])
        tokens = {token.lower() for match in _REQUIREMENTS.finditer(text) for token in match.group(1).split()}
        for token in tokens:
            Requirement(token)  # unknown tokens fail generation loudly
        return frozenset(tokens)

    tasks: dict[str, dict[str, list[str]]] = {}
    domains: dict[str, list[str]] = {}
    for domain_dir in discover_domains(data_root):
        name = domain_dir.relative_to(data_root).as_posix()
        by_problem = {
            task.problem: sorted((declared(task.domain_path) | declared(task.task_path)) or {":strips"})
            for task in pypddl_datasets.fetch_domain(name).tasks
        }
        tasks[name] = dict(sorted(by_problem.items()))
        domains[name] = sorted(set().union(*map(set, by_problem.values()))) if by_problem else [":strips"]

    suites: dict[str, dict[str, list[str]]] = {}
    for suite, entries in SUITES.items():
        expanded = [_expand(domains[entry.partition(":")[0]]) for entry in entries]
        suites[suite] = {
            "union": sorted(frozenset().union(*expanded)),
            "intersection": sorted(frozenset.intersection(*expanded)),
        }

    return {
        "requirements.tasks.json": tasks,
        "requirements.domains.json": domains,
        "requirements.suites.json": suites,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=ROOT / "data")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "src/pypddl_datasets")
    args = parser.parse_args()

    for filename, content in generate(args.data_root.resolve()).items():
        path = args.output_dir / filename
        path.write_text(json.dumps(content, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print(f"[extract-requirements] wrote {len(content)} entries to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
