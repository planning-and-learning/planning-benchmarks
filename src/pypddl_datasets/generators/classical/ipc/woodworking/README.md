# woodworking (ipc)

Boards are cut into parts, which are planed, ground, varnished or glazed and coloured on machines.

## Source

- **Domain:** IPC 2008 Woodworking (authors not named in the domain or generator files); `domain.pddl` is the IPC 2011 file (identical to the 2008 ones up to case and comments), whose `cut-board` actions keep the old `boardsize`
- **Generator:** port of `pddl-generators/woodworking/create_woodworking_instance.py` (the IPC 2008 generator); Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/woodworking-{opt,sat}{08,11}-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_parts` | parts | 3–39 |
| `num_machines` | machines of each of the 7 kinds | 1 or 3 |
| `wood_factor` | available board wood relative to the parts' needs | 1.0, 1.2, 1.4 |

## Distribution

### Objects
7 machine kinds × `num_machines`; `max(round(0.7·parts), 2)` colours and `max(round(0.25·parts), 2)` woods sampled from fixed lists; `num_parts` parts; boards and board sizes derived from the wood demand.

### Initial state
- Each part is `unused` with probability 4/5, otherwise `available` with a random treatment, surface and colour (wood fixed by the goal), redrawn until the goal is not already satisfied.
- Part sizes uniform 1–3; for each wood the unused parts' sizes plus `(wood_factor − 1)` extra wood are packed into boards; board surfaces rough with probability 3/4.
- Colours are assigned to spray-varnishers and glazers so every needed colour is available; costs per part size (`spray-varnish-cost`, `glaze-cost`, `grind-cost`, `plane-cost`).

### Goal
Per part `available` plus a random subset (size 2, 2, 2, 3 or 4 uniformly) of treatment, surface, colour and wood, drawn uniformly.

### Other
Action costs with `(:metric minimize (total-cost))`. Name `wood-prob`. Header comment with parts, wood percentage and machines, like IPC.

## Comparison with reference tasks

All 100 IPC tasks, 5 distinct seeds per task at its parameters.

| aspect | reference tasks | this generator |
|---|---|---|
| colours | 5.24 | 5.24 |
| wood types | 3.66 | 3.57 |
| boards | 5.13 | 5.11 |
| parts initially available | 0.58 | 0.62 |
| parts with colour goal | 0.64 | 0.66 (0.64–0.73 per suite) |
| parts with wood goal | 0.65 | 0.63 |
| parts with surface goal | 0.66 | 0.66 |
| parts with treatment goal | 0.65 | 0.66 |

**Deviations:**
- Distribution: none found beyond sampling noise.
