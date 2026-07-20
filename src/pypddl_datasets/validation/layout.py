#!/usr/bin/env python3
"""Check the layout of the data tree: every domain directory is flat (its
domain and problem PDDL side by side, no subdirectories), every problem
file resolves to a domain file through the real pairing logic of
pypddl_datasets.fetching — so anything that passes here is fetchable — and,
in a git checkout, the large-file system invariants hold (oversized files
packed, twins materialized, packed files gitignored)."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypddl_datasets.discovery import discover_domains
from pypddl_datasets.fetching import pair_tasks
from pypddl_datasets.scripts.large_files import GITIGNORE_BEGIN, GITIGNORE_END, THRESHOLD_BYTES, packed_files


def large_file_errors(root: Path) -> list[str]:
    unpack = "python -m pypddl_datasets.scripts.large_files unpack"
    pack = "python -m pypddl_datasets.scripts.large_files pack"
    errors: list[str] = []
    gitignore = root.parent / ".gitignore"
    lines = gitignore.read_text(encoding="utf-8").splitlines() if gitignore.is_file() else []
    ignored: set[str] = set(lines[lines.index(GITIGNORE_BEGIN) + 1 : lines.index(GITIGNORE_END)]) if GITIGNORE_BEGIN in lines and GITIGNORE_END in lines else set()
    twins: set[Path] = set()
    for twin in packed_files(root):
        plain = twin.with_name(twin.name[: -len(".gz")])
        twins.add(plain)
        if not plain.is_file():
            errors.append(f"{plain.relative_to(root).as_posix()}: not materialized; run `{unpack}`")
        if plain.relative_to(root.parent).as_posix() not in ignored:
            errors.append(f"{plain.relative_to(root).as_posix()}: missing from the managed .gitignore block; run `{pack}`")
    for path in sorted(root.rglob("*.pddl")):
        if path.is_file() and path.stat().st_size >= THRESHOLD_BYTES and path not in twins:
            errors.append(f"{path.relative_to(root).as_posix()}: {path.stat().st_size >> 20} MiB exceeds the large-file threshold; run `{pack}`")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd() / "data")
    args = parser.parse_args(argv)
    root: Path = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")

    errors: list[str] = []
    if (root.parent / ".git").is_dir():  # large-file invariants only apply to checkouts
        errors += large_file_errors(root)
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
