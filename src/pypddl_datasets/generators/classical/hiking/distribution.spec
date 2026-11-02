language 1;
distribution hiking;
revision "2";
metadata {
    probability "Independent fair up/down tent states; fixed route and starting positions.";
    solvability "not asserted for arbitrary positive car counts";
    scope "membership and structural corner cases";
    cases ["(num_couples,num_cars,num_places)=(1,1,2)"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_couples: int;
param num_cars: int;
param num_places: int;

require valid_counts: num_couples >= 1 and num_cars >= 1 and num_places >= 2;
let Couples = names("couple", num_couples);
let Cars = names("car", num_cars);
let Tents = names("tent", num_couples);
let Places = names("place", num_places);
let Guy[i in range(num_couples)] = "guy" + str(i);
let Girl[i in range(num_couples)] = "girl" + str(i);
let People = values(Guy) + values(Girl);
objects Couples: couple;
objects Cars: car;
objects Tents: tent;
objects Places: place;
objects People: person;
relation initial.at_person(People, Places);
relation initial.at_car(Cars, Places);
relation initial.at_tent(Tents, Places);
relation initial.walked(Couples, Places);
relation initial.next(Places, Places);
relation initial.up(Tents);
relation initial.down(Tents);
relation initial.partners(Couples, People, People);
relation goal.walked(Couples, Places);
initial {
 rule partners: forall i in range(num_couples), p in People, q in People: initial.partners(Couples[i],p,q) iff (p == Guy[i] and q == Girl[i]);
 rule people_start: forall p in People, l in Places: initial.at_person(p,l) iff l == Places[0];
 rule cars_start: forall c in Cars, l in Places: initial.at_car(c,l) iff l == Places[0];
 rule tents_start: forall t in Tents, l in Places: initial.at_tent(t,l) iff l == Places[0];
 rule walked_start: forall c in Couples, l in Places: initial.walked(c,l) iff l == Places[0];
 rule route: forall i in range(num_places), j in range(num_places): initial.next(Places[i],Places[j]) iff j == i + 1;
 rule tent_state: forall t in Tents: initial.up(t) iff not initial.down(t);
}
goal { rule finish: forall c in Couples, l in Places: goal.walked(c,l) iff l == Places[num_places - 1]; }
joint {}
