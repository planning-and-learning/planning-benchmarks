#!/usr/bin/env python3
"""Run all data checks: layout first (validation.layout), then full PDDL
content validation (validation.pddl). Arguments are forwarded to the content
check; the layout check receives the --root."""

from __future__ import annotations

import argparse
import sys

from pypddl_datasets.validation import layout, pddl


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root")
    known, _ = parser.parse_known_args(argv)

    # A malformed tree makes content validation noise; fail fast on layout.
    status = layout.main(["--root", known.root] if known.root else [])
    if status:
        return status
    return pddl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
