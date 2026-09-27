# freecell (autoscale)

Solitaire: move all cards home suit by suit using free cells and empty columns.

## Source

- **Domain:** Fahiem Bacchus (AIPS-2000), typed pddl-generators version (`freecell/domain.pddl`)
- **Generator:** port of `pddl-generators/freecell/freecell.c` (Jörg Hoffmann, FF domain collection; Freiburg notice, see `LICENSES/LicenseRef-Freiburg.txt`); Python port in `generator.py`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-{agile,optimal}-strips/freecell` (60 tasks, parameters in the task names)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_cells` | free cells | 2–4 |
| `num_columns` | columns | 3–8 |
| `num_stacks` | initial stacks the cards are dealt onto | 1–8 |
| `suit_size` | cards per suit (all suits equal) | 3–18 |
| `num_suits` | suits | 4 |

## Distribution

### Objects
Cards `c0 ca c2 ...` per suit (the `x0` card is the empty home), `celln0..cellnN`, `coln0..colnC`, `n0..nK`, suits `c h s d`.

### Initial state
- Static: `value`, `successor`, `cellsuccessor`, `colsuccessor`, `hassuit`, and `canstack` for card i onto the next-higher card of the two opposite-colour suits (aces excluded), as upstream.
- Deal: repeatedly a uniform suit with undealt cards, a uniform undealt card of it, onto a uniform one of `num_stacks` stacks; a stack may stay empty.
- `home x0` per suit, `cellspace celln<cells>`, `colspace coln<columns - stacks>` (even if a stack stayed empty, as upstream).

### Goal
Every suit's top card home.

### Other
No action costs. Problem name `freecell-f<cells>-c<cols>-s<suits>-i<stacks>-<suit><size>...`, as upstream. Solvability is not checked (neither upstream).

## Comparison with reference tasks

All 60 Autoscale tasks regenerated at the parameters in their names (10 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| objects, static facts, goal | — | identical in 60/60 |
| non-empty initial stacks | 296 / 298 | 297 / 298 |
| mean highest stack | 13.38 | 13.59 |
| mean stack-height std. dev. | 2.34 | 2.55 |

**Deviations:** only one suit size for all suits (every Autoscale task uses equal sizes); problem fact order and line breaks differ.
