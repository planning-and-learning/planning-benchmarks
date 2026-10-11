#!/usr/bin/env python3
# Reconstruction of the IPC 2014 Genome Edit Distance tasks (ITT operations only;
# data/classical/downward-benchmarks/ged-{opt,sat}14-strips). The IPC tasks are pairs of
# real mitochondrial genomes; no generator was published, so this draws synthetic pairs
# in the compressed form of the IPC tasks (no shared adjacency except the circle's seam).

from __future__ import annotations

import argparse
import random
import sys
import time
from typing import cast


def _adjacencies(genome: list[int]) -> set[tuple[int, int]]:
    """Signed adjacencies of a genome read linearly from g1, on both strands."""
    pairs = list(zip(genome, genome[1:]))
    return {*pairs, *((-b, -a) for a, b in pairs)}


def make_problem(
    num_genes: int,
    seed: int | None = None,
    init_inverted_probability: float = 0.08,
    goal_inverted_probability: float = 0.45,
) -> str:
    """Generate a GED task: turn one signed circular genome into another.

    Genes ``g1..g<num_genes>``. The initial genome is ``g1..gn`` in order, every gene
    but ``g1`` inverted with ``init_inverted_probability``. The goal genome keeps
    ``g1`` (normal) first and ``gn`` (as initially) last, as in every IPC task, with
    the genes in between in uniformly random order, each inverted with
    ``goal_inverted_probability``. Goal genomes sharing a signed adjacency with the
    initial genome (read linearly from ``g1``) are redrawn: the IPC tasks merge such
    adjacencies into one gene.
    """
    genes = cast(object, num_genes)  # runtime guard: callers may pass floats or bools
    if not isinstance(genes, int) or isinstance(genes, bool) or genes < 4:
        raise ValueError("num_genes must be an integer at least 4")
    for name, value in (
        ("init_inverted_probability", init_inverted_probability),
        ("goal_inverted_probability", goal_inverted_probability),
    ):
        if not 0 <= value <= 1:
            raise ValueError(f"{name} must be in [0, 1]")

    rng = random.Random(seed if seed is not None else int(time.time()))
    init = [1, *(-g if rng.random() < init_inverted_probability else g for g in range(2, num_genes + 1))]
    shared = _adjacencies(init)
    while True:  # ponytail: rejection; about 2 draws per task at any size
        middle = rng.sample(range(2, num_genes), num_genes - 2)
        goal = [1, *(-g if rng.random() < goal_inverted_probability else g for g in middle), init[-1]]
        if not _adjacencies(goal) & shared:
            break

    def orientations(genome: list[int]) -> list[str]:
        return [f"({'inverted' if g < 0 else 'normal'} g{abs(g)})" for g in genome]

    def cycle(genome: list[int]) -> list[str]:
        return [f"(cw g{abs(a)} g{abs(b)})" for a, b in zip(genome, genome[1:] + genome[:1])]

    init_facts = [
        *orientations(init),
        *(f"(present g{g})" for g in range(1, num_genes + 1)),
        *cycle(init),
        "(idle)",
        "(= (total-cost) 0)",
    ]
    goal_facts = [*orientations(goal), *cycle(goal)]
    objects = " ".join(f"g{g}" for g in range(1, num_genes + 1))
    return f"""(define (problem ged-g{num_genes})
  (:domain genome-edit-distance)
  (:objects {objects})
  (:init
{chr(10).join("    " + f for f in init_facts)}
  )
  (:goal
    (and
{chr(10).join("      " + f for f in goal_facts)}
    )
  )
  (:metric minimize (total-cost))
)
""".lower()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Genome Edit Distance PDDL problem.")
    parser.add_argument("num_genes", type=int, help="number of genes (objects)")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    parser.add_argument("--init-inverted-probability", type=float, default=0.08, help="gene inverted initially")
    parser.add_argument("--goal-inverted-probability", type=float, default=0.45, help="gene inverted in the goal")
    args = parser.parse_args(argv)
    try:
        problem = make_problem(**vars(args))
    except ValueError as error:
        parser.error(str(error))
    print(problem, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
