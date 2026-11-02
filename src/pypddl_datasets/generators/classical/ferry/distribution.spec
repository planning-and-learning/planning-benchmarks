language 1;
distribution ferry;
revision "2";
metadata {
    probability "Independent uniform car origins, car destinations, and ferry origin.";
    solvability "guaranteed";
    scope "bounded whole-task support and weighting";
    cases ["(num_cars,num_locations)=(0,1),(0,2),(1,1),(1,2),(2,2): exact joint support"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_cars: int;
param num_locations: int;

require counts: num_cars >= 0 and num_locations >= 1;
let Cars = names("c", num_cars);
let Locations = names("l", num_locations);
objects Cars: object;
objects Locations: object;
relation initial.car(Cars);
relation initial.location(Locations);
relation initial.not_eq(Locations, Locations) as "not-eq";
relation initial.empty_ferry() as "empty-ferry";
relation initial.at_ferry(Locations) as "at-ferry";
relation initial.at(Cars, Locations);
relation goal.at(Cars, Locations);
initial {
 rule car_types: forall c in Cars: initial.car(c);
 rule location_types: forall l in Locations: initial.location(l);
 rule inequality: forall a in Locations, b in Locations: initial.not_eq(a,b) iff a != b;
 rule empty: initial.empty_ferry();
 rule ferry_location: count(l in Locations: initial.at_ferry(l)) == 1;
 rule car_locations: forall c in Cars: count(l in Locations: initial.at(c,l)) == 1;
}
goal { rule car_destinations: forall c in Cars: count(l in Locations: goal.at(c,l)) == 1; }
joint {}
