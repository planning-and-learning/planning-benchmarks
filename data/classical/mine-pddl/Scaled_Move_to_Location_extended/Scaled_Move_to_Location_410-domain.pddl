(define (domain Scaled_Move_to_Location_410)
(:requirements :strips :disjunctive-preconditions :existential-preconditions :negative-preconditions :typing)
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
	grass_block0 grass_block1 grass_block2 grass_block3 grass_block4 grass_block5 grass_block6 grass_block7 grass_block8 grass_block9 grass_block10 grass_block11 grass_block12 grass_block13 grass_block14 grass_block15 grass_block16 grass_block17 grass_block18 grass_block19 grass_block20 grass_block21 grass_block22 grass_block23 grass_block24 grass_block25 grass_block26 grass_block27 grass_block28 grass_block29 grass_block30 grass_block31 grass_block32 grass_block33 grass_block34 grass_block35 grass_block36 grass_block37 grass_block38 grass_block39 grass_block40 grass_block41 grass_block42 grass_block43 grass_block44 grass_block45 grass_block46 grass_block47 grass_block48 grass_block49 grass_block50 grass_block51 grass_block52 grass_block53 grass_block54 grass_block55 grass_block56 grass_block57 grass_block58 grass_block59 grass_block60 grass_block61 grass_block62 grass_block63 grass_block64 grass_block65 grass_block66 grass_block67 grass_block68 grass_block69 grass_block70 grass_block71 grass_block72 grass_block73 grass_block74 grass_block75 grass_block76 grass_block77 grass_block78 grass_block79 grass_block80 grass_block81 grass_block82 grass_block83 grass_block84 grass_block85 grass_block86 grass_block87 grass_block88 grass_block89 grass_block90 grass_block91 grass_block92 grass_block93 grass_block94 grass_block95 grass_block96 grass_block97 grass_block98 grass_block99 grass_block100 grass_block101 grass_block102 grass_block103 grass_block104 grass_block105 grass_block106 grass_block107 grass_block108 grass_block109 grass_block110 grass_block111 grass_block112 grass_block113 grass_block114 grass_block115 grass_block116 grass_block117 grass_block118 grass_block119 grass_block120 grass_block121 grass_block122 grass_block123 grass_block124 grass_block125 grass_block126 grass_block127 grass_block128 grass_block129 grass_block130 grass_block131 grass_block132 grass_block133 grass_block134 grass_block135 grass_block136 grass_block137 grass_block138 grass_block139 grass_block140 grass_block141 grass_block142 grass_block143 grass_block144 grass_block145 grass_block146 grass_block147 grass_block148 grass_block149 grass_block150 grass_block151 grass_block152 grass_block153 grass_block154 grass_block155 grass_block156 grass_block157 grass_block158 grass_block159 grass_block160 grass_block161 grass_block162 grass_block163 grass_block164 grass_block165 grass_block166 grass_block167 grass_block168 grass_block169 grass_block170 grass_block171 grass_block172 grass_block173 grass_block174 grass_block175 grass_block176 grass_block177 grass_block178 grass_block179 grass_block180 grass_block181 grass_block182 grass_block183 grass_block184 grass_block185 grass_block186 grass_block187 grass_block188 grass_block189 grass_block190 grass_block191 grass_block192 grass_block193 grass_block194 grass_block195 grass_block196 grass_block197 grass_block198 grass_block199 grass_block200 grass_block201 grass_block202 grass_block203 grass_block204 grass_block205 grass_block206 grass_block207 grass_block208 grass_block209 grass_block210 grass_block211 grass_block212 grass_block213 grass_block214 grass_block215 grass_block216 grass_block217 grass_block218 grass_block219 grass_block220 grass_block221 grass_block222 grass_block223 grass_block224 grass_block225 grass_block226 grass_block227 grass_block228 grass_block229 grass_block230 grass_block231 grass_block232 grass_block233 grass_block234 grass_block235 grass_block236 grass_block237 grass_block238 grass_block239 grass_block240 grass_block241 grass_block242 grass_block243 grass_block244 grass_block245 grass_block246 grass_block247 grass_block248 grass_block249 grass_block250 grass_block251 grass_block252 grass_block253 grass_block254 grass_block255 grass_block256 grass_block257 grass_block258 grass_block259 grass_block260 grass_block261 grass_block262 grass_block263 grass_block264 grass_block265 grass_block266 grass_block267 grass_block268 grass_block269 grass_block270 grass_block271 grass_block272 grass_block273 grass_block274 grass_block275 grass_block276 grass_block277 grass_block278 grass_block279 grass_block280 grass_block281 grass_block282 grass_block283 grass_block284 grass_block285 grass_block286 grass_block287 grass_block288 grass_block289 grass_block290 grass_block291 grass_block292 grass_block293 grass_block294 grass_block295 grass_block296 grass_block297 grass_block298 grass_block299 grass_block300 grass_block301 grass_block302 grass_block303 grass_block304 grass_block305 grass_block306 grass_block307 grass_block308 grass_block309 grass_block310 grass_block311 grass_block312 grass_block313 grass_block314 grass_block315 grass_block316 grass_block317 grass_block318 grass_block319 grass_block320 grass_block321 grass_block322 grass_block323 grass_block324 grass_block325 grass_block326 grass_block327 grass_block328 grass_block329 grass_block330 grass_block331 grass_block332 grass_block333 grass_block334 grass_block335 grass_block336 grass_block337 grass_block338 grass_block339 grass_block340 grass_block341 grass_block342 grass_block343 grass_block344 grass_block345 grass_block346 grass_block347 grass_block348 grass_block349 grass_block350 grass_block351 grass_block352 grass_block353 grass_block354 grass_block355 grass_block356 grass_block357 grass_block358 grass_block359 grass_block360 grass_block361 grass_block362 grass_block363 grass_block364 grass_block365 grass_block366 grass_block367 grass_block368 grass_block369 grass_block370 grass_block371 grass_block372 grass_block373 grass_block374 grass_block375 grass_block376 grass_block377 grass_block378 grass_block379 grass_block380 grass_block381 grass_block382 grass_block383 grass_block384 grass_block385 grass_block386 grass_block387 grass_block388 grass_block389 grass_block390 grass_block391 grass_block392 grass_block393 grass_block394 grass_block395 grass_block396 grass_block397 grass_block398 grass_block399 grass_block400 grass_block401 grass_block402 grass_block403 grass_block404 grass_block405 grass_block406 grass_block407 grass_block408 grass_block409 - grass_block
	grass_block-block0 grass_block-block1 grass_block-block2 grass_block-block3 grass_block-block4 grass_block-block5 grass_block-block6 grass_block-block7 grass_block-block8 grass_block-block9 grass_block-block10 grass_block-block11 grass_block-block12 grass_block-block13 grass_block-block14 grass_block-block15 grass_block-block16 grass_block-block17 grass_block-block18 grass_block-block19 grass_block-block20 grass_block-block21 grass_block-block22 grass_block-block23 grass_block-block24 grass_block-block25 grass_block-block26 grass_block-block27 grass_block-block28 grass_block-block29 grass_block-block30 grass_block-block31 grass_block-block32 grass_block-block33 grass_block-block34 grass_block-block35 grass_block-block36 grass_block-block37 grass_block-block38 grass_block-block39 grass_block-block40 grass_block-block41 grass_block-block42 grass_block-block43 grass_block-block44 grass_block-block45 grass_block-block46 grass_block-block47 grass_block-block48 grass_block-block49 grass_block-block50 grass_block-block51 grass_block-block52 grass_block-block53 grass_block-block54 grass_block-block55 grass_block-block56 grass_block-block57 grass_block-block58 grass_block-block59 grass_block-block60 grass_block-block61 grass_block-block62 grass_block-block63 grass_block-block64 grass_block-block65 grass_block-block66 grass_block-block67 grass_block-block68 grass_block-block69 grass_block-block70 grass_block-block71 grass_block-block72 grass_block-block73 grass_block-block74 grass_block-block75 grass_block-block76 grass_block-block77 grass_block-block78 grass_block-block79 grass_block-block80 grass_block-block81 grass_block-block82 grass_block-block83 grass_block-block84 grass_block-block85 grass_block-block86 grass_block-block87 grass_block-block88 grass_block-block89 grass_block-block90 grass_block-block91 grass_block-block92 grass_block-block93 grass_block-block94 grass_block-block95 grass_block-block96 grass_block-block97 grass_block-block98 grass_block-block99 grass_block-block100 grass_block-block101 grass_block-block102 grass_block-block103 grass_block-block104 grass_block-block105 grass_block-block106 grass_block-block107 grass_block-block108 grass_block-block109 grass_block-block110 grass_block-block111 grass_block-block112 grass_block-block113 grass_block-block114 grass_block-block115 grass_block-block116 grass_block-block117 grass_block-block118 grass_block-block119 grass_block-block120 grass_block-block121 grass_block-block122 grass_block-block123 grass_block-block124 grass_block-block125 grass_block-block126 grass_block-block127 grass_block-block128 grass_block-block129 grass_block-block130 grass_block-block131 grass_block-block132 grass_block-block133 grass_block-block134 grass_block-block135 grass_block-block136 grass_block-block137 grass_block-block138 grass_block-block139 grass_block-block140 grass_block-block141 grass_block-block142 grass_block-block143 grass_block-block144 grass_block-block145 grass_block-block146 grass_block-block147 grass_block-block148 grass_block-block149 grass_block-block150 grass_block-block151 grass_block-block152 grass_block-block153 grass_block-block154 grass_block-block155 grass_block-block156 grass_block-block157 grass_block-block158 grass_block-block159 grass_block-block160 grass_block-block161 grass_block-block162 grass_block-block163 grass_block-block164 grass_block-block165 grass_block-block166 grass_block-block167 grass_block-block168 grass_block-block169 grass_block-block170 grass_block-block171 grass_block-block172 grass_block-block173 grass_block-block174 grass_block-block175 grass_block-block176 grass_block-block177 grass_block-block178 grass_block-block179 grass_block-block180 grass_block-block181 grass_block-block182 grass_block-block183 grass_block-block184 grass_block-block185 grass_block-block186 grass_block-block187 grass_block-block188 grass_block-block189 grass_block-block190 grass_block-block191 grass_block-block192 grass_block-block193 grass_block-block194 grass_block-block195 grass_block-block196 grass_block-block197 grass_block-block198 grass_block-block199 grass_block-block200 grass_block-block201 grass_block-block202 grass_block-block203 grass_block-block204 grass_block-block205 grass_block-block206 grass_block-block207 grass_block-block208 grass_block-block209 grass_block-block210 grass_block-block211 grass_block-block212 grass_block-block213 grass_block-block214 grass_block-block215 grass_block-block216 grass_block-block217 grass_block-block218 grass_block-block219 grass_block-block220 grass_block-block221 grass_block-block222 grass_block-block223 grass_block-block224 grass_block-block225 grass_block-block226 grass_block-block227 grass_block-block228 grass_block-block229 grass_block-block230 grass_block-block231 grass_block-block232 grass_block-block233 grass_block-block234 grass_block-block235 grass_block-block236 grass_block-block237 grass_block-block238 grass_block-block239 grass_block-block240 grass_block-block241 grass_block-block242 grass_block-block243 grass_block-block244 grass_block-block245 grass_block-block246 grass_block-block247 grass_block-block248 grass_block-block249 grass_block-block250 grass_block-block251 grass_block-block252 grass_block-block253 grass_block-block254 grass_block-block255 grass_block-block256 grass_block-block257 grass_block-block258 grass_block-block259 grass_block-block260 grass_block-block261 grass_block-block262 grass_block-block263 grass_block-block264 grass_block-block265 grass_block-block266 grass_block-block267 grass_block-block268 grass_block-block269 grass_block-block270 grass_block-block271 grass_block-block272 grass_block-block273 grass_block-block274 grass_block-block275 grass_block-block276 grass_block-block277 grass_block-block278 grass_block-block279 grass_block-block280 grass_block-block281 grass_block-block282 grass_block-block283 grass_block-block284 grass_block-block285 grass_block-block286 grass_block-block287 grass_block-block288 grass_block-block289 grass_block-block290 grass_block-block291 grass_block-block292 grass_block-block293 grass_block-block294 grass_block-block295 grass_block-block296 grass_block-block297 grass_block-block298 grass_block-block299 grass_block-block300 grass_block-block301 grass_block-block302 grass_block-block303 grass_block-block304 grass_block-block305 grass_block-block306 grass_block-block307 grass_block-block308 grass_block-block309 grass_block-block310 grass_block-block311 grass_block-block312 grass_block-block313 grass_block-block314 grass_block-block315 grass_block-block316 grass_block-block317 grass_block-block318 grass_block-block319 grass_block-block320 grass_block-block321 grass_block-block322 grass_block-block323 grass_block-block324 grass_block-block325 grass_block-block326 grass_block-block327 grass_block-block328 grass_block-block329 grass_block-block330 grass_block-block331 grass_block-block332 grass_block-block333 grass_block-block334 grass_block-block335 grass_block-block336 grass_block-block337 grass_block-block338 grass_block-block339 grass_block-block340 grass_block-block341 grass_block-block342 grass_block-block343 grass_block-block344 grass_block-block345 grass_block-block346 grass_block-block347 grass_block-block348 grass_block-block349 grass_block-block350 grass_block-block351 grass_block-block352 grass_block-block353 grass_block-block354 grass_block-block355 grass_block-block356 grass_block-block357 grass_block-block358 grass_block-block359 grass_block-block360 grass_block-block361 grass_block-block362 grass_block-block363 grass_block-block364 grass_block-block365 grass_block-block366 grass_block-block367 grass_block-block368 grass_block-block369 grass_block-block370 grass_block-block371 grass_block-block372 grass_block-block373 grass_block-block374 grass_block-block375 grass_block-block376 grass_block-block377 grass_block-block378 grass_block-block379 grass_block-block380 grass_block-block381 grass_block-block382 grass_block-block383 grass_block-block384 grass_block-block385 grass_block-block386 grass_block-block387 grass_block-block388 grass_block-block389 grass_block-block390 grass_block-block391 grass_block-block392 grass_block-block393 grass_block-block394 grass_block-block395 grass_block-block396 grass_block-block397 grass_block-block398 grass_block-block399 grass_block-block400 grass_block-block401 grass_block-block402 grass_block-block403 grass_block-block404 grass_block-block405 grass_block-block406 grass_block-block407 grass_block-block408 grass_block-block409 - grass_block-block
	position-206 position-205 position-204 position-203 position-202 position-201 position-200 position-199 position-198 position-197 position-196 position-195 position-194 position-193 position-192 position-191 position-190 position-189 position-188 position-187 position-186 position-185 position-184 position-183 position-182 position-181 position-180 position-179 position-178 position-177 position-176 position-175 position-174 position-173 position-172 position-171 position-170 position-169 position-168 position-167 position-166 position-165 position-164 position-163 position-162 position-161 position-160 position-159 position-158 position-157 position-156 position-155 position-154 position-153 position-152 position-151 position-150 position-149 position-148 position-147 position-146 position-145 position-144 position-143 position-142 position-141 position-140 position-139 position-138 position-137 position-136 position-135 position-134 position-133 position-132 position-131 position-130 position-129 position-128 position-127 position-126 position-125 position-124 position-123 position-122 position-121 position-120 position-119 position-118 position-117 position-116 position-115 position-114 position-113 position-112 position-111 position-110 position-109 position-108 position-107 position-106 position-105 position-104 position-103 position-102 position-101 position-100 position-99 position-98 position-97 position-96 position-95 position-94 position-93 position-92 position-91 position-90 position-89 position-88 position-87 position-86 position-85 position-84 position-83 position-82 position-81 position-80 position-79 position-78 position-77 position-76 position-75 position-74 position-73 position-72 position-71 position-70 position-69 position-68 position-67 position-66 position-65 position-64 position-63 position-62 position-61 position-60 position-59 position-58 position-57 position-56 position-55 position-54 position-53 position-52 position-51 position-50 position-49 position-48 position-47 position-46 position-45 position-44 position-43 position-42 position-41 position-40 position-39 position-38 position-37 position-36 position-35 position-34 position-33 position-32 position-31 position-30 position-29 position-28 position-27 position-26 position-25 position-24 position-23 position-22 position-21 position-20 position-19 position-18 position-17 position-16 position-15 position-14 position-13 position-12 position-11 position-10 position-9 position-8 position-7 position-6 position-5 position-4 position-3 position-2 position-1 position0 position1 position2 position3 position4 position5 position6 position7 position8 position9 position10 position11 position12 position13 position14 position15 position16 position17 position18 position19 position20 position21 position22 position23 position24 position25 position26 position27 position28 position29 position30 position31 position32 position33 position34 position35 position36 position37 position38 position39 position40 position41 position42 position43 position44 position45 position46 position47 position48 position49 position50 position51 position52 position53 position54 position55 position56 position57 position58 position59 position60 position61 position62 position63 position64 position65 position66 position67 position68 position69 position70 position71 position72 position73 position74 position75 position76 position77 position78 position79 position80 position81 position82 position83 position84 position85 position86 position87 position88 position89 position90 position91 position92 position93 position94 position95 position96 position97 position98 position99 position100 position101 position102 position103 position104 position105 position106 position107 position108 position109 position110 position111 position112 position113 position114 position115 position116 position117 position118 position119 position120 position121 position122 position123 position124 position125 position126 position127 position128 position129 position130 position131 position132 position133 position134 position135 position136 position137 position138 position139 position140 position141 position142 position143 position144 position145 position146 position147 position148 position149 position150 position151 position152 position153 position154 position155 position156 position157 position158 position159 position160 position161 position162 position163 position164 position165 position166 position167 position168 position169 position170 position171 position172 position173 position174 position175 position176 position177 position178 position179 position180 position181 position182 position183 position184 position185 position186 position187 position188 position189 position190 position191 position192 position193 position194 position195 position196 position197 position198 position199 position200 position201 position202 position203 position204 position205 position206 position207 - position
	count0 count1 count2 count3 count4 count5 count6 count7 count8 count9 count10 count11 count12 count13 count14 count15 count16 count17 count18 count19 count20 count21 count22 count23 count24 count25 count26 count27 count28 count29 count30 count31 count32 count33 count34 count35 count36 count37 count38 count39 count40 count41 count42 count43 count44 count45 count46 count47 count48 count49 count50 count51 count52 count53 count54 count55 count56 count57 count58 count59 count60 count61 count62 count63 count64 - count
)
(:predicates
	(not-equal ?x1 - int ?x2 - int)
	(agent-has-n-grass_block ?ag - agent ?n - count)
	(goal-achieved ?ag - agent)
	(block-present ?b - block)
	(are-seq ?x1 - int ?x2 - int)
	(item-present ?i - item)
	(at-z ?l - locatable ?z - position)
	(agent-alive ?ag - agent)
	(at-y ?l - locatable ?y - position)
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
(at-x ?ag position204)
 (at-y ?ag position4)
 (at-z ?ag position0)
)  )
	:effect (and 
(goal-achieved ?ag))
)


)