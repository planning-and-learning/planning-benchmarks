% Parameters supplied as facts: num_cars(N), num_locations(N).
% This one model supports both joint sampling and exact probability inference.
:- use_module(library(lists)).
:- use_module(library(string)).

car(C) :- num_cars(N), Last is N-1, between(0,Last,I), concat([c,I],C).
location(L) :- num_locations(N), Last is N-1, between(0,Last,I), concat([l,I],L).
locations(Ls) :- findall(L, location(L), Ls).

origin(C,L) :- car(C), locations(Ls), select_uniform(origin(C),Ls,L,_).
destination(C,L) :- car(C), locations(Ls), select_uniform(destination(C),Ls,L,_).
ferry_location(L) :- locations(Ls), select_uniform(ferry,Ls,L,_).

object(C,untyped) :- car(C).
object(L,untyped) :- location(L).
initial(car(C)) :- car(C).
initial(location(L)) :- location(L).
initial('not-eq'(A,B)) :- location(A), location(B), A \= B.
initial('empty-ferry').
initial(at(C,L)) :- origin(C,L).
initial('at-ferry'(L)) :- ferry_location(L).
goal(at(C,L)) :- destination(C,L).

domain(ferry).
problem_name(Name) :- num_cars(C), num_locations(L), concat(['ferry-l',L,'-c',C],Name).
