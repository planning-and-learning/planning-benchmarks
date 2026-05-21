#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path


TOKEN_RE = re.compile(r";[^\n]*(?=\n|$)|[()]|[^\s()]+|\s+", re.MULTILINE)

RESERVED_WORDS = {
    "-",
    "*",
    "+",
    "/",
    "<",
    "<=",
    "=",
    ">",
    ">=",
    "always",
    "and",
    "assign",
    "at-most-once",
    "decrease",
    "define",
    "domain",
    "either",
    "exists",
    "forall",
    "imply",
    "increase",
    "maximize",
    "minimize",
    "not",
    "number",
    "object",
    "or",
    "over",
    "preference",
    "problem",
    "scale-down",
    "scale-up",
    "sometime",
    "sometime-after",
    "sometime-before",
    "total-time",
    "when",
}


class ParseError(ValueError):
    pass


class Atom(str):
    pass


Expression = Atom | list["Expression"]


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text)


def syntax_tokens(text: str) -> list[str]:
    return [
        token
        for token in tokenize(text)
        if not token.isspace() and not token.startswith(";")
    ]


def parse_expression(tokens: list[str], index: int = 0) -> tuple[Expression, int]:
    if index >= len(tokens):
        raise ParseError("Unexpected end of input")

    token = tokens[index]
    if token == "(":
        items: list[Expression] = []
        index += 1
        while index < len(tokens) and tokens[index] != ")":
            item, index = parse_expression(tokens, index)
            items.append(item)
        if index >= len(tokens):
            raise ParseError("Missing closing parenthesis")
        return items, index + 1
    if token == ")":
        raise ParseError("Unexpected closing parenthesis")
    return Atom(token), index + 1


def parse_pddl(text: str) -> Expression:
    tokens = syntax_tokens(text)
    expression, index = parse_expression(tokens)
    if index != len(tokens):
        raise ParseError("Unexpected content after first expression")
    return expression


def is_obfuscatable(token: str) -> bool:
    if token.isspace() or token.startswith(";") or token in {"(", ")"}:
        return False
    if token.startswith(":"):
        return False
    if re.fullmatch(r"[+-]?\d+(?:\.\d+)?", token):
        return False
    return token.lower() not in RESERVED_WORDS


def atom_text(expression: Expression) -> str | None:
    if isinstance(expression, Atom):
        return str(expression)
    return None


def head_text(expression: Expression) -> str | None:
    if isinstance(expression, list) and expression:
        return atom_text(expression[0])
    return None


def is_headed(expression: Expression, head: str) -> bool:
    text = head_text(expression)
    return text is not None and text.lower() == head


def stable_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def reorder_key(expression: Expression) -> tuple[str, str]:
    rendered = render_expression(expression)
    return stable_hash(rendered), rendered


def sorted_expressions(expressions: list[Expression]) -> list[Expression]:
    return sorted(expressions, key=reorder_key)


def collect_identifiers(paths: list[Path]) -> tuple[list[str], list[str]]:
    names = set()
    variables = set()
    for path in paths:
        for token in tokenize(path.read_text(encoding="utf-8")):
            if is_obfuscatable(token):
                if token.startswith("?"):
                    variables.add(token)
                else:
                    names.add(token)
    return sorted(names, key=lambda name: (name.lower(), name)), sorted(
        variables, key=lambda variable: (variable.lower(), variable)
    )


def build_mapping(paths: list[Path]) -> dict[str, str]:
    names, variables = collect_identifiers(paths)
    mapping = {name: f"x{i:04d}" for i, name in enumerate(names, start=1)}
    mapping.update({variable: f"?v{i:04d}" for i, variable in enumerate(variables, start=1)})
    return mapping


def obfuscate_text(text: str, mapping: dict[str, str]) -> str:
    output = []
    for token in tokenize(text):
        if token.startswith(";"):
            continue
        output.append(mapping.get(token, token))
    return "".join(output)


def obfuscate_expression(expression: Expression, mapping: dict[str, str]) -> Expression:
    if isinstance(expression, Atom):
        return Atom(mapping.get(str(expression), str(expression)))
    return [obfuscate_expression(item, mapping) for item in expression]


def split_typed_sequence(items: list[Expression]) -> list[list[Expression]]:
    groups = []
    group: list[Expression] = []
    index = 0
    while index < len(items):
        item = items[index]
        group.append(item)
        if atom_text(item) == "-" and index + 1 < len(items):
            group.append(items[index + 1])
            groups.append(group)
            group = []
            index += 2
        else:
            index += 1
    if group:
        groups.append(group)
    return groups


def reorder_typed_sequence(items: list[Expression]) -> list[Expression]:
    reordered = []
    for group in sorted(split_typed_sequence(items), key=reorder_key):
        if any(atom_text(item) == "-" for item in group):
            separator_index = next(
                index for index, item in enumerate(group) if atom_text(item) == "-"
            )
            reordered.extend(sorted_expressions(group[:separator_index]))
            reordered.extend(group[separator_index:])
        else:
            reordered.extend(sorted_expressions(group))
    return reordered


def reorder_and_expression(expression: list[Expression]) -> list[Expression]:
    if len(expression) <= 2:
        return expression
    return [expression[0], *sorted_expressions(expression[1:])]


def reorder_goal_expression(expression: Expression) -> Expression:
    if is_headed(expression, "and"):
        return reorder_and_expression(expression)  # type: ignore[arg-type]
    return expression


def reorder_init_items(items: list[Expression]) -> list[Expression]:
    assignments = []
    facts = []
    for item in items:
        if is_headed(item, "="):
            assignments.append(item)
        else:
            facts.append(item)
    return [*sorted_expressions(assignments), *sorted_expressions(facts)]


def reorder_expression(expression: Expression) -> Expression:
    if isinstance(expression, Atom) or not expression:
        return expression

    expression = [reorder_expression(item) for item in expression]
    head = atom_text(expression[0])
    lowered = head.lower() if head is not None else None

    if lowered == "and":
        return reorder_and_expression(expression)

    if lowered == ":predicates":
        return [expression[0], *sorted_expressions(expression[1:])]

    if lowered in {":constants", ":objects", ":types"}:
        return [expression[0], *reorder_typed_sequence(expression[1:])]

    if lowered == ":init":
        return [expression[0], *reorder_init_items(expression[1:])]

    if lowered == ":goal" and len(expression) == 2:
        return [expression[0], reorder_goal_expression(expression[1])]

    if lowered == "define":
        header = expression[1:2]
        sections = expression[2:]
        actions = [section for section in sections if is_headed(section, ":action")]
        other_sections = [
            section for section in sections if not is_headed(section, ":action")
        ]
        return [expression[0], *header, *other_sections, *sorted_expressions(actions)]

    return expression


def render_expression(expression: Expression, indent: int = 0) -> str:
    if isinstance(expression, Atom):
        return str(expression)
    if not expression:
        return "()"

    head = atom_text(expression[0])
    if head is not None and head.lower() in {":predicates", ":init"}:
        lines = ["(" + head]
        lines.extend(
            f"{' ' * (indent + 2)}{render_expression(item, indent + 2)}"
            for item in expression[1:]
        )
        lines[-1] += ")"
        return "\n".join(lines)

    if head is not None and head.lower() == "define":
        lines = ["(define"]
        lines.extend(
            f"{' ' * (indent + 2)}{render_expression(item, indent + 2)}"
            for item in expression[1:]
        )
        lines[-1] += ")"
        return "\n".join(lines)

    if head is not None and head.lower() == ":action":
        lines = [f"(:action {render_expression(expression[1], indent + 9)}"]
        index = 2
        while index < len(expression):
            if (
                index + 1 < len(expression)
                and isinstance(expression[index], Atom)
                and str(expression[index]).startswith(":")
            ):
                lines.append(
                    f"{' ' * (indent + 2)}{expression[index]} "
                    f"{render_expression(expression[index + 1], indent + 2)}"
                )
                index += 2
            else:
                lines.append(
                    f"{' ' * (indent + 2)}{render_expression(expression[index], indent + 2)}"
                )
                index += 1
        lines[-1] += ")"
        return "\n".join(lines)

    return "(" + " ".join(render_expression(item, indent) for item in expression) + ")"


def obfuscate_and_reorder_text(text: str, mapping: dict[str, str]) -> str:
    expression = parse_pddl(text)
    expression = obfuscate_expression(expression, mapping)
    expression = reorder_expression(expression)
    return render_expression(expression) + "\n"


def obfuscate_domain_dir(source_dir: Path, target_dir: Path) -> int:
    pddl_paths = sorted(source_dir.rglob("*.pddl"))
    if not pddl_paths:
        return 0

    mapping = build_mapping(pddl_paths)
    for source_path in pddl_paths:
        target_path = target_dir / source_path.relative_to(source_dir)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        text = source_path.read_text(encoding="utf-8")
        target_path.write_text(obfuscate_and_reorder_text(text, mapping), encoding="utf-8")
    return len(pddl_paths)


def obfuscate_tree(source_root: Path, target_root: Path) -> int:
    if target_root.exists():
        shutil.rmtree(target_root)
    target_root.mkdir(parents=True, exist_ok=True)

    count = 0
    for domain_file in sorted(source_root.rglob("domain.pddl")):
        source_domain_dir = domain_file.parent
        target_domain_dir = target_root / source_domain_dir.relative_to(source_root)
        count += obfuscate_domain_dir(source_domain_dir, target_domain_dir)
    return count


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create an obfuscated copy of generated PDDL data."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="source data root, default: this script's directory",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "obfuscated_data",
        help="target data root, default: repository obfuscated_data directory",
    )
    args = parser.parse_args(argv)

    count = obfuscate_tree(args.source.resolve(), args.target.resolve())
    print(f"Obfuscated {count} PDDL files into {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
