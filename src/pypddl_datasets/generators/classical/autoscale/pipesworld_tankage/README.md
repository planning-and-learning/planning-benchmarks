# pipesworld_tankage (autoscale)

Autoscale's pipesworld-tankage tasks are a subset of the IPC 2004 tasks; this package re-exports `../../ipc/pipesworld_tankage`.

## Source

- **Domain:** Frederico Liporace and Jörg Hoffmann, IPC 2004; Autoscale's copy (identical to the IPC file), lowercased
- **Generator:** Autoscale has no generator for this domain (it ships 30 IPC tasks); re-exports `../../ipc/pipesworld_tankage` (reconstruction from the IPC tasks)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/pipesworld-tankage` (30 tasks, byte-identical to IPC p11–p40)

## Parameters

See `../../ipc/pipesworld_tankage`. Reference range: net2–net4, 10–22 batches, 2–8 goals, tankage 20–90 %.

## Distribution

### Objects
As in `../../ipc/pipesworld_tankage`.

### Initial state
As in `../../ipc/pipesworld_tankage`: one of the five IPC networks, uniform products, pipes filled and remaining batches at uniform areas, IPC tank-slot rule.

### Goal
As in `../../ipc/pipesworld_tankage`: batches at the areas a random walk takes them to, all pipes `normal`.

### Other
No action costs. Every task is solvable.

## Comparison with reference tasks

The Autoscale tasks are IPC tasks; see the comparison in `../../ipc/pipesworld_tankage/README.md`.

**Deviations:** none beyond those of `../../ipc/pipesworld_tankage`.
