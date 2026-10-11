# pipesworld_notankage (autoscale)

Autoscale's pipesworld-notankage tasks are a subset of the IPC 2004 tasks; this package re-exports `../../ipc/pipesworld_notankage`.

## Source

- **Domain:** Frederico Liporace and Jörg Hoffmann, IPC 2004; Autoscale's copy (identical to the IPC file), lowercased
- **Generator:** Autoscale has no generator for this domain (it ships 30 IPC tasks); re-exports `../../ipc/pipesworld_notankage` (reconstruction from the IPC tasks)
- **Reference tasks:** `data/classical/autoscale-benchmarks-main/21.11-agile-strips/pipesworld-notankage` (30 tasks, byte-identical to IPC p21–p50)

## Parameters

See `../../ipc/pipesworld_notankage`. Reference range: net3–net5, 12–30 batches, 2–8 goals.

## Distribution

### Objects
As in `../../ipc/pipesworld_notankage`.

### Initial state
As in `../../ipc/pipesworld_notankage`: one of the five IPC networks, uniform products, pipes filled and remaining batches at uniform areas.

### Goal
As in `../../ipc/pipesworld_notankage`: batches at the areas a random walk takes them to.

### Other
No action costs. Every task is solvable.

## Comparison with reference tasks

The Autoscale tasks are IPC tasks; see the comparison in `../../ipc/pipesworld_notankage/README.md`.

**Deviations:** none beyond those of `../../ipc/pipesworld_notankage`.
