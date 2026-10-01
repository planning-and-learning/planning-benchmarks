# IPC 2023 learning-track generators

Generators for the ten IPC 2023 learning-track domains. Except for Sokoban, each package keeps the
generator as it was on 2026-09-27 before the IPC rework (commit HEAD), with the
learning track's own `domain.pddl` (verbatim), the minimal problem-writer changes
needed to parse against it, and options (default on) that close the support gaps
to the learning tasks; switching them off gives the morning behaviour. Sokoban
uses the upstream learning-track forward-walk generator at revision
`19d6a8ad4b354328154a2cc1f1a95f7c09fa9db6`, adapted from the LMP generator.
Reference tasks:
`data/classical/ipc2023-learning/<domain>_ipc2023_learning`.

| generator | morning generator | changes | open gaps vs the learning tasks |
|---|---|---|---|
| blocksworld | `blocks_4` | none | none |
| childsnack | `childsnack` | domain name | none (`gluten_factor=1.0` covers all-allergic tasks) |
| ferry | `ferry` | typed objects, no `not-eq` | none (goals may equal start) |
| floortile | `floortile` | domain name, no costs | none |
| miconic | `miconic` | `lift_start` (default random) | none |
| rovers | `rovers` | no `channel_free`/`available`; `learning_graphs`, `learning_goals` (default on) | none |
| satellite | `satellite` | `pointing_goal_may_hold` (default on) | none |
| sokoban | upstream learning-track generator (`19d6a8a`) | local seeded RNG, callable API, corrected BFS queue guard; failed samples raise `ValueError` without retries | valid parameters can still produce sampling failures |
| spanner | `spanner` | `usable` | none |
| transport | `transport` | random edge count, `random_capacities` (default on) | none |

Authors and license notices: [`../../CREDITS.md`](../../CREDITS.md).
