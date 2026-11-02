language 1;
distribution childsnack;
revision "2";
metadata {
    probability "Independent uniform fixed-size allergy and gluten-free subsets; independent uniform waiting tables.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_children,num_trays,gluten_factor)=(2,1,0.5)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_children: int;
param num_trays: int;
param gluten_factor: float;
param const_ratio: float = 1.2;

require counts: num_children >= 1 and num_trays >= 1;
require allergy_fraction: gluten_factor >= 0 and gluten_factor <= 1;
require resources: const_ratio >= 1;
let Children = names("child", num_children, 1);
let Breads = names("bread", num_children, 1);
let Contents = names("content", num_children, 1);
let Sandwiches = names("sandw", ceil(num_children * const_ratio), 1);
let Trays = names("tray", num_trays, 1);
let Tables = ["table1", "table2", "table3"];
let Kitchen = ["kitchen"];
let Allergic = min(num_children, int(num_children * gluten_factor));
objects Children: child;
objects Breads: "bread-portion";
objects Contents: "content-portion";
objects Sandwiches: sandwich;
objects Trays: tray;
objects Tables: place;
constants Kitchen: place;
relation initial.allergic_gluten(Children);
relation initial.not_allergic_gluten(Children);
relation initial.no_gluten_bread(Breads);
relation initial.no_gluten_content(Contents);
relation initial.at_kitchen_bread(Breads);
relation initial.at_kitchen_content(Contents);
relation initial.notexist(Sandwiches);
relation initial.at(Trays, Kitchen);
relation initial.waiting(Children, Tables);
relation goal.served(Children);
initial {
 rule allergic_count: count(c in Children: initial.allergic_gluten(c)) == Allergic;
 rule free_bread_count: count(b in Breads: initial.no_gluten_bread(b)) == Allergic;
 rule free_content_count: count(c in Contents: initial.no_gluten_content(c)) == Allergic;
 rule allergy_partition: forall c in Children: initial.not_allergic_gluten(c) iff not initial.allergic_gluten(c);
 rule waiting_table: forall c in Children: count(t in Tables: initial.waiting(c,t)) == 1;
 rule bread_supply: forall b in Breads: initial.at_kitchen_bread(b);
 rule content_supply: forall c in Contents: initial.at_kitchen_content(c);
 rule sandwiches_unmade: forall s in Sandwiches: initial.notexist(s);
 rule trays_in_kitchen: forall t in Trays: initial.at(t,"kitchen");
}
goal { rule children_served: forall c in Children: goal.served(c); }
joint {}
