(define (domain Scaled_Move_to_Location_151)
(:requirements :typing :negative-preconditions :universal-preconditions :existential-preconditions :disjunctive-preconditions)
(:types
	locatable int - object
	agent block item - locatable
	count position - int
	bedrock destructible-block - block
	grass_block - item
	grass_block-block - destructible-block
)

(:constants
	steve - agent
	grass_block0 grass_block1 grass_block2 grass_block3 grass_block4 grass_block5 grass_block6 grass_block7 grass_block8 grass_block9 grass_block10 grass_block11 grass_block12 grass_block13 grass_block14 grass_block15 grass_block16 grass_block17 grass_block18 grass_block19 grass_block20 grass_block21 grass_block22 grass_block23 grass_block24 grass_block25 grass_block26 grass_block27 grass_block28 grass_block29 grass_block30 grass_block31 grass_block32 grass_block33 grass_block34 grass_block35 grass_block36 grass_block37 grass_block38 grass_block39 grass_block40 grass_block41 grass_block42 grass_block43 grass_block44 grass_block45 grass_block46 grass_block47 grass_block48 grass_block49 grass_block50 grass_block51 grass_block52 grass_block53 grass_block54 grass_block55 grass_block56 grass_block57 grass_block58 grass_block59 grass_block60 grass_block61 grass_block62 grass_block63 grass_block64 grass_block65 grass_block66 grass_block67 grass_block68 grass_block69 grass_block70 grass_block71 grass_block72 grass_block73 grass_block74 grass_block75 grass_block76 grass_block77 grass_block78 grass_block79 grass_block80 grass_block81 grass_block82 grass_block83 grass_block84 grass_block85 grass_block86 grass_block87 grass_block88 grass_block89 grass_block90 grass_block91 grass_block92 grass_block93 grass_block94 grass_block95 grass_block96 grass_block97 grass_block98 grass_block99 grass_block100 grass_block101 grass_block102 grass_block103 grass_block104 grass_block105 grass_block106 grass_block107 grass_block108 grass_block109 grass_block110 grass_block111 grass_block112 grass_block113 grass_block114 grass_block115 grass_block116 grass_block117 grass_block118 grass_block119 grass_block120 grass_block121 grass_block122 grass_block123 grass_block124 grass_block125 grass_block126 grass_block127 grass_block128 grass_block129 grass_block130 grass_block131 grass_block132 grass_block133 grass_block134 grass_block135 grass_block136 grass_block137 grass_block138 grass_block139 grass_block140 grass_block141 grass_block142 grass_block143 grass_block144 grass_block145 grass_block146 grass_block147 grass_block148 grass_block149 grass_block150 - grass_block
	grass_block-block0 grass_block-block1 grass_block-block2 grass_block-block3 grass_block-block4 grass_block-block5 grass_block-block6 grass_block-block7 grass_block-block8 grass_block-block9 grass_block-block10 grass_block-block11 grass_block-block12 grass_block-block13 grass_block-block14 grass_block-block15 grass_block-block16 grass_block-block17 grass_block-block18 grass_block-block19 grass_block-block20 grass_block-block21 grass_block-block22 grass_block-block23 grass_block-block24 grass_block-block25 grass_block-block26 grass_block-block27 grass_block-block28 grass_block-block29 grass_block-block30 grass_block-block31 grass_block-block32 grass_block-block33 grass_block-block34 grass_block-block35 grass_block-block36 grass_block-block37 grass_block-block38 grass_block-block39 grass_block-block40 grass_block-block41 grass_block-block42 grass_block-block43 grass_block-block44 grass_block-block45 grass_block-block46 grass_block-block47 grass_block-block48 grass_block-block49 grass_block-block50 grass_block-block51 grass_block-block52 grass_block-block53 grass_block-block54 grass_block-block55 grass_block-block56 grass_block-block57 grass_block-block58 grass_block-block59 grass_block-block60 grass_block-block61 grass_block-block62 grass_block-block63 grass_block-block64 grass_block-block65 grass_block-block66 grass_block-block67 grass_block-block68 grass_block-block69 grass_block-block70 grass_block-block71 grass_block-block72 grass_block-block73 grass_block-block74 grass_block-block75 grass_block-block76 grass_block-block77 grass_block-block78 grass_block-block79 grass_block-block80 grass_block-block81 grass_block-block82 grass_block-block83 grass_block-block84 grass_block-block85 grass_block-block86 grass_block-block87 grass_block-block88 grass_block-block89 grass_block-block90 grass_block-block91 grass_block-block92 grass_block-block93 grass_block-block94 grass_block-block95 grass_block-block96 grass_block-block97 grass_block-block98 grass_block-block99 grass_block-block100 grass_block-block101 grass_block-block102 grass_block-block103 grass_block-block104 grass_block-block105 grass_block-block106 grass_block-block107 grass_block-block108 grass_block-block109 grass_block-block110 grass_block-block111 grass_block-block112 grass_block-block113 grass_block-block114 grass_block-block115 grass_block-block116 grass_block-block117 grass_block-block118 grass_block-block119 grass_block-block120 grass_block-block121 grass_block-block122 grass_block-block123 grass_block-block124 grass_block-block125 grass_block-block126 grass_block-block127 grass_block-block128 grass_block-block129 grass_block-block130 grass_block-block131 grass_block-block132 grass_block-block133 grass_block-block134 grass_block-block135 grass_block-block136 grass_block-block137 grass_block-block138 grass_block-block139 grass_block-block140 grass_block-block141 grass_block-block142 grass_block-block143 grass_block-block144 grass_block-block145 grass_block-block146 grass_block-block147 grass_block-block148 grass_block-block149 grass_block-block150 - grass_block-block
	position-76 position-75 position-74 position-73 position-72 position-71 position-70 position-69 position-68 position-67 position-66 position-65 position-64 position-63 position-62 position-61 position-60 position-59 position-58 position-57 position-56 position-55 position-54 position-53 position-52 position-51 position-50 position-49 position-48 position-47 position-46 position-45 position-44 position-43 position-42 position-41 position-40 position-39 position-38 position-37 position-36 position-35 position-34 position-33 position-32 position-31 position-30 position-29 position-28 position-27 position-26 position-25 position-24 position-23 position-22 position-21 position-20 position-19 position-18 position-17 position-16 position-15 position-14 position-13 position-12 position-11 position-10 position-9 position-8 position-7 position-6 position-5 position-4 position-3 position-2 position-1 position0 position1 position2 position3 position4 position5 position6 position7 position8 position9 position10 position11 position12 position13 position14 position15 position16 position17 position18 position19 position20 position21 position22 position23 position24 position25 position26 position27 position28 position29 position30 position31 position32 position33 position34 position35 position36 position37 position38 position39 position40 position41 position42 position43 position44 position45 position46 position47 position48 position49 position50 position51 position52 position53 position54 position55 position56 position57 position58 position59 position60 position61 position62 position63 position64 position65 position66 position67 position68 position69 position70 position71 position72 position73 position74 position75 position76 position77 - position
	count0 count1 count2 count3 count4 count5 count6 count7 count8 count9 count10 count11 count12 count13 count14 count15 count16 count17 count18 count19 count20 count21 count22 count23 count24 count25 count26 count27 count28 count29 count30 count31 count32 count33 count34 count35 count36 count37 count38 count39 count40 count41 count42 count43 count44 count45 count46 count47 count48 count49 count50 count51 count52 count53 count54 count55 count56 count57 count58 count59 count60 count61 count62 count63 count64 - count
)
(:predicates
	(goal-achieved ?ag - agent)
	(not-equal ?x1 - int ?x2 - int)
	(block-present ?b - block)
	(at-z ?l - locatable ?z - position)
	(item-present ?i - item)
	(at-y ?l - locatable ?y - position)
	(agent-alive ?ag - agent)
	(are-seq ?x1 - int ?x2 - int)
	(agent-has-n-grass_block ?ag - agent ?n - count)
	(at-x ?l - locatable ?x - position)
)

(:action move-north
	:parameters (?ag - agent ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?z_start - position ?z_end - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_end ?z_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z_end)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z_end)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_down)
 (at-z ?i ?z_end)
))))
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
)
)


(:action jumpup-north
	:parameters (?ag - agent ?x - position ?y_up - position ?y_up_up - position ?y_down - position ?z_start - position ?z_end - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_end ?z_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_up_up)
 (at-z ?b ?z_start)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z_end)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_down)
 (at-z ?b ?z_end)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_up)
 (at-z ?i ?z_end)
))))
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_up)
)
)


(:action jumpdown-north
	:parameters (?ag - agent ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position ?z_start - position ?z_end - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_end ?z_start)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z_end)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z_end)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (or (at-y ?i ?y_2_down)
) (at-z ?i ?z_end)
))))
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_2_down)
)
)


(:action break-grass_block-north
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?y - position ?y_up - position ?z - position ?z_front - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (at-x ?b ?x)
 (at-y ?b ?y)
 (at-z ?b ?z_front)
 (are-seq ?z_front ?z)
 (are-seq ?y ?y_up)
 (block-present ?b) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_up)
 (at-z ?i ?z_front)
))) (are-seq ?n_start ?n_end)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (block-present ?b)) (not (at-x ?b ?x)
) (not (at-y ?b ?y)
) (not (at-z ?b ?z_front)
) (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action place-grass_block-north
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?y - position ?y_down - position ?z - position ?z_front - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (not (block-present ?b)) (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x)
 (at-y ?bl ?y_down)
 (at-z ?bl ?z_front)
)) (not (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x)
 (at-y ?bl ?y)
 (at-z ?bl ?z_front)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y)
 (at-z ?i ?z_front)
))) (are-seq ?y_down ?y)
 (are-seq ?z_front ?z)
 (are-seq ?n_end ?n_start)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(block-present ?b) (at-x ?b ?x)
 (at-y ?b ?y)
 (at-z ?b ?z_front)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action move_and_pickup-grass_block-north
	:parameters (?ag - agent ?i - grass_block ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?z_start - position ?z_end - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_end ?z_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?n_start ?n_end)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z_end)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z_end)
))) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_down)
 (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (not (at-x ?i ?x)
) (not (at-y ?i ?y_down)
) (not (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)))
)


(:action jumpup_and_pickup-grass_block-north
	:parameters (?ag - agent ?i - grass_block ?x - position ?y_up - position ?y_up_up - position ?y_down - position ?z_start - position ?z_end - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_end ?z_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z_end)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z_start)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_down)
 (at-z ?b ?z_end)
)) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_up)
 (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-z ?ag ?z_start)
) (not (at-y ?ag ?y_down)
) (at-z ?ag ?z_end)
 (at-y ?ag ?y_up)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z_end)
))
)


(:action jumpdown_and_pickup-grass_block-north
	:parameters (?ag - agent ?i - grass_block ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position ?z_start - position ?z_end - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_end ?z_start)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z_end)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z_end)
)) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_2_down)
 (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-z ?ag ?z_start)
) (not (at-y ?ag ?y_down)
) (at-z ?ag ?z_end)
 (at-y ?ag ?y_2_down)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z_end)
))
)


(:action move-south
	:parameters (?ag - agent ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?z_start - position ?z_end - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_start ?z_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z_end)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z_end)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_down)
 (at-z ?i ?z_end)
))))
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
)
)


(:action jumpup-south
	:parameters (?ag - agent ?x - position ?y_up - position ?y_up_up - position ?y_down - position ?z_start - position ?z_end - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_start ?z_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_up_up)
 (at-z ?b ?z_start)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z_end)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_down)
 (at-z ?b ?z_end)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_up)
 (at-z ?i ?z_end)
))))
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_up)
)
)


(:action jumpdown-south
	:parameters (?ag - agent ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position ?z_start - position ?z_end - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_start ?z_end)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z_end)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z_end)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (or (at-y ?i ?y_2_down)
) (at-z ?i ?z_end)
))))
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_2_down)
)
)


(:action break-grass_block-south
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?y - position ?y_up - position ?z - position ?z_front - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (at-x ?b ?x)
 (at-y ?b ?y)
 (at-z ?b ?z_front)
 (are-seq ?z ?z_front)
 (are-seq ?y ?y_up)
 (block-present ?b) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_up)
 (at-z ?i ?z_front)
))) (are-seq ?n_start ?n_end)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (block-present ?b)) (not (at-x ?b ?x)
) (not (at-y ?b ?y)
) (not (at-z ?b ?z_front)
) (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action place-grass_block-south
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?y - position ?y_down - position ?z - position ?z_front - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (not (block-present ?b)) (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x)
 (at-y ?bl ?y_down)
 (at-z ?bl ?z_front)
)) (not (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x)
 (at-y ?bl ?y)
 (at-z ?bl ?z_front)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y)
 (at-z ?i ?z_front)
))) (are-seq ?y_down ?y)
 (are-seq ?z ?z_front)
 (are-seq ?n_end ?n_start)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(block-present ?b) (at-x ?b ?x)
 (at-y ?b ?y)
 (at-z ?b ?z_front)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action move_and_pickup-grass_block-south
	:parameters (?ag - agent ?i - grass_block ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?z_start - position ?z_end - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_start ?z_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?n_start ?n_end)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z_end)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z_end)
))) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_down)
 (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-z ?ag ?z_start)
) (at-z ?ag ?z_end)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (not (at-x ?i ?x)
) (not (at-y ?i ?y_down)
) (not (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)))
)


(:action jumpup_and_pickup-grass_block-south
	:parameters (?ag - agent ?i - grass_block ?x - position ?y_up - position ?y_up_up - position ?y_down - position ?z_start - position ?z_end - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_start ?z_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z_end)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z_start)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_down)
 (at-z ?b ?z_end)
)) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_up)
 (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-z ?ag ?z_start)
) (not (at-y ?ag ?y_down)
) (at-z ?ag ?z_end)
 (at-y ?ag ?y_up)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z_end)
))
)


(:action jumpdown_and_pickup-grass_block-south
	:parameters (?ag - agent ?i - grass_block ?x - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position ?z_start - position ?z_end - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z_start)
 (are-seq ?z_start ?z_end)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z_end)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z_end)
)) (and 
(item-present ?i)
 (at-x ?i ?x)
 (at-y ?i ?y_2_down)
 (at-z ?i ?z_end)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-z ?ag ?z_start)
) (not (at-y ?ag ?y_down)
) (at-z ?ag ?z_end)
 (at-y ?ag ?y_2_down)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z_end)
))
)


(:action move-east
	:parameters (?ag - agent ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_start ?x_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_down)
 (at-z ?i ?z)
))))
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
)
)


(:action jumpup-east
	:parameters (?ag - agent ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_up_up - position ?y_down - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_start ?x_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_start)
 (at-y ?b ?y_up_up)
 (at-z ?b ?z)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_down)
 (at-z ?b ?z)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_up)
 (at-z ?i ?z)
))))
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_up)
)
)


(:action jumpdown-east
	:parameters (?ag - agent ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_start ?x_end)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (or (at-y ?i ?y_2_down)
) (at-z ?i ?z)
))))
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_2_down)
)
)


(:action break-grass_block-east
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?x_front - position ?y - position ?y_up - position ?z - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (at-x ?b ?x_front)
 (at-y ?b ?y)
 (at-z ?b ?z)
 (are-seq ?x ?x_front)
 (are-seq ?y ?y_up)
 (block-present ?b) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_front)
 (at-y ?i ?y_up)
 (at-z ?i ?z)
))) (are-seq ?n_start ?n_end)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (block-present ?b)) (not (at-x ?b ?x_front)
) (not (at-y ?b ?y)
) (not (at-z ?b ?z)
) (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action place-grass_block-east
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?x_front - position ?y - position ?y_down - position ?z - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (not (block-present ?b)) (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x_front)
 (at-y ?bl ?y_down)
 (at-z ?bl ?z)
)) (not (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x_front)
 (at-y ?bl ?y)
 (at-z ?bl ?z)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_front)
 (at-y ?i ?y)
 (at-z ?i ?z)
))) (are-seq ?y_down ?y)
 (are-seq ?x ?x_front)
 (are-seq ?n_end ?n_start)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(block-present ?b) (at-x ?b ?x_front)
 (at-y ?b ?y)
 (at-z ?b ?z)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action move_and_pickup-grass_block-east
	:parameters (?ag - agent ?i - grass_block ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_start ?x_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?n_start ?n_end)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z)
))) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_down)
 (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (not (at-x ?i ?x_end)
) (not (at-y ?i ?y_down)
) (not (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)))
)


(:action jumpup_and_pickup-grass_block-east
	:parameters (?ag - agent ?i - grass_block ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_up_up - position ?y_down - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_start ?x_end)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_start)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_down)
 (at-z ?b ?z)
)) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_up)
 (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-x ?ag ?x_start)
) (not (at-y ?ag ?y_down)
) (at-x ?ag ?x_end)
 (at-y ?ag ?y_up)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x_end)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z)
))
)


(:action jumpdown_and_pickup-grass_block-east
	:parameters (?ag - agent ?i - grass_block ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_start ?x_end)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z)
)) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_2_down)
 (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-x ?ag ?x_start)
) (not (at-y ?ag ?y_down)
) (at-x ?ag ?x_end)
 (at-y ?ag ?y_2_down)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x_end)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z)
))
)


(:action move-west
	:parameters (?ag - agent ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_end ?x_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_down)
 (at-z ?i ?z)
))))
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
)
)


(:action jumpup-west
	:parameters (?ag - agent ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_up_up - position ?y_down - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_end ?x_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_start)
 (at-y ?b ?y_up_up)
 (at-z ?b ?z)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_down)
 (at-z ?b ?z)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_up)
 (at-z ?i ?z)
))))
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_up)
)
)


(:action jumpdown-west
	:parameters (?ag - agent ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_end ?x_start)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z)
)) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (or (at-y ?i ?y_2_down)
) (at-z ?i ?z)
))))
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
 (not (at-y ?ag ?y_down)
) (at-y ?ag ?y_2_down)
)
)


(:action break-grass_block-west
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?x_front - position ?y - position ?y_up - position ?z - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (at-x ?b ?x_front)
 (at-y ?b ?y)
 (at-z ?b ?z)
 (are-seq ?x_front ?x)
 (are-seq ?y ?y_up)
 (block-present ?b) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_front)
 (at-y ?i ?y_up)
 (at-z ?i ?z)
))) (are-seq ?n_start ?n_end)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (block-present ?b)) (not (at-x ?b ?x_front)
) (not (at-y ?b ?y)
) (not (at-z ?b ?z)
) (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action place-grass_block-west
	:parameters (?ag - agent ?b - grass_block-block ?x - position ?x_front - position ?y - position ?y_down - position ?z - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x)
 (at-y ?ag ?y)
 (at-z ?ag ?z)
 (not (block-present ?b)) (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x_front)
 (at-y ?bl ?y_down)
 (at-z ?bl ?z)
)) (not (exists (?bl - block) (and 
(block-present ?bl)
 (at-x ?bl ?x_front)
 (at-y ?bl ?y)
 (at-z ?bl ?z)
))) (not (exists (?i - item) (and 
(item-present ?i)
 (at-x ?i ?x_front)
 (at-y ?i ?y)
 (at-z ?i ?z)
))) (are-seq ?y_down ?y)
 (are-seq ?x_front ?x)
 (are-seq ?n_end ?n_start)
 (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(block-present ?b) (at-x ?b ?x_front)
 (at-y ?b ?y)
 (at-z ?b ?z)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
)
)


(:action move_and_pickup-grass_block-west
	:parameters (?ag - agent ?i - grass_block ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_end ?x_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?n_start ?n_end)
 (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_2_down)
 (at-z ?b ?z)
)) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
) (at-z ?b ?z)
))) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_down)
 (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-x ?ag ?x_start)
) (at-x ?ag ?x_end)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (not (at-x ?i ?x_end)
) (not (at-y ?i ?y_down)
) (not (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)))
)


(:action jumpup_and_pickup-grass_block-west
	:parameters (?ag - agent ?i - grass_block ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_up_up - position ?y_down - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_end ?x_start)
 (are-seq ?y_down ?y_up)
 (are-seq ?y_up ?y_up_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z)
))) (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_start)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_up_up)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_down)
 (at-z ?b ?z)
)) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_up)
 (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-x ?ag ?x_start)
) (not (at-y ?ag ?y_down)
) (at-x ?ag ?x_end)
 (at-y ?ag ?y_up)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x_end)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z)
))
)


(:action jumpdown_and_pickup-grass_block-west
	:parameters (?ag - agent ?i - grass_block ?z - position ?x_start - position ?x_end - position ?y_up - position ?y_down - position ?y_2_down - position ?y_3_down - position ?n_start - count ?n_end - count)
	:precondition (and 
(agent-alive ?ag)
 (at-x ?ag ?x_start)
 (at-y ?ag ?y_down)
 (at-z ?ag ?z)
 (are-seq ?x_end ?x_start)
 (are-seq ?y_3_down ?y_2_down)
 (are-seq ?y_2_down ?y_down)
 (are-seq ?y_down ?y_up)
 (are-seq ?n_start ?n_end)
 (not (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (or (at-y ?b ?y_up)
 (at-y ?b ?y_down)
 (at-y ?b ?y_2_down)
) (at-z ?b ?z)
))) (exists (?b - block) (and 
(block-present ?b)
 (at-x ?b ?x_end)
 (at-y ?b ?y_3_down)
 (at-z ?b ?z)
)) (and 
(item-present ?i)
 (at-x ?i ?x_end)
 (at-y ?i ?y_2_down)
 (at-z ?i ?z)
) (agent-has-n-grass_block ?ag ?n_start)
)
	:effect (and 
(not (at-x ?ag ?x_start)
) (not (at-y ?ag ?y_down)
) (at-x ?ag ?x_end)
 (at-y ?ag ?y_2_down)
 (not (agent-has-n-grass_block ?ag ?n_start)
) (agent-has-n-grass_block ?ag ?n_end)
 (not (item-present ?i)) (not (at-x ?i ?x_end)
) (not (at-y ?i ?y_up)
) (not (at-z ?i ?z)
))
)


(:action checkgoal
	:parameters (?ag - agent)
	:precondition (and 
(agent-alive ?ag)
 (and 
(at-x ?ag position75)
 (at-y ?ag position4)
 (at-z ?ag position0)
)  )
	:effect (and 
(goal-achieved ?ag))
)


)