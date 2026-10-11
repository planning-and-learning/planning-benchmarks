# ged (autoscale)

Genome edit distance: turn one signed circular genome into another with transpositions, inverted transpositions and inversions (ITT operations), each split into cut and splice steps, at minimum total cost.

## Source

- **Domain:** IPC 2014 (`ged-{opt,sat}14-strips`); the domain file names no author. Autoscale's copy (identical to IPC's), lowercased outside comments
- **Generator:** Autoscale has none (`tasks-of-domains-without-usable-generator/ged`: the IPC tasks plus the `ds1` and `ds2nd` sets from Patrik Haslum's website); re-exports `../../ipc/ged`, a reconstruction from the IPC tasks
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/ged` (30 `ds1` tasks: 36-gene genomes, 5–36 objects) and `21.11-optimal-strips/ged` (30 tasks: 19 IPC, 6 `ds1`, 5 `ds2nd`; 3–22 objects)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_genes` | genes (objects) after compression | agile: 5–36, optimal: 3–22 (generator: at least 4) |
| `init_inverted_probability` | a free gene is inverted in the initial genome | default 0.08 (IPC); 0.21 matches agile |
| `goal_inverted_probability` | a free gene is inverted in the goal genome | default 0.45 (IPC); 0.25 matches agile |

## Distribution

### Objects
`g1..g<num_genes>`.

### Initial state
The genome `g1..gn` as a `cw` cycle with random orientations (`g1` normal), `present` for every gene, `(idle)`, `(= (total-cost) 0)`.

### Goal
Orientation of every gene and the `cw` cycle of the goal genome: `g1` first, `gn` last, the rest in random order with random orientations, sharing no adjacency with the initial genome except the seam `gn g1`.

### Other
Metric `minimize (total-cost)`. Name `ged-g<num_genes>`. See `../../ipc/ged`.

## Comparison with reference tasks

Every Autoscale task regenerated at its own object count (20 seeds; 3-object tasks at 4):

| aspect | agile reference | generator (0.21 / 0.25) | optimal reference | generator (defaults) |
|---|---|---|---|---|
| objects | 29.33 | 29.33 | 8.80 | 8.83 |
| inverted share, initial / goal | 0.193 / 0.215 | 0.192 / 0.235 | 0.092 / 0.259 | 0.057 / 0.343 |
| genes whose orientation changes | 0.339 | 0.326 | 0.265 | 0.338 |
| shared adjacencies | 0.23 | 1 | 0.93 | 1 |

**Deviations:**
- As in `../../ipc/ged` (random genomes, plain `g<i>` names, at least 4 genes).
- The goal always keeps the last gene, so exactly one adjacency (the seam) is shared. Both genomes end with the same gene in all 40 IPC tasks and in 28 of the 30 optimal tasks, but only in 7 of the 30 agile (`ds1`) tasks.
