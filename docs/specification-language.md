# Distribution specification language, version 1

Each generator directory contains one public `distribution.spec`. It describes
labeled initial situations and goal conjunctions for fixed parameters. The
[Ferry contract](../src/pypddl_datasets/generators/classical/ferry/distribution.spec)
is a small complete example; [Nomystery](../src/pypddl_datasets/generators/classical/nomystery/distribution.spec)
shows bounded optimal-cost witnesses. Every domain states its own rules explicitly.

## Loading and inspection

```python
from pypddl_datasets.generators import get_specification, load_specification

print(get_specification("ferry").source)  # base installation, no solver import
spec = load_specification("ferry", {"num_cars": 1, "num_locations": 2},
                          max_groundings=10_000)  # requires [specs]
result = spec.enumerate(limit=8, timeout_ms=10_000)
assert result.complete and len(result.situations) == 8
```

The loader also accepts a domain's frozen `Parameters` dataclass. Parameter names,
types, defaults, and `require` clauses are independently declared in the file.
Unknown parameters and invalid inputs are errors. Parsed definitions are cached;
each load constructs a fresh specification, and its solver methods create fresh solvers.

`SpecificationError` reports a file, line, and column when a source expression
causes an error. Named compiled rules expose `.source` spans. `max_groundings`
limits finite construction work, including expression evaluation and enumeration
of declaration tuples. Exhaustion raises an error; it never weakens the contract.
The budget is an implementation work limit, not a portable count of logical atoms.

## Declarations

A file starts with `language 1;`, `distribution ferry;`, and `revision "2";`.
Language and distribution revisions are independent. Its `metadata` block holds
`probability`, `solvability`, and `scope` strings plus `cases` and `limitations`
string lists. These describe laws and evidence; they do not constrain support.

```text
param num_cars: int;
param probability: float = 0.5;
param height: int? = none;
require counts: num_cars >= 0;
let Cars = names("c", num_cars);
let Locations = ["l0", "l1"];
objects Cars: object;
objects Locations: object;
relation initial.at(Cars, Locations);
relation goal.at(Cars, Locations);
```

`int`, `float`, and `str` parameters may be nullable (`?`). Parameters are global inputs. Ground `let` values
refer to parameters and earlier nonparameter declarations. `names(prefix, count, start)` builds
labels, defaulting to start zero. `range` follows Python's exclusive-stop rule.
Indexed declarations use finite binders, for example
`let Cell[r in range(2), c in range(3)] = "p"+str(r)+"_"+str(c);`.
`values(Cell)` returns their values in declaration order.

`objects Names: type;` declares required objects; append `optional` to make their
presence part of the distribution. `present(name)` tests object presence.
`constants Names: type;` makes domain constants available to relations without
adding them to the problem's object declarations. Required objects remain present
for any selected rule groups. True atoms can only reference present objects, and
numeric declarations require their referenced objects to be present. PDDL names
are case normalized.

A relation declares all tuples in its Cartesian argument families. Add
`as "pddl-name"` when the PDDL spelling differs from the DSL identifier. A sparse
family declares only the tuples produced by its finite binders and ground guard:

```text
relation initial.sum[a in range(5), b in range(5) where a+b<5]
    (Levels[a], Levels[b], Levels[a+b]);
number initial.total_cost(): int(0, 0) as "total-cost";
metric minimize initial.total_cost();
aux rank[c in Cars]: int(0, num_cars);
aux selected[c in Cars]: bool;
```

Integer bounds are inclusive and remain active when checking selected rule groups.
Auxiliary variables are existential witnesses,
excluded from semantic task identity and enumeration blocking. Numbers are initial
integer-valued fluents; metrics refer to a declared nullary numeric fluent.

## Rules and expressions

```text
initial {
    rule car_location:
        forall c in Cars: count(l in Locations: initial.at(c,l)) == 1;
}
goal {
    rule car_destination:
        forall c in Cars: count(l in Locations: goal.at(c,l)) == 1;
}
joint {}
```

`initial`, `goal`, and `joint` group named Boolean rules. Their conjunction defines
whole-task membership. Quantifiers are finite `forall` and `exists`; `count` counts
true instances and `sum` adds integer expressions. Bindings may depend on earlier
bindings and may include `where` guards. Empty universal quantification is true,
empty existential quantification is false, and empty counts/sums are zero.

Use `not`, `and`, `or`, `implies`, `iff`, comparisons, and
`if condition then value else value`. Parenthesize nested quantifiers to make their
scope explicit. Ground guards and conditions short-circuit: an inactive branch
is not evaluated, so it may contain an index that exists only in the active case.
Symbolic guards constrain every relevant finite instance. Names and arities are
checked even in inactive branches; value-dependent type and index checks occur
during grounding.

Ground arithmetic uses Python integers and binary64 floats, preserving operation
order for `+ - * / // % **`. Available ground functions are `len`, `values`, `str`,
`min`, `max`, `abs`, `ceil`, `floor`, `trunc`, `round`, `int`, and `float`, as well
as `range` and `names`. Nonfinite numeric results are errors. Symbolic values are
Boolean or integer; symbolic arithmetic allows addition, subtraction, and
multiplication by ground integers. It excludes nonlinear products, division,
remainders, and powers. There are no imports, Python callbacks, or evaluation of
Python source.

## Meaning and evidence

An initial relation variable means an atom is present in the initial state. A goal
relation variable means an atom occurs in the positive goal conjunction; absence
does not demand that the atom be false in a final planning state. Membership binds
absent atoms to false, requires declared numeric initializations, and rejects
unexpected vocabulary or mismatched metrics.

`check_pddl` uses independent strict PDDL decoding. Membership can return `member`,
`nonmember`, `timeout`, or `unknown`. Enumeration returns `complete` only after
proving the remaining projected space empty; `limit`, `timeout`, and `unknown`
remain inconclusive. Compare projected semantic situations when testing support:
independent auxiliary witnesses must not create spurious differences.

Sample membership establishes evidence of soundness. Exact small-case enumeration
can expose missing support, but does not prove arbitrary-size completeness.
Probability laws require separate weighting tests; satisfying a contract does not
establish the sampler's probabilities. Each file documents its verified scope.
