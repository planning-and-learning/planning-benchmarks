language 1;
distribution tpp;
revision "2";
metadata {
    probability "Independent uniform depot starts and uniform positive stock at every market.";
    solvability "not asserted: stock may be insufficient";
    scope "membership and structural corner cases";
    cases ["(num_goods,num_trucks,num_markets,num_depots,max_level)=(1,1,1,1,2)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_goods: int;
param num_trucks: int;
param num_markets: int;
param num_depots: int;
param max_level: int;

require valid_counts: num_goods >= 1 and num_trucks >= 1 and num_markets >= 1 and num_depots >= 1 and max_level >= 1;
let Goods = names("goods", num_goods);
let Trucks = names("truck", num_trucks);
let Markets = names("market", num_markets);
let Depots = names("depot", num_depots);
let Places = Depots + Markets;
let Levels = names("level", max_level + 1);
objects Goods: goods;
objects Trucks: truck;
objects Markets: market;
objects Depots: depot;
objects Levels: level;
relation initial.next(Levels, Levels);
relation initial.connected(Places, Places);
relation initial.at(Trucks, Places);
relation initial.stored(Goods, Levels);
relation initial.loaded(Goods, Trucks, Levels);
relation initial.on_sale(Goods, Markets, Levels) as "on-sale";
relation initial.ready_to_load(Goods, Markets, Levels) as "ready-to-load";
relation goal.stored(Goods, Levels);
initial {
 rule level_order: forall i in range(max_level + 1), j in range(max_level + 1): initial.next(Levels[i],Levels[j]) iff i == j + 1;
 rule complete_roads: forall a in Places, b in Places: initial.connected(a,b) iff a != b;
 rule truck_depot: forall t in Trucks: count(d in Depots: initial.at(t,d)) == 1;
 rule no_truck_market: forall t in Trucks, m in Markets: not initial.at(t,m);
 rule empty_storage: forall g in Goods, l in Levels: initial.stored(g,l) iff l == Levels[0];
 rule empty_loads: forall g in Goods, t in Trucks, l in Levels: initial.loaded(g,t,l) iff l == Levels[0];
 rule empty_ready: forall g in Goods, m in Markets, l in Levels: initial.ready_to_load(g,m,l) iff l == Levels[0];
 rule stock_level: forall g in Goods, m in Markets: count(l in Levels: initial.on_sale(g,m,l)) == 1;
 rule positive_stock: forall g in Goods, m in Markets: not initial.on_sale(g,m,Levels[0]);
}
goal { rule requested_stock: forall g in Goods, l in Levels: goal.stored(g,l) iff l == Levels[max_level]; }
joint {}
