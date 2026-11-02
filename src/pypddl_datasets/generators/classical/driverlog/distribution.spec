language 1;
distribution driverlog;
revision "2";
metadata {
    probability "Independent Bernoulli edges conditioned on connectivity for roads and paths; uniform positions and different destinations; Bernoulli goal selection with uniform singleton repair within each nonzero-probability role.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_locations,num_drivers,num_trucks,num_packages)=(3,1,1,1); goal probability endpoints and near endpoints"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_locations: int;
param num_drivers: int;
param num_trucks: int;
param num_packages: int;
param package_goal_probability: float = 1.0;
param driver_goal_probability: float = 0.0;
param truck_goal_probability: float = 0.0;
param edge_probability: float = 0.5;

require valid_counts: num_locations >= 2 and num_drivers >= 1 and num_trucks >= 1 and num_packages >= 1;
require valid_probabilities: package_goal_probability >= 0 and package_goal_probability <= 1 and driver_goal_probability >= 0 and driver_goal_probability <= 1 and truck_goal_probability >= 0 and truck_goal_probability <= 1 and edge_probability > 0 and edge_probability <= 1;
let Locations = names("s", num_locations);
let Drivers = names("driver", num_drivers, 1);
let Trucks = names("truck", num_trucks, 1);
let Packages = names("package", num_packages, 1);
let Moving = Drivers + Trucks + Packages;
objects Locations: location;
objects Drivers: driver;
objects Trucks: truck;
objects Packages: obj;
relation initial.link(Locations, Locations);
relation initial.path(Locations, Locations);
relation initial.at(Moving, Locations);
relation initial.empty(Trucks);
relation goal.at(Moving, Locations);
aux road_rank[l in Locations]: int(0, num_locations - 1);
aux foot_rank[l in Locations]: int(0, num_locations - 1);
initial {
 rule road_symmetry: forall a in Locations, b in Locations: initial.link(a,b) iff initial.link(b,a);
 rule foot_symmetry: forall a in Locations, b in Locations: initial.path(a,b) iff initial.path(b,a);
 rule no_loops: forall l in Locations: not initial.link(l,l) and not initial.path(l,l);
 rule complete_boundary: forall a in Locations, b in Locations where a != b: if edge_probability == 1 then initial.link(a,b) and initial.path(a,b) else true;
 rule root_ranks: road_rank[Locations[0]] == 0 and foot_rank[Locations[0]] == 0;
 rule road_connected: forall l in Locations where l != Locations[0]: exists p in Locations: initial.link(l,p) and road_rank[p] < road_rank[l];
 rule foot_connected: forall l in Locations where l != Locations[0]: exists p in Locations: initial.path(l,p) and foot_rank[p] < foot_rank[l];
 rule positions: forall o in Moving: count(l in Locations: initial.at(o,l)) == 1;
 rule empty_trucks: forall t in Trucks: initial.empty(t);
}
goal {
 rule partial_destinations: forall o in Moving: count(l in Locations: goal.at(o,l)) <= 1;
 rule driver_endpoints: forall o in Drivers: if driver_goal_probability == 0 then count(l in Locations: goal.at(o,l)) == 0 else if driver_goal_probability == 1 then count(l in Locations: goal.at(o,l)) == 1 else true;
 rule truck_endpoints: forall o in Trucks: if truck_goal_probability == 0 then count(l in Locations: goal.at(o,l)) == 0 else if truck_goal_probability == 1 then count(l in Locations: goal.at(o,l)) == 1 else true;
 rule package_endpoints: forall o in Packages: if package_goal_probability == 0 then count(l in Locations: goal.at(o,l)) == 0 else if package_goal_probability == 1 then count(l in Locations: goal.at(o,l)) == 1 else true;
 rule driver_repair: if driver_goal_probability > 0 then count(o in Drivers, l in Locations: goal.at(o,l)) >= 1 else true;
 rule truck_repair: if truck_goal_probability > 0 then count(o in Trucks, l in Locations: goal.at(o,l)) >= 1 else true;
 rule package_repair: if package_goal_probability > 0 then count(o in Packages, l in Locations: goal.at(o,l)) >= 1 else true;
}
joint { rule changed_destinations: forall o in Moving, l in Locations: goal.at(o,l) implies not initial.at(o,l); }
