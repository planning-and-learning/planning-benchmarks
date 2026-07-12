#!/usr/bin/env python3
"""Regenerate the committed requirement metadata from data/ using the pypddl
parser (repository tooling, not shipped with the package):

- requirements.tasks.json:   {domain: {task: [requirements]}}
  (a task's requirements = pypddl's view of its domain file plus its own)
- requirements.domains.json: {domain: [union over its tasks]}
- requirements.suites.json:  {suite: [union over its domains]}
"""

from __future__ import annotations

import argparse
import functools
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

import pypddl_datasets
from pypddl_datasets.discovery import discover_domains
from pypddl.formalism import Parser, ParserOptions
from pypddl_datasets.requirements import Requirement
from pypddl_datasets.suites import SUITES


def generate(data_root: Path) -> dict[str, dict]:
    os.environ["PYPDDL_DATASETS_DATA"] = str(data_root)

    options = ParserOptions()
    options.add_action_costs = False

    @functools.cache
    def domain_parser(domain_path: Path) -> Parser:
        return Parser(domain_path, options)

    def tokens(requirements) -> frozenset[str]:
        values = frozenset(str(requirement) for requirement in requirements)
        for value in values:
            # pypddl reports usage-based explicit requirements only; a composite
            # or unknown token leaking through is a pypddl bug and fails loudly.
            Requirement(value)
        return values

    tasks: dict[str, dict[str, list[str]]] = {}
    domains: dict[str, list[str]] = {}
    for domain_dir in discover_domains(data_root):
        name = domain_dir.relative_to(data_root).as_posix()
        by_problem = {}
        for task in pypddl_datasets.fetch_domain(name).tasks:
            parser = domain_parser(task.domain_path)
            parsed = parser.parse_task(task.task_path)
            declared = tokens(parser.domain().get_requirements()) | tokens(parsed.get_requirements())
            by_problem[task.problem] = sorted(declared)
        tasks[name] = dict(sorted(by_problem.items()))
        domains[name] = sorted(set().union(*map(set, by_problem.values()))) if by_problem else []

    suites: dict[str, list[str]] = {}
    for suite, entries in SUITES.items():
        suites[suite] = sorted(set().union(*(set(domains[entry.partition(":")[0]]) for entry in entries)))

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
