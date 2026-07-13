#!/usr/bin/env python3
"""Check the layout of the data tree: every domain directory is flat (its
domain and problem PDDL side by side, no subdirectories), and every problem
file resolves to a domain file through the real pairing logic of
pypddl_datasets.fetching — so anything that passes here is fetchable."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypddl_datasets.discovery import discover_domains
from pypddl_datasets.fetching import pair_tasks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd() / "data")
    args = parser.parse_args(argv)
    root: Path = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")

    errors: list[str] = []
    domains = discover_domains(root)
    problems = 0
    for domain in domains:
        name = domain.relative_to(root).as_posix()
        for child in sorted(domain.iterdir()):
            if child.is_dir():
                errors.append(f"{name}: contains subdirectory {child.name}")
        try:
            problems += len(pair_tasks(name, domain))
        except ValueError as error:  # pairing names the unresolvable problem
            errors.append(f"{name}: {error}")

    print(f"[validate-layout] {len(domains)} domains, {problems} problems paired, {len(errors)} errors", flush=True)
    for error in errors:
        print("  " + error)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
