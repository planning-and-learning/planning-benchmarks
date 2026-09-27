# satellite (autoscale)

Satellites with instruments must be turned, powered and calibrated to take images of directions in given modes.

## Source

- **Domain:** Maria Fox and Derek Long, IPC 2002 (typed STRIPS version shipped with Autoscale)
- **Generator:** `satellite/satgen.cc` (IPC 2002, Long and Fox) with Autoscale's June 2021 patches, called as `satgen {seed} {satellites} 3 {modes} {targets} {observations}`. This package re-exports `../../ipc/satellite` with `typed=True, patched=True`.
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/satellite` (also `21.11-optimal-strips/satellite`)

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_satellites` | satellites | 2–57 |
| `max_instruments` | maximum instruments per satellite | 3 |
| `num_modes` | modes | 3 |
| `num_targets` | calibration directions (also allowed as start or pointing directions) | 12–278 |
| `num_observations` | observable directions | 5–60 |

## Distribution

### Objects
Same as `ipc/satellite`, declared with types `satellite`, `instrument`, `mode` and `direction`.

### Initial state
- Same as `ipc/satellite`, without type facts.
- Patch: modes that no instrument supports are added to a uniform instrument of a uniform satellite.

### Goal
- Patch: every observation is interesting and gets 1+rnd(M/3) distinct uniform `have_image` modes.
- Each satellite has a `pointing` goal to a uniform direction with probability 2/5.

### Other
- No action costs. The problem is named `satellite-s<S>-i<I>-m<M>-t<T>-o<O>`.
- Every image goal is achievable: all modes are supported and every instrument has a calibration target.

## Comparison with reference tasks

All 30 agile tasks, regenerated at their inferred S, maximum instruments, M, T and O:

| aspect | reference tasks | this generator |
|---|---|---|
| instruments per satellite | 2.05 | 1.99 |
| modes per instrument | 2.05 | 2.02 |
| calibration targets per instrument | 24.67 | 24.58 |
| image goals per goal direction | 1.00 | 1.00 |
| interesting observations | 1.00 | 1.00 |
| pointing goals per satellite | 0.38 | 0.41 |
| groundstations per task | 72.8 | 70.9 |

**Deviations:** none found.
