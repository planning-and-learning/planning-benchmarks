# settlers (ipc)

Build a settlement economy: harvest timber, stone and ore, process them, build vehicles, sawmills, ironworks, houses and rail links; resources are discretized levels with conditional-effect arithmetic.

## Source

- **Domain:** Marcel Steinmetz (IPC 2018), a discretized, resource-constrained variant of Patrik Haslum's IPC 2002 Settlers
- **Generator:** Autoscale's `pddl-generators/settlers/generator.py` (Marcel Steinmetz), with the IPC settings of `generate-instances.py`; Python port in `generator.py`. Upstream's CPLEX transport MIP is replaced by a feasible solution of the same MIP
- **Reference tasks:** `data/classical/downward-benchmarks/settlers-opt18-adl`, `data/classical/downward-benchmarks/settlers-sat18-adl`

## Parameters

| parameter | meaning | reference range |
|---|---|---|
| `num_locations`, `num_edges`, `num_seas` | map size (`--map` presets tiny 3/2/0, small 5/5/1, large 8/9/1, huge 16/18/2) | tiny, small (opt); small, large, huge (sat) |
| `num_goals` | number of goal draws | 1–6 (opt), 3–10 (sat) |
| `track` | resource/vehicle slack: `opt` 1.2×+4 / 1.2×+2, `sat` 1.5×+5 / 1.5×+3 | both |
| `seed` | random seed; the IPC task header records it | IPC header seeds |
| `prob_coast`, `prob_goal_*` | coast probability 1/2; goal weights house/building/rail 3/3/4 | fixed |

## Distribution

### Objects
Places `p0..`, potential vehicles `v0..` (minimal vehicles × factor + increment), resource levels above 10 as objects (levels 0–10 are domain constants).

### Initial state
- Map: woodland at p0, mountain and metalliferous uniform in the first half; coastal places join seas (every sea gets one place, then each further place with probability 1/2); roads connect the map (through seas where possible), then random extra roads, keeping woodland, mountain and metalliferous connected by land.
- Stone, timber and ore at their places: the minimal amount needed for the goals (including required sawmill/coal stack/ironworks, a cart, and ship transport for other islands) times the track factor plus increment; wood and coal as timber, iron as ore, housing as min(timber, stone). Everything else at level 0, with the `available-atleast-*`, `diff-*`, `add/del-atleast-*` arithmetic facts.

### Goal
Each draw is a house (weight 3; houses at a place accumulate to `housing p hlN`), a building (3; coal stack, sawmill or ironworks, each at most once per place) or a rail link along a road (4).

### Other
`(:metric minimize (total-cost))` with labour ×5 and pollution ×10 costs in the domain. The IPC tasks were made under Python 2, so draws use Python 2's `randint`/`sample`/`shuffle`. Upstream's CPLEX MIP for ship transport is replaced by round trips from each sea's wharf (≤8 units per trip, 2 units fuel per departure, last trip one-way): a feasible MIP solution, so resources are never below upstream's minimum.

## Comparison with reference tasks

| aspect | reference tasks | this generator |
|---|---|---|
| tasks reproduced from the header's seed, map, goals and track | 40 | 40 identical as object/init/goal sets |
| tasks needing ship transport | 0 of 40 | 86 of 300 random huge-map tasks |

**Deviations:**
- The IPC tasks were selected by hardness among 10,000 draws per setting (sorted by required resources, picked at the 5/25/50/75 % positions); the generator returns single draws, so it also produces ship-requiring tasks, which none of the IPC tasks is.
- Ship transport uses an upper bound of upstream's MIP optimum (never exercised by the IPC tasks).
- Problem names and header comment differ; objects are declared in a different order.
