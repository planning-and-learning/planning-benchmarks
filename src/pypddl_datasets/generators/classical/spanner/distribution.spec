language 1;
distribution spanner;
revision "2";
metadata {
    probability "Independent uniform spanner positions along the fixed directed route.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_spanners,num_nuts,num_locations)=(1,1,1); placement component (2,1,2)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_spanners: int;
param num_nuts: int;
param num_locations: int;

require valid_counts: num_spanners >= 1 and num_nuts >= 1 and num_locations >= 1 and num_nuts <= num_spanners;
let Spanners = names("spanner", num_spanners, 1);
let Nuts = names("nut", num_nuts, 1);
let Locations = names("location", num_locations, 1);
let Route = ["shed"] + Locations + ["gate"];
let Moving = ["bob"] + Spanners + Nuts;
objects ["bob"]: man;
objects Spanners: spanner;
objects Nuts: nut;
objects Route: location;
relation initial.at(Moving, Route);
relation initial.useable(Spanners);
relation initial.loose(Nuts);
relation initial.link(Route, Route);
relation goal.tightened(Nuts);
initial {
 rule person_start: forall l in Route: initial.at("bob",l) iff l == "shed";
 rule spanner_positions: forall s in Spanners: count(l in Locations: initial.at(s,l)) == 1;
 rule spanners_between_ends: forall s in Spanners: not initial.at(s,"shed") and not initial.at(s,"gate");
 rule usable_spanners: forall s in Spanners: initial.useable(s);
 rule loose_nuts: forall n in Nuts: initial.loose(n);
 rule nuts_at_gate: forall n in Nuts, l in Route: initial.at(n,l) iff l == "gate";
 rule directed_route: forall i in range(num_locations+2), j in range(num_locations+2): initial.link(Route[i],Route[j]) iff j == i + 1;
}
goal { rule tightened_nuts: forall n in Nuts: goal.tightened(n); }
joint {}
