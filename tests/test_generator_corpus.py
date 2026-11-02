"""Logical membership at the committed train/validation/test parameter scales."""
# Optional dependencies must be checked before importing executable contracts.
# pylint: disable=wrong-import-position
import importlib
import json
from pathlib import Path
from typing import cast

import pytest

pytest.importorskip("z3")
pytest.importorskip("pypddl")

from pypddl_datasets.generators import load_specification
from pypddl_datasets.generators.splits import SPLITS, Split

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = sorted(path.parent.name for path in
                 (ROOT / "src/pypddl_datasets/generators/classical").glob("*/generate_instances.py"))


@pytest.mark.parametrize("domain", DOMAINS)
@pytest.mark.parametrize("split", SPLITS)
def test_committed_instance_membership(domain: str, split: Split) -> None:
    directory = ROOT / "data/classical/generated" / f"{domain}-{split}"
    manifest = cast("dict[str, object]", json.loads((directory / "manifest.json").read_text()))
    record = cast("list[dict[str, object]]", manifest["instances"])[-1]
    parameters = cast("dict[str, object]", record["parameters"])
    generator = importlib.import_module(f"pypddl_datasets.generators.classical.{domain}.generator")
    specification = load_specification(domain, generator.Parameters(**parameters))
    result = specification.check_pddl(directory / cast(str, record["file"]), timeout_ms=30_000)
    assert result.is_member, (domain, split, parameters, result)
