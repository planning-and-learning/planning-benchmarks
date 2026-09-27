# schedule (ipc)

Parts must be reshaped, polished and painted on a set of machines, with a time-step operator that frees the machines.

## Source

- **Domain:** a variant from Manuela Veloso's Prodigy collection, prepared for AIPS-2000 by Fahiem Bacchus (ADL: conditional effects and universal preconditions)
- **Generator:** derived from `schedule.c` in Jörg Hoffmann's FF domain collection (© 2001 Albert Ludwigs University Freiburg, see the file header), rewritten to follow the IPC tasks, which `schedule.c`'s distribution does not produce; Python code in `generator.py`
- **Reference tasks:** `data/classical/downward-benchmarks/schedule`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_parts` | parts, and number of goal facts | 2–51 (3 tasks per size) |

## Distribution

### Objects
Parts named `a0 b0 … z0 a1 …` over the 23 letters `abcdefghijklmnoqprsuvwz` (as in IPC), shapes `circular oblong`, colours `blue yellow red black`, widths `one two three`, orientations `back front`.

### Initial state
- Every part draws a uniform shape (cylindrical, circular, oblong), a uniform surface (polished, rough, smooth), a uniform paint colour, and one hole of uniform width and orientation; all parts start `cold`.
- Both painters have every colour; the drill press and the punch have every width and orientation.

### Goal
Exactly `num_parts` goal facts: distinct (part, kind) pairs drawn uniformly from all pairs whose goal does not hold yet. A kind is "cylindrical" (only for non-cylindrical parts), "surface" (a uniform different surface) or "paint" (a uniform different colour). There are no hole goals, so a part gets 0–3 goals.

### Other
- No action costs.
- The problem is named `schedule-<P>`.
- Every goal is achievable, since the machines can produce any of these values.

## Comparison with reference tasks

Measured over all 150 IPC tasks and 150 generated tasks with the same part counts:

| aspect | reference tasks | this generator |
|---|---|---|
| parts painted / with a hole initially | 1.00 / 1.00 | 1.00 / 1.00 |
| initial shapes cylindrical / circular / oblong | 1304 / 1306 / 1365 | 1345 / 1299 / 1331 |
| goal facts per task | = parts (150/150) | = parts (150/150) |
| goal kinds shape / surface / paint / hole | 1017 / 1505 / 1453 / 0 | 999 / 1507 / 1469 / 0 |
| parts with 0 / 1 / 2 / 3 goals | 1177 / 1766 / 887 / 145 | 1124 / 1857 / 864 / 130 |
| goals already true, duplicate (part, kind) | 0 / 0 | 0 / 0 |
| `ashape` objects | `circular oblong` in 149/150 | `circular oblong` always |

**Deviations:**
- Problem names differ (`schedule-<P>-<k>` in IPC).
- One IPC task (2 parts) lists only `oblong` as a shape object; this generator always lists both.
