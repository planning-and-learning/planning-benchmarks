#!/usr/bin/env python3
"""Regenerate src/pypddl_datasets/requirements.json from data/.

Per domain: the union of the requirements declared by all of its files, its
task inventory, and per-task overrides where a task's requirements (its own
declarations plus its specific domain file's) differ from the domain union.
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


def generate(data_root: Path) -> dict:
    os.environ["PYPDDL_DATASETS_DATA"] = str(data_root)
    sys.path.insert(0, str(ROOT / "src"))
    import pypddl_datasets
    from pypddl_datasets.requirements import Requirement

    from package_data import discover_domains

    @functools.cache
    def declared(path: Path) -> frozenset[str]:
        text = re.sub(r";[^\n]*", "", path.read_text(encoding="utf-8", errors="replace")[:_HEAD_BYTES])
        tokens = {token.lower() for match in _REQUIREMENTS.finditer(text) for token in match.group(1).split()}
        for token in tokens:
            Requirement(token)  # unknown tokens fail generation loudly
        return frozenset(tokens)

    entries: dict[str, dict] = {}
    for domain_dir in discover_domains(data_root):
        name = domain_dir.relative_to(data_root).as_posix()
        tasks = pypddl_datasets.fetch_domain(name).tasks
        by_problem = {
            task.problem: (declared(task.domain_path) | declared(task.task_path)) or frozenset({":strips"})
            for task in tasks
        }
        union = sorted(set().union(*by_problem.values())) if by_problem else [":strips"]
        entry: dict = {"requirements": union, "problems": sorted(by_problem)}
        overrides = {
            problem: sorted(requirements)
            for problem, requirements in by_problem.items()
            if requirements != set(union)
        }
        if overrides:
            entry["tasks"] = dict(sorted(overrides.items()))
        entries[name] = entry
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=ROOT / "data")
    parser.add_argument("--output", type=Path, default=ROOT / "src/pypddl_datasets/requirements.json")
    args = parser.parse_args()

    entries = generate(args.data_root.resolve())
    args.output.write_text(json.dumps(entries, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"[extract-requirements] wrote {len(entries)} domains to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
