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
import json
import os
from collections.abc import Iterable
from pathlib import Path

from pypddl.formalism import Parser, ParserOptions

import pypddl_datasets
from pypddl_datasets.discovery import discover_domains
from pypddl_datasets.requirements import Requirement
from pypddl_datasets.suites import SUITES


Metadata = dict[str, list[str]] | dict[str, dict[str, list[str]]]


def generate(data_root: Path) -> dict[str, Metadata]:
    os.environ["PYPDDL_DATASETS_DATA"] = str(data_root)

    options = ParserOptions()
    options.add_action_costs = False

    def tokens(requirements: Iterable[object]) -> frozenset[str]:
        values = frozenset(str(requirement) for requirement in requirements)
        for value in values:
            # pypddl reports usage-based explicit requirements only; a composite
            # or unknown token leaking through is a pypddl bug and fails loudly.
            Requirement(value)
        return values

    def declared(task: pypddl_datasets.Task) -> frozenset[str]:
        """The requirements of `task`: its domain's and its own, read with a parser of its own that is freed on return.

        A parser keeps every task it parsed: kept across tasks (one cached per domain), every task of every family
        stayed alive (21 GB, beyond a CI runner's 16).
        """
        parser = Parser(task.domain_path, options)
        parsed = parser.parse_task(task.task_path)
        return tokens(parser.domain().get_requirements()) | tokens(parsed.get_requirements())

    tasks: dict[str, dict[str, list[str]]] = {}
    domains: dict[str, list[str]] = {}
    for domain_dir in discover_domains(data_root):
        name = domain_dir.relative_to(data_root).as_posix()
        by_problem: dict[str, list[str]] = {}
        for task in pypddl_datasets.fetch_domain(name).tasks:
            by_problem[task.problem] = sorted(declared(task))
        tasks[name] = dict(sorted(by_problem.items()))
        domains[name] = sorted(set[str]().union(*by_problem.values())) if by_problem else []

    suites: dict[str, list[str]] = {}
    for suite, entries in SUITES.items():
        suites[suite] = sorted(set[str]().union(*(domains[entry.partition(":")[0]] for entry in entries)))

    return {
        "requirements.tasks.json": tasks,
        "requirements.domains.json": domains,
        "requirements.suites.json": suites,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path.cwd() / "data")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)

    for filename, content in generate(args.data_root.resolve()).items():
        path = args.output_dir / filename
        path.write_text(json.dumps(content, indent=1, sort_keys=True) + "\n", encoding="utf-8")
        print(f"[extract-requirements] wrote {len(content)} entries to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
