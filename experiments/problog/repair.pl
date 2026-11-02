% Logistics/Grid-style Bernoulli subset, repaired only when it is empty.
:- use_module(library(lists)).
0.5::included(a).
0.5::included(b).
empty :- \+ included(a), \+ included(b).
fallback(X) :- select_uniform(fallback,[a,b],X,_).
selected(X) :- included(X).
selected(X) :- empty, fallback(X).
only_a :- selected(a), \+ selected(b).
only_b :- selected(b), \+ selected(a).
both :- selected(a), selected(b).
query(only_a).
query(only_b).
query(both).
