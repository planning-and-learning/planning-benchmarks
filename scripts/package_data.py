#!/usr/bin/env python3
"""Package the domain directories under data/ into per-domain tarballs plus a
pooch registry file, for upload as GitHub release assets."""

from __future__ import annotations

import argparse
import hashlib
import tarfile
from pathlib import Path

LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"


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


def archive_name(domain: Path, data_root: Path) -> str:
    return domain.relative_to(data_root).as_posix().replace("/", "--") + ".tar.gz"


def assert_no_lfs_pointers(domain: Path) -> None:
    for path in sorted(domain.rglob("*")):
        if path.is_file():
            with path.open("rb") as stream:
                if stream.read(len(LFS_POINTER_PREFIX)) == LFS_POINTER_PREFIX:
                    raise SystemExit(f"LFS pointer file at {path}; run 'git lfs pull' first")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path(__file__).resolve().parents[1] / "data")
    parser.add_argument("--output", type=Path, default=Path("dist/data"))
    parser.add_argument("--only", help="Only package domains under this data-relative prefix.")
    parser.add_argument("--dry-run", action="store_true", help="List archive names without writing anything.")
    args = parser.parse_args()

    domains = discover_domains(args.data_root)
    if args.only:
        prefix = args.only.rstrip("/")
        domains = [
            domain for domain in domains
            if domain.relative_to(args.data_root).as_posix().startswith(prefix)
        ]
    if not domains:
        raise SystemExit("no domains found")

    if args.dry_run:
        for domain in domains:
            print(archive_name(domain, args.data_root))
        return 0

    args.output.mkdir(parents=True, exist_ok=True)
    registry_lines = []
    for domain in domains:
        assert_no_lfs_pointers(domain)
        name = archive_name(domain, args.data_root)
        tar_path = args.output / name
        with tarfile.open(tar_path, "w:gz") as tar:
            for path in sorted(domain.rglob("*")):
                if path.is_file():
                    tar.add(path, arcname=path.relative_to(domain).as_posix())
        digest = hashlib.sha256(tar_path.read_bytes()).hexdigest()
        registry_lines.append(f"{name} sha256:{digest}")
        print(f"[package-data] {name} ({tar_path.stat().st_size} bytes)", flush=True)
    (args.output / "registry.txt").write_text("\n".join(registry_lines) + "\n", encoding="utf-8")
    print(f"[package-data] wrote {len(domains)} archives and registry.txt to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
