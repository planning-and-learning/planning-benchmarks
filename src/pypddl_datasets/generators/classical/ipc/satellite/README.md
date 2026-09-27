# satellite (ipc)

Satellites with instruments must be turned, powered and calibrated to take images of directions in given modes.

## Source

- **Domain:** Maria Fox and Derek Long, IPC 2002 (untyped STRIPS encoding with type predicates)
- **Generator:** `satellite/satgen.cc` (IPC 2002, Long and Fox), STRIPS mode, without Autoscale's 2021 patches; Python port in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/satellite`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_satellites` | satellites | 1–15 |
| `max_instruments` | maximum instruments per satellite | 3 (larger in a few hand-scaled tasks) |
| `num_modes` | modes | 3–10 |
| `num_targets` | calibration directions (also allowed as start or pointing directions) | 3–5 |
| `num_observations` | observable directions | 4–250 |
| `typed` | Autoscale's typed encoding instead of type predicates | IPC: off |
| `patched` | Autoscale's 2021 patches (all observations interesting, all modes supported) | IPC: off |

## Distribution

### Objects
- Satellites and instruments; modes `<type><i>` with type uniform in infrared, image, spectrograph, thermograph.
- Targets `star<i>` or `groundstation<i>`, then observations `star<i>`, `phenomenon<i>` or `planet<i>`; each name kind uniform.
- Untyped: kinds are given by `satellite`, `instrument`, `mode` and `direction` facts.

### Initial state
- Each satellite gets 1+rnd(`max_instruments`) instruments; each instrument supports 1+rnd(3) distinct uniform modes and has 1+rnd(T/3) distinct uniform calibration targets.
- Every satellite has `power_avail` and points at a uniform direction.
- Modes that no instrument supports stay unsupported (upstream before 2021).
- Fact order as in the IPC tasks: per satellite its type fact, per instrument its type, `supports` and `calibration_target` facts, then the satellite's `on_board`, `power_avail` and `pointing`; finally all `mode` and `direction` facts.

### Goal
- Each observation is interesting with probability 9/10; an interesting observation gets 1+rnd(M/3) distinct uniform `have_image` modes.
- Each satellite has a `pointing` goal to a uniform direction with probability 2/5.

### Other
- No action costs. The problem is named `satellite-s<S>-i<I>-m<M>-t<T>-o<O>`.
- As upstream before 2021, an image goal may need an unsupported mode, which makes the task unsolvable; it is rare (2% of modes are unsupported in both the IPC tasks and this generator).

## Comparison with reference tasks

All 36 IPC tasks, each regenerated at its inferred S, M, T and O with `max_instruments=3` (10 seeds):

| aspect | reference tasks | this generator |
|---|---|---|
| instruments per satellite | 2.26 | 1.98 |
| modes per instrument | 2.02 | 1.98 |
| calibration targets per instrument | 1.00 | 1.00 |
| observations with an image goal | 0.89 | 0.89 |
| modes per observation goal | 1.04 | 1.04 |
| pointing goals per satellite | 0.34 | 0.36 |
| unsupported modes | 0.02 | 0.02 |

**Deviations:**
- Instruments per satellite: IPC has 73 / 73 / 100 satellites with 1 / 2 / 3 instruments, ours is uniform (about 86 / 82 / 79 when regenerated with each task's own maximum; mean 2.26 vs 2.11). A few large IPC tasks have up to 10 instruments, reproducible only via `max_instruments`.
- Problem names encode the parameters (IPC: `strips-sat-x-1`).
