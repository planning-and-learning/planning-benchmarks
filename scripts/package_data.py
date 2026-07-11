#!/usr/bin/env python3
"""Package data/ into a single byte-reproducible data.tar.gz for upload as a
GitHub release asset, and print its sha256 (to pin in the package)."""

from __future__ import annotations

import argparse
import gzip
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


def assert_no_lfs_pointers(data_root: Path) -> None:
    for path in sorted(data_root.rglob("*")):
        if path.is_file():
            with path.open("rb") as stream:
                if stream.read(len(LFS_POINTER_PREFIX)) == LFS_POINTER_PREFIX:
                    raise SystemExit(f"LFS pointer file at {path}; run 'git lfs pull' first")


def write_archive(data_root: Path, tar_path: Path) -> None:
    """Byte-reproducible tar.gz (fixed metadata, no gzip timestamp): re-running
    produces identical bytes, so the pinned sha256 stays valid."""
    with open(tar_path, "wb") as out:
        with gzip.GzipFile(filename="", fileobj=out, mode="wb", mtime=0) as stream:
            with tarfile.open(fileobj=stream, mode="w") as tar:
                for path in sorted(data_root.rglob("*")):
                    if path.is_file():
                        info = tar.gettarinfo(path, arcname=path.relative_to(data_root).as_posix())
                        info.uid = info.gid = 0
                        info.uname = info.gname = ""
                        info.mtime = 0
                        info.mode = 0o644
                        with path.open("rb") as source:
                            tar.addfile(info, source)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path(__file__).resolve().parents[1] / "data")
    parser.add_argument("--output", type=Path, default=Path("dist-data/data.tar.gz"))
    parser.add_argument("--dry-run", action="store_true", help="List domains without writing anything.")
    args = parser.parse_args()

    domains = discover_domains(args.data_root)
    if not domains:
        raise SystemExit("no domains found")

    if args.dry_run:
        for domain in domains:
            print(domain.relative_to(args.data_root).as_posix())
        return 0

    assert_no_lfs_pointers(args.data_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_archive(args.data_root, args.output)
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    print(f"[package-data] {args.output} ({args.output.stat().st_size} bytes, {len(domains)} domains)")
    print(f"[package-data] sha256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
