"""Frozen graph proposal algorithms used by the Rovers reference sampler."""
# This historical oracle intentionally preserves the old source verbatim.
# pylint: disable=duplicate-code
from __future__ import annotations

from collections.abc import Iterable
from itertools import combinations
import math

from pypddl_datasets.generators.runtime import GenerationExhausted, RandomSource


def is_connected(num_nodes: int, edges: Iterable[tuple[int, int]]) -> bool:
    """Check connectivity of an undirected graph on range(num_nodes)."""
    if num_nodes < 1:
        return False
    neighbors: list[list[int]] = [[] for _ in range(num_nodes)]
    for left, right in edges:
        if not 0 <= left < num_nodes or not 0 <= right < num_nodes:
            raise ValueError("graph edge endpoint outside the object universe")
        neighbors[left].append(right)
        neighbors[right].append(left)
    reached = {0}
    frontier = [0]
    while frontier:
        for neighbor in neighbors[frontier.pop()]:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(neighbor)
    return len(reached) == num_nodes


def _graph_candidates(
    num_nodes: int, allowed_edges: Iterable[tuple[int, int]] | None
) -> tuple[tuple[int, int], ...]:
    if num_nodes < 1:
        raise ValueError("num_nodes must be positive")
    if allowed_edges is None:
        return tuple(combinations(range(num_nodes), 2))
    candidates = tuple(sorted({(min(left, right), max(left, right)) for left, right in allowed_edges}))
    if any(left == right for left, right in candidates):
        raise ValueError("self-loops are not permitted")
    if not is_connected(num_nodes, candidates):
        raise ValueError("the allowed edges cannot form a connected graph")
    return candidates


def connected_edges(  # pylint: disable=too-many-arguments
    num_nodes: int,
    rng: RandomSource,
    probability: float = 0.5,
    *,
    allowed_edges: Iterable[tuple[int, int]] | None = None,
    max_attempts: int = 10_000,
) -> set[tuple[int, int]]:
    """Independent undirected edges conditioned on connectivity.

    Every successful proposal has the Bernoulli law conditioned on being
    connected. Exhaustion is explicit: no backbone repair or fallback changes
    the measure. Restricting the candidate universe supports rover subgraphs.
    """
    if not math.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("edge probability must be finite and in [0, 1]")
    if max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    candidates = _graph_candidates(num_nodes, allowed_edges)
    if num_nodes > 1 and probability == 0:
        raise ValueError("a connected graph with multiple nodes needs positive probability")
    for _ in range(max_attempts):
        edges = {edge for edge in candidates if rng.random() < probability}
        if is_connected(num_nodes, edges):
            return edges
    raise GenerationExhausted(
        f"no connected graph in {max_attempts} proposals "
        f"(nodes={num_nodes}, edge_probability={probability})"
    )
