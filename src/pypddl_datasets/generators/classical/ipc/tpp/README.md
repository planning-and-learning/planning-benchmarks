# tpp (ipc)

A traveling purchaser buys goods at markets with trucks and brings them to depots.

## Source

- **Domain:** Alfonso Gerevini and Alessandro Saetti, IPC 2006 (IPC-5), TPP-Propositional
- **Generator:** port of `pddl-generators/tpp/tpp.c` (gen-TPP by Alfonso Gerevini and Alessandro Saetti, the IPC-5 generator); Python port in `generator.py`. `../../autoscale/tpp` re-exports it.
- **Reference tasks:** `data/classical/downward-benchmarks/tpp`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_products` | goods (`-p`) | 1–20 |
| `num_markets` | markets (`-m`) | 1–8 |
| `num_trucks` | trucks (`-t`) | 1–8 |
| `num_depots` | depots (`-d`) | 1–3 |
| `max_level` | highest quantity level (`-l`) | 1–6 |
| `seed` | random seed | – |

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

All 30 IPC tasks, each compared with 20 generated tasks at its parameters (read off the task's objects).

| aspect | reference tasks | this generator |
|---|---|---|
| market–market roads (mean; p10 / p20 / p30) | 4.67; 2 / 5 / 12 | 5.83; 2 / 6 / 17.6 |
| depot links (mean) | 2.00 | 2.00 |
| share of `on-sale` at `level0` | 0.44 | 0.43 |
| highest `on-sale` level (mean) | 1.90 | 1.90 |
| goals at `max_level` | 0.37 | 0.34 |
| trucks start at a depot | yes | yes |
| names | problem `tpp` | problem `tpp-p…-m…-t…-d…-l…` |

**Deviations:**
- The largest tasks keep more market roads than IPC (p30: 17.6 vs 12); the road-cut count is uniform, and the IPC tasks sit at the sparse end.
- Problem name only otherwise.
