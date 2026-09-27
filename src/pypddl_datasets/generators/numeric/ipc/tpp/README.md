# tpp (numeric/ipc)

A truck buys goods at markets with prices and limited supplies and returns to the depot.

## Source

- **Domain:** TPP Metric, IPC 2006 (Alfonso Gerevini and Alessandro Saetti); tasks by Enrico Scala and Miquel Ramirez for IPC 2023
- **Generator:** reconstruction from the reference tasks; no generator for this encoding is published (`pddl-generators/tpp` has no metric mode)
- **Reference tasks:** `data/numeric/ipc2023/tpp`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_markets` | markets | 5–40 |
| `num_goods` | goods | 2–39 |
| `num_depots` | depots | 1 |
| `num_trucks` | trucks | 1 |

## Distribution

### Objects
`market1..`, `depot0..`, `truck0..`, `goods0..`.

### Initial state
- Each good is on sale at each market with probability 0.525, quantity uniform in 1..20 and price uniform in 1..50 (redrawn until some market sells it); otherwise `on-sale` 0 and no price.
- Places uniform in a 1000 × 1000 square; every ordered pair of places has the Euclidean distance (2 decimals) as `drive-cost`.
- Trucks at the first depot; `bought` 0, `request` uniform in 1..total supply of the good; `total-cost` 0.

### Goal
`(>= (bought g) (request g))` for every good and every truck back at the first depot.

### Other
`(:metric minimize (total-cost))`. Always solvable (every request is below the total supply).

## Comparison with reference tasks

All 20 tasks regenerated at their market and goods counts, 5 seeds each:

| aspect | reference tasks | this generator |
|---|---|---|
| on-sale share | 0.539 | 0.521 |
| mean price | 24.9 | 25.3 |
| median request / supply | 0.50 | 0.50 |
| median drive cost | 515 | 507 |
| max drive cost | 1098 | 1131 |

**Deviations:**
- The IPC tasks share one fixed map (the same places have the same costs in every task); this generator draws a map per seed.
- The IPC map is not uniform in a square (it spans about 900–1000 per side); the side 1000 is a fit.
