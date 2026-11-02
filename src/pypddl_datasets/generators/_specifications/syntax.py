"""Solver-independent parsing of finite, self-contained distribution contracts."""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from functools import lru_cache
import json
from importlib.resources import files
from types import MappingProxyType
from typing import Protocol, cast

from typing_extensions import override

from lark import Lark, Token, Tree
from lark.exceptions import UnexpectedInput


@dataclass(frozen=True)
class SourceSpan:
    source: str
    line: int
    column: int
    end_line: int
    end_column: int
    start: int = 0
    end: int = 0

    @override
    def __str__(self) -> str:
        return f"{self.source}:{self.line}:{self.column}"


class SpecificationError(ValueError):
    """A malformed or ill-typed contract, with its original source location."""

    def __init__(self, message: str, span: SourceSpan | None = None) -> None:
        self.span = span
        super().__init__(f"{span}: {message}" if span else message)


@dataclass(frozen=True)
class Node:
    """Compact immutable syntax tree; terminals retain their exact spelling."""

    kind: str
    children: tuple[Node, ...]
    span: SourceSpan
    value: str = ""


@dataclass(frozen=True)
class Parameter:
    name: str
    type_name: str
    nullable: bool
    default: Node | None
    span: SourceSpan


@dataclass(frozen=True)
class Definition:
    language: int
    distribution: str
    revision: str
    metadata: Mapping[str, str | tuple[str, ...]]
    parameters: tuple[Parameter, ...]
    statements: tuple[Node, ...]
    source_text: str
    source_name: str

    @property
    def constraint_sources(self) -> tuple[str, ...]:
        return tuple(self.source_text[node.children[1].span.start:node.children[1].span.end]
                     for node in self.statements if node.kind == "requirement")


@lru_cache(maxsize=1)
def _parser() -> Lark:
    grammar = files("pypddl_datasets.generators._specifications").joinpath("grammar.lark").read_text(encoding="utf-8")
    return Lark(grammar, parser="lalr", propagate_positions=True, maybe_placeholders=False)


def _node(tree: Tree[Token] | Token, source: str) -> Node:
    if isinstance(tree, Token):
        span = SourceSpan(source, tree.line or 1, tree.column or 1, tree.end_line or 1,
                          tree.end_column or 1, tree.start_pos or 0, tree.end_pos or 0)
        return Node("token", (), span, str(tree))
    meta = tree.meta
    span = SourceSpan(source, meta.line, meta.column, meta.end_line, meta.end_column,
                      meta.start_pos, meta.end_pos)
    return Node(str(tree.data), tuple(_node(child, source) for child in tree.children), span)


def string_value(node: Node) -> str:
    try:
        value: object = json.loads(node.value)
    except json.JSONDecodeError as error:
        raise SpecificationError("invalid string escape", node.span) from error
    if not isinstance(value, str):
        raise SpecificationError("expected a string", node.span)
    return value


def _metadata_value(node: Node) -> str | tuple[str, ...]:
    if node.kind == "string":
        return string_value(node.children[0])
    if node.kind == "list":
        children = node.children[0].children if node.children else ()
        if all(child.kind == "string" for child in children):
            return tuple(string_value(child.children[0]) for child in children)
    raise SpecificationError("metadata values must be strings or lists of strings", node.span)


def _metadata(node: Node) -> Mapping[str, str | tuple[str, ...]]:
    result: dict[str, str | tuple[str, ...]] = {}
    for entry in node.children:
        name, value = entry.children
        if name.value in result:
            raise SpecificationError(f"duplicate metadata field {name.value!r}", name.span)
        result[name.value] = _metadata_value(value)
    return MappingProxyType(result)


def _parameter(node: Node) -> Parameter:
    name, kind, *default = node.children
    type_name = kind.children[0].value
    if type_name not in {"int", "float", "str"}:
        raise SpecificationError(f"unsupported parameter type {type_name!r}", kind.span)
    return Parameter(name.value, type_name, len(kind.children) == 2,
                     default[0] if default else None, node.span)


class _Parser(Protocol):
    def parse(self, text: str) -> Tree[Token]: ...


def parse_definition(source: str, source_name: str = "<string>") -> Definition:
    """Parse without importing a solver, executing expressions, or loading code."""
    try:
        tree = cast(_Parser, _parser()).parse(source)
    except UnexpectedInput as error:
        span = SourceSpan(source_name, error.line, error.column, error.line, error.column)
        raise SpecificationError("invalid specification syntax", span) from error
    root = _node(tree, source_name)
    language, domain, revision, metadata, *statements = root.children
    if language.value != "1":
        raise SpecificationError(f"unsupported language version {language.value}", language.span)
    body_started = False
    for statement in statements:
        if statement.kind == "parameter" and body_started:
            raise SpecificationError("parameters must precede other declarations", statement.span)
        body_started = body_started or statement.kind != "parameter"
    parameters = tuple(_parameter(node) for node in statements if node.kind == "parameter")
    names = [parameter.name for parameter in parameters]
    if len(names) != len(set(names)):
        raise SpecificationError("duplicate parameter declaration", root.span)
    return Definition(1, domain.value, string_value(revision), _metadata(metadata), parameters,
                      tuple(node for node in statements if node.kind != "parameter"), source, source_name)
