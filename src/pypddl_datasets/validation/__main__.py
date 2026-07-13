#!/usr/bin/env python3
"""Run all data checks: layout (validation.layout), suite configuration
(validation.suites), then full PDDL content validation (validation.pddl).
Arguments are forwarded to the content check; the cheap checks receive the
--root and fail fast."""

from __future__ import annotations

import argparse
import sys

from pypddl_datasets.validation import layout, pddl, suites


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--root")
    known, _ = parser.parse_known_args(argv)

    # A malformed tree or suite config makes content validation noise; fail fast.
    root_args = ["--root", known.root] if known.root else []
    for check in (layout, suites):
        status = check.main(list(root_args))
        if status:
            return status
    return pddl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
