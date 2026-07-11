#!/usr/bin/env python3

import argparse
import json
import re
from pathlib import Path
from typing import Any

from pypddl.formalism import Parser, ParserOptions


DECLARATION = re.compile(r"\(\s*define\s*\(\s*(domain|problem)\s+([^\s()]+)", re.IGNORECASE)
DOMAIN_REFERENCE = re.compile(r"\(\s*:domain\s+([^\s()]+)", re.IGNORECASE)
PROGRESS_INTERVAL = 100
Record = dict[str, Any]
ResolutionError = tuple[str, str]


def positive_int(value: str) -> int:
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return value


def classify(path: Path, root: Path) -> Record:
    text = re.sub(r";[^\n]*", "", path.read_text(encoding="utf-8", errors="replace"))
    declaration = DECLARATION.search(text)
    record = {
        "path": path.relative_to(root).as_posix(),
        "kind": "unknown",
        "name": None,
        "status": "not_processed",
    }
    if not declaration:
        return record

    record["kind"] = declaration.group(1).lower()
    record["name"] = declaration.group(2)
    if record["kind"] == "problem":
        reference = DOMAIN_REFERENCE.search(text)
        record["domain"] = reference.group(1) if reference else None
    return record


def domain_candidates(problem_path: Path) -> list[str]:
    stem = problem_path.stem
    return [
        "domain.pddl",
        f"{stem}-domain{problem_path.suffix}",
        f"{stem[:3]}-domain.pddl",
        f"domain_{problem_path.name}",
        f"domain-{problem_path.name}",
    ]


def find_domain(
    problem_path: Path,
    problem_domain: str | None,
    root: Path,
    domains_by_directory: dict[Path, list[tuple[Path, str]]],
) -> tuple[Path | None, ResolutionError | None]:
    directory = problem_path.parent
    while directory == root or root in directory.parents:
        domains = domains_by_directory.get(directory, [])
        by_name = {path.name: path for path, _ in domains}
        for candidate in domain_candidates(problem_path):
            if candidate in by_name:
                return by_name[candidate], None

        matching = [path for path, name in domains if problem_domain and name.lower() == problem_domain.lower()]
        if len(matching) == 1:
            return matching[0], None
        if len(matching) > 1:
            names = ", ".join(path.relative_to(root).as_posix() for path in matching)
            return None, ("AmbiguousDomainError", f"multiple matching domain files: {names}")

        if directory == root:
            break
        directory = directory.parent
    return None, ("DomainNotFoundError", f"no domain file found for domain {problem_domain!r}")


def set_error(record: Record, error_type: str, message: str) -> None:
    record["status"] = "error"
    record["error"] = {"type": error_type, "message": message}


def log_progress(kind: str, checked: int, total: int, errors: int, force: bool = False) -> None:
    if force or checked == total or checked % PROGRESS_INTERVAL == 0:
        print(f"[validate] {kind}: {checked}/{total} checked ({errors} errors)", flush=True)


def validate(root: Path, error_limit: int | None, strict: bool = False) -> Record:
    paths = sorted(path for path in root.rglob("*") if path.is_file() and path.suffix.lower() == ".pddl")
    records = [classify(path, root) for path in paths]
    path_by_name = {record["path"]: root / record["path"] for record in records}
    domains = [record for record in records if record["kind"] == "domain"]
    problems = [record for record in records if record["kind"] == "problem"]
    unknown = [record for record in records if record["kind"] == "unknown"]
    print(
        f"[validate] discovered {len(paths)} PDDL files: "
        f"{len(domains)} domains, {len(problems)} problems, {len(unknown)} unclassified",
        flush=True,
    )

    errors = 0
    checked_domains = 0
    checked_problems = 0
    terminated_early = False
    valid_domains = set()
    domains_by_directory = {}
    parser_options = ParserOptions()
    parser_options.strict = strict

    for record in unknown:
        set_error(record, "ClassificationError", "missing '(define (domain ...)' or '(define (problem ...)' declaration")
        errors += 1
        if error_limit is not None and errors >= error_limit:
            terminated_early = True
            break

    if not terminated_early:
        for record in domains:
            path = path_by_name[record["path"]]
            domains_by_directory.setdefault(path.parent, []).append((path, record["name"]))
            checked_domains += 1
            try:
                Parser(path, parser_options)
                record["status"] = "ok"
                valid_domains.add(path)
            except Exception as error:
                set_error(record, type(error).__name__, str(error))
                errors += 1
            log_progress("domains", checked_domains, len(domains), errors)
            if error_limit is not None and errors >= error_limit:
                terminated_early = True
                break

    if not terminated_early:
        for record in problems:
            problem_path = path_by_name[record["path"]]
            checked_problems += 1
            if not record["domain"]:
                set_error(record, "DomainReferenceError", "missing '(:domain ...)' declaration")
                errors += 1
            else:
                domain_path, resolution_error = find_domain(
                    problem_path, record["domain"], root, domains_by_directory
                )
                if resolution_error:
                    set_error(record, *resolution_error)
                    errors += 1
                elif domain_path not in valid_domains:
                    relative_domain = domain_path.relative_to(root).as_posix()
                    record["domain_file"] = relative_domain
                    set_error(record, "DomainParseError", f"domain file failed to parse: {relative_domain}")
                    errors += 1
                else:
                    record["domain_file"] = domain_path.relative_to(root).as_posix()
                    try:
                        Parser(domain_path, parser_options).parse_task(problem_path)
                        record["status"] = "ok"
                    except Exception as error:
                        set_error(record, type(error).__name__, str(error))
                        errors += 1
            log_progress("problems", checked_problems, len(problems), errors)
            if error_limit is not None and errors >= error_limit:
                terminated_early = True
                break
    if checked_domains != len(domains):
        log_progress("domains", checked_domains, len(domains), errors, force=True)
    if checked_problems != len(problems):
        log_progress("problems", checked_problems, len(problems), errors, force=True)
    if terminated_early:
        print(f"[validate] stopped after reaching the error limit ({error_limit})", flush=True)

    return {
        "root": str(root),
        "error_limit": error_limit,
        "strict": strict,
        "terminated_early": terminated_early,
        "summary": {
            "files": len(records),
            "domains": len(domains),
            "problems": len(problems),
            "unclassified": len(unknown),
            "checked_domains": checked_domains,
            "checked_problems": checked_problems,
            "errors": errors,
        },
        "files": records,
        "errors": [
            {"path": record["path"], "kind": record["kind"], **record["error"]}
            for record in records
            if record["status"] == "error"
        ],
    }


def split_report(report: Record) -> tuple[Record, Record]:
    metadata: Record = {
        "root": report["root"],
        "error_limit": report["error_limit"],
        "strict": report["strict"],
        "terminated_early": report["terminated_early"],
        "summary": report["summary"],
    }
    return (
        {**metadata, "files": [record for record in report["files"] if record["status"] == "ok"]},
        {
            **metadata,
            "files": [record for record in report["files"] if record["status"] == "error"],
            "unprocessed": [record for record in report["files"] if record["status"] == "not_processed"],
        },
    )


def main() -> int:
    script_root: Path = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Recursively validate PDDL domains and problems with pypddl.")
    parser.add_argument("--root", type=Path, default=script_root, help="Directory to traverse (default: repository root).")
    parser.add_argument("--success-output", type=Path, help="Success report path (default: <root>/validate.sucess.json).")
    parser.add_argument("--error-output", type=Path, help="Error report path (default: <root>/validate.error.json).")
    parser.add_argument("--limit", type=positive_int, help="Stop after this many errors.")
    parser.add_argument("--strict", action="store_true", help="Enable strict semantic PDDL validation.")
    args = parser.parse_args()

    root: Path = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    success_output: Path = args.success_output.resolve() if args.success_output else root / "validate.sucess.json"
    error_output: Path = args.error_output.resolve() if args.error_output else root / "validate.error.json"
    report = validate(root, args.limit, args.strict)
    success_report, error_report = split_report(report)
    for output, contents in [(success_output, success_report), (error_output, error_report)]:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(contents, indent=2) + "\n", encoding="utf-8")
    print(
        f"[validate] wrote {success_output} and {error_output} with {report['summary']['errors']} errors",
        flush=True,
    )
    return int(report["summary"]["errors"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
