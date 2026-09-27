# Autoscale generators

Python ports of the generators in
[AI-Planning/autoscale `pddl-generators/`](https://github.com/AI-Planning/autoscale/tree/main/pddl-generators),
restricted to the options that
[`autoscale/domains.py`](https://github.com/AI-Planning/autoscale/blob/main/autoscale/domains.py)
passes. Each `domain.pddl` is the one shipped with the Autoscale 21.11
benchmarks (lowercased), so the reference distribution is
[`data/classical/autoscale-benchmarks-main/21.11-agile-strips`](../../../../../data/classical/autoscale-benchmarks-main/21.11-agile-strips)
(same generators and domains as `21.11-optimal-strips`, different parameter
sequences).

The ports match the upstream distribution, not its bytes: they use Python's
`random` instead of the original C/Perl RNGs. Deliberate deviations (upstream
bugs, crashes on edge cases) are noted in each `generator.py`.

26 of the 27 generated agile domains have a package here; openstacks is left
out because its per-task domains are ground. Most only re-export
[`../ipc`](../ipc) and add Autoscale's (lowercased) `domain.pddl`, passing a
flag where Autoscale's tasks differ from the IPC ones: `typed=True` (depots,
driverlog, miconic, satellite, zenotravel), `action_costs=True` (barman, transport),
`patched=True` (satellite), `style="autoscale"` (grid), `autoscale=True`
(rovers), `full_sum_table=False` (nomystery).
Own implementations remain for blocksworld (bwstates goal with `on` facts
only) and logistics.
The remaining agile domains (agricola,
airport, freecell, ged, mprime, organic-synthesis-split, parcprinter, pathways,
pegsol, pipesworld-notankage, pipesworld-tankage, sokoban, tetris, thoughtful,
tidybot) are IPC task selections without a generator.

Each package's `README.md` describes its distribution and compares it with
the agile tasks. Authors and license notices: [`../../CREDITS.md`](../../CREDITS.md).
