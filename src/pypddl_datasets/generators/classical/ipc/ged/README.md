# ged (ipc)

Genome edit distance: turn one signed circular genome into another with transpositions, inverted transpositions and inversions (ITT operations), each split into cut and splice steps, at minimum total cost.

## Source

- **Domain:** IPC 2014 (`ged-{opt,sat}14-strips`, split multi-step formulation with ITT operations only); the domain file names no author. Autoscale's README for its GED tasks says the further task sets come from Patrik Haslum's website (`ged.tar.bz2`)
- **Generator:** reconstruction from the IPC tasks. These are pairs of real mitochondrial genomes (105 genes), compressed by merging every adjacency the two genomes share into one `SUB<i>` object; no generator was published, so this draws synthetic genome pairs directly in compressed form
- **Reference tasks:** `data/classical/downward-benchmarks/ged-{opt,sat}14-strips` (40 tasks, 3–26 objects)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_genes` | genes (objects) after compression | 3–26 (generator: at least 4) |
| `init_inverted_probability` | a free gene is inverted in the initial genome | 0.08 (default; measured share 0.07) |
| `goal_inverted_probability` | a free gene is inverted in the goal genome | 0.45 (default; measured share 0.37) |

The defaults reproduce the IPC tasks' inverted shares (which include the fixed first and last gene).

## Distribution

### Objects
`g1..g<num_genes>`.

### Initial state
- The genome `g1..gn` as a `cw` cycle; `g1` normal, every other gene `inverted` with `init_inverted_probability`, else `normal`.
- `present` for every gene, `(idle)`, `(= (total-cost) 0)`. No `free`, `gone`, `duplicate` or `swappable` facts (ITT only), as in the IPC tasks.

### Goal
- `normal`/`inverted` for every gene and the `cw` cycle of the goal genome: `g1` (normal) first, `gn` (as initially) last, the genes in between in uniformly random order, each inverted with `goal_inverted_probability`.
- A goal genome that shares a signed adjacency (on either strand) with the initial genome, read linearly from `g1`, is redrawn (about 2 draws per task). So exactly one adjacency is shared, the seam `gn g1`, as in every IPC task: their compression is linear and both genomes start and end with the same gene.

### Other
Metric `minimize (total-cost)`. Name `ged-g<num_genes>`. Solvable: moving one gene is a transposition of a one-gene segment, so ITT reaches every cyclic order, and `invert-single-gene-{a,b}` fixes any orientation.

## Comparison with reference tasks

All 40 IPC tasks, each regenerated at its own object count (20 seeds; the three 3-object tasks at 4):

| aspect | reference tasks | this generator |
|---|---|---|
| objects | 13.45 | 13.53 |
| inverted share, initial / goal | 0.068 / 0.369 | 0.061 / 0.371 |
| genes whose orientation changes | 0.355 | 0.369 |
| shared adjacencies (both strands) | 1 (the seam) | 1 (the seam) |
| goal facts | one orientation per gene plus `n` `cw` | same |
| optimal cost (`astar(lmcut())`), n = 4 / 5 / 6 / 7 | 2.0 / 3.0 / 4.0 / 4.4 | 2.0 / 2.6 / 3.6 / 4.6 (5 seeds each) |

Larger generated tasks solve with `lama-first` (n = 12 / 24 / 36: cost 18 / 63 / 137), plans checked with VAL.

**Deviations:**
- Genomes are random signed permutations rather than real genomes related by a few rearrangements; at the same object count the optimal costs still agree within 0.4 (table).
- No `SUB<i>` objects or gene names (`I`, `Q`, `G97`, …): every object is a plain gene `g<i>`, and the initial genome is always `g1..gn` in order. Compressing generated genomes would only change names, since the drawn pair shares no adjacency besides the seam.
- At least 4 genes: with 3, fixed first and last genes leave one orientation choice, so a 0 or 1 goal probability could never avoid shared adjacencies. The IPC's three 3-object tasks have cost 1.
