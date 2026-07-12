"""Domain discovery over a local data tree."""

from __future__ import annotations

from pathlib import Path


def discover_domains(data_root: Path) -> list[Path]:
    """A domain is a maximal directory containing at least one .pddl file directly."""
    domains: list[Path] = []

    def walk(directory: Path) -> None:
        if any(child.suffix == ".pddl" for child in directory.iterdir() if child.is_file()):
            domains.append(directory)
            return
        for child in directory.iterdir():
            if child.is_dir():
                walk(child)

    walk(data_root)
    return sorted(domains)
