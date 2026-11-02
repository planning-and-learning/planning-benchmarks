language 1;
distribution nomystery;
revision "2";
metadata {
    probability "Bernoulli edges conditioned on connectivity; independent uniform positive edge costs and positions, different package destinations; fuel equals int(constrainedness * optimum), using Python float multiplication then truncation.";
    solvability "when scaled fuel >= optimum; floating-point scaling can round down for very large costs";
    scope "bounded whole-task support for the declared tiny case; sampled membership elsewhere";
    cases ["2 locations, 1 package, edge cost 1: all 4 tasks; 2..3 locations and 1..2 packages: independent weighted-optimum and membership checks"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_locations: int = 6;
param num_packages: int = 6;
param edge_factor: float = 1.5;
param max_edge_cost: int = 25;
param constrainedness: float = 1.0;
param edge_probability: float? = 0.5;

require positive_counts: num_locations >= 2 and num_packages >= 1 and max_edge_cost >= 1;
require density_and_fuel_factors: edge_factor >= 1 and constrainedness >= 1;
let Probability = if edge_probability == none then min(1.0, 2 * edge_factor / (num_locations - 1)) else edge_probability;
require graph_probability: Probability > 0 and Probability <= 1;

# Serving packages separately uses at most 2P simple paths, each with N-1 edges.
let OptimumBound = 2 * num_packages * (num_locations - 1) * max_edge_cost;
let LevelBound = max(max_edge_cost, trunc(constrainedness * OptimumBound));
let LocationIndices = range(num_locations);
let PackageIndices = range(num_packages);
let CostIndices = range(1, max_edge_cost + 1);
let FuelIndices = range(LevelBound + 1);
let OptimumValues = range(OptimumBound + 1);
let Locations = names("l", num_locations);
let Packages = names("p", num_packages);
let Trucks = ["t0"];
let Movables = Trucks + Packages;
let Levels = names("level", LevelBound + 1);
let CostLevels = names("level", max_edge_cost, 1);

# Status digits are waiting=0, carried=1, delivered=2. The complete finite
# Bellman system supplies an independent exact optimum, not a bounded rollout.
let StatusCount = 3 ** num_packages;
let Statuses = range(StatusCount);
let Powers[p in PackageIndices] = 3 ** p;
let Stage[s in Statuses, p in PackageIndices] = (s // Powers[p]) % 3;
let ScaledFuel[c in OptimumValues] = trunc(constrainedness * c);

objects Locations: location;
objects Packages: package;
objects Trucks: truck;
objects Levels: fuellevel optional;

relation initial.connected(Locations, Locations);
relation initial.fuelcost(CostLevels, Locations, Locations);
relation initial.at(Movables, Locations);
relation initial.fuel(Trucks, Levels);
relation goal.at(Packages, Locations);
# The addition table is sparse: undefined triples remain outside the vocabulary.
relation initial.sum[a in FuelIndices, c in CostIndices where a + c <= LevelBound](Levels[a], Levels[c], Levels[a + c]);
number initial.total_cost(): int(0, 0) as "total-cost";
metric minimize initial.total_cost();

aux connection_rank[l in LocationIndices]: int(0, num_locations - 1);
aux road_cost[a in LocationIndices, b in LocationIndices]: int(0, max_edge_cost);
aux distance[s in Statuses, l in LocationIndices]: int(0, OptimumBound);
aux optimum: int(0, OptimumBound);
aux initial_fuel: int(0, LevelBound);
aux maximum_fuel: int(max_edge_cost, LevelBound);
aux cost_used[c in CostIndices]: bool;

initial {
    rule simple_roads: forall l in Locations: not initial.connected(l, l);
    rule symmetric_roads: forall a in Locations, b in Locations:
        initial.connected(a, b) iff initial.connected(b, a);
    rule probability_one_roads: forall a in Locations, b in Locations where Probability == 1 and a != b:
        initial.connected(a, b);
    rule connection_root: connection_rank[0] == 0;
    rule connected_graph: forall l in LocationIndices where l > 0:
        exists predecessor in LocationIndices where predecessor != l:
            initial.connected(Locations[l], Locations[predecessor]) and connection_rank[predecessor] < connection_rank[l];
    rule one_cost_per_road: forall a in Locations, b in Locations:
        count(c in CostLevels: initial.fuelcost(c, a, b)) == (if initial.connected(a, b) then 1 else 0);
    rule symmetric_costs: forall c in CostLevels, a in Locations, b in Locations:
        initial.fuelcost(c, a, b) iff initial.fuelcost(c, b, a);
    rule complete_placements: forall x in Movables: count(l in Locations: initial.at(x, l)) == 1;
    rule zero_total_cost: initial.total_cost() == 0;
}

goal {
    rule package_destinations: forall p in Packages: count(l in Locations: goal.at(p, l)) == 1;
}

joint {
    rule different_endpoints: forall p in Packages, l in Locations:
        not (initial.at(p, l) and goal.at(p, l));
    rule encoded_road_cost: forall a in LocationIndices, b in LocationIndices:
        road_cost[a, b] == sum(c in CostIndices: if initial.fuelcost(Levels[c], Locations[a], Locations[b]) then c else 0);

    # Every nonterminal state's cost is no greater than any enabled successor
    # and is attained by one of them. Zero-cost transitions strictly advance a
    # package digit; positive road costs preclude an equality-attaining cycle.
    rule terminal_distances: forall l in LocationIndices: distance[StatusCount - 1, l] == 0;
    rule bellman_drive_bounds: forall s in Statuses, a in LocationIndices, b in LocationIndices where s != StatusCount - 1 and a != b:
        initial.connected(Locations[a], Locations[b]) implies distance[s, a] <= road_cost[a, b] + distance[s, b];
    rule bellman_service_bounds: forall s in Statuses, l in LocationIndices, p in PackageIndices where s != StatusCount - 1 and Stage[s, p] < 2:
        (if Stage[s, p] == 0 then initial.at(Packages[p], Locations[l]) else goal.at(Packages[p], Locations[l]))
        implies distance[s, l] <= distance[s + Powers[p], l];
    rule bellman_attaining_successor: forall s in Statuses, l in LocationIndices where s != StatusCount - 1:
        (exists other in LocationIndices where other != l:
            initial.connected(Locations[l], Locations[other]) and distance[s, l] == road_cost[l, other] + distance[s, other])
        or (exists p in PackageIndices where Stage[s, p] < 2:
            (if Stage[s, p] == 0 then initial.at(Packages[p], Locations[l]) else goal.at(Packages[p], Locations[l]))
            and distance[s, l] == distance[s + Powers[p], l]);
    rule initial_route_optimum:
        optimum == sum(l in LocationIndices: if initial.at("t0", Locations[l]) then distance[0, l] else 0);

    # The lookup preserves the legacy binary64 multiply-then-truncate law.
    # Rational multiplication would change support at floating-point boundaries.
    rule scaled_optimal_fuel:
        initial_fuel == sum(c in OptimumValues: if optimum == c then ScaledFuel[c] else 0);
    rule maximum_fuel_level:
        maximum_fuel == (if initial_fuel > max_edge_cost then initial_fuel else max_edge_cost);
    rule fuel_value: forall l in FuelIndices: initial.fuel("t0", Levels[l]) iff initial_fuel == l;
    rule fuel_level_prefix: forall l in FuelIndices: present(Levels[l]) iff l <= maximum_fuel;
    rule used_road_costs: forall c in CostIndices:
        cost_used[c] iff (exists a in Locations, b in Locations where a != b: initial.fuelcost(Levels[c], a, b));
    rule complete_addition_table: forall a in FuelIndices, c in CostIndices where a + c <= LevelBound:
        initial.sum(Levels[a], Levels[c], Levels[a + c]) iff (cost_used[c] and a + c <= maximum_fuel);
}
