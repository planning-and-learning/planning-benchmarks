language 1;
distribution logistics;
revision "2";
metadata {
    probability "Uniform truck city allocation, airport roles, and positions within roles; uniform distinct package endpoints; Bernoulli goals with singleton repair.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_cities,city_size,num_packages,num_airplanes)=(1,2,1,1); goal probability boundaries"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_cities: int;
param city_size: int;
param num_packages: int;
param num_airplanes: int;
param goal_package_probability: float = 1.0;

require valid_counts: num_cities >= 1 and city_size >= 2 and num_packages >= 1 and num_airplanes >= 1;
require valid_probability: goal_package_probability >= 0 and goal_package_probability <= 1;
let Cities = names("c", num_cities);
let Trucks = names("t", num_cities);
let Airplanes = names("a", num_airplanes);
let Packages = names("p", num_packages);
let Place[c in range(num_cities), i in range(city_size)] = "l" + str(c) + "-" + str(i);
let Locations = values(Place);
let Moving = Trucks + Airplanes + Packages;
objects Cities + Moving + Locations: object;
relation initial.city(Cities);
relation initial.truck(Trucks);
relation initial.airplane(Airplanes);
relation initial.obj(Packages);
relation initial.location(Locations);
relation initial.in_city(Locations, Cities) as "in-city";
relation initial.airport(Locations);
relation initial.at(Moving, Locations);
relation goal.at(Packages, Locations);
initial {
 rule cities: forall c in Cities: initial.city(c);
 rule trucks: forall t in Trucks: initial.truck(t);
 rule airplanes: forall a in Airplanes: initial.airplane(a);
 rule packages: forall p in Packages: initial.obj(p);
 rule places: forall l in Locations: initial.location(l);
 rule city_geometry: forall c in range(num_cities), i in range(city_size), d in range(num_cities): initial.in_city(Place[c,i],Cities[d]) iff c == d;
 rule airport_roles: forall c in range(num_cities): count(i in range(city_size): initial.airport(Place[c,i])) == 1;
 rule city_trucks: forall c in range(num_cities): count(t in Trucks, i in range(city_size): initial.at(t,Place[c,i])) == 1;
 rule unique_positions: forall o in Moving: count(l in Locations: initial.at(o,l)) == 1;
 rule airplane_airports: forall a in Airplanes, l in Locations: initial.at(a,l) implies initial.airport(l);
}
goal {
 rule package_destination: forall p in Packages: count(l in Locations: goal.at(p,l)) <= 1;
 rule inclusion_endpoints: forall p in Packages: if goal_package_probability == 0 then count(l in Locations: goal.at(p,l)) == 0 else if goal_package_probability == 1 then count(l in Locations: goal.at(p,l)) == 1 else true;
 rule nonempty_repair: if goal_package_probability > 0 then count(p in Packages, l in Locations: goal.at(p,l)) >= 1 else true;
}
joint { rule changed_destinations: forall p in Packages, l in Locations: goal.at(p,l) implies not initial.at(p,l); }
