# flashfill (ipc)

Synthesize a string-transformation program (Excel flash fill) as a planning program: the plan writes program lines that must map every example input to its output.

## Source

- **Domain:** Javier Segovia-Aguas (IPC 2018), planning programs compilation (Segovia-Aguas, Jiménez, Jonsson, ICAPS 2016)
- **Generator:** example generators `domains/excel_variables/gen0{1,2,4,5}.py` of Autoscale's `pddl-generators/flashfill` (Javier Segovia-Aguas), ported; the compiled domain is rebuilt from per-family skeletons (`skeleton-*.pddl.gz`, IPC domains with the example-dependent parts cut out) instead of the C++ compiler
- **Reference tasks:** `data/classical/downward-benchmarks/flashfill-sat18-adl` (one domain file per task)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `family` | `add-paren`, `extract-minutes`, `first-last-initial`, `initials` | 5 tasks each |
| `num_tests` | number of examples | 2–5 |
| `min_size`, `max_size` | example string length (name and surname lengths are equal) | 3–7 (extract-minutes: 7 characters) |
| `seed` | random seed | — |

## Distribution

### Objects
None in the problem; the domain declares the used characters and limiters, `str` (and `str2`), `res`, indices `i0..` up to the longest example + 1, input variables and two stack rows as constants.

### Initial state
Example 0: input string(s) with `hiindex`, `loindex`, `size`, `input-assignment`, the `next` chain, one `assignment` per character (extract-minutes keeps upstream's extra `(assignment str i0 lpar)`); `(test-0)`, the stack's first row, and `empty-l` for every program line (7, 7, 8 and 6 lines per family).

### Goal
`(done-programming)`: reached after the program produced every example's output; example k's output is checked by `repeat-end-main-k-*`, which loads example k+1.

### Other
`(:metric minimize (total-cost))`. Characters are uniform lowercase letters (add-paren, first-last-initial, initials) or random time digits (extract-minutes: hour 0–9, minutes and seconds 0–59). The program-line count is fixed per family (the IPC one); other line counts need a port of the planning-programs compiler.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| domains rebuilt from each task's own examples | 20 | 20 byte-identical (problems identical up to a final newline) |
| example lengths 3/4/5/6/7 (non-extract families) | 6/4/3/2/1 of 16 | uniform |
| tests per task | 2, 2, 3, 4, 5 per family | parameter |

**Deviations:** example lengths are uniform in [3, 7] while the IPC examples lean short (mean 4.25 vs 5); problem names differ.
