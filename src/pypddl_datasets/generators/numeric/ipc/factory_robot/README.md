# factory_robot (numeric/ipc)

Robots with energy, heat and production modes move between factory stations to accumulate workload.

## Source

- **Domain:** Joan Espasa Arxer, IPC 2026 numeric track
- **Generator:** reconstruction of `generate.py`, whose calls the IPC tasks record (`--robots R --stations S --workload W --max-temp T --seed 42`) but which was not published; Python in `generator.py`
- **Reference tasks:** `data/numeric/ipc2026/factory-robot`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_robots` | robots | 2–12 |
| `num_stations` | stations (default robots + 3) | 5–14 |
| `workload` | target workload per robot (± 2) | 40–130 |
| `max_temp` | temperature bound | 20–50 |

## Distribution

### Objects
Robots `r0..`; stations `charging`, `cooling`, `assembly0..`.

### Initial state
- Complete station graph; `has-charger charging`, `has-calibrator cooling`; `cooling-power` 4 or 6 at `cooling`, 0 elsewhere.
- Robots on distinct random stations, the rest `free`; all `calibrated`; workload, temperature and production 0.
- Per robot: capacity ∈ {80, 100, 120, 150}, energy = capacity − U(0..20), work-cost ∈ {8, 10, 12, 15}, max-temp = `max_temp` + U(0..5), efficiency U(2..4).

### Goal
Workload ≥ `workload` + U(−2..2) for every robot; temperature of `r0` ≤ `max_temp`.

### Other
No metric, as in the IPC tasks. Solvable: turbo work has no temperature precondition, `charging` recharges, and at least two stations are always free; name `factory-<R>r-<S>s`.

## Comparison with reference tasks

Regenerated at each IPC task's call (3 seeds each):

| aspect | reference tasks | this generator |
|---|---|---|
| value sets: capacity / work-cost / efficiency / max-temp offset / goal offset | {80,100,120,150} / {8,10,12,15} / 2–4 / 0–5 / −2..2 | same sets |
| mean capacity | 95.0 | 112.5 |
| mean energy gap to capacity | 9.1 | 11.6 |
| mean work-cost | 10.1 | 11.0 |

**Deviations:** the IPC generator draws capacities 80 and work-cost 8/10 more often (all 20 tasks use seed 42, so the value per robot index repeats); here values are uniform over the same sets.
