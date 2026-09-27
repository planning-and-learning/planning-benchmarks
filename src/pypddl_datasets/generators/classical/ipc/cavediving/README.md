# cavediving (ipc)

Divers lay chains of air tanks through a tree-shaped cave to photograph objectives, and must not work with divers they distrust.

## Source

- **Domain:** Nathan Robinson, Christian Muise, Charles Gretton, IPC 2014
- **Generator:** `pddl-generators/cavediving/generator/generator.py` (same authors; ISC-style license, notice kept in `generator.py`), ADL mode with ordered tanks; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/cavediving-14-adl`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `cave_branches` | depths of the cave branches (first = deepest) | 1–3 branches, depths 2–4 |
| `objectives` | depths of the photographed leaves | 1–2 objectives, depths 2–4 |
| `neg_link_prob` | probability that a diver pair precludes each other | 0.5 |
| `perturb_hiring_costs` | relative noise on hiring costs | about 0.1 |
| `min_hiring_cost`, `max_hiring_cost`, `other_action_cost` | cost range and cost of other actions | 10, 100, 1 |

## Distribution

### Objects
Locations `l0..` (a tree), divers `d0..` (2^(d−1) per objective at depth d), tanks `t0..` (2^(d+1) per objective, minus one) plus `dummy`, quantities `zero..four`.

### Initial state
- The first branch runs from the entrance `l0`; each further branch starts at a uniform node shallower than its depth. `connected` both ways.
- Every diver `available` with capacity `four`; tanks in an ordered `next-tank` chain, the first one in storage.
- Diver pairs that aren't in the helper chain (divers bringing tanks to the next diver) preclude each other with `neg_link_prob`.
- Hiring costs rank the divers by number of precludes (fewer precludes, higher cost), perturbed by `perturb_hiring_costs`; `other-cost` and `total-cost 0`.

### Goal
`have-photo` at each objective leaf (uniform among the leaves at its depth), and every diver `decompressing`.

### Other
`(:metric minimize (total-cost))`. Exactly the tanks and divers needed (upstream's adjustments are 0 in the IPC tasks); no negative cycles, so tasks are solvable. Name `cave-diving-adl-b<branches>-o<objectives>-s<seed>` unless `name` is given.

## Comparison with reference tasks

All 20 IPC tasks regenerated at their own branch and objective depths (20 seeds each, `perturb_hiring_costs=0.1`):

| aspect | reference tasks | this generator |
|---|---|---|
| tanks, divers, goals | formula | same formula (20/20) |
| `connected` facts | 7.30 | 7.36 |
| `precludes` facts | 4.60 | 4.26 |
| mean hiring cost | 39.7 | 43.0 |

**Deviations:** none found; the perturbation used for the IPC tasks isn't recorded, 0.1 is upstream's README example.
