"""Compose experimental declarative graph laws into an unchanged Rovers model.

No Python graph sampling or production model edits are performed. The sparse
variant approximates classic IPC edge scaling, not its distribution; ipc2023
reproduces its graph construction but retains our other Rovers distributions.
"""
from __future__ import annotations

from pathlib import Path

from pypddl_datasets.generators.probabilistic import model_source

VARIANTS = ("current", "sparse", "ipc2023")
ROOT = Path(__file__).resolve().parent
START = "% Finite local rejection, with the visibility fixed during movement retries."
END = "% The seven equiprobable nonempty subsets, in the legacy bit-mask order."


def source(variant: str, parameters: dict[str, int | float]) -> str:
    """Keep the canonical library prefix, enabling its existing accelerations."""
    if variant not in VARIANTS:
        raise ValueError(f"unknown graph variant: {variant}")
    original = model_source("rovers", parameters)
    if variant == "current":
        return original
    if original.count(START) != 1 or original.count(END) != 1:
        raise ValueError("the Rovers graph section changed; review the experiment")
    before, body = original.split(START, 1)
    _, after = body.split(END, 1)
    return "\n".join((before, (ROOT / "graph_samplers.pl").read_text(),
                       (ROOT / "rovers_graphs.pl").read_text(),
                       f"graph_variant({variant}).", END + after))
