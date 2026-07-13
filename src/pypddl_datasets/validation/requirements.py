#!/usr/bin/env python3
"""Check that the committed requirements.*.json metadata is up to date with
data/ by regenerating it (scripts/extract_requirements.py) and comparing.
Run by the data release pipeline — deliberately not per pull request, so
concurrent data PRs need not each regenerate the shared metadata files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pypddl_datasets.scripts.extract_requirements import generate

PACKAGE = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd() / "data")
    args = parser.parse_args(argv)
    root: Path = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")

    stale: list[str] = []
    for filename, generated in generate(root).items():
        committed = json.loads((PACKAGE / filename).read_text(encoding="utf-8"))
        if generated != committed:
            stale.append(filename)

    print(f"[validate-requirements] 3 metadata files checked, {len(stale)} stale", flush=True)
    for filename in stale:
        print(f"  {filename} is stale; regenerate with scripts/extract_requirements.py")
    return int(bool(stale))


if __name__ == "__main__":
    raise SystemExit(main())
