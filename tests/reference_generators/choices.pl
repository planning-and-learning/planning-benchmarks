% Generic finite choices. Keep ratios as probability expressions: computing
% Weight is 1/N first would introduce binary64 bias into discrete uniform draws.
:- use_module(library(lists)).
(1/N)::uniform_head(Id,N,X,Xs).
uniform_choice(_, [X], X, []).
uniform_choice(Id,[X|Xs],X,Xs) :- Xs \= [], length([X|Xs],N), uniform_head(Id,N,X,Xs).
uniform_choice(Id,[X|Xs],V,[X|Rest]) :- Xs \= [], length([X|Xs],N),
    \+ uniform_head(Id,N,X,Xs), uniform_choice(Id,Xs,V,Rest).
uniform_int(Id,Low,High,V) :- numlist(Low,High,Values), uniform_choice(Id,Values,V,_).

(W/Total)::weighted_head(Id,W,Total,X,Xs).
weighted_choice(Id,Weights,Values,V,Rest) :- sum_list(Weights,Total), Total > 0,
    weighted_choice_remaining(Id,Total,Weights,Values,V,Rest).
weighted_choice_remaining(_,_,[W],[X],X,[]) :- W > 0.
weighted_choice_remaining(Id,Total,[W|Ws],[X|Xs],X,Xs) :- Xs \= [], Total > 0,
    weighted_head(Id,W,Total,X,Xs).
weighted_choice_remaining(Id,Total,[W|Ws],[X|Xs],V,[X|Rest]) :- Xs \= [], Total > 0,
    \+ weighted_head(Id,W,Total,X,Xs), Remaining is Total-W,
    weighted_choice_remaining(Id,Remaining,Ws,Xs,V,Rest).
