"""pytest plugin that regenerates tests/generator_samples.json from the generator tests.

It records the arguments of every successful make_problem call and keeps,
per generator module, the smallest call for each combination of flag/style values
plus the smallest calls overall (6 at least). Run from the repository root:

    PYTHONPATH=tests .venv/bin/pytest -q -p record_generator_samples tests \\
        --ignore tests/test_generators_parse.py \\
        -k "not fetch and not package and not release and not requirements_metadata"
"""

import json
import sys
from pathlib import Path
from types import FrameType
from typing import Any, cast

OUT = Path(__file__).with_name("generator_samples.json")
MAX_PER_FLAGS = 10  # recorded calls kept per module and flag combination
MIN_KEPT = 6

_calls: dict[str, list[dict[str, Any]]] = {}
_stack: list[tuple[str, dict[str, Any]]] = []


def _primitive(value: object) -> bool:
    if value is None or isinstance(value, (bool, int, float, str)):
        return True
    if isinstance(value, (tuple, list)):
        items = cast("tuple[object, ...] | list[object]", value)
        return all(_primitive(item) for item in items)
    return False


def _flags(kwargs: dict[str, Any]) -> str:
    return json.dumps({k: v for k, v in kwargs.items() if isinstance(v, (bool, str)) or v is None}, sort_keys=True)


def _size(kwargs: dict[str, Any]) -> float:
    return sum(abs(v) for v in kwargs.values() if isinstance(v, (int, float)) and not isinstance(v, bool))


def _profile(frame: FrameType, event: str, arg: object) -> None:
    code = frame.f_code
    if code.co_name != "make_problem" or "/generators/" not in code.co_filename:
        return
    if event == "call":
        names = code.co_varnames[: code.co_argcount + code.co_kwonlyargcount]
        _stack.append((str(frame.f_globals.get("__name__", "")), {n: frame.f_locals[n] for n in names}))
    elif event == "return" and _stack:
        module, kwargs = _stack.pop()
        if not isinstance(arg, str) or not all(_primitive(v) for v in kwargs.values()):
            return
        recorded = _calls.setdefault(module, [])
        if kwargs not in recorded and sum(_flags(k) == _flags(kwargs) for k in recorded) < MAX_PER_FLAGS:
            recorded.append(kwargs)


def pytest_configure() -> None:
    sys.setprofile(_profile)


def pytest_unconfigure() -> None:
    sys.setprofile(None)
    samples: dict[str, list[dict[str, Any]]] = {}
    for module, calls in sorted(_calls.items()):
        key = module.removeprefix("pypddl_datasets.generators.").removesuffix(".generator").replace(".", "/")
        ordered = sorted(calls, key=_size)
        seen: set[str] = set()
        kept: list[dict[str, Any]] = []
        for kwargs in ordered:
            if _flags(kwargs) not in seen:
                seen.add(_flags(kwargs))
                kept.append(kwargs)
        kept += [k for k in ordered if k not in kept][: max(0, MIN_KEPT - len(kept))]
        samples[key] = kept
    OUT.write_text(json.dumps(samples, indent=1, sort_keys=True) + "\n", encoding="utf-8")
