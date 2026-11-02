"""Public discovery and generation remain usable without optional solvers."""
from dataclasses import fields, is_dataclass, replace
import importlib
import subprocess
import sys

import pytest

from pypddl_datasets.generators import get_specification, list_specifications
from pypddl_datasets.generators.runtime import (
    Assignment, Problem, atom, objects, semantic_fingerprint,
)


@pytest.mark.parametrize("description", list_specifications(), ids=lambda description: description.domain)
def test_all_public_generator_modules(description: object) -> None:
    # Obtain the typed descriptor here so pytest's parametrization needs no plugin.
    domain = str(getattr(description, "domain"))
    specification = get_specification(domain)
    assert specification.parameters
    assert f"distribution {domain};" in specification.source
    assert specification.parameter_constraints
    module = importlib.import_module(f"pypddl_datasets.generators.classical.{domain}.generator")
    assert callable(module.Parameters) and callable(module.sample) and callable(module.render)
    parameters_class: object = module.Parameters
    assert is_dataclass(parameters_class)
    assert specification.parameters == tuple(field.name for field in fields(parameters_class))


def test_discovery_without_optional_dependencies() -> None:
    script = '''
import importlib
import importlib.abc
import sys
class BlockOptional(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[0] in {"z3", "pypddl"}:
            raise ImportError("optional dependency deliberately unavailable")
sys.meta_path.insert(0, BlockOptional())
from pypddl_datasets.generators import list_specifications, get_specification
assert len(list_specifications()) == 23
for description in list_specifications():
    assert get_specification(description.domain) == description
    assert "initial {" in description.source and "goal {" in description.source
    importlib.import_module("pypddl_datasets.generators.classical." + description.domain + ".generator")
'''
    subprocess.run([sys.executable, "-c", script], check=True, capture_output=True, text=True)


def test_semantic_identity_preserves_labels_but_ignores_presentation() -> None:
    original = Problem("first", "toy", objects(["x", "y"]),
                       (atom("ready", "x"), Assignment(atom("fuel"), 1)), (atom("done", "y"),))
    reordered = replace(original, name="second", objects=tuple(reversed(original.objects)),
                        initial=(Assignment(atom("fuel"), 1.0), atom("ready", "x"), atom("ready", "x")))
    assert semantic_fingerprint(original) == semantic_fingerprint(reordered)
    assert semantic_fingerprint(original) != semantic_fingerprint(replace(original, goal=(atom("done", "x"),)))


def test_unknown_specification_is_an_error() -> None:
    with pytest.raises(KeyError, match="Unknown generator"):
        get_specification("missing")
