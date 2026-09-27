# data_network (autoscale)

Servers in a network produce data items by running scripts on inputs and send them between servers, minimizing total cost.

## Source

- **Domain:** Manuel Heusner, Florian Pommerening, Alvaro Torralba, IPC 2018 (same domain file as the IPC)
- **Generator:** `data-network/generator/generator.py` (Manuel Heusner), called by Autoscale as `generator.py {items} {layers} {scripts} {network} {seed}`; `generator.py` re-exports `../../ipc/data_network`
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/data-network`, `data/classical/autoscale-benchmarks-main/21.11-optimal-strips/data-network`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_items` | data items (Autoscale: `layers + extra_items`) | agile: 12-65 |
| `num_layers` | layers | agile: 3-4 (Autoscale enum 2-6) |
| `num_scripts` | scripts (Autoscale: `max(1, items - 2) + extra_scripts`) | agile: 52-188 |
| `network` | server network | agile: `ring-network` only (Autoscale enum tiny/small/ring) |
| `seed` | random seed | agile: 2019-2048 |

## Distribution

### Objects
The same as `ipc/data_network`.

### Initial state
The same as `ipc/data_network`: layered production scripts, data sizes uniform in 1..5, layer-0 items saved on random servers, and costs fixed by the network module.

### Goal
Every item no script consumes is saved on a uniformly random server.

### Other
Action costs with a `total-cost` metric. Problem name `p{items}-{layers}-{scripts}-{network}-{seed}`, the same scheme as Autoscale. Solvable by construction.

## Comparison with reference tasks

30 agile tasks, each generated at its own parameters and seed:

| aspect | reference tasks | this generator |
|---|---|---|
| objects: data / scripts / servers / numbers | 1154 / 3685 / 210 / 510 | identical |
| init `script-io` / `process-cost` / `send-cost` / `io-cost` | 3685 / 25795 / 3552 / 1036 | identical |
| init `saved` | 383 | 376 |
| init `sum` | 2073 | 2069 |
| goal `saved` | 340 | 347 |
| metric | 30 | 30 |

**Deviations:**
- None structural. The remaining gaps are in counts that depend on the random draws, and they are within noise.
