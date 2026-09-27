# tpp (autoscale)

A traveling purchaser buys goods at markets with trucks and brings them to depots.

## Source

- **Domain:** Alfonso Gerevini and Alessandro Saetti, IPC 2006 (IPC-5), TPP-Propositional
- **Generator:** `pddl-generators/tpp/tpp.c` (gen-TPP by Alfonso Gerevini and Alessandro Saetti) as called by Autoscale: `tpp -s <seed> -m <markets> -p <products> -t <trucks> -d <depots> -l <goods>`. `generator.py` re-exports `../../ipc/tpp`; the domain files agree up to comments.
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/tpp` (also `21.11-optimal-strips/tpp`)

## Parameters

| parameter | meaning | reference range (`domains.py`; agile tasks) |
|---|---|---|
| `num_products` | goods (`-p`) | 2–20 + slope; 2–31 |
| `num_markets` | markets (`-m`) | 1–10; 3 |
| `num_trucks` | trucks (`-t`) | 2–10; 2–13 |
| `num_depots` | depots (`-d`) | 1–10; 1–64 |
| `max_level` | highest quantity level (`-l`, "goods") | 3–10; 7–12 |

## Distribution

### Objects
`goods1..`, `truck1..`, `market1..`, `depot1..`, `level0..level<max_level>`.

### Initial state
- Roads: start from the complete market graph, attempt a uniform number (1..#edges) of random road cuts, keeping a cut only if the markets stay connected; each depot is linked to one uniform market.
- Supply: per product, each market (in order) sells it with probability 1/2 (one uniformly chosen market always does) at a level uniform in 1..`ceil(max_level / (markets // 2))`, capped so the total reaches at most `max_level`; other markets sell at `level0`.
- Trucks at uniform depots; `stored`/`loaded`/`ready-to-load` at `level0`; `next` chain.

### Goal
Per product `stored` at a level uniform in 1..min(total supply, `max_level`).

### Other
No costs or metric. Name `tpp-p<P>-m<M>-t<T>-d<D>-l<L>`. Always solvable (goal ≤ supply, connected roads).

## Comparison with reference tasks

All 30 agile tasks, generated at their parameters.

| aspect | reference tasks | this generator |
|---|---|---|
| market–market roads | 2.0 | 2.0 |
| depot links | 32.4 | 32.4 |
| share of `on-sale` at `level0` | 0.42 | 0.42 |
| highest `on-sale` level | 8.87 | 9.05 |
| goals at `max_level` | 0.06 | 0.07 |
| trucks start at a depot | yes | yes |

**Deviations:** none found. The same generator also matches the IPC tasks closely (see `ipc/tpp`).
