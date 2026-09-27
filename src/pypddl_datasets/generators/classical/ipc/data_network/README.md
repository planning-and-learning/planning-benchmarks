# data_network (ipc)

Servers in a network produce data items by running scripts on inputs and send them between servers, minimizing processing, I/O and transfer cost.

## Source

- **Domain:** Manuel Heusner, Florian Pommerening, Alvaro Torralba, IPC 2018
- **Generator:** `data-network/generator/generator.py` (Manuel Heusner) with the `tiny-network`, `small-network` and `ring-network` modules; Python port in `generator.py` (numpy RNG replaced by `random.Random`)
- **Reference tasks:** `data/classical/downward-benchmarks/data-network-opt18-strips`, `data/classical/downward-benchmarks/data-network-sat18-strips`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_items` | data items | 5-56 |
| `num_layers` | layers of the production DAG (< `num_items`) | 3 |
| `num_scripts` | scripts (>= `num_items - 2`) | 10-119 |
| `network` | server network module | `tiny-network`, `small-network`, `ring-network` |
| `seed` | random seed; IPC names end with it | 0-39 |

## Distribution

### Objects
Data items `data-{layer}-{i}`, scripts `script{i}`, the servers of the chosen network, and `number{k}` counters up to the largest server capacity.

### Initial state
- Items are spread over the layers, with at least one item per layer and two on layer 0.
- Data sizes are uniform in 1..5.
- Layer-0 items are `saved` on uniformly random servers.
- Each item on layer k > 0 is the output of a script. The script takes one input from layer k-1 and a different input from any lower layer.
- The remaining scripts are random extra producers.
- The network module fixes server capacities, `usage`, `connected` links, `send-cost`, `io-cost` and `process-cost`. `sum` and `less-equal` tables cover the numbers.

### Goal
Every item that no script consumes must be `saved` on a uniformly random server.

### Other
- Action costs, with `(= (total-cost) 0)` and `(:metric minimize (total-cost))`.
- Problem name `p{items}-{layers}-{scripts}-{network}-{seed}`, the same scheme as IPC.
- Every goal item can be produced from layer 0 by construction, so tasks are solvable.

## Comparison with reference tasks

Generated at each IPC task's own parameters and seed (40 tasks):

| aspect | reference tasks | this generator |
|---|---|---|
| problem names | 40 | 40 identical |
| objects: data / scripts / servers / numbers | 818 / 1587 / 200 / 680 | 818 / 1587 / 200 / 680 |
| init `script-io`, `connected`, `process-cost`, `less-equal`, `capacity` | 1587, 544, 8085, 960, 200 | identical |
| init `saved` (layer 0) | 302 | 299.1 +- 9.9 (20 seeds) |
| data sizes 1/2/3/4/5 | 161 / 165 / 144 / 170 / 178 | 167 / 161 / 162 / 165 / 162 (mean of 20 seeds) |
| goal `saved` | 288 | 265.4 +- 12.9 (20 seeds; range 236-288) |
| metric | 40 | 40 |

**Deviations:**
- None structural.
- The IPC goal count (288) sits at the top of our 20-seed range, 1.8 sd above the mean. That is consistent with seed noise, but it is the largest gap.
