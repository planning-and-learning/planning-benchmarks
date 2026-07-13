#!/usr/bin/env python3
"""Make data/ strict-clean: iteratively parse every domain/task with pypddl in
strict mode and repair the (:requirements ...) declarations the errors point
at — remove aggregates and unused tokens, add missing ones. Repository
tooling; file contents outside the requirements line are never touched."""

from __future__ import annotations

import argparse
import functools
import os
import re
from collections import Counter
from collections.abc import Callable
from pathlib import Path

import pypddl_datasets
from pypddl_datasets.discovery import discover_domains
from pypddl import formalism
from pypddl.formalism import Parser, ParserOptions

TOKEN = re.compile(
    r"(?:Missing required PDDL requirement|Aggregate PDDL requirement must be declared atomically"
    r"|Unused PDDL requirement|Task requirement already declared by the domain): (:[a-z0-9-]+)"
)
REQUIREMENTS = re.compile(r"\(\s*:requirements([^)]*)\)", re.IGNORECASE)
DOMAIN_HEADER = re.compile(r"\(\s*define\s*\(\s*domain[^)]*\)", re.IGNORECASE)
PROBLEM_DOMAIN = re.compile(r"\(\s*:domain[^)]*\)", re.IGNORECASE)
MAX_ROUNDS = 40


def edit_requirements(path: Path, add: str | None = None, remove: str | None = None) -> None:
    text = path.read_text(encoding="utf-8")
    match = REQUIREMENTS.search(text)
    if match and ";" in match.group(1):
        raise RuntimeError(f"comment inside (:requirements ...) in {path}; fix the layout manually")
    if match:
        tokens = [t for t in match.group(1).split() if t != remove]
        if add and add not in tokens:
            tokens.append(add)
        tokens = sorted(set(tokens), key=lambda t: (t != ":strips", t))
        replacement = "" if not tokens else "(:requirements " + " ".join(tokens) + ")"
        start, end = match.span()
        if not tokens:  # drop the whole line if it became empty
            line_start = text.rfind("\n", 0, start) + 1
            line_end = text.find("\n", end)
            if text[line_start:start].strip() == "" and (line_end == -1 or text[end:line_end].strip() == ""):
                start, end = line_start, (len(text) if line_end == -1 else line_end + 1)
        text = text[:start] + replacement + text[end:]
    elif add:
        # problems declare requirements after (:domain ...); domains after the define header
        anchor = PROBLEM_DOMAIN.search(text) or DOMAIN_HEADER.search(text)
        if anchor is None:
            raise RuntimeError(f"no insertion anchor in {path}")
        end = anchor.end()
        text = text[:end] + f"\n  (:requirements {add})" + text[end:]
    path.write_text(text, encoding="utf-8")


def repair(path: Path, parse: Callable[[], object], stats: Counter[str], failures: list[str]) -> None:
    for _ in range(MAX_ROUNDS):
        try:
            parse()
            return
        except (formalism.AggregateRequirementError, formalism.UnusedRequirementError, formalism.RedundantRequirementError) as error:
            token = TOKEN.search(str(error))
            assert token, str(error)
            edit_requirements(path, remove=token.group(1))
            stats[f"removed {token.group(1)}"] += 1
        except formalism.MissingRequirementError as error:
            token = TOKEN.search(str(error))
            assert token, str(error)
            edit_requirements(path, add=token.group(1))
            stats[f"added {token.group(1)}"] += 1
        except Exception as error:  # noqa: BLE001 — anything non-mechanical is reported, not guessed at
            failures.append(f"{path}: {type(error).__name__}: {str(error).splitlines()[0] if str(error) else ''}")
            return
    failures.append(f"{path}: did not converge after {MAX_ROUNDS} rounds")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path.cwd() / "data")
    args = parser.parse_args()
    data_root = args.data_root.resolve()
    os.environ["PYPDDL_DATASETS_DATA"] = str(data_root)

    options = ParserOptions()
    options.strict = True  # add_action_costs stays default, matching validation.pddl --strict

    stats: Counter[str] = Counter()
    failures: list[str] = []

    @functools.cache
    def repaired_domain_parser(domain_path: Path) -> Parser | None:
        repair(domain_path, lambda: Parser(domain_path, options), stats, failures)
        try:
            return Parser(domain_path, options)
        except Exception:  # noqa: BLE001 — already recorded by repair()
            return None

    for index, domain_dir in enumerate(discover_domains(data_root), start=1):
        name = domain_dir.relative_to(data_root).as_posix()
        for task in pypddl_datasets.fetch_domain(name).tasks:
            domain_parser = repaired_domain_parser(task.domain_path)
            if domain_parser is None:
                continue
            # generated pypddl stub types parse_task with a bare os.PathLike;
            # drop the suppression once the loki stubgen emits os.PathLike[str]
            repair(
                task.task_path,
                lambda parser=domain_parser, path=task.task_path: parser.parse_task(path),  # pyright: ignore[reportUnknownMemberType]
                stats,
                failures,
            )
        if index % 50 == 0:
            print(f"[strict-clean] {index} domains processed", flush=True)

    print(f"[strict-clean] edits: {sum(stats.values())}")
    for what, count in stats.most_common():
        print(f"  {count:5d}  {what}")
    if failures:
        print(f"[strict-clean] unresolved ({len(failures)}):")
        for failure in failures[:30]:
            print("  " + failure)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
