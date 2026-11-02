language 1;
distribution blocks_3;
revision "2";
metadata {
    probability "Independent uniform labeled stack arrangements for initial and goal.";
    solvability "guaranteed";
    scope "bounded whole-task support and weighting";
    cases ["3 blocks: all 169 initial/goal pairs"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_blocks: int;

require counts: num_blocks >= 1;
let Blocks = names("b", num_blocks, 1);
objects Blocks: object;
relation initial.on(Blocks, Blocks);
relation initial.on_table(Blocks) as "on-table";
relation initial.clear(Blocks);
relation goal.on(Blocks, Blocks);
relation goal.on_table(Blocks) as "on-table";
relation goal.clear(Blocks);

aux initial_height[b in Blocks]: int(0, num_blocks - 1);
aux goal_height[b in Blocks]: int(0, num_blocks - 1);
initial {
 rule unique_support: forall b in Blocks: count(c in Blocks where c != b: initial.on(b,c)) + (if initial.on_table(b) then 1 else 0) == 1;
 rule no_self_support: forall b in Blocks: not initial.on(b,b);
 rule no_branching: forall b in Blocks: count(c in Blocks where c != b: initial.on(c,b)) <= 1;
 rule clear_top: forall b in Blocks: initial.clear(b) iff not (exists c in Blocks where c != b: initial.on(c,b));
 rule acyclic: forall b in Blocks, c in Blocks where b != c: initial.on(b,c) implies initial_height[b] > initial_height[c];
}
goal {
 rule unique_support: forall b in Blocks: count(c in Blocks where c != b: goal.on(b,c)) + (if goal.on_table(b) then 1 else 0) == 1;
 rule no_self_support: forall b in Blocks: not goal.on(b,b);
 rule no_branching: forall b in Blocks: count(c in Blocks where c != b: goal.on(c,b)) <= 1;
 rule clear_top: forall b in Blocks: goal.clear(b) iff not (exists c in Blocks where c != b: goal.on(c,b));
 rule acyclic: forall b in Blocks, c in Blocks where b != c: goal.on(b,c) implies goal_height[b] > goal_height[c];
}
joint {}
