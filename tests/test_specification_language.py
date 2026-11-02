"""Language semantics independently of any particular generator distribution."""
from __future__ import annotations

from importlib.resources import files
from typing import TYPE_CHECKING, cast

import pytest

from pypddl_datasets.generators._specifications.syntax import SpecificationError, parse_definition

if TYPE_CHECKING:
    from pypddl_datasets.generators._specifications.core import Specification


def _source(body: str) -> str:
    return 'language 1; distribution ferry; revision "2"; metadata {}\n' + body


def _compile(body: str, max_groundings: int | None = None) -> Specification:
    pytest.importorskip("z3")
    from pypddl_datasets.generators._specifications.compiler import compile_definition
    return compile_definition(parse_definition(_source(body), "case.spec"), {}, max_groundings)


def test_parser_preserves_metadata_parameters_and_source_locations() -> None:
    source = '''language 1;
distribution ferry;
revision "2";
metadata { probability "fair \\"coin\\""; cases ["one", "two"]; }
param size: int = 2;
param height: int? = none;
require positive: size >= 1;
'''
    definition = parse_definition(source, "ferry/distribution.spec")
    assert definition.source_text == source
    assert definition.metadata["probability"] == 'fair "coin"'
    assert definition.metadata["cases"] == ("one", "two")
    assert definition.parameters[1].nullable
    assert definition.parameters[0].span.line == 5
    assert definition.constraint_sources == ("size >= 1",)


@pytest.mark.parametrize("body", [
    'language 2; distribution ferry; revision "2"; metadata {}',
    _source("param n: int; param n: int;"),
    _source("param n: executable;"),
    'language 1; distribution ferry; revision "2"; metadata { scope 2; }',
    'language 1; distribution ferry; revision "2"; metadata { scope "a"; scope "b"; }',
    _source('import "arbitrary.py";'),
    r'language 1; distribution ferry; revision "2"; metadata { scope "\q"; }',
])
def test_parser_rejects_invalid_contracts_with_locations(body: str) -> None:
    with pytest.raises(SpecificationError, match=r"bad.spec:\d+:\d+"):
        parse_definition(body, "bad.spec")


def test_keyword_prefixes_and_precedence() -> None:
    specification = _compile('''
        let initial_rank = 2;
        let count_value = 3;
        let not_a_keyword = 4;
        require powers: 2 ** 3 ** 2 == 512;
        require unary: -2 ** 2 == -4;
        require comparison: not initial_rank == count_value;
        require remainder: 17 // 3 % 2 == 1;
        require order: 2 + 3 * 4 == 14 and not_a_keyword == 4;
    ''')
    assert specification.enumerate().complete


def test_empty_domains_and_dead_ground_branches() -> None:
    specification = _compile('''
        let Empty = range(0);
        let Array[i in range(1)] = i;
        let Kept[i in range(2) where i == 0] = Array[i];
        require short_and: not (false and Array[99] == 2);
        require short_or: true or Array[99] == 2;
        require short_implies: false implies Array[99] == 2;
        require short_if: (if true then Array[0] else Array[99]) == 0;
        require empty_forall: forall i in Empty: Array[99] == 0;
        require empty_exists: not (exists i in Empty: Array[99] == 0);
        require empty_sum: sum(i in Empty: Array[99]) == 0;
        require empty_count: count(i in Empty: Array[99] == 0) == 0;
        require skipped: forall i in range(3) where i == 0: Array[i] == 0;
        require retained: values(Kept) == [0];
    ''')
    assert specification.enumerate().complete


def test_ground_binary64_rounding_is_preserved() -> None:
    specification = _compile('''
        require fuel: trunc(1.0 * 9007199254740993) == 9007199254740992;
        require ceiling: ceil(3 * (1.1 - 1)) == 1;
        require ties: round(2.5) == 2 and round(3.5) == 4;
        require truncation: trunc(-1.9) == -1 and floor(-1.9) == -2;
        require name_order: names("x", 3, 1) == ["x1", "x2", "x3"];
    ''')
    assert specification.enumerate().complete


def test_sparse_relations_bind_only_the_declared_tuples() -> None:
    specification = _compile('''
        let Nodes = names("n", 3);
        objects Nodes: "location";
        relation initial.next[i in range(2)](Nodes[i], Nodes[i + 1]);
        initial { rule route: forall i in range(2): initial.next(Nodes[i], Nodes[i + 1]); }
    ''')
    assert len(specification.semantic_variables) == 5
    result = specification.enumerate()
    assert result.complete and len(result.situations) == 1
    assert specification.initial[-1].source is not None
    assert specification.initial[-1].source.source == "case.spec"
    with pytest.raises(SpecificationError, match="outside declared family"):
        _compile('''let Nodes = names("n", 2); objects Nodes: object;
            relation initial.edge[i in range(1)](Nodes[i], Nodes[i + 1]);
            initial { rule invalid: initial.edge("n1", "n0"); }''')


def test_auxiliary_choices_are_projected_and_symbolic_guards_are_logical() -> None:
    specification = _compile('''
        let Items = ["a", "b"];
        objects Items: object optional;
        aux unused[i in Items]: bool;
        aux rank[i in Items]: int(0, 1);
        relation initial.selected(Items);
        initial {
            rule present_selected: forall i in Items: present(i) iff initial.selected(i);
            rule exactly_one: count(i in Items: initial.selected(i)) == 1;
        }
        joint {
            rule guarded: forall i in Items where initial.selected(i): rank[i] == 1;
            rule counting: sum(i in Items where initial.selected(i): rank[i]) == 1;
        }
    ''')
    result = specification.enumerate()
    assert result.complete and len(result.situations) == 2
    assert len(specification.auxiliary_variables) == 4
    assert all(specification.check(situation).is_member for situation in result.situations)


def test_initialized_numbers_and_metric_are_declared_separately() -> None:
    specification = _compile('''
        number initial.cost(): int(0, 0) as "total-cost";
        metric minimize initial.cost();
        initial { rule zero: initial.cost() == 0; }
    ''')
    assert specification.metric == ("minimize", "total-cost")
    assert specification.enumerate().complete


@pytest.mark.parametrize("body,reason", [
    ("let A = B; let B = 2;", "forward-referenced"),
    ("let A = 1; let A = 2;", "duplicate declaration"),
    ("require x: true; require x: true;", "duplicate rule"),
    ("aux x: int(2, 1);", "lower bound"),
    ("let x = 1 / 0;", "division"),
    ("let x = 1e309;", "finite"),
    ("let x = __import__(\"os\");", "unknown builtin"),
    ("let x = true + 1;", "ground number"),
    ("aux x: int(0, 2); let y = x;", "ground expression"),
    ("aux x: int(0, 2); joint {rule nonlinear: x * x == 1;}", "affine"),
    ("aux x: int(0, 2); joint {rule division: x // 2 == 1;}", "affine"),
    ("aux x: int(0, 2); joint {rule float: x == 0.5;}", "ground integer"),
    ("let A = [1]; aux x: int(0, 0); joint {rule index: A[x] == 1;}", "ground scalar"),
    ("initial {rule missing: initial.undeclared();}", "undeclared relation"),
    ('objects ["a"]: object; objects ["a"]: object;', "duplicate object"),
    ('relation initial.bad(["missing"]);', "undeclared objects"),
])
def test_compiler_rejects_unsupported_or_ill_typed_expressions(body: str, reason: str) -> None:
    with pytest.raises(SpecificationError, match=reason):
        _compile(body)


def test_parameter_defaults_and_type_errors() -> None:
    pytest.importorskip("z3")
    from pypddl_datasets.generators._specifications.compiler import compile_definition
    definition = parse_definition(_source('''
        param width: int = 3; param height: int? = none; param label: str = "grid";
        let rows = if height == none then width else height;
        require valid: rows > 0;
    '''))
    assert compile_definition(definition, {}).enumerate().complete
    for parameters in ({"width": True}, {"width": 1.5}, {"height": "wrong"}, {"unknown": 1}):
        with pytest.raises(SpecificationError):
            compile_definition(definition, parameters)


def test_grounding_budget_fails_explicitly_before_large_expansion() -> None:
    pytest.importorskip("z3")
    from pypddl_datasets.generators._specifications.compiler import GroundingLimitError
    with pytest.raises(GroundingLimitError, match="case.spec"):
        _compile("let Huge = range(1000000000);", max_groundings=10)


def test_declared_integer_bounds_survive_rule_group_selection() -> None:
    specification = _compile("""
        number initial.cost(): int(0, 1);
        aux rank: int(1, 1);
        initial {rule value: initial.cost() == rank;}
    """)
    result = specification.enumerate(groups=("initial",))
    assert result.complete and len(result.situations) == 1
    assert len(specification.declarations) == 2
    assert all(declaration.source is not None for declaration in specification.declarations)


@pytest.mark.parametrize("body,reason", [
    ("require empty: forall i in range(0): missing == 1;", "unknown"),
    ("let unused[i in range(0)] = missing;", "unknown"),
    ("let unused[i in range(0) where missing] = i;", "unknown"),
    ("require dead: true or missing == 1;", "unknown"),
    ("require empty: forall i in range(0): initial.missing();", "undeclared"),
    ("require dead: true or abs() == 1;", "arguments"),
    ('relation initial.a() as "same"; relation initial.b() as "same";', "duplicate semantic"),
])
def test_static_name_and_declaration_checks_cover_unreached_code(body: str, reason: str) -> None:
    with pytest.raises(SpecificationError, match=reason):
        _compile(body)


@pytest.mark.parametrize("value", [True, 1.5, 0, -1])
def test_construction_budget_requires_a_positive_integer(value: object) -> None:
    with pytest.raises(SpecificationError, match="positive integer"):
        _compile("", max_groundings=cast(int, value))


def test_grammar_is_strict_lalr_without_lexer_collisions() -> None:
    pytest.importorskip("interegular")
    from lark import Lark
    grammar = files("pypddl_datasets.generators._specifications").joinpath("grammar.lark").read_text(encoding="utf-8")
    Lark(grammar, parser="lalr", strict=True)


@pytest.mark.parametrize("body,reason", [
    ("aux x[i in []]: int(2, 1);", "lower bound"),
    ("number initial.x([]): int(2, 1);", "lower bound"),
    ("aux n: int(0, 1); aux x[i in []]: int(0, n);", "ground expression"),
    ("aux n: int(0, 1); number initial.x([]): int(0, n);", "ground expression"),
    ('relation initial.p() as "same"; objects ["a"]: object; relation goal.q(["a"]) as "same";', "arity"),
    ('objects [""]: object;', "identifier"),
    ('objects ["a b"]: object;', "identifier"),
    ('objects ["a"]: "bad type";', "identifier"),
    ('relation initial.x() as "x)";', "identifier"),
    ("require x: true == 1;", "incompatible types"),
    ("aux x: int(0, 1); joint {rule x: [x] == [1];}", "ground values"),
    ("aux x: int(0, 1); joint {rule x: [x] != [1];}", "ground values"),
    ("aux x[i in [true, 1]]: bool;", "duplicate finite"),
    ("let x[i in [1, 1]] = i;", "duplicate finite"),
])
def test_declaration_validation_regressions(body: str, reason: str) -> None:
    with pytest.raises(SpecificationError, match=reason):
        _compile(body)


def test_optional_atom_arguments_and_mandatory_objects_are_always_present() -> None:
    specification = _compile("""
        objects ["required"]: object;
        objects ["optional"]: object optional;
        relation goal.selected(["optional"]);
    """)
    result = specification.enumerate(groups=("goal",))
    assert result.complete and len(result.situations) == 3
    assert all(dict(situation.values)[key] for situation in result.situations
               for key in specification.semantic_variables if key.kind == "object" and key.predicate == "required")
    numeric = _compile('objects ["a"]: object optional; number initial.cost(["a"]): int(0, 0);')
    assert len(numeric.enumerate().situations) == 1


def test_parameters_must_precede_the_body() -> None:
    with pytest.raises(SpecificationError, match="parameters must precede"):
        parse_definition(_source("let x = n; param n: int = 3;"))
