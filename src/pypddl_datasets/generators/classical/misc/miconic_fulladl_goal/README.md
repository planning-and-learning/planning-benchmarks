# miconic_fulladl_goal (misc)

Variant of [IPC Miconic-ADL](../../ipc/miconic_fulladl/README.md) with the same
parameters, random draws, objects, initial state, and actions. The generator
delegates to the IPC implementation, retaining its validation and distribution.

The fixed domain `miconic-fulladl-goal` moves the universal goal into a nullary
derived predicate:

```pddl
(:derived (goal_satisfied)
  (forall (?p - passenger) (served ?p)))
```

Every generated problem checks `(:goal (goal_satisfied))`. This is equivalent to
the original goal and adds the `:derived-predicates` requirement.

The command-line options are identical to `ipc/miconic_fulladl`:

```sh
python -m pypddl_datasets.generators.classical.misc.miconic_fulladl_goal.generator -f 10 -p 5 -r 2
```

Based on Jana Koehler's AIPS-2000 domain and generator; the original
[Freiburg notice](../../../CREDITS.md#freiburg) applies. There are no reference
tasks for this encoding.
