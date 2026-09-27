# markettrader (numeric/ipc)

A trader with a camel buys goods where they are cheap and sells them where they are expensive, to raise cash from 100 to 1000.

## Source

- **Domain:** Amanda Coles, Maria Fox and Derek Long, "A hybrid LP-RPG heuristic for modelling numeric resource flows in planning", JAIR 46 (2013); IPC 2023 numeric track
- **Generator:** reconstruction from the reference tasks (no generator was published with the IPC 2023 dataset, and none was found elsewhere)
- **Reference tasks:** `data/numeric/ipc2023/markettrader`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_markets` | number of markets | 2–5 |
| `seed` | random seed | — |

## Distribution

### Objects
`num_markets` markets drawn from the reference tasks' 59 city names, `camel0`, and the fixed 17 goods (Food … TuringMachines).

### Initial state
- Roads: a random spanning tree plus every other market pair with probability 0.5, symmetric `can-drive` with equal `drive-cost` uniform in 0.8..7.0 (one decimal).
- Per market and good: `price` uniform over the good's reference range (one decimal); `on-sale` 0 with the good's reference probability, else uniform over its reference range (e.g. TuringMachines never on sale, Minerals always 53–60).
- With probability 0.1 a market has no `price`/`on-sale` facts for Kittens and Gold, and with a third of that also Copper (undefined fluents, as in the reference tasks).
- `bought` 0 for every good, camel at the last market, `cash` 100, `capacity` 20, `fuel` 7.0, `fuel-used` 0.

### Goal
`(>= (cash) 1000)`.

### Other
No metric (the reference tasks comment out `minimize (fuel-used)`). Draws repeat until some road connects a market selling a good for at most 93 with a neighbour paying more by enough to cover the round trip at capacity 20, so repeated trading reaches the goal; all 20 reference tasks pass this check. The `sellprice` function is declared but never initialised, as in the tasks. Problem name `marketcount<num_markets>`.

## Comparison with reference tasks

Five seeds per reference task at its market count:

| aspect | reference tasks | this generator |
|---|---|---|
| road density (directed roads / M(M−1)) | 0.85 | 0.78 |
| share of `on-sale` facts that are 0 | 0.323 | 0.322 |
| mean drive cost | 4.67 | 4.02 |
| undefined good–market pairs per task | 0.55 | 0.45 |
| tasks with a profitable trade | 20 of 20 | all (by construction) |

**Deviations:**
- Prices are uniform per good; the reference tasks may correlate prices across markets.
- Drive costs are uniform; the references are slightly higher on average.
