language 1;
distribution barman;
revision "2";
metadata {
    probability "Uniform ordered distinct recipe ingredients; uniform goal-shot subset; independent ingredient/cocktail mixture and uniform beverage choices.";
    solvability "guaranteed";
    scope "membership and structural corner cases";
    cases ["(num_cocktails,num_ingredients,num_shots)=(1,2,2); mixture probability 0,1e-6,0.999999,1"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_cocktails: int;
param num_ingredients: int;
param num_shots: int;
param ingredient_goal_probability: float = 0.0;
param num_goals: int? = none;

require counts: num_cocktails >= 1 and num_ingredients >= 2 and num_shots >= 2;
require probability: ingredient_goal_probability >= 0 and ingredient_goal_probability <= 1;
let GoalCount = if num_goals == none then num_shots - 1 else num_goals;
require goal_count: GoalCount >= 1 and GoalCount <= num_shots;
let Cocktails = names("cocktail", num_cocktails, 1);
let Ingredients = names("ingredient", num_ingredients, 1);
let Dispensers = names("dispenser", num_ingredients, 1);
let Shots = names("shot", num_shots, 1);
let Hands = ["left", "right"];
let Shakers = ["shaker1"];
let Levels = ["l0", "l1", "l2"];
let Containers = Shakers + Shots;
let Beverages = if ingredient_goal_probability == 0 then Cocktails else if ingredient_goal_probability == 1 then Ingredients else Ingredients + Cocktails;
objects Cocktails: cocktail;
objects Ingredients: ingredient;
objects Dispensers: dispenser;
objects Shots: shot;
objects Hands: hand;
objects Shakers: shaker;
objects Levels: level;
relation initial.handempty(Hands);
relation initial.ontable(Containers);
relation initial.clean(Containers);
relation initial.empty(Containers);
relation initial.shaker_empty_level(Shakers, Levels) as "shaker-empty-level";
relation initial.shaker_level(Shakers, Levels) as "shaker-level";
relation initial.dispenses(Dispensers, Ingredients);
relation initial.next(Levels, Levels);
relation initial.cocktail_part1(Cocktails, Ingredients) as "cocktail-part1";
relation initial.cocktail_part2(Cocktails, Ingredients) as "cocktail-part2";
relation goal.contains(Shots, Beverages);
number initial.total_cost(): int(0, 0) as "total-cost";
metric minimize initial.total_cost();
initial {
 rule hands_empty: forall h in Hands: initial.handempty(h);
 rule clean_empty_containers: forall c in Containers: initial.ontable(c) and initial.clean(c) and initial.empty(c);
 rule empty_shaker_level: forall l in Levels: initial.shaker_empty_level("shaker1",l) iff l == "l0";
 rule initial_shaker_level: forall l in Levels: initial.shaker_level("shaker1",l) iff l == "l0";
 rule dispensers: forall i in range(num_ingredients), j in range(num_ingredients): initial.dispenses(Dispensers[i],Ingredients[j]) iff i == j;
 rule levels: forall i in range(3), j in range(3): initial.next(Levels[i],Levels[j]) iff j == i + 1;
 rule first_ingredient: forall c in Cocktails: count(i in Ingredients: initial.cocktail_part1(c,i)) == 1;
 rule second_ingredient: forall c in Cocktails: count(i in Ingredients: initial.cocktail_part2(c,i)) == 1;
 rule different_ingredients: forall c in Cocktails, i in Ingredients: not (initial.cocktail_part1(c,i) and initial.cocktail_part2(c,i));
}
goal {
 rule one_beverage_per_shot: forall s in Shots: count(b in Beverages: goal.contains(s,b)) <= 1;
 rule requested_shots: count(s in Shots, b in Beverages: goal.contains(s,b)) == GoalCount;
}
joint {}
