"""Bounded preparation reuse; sampled worlds and engine executions stay isolated."""
from __future__ import annotations

from collections import OrderedDict
from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass
from threading import local
from typing import Any

from problog.engine import DefaultEngine
from problog.logic import Term

_CACHE_SIZE = 32


@dataclass(frozen=True)
class PreparedProgram:
    """Static clauses and query declarations, with an exclusively borrowed engine."""
    engine: DefaultEngine
    database: Any
    queries: list[tuple[str, Term]]


class _ThreadPrograms(local):
    def __init__(self) -> None:
        self.cache: OrderedDict[tuple[str, bool], PreparedProgram] = OrderedDict()


_PROGRAMS = _ThreadPrograms()


def clear_prepared_cache() -> None:
    """Release this thread's idle prepared programs, for benchmarks and tests."""
    _PROGRAMS.cache.clear()



@contextmanager
def prepared_program(source: str, *, accelerated: bool = True) -> Generator[PreparedProgram, None, None]:
    """Reuse only successful, idle executions in the calling thread.

    Removing a borrowed entry also isolates reentrant calls through a custom RNG.
    An exception exits at ``yield`` and never returns the engine to the cache.
    Per-world choice dictionaries and grounding tables belong to fresh formulas;
    they must never be stored here.
    """
    from .programs import create_sampling_program

    key = (source, accelerated)
    prepared = _PROGRAMS.cache.pop(key, None)
    if prepared is None:
        prepared = PreparedProgram(*create_sampling_program(source, accelerated=accelerated))
    yield prepared
    _PROGRAMS.cache[key] = prepared
    if len(_PROGRAMS.cache) > _CACHE_SIZE:
        _PROGRAMS.cache.popitem(last=False)
