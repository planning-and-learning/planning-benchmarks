# Numeric IPC generators

Generators for the IPC 2023 and IPC 2026 numeric-track domains. The reference
tasks are `data/numeric/ipc2023/<domain>` and `data/numeric/ipc2026/<domain>`
(suites `ipc2023-numeric` and `ipc2026-numeric`), mirrored from
[ipc2023-numeric/ipc2023-dataset](https://github.com/ipc2023-numeric/ipc2023-dataset)
and [ipc2026-numeric/ipc2026-dataset](https://github.com/ipc2026-numeric/ipc2026-dataset).
Neither dataset ships generators, so each generator is either a port of a
published generator or a reconstruction from the reference tasks; each
package's `README.md` says which and compares its distribution with the tasks.
All output is lowercase and each `domain.pddl` is the reference domain file.

| generator | reference | generator source |
|---|---|---|
| block_grouping | ipc2023/block-grouping | reconstruction |
| coins | ipc2026/coins | reconstruction (deterministic) |
| counters | ipc2023/counters | reconstruction (`init` selects the three task families) |
| delivery | ipc2023/delivery | reconstruction (the reference maps are hand-made) |
| drone | ipc2023/drone | reconstruction (deterministic) |
| expedition | ipc2023/expedition, ipc2026/expedition | reconstruction (deterministic) |
| ext_plant_watering | ipc2023/ext-plant-watering | reconstruction |
| factory_robot | ipc2026/factory-robot | reconstruction |
| farmland | ipc2023/farmland | port of `farmlandgenerator.py` (Enrico Scala) |
| fo_counters | ipc2023/fo-counters | reconstruction |
| fo_farmland | ipc2023/fo-farmland | farmland port |
| fo_sailing | ipc2023/fo-sailing | sailing port |
| forestfire | ipc2026/forestfire | reconstruction |
| game_2048 | ipc2026/2048 | reconstruction (backward search from the goal board) |
| gear_car | ipc2026/gear-car | reconstruction (deterministic) |
| hydropower | ipc2023/hydropower | reconstruction |
| line_exchange_snp | ipc2026/line-exchange-snp | reconstruction |
| markettrader | ipc2023/markettrader | reconstruction |
| mprime | ipc2023/mprime | translation of `classical/ipc/mprime` |
| onlycraft | ipc2026/onlycraft-{opt,sat} | reconstruction |
| pathwaysmetric | ipc2023/pathwaysmetric | port of pathways `main.c -N` (reuses `classical/ipc/pathways`) |
| petri_net | ipc2026/petri-net | reconstruction (three net templates) |
| rainbowttles | ipc2026/rainbowttles-{opt,sat} | reconstruction |
| rover | ipc2023/rover | port of `rovgen -n` (reuses `classical/ipc/rovers`) |
| sailing | ipc2023/sailing | port of `generate_saving.py` (Enrico Scala) |
| sailing_wind | ipc2026/sailing-wind-{opt,sat} | reconstruction |
| settlers_snp | ipc2026/settlers-snp | reconstruction |
| settlersnumeric | ipc2023/settlersnumeric | reconstruction |
| sugar | ipc2023/sugar | reconstruction (one hand-written template) |
| tpp | ipc2023/tpp | reconstruction |
| zenotravel | ipc2023/zenotravel | port of `zenogenerator -n` |
| ztalloc_sum | ipc2026/ztalloc-sum | reconstruction |

Authors and license notices: [`../../CREDITS.md`](../../CREDITS.md).
