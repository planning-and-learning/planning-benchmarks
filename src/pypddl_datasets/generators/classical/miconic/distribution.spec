language 1;
distribution miconic;
revision "2";
metadata {
    probability "Independent uniform origins and different destinations; one-floor endpoints coincide; lift starts at the lowest floor.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_floors,num_passengers)=(1,1)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_floors: int;
param num_passengers: int;

require valid_counts: num_floors >= 1 and num_passengers >= 1;
let Floors = names("f", num_floors);
let Passengers = names("p", num_passengers);
objects Floors: floor;
objects Passengers: passenger;
relation initial.above(Floors, Floors);
relation initial.lift_at(Floors) as "lift-at";
relation initial.origin(Passengers, Floors);
relation initial.destin(Passengers, Floors);
relation goal.served(Passengers);
initial {
 rule floor_order: forall i in range(num_floors), j in range(num_floors): initial.above(Floors[i],Floors[j]) iff i < j;
 rule lift_start: forall f in Floors: initial.lift_at(f) iff f == Floors[0];
 rule origins: forall p in Passengers: count(f in Floors: initial.origin(p,f)) == 1;
 rule destinations: forall p in Passengers: count(f in Floors: initial.destin(p,f)) == 1;
 rule distinct_endpoints: forall p in Passengers, f in Floors: if num_floors > 1 then not (initial.origin(p,f) and initial.destin(p,f)) else true;
}
goal { rule all_served: forall p in Passengers: goal.served(p); }
joint {}
