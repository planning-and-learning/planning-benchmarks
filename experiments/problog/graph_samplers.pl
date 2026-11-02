% Experimental, domain-independent graph distributions. All sampling stays in
% ProbLog; only the existing generic choice primitives use native acceleration.

% Uniform integer without materializing the complete integer interval.
graph_integer(_,Low,Low,Low).
graph_integer(Id,Low,High,V) :- Low<High,Mid is (Low+High)//2,
    Left is Mid-Low+1,Total is High-Low+1,
    bernoulli_member(interval(Id,Low,High),Left/Total,left),
    graph_integer(Id,Low,Mid,V).
graph_integer(Id,Low,High,V) :- Low<High,Mid is (Low+High)//2,
    Left is Mid-Low+1,Total is High-Low+1,
    \+ bernoulli_member(interval(Id,Low,High),Left/Total,left),
    Next is Mid+1,graph_integer(Id,Next,High,V).

% A shuffled vertex order followed by uniform attachment to an earlier vertex.
% This is a random recursive tree with shuffled labels, not a uniform tree.
growing_tree(Id,Vertices,Tree) :- uniform_choice(root(Id),Vertices,Root,Rest),
    grow_tree(Id,1,Rest,[Root],Edges),sort(Edges,Tree).
grow_tree(_,_,[],_,[]).
grow_tree(Id,Step,Remaining,Seen,[e(A,B)|Edges]) :- Remaining\=[],
    uniform_choice(vertex(Id,Step),Remaining,V,Rest),
    uniform_choice(parent(Id,Step),Seen,P,_),A is min(V,P),B is max(V,P),
    Next is Step+1,grow_tree(Id,Next,Rest,[V|Seen],Edges).

% Uniform fixed-cardinality subset in one pass, retaining input order.
% K/N is an exact probability expression; it is never rounded with `is`.
graph_subset(_,0,_,_,[]).
graph_subset(_,K,K,Values,Values) :- K>0.
graph_subset(Id,K,N,[X|Xs],[X|Selected]) :- K>0,K<N,
    bernoulli_member(subset(Id,N,K),K/N,X),NextK is K-1,NextN is N-1,
    graph_subset(Id,NextK,NextN,Xs,Selected).
graph_subset(Id,K,N,[X|Xs],Selected) :- K>0,K<N,
    \+ bernoulli_member(subset(Id,N,K),K/N,X),NextN is N-1,
    graph_subset(Id,K,NextN,Xs,Selected).

% IPC 2023: uniform total edge count, then uniform missing-edge subset.
tree_plus_edges(Id,N,Tree,Total,Edges,Extra) :- Last is N-1,
    findall(e(A,B),(between(0,Last,A),between(0,Last,B),A<B,
        \+ ground_member(e(A,B),Tree)),Missing),
    length(Tree,T),length(Missing,M),K is Total-T,
    graph_subset(Id,K,M,Missing,Extra),append(Tree,Extra,Edges).

% Sparse structural proxy: fixed count of random endpoint-pair attempts,
% discarding loops/duplicates, and retaining the connected tree backbone.
sparse_tree_edges(Id,N,Tree,Attempts,Edges,Extra) :-
    findall(e(A,B),(between(1,Attempts,I),Last is N-1,
        graph_integer(endpoint(Id,I,left),0,Last,U),
        graph_integer(endpoint(Id,I,right),0,Last,V),U\=V,
        A is min(U,V),B is max(U,V)),Proposals),
    append(Tree,Proposals,All),sort(All,Edges),
    findall(E,(ground_member(E,Edges),\+ ground_member(E,Tree)),Extra).

backbone_subgraph(Id,Tree,Extra,P,Graph) :-
    bernoulli_subset(Id,P,Extra,Selected),append(Tree,Selected,Graph).
