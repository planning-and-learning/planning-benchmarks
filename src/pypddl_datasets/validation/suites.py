#!/usr/bin/env python3
"""Check that the shipped suite definitions (pypddl_datasets.suites.SUITES)
are consistent with the data tree: every entry resolves to a domain directory
(and instance file, for "<domain>:<instance>" entries), "-test" suites select
only from their base suite, the SUITE_* definitions and the SUITES mapping
are alphabetically sorted, and
every benchmark suite has a "-test" smoke
companion (fixture, split, and profiling suites are exempt). The companion is
a one-instance-per-domain miniature so experiments can dry-run their whole
pipeline by swapping the suite name before committing to the full run."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypddl_datasets import suites as suite_definitions
from pypddl_datasets.discovery import discover_domains
from pypddl_datasets.suites import SUITES

# tests-* are the smoke suites themselves; generated-{train,valid,test} are
# learning splits; profiling-* feed the C++ profiling harnesses.
EXEMPT_PREFIXES = ("tests-", "generated-", "profiling-")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd() / "data")
    args = parser.parse_args(argv)
    root: Path = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")

    domains = {d.relative_to(root).as_posix() for d in discover_domains(root)}
    errors: list[str] = []
    for name, expected in zip(SUITES, sorted(SUITES)):
        if name != expected:
            errors.append(f"{name}: SUITES is not alphabetically sorted ({expected} belongs here)")
            break
    definitions = [name for name in vars(suite_definitions) if name.startswith("SUITE_")]
    for name, expected in zip(definitions, sorted(definitions)):
        if name != expected:
            errors.append(f"{name}: SUITE_* definitions are not alphabetically sorted ({expected} belongs here)")
            break
    for suite, entries in SUITES.items():
        if not entries:
            errors.append(f"{suite}: empty suite")
        base = SUITES.get(suite.removesuffix("-test")) if suite.endswith("-test") else None
        base_domains = {entry.partition(":")[0] for entry in base} if base is not None else None
        for entry in entries:
            domain, _, instance = entry.partition(":")
            if domain not in domains:
                errors.append(f"{suite}: {domain} is not a domain directory")
            elif instance and not (root / domain / instance).is_file():
                errors.append(f"{suite}: {entry} does not exist")
            if base_domains is not None and domain not in base_domains:
                errors.append(f"{suite}: {domain} is not part of {suite.removesuffix('-test')}")
        if not suite.endswith("-test") and not suite.startswith(EXEMPT_PREFIXES) and f"{suite}-test" not in SUITES:
            errors.append(f"{suite}: missing companion suite {suite}-test")

    print(f"[validate-suites] {len(SUITES)} suites checked, {len(errors)} errors", flush=True)
    for error in errors:
        print("  " + error)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
