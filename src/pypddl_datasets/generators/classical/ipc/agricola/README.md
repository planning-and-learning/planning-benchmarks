# agricola (ipc)

A single-player simplification of the Agricola board game: workers take action cards each round to gather food and resources, grow the family and survive the harvests.

## Source

- **Domain:** Tomas de la Rosa (Universidad Carlos III de Madrid), IPC 2018
- **Generator:** pddl-generators `agricola/GenAgricola.py` by Tomas de la Rosa; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/agricola-opt18-strips`, `data/classical/downward-benchmarks/agricola-sat18-strips` (identical domain files; `domain.pddl` is that file, lowercased)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `last_stage` | stage whose harvest must end (goal) | opt: 3–9, sat: 3–12 |
| `num_workers` | worker/room objects; family size limit | opt: 4–6, sat: 5–10 |
| `must_create_workers` | goal also requires `num_workers` workers | opt: never, sat: p11–p20 |
| `num_ints` | minimum number of integer objects | 16 (default; raised to `2 + 2 * num_workers`) |
| `seed` | random seed | – |

## Distribution

### Objects
`num1..numN` with `N = max(num_ints, 2 + 2 * num_workers)` (plus constant `num0`), `stage1..stage(last_stage+1)`, `round1..roundK` where `K = h(last_stage) + 1` and the harvest rounds are `h = 4, 7, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20`, `worker1..workerW` and `room1..roomW` for `W = num_workers`. Action cards, goods and phases are domain constants.

### Initial state
Fixed: the number chain (`next_num`, `next2_num`, `num_substract` for all `0 ≤ j ≤ i ≤ N`), stage/round/worker chains (`worker1 → noworker`), round categories (normal rounds 1, 2, 3, 5, 6, 8, 10, 12, the rest harvest), the eight always-open cards, all sixteen `available_action` cards, `food_required` of 2k and 2k+1 for worker k ≥ 2, two workers in two built rooms, `space_rooms` for rooms 3..W, resource supplies, and `group_worker_cost` 60, 30, 15, 6, 4 (for W ≤ 6; larger W prepend +30 steps, e.g. 180 … 4 for W = 10), `(= (total-cost) 0)`.
Random: the four stage-1 round cards (fences, sheep, sow, family) are a uniform permutation over rounds 1–4 and the first one is open from the start; the four stage-2 cards (improve, carrot, boar, cattle) are a uniform permutation over rounds 5–8; rounds ≥ 9 draw `void`; initial food is uniform in 0..3.

### Goal
`(harvest_phase stage<last_stage> harvest_end)`, plus `(max_worker worker<num_workers>)` when `must_create_workers`.

### Other
Action costs, `(:metric minimize (total-cost))`. Problem name `agricola-[allworkers-]<last_stage>-<num_workers>`. Upstream warns that tasks may be unsolvable (e.g. the family starves at a harvest); there is no solvability check, as upstream.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| all objects, init and goal facts except the random draws (40 tasks, generated with the task's parameters) | – | identical in 40/40 tasks |
| initial food 0/1/2/3 | 11/10/10/9 of 40 | 24.8/25.3/25.3/24.6 % (4000 seeds) |
| first open round card fences/sheep/sow/family | 17/10/8/5 of 40 | 24.9/24.8/25.2/25.1 % |
| `(= (total-cost) 0)` in init | 40/40 | always |

**Deviations:**
- Upstream `GenAgricola.py` omits `(= (total-cost) 0)`; the IPC tasks (and this port) contain it.
- Problem names differ (`opt01-3-4` / `sat31-allworkers-3-5` in the IPC; `agricola-3-4` / `agricola-allworkers-3-5` here).
- The IPC first-card counts are uneven (17 of 40 fences; χ² = 7.8, 3 d.o.f., p ≈ 0.05), presumably an artifact of the consecutive seeds used upstream; the generator draws uniformly like upstream.
