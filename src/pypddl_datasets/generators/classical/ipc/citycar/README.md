# citycar (ipc)

Roads are built and demolished on a junction grid so that cars get from their garages to their destinations.

## Source

- **Domain:** Mauro Vallati (University of Huddersfield), IPC 2014
- **Generator:** `pddl-generators/citycar/generator.py` (Mauro Vallati; `--density` added by Masataro Asai); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/citycar-opt14-adl` (domain `domain_citycar14opt.pddl`), `data/classical/downward-benchmarks/citycar-sat14-adl` (domain `domain.pddl`; adds `(not (= ?xy_initial ?xy_final))` preconditions). Both accept the same problems.

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_rows`, `num_columns` | junction grid | 2×2–4×4 |
| `num_cars` | cars | 2–6 |
| `num_garages` | garages | 1–3 |
| `density` | probability that an interior junction is usable | 1.0 |

## Distribution

### Objects
Junctions `junction<r>-<c>`, cars, garages and `num_rows + 2` roads.

### Initial state
- `same_line` for horizontal and vertical neighbours and `diagonal` for diagonal neighbours, both directions.
- `clear` for every junction; with `density < 1` each interior junction is clear only with that probability.
- Each garage at a uniform junction of row 0; each car `starting` in a uniform garage; `(= (total-cost) 0)`.

### Goal
Every car `arrived` at a uniform junction of the last row.

### Other
`(:metric minimize (total-cost))` (building 20/30, demolishing 10, moving 1). Name `citycar-<rows>-<columns>-<cars>`, like upstream.

## Comparison with reference tasks

All 40 IPC tasks regenerated at the parameters in their file names (opt `p<rows>-<columns>-<cars>-<garages>-<seed>`, sat `p<size>-<cars>-<garages>-<sparse>-<seed>`):

| aspect | reference tasks | this generator |
|---|---|---|
| init fact-kind counts | — | identical in 40/40 |
| roads | `rows + 2` (39/40) | `rows + 2` |
| garage rows / goal rows | 0 / last | 0 / last |

**Deviations:**
- The draws differ: the IPC tasks predate the Python 3 port, so no task is reproduced exactly.
- opt `p2-2-2-1-2` declares no roads at all, which makes it unsolvable; this generator always declares `rows + 2`.
