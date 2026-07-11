(define (problem Cut_Tree_Medium_problem)
	(:domain Cut_Tree_Medium)

(:init
	(are-seq position-21 position-20)

	(are-seq position-20 position-19)

	(are-seq position-19 position-18)

	(are-seq position-18 position-17)

	(are-seq position-17 position-16)

	(are-seq position-16 position-15)

	(are-seq position-15 position-14)

	(are-seq position-14 position-13)

	(are-seq position-13 position-12)

	(are-seq position-12 position-11)

	(are-seq position-11 position-10)

	(are-seq position-10 position-9)

	(are-seq position-9 position-8)

	(are-seq position-8 position-7)

	(are-seq position-7 position-6)

	(are-seq position-6 position-5)

	(are-seq position-5 position-4)

	(are-seq position-4 position-3)

	(are-seq position-3 position-2)

	(are-seq position-2 position-1)

	(are-seq position-1 position0)

	(are-seq position0 position1)

	(are-seq position1 position2)

	(are-seq position2 position3)

	(are-seq position3 position4)

	(are-seq position4 position5)

	(are-seq position5 position6)

	(are-seq position6 position7)

	(are-seq position7 position8)

	(are-seq position8 position9)

	(are-seq position9 position10)

	(are-seq position10 position11)

	(are-seq position11 position12)

	(are-seq position12 position13)

	(are-seq position13 position14)

	(are-seq position14 position15)

	(are-seq position15 position16)

	(are-seq position16 position17)

	(are-seq position17 position18)

	(are-seq position18 position19)

	(are-seq position19 position20)

	(are-seq position20 position21)

	(are-seq position21 position22)

	(are-seq count0 count1)

	(are-seq count1 count2)

	(are-seq count2 count3)

	(are-seq count3 count4)

	(are-seq count4 count5)

	(are-seq count5 count6)

	(are-seq count6 count7)

	(are-seq count7 count8)

	(are-seq count8 count9)

	(are-seq count9 count10)

	(are-seq count10 count11)

	(are-seq count11 count12)

	(are-seq count12 count13)

	(are-seq count13 count14)

	(are-seq count14 count15)

	(are-seq count15 count16)

	(are-seq count16 count17)

	(are-seq count17 count18)

	(are-seq count18 count19)

	(are-seq count19 count20)

	(are-seq count20 count21)

	(are-seq count21 count22)

	(are-seq count22 count23)

	(are-seq count23 count24)

	(are-seq count24 count25)

	(are-seq count25 count26)

	(are-seq count26 count27)

	(are-seq count27 count28)

	(are-seq count28 count29)

	(are-seq count29 count30)

	(are-seq count30 count31)

	(are-seq count31 count32)

	(are-seq count32 count33)

	(are-seq count33 count34)

	(are-seq count34 count35)

	(are-seq count35 count36)

	(are-seq count36 count37)

	(are-seq count37 count38)

	(are-seq count38 count39)

	(are-seq count39 count40)

	(are-seq count40 count41)

	(are-seq count41 count42)

	(are-seq count42 count43)

	(are-seq count43 count44)

	(are-seq count44 count45)

	(are-seq count45 count46)

	(are-seq count46 count47)

	(are-seq count47 count48)

	(are-seq count48 count49)

	(are-seq count49 count50)

	(are-seq count50 count51)

	(are-seq count51 count52)

	(are-seq count52 count53)

	(are-seq count53 count54)

	(are-seq count54 count55)

	(are-seq count55 count56)

	(are-seq count56 count57)

	(are-seq count57 count58)

	(are-seq count58 count59)

	(are-seq count59 count60)

	(are-seq count60 count61)

	(are-seq count61 count62)

	(are-seq count62 count63)

	(are-seq count63 count64)

	(at-x steve position0)

	(at-y steve position4)

	(at-z steve position0)

	(agent-alive steve)
	(agent-has-n-cobblestone steve count64)

	(agent-has-n-grass_block steve count0)

	(agent-has-n-leaves steve count0)

	(agent-has-n-log steve count0)

	(at-x grass_block-block0 position-20)

	(at-y grass_block-block0 position3)

	(at-z grass_block-block0 position-20)

	(block-present grass_block-block0)
	(at-x grass_block-block1 position-20)

	(at-y grass_block-block1 position3)

	(at-z grass_block-block1 position-19)

	(block-present grass_block-block1)
	(at-x grass_block-block2 position-20)

	(at-y grass_block-block2 position3)

	(at-z grass_block-block2 position-18)

	(block-present grass_block-block2)
	(at-x grass_block-block3 position-20)

	(at-y grass_block-block3 position3)

	(at-z grass_block-block3 position-17)

	(block-present grass_block-block3)
	(at-x grass_block-block4 position-20)

	(at-y grass_block-block4 position3)

	(at-z grass_block-block4 position-16)

	(block-present grass_block-block4)
	(at-x grass_block-block5 position-20)

	(at-y grass_block-block5 position3)

	(at-z grass_block-block5 position-15)

	(block-present grass_block-block5)
	(at-x grass_block-block6 position-20)

	(at-y grass_block-block6 position3)

	(at-z grass_block-block6 position-14)

	(block-present grass_block-block6)
	(at-x grass_block-block7 position-20)

	(at-y grass_block-block7 position3)

	(at-z grass_block-block7 position-13)

	(block-present grass_block-block7)
	(at-x grass_block-block8 position-20)

	(at-y grass_block-block8 position3)

	(at-z grass_block-block8 position-12)

	(block-present grass_block-block8)
	(at-x grass_block-block9 position-20)

	(at-y grass_block-block9 position3)

	(at-z grass_block-block9 position-11)

	(block-present grass_block-block9)
	(at-x grass_block-block10 position-20)

	(at-y grass_block-block10 position3)

	(at-z grass_block-block10 position-10)

	(block-present grass_block-block10)
	(at-x grass_block-block11 position-20)

	(at-y grass_block-block11 position3)

	(at-z grass_block-block11 position-9)

	(block-present grass_block-block11)
	(at-x grass_block-block12 position-20)

	(at-y grass_block-block12 position3)

	(at-z grass_block-block12 position-8)

	(block-present grass_block-block12)
	(at-x grass_block-block13 position-20)

	(at-y grass_block-block13 position3)

	(at-z grass_block-block13 position-7)

	(block-present grass_block-block13)
	(at-x grass_block-block14 position-20)

	(at-y grass_block-block14 position3)

	(at-z grass_block-block14 position-6)

	(block-present grass_block-block14)
	(at-x grass_block-block15 position-20)

	(at-y grass_block-block15 position3)

	(at-z grass_block-block15 position-5)

	(block-present grass_block-block15)
	(at-x grass_block-block16 position-20)

	(at-y grass_block-block16 position3)

	(at-z grass_block-block16 position-4)

	(block-present grass_block-block16)
	(at-x grass_block-block17 position-20)

	(at-y grass_block-block17 position3)

	(at-z grass_block-block17 position-3)

	(block-present grass_block-block17)
	(at-x grass_block-block18 position-20)

	(at-y grass_block-block18 position3)

	(at-z grass_block-block18 position-2)

	(block-present grass_block-block18)
	(at-x grass_block-block19 position-20)

	(at-y grass_block-block19 position3)

	(at-z grass_block-block19 position-1)

	(block-present grass_block-block19)
	(at-x grass_block-block20 position-20)

	(at-y grass_block-block20 position3)

	(at-z grass_block-block20 position0)

	(block-present grass_block-block20)
	(at-x grass_block-block21 position-20)

	(at-y grass_block-block21 position3)

	(at-z grass_block-block21 position1)

	(block-present grass_block-block21)
	(at-x grass_block-block22 position-20)

	(at-y grass_block-block22 position3)

	(at-z grass_block-block22 position2)

	(block-present grass_block-block22)
	(at-x grass_block-block23 position-20)

	(at-y grass_block-block23 position3)

	(at-z grass_block-block23 position3)

	(block-present grass_block-block23)
	(at-x grass_block-block24 position-20)

	(at-y grass_block-block24 position3)

	(at-z grass_block-block24 position4)

	(block-present grass_block-block24)
	(at-x grass_block-block25 position-20)

	(at-y grass_block-block25 position3)

	(at-z grass_block-block25 position5)

	(block-present grass_block-block25)
	(at-x grass_block-block26 position-20)

	(at-y grass_block-block26 position3)

	(at-z grass_block-block26 position6)

	(block-present grass_block-block26)
	(at-x grass_block-block27 position-20)

	(at-y grass_block-block27 position3)

	(at-z grass_block-block27 position7)

	(block-present grass_block-block27)
	(at-x grass_block-block28 position-20)

	(at-y grass_block-block28 position3)

	(at-z grass_block-block28 position8)

	(block-present grass_block-block28)
	(at-x grass_block-block29 position-20)

	(at-y grass_block-block29 position3)

	(at-z grass_block-block29 position9)

	(block-present grass_block-block29)
	(at-x grass_block-block30 position-20)

	(at-y grass_block-block30 position3)

	(at-z grass_block-block30 position10)

	(block-present grass_block-block30)
	(at-x grass_block-block31 position-20)

	(at-y grass_block-block31 position3)

	(at-z grass_block-block31 position11)

	(block-present grass_block-block31)
	(at-x grass_block-block32 position-20)

	(at-y grass_block-block32 position3)

	(at-z grass_block-block32 position12)

	(block-present grass_block-block32)
	(at-x grass_block-block33 position-20)

	(at-y grass_block-block33 position3)

	(at-z grass_block-block33 position13)

	(block-present grass_block-block33)
	(at-x grass_block-block34 position-20)

	(at-y grass_block-block34 position3)

	(at-z grass_block-block34 position14)

	(block-present grass_block-block34)
	(at-x grass_block-block35 position-20)

	(at-y grass_block-block35 position3)

	(at-z grass_block-block35 position15)

	(block-present grass_block-block35)
	(at-x grass_block-block36 position-20)

	(at-y grass_block-block36 position3)

	(at-z grass_block-block36 position16)

	(block-present grass_block-block36)
	(at-x grass_block-block37 position-20)

	(at-y grass_block-block37 position3)

	(at-z grass_block-block37 position17)

	(block-present grass_block-block37)
	(at-x grass_block-block38 position-20)

	(at-y grass_block-block38 position3)

	(at-z grass_block-block38 position18)

	(block-present grass_block-block38)
	(at-x grass_block-block39 position-20)

	(at-y grass_block-block39 position3)

	(at-z grass_block-block39 position19)

	(block-present grass_block-block39)
	(at-x grass_block-block40 position-20)

	(at-y grass_block-block40 position3)

	(at-z grass_block-block40 position20)

	(block-present grass_block-block40)
	(at-x grass_block-block41 position-19)

	(at-y grass_block-block41 position3)

	(at-z grass_block-block41 position-20)

	(block-present grass_block-block41)
	(at-x grass_block-block42 position-19)

	(at-y grass_block-block42 position3)

	(at-z grass_block-block42 position-19)

	(block-present grass_block-block42)
	(at-x grass_block-block43 position-19)

	(at-y grass_block-block43 position3)

	(at-z grass_block-block43 position-18)

	(block-present grass_block-block43)
	(at-x grass_block-block44 position-19)

	(at-y grass_block-block44 position3)

	(at-z grass_block-block44 position-17)

	(block-present grass_block-block44)
	(at-x grass_block-block45 position-19)

	(at-y grass_block-block45 position3)

	(at-z grass_block-block45 position-16)

	(block-present grass_block-block45)
	(at-x grass_block-block46 position-19)

	(at-y grass_block-block46 position3)

	(at-z grass_block-block46 position-15)

	(block-present grass_block-block46)
	(at-x grass_block-block47 position-19)

	(at-y grass_block-block47 position3)

	(at-z grass_block-block47 position-14)

	(block-present grass_block-block47)
	(at-x grass_block-block48 position-19)

	(at-y grass_block-block48 position3)

	(at-z grass_block-block48 position-13)

	(block-present grass_block-block48)
	(at-x grass_block-block49 position-19)

	(at-y grass_block-block49 position3)

	(at-z grass_block-block49 position-12)

	(block-present grass_block-block49)
	(at-x grass_block-block50 position-19)

	(at-y grass_block-block50 position3)

	(at-z grass_block-block50 position-11)

	(block-present grass_block-block50)
	(at-x grass_block-block51 position-19)

	(at-y grass_block-block51 position3)

	(at-z grass_block-block51 position-10)

	(block-present grass_block-block51)
	(at-x grass_block-block52 position-19)

	(at-y grass_block-block52 position3)

	(at-z grass_block-block52 position-9)

	(block-present grass_block-block52)
	(at-x grass_block-block53 position-19)

	(at-y grass_block-block53 position3)

	(at-z grass_block-block53 position-8)

	(block-present grass_block-block53)
	(at-x grass_block-block54 position-19)

	(at-y grass_block-block54 position3)

	(at-z grass_block-block54 position-7)

	(block-present grass_block-block54)
	(at-x grass_block-block55 position-19)

	(at-y grass_block-block55 position3)

	(at-z grass_block-block55 position-6)

	(block-present grass_block-block55)
	(at-x grass_block-block56 position-19)

	(at-y grass_block-block56 position3)

	(at-z grass_block-block56 position-5)

	(block-present grass_block-block56)
	(at-x grass_block-block57 position-19)

	(at-y grass_block-block57 position3)

	(at-z grass_block-block57 position-4)

	(block-present grass_block-block57)
	(at-x grass_block-block58 position-19)

	(at-y grass_block-block58 position3)

	(at-z grass_block-block58 position-3)

	(block-present grass_block-block58)
	(at-x grass_block-block59 position-19)

	(at-y grass_block-block59 position3)

	(at-z grass_block-block59 position-2)

	(block-present grass_block-block59)
	(at-x grass_block-block60 position-19)

	(at-y grass_block-block60 position3)

	(at-z grass_block-block60 position-1)

	(block-present grass_block-block60)
	(at-x grass_block-block61 position-19)

	(at-y grass_block-block61 position3)

	(at-z grass_block-block61 position0)

	(block-present grass_block-block61)
	(at-x grass_block-block62 position-19)

	(at-y grass_block-block62 position3)

	(at-z grass_block-block62 position1)

	(block-present grass_block-block62)
	(at-x grass_block-block63 position-19)

	(at-y grass_block-block63 position3)

	(at-z grass_block-block63 position2)

	(block-present grass_block-block63)
	(at-x grass_block-block64 position-19)

	(at-y grass_block-block64 position3)

	(at-z grass_block-block64 position3)

	(block-present grass_block-block64)
	(at-x grass_block-block65 position-19)

	(at-y grass_block-block65 position3)

	(at-z grass_block-block65 position4)

	(block-present grass_block-block65)
	(at-x grass_block-block66 position-19)

	(at-y grass_block-block66 position3)

	(at-z grass_block-block66 position5)

	(block-present grass_block-block66)
	(at-x grass_block-block67 position-19)

	(at-y grass_block-block67 position3)

	(at-z grass_block-block67 position6)

	(block-present grass_block-block67)
	(at-x grass_block-block68 position-19)

	(at-y grass_block-block68 position3)

	(at-z grass_block-block68 position7)

	(block-present grass_block-block68)
	(at-x grass_block-block69 position-19)

	(at-y grass_block-block69 position3)

	(at-z grass_block-block69 position8)

	(block-present grass_block-block69)
	(at-x grass_block-block70 position-19)

	(at-y grass_block-block70 position3)

	(at-z grass_block-block70 position9)

	(block-present grass_block-block70)
	(at-x grass_block-block71 position-19)

	(at-y grass_block-block71 position3)

	(at-z grass_block-block71 position10)

	(block-present grass_block-block71)
	(at-x grass_block-block72 position-19)

	(at-y grass_block-block72 position3)

	(at-z grass_block-block72 position11)

	(block-present grass_block-block72)
	(at-x grass_block-block73 position-19)

	(at-y grass_block-block73 position3)

	(at-z grass_block-block73 position12)

	(block-present grass_block-block73)
	(at-x grass_block-block74 position-19)

	(at-y grass_block-block74 position3)

	(at-z grass_block-block74 position13)

	(block-present grass_block-block74)
	(at-x grass_block-block75 position-19)

	(at-y grass_block-block75 position3)

	(at-z grass_block-block75 position14)

	(block-present grass_block-block75)
	(at-x grass_block-block76 position-19)

	(at-y grass_block-block76 position3)

	(at-z grass_block-block76 position15)

	(block-present grass_block-block76)
	(at-x grass_block-block77 position-19)

	(at-y grass_block-block77 position3)

	(at-z grass_block-block77 position16)

	(block-present grass_block-block77)
	(at-x grass_block-block78 position-19)

	(at-y grass_block-block78 position3)

	(at-z grass_block-block78 position17)

	(block-present grass_block-block78)
	(at-x grass_block-block79 position-19)

	(at-y grass_block-block79 position3)

	(at-z grass_block-block79 position18)

	(block-present grass_block-block79)
	(at-x grass_block-block80 position-19)

	(at-y grass_block-block80 position3)

	(at-z grass_block-block80 position19)

	(block-present grass_block-block80)
	(at-x grass_block-block81 position-19)

	(at-y grass_block-block81 position3)

	(at-z grass_block-block81 position20)

	(block-present grass_block-block81)
	(at-x grass_block-block82 position-18)

	(at-y grass_block-block82 position3)

	(at-z grass_block-block82 position-20)

	(block-present grass_block-block82)
	(at-x grass_block-block83 position-18)

	(at-y grass_block-block83 position3)

	(at-z grass_block-block83 position-19)

	(block-present grass_block-block83)
	(at-x grass_block-block84 position-18)

	(at-y grass_block-block84 position3)

	(at-z grass_block-block84 position-18)

	(block-present grass_block-block84)
	(at-x grass_block-block85 position-18)

	(at-y grass_block-block85 position3)

	(at-z grass_block-block85 position-17)

	(block-present grass_block-block85)
	(at-x grass_block-block86 position-18)

	(at-y grass_block-block86 position3)

	(at-z grass_block-block86 position-16)

	(block-present grass_block-block86)
	(at-x grass_block-block87 position-18)

	(at-y grass_block-block87 position3)

	(at-z grass_block-block87 position-15)

	(block-present grass_block-block87)
	(at-x grass_block-block88 position-18)

	(at-y grass_block-block88 position3)

	(at-z grass_block-block88 position-14)

	(block-present grass_block-block88)
	(at-x grass_block-block89 position-18)

	(at-y grass_block-block89 position3)

	(at-z grass_block-block89 position-13)

	(block-present grass_block-block89)
	(at-x grass_block-block90 position-18)

	(at-y grass_block-block90 position3)

	(at-z grass_block-block90 position-12)

	(block-present grass_block-block90)
	(at-x grass_block-block91 position-18)

	(at-y grass_block-block91 position3)

	(at-z grass_block-block91 position-11)

	(block-present grass_block-block91)
	(at-x grass_block-block92 position-18)

	(at-y grass_block-block92 position3)

	(at-z grass_block-block92 position-10)

	(block-present grass_block-block92)
	(at-x grass_block-block93 position-18)

	(at-y grass_block-block93 position3)

	(at-z grass_block-block93 position-9)

	(block-present grass_block-block93)
	(at-x grass_block-block94 position-18)

	(at-y grass_block-block94 position3)

	(at-z grass_block-block94 position-8)

	(block-present grass_block-block94)
	(at-x grass_block-block95 position-18)

	(at-y grass_block-block95 position3)

	(at-z grass_block-block95 position-7)

	(block-present grass_block-block95)
	(at-x grass_block-block96 position-18)

	(at-y grass_block-block96 position3)

	(at-z grass_block-block96 position-6)

	(block-present grass_block-block96)
	(at-x grass_block-block97 position-18)

	(at-y grass_block-block97 position3)

	(at-z grass_block-block97 position-5)

	(block-present grass_block-block97)
	(at-x grass_block-block98 position-18)

	(at-y grass_block-block98 position3)

	(at-z grass_block-block98 position-4)

	(block-present grass_block-block98)
	(at-x grass_block-block99 position-18)

	(at-y grass_block-block99 position3)

	(at-z grass_block-block99 position-3)

	(block-present grass_block-block99)
	(at-x grass_block-block100 position-18)

	(at-y grass_block-block100 position3)

	(at-z grass_block-block100 position-2)

	(block-present grass_block-block100)
	(at-x grass_block-block101 position-18)

	(at-y grass_block-block101 position3)

	(at-z grass_block-block101 position-1)

	(block-present grass_block-block101)
	(at-x grass_block-block102 position-18)

	(at-y grass_block-block102 position3)

	(at-z grass_block-block102 position0)

	(block-present grass_block-block102)
	(at-x grass_block-block103 position-18)

	(at-y grass_block-block103 position3)

	(at-z grass_block-block103 position1)

	(block-present grass_block-block103)
	(at-x grass_block-block104 position-18)

	(at-y grass_block-block104 position3)

	(at-z grass_block-block104 position2)

	(block-present grass_block-block104)
	(at-x grass_block-block105 position-18)

	(at-y grass_block-block105 position3)

	(at-z grass_block-block105 position3)

	(block-present grass_block-block105)
	(at-x grass_block-block106 position-18)

	(at-y grass_block-block106 position3)

	(at-z grass_block-block106 position4)

	(block-present grass_block-block106)
	(at-x grass_block-block107 position-18)

	(at-y grass_block-block107 position3)

	(at-z grass_block-block107 position5)

	(block-present grass_block-block107)
	(at-x grass_block-block108 position-18)

	(at-y grass_block-block108 position3)

	(at-z grass_block-block108 position6)

	(block-present grass_block-block108)
	(at-x grass_block-block109 position-18)

	(at-y grass_block-block109 position3)

	(at-z grass_block-block109 position7)

	(block-present grass_block-block109)
	(at-x grass_block-block110 position-18)

	(at-y grass_block-block110 position3)

	(at-z grass_block-block110 position8)

	(block-present grass_block-block110)
	(at-x grass_block-block111 position-18)

	(at-y grass_block-block111 position3)

	(at-z grass_block-block111 position9)

	(block-present grass_block-block111)
	(at-x grass_block-block112 position-18)

	(at-y grass_block-block112 position3)

	(at-z grass_block-block112 position10)

	(block-present grass_block-block112)
	(at-x grass_block-block113 position-18)

	(at-y grass_block-block113 position3)

	(at-z grass_block-block113 position11)

	(block-present grass_block-block113)
	(at-x grass_block-block114 position-18)

	(at-y grass_block-block114 position3)

	(at-z grass_block-block114 position12)

	(block-present grass_block-block114)
	(at-x grass_block-block115 position-18)

	(at-y grass_block-block115 position3)

	(at-z grass_block-block115 position13)

	(block-present grass_block-block115)
	(at-x grass_block-block116 position-18)

	(at-y grass_block-block116 position3)

	(at-z grass_block-block116 position14)

	(block-present grass_block-block116)
	(at-x grass_block-block117 position-18)

	(at-y grass_block-block117 position3)

	(at-z grass_block-block117 position15)

	(block-present grass_block-block117)
	(at-x grass_block-block118 position-18)

	(at-y grass_block-block118 position3)

	(at-z grass_block-block118 position16)

	(block-present grass_block-block118)
	(at-x grass_block-block119 position-18)

	(at-y grass_block-block119 position3)

	(at-z grass_block-block119 position17)

	(block-present grass_block-block119)
	(at-x grass_block-block120 position-18)

	(at-y grass_block-block120 position3)

	(at-z grass_block-block120 position18)

	(block-present grass_block-block120)
	(at-x grass_block-block121 position-18)

	(at-y grass_block-block121 position3)

	(at-z grass_block-block121 position19)

	(block-present grass_block-block121)
	(at-x grass_block-block122 position-18)

	(at-y grass_block-block122 position3)

	(at-z grass_block-block122 position20)

	(block-present grass_block-block122)
	(at-x grass_block-block123 position-17)

	(at-y grass_block-block123 position3)

	(at-z grass_block-block123 position-20)

	(block-present grass_block-block123)
	(at-x grass_block-block124 position-17)

	(at-y grass_block-block124 position3)

	(at-z grass_block-block124 position-19)

	(block-present grass_block-block124)
	(at-x grass_block-block125 position-17)

	(at-y grass_block-block125 position3)

	(at-z grass_block-block125 position-18)

	(block-present grass_block-block125)
	(at-x grass_block-block126 position-17)

	(at-y grass_block-block126 position3)

	(at-z grass_block-block126 position-17)

	(block-present grass_block-block126)
	(at-x grass_block-block127 position-17)

	(at-y grass_block-block127 position3)

	(at-z grass_block-block127 position-16)

	(block-present grass_block-block127)
	(at-x grass_block-block128 position-17)

	(at-y grass_block-block128 position3)

	(at-z grass_block-block128 position-15)

	(block-present grass_block-block128)
	(at-x grass_block-block129 position-17)

	(at-y grass_block-block129 position3)

	(at-z grass_block-block129 position-14)

	(block-present grass_block-block129)
	(at-x grass_block-block130 position-17)

	(at-y grass_block-block130 position3)

	(at-z grass_block-block130 position-13)

	(block-present grass_block-block130)
	(at-x grass_block-block131 position-17)

	(at-y grass_block-block131 position3)

	(at-z grass_block-block131 position-12)

	(block-present grass_block-block131)
	(at-x grass_block-block132 position-17)

	(at-y grass_block-block132 position3)

	(at-z grass_block-block132 position-11)

	(block-present grass_block-block132)
	(at-x grass_block-block133 position-17)

	(at-y grass_block-block133 position3)

	(at-z grass_block-block133 position-10)

	(block-present grass_block-block133)
	(at-x grass_block-block134 position-17)

	(at-y grass_block-block134 position3)

	(at-z grass_block-block134 position-9)

	(block-present grass_block-block134)
	(at-x grass_block-block135 position-17)

	(at-y grass_block-block135 position3)

	(at-z grass_block-block135 position-8)

	(block-present grass_block-block135)
	(at-x grass_block-block136 position-17)

	(at-y grass_block-block136 position3)

	(at-z grass_block-block136 position-7)

	(block-present grass_block-block136)
	(at-x grass_block-block137 position-17)

	(at-y grass_block-block137 position3)

	(at-z grass_block-block137 position-6)

	(block-present grass_block-block137)
	(at-x grass_block-block138 position-17)

	(at-y grass_block-block138 position3)

	(at-z grass_block-block138 position-5)

	(block-present grass_block-block138)
	(at-x grass_block-block139 position-17)

	(at-y grass_block-block139 position3)

	(at-z grass_block-block139 position-4)

	(block-present grass_block-block139)
	(at-x grass_block-block140 position-17)

	(at-y grass_block-block140 position3)

	(at-z grass_block-block140 position-3)

	(block-present grass_block-block140)
	(at-x grass_block-block141 position-17)

	(at-y grass_block-block141 position3)

	(at-z grass_block-block141 position-2)

	(block-present grass_block-block141)
	(at-x grass_block-block142 position-17)

	(at-y grass_block-block142 position3)

	(at-z grass_block-block142 position-1)

	(block-present grass_block-block142)
	(at-x grass_block-block143 position-17)

	(at-y grass_block-block143 position3)

	(at-z grass_block-block143 position0)

	(block-present grass_block-block143)
	(at-x grass_block-block144 position-17)

	(at-y grass_block-block144 position3)

	(at-z grass_block-block144 position1)

	(block-present grass_block-block144)
	(at-x grass_block-block145 position-17)

	(at-y grass_block-block145 position3)

	(at-z grass_block-block145 position2)

	(block-present grass_block-block145)
	(at-x grass_block-block146 position-17)

	(at-y grass_block-block146 position3)

	(at-z grass_block-block146 position3)

	(block-present grass_block-block146)
	(at-x grass_block-block147 position-17)

	(at-y grass_block-block147 position3)

	(at-z grass_block-block147 position4)

	(block-present grass_block-block147)
	(at-x grass_block-block148 position-17)

	(at-y grass_block-block148 position3)

	(at-z grass_block-block148 position5)

	(block-present grass_block-block148)
	(at-x grass_block-block149 position-17)

	(at-y grass_block-block149 position3)

	(at-z grass_block-block149 position6)

	(block-present grass_block-block149)
	(at-x grass_block-block150 position-17)

	(at-y grass_block-block150 position3)

	(at-z grass_block-block150 position7)

	(block-present grass_block-block150)
	(at-x grass_block-block151 position-17)

	(at-y grass_block-block151 position3)

	(at-z grass_block-block151 position8)

	(block-present grass_block-block151)
	(at-x grass_block-block152 position-17)

	(at-y grass_block-block152 position3)

	(at-z grass_block-block152 position9)

	(block-present grass_block-block152)
	(at-x grass_block-block153 position-17)

	(at-y grass_block-block153 position3)

	(at-z grass_block-block153 position10)

	(block-present grass_block-block153)
	(at-x grass_block-block154 position-17)

	(at-y grass_block-block154 position3)

	(at-z grass_block-block154 position11)

	(block-present grass_block-block154)
	(at-x grass_block-block155 position-17)

	(at-y grass_block-block155 position3)

	(at-z grass_block-block155 position12)

	(block-present grass_block-block155)
	(at-x grass_block-block156 position-17)

	(at-y grass_block-block156 position3)

	(at-z grass_block-block156 position13)

	(block-present grass_block-block156)
	(at-x grass_block-block157 position-17)

	(at-y grass_block-block157 position3)

	(at-z grass_block-block157 position14)

	(block-present grass_block-block157)
	(at-x grass_block-block158 position-17)

	(at-y grass_block-block158 position3)

	(at-z grass_block-block158 position15)

	(block-present grass_block-block158)
	(at-x grass_block-block159 position-17)

	(at-y grass_block-block159 position3)

	(at-z grass_block-block159 position16)

	(block-present grass_block-block159)
	(at-x grass_block-block160 position-17)

	(at-y grass_block-block160 position3)

	(at-z grass_block-block160 position17)

	(block-present grass_block-block160)
	(at-x grass_block-block161 position-17)

	(at-y grass_block-block161 position3)

	(at-z grass_block-block161 position18)

	(block-present grass_block-block161)
	(at-x grass_block-block162 position-17)

	(at-y grass_block-block162 position3)

	(at-z grass_block-block162 position19)

	(block-present grass_block-block162)
	(at-x grass_block-block163 position-17)

	(at-y grass_block-block163 position3)

	(at-z grass_block-block163 position20)

	(block-present grass_block-block163)
	(at-x grass_block-block164 position-16)

	(at-y grass_block-block164 position3)

	(at-z grass_block-block164 position-20)

	(block-present grass_block-block164)
	(at-x grass_block-block165 position-16)

	(at-y grass_block-block165 position3)

	(at-z grass_block-block165 position-19)

	(block-present grass_block-block165)
	(at-x grass_block-block166 position-16)

	(at-y grass_block-block166 position3)

	(at-z grass_block-block166 position-18)

	(block-present grass_block-block166)
	(at-x grass_block-block167 position-16)

	(at-y grass_block-block167 position3)

	(at-z grass_block-block167 position-17)

	(block-present grass_block-block167)
	(at-x grass_block-block168 position-16)

	(at-y grass_block-block168 position3)

	(at-z grass_block-block168 position-16)

	(block-present grass_block-block168)
	(at-x grass_block-block169 position-16)

	(at-y grass_block-block169 position3)

	(at-z grass_block-block169 position-15)

	(block-present grass_block-block169)
	(at-x grass_block-block170 position-16)

	(at-y grass_block-block170 position3)

	(at-z grass_block-block170 position-14)

	(block-present grass_block-block170)
	(at-x grass_block-block171 position-16)

	(at-y grass_block-block171 position3)

	(at-z grass_block-block171 position-13)

	(block-present grass_block-block171)
	(at-x grass_block-block172 position-16)

	(at-y grass_block-block172 position3)

	(at-z grass_block-block172 position-12)

	(block-present grass_block-block172)
	(at-x grass_block-block173 position-16)

	(at-y grass_block-block173 position3)

	(at-z grass_block-block173 position-11)

	(block-present grass_block-block173)
	(at-x grass_block-block174 position-16)

	(at-y grass_block-block174 position3)

	(at-z grass_block-block174 position-10)

	(block-present grass_block-block174)
	(at-x grass_block-block175 position-16)

	(at-y grass_block-block175 position3)

	(at-z grass_block-block175 position-9)

	(block-present grass_block-block175)
	(at-x grass_block-block176 position-16)

	(at-y grass_block-block176 position3)

	(at-z grass_block-block176 position-8)

	(block-present grass_block-block176)
	(at-x grass_block-block177 position-16)

	(at-y grass_block-block177 position3)

	(at-z grass_block-block177 position-7)

	(block-present grass_block-block177)
	(at-x grass_block-block178 position-16)

	(at-y grass_block-block178 position3)

	(at-z grass_block-block178 position-6)

	(block-present grass_block-block178)
	(at-x grass_block-block179 position-16)

	(at-y grass_block-block179 position3)

	(at-z grass_block-block179 position-5)

	(block-present grass_block-block179)
	(at-x grass_block-block180 position-16)

	(at-y grass_block-block180 position3)

	(at-z grass_block-block180 position-4)

	(block-present grass_block-block180)
	(at-x grass_block-block181 position-16)

	(at-y grass_block-block181 position3)

	(at-z grass_block-block181 position-3)

	(block-present grass_block-block181)
	(at-x grass_block-block182 position-16)

	(at-y grass_block-block182 position3)

	(at-z grass_block-block182 position-2)

	(block-present grass_block-block182)
	(at-x grass_block-block183 position-16)

	(at-y grass_block-block183 position3)

	(at-z grass_block-block183 position-1)

	(block-present grass_block-block183)
	(at-x grass_block-block184 position-16)

	(at-y grass_block-block184 position3)

	(at-z grass_block-block184 position0)

	(block-present grass_block-block184)
	(at-x grass_block-block185 position-16)

	(at-y grass_block-block185 position3)

	(at-z grass_block-block185 position1)

	(block-present grass_block-block185)
	(at-x grass_block-block186 position-16)

	(at-y grass_block-block186 position3)

	(at-z grass_block-block186 position2)

	(block-present grass_block-block186)
	(at-x grass_block-block187 position-16)

	(at-y grass_block-block187 position3)

	(at-z grass_block-block187 position3)

	(block-present grass_block-block187)
	(at-x grass_block-block188 position-16)

	(at-y grass_block-block188 position3)

	(at-z grass_block-block188 position4)

	(block-present grass_block-block188)
	(at-x grass_block-block189 position-16)

	(at-y grass_block-block189 position3)

	(at-z grass_block-block189 position5)

	(block-present grass_block-block189)
	(at-x grass_block-block190 position-16)

	(at-y grass_block-block190 position3)

	(at-z grass_block-block190 position6)

	(block-present grass_block-block190)
	(at-x grass_block-block191 position-16)

	(at-y grass_block-block191 position3)

	(at-z grass_block-block191 position7)

	(block-present grass_block-block191)
	(at-x grass_block-block192 position-16)

	(at-y grass_block-block192 position3)

	(at-z grass_block-block192 position8)

	(block-present grass_block-block192)
	(at-x grass_block-block193 position-16)

	(at-y grass_block-block193 position3)

	(at-z grass_block-block193 position9)

	(block-present grass_block-block193)
	(at-x grass_block-block194 position-16)

	(at-y grass_block-block194 position3)

	(at-z grass_block-block194 position10)

	(block-present grass_block-block194)
	(at-x grass_block-block195 position-16)

	(at-y grass_block-block195 position3)

	(at-z grass_block-block195 position11)

	(block-present grass_block-block195)
	(at-x grass_block-block196 position-16)

	(at-y grass_block-block196 position3)

	(at-z grass_block-block196 position12)

	(block-present grass_block-block196)
	(at-x grass_block-block197 position-16)

	(at-y grass_block-block197 position3)

	(at-z grass_block-block197 position13)

	(block-present grass_block-block197)
	(at-x grass_block-block198 position-16)

	(at-y grass_block-block198 position3)

	(at-z grass_block-block198 position14)

	(block-present grass_block-block198)
	(at-x grass_block-block199 position-16)

	(at-y grass_block-block199 position3)

	(at-z grass_block-block199 position15)

	(block-present grass_block-block199)
	(at-x grass_block-block200 position-16)

	(at-y grass_block-block200 position3)

	(at-z grass_block-block200 position16)

	(block-present grass_block-block200)
	(at-x grass_block-block201 position-16)

	(at-y grass_block-block201 position3)

	(at-z grass_block-block201 position17)

	(block-present grass_block-block201)
	(at-x grass_block-block202 position-16)

	(at-y grass_block-block202 position3)

	(at-z grass_block-block202 position18)

	(block-present grass_block-block202)
	(at-x grass_block-block203 position-16)

	(at-y grass_block-block203 position3)

	(at-z grass_block-block203 position19)

	(block-present grass_block-block203)
	(at-x grass_block-block204 position-16)

	(at-y grass_block-block204 position3)

	(at-z grass_block-block204 position20)

	(block-present grass_block-block204)
	(at-x grass_block-block205 position-15)

	(at-y grass_block-block205 position3)

	(at-z grass_block-block205 position-20)

	(block-present grass_block-block205)
	(at-x grass_block-block206 position-15)

	(at-y grass_block-block206 position3)

	(at-z grass_block-block206 position-19)

	(block-present grass_block-block206)
	(at-x grass_block-block207 position-15)

	(at-y grass_block-block207 position3)

	(at-z grass_block-block207 position-18)

	(block-present grass_block-block207)
	(at-x grass_block-block208 position-15)

	(at-y grass_block-block208 position3)

	(at-z grass_block-block208 position-17)

	(block-present grass_block-block208)
	(at-x grass_block-block209 position-15)

	(at-y grass_block-block209 position3)

	(at-z grass_block-block209 position-16)

	(block-present grass_block-block209)
	(at-x grass_block-block210 position-15)

	(at-y grass_block-block210 position3)

	(at-z grass_block-block210 position-15)

	(block-present grass_block-block210)
	(at-x grass_block-block211 position-15)

	(at-y grass_block-block211 position3)

	(at-z grass_block-block211 position-14)

	(block-present grass_block-block211)
	(at-x grass_block-block212 position-15)

	(at-y grass_block-block212 position3)

	(at-z grass_block-block212 position-13)

	(block-present grass_block-block212)
	(at-x grass_block-block213 position-15)

	(at-y grass_block-block213 position3)

	(at-z grass_block-block213 position-12)

	(block-present grass_block-block213)
	(at-x grass_block-block214 position-15)

	(at-y grass_block-block214 position3)

	(at-z grass_block-block214 position-11)

	(block-present grass_block-block214)
	(at-x grass_block-block215 position-15)

	(at-y grass_block-block215 position3)

	(at-z grass_block-block215 position-10)

	(block-present grass_block-block215)
	(at-x grass_block-block216 position-15)

	(at-y grass_block-block216 position3)

	(at-z grass_block-block216 position-9)

	(block-present grass_block-block216)
	(at-x grass_block-block217 position-15)

	(at-y grass_block-block217 position3)

	(at-z grass_block-block217 position-8)

	(block-present grass_block-block217)
	(at-x grass_block-block218 position-15)

	(at-y grass_block-block218 position3)

	(at-z grass_block-block218 position-7)

	(block-present grass_block-block218)
	(at-x grass_block-block219 position-15)

	(at-y grass_block-block219 position3)

	(at-z grass_block-block219 position-6)

	(block-present grass_block-block219)
	(at-x grass_block-block220 position-15)

	(at-y grass_block-block220 position3)

	(at-z grass_block-block220 position-5)

	(block-present grass_block-block220)
	(at-x grass_block-block221 position-15)

	(at-y grass_block-block221 position3)

	(at-z grass_block-block221 position-4)

	(block-present grass_block-block221)
	(at-x grass_block-block222 position-15)

	(at-y grass_block-block222 position3)

	(at-z grass_block-block222 position-3)

	(block-present grass_block-block222)
	(at-x grass_block-block223 position-15)

	(at-y grass_block-block223 position3)

	(at-z grass_block-block223 position-2)

	(block-present grass_block-block223)
	(at-x grass_block-block224 position-15)

	(at-y grass_block-block224 position3)

	(at-z grass_block-block224 position-1)

	(block-present grass_block-block224)
	(at-x grass_block-block225 position-15)

	(at-y grass_block-block225 position3)

	(at-z grass_block-block225 position0)

	(block-present grass_block-block225)
	(at-x grass_block-block226 position-15)

	(at-y grass_block-block226 position3)

	(at-z grass_block-block226 position1)

	(block-present grass_block-block226)
	(at-x grass_block-block227 position-15)

	(at-y grass_block-block227 position3)

	(at-z grass_block-block227 position2)

	(block-present grass_block-block227)
	(at-x grass_block-block228 position-15)

	(at-y grass_block-block228 position3)

	(at-z grass_block-block228 position3)

	(block-present grass_block-block228)
	(at-x grass_block-block229 position-15)

	(at-y grass_block-block229 position3)

	(at-z grass_block-block229 position4)

	(block-present grass_block-block229)
	(at-x grass_block-block230 position-15)

	(at-y grass_block-block230 position3)

	(at-z grass_block-block230 position5)

	(block-present grass_block-block230)
	(at-x grass_block-block231 position-15)

	(at-y grass_block-block231 position3)

	(at-z grass_block-block231 position6)

	(block-present grass_block-block231)
	(at-x grass_block-block232 position-15)

	(at-y grass_block-block232 position3)

	(at-z grass_block-block232 position7)

	(block-present grass_block-block232)
	(at-x grass_block-block233 position-15)

	(at-y grass_block-block233 position3)

	(at-z grass_block-block233 position8)

	(block-present grass_block-block233)
	(at-x grass_block-block234 position-15)

	(at-y grass_block-block234 position3)

	(at-z grass_block-block234 position9)

	(block-present grass_block-block234)
	(at-x grass_block-block235 position-15)

	(at-y grass_block-block235 position3)

	(at-z grass_block-block235 position10)

	(block-present grass_block-block235)
	(at-x grass_block-block236 position-15)

	(at-y grass_block-block236 position3)

	(at-z grass_block-block236 position11)

	(block-present grass_block-block236)
	(at-x grass_block-block237 position-15)

	(at-y grass_block-block237 position3)

	(at-z grass_block-block237 position12)

	(block-present grass_block-block237)
	(at-x grass_block-block238 position-15)

	(at-y grass_block-block238 position3)

	(at-z grass_block-block238 position13)

	(block-present grass_block-block238)
	(at-x grass_block-block239 position-15)

	(at-y grass_block-block239 position3)

	(at-z grass_block-block239 position14)

	(block-present grass_block-block239)
	(at-x grass_block-block240 position-15)

	(at-y grass_block-block240 position3)

	(at-z grass_block-block240 position15)

	(block-present grass_block-block240)
	(at-x grass_block-block241 position-15)

	(at-y grass_block-block241 position3)

	(at-z grass_block-block241 position16)

	(block-present grass_block-block241)
	(at-x grass_block-block242 position-15)

	(at-y grass_block-block242 position3)

	(at-z grass_block-block242 position17)

	(block-present grass_block-block242)
	(at-x grass_block-block243 position-15)

	(at-y grass_block-block243 position3)

	(at-z grass_block-block243 position18)

	(block-present grass_block-block243)
	(at-x grass_block-block244 position-15)

	(at-y grass_block-block244 position3)

	(at-z grass_block-block244 position19)

	(block-present grass_block-block244)
	(at-x grass_block-block245 position-15)

	(at-y grass_block-block245 position3)

	(at-z grass_block-block245 position20)

	(block-present grass_block-block245)
	(at-x grass_block-block246 position-14)

	(at-y grass_block-block246 position3)

	(at-z grass_block-block246 position-20)

	(block-present grass_block-block246)
	(at-x grass_block-block247 position-14)

	(at-y grass_block-block247 position3)

	(at-z grass_block-block247 position-19)

	(block-present grass_block-block247)
	(at-x grass_block-block248 position-14)

	(at-y grass_block-block248 position3)

	(at-z grass_block-block248 position-18)

	(block-present grass_block-block248)
	(at-x grass_block-block249 position-14)

	(at-y grass_block-block249 position3)

	(at-z grass_block-block249 position-17)

	(block-present grass_block-block249)
	(at-x grass_block-block250 position-14)

	(at-y grass_block-block250 position3)

	(at-z grass_block-block250 position-16)

	(block-present grass_block-block250)
	(at-x grass_block-block251 position-14)

	(at-y grass_block-block251 position3)

	(at-z grass_block-block251 position-15)

	(block-present grass_block-block251)
	(at-x grass_block-block252 position-14)

	(at-y grass_block-block252 position3)

	(at-z grass_block-block252 position-14)

	(block-present grass_block-block252)
	(at-x grass_block-block253 position-14)

	(at-y grass_block-block253 position3)

	(at-z grass_block-block253 position-13)

	(block-present grass_block-block253)
	(at-x grass_block-block254 position-14)

	(at-y grass_block-block254 position3)

	(at-z grass_block-block254 position-12)

	(block-present grass_block-block254)
	(at-x grass_block-block255 position-14)

	(at-y grass_block-block255 position3)

	(at-z grass_block-block255 position-11)

	(block-present grass_block-block255)
	(at-x grass_block-block256 position-14)

	(at-y grass_block-block256 position3)

	(at-z grass_block-block256 position-10)

	(block-present grass_block-block256)
	(at-x grass_block-block257 position-14)

	(at-y grass_block-block257 position3)

	(at-z grass_block-block257 position-9)

	(block-present grass_block-block257)
	(at-x grass_block-block258 position-14)

	(at-y grass_block-block258 position3)

	(at-z grass_block-block258 position-8)

	(block-present grass_block-block258)
	(at-x grass_block-block259 position-14)

	(at-y grass_block-block259 position3)

	(at-z grass_block-block259 position-7)

	(block-present grass_block-block259)
	(at-x grass_block-block260 position-14)

	(at-y grass_block-block260 position3)

	(at-z grass_block-block260 position-6)

	(block-present grass_block-block260)
	(at-x grass_block-block261 position-14)

	(at-y grass_block-block261 position3)

	(at-z grass_block-block261 position-5)

	(block-present grass_block-block261)
	(at-x grass_block-block262 position-14)

	(at-y grass_block-block262 position3)

	(at-z grass_block-block262 position-4)

	(block-present grass_block-block262)
	(at-x grass_block-block263 position-14)

	(at-y grass_block-block263 position3)

	(at-z grass_block-block263 position-3)

	(block-present grass_block-block263)
	(at-x grass_block-block264 position-14)

	(at-y grass_block-block264 position3)

	(at-z grass_block-block264 position-2)

	(block-present grass_block-block264)
	(at-x grass_block-block265 position-14)

	(at-y grass_block-block265 position3)

	(at-z grass_block-block265 position-1)

	(block-present grass_block-block265)
	(at-x grass_block-block266 position-14)

	(at-y grass_block-block266 position3)

	(at-z grass_block-block266 position0)

	(block-present grass_block-block266)
	(at-x grass_block-block267 position-14)

	(at-y grass_block-block267 position3)

	(at-z grass_block-block267 position1)

	(block-present grass_block-block267)
	(at-x grass_block-block268 position-14)

	(at-y grass_block-block268 position3)

	(at-z grass_block-block268 position2)

	(block-present grass_block-block268)
	(at-x grass_block-block269 position-14)

	(at-y grass_block-block269 position3)

	(at-z grass_block-block269 position3)

	(block-present grass_block-block269)
	(at-x grass_block-block270 position-14)

	(at-y grass_block-block270 position3)

	(at-z grass_block-block270 position4)

	(block-present grass_block-block270)
	(at-x grass_block-block271 position-14)

	(at-y grass_block-block271 position3)

	(at-z grass_block-block271 position5)

	(block-present grass_block-block271)
	(at-x grass_block-block272 position-14)

	(at-y grass_block-block272 position3)

	(at-z grass_block-block272 position6)

	(block-present grass_block-block272)
	(at-x grass_block-block273 position-14)

	(at-y grass_block-block273 position3)

	(at-z grass_block-block273 position7)

	(block-present grass_block-block273)
	(at-x grass_block-block274 position-14)

	(at-y grass_block-block274 position3)

	(at-z grass_block-block274 position8)

	(block-present grass_block-block274)
	(at-x grass_block-block275 position-14)

	(at-y grass_block-block275 position3)

	(at-z grass_block-block275 position9)

	(block-present grass_block-block275)
	(at-x grass_block-block276 position-14)

	(at-y grass_block-block276 position3)

	(at-z grass_block-block276 position10)

	(block-present grass_block-block276)
	(at-x grass_block-block277 position-14)

	(at-y grass_block-block277 position3)

	(at-z grass_block-block277 position11)

	(block-present grass_block-block277)
	(at-x grass_block-block278 position-14)

	(at-y grass_block-block278 position3)

	(at-z grass_block-block278 position12)

	(block-present grass_block-block278)
	(at-x grass_block-block279 position-14)

	(at-y grass_block-block279 position3)

	(at-z grass_block-block279 position13)

	(block-present grass_block-block279)
	(at-x grass_block-block280 position-14)

	(at-y grass_block-block280 position3)

	(at-z grass_block-block280 position14)

	(block-present grass_block-block280)
	(at-x grass_block-block281 position-14)

	(at-y grass_block-block281 position3)

	(at-z grass_block-block281 position15)

	(block-present grass_block-block281)
	(at-x grass_block-block282 position-14)

	(at-y grass_block-block282 position3)

	(at-z grass_block-block282 position16)

	(block-present grass_block-block282)
	(at-x grass_block-block283 position-14)

	(at-y grass_block-block283 position3)

	(at-z grass_block-block283 position17)

	(block-present grass_block-block283)
	(at-x grass_block-block284 position-14)

	(at-y grass_block-block284 position3)

	(at-z grass_block-block284 position18)

	(block-present grass_block-block284)
	(at-x grass_block-block285 position-14)

	(at-y grass_block-block285 position3)

	(at-z grass_block-block285 position19)

	(block-present grass_block-block285)
	(at-x grass_block-block286 position-14)

	(at-y grass_block-block286 position3)

	(at-z grass_block-block286 position20)

	(block-present grass_block-block286)
	(at-x grass_block-block287 position-13)

	(at-y grass_block-block287 position3)

	(at-z grass_block-block287 position-20)

	(block-present grass_block-block287)
	(at-x grass_block-block288 position-13)

	(at-y grass_block-block288 position3)

	(at-z grass_block-block288 position-19)

	(block-present grass_block-block288)
	(at-x grass_block-block289 position-13)

	(at-y grass_block-block289 position3)

	(at-z grass_block-block289 position-18)

	(block-present grass_block-block289)
	(at-x grass_block-block290 position-13)

	(at-y grass_block-block290 position3)

	(at-z grass_block-block290 position-17)

	(block-present grass_block-block290)
	(at-x grass_block-block291 position-13)

	(at-y grass_block-block291 position3)

	(at-z grass_block-block291 position-16)

	(block-present grass_block-block291)
	(at-x grass_block-block292 position-13)

	(at-y grass_block-block292 position3)

	(at-z grass_block-block292 position-15)

	(block-present grass_block-block292)
	(at-x grass_block-block293 position-13)

	(at-y grass_block-block293 position3)

	(at-z grass_block-block293 position-14)

	(block-present grass_block-block293)
	(at-x grass_block-block294 position-13)

	(at-y grass_block-block294 position3)

	(at-z grass_block-block294 position-13)

	(block-present grass_block-block294)
	(at-x grass_block-block295 position-13)

	(at-y grass_block-block295 position3)

	(at-z grass_block-block295 position-12)

	(block-present grass_block-block295)
	(at-x grass_block-block296 position-13)

	(at-y grass_block-block296 position3)

	(at-z grass_block-block296 position-11)

	(block-present grass_block-block296)
	(at-x grass_block-block297 position-13)

	(at-y grass_block-block297 position3)

	(at-z grass_block-block297 position-10)

	(block-present grass_block-block297)
	(at-x grass_block-block298 position-13)

	(at-y grass_block-block298 position3)

	(at-z grass_block-block298 position-9)

	(block-present grass_block-block298)
	(at-x grass_block-block299 position-13)

	(at-y grass_block-block299 position3)

	(at-z grass_block-block299 position-8)

	(block-present grass_block-block299)
	(at-x grass_block-block300 position-13)

	(at-y grass_block-block300 position3)

	(at-z grass_block-block300 position-7)

	(block-present grass_block-block300)
	(at-x grass_block-block301 position-13)

	(at-y grass_block-block301 position3)

	(at-z grass_block-block301 position-6)

	(block-present grass_block-block301)
	(at-x grass_block-block302 position-13)

	(at-y grass_block-block302 position3)

	(at-z grass_block-block302 position-5)

	(block-present grass_block-block302)
	(at-x grass_block-block303 position-13)

	(at-y grass_block-block303 position3)

	(at-z grass_block-block303 position-4)

	(block-present grass_block-block303)
	(at-x grass_block-block304 position-13)

	(at-y grass_block-block304 position3)

	(at-z grass_block-block304 position-3)

	(block-present grass_block-block304)
	(at-x grass_block-block305 position-13)

	(at-y grass_block-block305 position3)

	(at-z grass_block-block305 position-2)

	(block-present grass_block-block305)
	(at-x grass_block-block306 position-13)

	(at-y grass_block-block306 position3)

	(at-z grass_block-block306 position-1)

	(block-present grass_block-block306)
	(at-x grass_block-block307 position-13)

	(at-y grass_block-block307 position3)

	(at-z grass_block-block307 position0)

	(block-present grass_block-block307)
	(at-x grass_block-block308 position-13)

	(at-y grass_block-block308 position3)

	(at-z grass_block-block308 position1)

	(block-present grass_block-block308)
	(at-x grass_block-block309 position-13)

	(at-y grass_block-block309 position3)

	(at-z grass_block-block309 position2)

	(block-present grass_block-block309)
	(at-x grass_block-block310 position-13)

	(at-y grass_block-block310 position3)

	(at-z grass_block-block310 position3)

	(block-present grass_block-block310)
	(at-x grass_block-block311 position-13)

	(at-y grass_block-block311 position3)

	(at-z grass_block-block311 position4)

	(block-present grass_block-block311)
	(at-x grass_block-block312 position-13)

	(at-y grass_block-block312 position3)

	(at-z grass_block-block312 position5)

	(block-present grass_block-block312)
	(at-x grass_block-block313 position-13)

	(at-y grass_block-block313 position3)

	(at-z grass_block-block313 position6)

	(block-present grass_block-block313)
	(at-x grass_block-block314 position-13)

	(at-y grass_block-block314 position3)

	(at-z grass_block-block314 position7)

	(block-present grass_block-block314)
	(at-x grass_block-block315 position-13)

	(at-y grass_block-block315 position3)

	(at-z grass_block-block315 position8)

	(block-present grass_block-block315)
	(at-x grass_block-block316 position-13)

	(at-y grass_block-block316 position3)

	(at-z grass_block-block316 position9)

	(block-present grass_block-block316)
	(at-x grass_block-block317 position-13)

	(at-y grass_block-block317 position3)

	(at-z grass_block-block317 position10)

	(block-present grass_block-block317)
	(at-x grass_block-block318 position-13)

	(at-y grass_block-block318 position3)

	(at-z grass_block-block318 position11)

	(block-present grass_block-block318)
	(at-x grass_block-block319 position-13)

	(at-y grass_block-block319 position3)

	(at-z grass_block-block319 position12)

	(block-present grass_block-block319)
	(at-x grass_block-block320 position-13)

	(at-y grass_block-block320 position3)

	(at-z grass_block-block320 position13)

	(block-present grass_block-block320)
	(at-x grass_block-block321 position-13)

	(at-y grass_block-block321 position3)

	(at-z grass_block-block321 position14)

	(block-present grass_block-block321)
	(at-x grass_block-block322 position-13)

	(at-y grass_block-block322 position3)

	(at-z grass_block-block322 position15)

	(block-present grass_block-block322)
	(at-x grass_block-block323 position-13)

	(at-y grass_block-block323 position3)

	(at-z grass_block-block323 position16)

	(block-present grass_block-block323)
	(at-x grass_block-block324 position-13)

	(at-y grass_block-block324 position3)

	(at-z grass_block-block324 position17)

	(block-present grass_block-block324)
	(at-x grass_block-block325 position-13)

	(at-y grass_block-block325 position3)

	(at-z grass_block-block325 position18)

	(block-present grass_block-block325)
	(at-x grass_block-block326 position-13)

	(at-y grass_block-block326 position3)

	(at-z grass_block-block326 position19)

	(block-present grass_block-block326)
	(at-x grass_block-block327 position-13)

	(at-y grass_block-block327 position3)

	(at-z grass_block-block327 position20)

	(block-present grass_block-block327)
	(at-x grass_block-block328 position-12)

	(at-y grass_block-block328 position3)

	(at-z grass_block-block328 position-20)

	(block-present grass_block-block328)
	(at-x grass_block-block329 position-12)

	(at-y grass_block-block329 position3)

	(at-z grass_block-block329 position-19)

	(block-present grass_block-block329)
	(at-x grass_block-block330 position-12)

	(at-y grass_block-block330 position3)

	(at-z grass_block-block330 position-18)

	(block-present grass_block-block330)
	(at-x grass_block-block331 position-12)

	(at-y grass_block-block331 position3)

	(at-z grass_block-block331 position-17)

	(block-present grass_block-block331)
	(at-x grass_block-block332 position-12)

	(at-y grass_block-block332 position3)

	(at-z grass_block-block332 position-16)

	(block-present grass_block-block332)
	(at-x grass_block-block333 position-12)

	(at-y grass_block-block333 position3)

	(at-z grass_block-block333 position-15)

	(block-present grass_block-block333)
	(at-x grass_block-block334 position-12)

	(at-y grass_block-block334 position3)

	(at-z grass_block-block334 position-14)

	(block-present grass_block-block334)
	(at-x grass_block-block335 position-12)

	(at-y grass_block-block335 position3)

	(at-z grass_block-block335 position-13)

	(block-present grass_block-block335)
	(at-x grass_block-block336 position-12)

	(at-y grass_block-block336 position3)

	(at-z grass_block-block336 position-12)

	(block-present grass_block-block336)
	(at-x grass_block-block337 position-12)

	(at-y grass_block-block337 position3)

	(at-z grass_block-block337 position-11)

	(block-present grass_block-block337)
	(at-x grass_block-block338 position-12)

	(at-y grass_block-block338 position3)

	(at-z grass_block-block338 position-10)

	(block-present grass_block-block338)
	(at-x grass_block-block339 position-12)

	(at-y grass_block-block339 position3)

	(at-z grass_block-block339 position-9)

	(block-present grass_block-block339)
	(at-x grass_block-block340 position-12)

	(at-y grass_block-block340 position3)

	(at-z grass_block-block340 position-8)

	(block-present grass_block-block340)
	(at-x grass_block-block341 position-12)

	(at-y grass_block-block341 position3)

	(at-z grass_block-block341 position-7)

	(block-present grass_block-block341)
	(at-x grass_block-block342 position-12)

	(at-y grass_block-block342 position3)

	(at-z grass_block-block342 position-6)

	(block-present grass_block-block342)
	(at-x grass_block-block343 position-12)

	(at-y grass_block-block343 position3)

	(at-z grass_block-block343 position-5)

	(block-present grass_block-block343)
	(at-x grass_block-block344 position-12)

	(at-y grass_block-block344 position3)

	(at-z grass_block-block344 position-4)

	(block-present grass_block-block344)
	(at-x grass_block-block345 position-12)

	(at-y grass_block-block345 position3)

	(at-z grass_block-block345 position-3)

	(block-present grass_block-block345)
	(at-x grass_block-block346 position-12)

	(at-y grass_block-block346 position3)

	(at-z grass_block-block346 position-2)

	(block-present grass_block-block346)
	(at-x grass_block-block347 position-12)

	(at-y grass_block-block347 position3)

	(at-z grass_block-block347 position-1)

	(block-present grass_block-block347)
	(at-x grass_block-block348 position-12)

	(at-y grass_block-block348 position3)

	(at-z grass_block-block348 position0)

	(block-present grass_block-block348)
	(at-x grass_block-block349 position-12)

	(at-y grass_block-block349 position3)

	(at-z grass_block-block349 position1)

	(block-present grass_block-block349)
	(at-x grass_block-block350 position-12)

	(at-y grass_block-block350 position3)

	(at-z grass_block-block350 position2)

	(block-present grass_block-block350)
	(at-x grass_block-block351 position-12)

	(at-y grass_block-block351 position3)

	(at-z grass_block-block351 position3)

	(block-present grass_block-block351)
	(at-x grass_block-block352 position-12)

	(at-y grass_block-block352 position3)

	(at-z grass_block-block352 position4)

	(block-present grass_block-block352)
	(at-x grass_block-block353 position-12)

	(at-y grass_block-block353 position3)

	(at-z grass_block-block353 position5)

	(block-present grass_block-block353)
	(at-x grass_block-block354 position-12)

	(at-y grass_block-block354 position3)

	(at-z grass_block-block354 position6)

	(block-present grass_block-block354)
	(at-x grass_block-block355 position-12)

	(at-y grass_block-block355 position3)

	(at-z grass_block-block355 position7)

	(block-present grass_block-block355)
	(at-x grass_block-block356 position-12)

	(at-y grass_block-block356 position3)

	(at-z grass_block-block356 position8)

	(block-present grass_block-block356)
	(at-x grass_block-block357 position-12)

	(at-y grass_block-block357 position3)

	(at-z grass_block-block357 position9)

	(block-present grass_block-block357)
	(at-x grass_block-block358 position-12)

	(at-y grass_block-block358 position3)

	(at-z grass_block-block358 position10)

	(block-present grass_block-block358)
	(at-x grass_block-block359 position-12)

	(at-y grass_block-block359 position3)

	(at-z grass_block-block359 position11)

	(block-present grass_block-block359)
	(at-x grass_block-block360 position-12)

	(at-y grass_block-block360 position3)

	(at-z grass_block-block360 position12)

	(block-present grass_block-block360)
	(at-x grass_block-block361 position-12)

	(at-y grass_block-block361 position3)

	(at-z grass_block-block361 position13)

	(block-present grass_block-block361)
	(at-x grass_block-block362 position-12)

	(at-y grass_block-block362 position3)

	(at-z grass_block-block362 position14)

	(block-present grass_block-block362)
	(at-x grass_block-block363 position-12)

	(at-y grass_block-block363 position3)

	(at-z grass_block-block363 position15)

	(block-present grass_block-block363)
	(at-x grass_block-block364 position-12)

	(at-y grass_block-block364 position3)

	(at-z grass_block-block364 position16)

	(block-present grass_block-block364)
	(at-x grass_block-block365 position-12)

	(at-y grass_block-block365 position3)

	(at-z grass_block-block365 position17)

	(block-present grass_block-block365)
	(at-x grass_block-block366 position-12)

	(at-y grass_block-block366 position3)

	(at-z grass_block-block366 position18)

	(block-present grass_block-block366)
	(at-x grass_block-block367 position-12)

	(at-y grass_block-block367 position3)

	(at-z grass_block-block367 position19)

	(block-present grass_block-block367)
	(at-x grass_block-block368 position-12)

	(at-y grass_block-block368 position3)

	(at-z grass_block-block368 position20)

	(block-present grass_block-block368)
	(at-x grass_block-block369 position-11)

	(at-y grass_block-block369 position3)

	(at-z grass_block-block369 position-20)

	(block-present grass_block-block369)
	(at-x grass_block-block370 position-11)

	(at-y grass_block-block370 position3)

	(at-z grass_block-block370 position-19)

	(block-present grass_block-block370)
	(at-x grass_block-block371 position-11)

	(at-y grass_block-block371 position3)

	(at-z grass_block-block371 position-18)

	(block-present grass_block-block371)
	(at-x grass_block-block372 position-11)

	(at-y grass_block-block372 position3)

	(at-z grass_block-block372 position-17)

	(block-present grass_block-block372)
	(at-x grass_block-block373 position-11)

	(at-y grass_block-block373 position3)

	(at-z grass_block-block373 position-16)

	(block-present grass_block-block373)
	(at-x grass_block-block374 position-11)

	(at-y grass_block-block374 position3)

	(at-z grass_block-block374 position-15)

	(block-present grass_block-block374)
	(at-x grass_block-block375 position-11)

	(at-y grass_block-block375 position3)

	(at-z grass_block-block375 position-14)

	(block-present grass_block-block375)
	(at-x grass_block-block376 position-11)

	(at-y grass_block-block376 position3)

	(at-z grass_block-block376 position-13)

	(block-present grass_block-block376)
	(at-x grass_block-block377 position-11)

	(at-y grass_block-block377 position3)

	(at-z grass_block-block377 position-12)

	(block-present grass_block-block377)
	(at-x grass_block-block378 position-11)

	(at-y grass_block-block378 position3)

	(at-z grass_block-block378 position-11)

	(block-present grass_block-block378)
	(at-x grass_block-block379 position-11)

	(at-y grass_block-block379 position3)

	(at-z grass_block-block379 position-10)

	(block-present grass_block-block379)
	(at-x grass_block-block380 position-11)

	(at-y grass_block-block380 position3)

	(at-z grass_block-block380 position-9)

	(block-present grass_block-block380)
	(at-x grass_block-block381 position-11)

	(at-y grass_block-block381 position3)

	(at-z grass_block-block381 position-8)

	(block-present grass_block-block381)
	(at-x grass_block-block382 position-11)

	(at-y grass_block-block382 position3)

	(at-z grass_block-block382 position-7)

	(block-present grass_block-block382)
	(at-x grass_block-block383 position-11)

	(at-y grass_block-block383 position3)

	(at-z grass_block-block383 position-6)

	(block-present grass_block-block383)
	(at-x grass_block-block384 position-11)

	(at-y grass_block-block384 position3)

	(at-z grass_block-block384 position-5)

	(block-present grass_block-block384)
	(at-x grass_block-block385 position-11)

	(at-y grass_block-block385 position3)

	(at-z grass_block-block385 position-4)

	(block-present grass_block-block385)
	(at-x grass_block-block386 position-11)

	(at-y grass_block-block386 position3)

	(at-z grass_block-block386 position-3)

	(block-present grass_block-block386)
	(at-x grass_block-block387 position-11)

	(at-y grass_block-block387 position3)

	(at-z grass_block-block387 position-2)

	(block-present grass_block-block387)
	(at-x grass_block-block388 position-11)

	(at-y grass_block-block388 position3)

	(at-z grass_block-block388 position-1)

	(block-present grass_block-block388)
	(at-x grass_block-block389 position-11)

	(at-y grass_block-block389 position3)

	(at-z grass_block-block389 position0)

	(block-present grass_block-block389)
	(at-x grass_block-block390 position-11)

	(at-y grass_block-block390 position3)

	(at-z grass_block-block390 position1)

	(block-present grass_block-block390)
	(at-x grass_block-block391 position-11)

	(at-y grass_block-block391 position3)

	(at-z grass_block-block391 position2)

	(block-present grass_block-block391)
	(at-x grass_block-block392 position-11)

	(at-y grass_block-block392 position3)

	(at-z grass_block-block392 position3)

	(block-present grass_block-block392)
	(at-x grass_block-block393 position-11)

	(at-y grass_block-block393 position3)

	(at-z grass_block-block393 position4)

	(block-present grass_block-block393)
	(at-x grass_block-block394 position-11)

	(at-y grass_block-block394 position3)

	(at-z grass_block-block394 position5)

	(block-present grass_block-block394)
	(at-x grass_block-block395 position-11)

	(at-y grass_block-block395 position3)

	(at-z grass_block-block395 position6)

	(block-present grass_block-block395)
	(at-x grass_block-block396 position-11)

	(at-y grass_block-block396 position3)

	(at-z grass_block-block396 position7)

	(block-present grass_block-block396)
	(at-x grass_block-block397 position-11)

	(at-y grass_block-block397 position3)

	(at-z grass_block-block397 position8)

	(block-present grass_block-block397)
	(at-x grass_block-block398 position-11)

	(at-y grass_block-block398 position3)

	(at-z grass_block-block398 position9)

	(block-present grass_block-block398)
	(at-x grass_block-block399 position-11)

	(at-y grass_block-block399 position3)

	(at-z grass_block-block399 position10)

	(block-present grass_block-block399)
	(at-x grass_block-block400 position-11)

	(at-y grass_block-block400 position3)

	(at-z grass_block-block400 position11)

	(block-present grass_block-block400)
	(at-x grass_block-block401 position-11)

	(at-y grass_block-block401 position3)

	(at-z grass_block-block401 position12)

	(block-present grass_block-block401)
	(at-x grass_block-block402 position-11)

	(at-y grass_block-block402 position3)

	(at-z grass_block-block402 position13)

	(block-present grass_block-block402)
	(at-x grass_block-block403 position-11)

	(at-y grass_block-block403 position3)

	(at-z grass_block-block403 position14)

	(block-present grass_block-block403)
	(at-x grass_block-block404 position-11)

	(at-y grass_block-block404 position3)

	(at-z grass_block-block404 position15)

	(block-present grass_block-block404)
	(at-x grass_block-block405 position-11)

	(at-y grass_block-block405 position3)

	(at-z grass_block-block405 position16)

	(block-present grass_block-block405)
	(at-x grass_block-block406 position-11)

	(at-y grass_block-block406 position3)

	(at-z grass_block-block406 position17)

	(block-present grass_block-block406)
	(at-x grass_block-block407 position-11)

	(at-y grass_block-block407 position3)

	(at-z grass_block-block407 position18)

	(block-present grass_block-block407)
	(at-x grass_block-block408 position-11)

	(at-y grass_block-block408 position3)

	(at-z grass_block-block408 position19)

	(block-present grass_block-block408)
	(at-x grass_block-block409 position-11)

	(at-y grass_block-block409 position3)

	(at-z grass_block-block409 position20)

	(block-present grass_block-block409)
	(at-x grass_block-block410 position-10)

	(at-y grass_block-block410 position3)

	(at-z grass_block-block410 position-20)

	(block-present grass_block-block410)
	(at-x grass_block-block411 position-10)

	(at-y grass_block-block411 position3)

	(at-z grass_block-block411 position-19)

	(block-present grass_block-block411)
	(at-x grass_block-block412 position-10)

	(at-y grass_block-block412 position3)

	(at-z grass_block-block412 position-18)

	(block-present grass_block-block412)
	(at-x grass_block-block413 position-10)

	(at-y grass_block-block413 position3)

	(at-z grass_block-block413 position-17)

	(block-present grass_block-block413)
	(at-x grass_block-block414 position-10)

	(at-y grass_block-block414 position3)

	(at-z grass_block-block414 position-16)

	(block-present grass_block-block414)
	(at-x grass_block-block415 position-10)

	(at-y grass_block-block415 position3)

	(at-z grass_block-block415 position-15)

	(block-present grass_block-block415)
	(at-x grass_block-block416 position-10)

	(at-y grass_block-block416 position3)

	(at-z grass_block-block416 position-14)

	(block-present grass_block-block416)
	(at-x grass_block-block417 position-10)

	(at-y grass_block-block417 position3)

	(at-z grass_block-block417 position-13)

	(block-present grass_block-block417)
	(at-x grass_block-block418 position-10)

	(at-y grass_block-block418 position3)

	(at-z grass_block-block418 position-12)

	(block-present grass_block-block418)
	(at-x grass_block-block419 position-10)

	(at-y grass_block-block419 position3)

	(at-z grass_block-block419 position-11)

	(block-present grass_block-block419)
	(at-x grass_block-block420 position-10)

	(at-y grass_block-block420 position3)

	(at-z grass_block-block420 position-10)

	(block-present grass_block-block420)
	(at-x grass_block-block421 position-10)

	(at-y grass_block-block421 position3)

	(at-z grass_block-block421 position-9)

	(block-present grass_block-block421)
	(at-x grass_block-block422 position-10)

	(at-y grass_block-block422 position3)

	(at-z grass_block-block422 position-8)

	(block-present grass_block-block422)
	(at-x grass_block-block423 position-10)

	(at-y grass_block-block423 position3)

	(at-z grass_block-block423 position-7)

	(block-present grass_block-block423)
	(at-x grass_block-block424 position-10)

	(at-y grass_block-block424 position3)

	(at-z grass_block-block424 position-6)

	(block-present grass_block-block424)
	(at-x grass_block-block425 position-10)

	(at-y grass_block-block425 position3)

	(at-z grass_block-block425 position-5)

	(block-present grass_block-block425)
	(at-x grass_block-block426 position-10)

	(at-y grass_block-block426 position3)

	(at-z grass_block-block426 position-4)

	(block-present grass_block-block426)
	(at-x grass_block-block427 position-10)

	(at-y grass_block-block427 position3)

	(at-z grass_block-block427 position-3)

	(block-present grass_block-block427)
	(at-x grass_block-block428 position-10)

	(at-y grass_block-block428 position3)

	(at-z grass_block-block428 position-2)

	(block-present grass_block-block428)
	(at-x grass_block-block429 position-10)

	(at-y grass_block-block429 position3)

	(at-z grass_block-block429 position-1)

	(block-present grass_block-block429)
	(at-x grass_block-block430 position-10)

	(at-y grass_block-block430 position3)

	(at-z grass_block-block430 position0)

	(block-present grass_block-block430)
	(at-x grass_block-block431 position-10)

	(at-y grass_block-block431 position3)

	(at-z grass_block-block431 position1)

	(block-present grass_block-block431)
	(at-x grass_block-block432 position-10)

	(at-y grass_block-block432 position3)

	(at-z grass_block-block432 position2)

	(block-present grass_block-block432)
	(at-x grass_block-block433 position-10)

	(at-y grass_block-block433 position3)

	(at-z grass_block-block433 position3)

	(block-present grass_block-block433)
	(at-x grass_block-block434 position-10)

	(at-y grass_block-block434 position3)

	(at-z grass_block-block434 position4)

	(block-present grass_block-block434)
	(at-x grass_block-block435 position-10)

	(at-y grass_block-block435 position3)

	(at-z grass_block-block435 position5)

	(block-present grass_block-block435)
	(at-x grass_block-block436 position-10)

	(at-y grass_block-block436 position3)

	(at-z grass_block-block436 position6)

	(block-present grass_block-block436)
	(at-x grass_block-block437 position-10)

	(at-y grass_block-block437 position3)

	(at-z grass_block-block437 position7)

	(block-present grass_block-block437)
	(at-x grass_block-block438 position-10)

	(at-y grass_block-block438 position3)

	(at-z grass_block-block438 position8)

	(block-present grass_block-block438)
	(at-x grass_block-block439 position-10)

	(at-y grass_block-block439 position3)

	(at-z grass_block-block439 position9)

	(block-present grass_block-block439)
	(at-x grass_block-block440 position-10)

	(at-y grass_block-block440 position3)

	(at-z grass_block-block440 position10)

	(block-present grass_block-block440)
	(at-x grass_block-block441 position-10)

	(at-y grass_block-block441 position3)

	(at-z grass_block-block441 position11)

	(block-present grass_block-block441)
	(at-x grass_block-block442 position-10)

	(at-y grass_block-block442 position3)

	(at-z grass_block-block442 position12)

	(block-present grass_block-block442)
	(at-x grass_block-block443 position-10)

	(at-y grass_block-block443 position3)

	(at-z grass_block-block443 position13)

	(block-present grass_block-block443)
	(at-x grass_block-block444 position-10)

	(at-y grass_block-block444 position3)

	(at-z grass_block-block444 position14)

	(block-present grass_block-block444)
	(at-x grass_block-block445 position-10)

	(at-y grass_block-block445 position3)

	(at-z grass_block-block445 position15)

	(block-present grass_block-block445)
	(at-x grass_block-block446 position-10)

	(at-y grass_block-block446 position3)

	(at-z grass_block-block446 position16)

	(block-present grass_block-block446)
	(at-x grass_block-block447 position-10)

	(at-y grass_block-block447 position3)

	(at-z grass_block-block447 position17)

	(block-present grass_block-block447)
	(at-x grass_block-block448 position-10)

	(at-y grass_block-block448 position3)

	(at-z grass_block-block448 position18)

	(block-present grass_block-block448)
	(at-x grass_block-block449 position-10)

	(at-y grass_block-block449 position3)

	(at-z grass_block-block449 position19)

	(block-present grass_block-block449)
	(at-x grass_block-block450 position-10)

	(at-y grass_block-block450 position3)

	(at-z grass_block-block450 position20)

	(block-present grass_block-block450)
	(at-x grass_block-block451 position-9)

	(at-y grass_block-block451 position3)

	(at-z grass_block-block451 position-20)

	(block-present grass_block-block451)
	(at-x grass_block-block452 position-9)

	(at-y grass_block-block452 position3)

	(at-z grass_block-block452 position-19)

	(block-present grass_block-block452)
	(at-x grass_block-block453 position-9)

	(at-y grass_block-block453 position3)

	(at-z grass_block-block453 position-18)

	(block-present grass_block-block453)
	(at-x grass_block-block454 position-9)

	(at-y grass_block-block454 position3)

	(at-z grass_block-block454 position-17)

	(block-present grass_block-block454)
	(at-x grass_block-block455 position-9)

	(at-y grass_block-block455 position3)

	(at-z grass_block-block455 position-16)

	(block-present grass_block-block455)
	(at-x grass_block-block456 position-9)

	(at-y grass_block-block456 position3)

	(at-z grass_block-block456 position-15)

	(block-present grass_block-block456)
	(at-x grass_block-block457 position-9)

	(at-y grass_block-block457 position3)

	(at-z grass_block-block457 position-14)

	(block-present grass_block-block457)
	(at-x grass_block-block458 position-9)

	(at-y grass_block-block458 position3)

	(at-z grass_block-block458 position-13)

	(block-present grass_block-block458)
	(at-x grass_block-block459 position-9)

	(at-y grass_block-block459 position3)

	(at-z grass_block-block459 position-12)

	(block-present grass_block-block459)
	(at-x grass_block-block460 position-9)

	(at-y grass_block-block460 position3)

	(at-z grass_block-block460 position-11)

	(block-present grass_block-block460)
	(at-x grass_block-block461 position-9)

	(at-y grass_block-block461 position3)

	(at-z grass_block-block461 position-10)

	(block-present grass_block-block461)
	(at-x grass_block-block462 position-9)

	(at-y grass_block-block462 position3)

	(at-z grass_block-block462 position-9)

	(block-present grass_block-block462)
	(at-x grass_block-block463 position-9)

	(at-y grass_block-block463 position3)

	(at-z grass_block-block463 position-8)

	(block-present grass_block-block463)
	(at-x grass_block-block464 position-9)

	(at-y grass_block-block464 position3)

	(at-z grass_block-block464 position-7)

	(block-present grass_block-block464)
	(at-x grass_block-block465 position-9)

	(at-y grass_block-block465 position3)

	(at-z grass_block-block465 position-6)

	(block-present grass_block-block465)
	(at-x grass_block-block466 position-9)

	(at-y grass_block-block466 position3)

	(at-z grass_block-block466 position-5)

	(block-present grass_block-block466)
	(at-x grass_block-block467 position-9)

	(at-y grass_block-block467 position3)

	(at-z grass_block-block467 position-4)

	(block-present grass_block-block467)
	(at-x grass_block-block468 position-9)

	(at-y grass_block-block468 position3)

	(at-z grass_block-block468 position-3)

	(block-present grass_block-block468)
	(at-x grass_block-block469 position-9)

	(at-y grass_block-block469 position3)

	(at-z grass_block-block469 position-2)

	(block-present grass_block-block469)
	(at-x grass_block-block470 position-9)

	(at-y grass_block-block470 position3)

	(at-z grass_block-block470 position-1)

	(block-present grass_block-block470)
	(at-x grass_block-block471 position-9)

	(at-y grass_block-block471 position3)

	(at-z grass_block-block471 position0)

	(block-present grass_block-block471)
	(at-x grass_block-block472 position-9)

	(at-y grass_block-block472 position3)

	(at-z grass_block-block472 position1)

	(block-present grass_block-block472)
	(at-x grass_block-block473 position-9)

	(at-y grass_block-block473 position3)

	(at-z grass_block-block473 position2)

	(block-present grass_block-block473)
	(at-x grass_block-block474 position-9)

	(at-y grass_block-block474 position3)

	(at-z grass_block-block474 position3)

	(block-present grass_block-block474)
	(at-x grass_block-block475 position-9)

	(at-y grass_block-block475 position3)

	(at-z grass_block-block475 position4)

	(block-present grass_block-block475)
	(at-x grass_block-block476 position-9)

	(at-y grass_block-block476 position3)

	(at-z grass_block-block476 position5)

	(block-present grass_block-block476)
	(at-x grass_block-block477 position-9)

	(at-y grass_block-block477 position3)

	(at-z grass_block-block477 position6)

	(block-present grass_block-block477)
	(at-x grass_block-block478 position-9)

	(at-y grass_block-block478 position3)

	(at-z grass_block-block478 position7)

	(block-present grass_block-block478)
	(at-x grass_block-block479 position-9)

	(at-y grass_block-block479 position3)

	(at-z grass_block-block479 position8)

	(block-present grass_block-block479)
	(at-x grass_block-block480 position-9)

	(at-y grass_block-block480 position3)

	(at-z grass_block-block480 position9)

	(block-present grass_block-block480)
	(at-x grass_block-block481 position-9)

	(at-y grass_block-block481 position3)

	(at-z grass_block-block481 position10)

	(block-present grass_block-block481)
	(at-x grass_block-block482 position-9)

	(at-y grass_block-block482 position3)

	(at-z grass_block-block482 position11)

	(block-present grass_block-block482)
	(at-x grass_block-block483 position-9)

	(at-y grass_block-block483 position3)

	(at-z grass_block-block483 position12)

	(block-present grass_block-block483)
	(at-x grass_block-block484 position-9)

	(at-y grass_block-block484 position3)

	(at-z grass_block-block484 position13)

	(block-present grass_block-block484)
	(at-x grass_block-block485 position-9)

	(at-y grass_block-block485 position3)

	(at-z grass_block-block485 position14)

	(block-present grass_block-block485)
	(at-x grass_block-block486 position-9)

	(at-y grass_block-block486 position3)

	(at-z grass_block-block486 position15)

	(block-present grass_block-block486)
	(at-x grass_block-block487 position-9)

	(at-y grass_block-block487 position3)

	(at-z grass_block-block487 position16)

	(block-present grass_block-block487)
	(at-x grass_block-block488 position-9)

	(at-y grass_block-block488 position3)

	(at-z grass_block-block488 position17)

	(block-present grass_block-block488)
	(at-x grass_block-block489 position-9)

	(at-y grass_block-block489 position3)

	(at-z grass_block-block489 position18)

	(block-present grass_block-block489)
	(at-x grass_block-block490 position-9)

	(at-y grass_block-block490 position3)

	(at-z grass_block-block490 position19)

	(block-present grass_block-block490)
	(at-x grass_block-block491 position-9)

	(at-y grass_block-block491 position3)

	(at-z grass_block-block491 position20)

	(block-present grass_block-block491)
	(at-x grass_block-block492 position-8)

	(at-y grass_block-block492 position3)

	(at-z grass_block-block492 position-20)

	(block-present grass_block-block492)
	(at-x grass_block-block493 position-8)

	(at-y grass_block-block493 position3)

	(at-z grass_block-block493 position-19)

	(block-present grass_block-block493)
	(at-x grass_block-block494 position-8)

	(at-y grass_block-block494 position3)

	(at-z grass_block-block494 position-18)

	(block-present grass_block-block494)
	(at-x grass_block-block495 position-8)

	(at-y grass_block-block495 position3)

	(at-z grass_block-block495 position-17)

	(block-present grass_block-block495)
	(at-x grass_block-block496 position-8)

	(at-y grass_block-block496 position3)

	(at-z grass_block-block496 position-16)

	(block-present grass_block-block496)
	(at-x grass_block-block497 position-8)

	(at-y grass_block-block497 position3)

	(at-z grass_block-block497 position-15)

	(block-present grass_block-block497)
	(at-x grass_block-block498 position-8)

	(at-y grass_block-block498 position3)

	(at-z grass_block-block498 position-14)

	(block-present grass_block-block498)
	(at-x grass_block-block499 position-8)

	(at-y grass_block-block499 position3)

	(at-z grass_block-block499 position-13)

	(block-present grass_block-block499)
	(at-x grass_block-block500 position-8)

	(at-y grass_block-block500 position3)

	(at-z grass_block-block500 position-12)

	(block-present grass_block-block500)
	(at-x grass_block-block501 position-8)

	(at-y grass_block-block501 position3)

	(at-z grass_block-block501 position-11)

	(block-present grass_block-block501)
	(at-x grass_block-block502 position-8)

	(at-y grass_block-block502 position3)

	(at-z grass_block-block502 position-10)

	(block-present grass_block-block502)
	(at-x grass_block-block503 position-8)

	(at-y grass_block-block503 position3)

	(at-z grass_block-block503 position-9)

	(block-present grass_block-block503)
	(at-x grass_block-block504 position-8)

	(at-y grass_block-block504 position3)

	(at-z grass_block-block504 position-8)

	(block-present grass_block-block504)
	(at-x grass_block-block505 position-8)

	(at-y grass_block-block505 position3)

	(at-z grass_block-block505 position-7)

	(block-present grass_block-block505)
	(at-x grass_block-block506 position-8)

	(at-y grass_block-block506 position3)

	(at-z grass_block-block506 position-6)

	(block-present grass_block-block506)
	(at-x grass_block-block507 position-8)

	(at-y grass_block-block507 position3)

	(at-z grass_block-block507 position-5)

	(block-present grass_block-block507)
	(at-x grass_block-block508 position-8)

	(at-y grass_block-block508 position3)

	(at-z grass_block-block508 position-4)

	(block-present grass_block-block508)
	(at-x grass_block-block509 position-8)

	(at-y grass_block-block509 position3)

	(at-z grass_block-block509 position-3)

	(block-present grass_block-block509)
	(at-x grass_block-block510 position-8)

	(at-y grass_block-block510 position3)

	(at-z grass_block-block510 position-2)

	(block-present grass_block-block510)
	(at-x grass_block-block511 position-8)

	(at-y grass_block-block511 position3)

	(at-z grass_block-block511 position-1)

	(block-present grass_block-block511)
	(at-x grass_block-block512 position-8)

	(at-y grass_block-block512 position3)

	(at-z grass_block-block512 position0)

	(block-present grass_block-block512)
	(at-x grass_block-block513 position-8)

	(at-y grass_block-block513 position3)

	(at-z grass_block-block513 position1)

	(block-present grass_block-block513)
	(at-x grass_block-block514 position-8)

	(at-y grass_block-block514 position3)

	(at-z grass_block-block514 position2)

	(block-present grass_block-block514)
	(at-x grass_block-block515 position-8)

	(at-y grass_block-block515 position3)

	(at-z grass_block-block515 position3)

	(block-present grass_block-block515)
	(at-x grass_block-block516 position-8)

	(at-y grass_block-block516 position3)

	(at-z grass_block-block516 position4)

	(block-present grass_block-block516)
	(at-x grass_block-block517 position-8)

	(at-y grass_block-block517 position3)

	(at-z grass_block-block517 position5)

	(block-present grass_block-block517)
	(at-x grass_block-block518 position-8)

	(at-y grass_block-block518 position3)

	(at-z grass_block-block518 position6)

	(block-present grass_block-block518)
	(at-x grass_block-block519 position-8)

	(at-y grass_block-block519 position3)

	(at-z grass_block-block519 position7)

	(block-present grass_block-block519)
	(at-x grass_block-block520 position-8)

	(at-y grass_block-block520 position3)

	(at-z grass_block-block520 position8)

	(block-present grass_block-block520)
	(at-x grass_block-block521 position-8)

	(at-y grass_block-block521 position3)

	(at-z grass_block-block521 position9)

	(block-present grass_block-block521)
	(at-x grass_block-block522 position-8)

	(at-y grass_block-block522 position3)

	(at-z grass_block-block522 position10)

	(block-present grass_block-block522)
	(at-x grass_block-block523 position-8)

	(at-y grass_block-block523 position3)

	(at-z grass_block-block523 position11)

	(block-present grass_block-block523)
	(at-x grass_block-block524 position-8)

	(at-y grass_block-block524 position3)

	(at-z grass_block-block524 position12)

	(block-present grass_block-block524)
	(at-x grass_block-block525 position-8)

	(at-y grass_block-block525 position3)

	(at-z grass_block-block525 position13)

	(block-present grass_block-block525)
	(at-x grass_block-block526 position-8)

	(at-y grass_block-block526 position3)

	(at-z grass_block-block526 position14)

	(block-present grass_block-block526)
	(at-x grass_block-block527 position-8)

	(at-y grass_block-block527 position3)

	(at-z grass_block-block527 position15)

	(block-present grass_block-block527)
	(at-x grass_block-block528 position-8)

	(at-y grass_block-block528 position3)

	(at-z grass_block-block528 position16)

	(block-present grass_block-block528)
	(at-x grass_block-block529 position-8)

	(at-y grass_block-block529 position3)

	(at-z grass_block-block529 position17)

	(block-present grass_block-block529)
	(at-x grass_block-block530 position-8)

	(at-y grass_block-block530 position3)

	(at-z grass_block-block530 position18)

	(block-present grass_block-block530)
	(at-x grass_block-block531 position-8)

	(at-y grass_block-block531 position3)

	(at-z grass_block-block531 position19)

	(block-present grass_block-block531)
	(at-x grass_block-block532 position-8)

	(at-y grass_block-block532 position3)

	(at-z grass_block-block532 position20)

	(block-present grass_block-block532)
	(at-x grass_block-block533 position-7)

	(at-y grass_block-block533 position3)

	(at-z grass_block-block533 position-20)

	(block-present grass_block-block533)
	(at-x grass_block-block534 position-7)

	(at-y grass_block-block534 position3)

	(at-z grass_block-block534 position-19)

	(block-present grass_block-block534)
	(at-x grass_block-block535 position-7)

	(at-y grass_block-block535 position3)

	(at-z grass_block-block535 position-18)

	(block-present grass_block-block535)
	(at-x grass_block-block536 position-7)

	(at-y grass_block-block536 position3)

	(at-z grass_block-block536 position-17)

	(block-present grass_block-block536)
	(at-x grass_block-block537 position-7)

	(at-y grass_block-block537 position3)

	(at-z grass_block-block537 position-16)

	(block-present grass_block-block537)
	(at-x grass_block-block538 position-7)

	(at-y grass_block-block538 position3)

	(at-z grass_block-block538 position-15)

	(block-present grass_block-block538)
	(at-x grass_block-block539 position-7)

	(at-y grass_block-block539 position3)

	(at-z grass_block-block539 position-14)

	(block-present grass_block-block539)
	(at-x grass_block-block540 position-7)

	(at-y grass_block-block540 position3)

	(at-z grass_block-block540 position-13)

	(block-present grass_block-block540)
	(at-x grass_block-block541 position-7)

	(at-y grass_block-block541 position3)

	(at-z grass_block-block541 position-12)

	(block-present grass_block-block541)
	(at-x grass_block-block542 position-7)

	(at-y grass_block-block542 position3)

	(at-z grass_block-block542 position-11)

	(block-present grass_block-block542)
	(at-x grass_block-block543 position-7)

	(at-y grass_block-block543 position3)

	(at-z grass_block-block543 position-10)

	(block-present grass_block-block543)
	(at-x grass_block-block544 position-7)

	(at-y grass_block-block544 position3)

	(at-z grass_block-block544 position-9)

	(block-present grass_block-block544)
	(at-x grass_block-block545 position-7)

	(at-y grass_block-block545 position3)

	(at-z grass_block-block545 position-8)

	(block-present grass_block-block545)
	(at-x grass_block-block546 position-7)

	(at-y grass_block-block546 position3)

	(at-z grass_block-block546 position-7)

	(block-present grass_block-block546)
	(at-x grass_block-block547 position-7)

	(at-y grass_block-block547 position3)

	(at-z grass_block-block547 position-6)

	(block-present grass_block-block547)
	(at-x grass_block-block548 position-7)

	(at-y grass_block-block548 position3)

	(at-z grass_block-block548 position-5)

	(block-present grass_block-block548)
	(at-x grass_block-block549 position-7)

	(at-y grass_block-block549 position3)

	(at-z grass_block-block549 position-4)

	(block-present grass_block-block549)
	(at-x grass_block-block550 position-7)

	(at-y grass_block-block550 position3)

	(at-z grass_block-block550 position-3)

	(block-present grass_block-block550)
	(at-x grass_block-block551 position-7)

	(at-y grass_block-block551 position3)

	(at-z grass_block-block551 position-2)

	(block-present grass_block-block551)
	(at-x grass_block-block552 position-7)

	(at-y grass_block-block552 position3)

	(at-z grass_block-block552 position-1)

	(block-present grass_block-block552)
	(at-x grass_block-block553 position-7)

	(at-y grass_block-block553 position3)

	(at-z grass_block-block553 position0)

	(block-present grass_block-block553)
	(at-x grass_block-block554 position-7)

	(at-y grass_block-block554 position3)

	(at-z grass_block-block554 position1)

	(block-present grass_block-block554)
	(at-x grass_block-block555 position-7)

	(at-y grass_block-block555 position3)

	(at-z grass_block-block555 position2)

	(block-present grass_block-block555)
	(at-x grass_block-block556 position-7)

	(at-y grass_block-block556 position3)

	(at-z grass_block-block556 position3)

	(block-present grass_block-block556)
	(at-x grass_block-block557 position-7)

	(at-y grass_block-block557 position3)

	(at-z grass_block-block557 position4)

	(block-present grass_block-block557)
	(at-x grass_block-block558 position-7)

	(at-y grass_block-block558 position3)

	(at-z grass_block-block558 position5)

	(block-present grass_block-block558)
	(at-x grass_block-block559 position-7)

	(at-y grass_block-block559 position3)

	(at-z grass_block-block559 position6)

	(block-present grass_block-block559)
	(at-x grass_block-block560 position-7)

	(at-y grass_block-block560 position3)

	(at-z grass_block-block560 position7)

	(block-present grass_block-block560)
	(at-x grass_block-block561 position-7)

	(at-y grass_block-block561 position3)

	(at-z grass_block-block561 position8)

	(block-present grass_block-block561)
	(at-x grass_block-block562 position-7)

	(at-y grass_block-block562 position3)

	(at-z grass_block-block562 position9)

	(block-present grass_block-block562)
	(at-x grass_block-block563 position-7)

	(at-y grass_block-block563 position3)

	(at-z grass_block-block563 position10)

	(block-present grass_block-block563)
	(at-x grass_block-block564 position-7)

	(at-y grass_block-block564 position3)

	(at-z grass_block-block564 position11)

	(block-present grass_block-block564)
	(at-x grass_block-block565 position-7)

	(at-y grass_block-block565 position3)

	(at-z grass_block-block565 position12)

	(block-present grass_block-block565)
	(at-x grass_block-block566 position-7)

	(at-y grass_block-block566 position3)

	(at-z grass_block-block566 position13)

	(block-present grass_block-block566)
	(at-x grass_block-block567 position-7)

	(at-y grass_block-block567 position3)

	(at-z grass_block-block567 position14)

	(block-present grass_block-block567)
	(at-x grass_block-block568 position-7)

	(at-y grass_block-block568 position3)

	(at-z grass_block-block568 position15)

	(block-present grass_block-block568)
	(at-x grass_block-block569 position-7)

	(at-y grass_block-block569 position3)

	(at-z grass_block-block569 position16)

	(block-present grass_block-block569)
	(at-x grass_block-block570 position-7)

	(at-y grass_block-block570 position3)

	(at-z grass_block-block570 position17)

	(block-present grass_block-block570)
	(at-x grass_block-block571 position-7)

	(at-y grass_block-block571 position3)

	(at-z grass_block-block571 position18)

	(block-present grass_block-block571)
	(at-x grass_block-block572 position-7)

	(at-y grass_block-block572 position3)

	(at-z grass_block-block572 position19)

	(block-present grass_block-block572)
	(at-x grass_block-block573 position-7)

	(at-y grass_block-block573 position3)

	(at-z grass_block-block573 position20)

	(block-present grass_block-block573)
	(at-x grass_block-block574 position-6)

	(at-y grass_block-block574 position3)

	(at-z grass_block-block574 position-20)

	(block-present grass_block-block574)
	(at-x grass_block-block575 position-6)

	(at-y grass_block-block575 position3)

	(at-z grass_block-block575 position-19)

	(block-present grass_block-block575)
	(at-x grass_block-block576 position-6)

	(at-y grass_block-block576 position3)

	(at-z grass_block-block576 position-18)

	(block-present grass_block-block576)
	(at-x grass_block-block577 position-6)

	(at-y grass_block-block577 position3)

	(at-z grass_block-block577 position-17)

	(block-present grass_block-block577)
	(at-x grass_block-block578 position-6)

	(at-y grass_block-block578 position3)

	(at-z grass_block-block578 position-16)

	(block-present grass_block-block578)
	(at-x grass_block-block579 position-6)

	(at-y grass_block-block579 position3)

	(at-z grass_block-block579 position-15)

	(block-present grass_block-block579)
	(at-x grass_block-block580 position-6)

	(at-y grass_block-block580 position3)

	(at-z grass_block-block580 position-14)

	(block-present grass_block-block580)
	(at-x grass_block-block581 position-6)

	(at-y grass_block-block581 position3)

	(at-z grass_block-block581 position-13)

	(block-present grass_block-block581)
	(at-x grass_block-block582 position-6)

	(at-y grass_block-block582 position3)

	(at-z grass_block-block582 position-12)

	(block-present grass_block-block582)
	(at-x grass_block-block583 position-6)

	(at-y grass_block-block583 position3)

	(at-z grass_block-block583 position-11)

	(block-present grass_block-block583)
	(at-x grass_block-block584 position-6)

	(at-y grass_block-block584 position3)

	(at-z grass_block-block584 position-10)

	(block-present grass_block-block584)
	(at-x grass_block-block585 position-6)

	(at-y grass_block-block585 position3)

	(at-z grass_block-block585 position-9)

	(block-present grass_block-block585)
	(at-x grass_block-block586 position-6)

	(at-y grass_block-block586 position3)

	(at-z grass_block-block586 position-8)

	(block-present grass_block-block586)
	(at-x grass_block-block587 position-6)

	(at-y grass_block-block587 position3)

	(at-z grass_block-block587 position-7)

	(block-present grass_block-block587)
	(at-x grass_block-block588 position-6)

	(at-y grass_block-block588 position3)

	(at-z grass_block-block588 position-6)

	(block-present grass_block-block588)
	(at-x grass_block-block589 position-6)

	(at-y grass_block-block589 position3)

	(at-z grass_block-block589 position-5)

	(block-present grass_block-block589)
	(at-x grass_block-block590 position-6)

	(at-y grass_block-block590 position3)

	(at-z grass_block-block590 position-4)

	(block-present grass_block-block590)
	(at-x grass_block-block591 position-6)

	(at-y grass_block-block591 position3)

	(at-z grass_block-block591 position-3)

	(block-present grass_block-block591)
	(at-x grass_block-block592 position-6)

	(at-y grass_block-block592 position3)

	(at-z grass_block-block592 position-2)

	(block-present grass_block-block592)
	(at-x grass_block-block593 position-6)

	(at-y grass_block-block593 position3)

	(at-z grass_block-block593 position-1)

	(block-present grass_block-block593)
	(at-x grass_block-block594 position-6)

	(at-y grass_block-block594 position3)

	(at-z grass_block-block594 position0)

	(block-present grass_block-block594)
	(at-x grass_block-block595 position-6)

	(at-y grass_block-block595 position3)

	(at-z grass_block-block595 position1)

	(block-present grass_block-block595)
	(at-x grass_block-block596 position-6)

	(at-y grass_block-block596 position3)

	(at-z grass_block-block596 position2)

	(block-present grass_block-block596)
	(at-x grass_block-block597 position-6)

	(at-y grass_block-block597 position3)

	(at-z grass_block-block597 position3)

	(block-present grass_block-block597)
	(at-x grass_block-block598 position-6)

	(at-y grass_block-block598 position3)

	(at-z grass_block-block598 position4)

	(block-present grass_block-block598)
	(at-x grass_block-block599 position-6)

	(at-y grass_block-block599 position3)

	(at-z grass_block-block599 position5)

	(block-present grass_block-block599)
	(at-x grass_block-block600 position-6)

	(at-y grass_block-block600 position3)

	(at-z grass_block-block600 position6)

	(block-present grass_block-block600)
	(at-x grass_block-block601 position-6)

	(at-y grass_block-block601 position3)

	(at-z grass_block-block601 position7)

	(block-present grass_block-block601)
	(at-x grass_block-block602 position-6)

	(at-y grass_block-block602 position3)

	(at-z grass_block-block602 position8)

	(block-present grass_block-block602)
	(at-x grass_block-block603 position-6)

	(at-y grass_block-block603 position3)

	(at-z grass_block-block603 position9)

	(block-present grass_block-block603)
	(at-x grass_block-block604 position-6)

	(at-y grass_block-block604 position3)

	(at-z grass_block-block604 position10)

	(block-present grass_block-block604)
	(at-x grass_block-block605 position-6)

	(at-y grass_block-block605 position3)

	(at-z grass_block-block605 position11)

	(block-present grass_block-block605)
	(at-x grass_block-block606 position-6)

	(at-y grass_block-block606 position3)

	(at-z grass_block-block606 position12)

	(block-present grass_block-block606)
	(at-x grass_block-block607 position-6)

	(at-y grass_block-block607 position3)

	(at-z grass_block-block607 position13)

	(block-present grass_block-block607)
	(at-x grass_block-block608 position-6)

	(at-y grass_block-block608 position3)

	(at-z grass_block-block608 position14)

	(block-present grass_block-block608)
	(at-x grass_block-block609 position-6)

	(at-y grass_block-block609 position3)

	(at-z grass_block-block609 position15)

	(block-present grass_block-block609)
	(at-x grass_block-block610 position-6)

	(at-y grass_block-block610 position3)

	(at-z grass_block-block610 position16)

	(block-present grass_block-block610)
	(at-x grass_block-block611 position-6)

	(at-y grass_block-block611 position3)

	(at-z grass_block-block611 position17)

	(block-present grass_block-block611)
	(at-x grass_block-block612 position-6)

	(at-y grass_block-block612 position3)

	(at-z grass_block-block612 position18)

	(block-present grass_block-block612)
	(at-x grass_block-block613 position-6)

	(at-y grass_block-block613 position3)

	(at-z grass_block-block613 position19)

	(block-present grass_block-block613)
	(at-x grass_block-block614 position-6)

	(at-y grass_block-block614 position3)

	(at-z grass_block-block614 position20)

	(block-present grass_block-block614)
	(at-x grass_block-block615 position-5)

	(at-y grass_block-block615 position3)

	(at-z grass_block-block615 position-20)

	(block-present grass_block-block615)
	(at-x grass_block-block616 position-5)

	(at-y grass_block-block616 position3)

	(at-z grass_block-block616 position-19)

	(block-present grass_block-block616)
	(at-x grass_block-block617 position-5)

	(at-y grass_block-block617 position3)

	(at-z grass_block-block617 position-18)

	(block-present grass_block-block617)
	(at-x grass_block-block618 position-5)

	(at-y grass_block-block618 position3)

	(at-z grass_block-block618 position-17)

	(block-present grass_block-block618)
	(at-x grass_block-block619 position-5)

	(at-y grass_block-block619 position3)

	(at-z grass_block-block619 position-16)

	(block-present grass_block-block619)
	(at-x grass_block-block620 position-5)

	(at-y grass_block-block620 position3)

	(at-z grass_block-block620 position-15)

	(block-present grass_block-block620)
	(at-x grass_block-block621 position-5)

	(at-y grass_block-block621 position3)

	(at-z grass_block-block621 position-14)

	(block-present grass_block-block621)
	(at-x grass_block-block622 position-5)

	(at-y grass_block-block622 position3)

	(at-z grass_block-block622 position-13)

	(block-present grass_block-block622)
	(at-x grass_block-block623 position-5)

	(at-y grass_block-block623 position3)

	(at-z grass_block-block623 position-12)

	(block-present grass_block-block623)
	(at-x grass_block-block624 position-5)

	(at-y grass_block-block624 position3)

	(at-z grass_block-block624 position-11)

	(block-present grass_block-block624)
	(at-x grass_block-block625 position-5)

	(at-y grass_block-block625 position3)

	(at-z grass_block-block625 position-10)

	(block-present grass_block-block625)
	(at-x grass_block-block626 position-5)

	(at-y grass_block-block626 position3)

	(at-z grass_block-block626 position-9)

	(block-present grass_block-block626)
	(at-x grass_block-block627 position-5)

	(at-y grass_block-block627 position3)

	(at-z grass_block-block627 position-8)

	(block-present grass_block-block627)
	(at-x grass_block-block628 position-5)

	(at-y grass_block-block628 position3)

	(at-z grass_block-block628 position-7)

	(block-present grass_block-block628)
	(at-x grass_block-block629 position-5)

	(at-y grass_block-block629 position3)

	(at-z grass_block-block629 position-6)

	(block-present grass_block-block629)
	(at-x grass_block-block630 position-5)

	(at-y grass_block-block630 position3)

	(at-z grass_block-block630 position-5)

	(block-present grass_block-block630)
	(at-x grass_block-block631 position-5)

	(at-y grass_block-block631 position3)

	(at-z grass_block-block631 position-4)

	(block-present grass_block-block631)
	(at-x grass_block-block632 position-5)

	(at-y grass_block-block632 position3)

	(at-z grass_block-block632 position-3)

	(block-present grass_block-block632)
	(at-x grass_block-block633 position-5)

	(at-y grass_block-block633 position3)

	(at-z grass_block-block633 position-2)

	(block-present grass_block-block633)
	(at-x grass_block-block634 position-5)

	(at-y grass_block-block634 position3)

	(at-z grass_block-block634 position-1)

	(block-present grass_block-block634)
	(at-x grass_block-block635 position-5)

	(at-y grass_block-block635 position3)

	(at-z grass_block-block635 position0)

	(block-present grass_block-block635)
	(at-x grass_block-block636 position-5)

	(at-y grass_block-block636 position3)

	(at-z grass_block-block636 position1)

	(block-present grass_block-block636)
	(at-x grass_block-block637 position-5)

	(at-y grass_block-block637 position3)

	(at-z grass_block-block637 position2)

	(block-present grass_block-block637)
	(at-x grass_block-block638 position-5)

	(at-y grass_block-block638 position3)

	(at-z grass_block-block638 position3)

	(block-present grass_block-block638)
	(at-x grass_block-block639 position-5)

	(at-y grass_block-block639 position3)

	(at-z grass_block-block639 position4)

	(block-present grass_block-block639)
	(at-x grass_block-block640 position-5)

	(at-y grass_block-block640 position3)

	(at-z grass_block-block640 position5)

	(block-present grass_block-block640)
	(at-x grass_block-block641 position-5)

	(at-y grass_block-block641 position3)

	(at-z grass_block-block641 position6)

	(block-present grass_block-block641)
	(at-x grass_block-block642 position-5)

	(at-y grass_block-block642 position3)

	(at-z grass_block-block642 position7)

	(block-present grass_block-block642)
	(at-x grass_block-block643 position-5)

	(at-y grass_block-block643 position3)

	(at-z grass_block-block643 position8)

	(block-present grass_block-block643)
	(at-x grass_block-block644 position-5)

	(at-y grass_block-block644 position3)

	(at-z grass_block-block644 position9)

	(block-present grass_block-block644)
	(at-x grass_block-block645 position-5)

	(at-y grass_block-block645 position3)

	(at-z grass_block-block645 position10)

	(block-present grass_block-block645)
	(at-x grass_block-block646 position-5)

	(at-y grass_block-block646 position3)

	(at-z grass_block-block646 position11)

	(block-present grass_block-block646)
	(at-x grass_block-block647 position-5)

	(at-y grass_block-block647 position3)

	(at-z grass_block-block647 position12)

	(block-present grass_block-block647)
	(at-x grass_block-block648 position-5)

	(at-y grass_block-block648 position3)

	(at-z grass_block-block648 position13)

	(block-present grass_block-block648)
	(at-x grass_block-block649 position-5)

	(at-y grass_block-block649 position3)

	(at-z grass_block-block649 position14)

	(block-present grass_block-block649)
	(at-x grass_block-block650 position-5)

	(at-y grass_block-block650 position3)

	(at-z grass_block-block650 position15)

	(block-present grass_block-block650)
	(at-x grass_block-block651 position-5)

	(at-y grass_block-block651 position3)

	(at-z grass_block-block651 position16)

	(block-present grass_block-block651)
	(at-x grass_block-block652 position-5)

	(at-y grass_block-block652 position3)

	(at-z grass_block-block652 position17)

	(block-present grass_block-block652)
	(at-x grass_block-block653 position-5)

	(at-y grass_block-block653 position3)

	(at-z grass_block-block653 position18)

	(block-present grass_block-block653)
	(at-x grass_block-block654 position-5)

	(at-y grass_block-block654 position3)

	(at-z grass_block-block654 position19)

	(block-present grass_block-block654)
	(at-x grass_block-block655 position-5)

	(at-y grass_block-block655 position3)

	(at-z grass_block-block655 position20)

	(block-present grass_block-block655)
	(at-x grass_block-block656 position-4)

	(at-y grass_block-block656 position3)

	(at-z grass_block-block656 position-20)

	(block-present grass_block-block656)
	(at-x grass_block-block657 position-4)

	(at-y grass_block-block657 position3)

	(at-z grass_block-block657 position-19)

	(block-present grass_block-block657)
	(at-x grass_block-block658 position-4)

	(at-y grass_block-block658 position3)

	(at-z grass_block-block658 position-18)

	(block-present grass_block-block658)
	(at-x grass_block-block659 position-4)

	(at-y grass_block-block659 position3)

	(at-z grass_block-block659 position-17)

	(block-present grass_block-block659)
	(at-x grass_block-block660 position-4)

	(at-y grass_block-block660 position3)

	(at-z grass_block-block660 position-16)

	(block-present grass_block-block660)
	(at-x grass_block-block661 position-4)

	(at-y grass_block-block661 position3)

	(at-z grass_block-block661 position-15)

	(block-present grass_block-block661)
	(at-x grass_block-block662 position-4)

	(at-y grass_block-block662 position3)

	(at-z grass_block-block662 position-14)

	(block-present grass_block-block662)
	(at-x grass_block-block663 position-4)

	(at-y grass_block-block663 position3)

	(at-z grass_block-block663 position-13)

	(block-present grass_block-block663)
	(at-x grass_block-block664 position-4)

	(at-y grass_block-block664 position3)

	(at-z grass_block-block664 position-12)

	(block-present grass_block-block664)
	(at-x grass_block-block665 position-4)

	(at-y grass_block-block665 position3)

	(at-z grass_block-block665 position-11)

	(block-present grass_block-block665)
	(at-x grass_block-block666 position-4)

	(at-y grass_block-block666 position3)

	(at-z grass_block-block666 position-10)

	(block-present grass_block-block666)
	(at-x grass_block-block667 position-4)

	(at-y grass_block-block667 position3)

	(at-z grass_block-block667 position-9)

	(block-present grass_block-block667)
	(at-x grass_block-block668 position-4)

	(at-y grass_block-block668 position3)

	(at-z grass_block-block668 position-8)

	(block-present grass_block-block668)
	(at-x grass_block-block669 position-4)

	(at-y grass_block-block669 position3)

	(at-z grass_block-block669 position-7)

	(block-present grass_block-block669)
	(at-x grass_block-block670 position-4)

	(at-y grass_block-block670 position3)

	(at-z grass_block-block670 position-6)

	(block-present grass_block-block670)
	(at-x grass_block-block671 position-4)

	(at-y grass_block-block671 position3)

	(at-z grass_block-block671 position-5)

	(block-present grass_block-block671)
	(at-x grass_block-block672 position-4)

	(at-y grass_block-block672 position3)

	(at-z grass_block-block672 position-4)

	(block-present grass_block-block672)
	(at-x grass_block-block673 position-4)

	(at-y grass_block-block673 position3)

	(at-z grass_block-block673 position-3)

	(block-present grass_block-block673)
	(at-x grass_block-block674 position-4)

	(at-y grass_block-block674 position3)

	(at-z grass_block-block674 position-2)

	(block-present grass_block-block674)
	(at-x grass_block-block675 position-4)

	(at-y grass_block-block675 position3)

	(at-z grass_block-block675 position-1)

	(block-present grass_block-block675)
	(at-x grass_block-block676 position-4)

	(at-y grass_block-block676 position3)

	(at-z grass_block-block676 position0)

	(block-present grass_block-block676)
	(at-x grass_block-block677 position-4)

	(at-y grass_block-block677 position3)

	(at-z grass_block-block677 position1)

	(block-present grass_block-block677)
	(at-x grass_block-block678 position-4)

	(at-y grass_block-block678 position3)

	(at-z grass_block-block678 position2)

	(block-present grass_block-block678)
	(at-x grass_block-block679 position-4)

	(at-y grass_block-block679 position3)

	(at-z grass_block-block679 position3)

	(block-present grass_block-block679)
	(at-x grass_block-block680 position-4)

	(at-y grass_block-block680 position3)

	(at-z grass_block-block680 position4)

	(block-present grass_block-block680)
	(at-x grass_block-block681 position-4)

	(at-y grass_block-block681 position3)

	(at-z grass_block-block681 position5)

	(block-present grass_block-block681)
	(at-x grass_block-block682 position-4)

	(at-y grass_block-block682 position3)

	(at-z grass_block-block682 position6)

	(block-present grass_block-block682)
	(at-x grass_block-block683 position-4)

	(at-y grass_block-block683 position3)

	(at-z grass_block-block683 position7)

	(block-present grass_block-block683)
	(at-x grass_block-block684 position-4)

	(at-y grass_block-block684 position3)

	(at-z grass_block-block684 position8)

	(block-present grass_block-block684)
	(at-x grass_block-block685 position-4)

	(at-y grass_block-block685 position3)

	(at-z grass_block-block685 position9)

	(block-present grass_block-block685)
	(at-x grass_block-block686 position-4)

	(at-y grass_block-block686 position3)

	(at-z grass_block-block686 position10)

	(block-present grass_block-block686)
	(at-x grass_block-block687 position-4)

	(at-y grass_block-block687 position3)

	(at-z grass_block-block687 position11)

	(block-present grass_block-block687)
	(at-x grass_block-block688 position-4)

	(at-y grass_block-block688 position3)

	(at-z grass_block-block688 position12)

	(block-present grass_block-block688)
	(at-x grass_block-block689 position-4)

	(at-y grass_block-block689 position3)

	(at-z grass_block-block689 position13)

	(block-present grass_block-block689)
	(at-x grass_block-block690 position-4)

	(at-y grass_block-block690 position3)

	(at-z grass_block-block690 position14)

	(block-present grass_block-block690)
	(at-x grass_block-block691 position-4)

	(at-y grass_block-block691 position3)

	(at-z grass_block-block691 position15)

	(block-present grass_block-block691)
	(at-x grass_block-block692 position-4)

	(at-y grass_block-block692 position3)

	(at-z grass_block-block692 position16)

	(block-present grass_block-block692)
	(at-x grass_block-block693 position-4)

	(at-y grass_block-block693 position3)

	(at-z grass_block-block693 position17)

	(block-present grass_block-block693)
	(at-x grass_block-block694 position-4)

	(at-y grass_block-block694 position3)

	(at-z grass_block-block694 position18)

	(block-present grass_block-block694)
	(at-x grass_block-block695 position-4)

	(at-y grass_block-block695 position3)

	(at-z grass_block-block695 position19)

	(block-present grass_block-block695)
	(at-x grass_block-block696 position-4)

	(at-y grass_block-block696 position3)

	(at-z grass_block-block696 position20)

	(block-present grass_block-block696)
	(at-x grass_block-block697 position-3)

	(at-y grass_block-block697 position3)

	(at-z grass_block-block697 position-20)

	(block-present grass_block-block697)
	(at-x grass_block-block698 position-3)

	(at-y grass_block-block698 position3)

	(at-z grass_block-block698 position-19)

	(block-present grass_block-block698)
	(at-x grass_block-block699 position-3)

	(at-y grass_block-block699 position3)

	(at-z grass_block-block699 position-18)

	(block-present grass_block-block699)
	(at-x grass_block-block700 position-3)

	(at-y grass_block-block700 position3)

	(at-z grass_block-block700 position-17)

	(block-present grass_block-block700)
	(at-x grass_block-block701 position-3)

	(at-y grass_block-block701 position3)

	(at-z grass_block-block701 position-16)

	(block-present grass_block-block701)
	(at-x grass_block-block702 position-3)

	(at-y grass_block-block702 position3)

	(at-z grass_block-block702 position-15)

	(block-present grass_block-block702)
	(at-x grass_block-block703 position-3)

	(at-y grass_block-block703 position3)

	(at-z grass_block-block703 position-14)

	(block-present grass_block-block703)
	(at-x grass_block-block704 position-3)

	(at-y grass_block-block704 position3)

	(at-z grass_block-block704 position-13)

	(block-present grass_block-block704)
	(at-x grass_block-block705 position-3)

	(at-y grass_block-block705 position3)

	(at-z grass_block-block705 position-12)

	(block-present grass_block-block705)
	(at-x grass_block-block706 position-3)

	(at-y grass_block-block706 position3)

	(at-z grass_block-block706 position-11)

	(block-present grass_block-block706)
	(at-x grass_block-block707 position-3)

	(at-y grass_block-block707 position3)

	(at-z grass_block-block707 position-10)

	(block-present grass_block-block707)
	(at-x grass_block-block708 position-3)

	(at-y grass_block-block708 position3)

	(at-z grass_block-block708 position-9)

	(block-present grass_block-block708)
	(at-x grass_block-block709 position-3)

	(at-y grass_block-block709 position3)

	(at-z grass_block-block709 position-8)

	(block-present grass_block-block709)
	(at-x grass_block-block710 position-3)

	(at-y grass_block-block710 position3)

	(at-z grass_block-block710 position-7)

	(block-present grass_block-block710)
	(at-x grass_block-block711 position-3)

	(at-y grass_block-block711 position3)

	(at-z grass_block-block711 position-6)

	(block-present grass_block-block711)
	(at-x grass_block-block712 position-3)

	(at-y grass_block-block712 position3)

	(at-z grass_block-block712 position-5)

	(block-present grass_block-block712)
	(at-x grass_block-block713 position-3)

	(at-y grass_block-block713 position3)

	(at-z grass_block-block713 position-4)

	(block-present grass_block-block713)
	(at-x grass_block-block714 position-3)

	(at-y grass_block-block714 position3)

	(at-z grass_block-block714 position-3)

	(block-present grass_block-block714)
	(at-x grass_block-block715 position-3)

	(at-y grass_block-block715 position3)

	(at-z grass_block-block715 position-2)

	(block-present grass_block-block715)
	(at-x grass_block-block716 position-3)

	(at-y grass_block-block716 position3)

	(at-z grass_block-block716 position-1)

	(block-present grass_block-block716)
	(at-x grass_block-block717 position-3)

	(at-y grass_block-block717 position3)

	(at-z grass_block-block717 position0)

	(block-present grass_block-block717)
	(at-x grass_block-block718 position-3)

	(at-y grass_block-block718 position3)

	(at-z grass_block-block718 position1)

	(block-present grass_block-block718)
	(at-x grass_block-block719 position-3)

	(at-y grass_block-block719 position3)

	(at-z grass_block-block719 position2)

	(block-present grass_block-block719)
	(at-x grass_block-block720 position-3)

	(at-y grass_block-block720 position3)

	(at-z grass_block-block720 position3)

	(block-present grass_block-block720)
	(at-x grass_block-block721 position-3)

	(at-y grass_block-block721 position3)

	(at-z grass_block-block721 position4)

	(block-present grass_block-block721)
	(at-x grass_block-block722 position-3)

	(at-y grass_block-block722 position3)

	(at-z grass_block-block722 position5)

	(block-present grass_block-block722)
	(at-x grass_block-block723 position-3)

	(at-y grass_block-block723 position3)

	(at-z grass_block-block723 position6)

	(block-present grass_block-block723)
	(at-x grass_block-block724 position-3)

	(at-y grass_block-block724 position3)

	(at-z grass_block-block724 position7)

	(block-present grass_block-block724)
	(at-x grass_block-block725 position-3)

	(at-y grass_block-block725 position3)

	(at-z grass_block-block725 position8)

	(block-present grass_block-block725)
	(at-x grass_block-block726 position-3)

	(at-y grass_block-block726 position3)

	(at-z grass_block-block726 position9)

	(block-present grass_block-block726)
	(at-x grass_block-block727 position-3)

	(at-y grass_block-block727 position3)

	(at-z grass_block-block727 position10)

	(block-present grass_block-block727)
	(at-x grass_block-block728 position-3)

	(at-y grass_block-block728 position3)

	(at-z grass_block-block728 position11)

	(block-present grass_block-block728)
	(at-x grass_block-block729 position-3)

	(at-y grass_block-block729 position3)

	(at-z grass_block-block729 position12)

	(block-present grass_block-block729)
	(at-x grass_block-block730 position-3)

	(at-y grass_block-block730 position3)

	(at-z grass_block-block730 position13)

	(block-present grass_block-block730)
	(at-x grass_block-block731 position-3)

	(at-y grass_block-block731 position3)

	(at-z grass_block-block731 position14)

	(block-present grass_block-block731)
	(at-x grass_block-block732 position-3)

	(at-y grass_block-block732 position3)

	(at-z grass_block-block732 position15)

	(block-present grass_block-block732)
	(at-x grass_block-block733 position-3)

	(at-y grass_block-block733 position3)

	(at-z grass_block-block733 position16)

	(block-present grass_block-block733)
	(at-x grass_block-block734 position-3)

	(at-y grass_block-block734 position3)

	(at-z grass_block-block734 position17)

	(block-present grass_block-block734)
	(at-x grass_block-block735 position-3)

	(at-y grass_block-block735 position3)

	(at-z grass_block-block735 position18)

	(block-present grass_block-block735)
	(at-x grass_block-block736 position-3)

	(at-y grass_block-block736 position3)

	(at-z grass_block-block736 position19)

	(block-present grass_block-block736)
	(at-x grass_block-block737 position-3)

	(at-y grass_block-block737 position3)

	(at-z grass_block-block737 position20)

	(block-present grass_block-block737)
	(at-x grass_block-block738 position-2)

	(at-y grass_block-block738 position3)

	(at-z grass_block-block738 position-20)

	(block-present grass_block-block738)
	(at-x grass_block-block739 position-2)

	(at-y grass_block-block739 position3)

	(at-z grass_block-block739 position-19)

	(block-present grass_block-block739)
	(at-x grass_block-block740 position-2)

	(at-y grass_block-block740 position3)

	(at-z grass_block-block740 position-18)

	(block-present grass_block-block740)
	(at-x grass_block-block741 position-2)

	(at-y grass_block-block741 position3)

	(at-z grass_block-block741 position-17)

	(block-present grass_block-block741)
	(at-x grass_block-block742 position-2)

	(at-y grass_block-block742 position3)

	(at-z grass_block-block742 position-16)

	(block-present grass_block-block742)
	(at-x grass_block-block743 position-2)

	(at-y grass_block-block743 position3)

	(at-z grass_block-block743 position-15)

	(block-present grass_block-block743)
	(at-x grass_block-block744 position-2)

	(at-y grass_block-block744 position3)

	(at-z grass_block-block744 position-14)

	(block-present grass_block-block744)
	(at-x grass_block-block745 position-2)

	(at-y grass_block-block745 position3)

	(at-z grass_block-block745 position-13)

	(block-present grass_block-block745)
	(at-x grass_block-block746 position-2)

	(at-y grass_block-block746 position3)

	(at-z grass_block-block746 position-12)

	(block-present grass_block-block746)
	(at-x grass_block-block747 position-2)

	(at-y grass_block-block747 position3)

	(at-z grass_block-block747 position-11)

	(block-present grass_block-block747)
	(at-x grass_block-block748 position-2)

	(at-y grass_block-block748 position3)

	(at-z grass_block-block748 position-10)

	(block-present grass_block-block748)
	(at-x grass_block-block749 position-2)

	(at-y grass_block-block749 position3)

	(at-z grass_block-block749 position-9)

	(block-present grass_block-block749)
	(at-x grass_block-block750 position-2)

	(at-y grass_block-block750 position3)

	(at-z grass_block-block750 position-8)

	(block-present grass_block-block750)
	(at-x grass_block-block751 position-2)

	(at-y grass_block-block751 position3)

	(at-z grass_block-block751 position-7)

	(block-present grass_block-block751)
	(at-x grass_block-block752 position-2)

	(at-y grass_block-block752 position3)

	(at-z grass_block-block752 position-6)

	(block-present grass_block-block752)
	(at-x grass_block-block753 position-2)

	(at-y grass_block-block753 position3)

	(at-z grass_block-block753 position-5)

	(block-present grass_block-block753)
	(at-x grass_block-block754 position-2)

	(at-y grass_block-block754 position3)

	(at-z grass_block-block754 position-4)

	(block-present grass_block-block754)
	(at-x grass_block-block755 position-2)

	(at-y grass_block-block755 position3)

	(at-z grass_block-block755 position-3)

	(block-present grass_block-block755)
	(at-x grass_block-block756 position-2)

	(at-y grass_block-block756 position3)

	(at-z grass_block-block756 position-2)

	(block-present grass_block-block756)
	(at-x grass_block-block757 position-2)

	(at-y grass_block-block757 position3)

	(at-z grass_block-block757 position-1)

	(block-present grass_block-block757)
	(at-x grass_block-block758 position-2)

	(at-y grass_block-block758 position3)

	(at-z grass_block-block758 position0)

	(block-present grass_block-block758)
	(at-x grass_block-block759 position-2)

	(at-y grass_block-block759 position3)

	(at-z grass_block-block759 position1)

	(block-present grass_block-block759)
	(at-x grass_block-block760 position-2)

	(at-y grass_block-block760 position3)

	(at-z grass_block-block760 position2)

	(block-present grass_block-block760)
	(at-x grass_block-block761 position-2)

	(at-y grass_block-block761 position3)

	(at-z grass_block-block761 position3)

	(block-present grass_block-block761)
	(at-x grass_block-block762 position-2)

	(at-y grass_block-block762 position3)

	(at-z grass_block-block762 position4)

	(block-present grass_block-block762)
	(at-x grass_block-block763 position-2)

	(at-y grass_block-block763 position3)

	(at-z grass_block-block763 position5)

	(block-present grass_block-block763)
	(at-x grass_block-block764 position-2)

	(at-y grass_block-block764 position3)

	(at-z grass_block-block764 position6)

	(block-present grass_block-block764)
	(at-x grass_block-block765 position-2)

	(at-y grass_block-block765 position3)

	(at-z grass_block-block765 position7)

	(block-present grass_block-block765)
	(at-x grass_block-block766 position-2)

	(at-y grass_block-block766 position3)

	(at-z grass_block-block766 position8)

	(block-present grass_block-block766)
	(at-x grass_block-block767 position-2)

	(at-y grass_block-block767 position3)

	(at-z grass_block-block767 position9)

	(block-present grass_block-block767)
	(at-x grass_block-block768 position-2)

	(at-y grass_block-block768 position3)

	(at-z grass_block-block768 position10)

	(block-present grass_block-block768)
	(at-x grass_block-block769 position-2)

	(at-y grass_block-block769 position3)

	(at-z grass_block-block769 position11)

	(block-present grass_block-block769)
	(at-x grass_block-block770 position-2)

	(at-y grass_block-block770 position3)

	(at-z grass_block-block770 position12)

	(block-present grass_block-block770)
	(at-x grass_block-block771 position-2)

	(at-y grass_block-block771 position3)

	(at-z grass_block-block771 position13)

	(block-present grass_block-block771)
	(at-x grass_block-block772 position-2)

	(at-y grass_block-block772 position3)

	(at-z grass_block-block772 position14)

	(block-present grass_block-block772)
	(at-x grass_block-block773 position-2)

	(at-y grass_block-block773 position3)

	(at-z grass_block-block773 position15)

	(block-present grass_block-block773)
	(at-x grass_block-block774 position-2)

	(at-y grass_block-block774 position3)

	(at-z grass_block-block774 position16)

	(block-present grass_block-block774)
	(at-x grass_block-block775 position-2)

	(at-y grass_block-block775 position3)

	(at-z grass_block-block775 position17)

	(block-present grass_block-block775)
	(at-x grass_block-block776 position-2)

	(at-y grass_block-block776 position3)

	(at-z grass_block-block776 position18)

	(block-present grass_block-block776)
	(at-x grass_block-block777 position-2)

	(at-y grass_block-block777 position3)

	(at-z grass_block-block777 position19)

	(block-present grass_block-block777)
	(at-x grass_block-block778 position-2)

	(at-y grass_block-block778 position3)

	(at-z grass_block-block778 position20)

	(block-present grass_block-block778)
	(at-x grass_block-block779 position-1)

	(at-y grass_block-block779 position3)

	(at-z grass_block-block779 position-20)

	(block-present grass_block-block779)
	(at-x grass_block-block780 position-1)

	(at-y grass_block-block780 position3)

	(at-z grass_block-block780 position-19)

	(block-present grass_block-block780)
	(at-x grass_block-block781 position-1)

	(at-y grass_block-block781 position3)

	(at-z grass_block-block781 position-18)

	(block-present grass_block-block781)
	(at-x grass_block-block782 position-1)

	(at-y grass_block-block782 position3)

	(at-z grass_block-block782 position-17)

	(block-present grass_block-block782)
	(at-x grass_block-block783 position-1)

	(at-y grass_block-block783 position3)

	(at-z grass_block-block783 position-16)

	(block-present grass_block-block783)
	(at-x grass_block-block784 position-1)

	(at-y grass_block-block784 position3)

	(at-z grass_block-block784 position-15)

	(block-present grass_block-block784)
	(at-x grass_block-block785 position-1)

	(at-y grass_block-block785 position3)

	(at-z grass_block-block785 position-14)

	(block-present grass_block-block785)
	(at-x grass_block-block786 position-1)

	(at-y grass_block-block786 position3)

	(at-z grass_block-block786 position-13)

	(block-present grass_block-block786)
	(at-x grass_block-block787 position-1)

	(at-y grass_block-block787 position3)

	(at-z grass_block-block787 position-12)

	(block-present grass_block-block787)
	(at-x grass_block-block788 position-1)

	(at-y grass_block-block788 position3)

	(at-z grass_block-block788 position-11)

	(block-present grass_block-block788)
	(at-x grass_block-block789 position-1)

	(at-y grass_block-block789 position3)

	(at-z grass_block-block789 position-10)

	(block-present grass_block-block789)
	(at-x grass_block-block790 position-1)

	(at-y grass_block-block790 position3)

	(at-z grass_block-block790 position-9)

	(block-present grass_block-block790)
	(at-x grass_block-block791 position-1)

	(at-y grass_block-block791 position3)

	(at-z grass_block-block791 position-8)

	(block-present grass_block-block791)
	(at-x grass_block-block792 position-1)

	(at-y grass_block-block792 position3)

	(at-z grass_block-block792 position-7)

	(block-present grass_block-block792)
	(at-x grass_block-block793 position-1)

	(at-y grass_block-block793 position3)

	(at-z grass_block-block793 position-6)

	(block-present grass_block-block793)
	(at-x grass_block-block794 position-1)

	(at-y grass_block-block794 position3)

	(at-z grass_block-block794 position-5)

	(block-present grass_block-block794)
	(at-x grass_block-block795 position-1)

	(at-y grass_block-block795 position3)

	(at-z grass_block-block795 position-4)

	(block-present grass_block-block795)
	(at-x grass_block-block796 position-1)

	(at-y grass_block-block796 position3)

	(at-z grass_block-block796 position-3)

	(block-present grass_block-block796)
	(at-x grass_block-block797 position-1)

	(at-y grass_block-block797 position3)

	(at-z grass_block-block797 position-2)

	(block-present grass_block-block797)
	(at-x grass_block-block798 position-1)

	(at-y grass_block-block798 position3)

	(at-z grass_block-block798 position-1)

	(block-present grass_block-block798)
	(at-x grass_block-block799 position-1)

	(at-y grass_block-block799 position3)

	(at-z grass_block-block799 position0)

	(block-present grass_block-block799)
	(at-x grass_block-block800 position-1)

	(at-y grass_block-block800 position3)

	(at-z grass_block-block800 position1)

	(block-present grass_block-block800)
	(at-x grass_block-block801 position-1)

	(at-y grass_block-block801 position3)

	(at-z grass_block-block801 position2)

	(block-present grass_block-block801)
	(at-x grass_block-block802 position-1)

	(at-y grass_block-block802 position3)

	(at-z grass_block-block802 position3)

	(block-present grass_block-block802)
	(at-x grass_block-block803 position-1)

	(at-y grass_block-block803 position3)

	(at-z grass_block-block803 position4)

	(block-present grass_block-block803)
	(at-x grass_block-block804 position-1)

	(at-y grass_block-block804 position3)

	(at-z grass_block-block804 position5)

	(block-present grass_block-block804)
	(at-x grass_block-block805 position-1)

	(at-y grass_block-block805 position3)

	(at-z grass_block-block805 position6)

	(block-present grass_block-block805)
	(at-x grass_block-block806 position-1)

	(at-y grass_block-block806 position3)

	(at-z grass_block-block806 position7)

	(block-present grass_block-block806)
	(at-x grass_block-block807 position-1)

	(at-y grass_block-block807 position3)

	(at-z grass_block-block807 position8)

	(block-present grass_block-block807)
	(at-x grass_block-block808 position-1)

	(at-y grass_block-block808 position3)

	(at-z grass_block-block808 position9)

	(block-present grass_block-block808)
	(at-x grass_block-block809 position-1)

	(at-y grass_block-block809 position3)

	(at-z grass_block-block809 position10)

	(block-present grass_block-block809)
	(at-x grass_block-block810 position-1)

	(at-y grass_block-block810 position3)

	(at-z grass_block-block810 position11)

	(block-present grass_block-block810)
	(at-x grass_block-block811 position-1)

	(at-y grass_block-block811 position3)

	(at-z grass_block-block811 position12)

	(block-present grass_block-block811)
	(at-x grass_block-block812 position-1)

	(at-y grass_block-block812 position3)

	(at-z grass_block-block812 position13)

	(block-present grass_block-block812)
	(at-x grass_block-block813 position-1)

	(at-y grass_block-block813 position3)

	(at-z grass_block-block813 position14)

	(block-present grass_block-block813)
	(at-x grass_block-block814 position-1)

	(at-y grass_block-block814 position3)

	(at-z grass_block-block814 position15)

	(block-present grass_block-block814)
	(at-x grass_block-block815 position-1)

	(at-y grass_block-block815 position3)

	(at-z grass_block-block815 position16)

	(block-present grass_block-block815)
	(at-x grass_block-block816 position-1)

	(at-y grass_block-block816 position3)

	(at-z grass_block-block816 position17)

	(block-present grass_block-block816)
	(at-x grass_block-block817 position-1)

	(at-y grass_block-block817 position3)

	(at-z grass_block-block817 position18)

	(block-present grass_block-block817)
	(at-x grass_block-block818 position-1)

	(at-y grass_block-block818 position3)

	(at-z grass_block-block818 position19)

	(block-present grass_block-block818)
	(at-x grass_block-block819 position-1)

	(at-y grass_block-block819 position3)

	(at-z grass_block-block819 position20)

	(block-present grass_block-block819)
	(at-x grass_block-block820 position0)

	(at-y grass_block-block820 position3)

	(at-z grass_block-block820 position-20)

	(block-present grass_block-block820)
	(at-x grass_block-block821 position0)

	(at-y grass_block-block821 position3)

	(at-z grass_block-block821 position-19)

	(block-present grass_block-block821)
	(at-x grass_block-block822 position0)

	(at-y grass_block-block822 position3)

	(at-z grass_block-block822 position-18)

	(block-present grass_block-block822)
	(at-x grass_block-block823 position0)

	(at-y grass_block-block823 position3)

	(at-z grass_block-block823 position-17)

	(block-present grass_block-block823)
	(at-x grass_block-block824 position0)

	(at-y grass_block-block824 position3)

	(at-z grass_block-block824 position-16)

	(block-present grass_block-block824)
	(at-x grass_block-block825 position0)

	(at-y grass_block-block825 position3)

	(at-z grass_block-block825 position-15)

	(block-present grass_block-block825)
	(at-x grass_block-block826 position0)

	(at-y grass_block-block826 position3)

	(at-z grass_block-block826 position-14)

	(block-present grass_block-block826)
	(at-x grass_block-block827 position0)

	(at-y grass_block-block827 position3)

	(at-z grass_block-block827 position-13)

	(block-present grass_block-block827)
	(at-x grass_block-block828 position0)

	(at-y grass_block-block828 position3)

	(at-z grass_block-block828 position-12)

	(block-present grass_block-block828)
	(at-x grass_block-block829 position0)

	(at-y grass_block-block829 position3)

	(at-z grass_block-block829 position-11)

	(block-present grass_block-block829)
	(at-x grass_block-block830 position0)

	(at-y grass_block-block830 position3)

	(at-z grass_block-block830 position-10)

	(block-present grass_block-block830)
	(at-x grass_block-block831 position0)

	(at-y grass_block-block831 position3)

	(at-z grass_block-block831 position-9)

	(block-present grass_block-block831)
	(at-x grass_block-block832 position0)

	(at-y grass_block-block832 position3)

	(at-z grass_block-block832 position-8)

	(block-present grass_block-block832)
	(at-x grass_block-block833 position0)

	(at-y grass_block-block833 position3)

	(at-z grass_block-block833 position-7)

	(block-present grass_block-block833)
	(at-x grass_block-block834 position0)

	(at-y grass_block-block834 position3)

	(at-z grass_block-block834 position-6)

	(block-present grass_block-block834)
	(at-x grass_block-block835 position0)

	(at-y grass_block-block835 position3)

	(at-z grass_block-block835 position-5)

	(block-present grass_block-block835)
	(at-x grass_block-block836 position0)

	(at-y grass_block-block836 position3)

	(at-z grass_block-block836 position-4)

	(block-present grass_block-block836)
	(at-x grass_block-block837 position0)

	(at-y grass_block-block837 position3)

	(at-z grass_block-block837 position-3)

	(block-present grass_block-block837)
	(at-x grass_block-block838 position0)

	(at-y grass_block-block838 position3)

	(at-z grass_block-block838 position-2)

	(block-present grass_block-block838)
	(at-x grass_block-block839 position0)

	(at-y grass_block-block839 position3)

	(at-z grass_block-block839 position-1)

	(block-present grass_block-block839)
	(at-x grass_block-block840 position0)

	(at-y grass_block-block840 position3)

	(at-z grass_block-block840 position0)

	(block-present grass_block-block840)
	(at-x grass_block-block841 position0)

	(at-y grass_block-block841 position3)

	(at-z grass_block-block841 position1)

	(block-present grass_block-block841)
	(at-x grass_block-block842 position0)

	(at-y grass_block-block842 position3)

	(at-z grass_block-block842 position2)

	(block-present grass_block-block842)
	(at-x grass_block-block843 position0)

	(at-y grass_block-block843 position3)

	(at-z grass_block-block843 position3)

	(block-present grass_block-block843)
	(at-x grass_block-block844 position0)

	(at-y grass_block-block844 position3)

	(at-z grass_block-block844 position4)

	(block-present grass_block-block844)
	(at-x grass_block-block845 position0)

	(at-y grass_block-block845 position3)

	(at-z grass_block-block845 position5)

	(block-present grass_block-block845)
	(at-x grass_block-block846 position0)

	(at-y grass_block-block846 position3)

	(at-z grass_block-block846 position6)

	(block-present grass_block-block846)
	(at-x grass_block-block847 position0)

	(at-y grass_block-block847 position3)

	(at-z grass_block-block847 position7)

	(block-present grass_block-block847)
	(at-x grass_block-block848 position0)

	(at-y grass_block-block848 position3)

	(at-z grass_block-block848 position8)

	(block-present grass_block-block848)
	(at-x grass_block-block849 position0)

	(at-y grass_block-block849 position3)

	(at-z grass_block-block849 position9)

	(block-present grass_block-block849)
	(at-x grass_block-block850 position0)

	(at-y grass_block-block850 position3)

	(at-z grass_block-block850 position10)

	(block-present grass_block-block850)
	(at-x grass_block-block851 position0)

	(at-y grass_block-block851 position3)

	(at-z grass_block-block851 position11)

	(block-present grass_block-block851)
	(at-x grass_block-block852 position0)

	(at-y grass_block-block852 position3)

	(at-z grass_block-block852 position12)

	(block-present grass_block-block852)
	(at-x grass_block-block853 position0)

	(at-y grass_block-block853 position3)

	(at-z grass_block-block853 position13)

	(block-present grass_block-block853)
	(at-x grass_block-block854 position0)

	(at-y grass_block-block854 position3)

	(at-z grass_block-block854 position14)

	(block-present grass_block-block854)
	(at-x grass_block-block855 position0)

	(at-y grass_block-block855 position3)

	(at-z grass_block-block855 position15)

	(block-present grass_block-block855)
	(at-x grass_block-block856 position0)

	(at-y grass_block-block856 position3)

	(at-z grass_block-block856 position16)

	(block-present grass_block-block856)
	(at-x grass_block-block857 position0)

	(at-y grass_block-block857 position3)

	(at-z grass_block-block857 position17)

	(block-present grass_block-block857)
	(at-x grass_block-block858 position0)

	(at-y grass_block-block858 position3)

	(at-z grass_block-block858 position18)

	(block-present grass_block-block858)
	(at-x grass_block-block859 position0)

	(at-y grass_block-block859 position3)

	(at-z grass_block-block859 position19)

	(block-present grass_block-block859)
	(at-x grass_block-block860 position0)

	(at-y grass_block-block860 position3)

	(at-z grass_block-block860 position20)

	(block-present grass_block-block860)
	(at-x grass_block-block861 position1)

	(at-y grass_block-block861 position3)

	(at-z grass_block-block861 position-20)

	(block-present grass_block-block861)
	(at-x grass_block-block862 position1)

	(at-y grass_block-block862 position3)

	(at-z grass_block-block862 position-19)

	(block-present grass_block-block862)
	(at-x grass_block-block863 position1)

	(at-y grass_block-block863 position3)

	(at-z grass_block-block863 position-18)

	(block-present grass_block-block863)
	(at-x grass_block-block864 position1)

	(at-y grass_block-block864 position3)

	(at-z grass_block-block864 position-17)

	(block-present grass_block-block864)
	(at-x grass_block-block865 position1)

	(at-y grass_block-block865 position3)

	(at-z grass_block-block865 position-16)

	(block-present grass_block-block865)
	(at-x grass_block-block866 position1)

	(at-y grass_block-block866 position3)

	(at-z grass_block-block866 position-15)

	(block-present grass_block-block866)
	(at-x grass_block-block867 position1)

	(at-y grass_block-block867 position3)

	(at-z grass_block-block867 position-14)

	(block-present grass_block-block867)
	(at-x grass_block-block868 position1)

	(at-y grass_block-block868 position3)

	(at-z grass_block-block868 position-13)

	(block-present grass_block-block868)
	(at-x grass_block-block869 position1)

	(at-y grass_block-block869 position3)

	(at-z grass_block-block869 position-12)

	(block-present grass_block-block869)
	(at-x grass_block-block870 position1)

	(at-y grass_block-block870 position3)

	(at-z grass_block-block870 position-11)

	(block-present grass_block-block870)
	(at-x grass_block-block871 position1)

	(at-y grass_block-block871 position3)

	(at-z grass_block-block871 position-10)

	(block-present grass_block-block871)
	(at-x grass_block-block872 position1)

	(at-y grass_block-block872 position3)

	(at-z grass_block-block872 position-9)

	(block-present grass_block-block872)
	(at-x grass_block-block873 position1)

	(at-y grass_block-block873 position3)

	(at-z grass_block-block873 position-8)

	(block-present grass_block-block873)
	(at-x grass_block-block874 position1)

	(at-y grass_block-block874 position3)

	(at-z grass_block-block874 position-7)

	(block-present grass_block-block874)
	(at-x grass_block-block875 position1)

	(at-y grass_block-block875 position3)

	(at-z grass_block-block875 position-6)

	(block-present grass_block-block875)
	(at-x grass_block-block876 position1)

	(at-y grass_block-block876 position3)

	(at-z grass_block-block876 position-5)

	(block-present grass_block-block876)
	(at-x grass_block-block877 position1)

	(at-y grass_block-block877 position3)

	(at-z grass_block-block877 position-4)

	(block-present grass_block-block877)
	(at-x grass_block-block878 position1)

	(at-y grass_block-block878 position3)

	(at-z grass_block-block878 position-3)

	(block-present grass_block-block878)
	(at-x grass_block-block879 position1)

	(at-y grass_block-block879 position3)

	(at-z grass_block-block879 position-2)

	(block-present grass_block-block879)
	(at-x grass_block-block880 position1)

	(at-y grass_block-block880 position3)

	(at-z grass_block-block880 position-1)

	(block-present grass_block-block880)
	(at-x grass_block-block881 position1)

	(at-y grass_block-block881 position3)

	(at-z grass_block-block881 position0)

	(block-present grass_block-block881)
	(at-x grass_block-block882 position1)

	(at-y grass_block-block882 position3)

	(at-z grass_block-block882 position1)

	(block-present grass_block-block882)
	(at-x grass_block-block883 position1)

	(at-y grass_block-block883 position3)

	(at-z grass_block-block883 position2)

	(block-present grass_block-block883)
	(at-x grass_block-block884 position1)

	(at-y grass_block-block884 position3)

	(at-z grass_block-block884 position3)

	(block-present grass_block-block884)
	(at-x grass_block-block885 position1)

	(at-y grass_block-block885 position3)

	(at-z grass_block-block885 position4)

	(block-present grass_block-block885)
	(at-x grass_block-block886 position1)

	(at-y grass_block-block886 position3)

	(at-z grass_block-block886 position5)

	(block-present grass_block-block886)
	(at-x grass_block-block887 position1)

	(at-y grass_block-block887 position3)

	(at-z grass_block-block887 position6)

	(block-present grass_block-block887)
	(at-x grass_block-block888 position1)

	(at-y grass_block-block888 position3)

	(at-z grass_block-block888 position7)

	(block-present grass_block-block888)
	(at-x grass_block-block889 position1)

	(at-y grass_block-block889 position3)

	(at-z grass_block-block889 position8)

	(block-present grass_block-block889)
	(at-x grass_block-block890 position1)

	(at-y grass_block-block890 position3)

	(at-z grass_block-block890 position9)

	(block-present grass_block-block890)
	(at-x grass_block-block891 position1)

	(at-y grass_block-block891 position3)

	(at-z grass_block-block891 position10)

	(block-present grass_block-block891)
	(at-x grass_block-block892 position1)

	(at-y grass_block-block892 position3)

	(at-z grass_block-block892 position11)

	(block-present grass_block-block892)
	(at-x grass_block-block893 position1)

	(at-y grass_block-block893 position3)

	(at-z grass_block-block893 position12)

	(block-present grass_block-block893)
	(at-x grass_block-block894 position1)

	(at-y grass_block-block894 position3)

	(at-z grass_block-block894 position13)

	(block-present grass_block-block894)
	(at-x grass_block-block895 position1)

	(at-y grass_block-block895 position3)

	(at-z grass_block-block895 position14)

	(block-present grass_block-block895)
	(at-x grass_block-block896 position1)

	(at-y grass_block-block896 position3)

	(at-z grass_block-block896 position15)

	(block-present grass_block-block896)
	(at-x grass_block-block897 position1)

	(at-y grass_block-block897 position3)

	(at-z grass_block-block897 position16)

	(block-present grass_block-block897)
	(at-x grass_block-block898 position1)

	(at-y grass_block-block898 position3)

	(at-z grass_block-block898 position17)

	(block-present grass_block-block898)
	(at-x grass_block-block899 position1)

	(at-y grass_block-block899 position3)

	(at-z grass_block-block899 position18)

	(block-present grass_block-block899)
	(at-x grass_block-block900 position1)

	(at-y grass_block-block900 position3)

	(at-z grass_block-block900 position19)

	(block-present grass_block-block900)
	(at-x grass_block-block901 position1)

	(at-y grass_block-block901 position3)

	(at-z grass_block-block901 position20)

	(block-present grass_block-block901)
	(at-x grass_block-block902 position2)

	(at-y grass_block-block902 position3)

	(at-z grass_block-block902 position-20)

	(block-present grass_block-block902)
	(at-x grass_block-block903 position2)

	(at-y grass_block-block903 position3)

	(at-z grass_block-block903 position-19)

	(block-present grass_block-block903)
	(at-x grass_block-block904 position2)

	(at-y grass_block-block904 position3)

	(at-z grass_block-block904 position-18)

	(block-present grass_block-block904)
	(at-x grass_block-block905 position2)

	(at-y grass_block-block905 position3)

	(at-z grass_block-block905 position-17)

	(block-present grass_block-block905)
	(at-x grass_block-block906 position2)

	(at-y grass_block-block906 position3)

	(at-z grass_block-block906 position-16)

	(block-present grass_block-block906)
	(at-x grass_block-block907 position2)

	(at-y grass_block-block907 position3)

	(at-z grass_block-block907 position-15)

	(block-present grass_block-block907)
	(at-x grass_block-block908 position2)

	(at-y grass_block-block908 position3)

	(at-z grass_block-block908 position-14)

	(block-present grass_block-block908)
	(at-x grass_block-block909 position2)

	(at-y grass_block-block909 position3)

	(at-z grass_block-block909 position-13)

	(block-present grass_block-block909)
	(at-x grass_block-block910 position2)

	(at-y grass_block-block910 position3)

	(at-z grass_block-block910 position-12)

	(block-present grass_block-block910)
	(at-x grass_block-block911 position2)

	(at-y grass_block-block911 position3)

	(at-z grass_block-block911 position-11)

	(block-present grass_block-block911)
	(at-x grass_block-block912 position2)

	(at-y grass_block-block912 position3)

	(at-z grass_block-block912 position-10)

	(block-present grass_block-block912)
	(at-x grass_block-block913 position2)

	(at-y grass_block-block913 position3)

	(at-z grass_block-block913 position-9)

	(block-present grass_block-block913)
	(at-x grass_block-block914 position2)

	(at-y grass_block-block914 position3)

	(at-z grass_block-block914 position-8)

	(block-present grass_block-block914)
	(at-x grass_block-block915 position2)

	(at-y grass_block-block915 position3)

	(at-z grass_block-block915 position-7)

	(block-present grass_block-block915)
	(at-x grass_block-block916 position2)

	(at-y grass_block-block916 position3)

	(at-z grass_block-block916 position-6)

	(block-present grass_block-block916)
	(at-x grass_block-block917 position2)

	(at-y grass_block-block917 position3)

	(at-z grass_block-block917 position-5)

	(block-present grass_block-block917)
	(at-x grass_block-block918 position2)

	(at-y grass_block-block918 position3)

	(at-z grass_block-block918 position-4)

	(block-present grass_block-block918)
	(at-x grass_block-block919 position2)

	(at-y grass_block-block919 position3)

	(at-z grass_block-block919 position-3)

	(block-present grass_block-block919)
	(at-x grass_block-block920 position2)

	(at-y grass_block-block920 position3)

	(at-z grass_block-block920 position-2)

	(block-present grass_block-block920)
	(at-x grass_block-block921 position2)

	(at-y grass_block-block921 position3)

	(at-z grass_block-block921 position-1)

	(block-present grass_block-block921)
	(at-x grass_block-block922 position2)

	(at-y grass_block-block922 position3)

	(at-z grass_block-block922 position0)

	(block-present grass_block-block922)
	(at-x grass_block-block923 position2)

	(at-y grass_block-block923 position3)

	(at-z grass_block-block923 position1)

	(block-present grass_block-block923)
	(at-x grass_block-block924 position2)

	(at-y grass_block-block924 position3)

	(at-z grass_block-block924 position2)

	(block-present grass_block-block924)
	(at-x grass_block-block925 position2)

	(at-y grass_block-block925 position3)

	(at-z grass_block-block925 position3)

	(block-present grass_block-block925)
	(at-x grass_block-block926 position2)

	(at-y grass_block-block926 position3)

	(at-z grass_block-block926 position4)

	(block-present grass_block-block926)
	(at-x grass_block-block927 position2)

	(at-y grass_block-block927 position3)

	(at-z grass_block-block927 position5)

	(block-present grass_block-block927)
	(at-x grass_block-block928 position2)

	(at-y grass_block-block928 position3)

	(at-z grass_block-block928 position6)

	(block-present grass_block-block928)
	(at-x grass_block-block929 position2)

	(at-y grass_block-block929 position3)

	(at-z grass_block-block929 position7)

	(block-present grass_block-block929)
	(at-x grass_block-block930 position2)

	(at-y grass_block-block930 position3)

	(at-z grass_block-block930 position8)

	(block-present grass_block-block930)
	(at-x grass_block-block931 position2)

	(at-y grass_block-block931 position3)

	(at-z grass_block-block931 position9)

	(block-present grass_block-block931)
	(at-x grass_block-block932 position2)

	(at-y grass_block-block932 position3)

	(at-z grass_block-block932 position10)

	(block-present grass_block-block932)
	(at-x grass_block-block933 position2)

	(at-y grass_block-block933 position3)

	(at-z grass_block-block933 position11)

	(block-present grass_block-block933)
	(at-x grass_block-block934 position2)

	(at-y grass_block-block934 position3)

	(at-z grass_block-block934 position12)

	(block-present grass_block-block934)
	(at-x grass_block-block935 position2)

	(at-y grass_block-block935 position3)

	(at-z grass_block-block935 position13)

	(block-present grass_block-block935)
	(at-x grass_block-block936 position2)

	(at-y grass_block-block936 position3)

	(at-z grass_block-block936 position14)

	(block-present grass_block-block936)
	(at-x grass_block-block937 position2)

	(at-y grass_block-block937 position3)

	(at-z grass_block-block937 position15)

	(block-present grass_block-block937)
	(at-x grass_block-block938 position2)

	(at-y grass_block-block938 position3)

	(at-z grass_block-block938 position16)

	(block-present grass_block-block938)
	(at-x grass_block-block939 position2)

	(at-y grass_block-block939 position3)

	(at-z grass_block-block939 position17)

	(block-present grass_block-block939)
	(at-x grass_block-block940 position2)

	(at-y grass_block-block940 position3)

	(at-z grass_block-block940 position18)

	(block-present grass_block-block940)
	(at-x grass_block-block941 position2)

	(at-y grass_block-block941 position3)

	(at-z grass_block-block941 position19)

	(block-present grass_block-block941)
	(at-x grass_block-block942 position2)

	(at-y grass_block-block942 position3)

	(at-z grass_block-block942 position20)

	(block-present grass_block-block942)
	(at-x grass_block-block943 position3)

	(at-y grass_block-block943 position3)

	(at-z grass_block-block943 position-20)

	(block-present grass_block-block943)
	(at-x grass_block-block944 position3)

	(at-y grass_block-block944 position3)

	(at-z grass_block-block944 position-19)

	(block-present grass_block-block944)
	(at-x grass_block-block945 position3)

	(at-y grass_block-block945 position3)

	(at-z grass_block-block945 position-18)

	(block-present grass_block-block945)
	(at-x grass_block-block946 position3)

	(at-y grass_block-block946 position3)

	(at-z grass_block-block946 position-17)

	(block-present grass_block-block946)
	(at-x grass_block-block947 position3)

	(at-y grass_block-block947 position3)

	(at-z grass_block-block947 position-16)

	(block-present grass_block-block947)
	(at-x grass_block-block948 position3)

	(at-y grass_block-block948 position3)

	(at-z grass_block-block948 position-15)

	(block-present grass_block-block948)
	(at-x grass_block-block949 position3)

	(at-y grass_block-block949 position3)

	(at-z grass_block-block949 position-14)

	(block-present grass_block-block949)
	(at-x grass_block-block950 position3)

	(at-y grass_block-block950 position3)

	(at-z grass_block-block950 position-13)

	(block-present grass_block-block950)
	(at-x grass_block-block951 position3)

	(at-y grass_block-block951 position3)

	(at-z grass_block-block951 position-12)

	(block-present grass_block-block951)
	(at-x grass_block-block952 position3)

	(at-y grass_block-block952 position3)

	(at-z grass_block-block952 position-11)

	(block-present grass_block-block952)
	(at-x grass_block-block953 position3)

	(at-y grass_block-block953 position3)

	(at-z grass_block-block953 position-10)

	(block-present grass_block-block953)
	(at-x grass_block-block954 position3)

	(at-y grass_block-block954 position3)

	(at-z grass_block-block954 position-9)

	(block-present grass_block-block954)
	(at-x grass_block-block955 position3)

	(at-y grass_block-block955 position3)

	(at-z grass_block-block955 position-8)

	(block-present grass_block-block955)
	(at-x grass_block-block956 position3)

	(at-y grass_block-block956 position3)

	(at-z grass_block-block956 position-7)

	(block-present grass_block-block956)
	(at-x grass_block-block957 position3)

	(at-y grass_block-block957 position3)

	(at-z grass_block-block957 position-6)

	(block-present grass_block-block957)
	(at-x grass_block-block958 position3)

	(at-y grass_block-block958 position3)

	(at-z grass_block-block958 position-5)

	(block-present grass_block-block958)
	(at-x grass_block-block959 position3)

	(at-y grass_block-block959 position3)

	(at-z grass_block-block959 position-4)

	(block-present grass_block-block959)
	(at-x grass_block-block960 position3)

	(at-y grass_block-block960 position3)

	(at-z grass_block-block960 position-3)

	(block-present grass_block-block960)
	(at-x grass_block-block961 position3)

	(at-y grass_block-block961 position3)

	(at-z grass_block-block961 position-2)

	(block-present grass_block-block961)
	(at-x grass_block-block962 position3)

	(at-y grass_block-block962 position3)

	(at-z grass_block-block962 position-1)

	(block-present grass_block-block962)
	(at-x grass_block-block963 position3)

	(at-y grass_block-block963 position3)

	(at-z grass_block-block963 position0)

	(block-present grass_block-block963)
	(at-x grass_block-block964 position3)

	(at-y grass_block-block964 position3)

	(at-z grass_block-block964 position1)

	(block-present grass_block-block964)
	(at-x grass_block-block965 position3)

	(at-y grass_block-block965 position3)

	(at-z grass_block-block965 position2)

	(block-present grass_block-block965)
	(at-x grass_block-block966 position3)

	(at-y grass_block-block966 position3)

	(at-z grass_block-block966 position3)

	(block-present grass_block-block966)
	(at-x grass_block-block967 position3)

	(at-y grass_block-block967 position3)

	(at-z grass_block-block967 position4)

	(block-present grass_block-block967)
	(at-x grass_block-block968 position3)

	(at-y grass_block-block968 position3)

	(at-z grass_block-block968 position5)

	(block-present grass_block-block968)
	(at-x grass_block-block969 position3)

	(at-y grass_block-block969 position3)

	(at-z grass_block-block969 position6)

	(block-present grass_block-block969)
	(at-x grass_block-block970 position3)

	(at-y grass_block-block970 position3)

	(at-z grass_block-block970 position7)

	(block-present grass_block-block970)
	(at-x grass_block-block971 position3)

	(at-y grass_block-block971 position3)

	(at-z grass_block-block971 position8)

	(block-present grass_block-block971)
	(at-x grass_block-block972 position3)

	(at-y grass_block-block972 position3)

	(at-z grass_block-block972 position9)

	(block-present grass_block-block972)
	(at-x grass_block-block973 position3)

	(at-y grass_block-block973 position3)

	(at-z grass_block-block973 position10)

	(block-present grass_block-block973)
	(at-x grass_block-block974 position3)

	(at-y grass_block-block974 position3)

	(at-z grass_block-block974 position11)

	(block-present grass_block-block974)
	(at-x grass_block-block975 position3)

	(at-y grass_block-block975 position3)

	(at-z grass_block-block975 position12)

	(block-present grass_block-block975)
	(at-x grass_block-block976 position3)

	(at-y grass_block-block976 position3)

	(at-z grass_block-block976 position13)

	(block-present grass_block-block976)
	(at-x grass_block-block977 position3)

	(at-y grass_block-block977 position3)

	(at-z grass_block-block977 position14)

	(block-present grass_block-block977)
	(at-x grass_block-block978 position3)

	(at-y grass_block-block978 position3)

	(at-z grass_block-block978 position15)

	(block-present grass_block-block978)
	(at-x grass_block-block979 position3)

	(at-y grass_block-block979 position3)

	(at-z grass_block-block979 position16)

	(block-present grass_block-block979)
	(at-x grass_block-block980 position3)

	(at-y grass_block-block980 position3)

	(at-z grass_block-block980 position17)

	(block-present grass_block-block980)
	(at-x grass_block-block981 position3)

	(at-y grass_block-block981 position3)

	(at-z grass_block-block981 position18)

	(block-present grass_block-block981)
	(at-x grass_block-block982 position3)

	(at-y grass_block-block982 position3)

	(at-z grass_block-block982 position19)

	(block-present grass_block-block982)
	(at-x grass_block-block983 position3)

	(at-y grass_block-block983 position3)

	(at-z grass_block-block983 position20)

	(block-present grass_block-block983)
	(at-x grass_block-block984 position4)

	(at-y grass_block-block984 position3)

	(at-z grass_block-block984 position-20)

	(block-present grass_block-block984)
	(at-x grass_block-block985 position4)

	(at-y grass_block-block985 position3)

	(at-z grass_block-block985 position-19)

	(block-present grass_block-block985)
	(at-x grass_block-block986 position4)

	(at-y grass_block-block986 position3)

	(at-z grass_block-block986 position-18)

	(block-present grass_block-block986)
	(at-x grass_block-block987 position4)

	(at-y grass_block-block987 position3)

	(at-z grass_block-block987 position-17)

	(block-present grass_block-block987)
	(at-x grass_block-block988 position4)

	(at-y grass_block-block988 position3)

	(at-z grass_block-block988 position-16)

	(block-present grass_block-block988)
	(at-x grass_block-block989 position4)

	(at-y grass_block-block989 position3)

	(at-z grass_block-block989 position-15)

	(block-present grass_block-block989)
	(at-x grass_block-block990 position4)

	(at-y grass_block-block990 position3)

	(at-z grass_block-block990 position-14)

	(block-present grass_block-block990)
	(at-x grass_block-block991 position4)

	(at-y grass_block-block991 position3)

	(at-z grass_block-block991 position-13)

	(block-present grass_block-block991)
	(at-x grass_block-block992 position4)

	(at-y grass_block-block992 position3)

	(at-z grass_block-block992 position-12)

	(block-present grass_block-block992)
	(at-x grass_block-block993 position4)

	(at-y grass_block-block993 position3)

	(at-z grass_block-block993 position-11)

	(block-present grass_block-block993)
	(at-x grass_block-block994 position4)

	(at-y grass_block-block994 position3)

	(at-z grass_block-block994 position-10)

	(block-present grass_block-block994)
	(at-x grass_block-block995 position4)

	(at-y grass_block-block995 position3)

	(at-z grass_block-block995 position-9)

	(block-present grass_block-block995)
	(at-x grass_block-block996 position4)

	(at-y grass_block-block996 position3)

	(at-z grass_block-block996 position-8)

	(block-present grass_block-block996)
	(at-x grass_block-block997 position4)

	(at-y grass_block-block997 position3)

	(at-z grass_block-block997 position-7)

	(block-present grass_block-block997)
	(at-x grass_block-block998 position4)

	(at-y grass_block-block998 position3)

	(at-z grass_block-block998 position-6)

	(block-present grass_block-block998)
	(at-x grass_block-block999 position4)

	(at-y grass_block-block999 position3)

	(at-z grass_block-block999 position-5)

	(block-present grass_block-block999)
	(at-x grass_block-block1000 position4)

	(at-y grass_block-block1000 position3)

	(at-z grass_block-block1000 position-4)

	(block-present grass_block-block1000)
	(at-x grass_block-block1001 position4)

	(at-y grass_block-block1001 position3)

	(at-z grass_block-block1001 position-3)

	(block-present grass_block-block1001)
	(at-x grass_block-block1002 position4)

	(at-y grass_block-block1002 position3)

	(at-z grass_block-block1002 position-2)

	(block-present grass_block-block1002)
	(at-x grass_block-block1003 position4)

	(at-y grass_block-block1003 position3)

	(at-z grass_block-block1003 position-1)

	(block-present grass_block-block1003)
	(at-x grass_block-block1004 position4)

	(at-y grass_block-block1004 position3)

	(at-z grass_block-block1004 position0)

	(block-present grass_block-block1004)
	(at-x grass_block-block1005 position4)

	(at-y grass_block-block1005 position3)

	(at-z grass_block-block1005 position1)

	(block-present grass_block-block1005)
	(at-x grass_block-block1006 position4)

	(at-y grass_block-block1006 position3)

	(at-z grass_block-block1006 position2)

	(block-present grass_block-block1006)
	(at-x grass_block-block1007 position4)

	(at-y grass_block-block1007 position3)

	(at-z grass_block-block1007 position3)

	(block-present grass_block-block1007)
	(at-x grass_block-block1008 position4)

	(at-y grass_block-block1008 position3)

	(at-z grass_block-block1008 position4)

	(block-present grass_block-block1008)
	(at-x grass_block-block1009 position4)

	(at-y grass_block-block1009 position3)

	(at-z grass_block-block1009 position5)

	(block-present grass_block-block1009)
	(at-x grass_block-block1010 position4)

	(at-y grass_block-block1010 position3)

	(at-z grass_block-block1010 position6)

	(block-present grass_block-block1010)
	(at-x grass_block-block1011 position4)

	(at-y grass_block-block1011 position3)

	(at-z grass_block-block1011 position7)

	(block-present grass_block-block1011)
	(at-x grass_block-block1012 position4)

	(at-y grass_block-block1012 position3)

	(at-z grass_block-block1012 position8)

	(block-present grass_block-block1012)
	(at-x grass_block-block1013 position4)

	(at-y grass_block-block1013 position3)

	(at-z grass_block-block1013 position9)

	(block-present grass_block-block1013)
	(at-x grass_block-block1014 position4)

	(at-y grass_block-block1014 position3)

	(at-z grass_block-block1014 position10)

	(block-present grass_block-block1014)
	(at-x grass_block-block1015 position4)

	(at-y grass_block-block1015 position3)

	(at-z grass_block-block1015 position11)

	(block-present grass_block-block1015)
	(at-x grass_block-block1016 position4)

	(at-y grass_block-block1016 position3)

	(at-z grass_block-block1016 position12)

	(block-present grass_block-block1016)
	(at-x grass_block-block1017 position4)

	(at-y grass_block-block1017 position3)

	(at-z grass_block-block1017 position13)

	(block-present grass_block-block1017)
	(at-x grass_block-block1018 position4)

	(at-y grass_block-block1018 position3)

	(at-z grass_block-block1018 position14)

	(block-present grass_block-block1018)
	(at-x grass_block-block1019 position4)

	(at-y grass_block-block1019 position3)

	(at-z grass_block-block1019 position15)

	(block-present grass_block-block1019)
	(at-x grass_block-block1020 position4)

	(at-y grass_block-block1020 position3)

	(at-z grass_block-block1020 position16)

	(block-present grass_block-block1020)
	(at-x grass_block-block1021 position4)

	(at-y grass_block-block1021 position3)

	(at-z grass_block-block1021 position17)

	(block-present grass_block-block1021)
	(at-x grass_block-block1022 position4)

	(at-y grass_block-block1022 position3)

	(at-z grass_block-block1022 position18)

	(block-present grass_block-block1022)
	(at-x grass_block-block1023 position4)

	(at-y grass_block-block1023 position3)

	(at-z grass_block-block1023 position19)

	(block-present grass_block-block1023)
	(at-x grass_block-block1024 position4)

	(at-y grass_block-block1024 position3)

	(at-z grass_block-block1024 position20)

	(block-present grass_block-block1024)
	(at-x grass_block-block1025 position5)

	(at-y grass_block-block1025 position3)

	(at-z grass_block-block1025 position-20)

	(block-present grass_block-block1025)
	(at-x grass_block-block1026 position5)

	(at-y grass_block-block1026 position3)

	(at-z grass_block-block1026 position-19)

	(block-present grass_block-block1026)
	(at-x grass_block-block1027 position5)

	(at-y grass_block-block1027 position3)

	(at-z grass_block-block1027 position-18)

	(block-present grass_block-block1027)
	(at-x grass_block-block1028 position5)

	(at-y grass_block-block1028 position3)

	(at-z grass_block-block1028 position-17)

	(block-present grass_block-block1028)
	(at-x grass_block-block1029 position5)

	(at-y grass_block-block1029 position3)

	(at-z grass_block-block1029 position-16)

	(block-present grass_block-block1029)
	(at-x grass_block-block1030 position5)

	(at-y grass_block-block1030 position3)

	(at-z grass_block-block1030 position-15)

	(block-present grass_block-block1030)
	(at-x grass_block-block1031 position5)

	(at-y grass_block-block1031 position3)

	(at-z grass_block-block1031 position-14)

	(block-present grass_block-block1031)
	(at-x grass_block-block1032 position5)

	(at-y grass_block-block1032 position3)

	(at-z grass_block-block1032 position-13)

	(block-present grass_block-block1032)
	(at-x grass_block-block1033 position5)

	(at-y grass_block-block1033 position3)

	(at-z grass_block-block1033 position-12)

	(block-present grass_block-block1033)
	(at-x grass_block-block1034 position5)

	(at-y grass_block-block1034 position3)

	(at-z grass_block-block1034 position-11)

	(block-present grass_block-block1034)
	(at-x grass_block-block1035 position5)

	(at-y grass_block-block1035 position3)

	(at-z grass_block-block1035 position-10)

	(block-present grass_block-block1035)
	(at-x grass_block-block1036 position5)

	(at-y grass_block-block1036 position3)

	(at-z grass_block-block1036 position-9)

	(block-present grass_block-block1036)
	(at-x grass_block-block1037 position5)

	(at-y grass_block-block1037 position3)

	(at-z grass_block-block1037 position-8)

	(block-present grass_block-block1037)
	(at-x grass_block-block1038 position5)

	(at-y grass_block-block1038 position3)

	(at-z grass_block-block1038 position-7)

	(block-present grass_block-block1038)
	(at-x grass_block-block1039 position5)

	(at-y grass_block-block1039 position3)

	(at-z grass_block-block1039 position-6)

	(block-present grass_block-block1039)
	(at-x grass_block-block1040 position5)

	(at-y grass_block-block1040 position3)

	(at-z grass_block-block1040 position-5)

	(block-present grass_block-block1040)
	(at-x grass_block-block1041 position5)

	(at-y grass_block-block1041 position3)

	(at-z grass_block-block1041 position-4)

	(block-present grass_block-block1041)
	(at-x grass_block-block1042 position5)

	(at-y grass_block-block1042 position3)

	(at-z grass_block-block1042 position-3)

	(block-present grass_block-block1042)
	(at-x grass_block-block1043 position5)

	(at-y grass_block-block1043 position3)

	(at-z grass_block-block1043 position-2)

	(block-present grass_block-block1043)
	(at-x grass_block-block1044 position5)

	(at-y grass_block-block1044 position3)

	(at-z grass_block-block1044 position-1)

	(block-present grass_block-block1044)
	(at-x grass_block-block1045 position5)

	(at-y grass_block-block1045 position3)

	(at-z grass_block-block1045 position0)

	(block-present grass_block-block1045)
	(at-x grass_block-block1046 position5)

	(at-y grass_block-block1046 position3)

	(at-z grass_block-block1046 position1)

	(block-present grass_block-block1046)
	(at-x grass_block-block1047 position5)

	(at-y grass_block-block1047 position3)

	(at-z grass_block-block1047 position2)

	(block-present grass_block-block1047)
	(at-x grass_block-block1048 position5)

	(at-y grass_block-block1048 position3)

	(at-z grass_block-block1048 position3)

	(block-present grass_block-block1048)
	(at-x grass_block-block1049 position5)

	(at-y grass_block-block1049 position3)

	(at-z grass_block-block1049 position4)

	(block-present grass_block-block1049)
	(at-x grass_block-block1050 position5)

	(at-y grass_block-block1050 position3)

	(at-z grass_block-block1050 position5)

	(block-present grass_block-block1050)
	(at-x grass_block-block1051 position5)

	(at-y grass_block-block1051 position3)

	(at-z grass_block-block1051 position6)

	(block-present grass_block-block1051)
	(at-x grass_block-block1052 position5)

	(at-y grass_block-block1052 position3)

	(at-z grass_block-block1052 position7)

	(block-present grass_block-block1052)
	(at-x grass_block-block1053 position5)

	(at-y grass_block-block1053 position3)

	(at-z grass_block-block1053 position8)

	(block-present grass_block-block1053)
	(at-x grass_block-block1054 position5)

	(at-y grass_block-block1054 position3)

	(at-z grass_block-block1054 position9)

	(block-present grass_block-block1054)
	(at-x grass_block-block1055 position5)

	(at-y grass_block-block1055 position3)

	(at-z grass_block-block1055 position10)

	(block-present grass_block-block1055)
	(at-x grass_block-block1056 position5)

	(at-y grass_block-block1056 position3)

	(at-z grass_block-block1056 position11)

	(block-present grass_block-block1056)
	(at-x grass_block-block1057 position5)

	(at-y grass_block-block1057 position3)

	(at-z grass_block-block1057 position12)

	(block-present grass_block-block1057)
	(at-x grass_block-block1058 position5)

	(at-y grass_block-block1058 position3)

	(at-z grass_block-block1058 position13)

	(block-present grass_block-block1058)
	(at-x grass_block-block1059 position5)

	(at-y grass_block-block1059 position3)

	(at-z grass_block-block1059 position14)

	(block-present grass_block-block1059)
	(at-x grass_block-block1060 position5)

	(at-y grass_block-block1060 position3)

	(at-z grass_block-block1060 position15)

	(block-present grass_block-block1060)
	(at-x grass_block-block1061 position5)

	(at-y grass_block-block1061 position3)

	(at-z grass_block-block1061 position16)

	(block-present grass_block-block1061)
	(at-x grass_block-block1062 position5)

	(at-y grass_block-block1062 position3)

	(at-z grass_block-block1062 position17)

	(block-present grass_block-block1062)
	(at-x grass_block-block1063 position5)

	(at-y grass_block-block1063 position3)

	(at-z grass_block-block1063 position18)

	(block-present grass_block-block1063)
	(at-x grass_block-block1064 position5)

	(at-y grass_block-block1064 position3)

	(at-z grass_block-block1064 position19)

	(block-present grass_block-block1064)
	(at-x grass_block-block1065 position5)

	(at-y grass_block-block1065 position3)

	(at-z grass_block-block1065 position20)

	(block-present grass_block-block1065)
	(at-x grass_block-block1066 position6)

	(at-y grass_block-block1066 position3)

	(at-z grass_block-block1066 position-20)

	(block-present grass_block-block1066)
	(at-x grass_block-block1067 position6)

	(at-y grass_block-block1067 position3)

	(at-z grass_block-block1067 position-19)

	(block-present grass_block-block1067)
	(at-x grass_block-block1068 position6)

	(at-y grass_block-block1068 position3)

	(at-z grass_block-block1068 position-18)

	(block-present grass_block-block1068)
	(at-x grass_block-block1069 position6)

	(at-y grass_block-block1069 position3)

	(at-z grass_block-block1069 position-17)

	(block-present grass_block-block1069)
	(at-x grass_block-block1070 position6)

	(at-y grass_block-block1070 position3)

	(at-z grass_block-block1070 position-16)

	(block-present grass_block-block1070)
	(at-x grass_block-block1071 position6)

	(at-y grass_block-block1071 position3)

	(at-z grass_block-block1071 position-15)

	(block-present grass_block-block1071)
	(at-x grass_block-block1072 position6)

	(at-y grass_block-block1072 position3)

	(at-z grass_block-block1072 position-14)

	(block-present grass_block-block1072)
	(at-x grass_block-block1073 position6)

	(at-y grass_block-block1073 position3)

	(at-z grass_block-block1073 position-13)

	(block-present grass_block-block1073)
	(at-x grass_block-block1074 position6)

	(at-y grass_block-block1074 position3)

	(at-z grass_block-block1074 position-12)

	(block-present grass_block-block1074)
	(at-x grass_block-block1075 position6)

	(at-y grass_block-block1075 position3)

	(at-z grass_block-block1075 position-11)

	(block-present grass_block-block1075)
	(at-x grass_block-block1076 position6)

	(at-y grass_block-block1076 position3)

	(at-z grass_block-block1076 position-10)

	(block-present grass_block-block1076)
	(at-x grass_block-block1077 position6)

	(at-y grass_block-block1077 position3)

	(at-z grass_block-block1077 position-9)

	(block-present grass_block-block1077)
	(at-x grass_block-block1078 position6)

	(at-y grass_block-block1078 position3)

	(at-z grass_block-block1078 position-8)

	(block-present grass_block-block1078)
	(at-x grass_block-block1079 position6)

	(at-y grass_block-block1079 position3)

	(at-z grass_block-block1079 position-7)

	(block-present grass_block-block1079)
	(at-x grass_block-block1080 position6)

	(at-y grass_block-block1080 position3)

	(at-z grass_block-block1080 position-6)

	(block-present grass_block-block1080)
	(at-x grass_block-block1081 position6)

	(at-y grass_block-block1081 position3)

	(at-z grass_block-block1081 position-5)

	(block-present grass_block-block1081)
	(at-x grass_block-block1082 position6)

	(at-y grass_block-block1082 position3)

	(at-z grass_block-block1082 position-4)

	(block-present grass_block-block1082)
	(at-x grass_block-block1083 position6)

	(at-y grass_block-block1083 position3)

	(at-z grass_block-block1083 position-3)

	(block-present grass_block-block1083)
	(at-x grass_block-block1084 position6)

	(at-y grass_block-block1084 position3)

	(at-z grass_block-block1084 position-2)

	(block-present grass_block-block1084)
	(at-x grass_block-block1085 position6)

	(at-y grass_block-block1085 position3)

	(at-z grass_block-block1085 position-1)

	(block-present grass_block-block1085)
	(at-x grass_block-block1086 position6)

	(at-y grass_block-block1086 position3)

	(at-z grass_block-block1086 position0)

	(block-present grass_block-block1086)
	(at-x grass_block-block1087 position6)

	(at-y grass_block-block1087 position3)

	(at-z grass_block-block1087 position1)

	(block-present grass_block-block1087)
	(at-x grass_block-block1088 position6)

	(at-y grass_block-block1088 position3)

	(at-z grass_block-block1088 position2)

	(block-present grass_block-block1088)
	(at-x grass_block-block1089 position6)

	(at-y grass_block-block1089 position3)

	(at-z grass_block-block1089 position3)

	(block-present grass_block-block1089)
	(at-x grass_block-block1090 position6)

	(at-y grass_block-block1090 position3)

	(at-z grass_block-block1090 position4)

	(block-present grass_block-block1090)
	(at-x grass_block-block1091 position6)

	(at-y grass_block-block1091 position3)

	(at-z grass_block-block1091 position5)

	(block-present grass_block-block1091)
	(at-x grass_block-block1092 position6)

	(at-y grass_block-block1092 position3)

	(at-z grass_block-block1092 position6)

	(block-present grass_block-block1092)
	(at-x grass_block-block1093 position6)

	(at-y grass_block-block1093 position3)

	(at-z grass_block-block1093 position7)

	(block-present grass_block-block1093)
	(at-x grass_block-block1094 position6)

	(at-y grass_block-block1094 position3)

	(at-z grass_block-block1094 position8)

	(block-present grass_block-block1094)
	(at-x grass_block-block1095 position6)

	(at-y grass_block-block1095 position3)

	(at-z grass_block-block1095 position9)

	(block-present grass_block-block1095)
	(at-x grass_block-block1096 position6)

	(at-y grass_block-block1096 position3)

	(at-z grass_block-block1096 position10)

	(block-present grass_block-block1096)
	(at-x grass_block-block1097 position6)

	(at-y grass_block-block1097 position3)

	(at-z grass_block-block1097 position11)

	(block-present grass_block-block1097)
	(at-x grass_block-block1098 position6)

	(at-y grass_block-block1098 position3)

	(at-z grass_block-block1098 position12)

	(block-present grass_block-block1098)
	(at-x grass_block-block1099 position6)

	(at-y grass_block-block1099 position3)

	(at-z grass_block-block1099 position13)

	(block-present grass_block-block1099)
	(at-x grass_block-block1100 position6)

	(at-y grass_block-block1100 position3)

	(at-z grass_block-block1100 position14)

	(block-present grass_block-block1100)
	(at-x grass_block-block1101 position6)

	(at-y grass_block-block1101 position3)

	(at-z grass_block-block1101 position15)

	(block-present grass_block-block1101)
	(at-x grass_block-block1102 position6)

	(at-y grass_block-block1102 position3)

	(at-z grass_block-block1102 position16)

	(block-present grass_block-block1102)
	(at-x grass_block-block1103 position6)

	(at-y grass_block-block1103 position3)

	(at-z grass_block-block1103 position17)

	(block-present grass_block-block1103)
	(at-x grass_block-block1104 position6)

	(at-y grass_block-block1104 position3)

	(at-z grass_block-block1104 position18)

	(block-present grass_block-block1104)
	(at-x grass_block-block1105 position6)

	(at-y grass_block-block1105 position3)

	(at-z grass_block-block1105 position19)

	(block-present grass_block-block1105)
	(at-x grass_block-block1106 position6)

	(at-y grass_block-block1106 position3)

	(at-z grass_block-block1106 position20)

	(block-present grass_block-block1106)
	(at-x grass_block-block1107 position7)

	(at-y grass_block-block1107 position3)

	(at-z grass_block-block1107 position-20)

	(block-present grass_block-block1107)
	(at-x grass_block-block1108 position7)

	(at-y grass_block-block1108 position3)

	(at-z grass_block-block1108 position-19)

	(block-present grass_block-block1108)
	(at-x grass_block-block1109 position7)

	(at-y grass_block-block1109 position3)

	(at-z grass_block-block1109 position-18)

	(block-present grass_block-block1109)
	(at-x grass_block-block1110 position7)

	(at-y grass_block-block1110 position3)

	(at-z grass_block-block1110 position-17)

	(block-present grass_block-block1110)
	(at-x grass_block-block1111 position7)

	(at-y grass_block-block1111 position3)

	(at-z grass_block-block1111 position-16)

	(block-present grass_block-block1111)
	(at-x grass_block-block1112 position7)

	(at-y grass_block-block1112 position3)

	(at-z grass_block-block1112 position-15)

	(block-present grass_block-block1112)
	(at-x grass_block-block1113 position7)

	(at-y grass_block-block1113 position3)

	(at-z grass_block-block1113 position-14)

	(block-present grass_block-block1113)
	(at-x grass_block-block1114 position7)

	(at-y grass_block-block1114 position3)

	(at-z grass_block-block1114 position-13)

	(block-present grass_block-block1114)
	(at-x grass_block-block1115 position7)

	(at-y grass_block-block1115 position3)

	(at-z grass_block-block1115 position-12)

	(block-present grass_block-block1115)
	(at-x grass_block-block1116 position7)

	(at-y grass_block-block1116 position3)

	(at-z grass_block-block1116 position-11)

	(block-present grass_block-block1116)
	(at-x grass_block-block1117 position7)

	(at-y grass_block-block1117 position3)

	(at-z grass_block-block1117 position-10)

	(block-present grass_block-block1117)
	(at-x grass_block-block1118 position7)

	(at-y grass_block-block1118 position3)

	(at-z grass_block-block1118 position-9)

	(block-present grass_block-block1118)
	(at-x grass_block-block1119 position7)

	(at-y grass_block-block1119 position3)

	(at-z grass_block-block1119 position-8)

	(block-present grass_block-block1119)
	(at-x grass_block-block1120 position7)

	(at-y grass_block-block1120 position3)

	(at-z grass_block-block1120 position-7)

	(block-present grass_block-block1120)
	(at-x grass_block-block1121 position7)

	(at-y grass_block-block1121 position3)

	(at-z grass_block-block1121 position-6)

	(block-present grass_block-block1121)
	(at-x grass_block-block1122 position7)

	(at-y grass_block-block1122 position3)

	(at-z grass_block-block1122 position-5)

	(block-present grass_block-block1122)
	(at-x grass_block-block1123 position7)

	(at-y grass_block-block1123 position3)

	(at-z grass_block-block1123 position-4)

	(block-present grass_block-block1123)
	(at-x grass_block-block1124 position7)

	(at-y grass_block-block1124 position3)

	(at-z grass_block-block1124 position-3)

	(block-present grass_block-block1124)
	(at-x grass_block-block1125 position7)

	(at-y grass_block-block1125 position3)

	(at-z grass_block-block1125 position-2)

	(block-present grass_block-block1125)
	(at-x grass_block-block1126 position7)

	(at-y grass_block-block1126 position3)

	(at-z grass_block-block1126 position-1)

	(block-present grass_block-block1126)
	(at-x grass_block-block1127 position7)

	(at-y grass_block-block1127 position3)

	(at-z grass_block-block1127 position0)

	(block-present grass_block-block1127)
	(at-x grass_block-block1128 position7)

	(at-y grass_block-block1128 position3)

	(at-z grass_block-block1128 position1)

	(block-present grass_block-block1128)
	(at-x grass_block-block1129 position7)

	(at-y grass_block-block1129 position3)

	(at-z grass_block-block1129 position2)

	(block-present grass_block-block1129)
	(at-x grass_block-block1130 position7)

	(at-y grass_block-block1130 position3)

	(at-z grass_block-block1130 position3)

	(block-present grass_block-block1130)
	(at-x grass_block-block1131 position7)

	(at-y grass_block-block1131 position3)

	(at-z grass_block-block1131 position4)

	(block-present grass_block-block1131)
	(at-x grass_block-block1132 position7)

	(at-y grass_block-block1132 position3)

	(at-z grass_block-block1132 position5)

	(block-present grass_block-block1132)
	(at-x grass_block-block1133 position7)

	(at-y grass_block-block1133 position3)

	(at-z grass_block-block1133 position6)

	(block-present grass_block-block1133)
	(at-x grass_block-block1134 position7)

	(at-y grass_block-block1134 position3)

	(at-z grass_block-block1134 position7)

	(block-present grass_block-block1134)
	(at-x grass_block-block1135 position7)

	(at-y grass_block-block1135 position3)

	(at-z grass_block-block1135 position8)

	(block-present grass_block-block1135)
	(at-x grass_block-block1136 position7)

	(at-y grass_block-block1136 position3)

	(at-z grass_block-block1136 position9)

	(block-present grass_block-block1136)
	(at-x grass_block-block1137 position7)

	(at-y grass_block-block1137 position3)

	(at-z grass_block-block1137 position10)

	(block-present grass_block-block1137)
	(at-x grass_block-block1138 position7)

	(at-y grass_block-block1138 position3)

	(at-z grass_block-block1138 position11)

	(block-present grass_block-block1138)
	(at-x grass_block-block1139 position7)

	(at-y grass_block-block1139 position3)

	(at-z grass_block-block1139 position12)

	(block-present grass_block-block1139)
	(at-x grass_block-block1140 position7)

	(at-y grass_block-block1140 position3)

	(at-z grass_block-block1140 position13)

	(block-present grass_block-block1140)
	(at-x grass_block-block1141 position7)

	(at-y grass_block-block1141 position3)

	(at-z grass_block-block1141 position14)

	(block-present grass_block-block1141)
	(at-x grass_block-block1142 position7)

	(at-y grass_block-block1142 position3)

	(at-z grass_block-block1142 position15)

	(block-present grass_block-block1142)
	(at-x grass_block-block1143 position7)

	(at-y grass_block-block1143 position3)

	(at-z grass_block-block1143 position16)

	(block-present grass_block-block1143)
	(at-x grass_block-block1144 position7)

	(at-y grass_block-block1144 position3)

	(at-z grass_block-block1144 position17)

	(block-present grass_block-block1144)
	(at-x grass_block-block1145 position7)

	(at-y grass_block-block1145 position3)

	(at-z grass_block-block1145 position18)

	(block-present grass_block-block1145)
	(at-x grass_block-block1146 position7)

	(at-y grass_block-block1146 position3)

	(at-z grass_block-block1146 position19)

	(block-present grass_block-block1146)
	(at-x grass_block-block1147 position7)

	(at-y grass_block-block1147 position3)

	(at-z grass_block-block1147 position20)

	(block-present grass_block-block1147)
	(at-x grass_block-block1148 position8)

	(at-y grass_block-block1148 position3)

	(at-z grass_block-block1148 position-20)

	(block-present grass_block-block1148)
	(at-x grass_block-block1149 position8)

	(at-y grass_block-block1149 position3)

	(at-z grass_block-block1149 position-19)

	(block-present grass_block-block1149)
	(at-x grass_block-block1150 position8)

	(at-y grass_block-block1150 position3)

	(at-z grass_block-block1150 position-18)

	(block-present grass_block-block1150)
	(at-x grass_block-block1151 position8)

	(at-y grass_block-block1151 position3)

	(at-z grass_block-block1151 position-17)

	(block-present grass_block-block1151)
	(at-x grass_block-block1152 position8)

	(at-y grass_block-block1152 position3)

	(at-z grass_block-block1152 position-16)

	(block-present grass_block-block1152)
	(at-x grass_block-block1153 position8)

	(at-y grass_block-block1153 position3)

	(at-z grass_block-block1153 position-15)

	(block-present grass_block-block1153)
	(at-x grass_block-block1154 position8)

	(at-y grass_block-block1154 position3)

	(at-z grass_block-block1154 position-14)

	(block-present grass_block-block1154)
	(at-x grass_block-block1155 position8)

	(at-y grass_block-block1155 position3)

	(at-z grass_block-block1155 position-13)

	(block-present grass_block-block1155)
	(at-x grass_block-block1156 position8)

	(at-y grass_block-block1156 position3)

	(at-z grass_block-block1156 position-12)

	(block-present grass_block-block1156)
	(at-x grass_block-block1157 position8)

	(at-y grass_block-block1157 position3)

	(at-z grass_block-block1157 position-11)

	(block-present grass_block-block1157)
	(at-x grass_block-block1158 position8)

	(at-y grass_block-block1158 position3)

	(at-z grass_block-block1158 position-10)

	(block-present grass_block-block1158)
	(at-x grass_block-block1159 position8)

	(at-y grass_block-block1159 position3)

	(at-z grass_block-block1159 position-9)

	(block-present grass_block-block1159)
	(at-x grass_block-block1160 position8)

	(at-y grass_block-block1160 position3)

	(at-z grass_block-block1160 position-8)

	(block-present grass_block-block1160)
	(at-x grass_block-block1161 position8)

	(at-y grass_block-block1161 position3)

	(at-z grass_block-block1161 position-7)

	(block-present grass_block-block1161)
	(at-x grass_block-block1162 position8)

	(at-y grass_block-block1162 position3)

	(at-z grass_block-block1162 position-6)

	(block-present grass_block-block1162)
	(at-x grass_block-block1163 position8)

	(at-y grass_block-block1163 position3)

	(at-z grass_block-block1163 position-5)

	(block-present grass_block-block1163)
	(at-x grass_block-block1164 position8)

	(at-y grass_block-block1164 position3)

	(at-z grass_block-block1164 position-4)

	(block-present grass_block-block1164)
	(at-x grass_block-block1165 position8)

	(at-y grass_block-block1165 position3)

	(at-z grass_block-block1165 position-3)

	(block-present grass_block-block1165)
	(at-x grass_block-block1166 position8)

	(at-y grass_block-block1166 position3)

	(at-z grass_block-block1166 position-2)

	(block-present grass_block-block1166)
	(at-x grass_block-block1167 position8)

	(at-y grass_block-block1167 position3)

	(at-z grass_block-block1167 position-1)

	(block-present grass_block-block1167)
	(at-x grass_block-block1168 position8)

	(at-y grass_block-block1168 position3)

	(at-z grass_block-block1168 position0)

	(block-present grass_block-block1168)
	(at-x grass_block-block1169 position8)

	(at-y grass_block-block1169 position3)

	(at-z grass_block-block1169 position1)

	(block-present grass_block-block1169)
	(at-x grass_block-block1170 position8)

	(at-y grass_block-block1170 position3)

	(at-z grass_block-block1170 position2)

	(block-present grass_block-block1170)
	(at-x grass_block-block1171 position8)

	(at-y grass_block-block1171 position3)

	(at-z grass_block-block1171 position3)

	(block-present grass_block-block1171)
	(at-x grass_block-block1172 position8)

	(at-y grass_block-block1172 position3)

	(at-z grass_block-block1172 position4)

	(block-present grass_block-block1172)
	(at-x grass_block-block1173 position8)

	(at-y grass_block-block1173 position3)

	(at-z grass_block-block1173 position5)

	(block-present grass_block-block1173)
	(at-x grass_block-block1174 position8)

	(at-y grass_block-block1174 position3)

	(at-z grass_block-block1174 position6)

	(block-present grass_block-block1174)
	(at-x grass_block-block1175 position8)

	(at-y grass_block-block1175 position3)

	(at-z grass_block-block1175 position7)

	(block-present grass_block-block1175)
	(at-x grass_block-block1176 position8)

	(at-y grass_block-block1176 position3)

	(at-z grass_block-block1176 position8)

	(block-present grass_block-block1176)
	(at-x grass_block-block1177 position8)

	(at-y grass_block-block1177 position3)

	(at-z grass_block-block1177 position9)

	(block-present grass_block-block1177)
	(at-x grass_block-block1178 position8)

	(at-y grass_block-block1178 position3)

	(at-z grass_block-block1178 position10)

	(block-present grass_block-block1178)
	(at-x grass_block-block1179 position8)

	(at-y grass_block-block1179 position3)

	(at-z grass_block-block1179 position11)

	(block-present grass_block-block1179)
	(at-x grass_block-block1180 position8)

	(at-y grass_block-block1180 position3)

	(at-z grass_block-block1180 position12)

	(block-present grass_block-block1180)
	(at-x grass_block-block1181 position8)

	(at-y grass_block-block1181 position3)

	(at-z grass_block-block1181 position13)

	(block-present grass_block-block1181)
	(at-x grass_block-block1182 position8)

	(at-y grass_block-block1182 position3)

	(at-z grass_block-block1182 position14)

	(block-present grass_block-block1182)
	(at-x grass_block-block1183 position8)

	(at-y grass_block-block1183 position3)

	(at-z grass_block-block1183 position15)

	(block-present grass_block-block1183)
	(at-x grass_block-block1184 position8)

	(at-y grass_block-block1184 position3)

	(at-z grass_block-block1184 position16)

	(block-present grass_block-block1184)
	(at-x grass_block-block1185 position8)

	(at-y grass_block-block1185 position3)

	(at-z grass_block-block1185 position17)

	(block-present grass_block-block1185)
	(at-x grass_block-block1186 position8)

	(at-y grass_block-block1186 position3)

	(at-z grass_block-block1186 position18)

	(block-present grass_block-block1186)
	(at-x grass_block-block1187 position8)

	(at-y grass_block-block1187 position3)

	(at-z grass_block-block1187 position19)

	(block-present grass_block-block1187)
	(at-x grass_block-block1188 position8)

	(at-y grass_block-block1188 position3)

	(at-z grass_block-block1188 position20)

	(block-present grass_block-block1188)
	(at-x grass_block-block1189 position9)

	(at-y grass_block-block1189 position3)

	(at-z grass_block-block1189 position-20)

	(block-present grass_block-block1189)
	(at-x grass_block-block1190 position9)

	(at-y grass_block-block1190 position3)

	(at-z grass_block-block1190 position-19)

	(block-present grass_block-block1190)
	(at-x grass_block-block1191 position9)

	(at-y grass_block-block1191 position3)

	(at-z grass_block-block1191 position-18)

	(block-present grass_block-block1191)
	(at-x grass_block-block1192 position9)

	(at-y grass_block-block1192 position3)

	(at-z grass_block-block1192 position-17)

	(block-present grass_block-block1192)
	(at-x grass_block-block1193 position9)

	(at-y grass_block-block1193 position3)

	(at-z grass_block-block1193 position-16)

	(block-present grass_block-block1193)
	(at-x grass_block-block1194 position9)

	(at-y grass_block-block1194 position3)

	(at-z grass_block-block1194 position-15)

	(block-present grass_block-block1194)
	(at-x grass_block-block1195 position9)

	(at-y grass_block-block1195 position3)

	(at-z grass_block-block1195 position-14)

	(block-present grass_block-block1195)
	(at-x grass_block-block1196 position9)

	(at-y grass_block-block1196 position3)

	(at-z grass_block-block1196 position-13)

	(block-present grass_block-block1196)
	(at-x grass_block-block1197 position9)

	(at-y grass_block-block1197 position3)

	(at-z grass_block-block1197 position-12)

	(block-present grass_block-block1197)
	(at-x grass_block-block1198 position9)

	(at-y grass_block-block1198 position3)

	(at-z grass_block-block1198 position-11)

	(block-present grass_block-block1198)
	(at-x grass_block-block1199 position9)

	(at-y grass_block-block1199 position3)

	(at-z grass_block-block1199 position-10)

	(block-present grass_block-block1199)
	(at-x grass_block-block1200 position9)

	(at-y grass_block-block1200 position3)

	(at-z grass_block-block1200 position-9)

	(block-present grass_block-block1200)
	(at-x grass_block-block1201 position9)

	(at-y grass_block-block1201 position3)

	(at-z grass_block-block1201 position-8)

	(block-present grass_block-block1201)
	(at-x grass_block-block1202 position9)

	(at-y grass_block-block1202 position3)

	(at-z grass_block-block1202 position-7)

	(block-present grass_block-block1202)
	(at-x grass_block-block1203 position9)

	(at-y grass_block-block1203 position3)

	(at-z grass_block-block1203 position-6)

	(block-present grass_block-block1203)
	(at-x grass_block-block1204 position9)

	(at-y grass_block-block1204 position3)

	(at-z grass_block-block1204 position-5)

	(block-present grass_block-block1204)
	(at-x grass_block-block1205 position9)

	(at-y grass_block-block1205 position3)

	(at-z grass_block-block1205 position-4)

	(block-present grass_block-block1205)
	(at-x grass_block-block1206 position9)

	(at-y grass_block-block1206 position3)

	(at-z grass_block-block1206 position-3)

	(block-present grass_block-block1206)
	(at-x grass_block-block1207 position9)

	(at-y grass_block-block1207 position3)

	(at-z grass_block-block1207 position-2)

	(block-present grass_block-block1207)
	(at-x grass_block-block1208 position9)

	(at-y grass_block-block1208 position3)

	(at-z grass_block-block1208 position-1)

	(block-present grass_block-block1208)
	(at-x grass_block-block1209 position9)

	(at-y grass_block-block1209 position3)

	(at-z grass_block-block1209 position0)

	(block-present grass_block-block1209)
	(at-x grass_block-block1210 position9)

	(at-y grass_block-block1210 position3)

	(at-z grass_block-block1210 position1)

	(block-present grass_block-block1210)
	(at-x grass_block-block1211 position9)

	(at-y grass_block-block1211 position3)

	(at-z grass_block-block1211 position2)

	(block-present grass_block-block1211)
	(at-x grass_block-block1212 position9)

	(at-y grass_block-block1212 position3)

	(at-z grass_block-block1212 position3)

	(block-present grass_block-block1212)
	(at-x grass_block-block1213 position9)

	(at-y grass_block-block1213 position3)

	(at-z grass_block-block1213 position4)

	(block-present grass_block-block1213)
	(at-x grass_block-block1214 position9)

	(at-y grass_block-block1214 position3)

	(at-z grass_block-block1214 position5)

	(block-present grass_block-block1214)
	(at-x grass_block-block1215 position9)

	(at-y grass_block-block1215 position3)

	(at-z grass_block-block1215 position6)

	(block-present grass_block-block1215)
	(at-x grass_block-block1216 position9)

	(at-y grass_block-block1216 position3)

	(at-z grass_block-block1216 position7)

	(block-present grass_block-block1216)
	(at-x grass_block-block1217 position9)

	(at-y grass_block-block1217 position3)

	(at-z grass_block-block1217 position8)

	(block-present grass_block-block1217)
	(at-x grass_block-block1218 position9)

	(at-y grass_block-block1218 position3)

	(at-z grass_block-block1218 position9)

	(block-present grass_block-block1218)
	(at-x grass_block-block1219 position9)

	(at-y grass_block-block1219 position3)

	(at-z grass_block-block1219 position10)

	(block-present grass_block-block1219)
	(at-x grass_block-block1220 position9)

	(at-y grass_block-block1220 position3)

	(at-z grass_block-block1220 position11)

	(block-present grass_block-block1220)
	(at-x grass_block-block1221 position9)

	(at-y grass_block-block1221 position3)

	(at-z grass_block-block1221 position12)

	(block-present grass_block-block1221)
	(at-x grass_block-block1222 position9)

	(at-y grass_block-block1222 position3)

	(at-z grass_block-block1222 position13)

	(block-present grass_block-block1222)
	(at-x grass_block-block1223 position9)

	(at-y grass_block-block1223 position3)

	(at-z grass_block-block1223 position14)

	(block-present grass_block-block1223)
	(at-x grass_block-block1224 position9)

	(at-y grass_block-block1224 position3)

	(at-z grass_block-block1224 position15)

	(block-present grass_block-block1224)
	(at-x grass_block-block1225 position9)

	(at-y grass_block-block1225 position3)

	(at-z grass_block-block1225 position16)

	(block-present grass_block-block1225)
	(at-x grass_block-block1226 position9)

	(at-y grass_block-block1226 position3)

	(at-z grass_block-block1226 position17)

	(block-present grass_block-block1226)
	(at-x grass_block-block1227 position9)

	(at-y grass_block-block1227 position3)

	(at-z grass_block-block1227 position18)

	(block-present grass_block-block1227)
	(at-x grass_block-block1228 position9)

	(at-y grass_block-block1228 position3)

	(at-z grass_block-block1228 position19)

	(block-present grass_block-block1228)
	(at-x grass_block-block1229 position9)

	(at-y grass_block-block1229 position3)

	(at-z grass_block-block1229 position20)

	(block-present grass_block-block1229)
	(at-x grass_block-block1230 position10)

	(at-y grass_block-block1230 position3)

	(at-z grass_block-block1230 position-20)

	(block-present grass_block-block1230)
	(at-x grass_block-block1231 position10)

	(at-y grass_block-block1231 position3)

	(at-z grass_block-block1231 position-19)

	(block-present grass_block-block1231)
	(at-x grass_block-block1232 position10)

	(at-y grass_block-block1232 position3)

	(at-z grass_block-block1232 position-18)

	(block-present grass_block-block1232)
	(at-x grass_block-block1233 position10)

	(at-y grass_block-block1233 position3)

	(at-z grass_block-block1233 position-17)

	(block-present grass_block-block1233)
	(at-x grass_block-block1234 position10)

	(at-y grass_block-block1234 position3)

	(at-z grass_block-block1234 position-16)

	(block-present grass_block-block1234)
	(at-x grass_block-block1235 position10)

	(at-y grass_block-block1235 position3)

	(at-z grass_block-block1235 position-15)

	(block-present grass_block-block1235)
	(at-x grass_block-block1236 position10)

	(at-y grass_block-block1236 position3)

	(at-z grass_block-block1236 position-14)

	(block-present grass_block-block1236)
	(at-x grass_block-block1237 position10)

	(at-y grass_block-block1237 position3)

	(at-z grass_block-block1237 position-13)

	(block-present grass_block-block1237)
	(at-x grass_block-block1238 position10)

	(at-y grass_block-block1238 position3)

	(at-z grass_block-block1238 position-12)

	(block-present grass_block-block1238)
	(at-x grass_block-block1239 position10)

	(at-y grass_block-block1239 position3)

	(at-z grass_block-block1239 position-11)

	(block-present grass_block-block1239)
	(at-x grass_block-block1240 position10)

	(at-y grass_block-block1240 position3)

	(at-z grass_block-block1240 position-10)

	(block-present grass_block-block1240)
	(at-x grass_block-block1241 position10)

	(at-y grass_block-block1241 position3)

	(at-z grass_block-block1241 position-9)

	(block-present grass_block-block1241)
	(at-x grass_block-block1242 position10)

	(at-y grass_block-block1242 position3)

	(at-z grass_block-block1242 position-8)

	(block-present grass_block-block1242)
	(at-x grass_block-block1243 position10)

	(at-y grass_block-block1243 position3)

	(at-z grass_block-block1243 position-7)

	(block-present grass_block-block1243)
	(at-x grass_block-block1244 position10)

	(at-y grass_block-block1244 position3)

	(at-z grass_block-block1244 position-6)

	(block-present grass_block-block1244)
	(at-x grass_block-block1245 position10)

	(at-y grass_block-block1245 position3)

	(at-z grass_block-block1245 position-5)

	(block-present grass_block-block1245)
	(at-x grass_block-block1246 position10)

	(at-y grass_block-block1246 position3)

	(at-z grass_block-block1246 position-4)

	(block-present grass_block-block1246)
	(at-x grass_block-block1247 position10)

	(at-y grass_block-block1247 position3)

	(at-z grass_block-block1247 position-3)

	(block-present grass_block-block1247)
	(at-x grass_block-block1248 position10)

	(at-y grass_block-block1248 position3)

	(at-z grass_block-block1248 position-2)

	(block-present grass_block-block1248)
	(at-x grass_block-block1249 position10)

	(at-y grass_block-block1249 position3)

	(at-z grass_block-block1249 position-1)

	(block-present grass_block-block1249)
	(at-x grass_block-block1250 position10)

	(at-y grass_block-block1250 position3)

	(at-z grass_block-block1250 position0)

	(block-present grass_block-block1250)
	(at-x grass_block-block1251 position10)

	(at-y grass_block-block1251 position3)

	(at-z grass_block-block1251 position1)

	(block-present grass_block-block1251)
	(at-x grass_block-block1252 position10)

	(at-y grass_block-block1252 position3)

	(at-z grass_block-block1252 position2)

	(block-present grass_block-block1252)
	(at-x grass_block-block1253 position10)

	(at-y grass_block-block1253 position3)

	(at-z grass_block-block1253 position3)

	(block-present grass_block-block1253)
	(at-x grass_block-block1254 position10)

	(at-y grass_block-block1254 position3)

	(at-z grass_block-block1254 position4)

	(block-present grass_block-block1254)
	(at-x grass_block-block1255 position10)

	(at-y grass_block-block1255 position3)

	(at-z grass_block-block1255 position5)

	(block-present grass_block-block1255)
	(at-x grass_block-block1256 position10)

	(at-y grass_block-block1256 position3)

	(at-z grass_block-block1256 position6)

	(block-present grass_block-block1256)
	(at-x grass_block-block1257 position10)

	(at-y grass_block-block1257 position3)

	(at-z grass_block-block1257 position7)

	(block-present grass_block-block1257)
	(at-x grass_block-block1258 position10)

	(at-y grass_block-block1258 position3)

	(at-z grass_block-block1258 position8)

	(block-present grass_block-block1258)
	(at-x grass_block-block1259 position10)

	(at-y grass_block-block1259 position3)

	(at-z grass_block-block1259 position9)

	(block-present grass_block-block1259)
	(at-x grass_block-block1260 position10)

	(at-y grass_block-block1260 position3)

	(at-z grass_block-block1260 position10)

	(block-present grass_block-block1260)
	(at-x grass_block-block1261 position10)

	(at-y grass_block-block1261 position3)

	(at-z grass_block-block1261 position11)

	(block-present grass_block-block1261)
	(at-x grass_block-block1262 position10)

	(at-y grass_block-block1262 position3)

	(at-z grass_block-block1262 position12)

	(block-present grass_block-block1262)
	(at-x grass_block-block1263 position10)

	(at-y grass_block-block1263 position3)

	(at-z grass_block-block1263 position13)

	(block-present grass_block-block1263)
	(at-x grass_block-block1264 position10)

	(at-y grass_block-block1264 position3)

	(at-z grass_block-block1264 position14)

	(block-present grass_block-block1264)
	(at-x grass_block-block1265 position10)

	(at-y grass_block-block1265 position3)

	(at-z grass_block-block1265 position15)

	(block-present grass_block-block1265)
	(at-x grass_block-block1266 position10)

	(at-y grass_block-block1266 position3)

	(at-z grass_block-block1266 position16)

	(block-present grass_block-block1266)
	(at-x grass_block-block1267 position10)

	(at-y grass_block-block1267 position3)

	(at-z grass_block-block1267 position17)

	(block-present grass_block-block1267)
	(at-x grass_block-block1268 position10)

	(at-y grass_block-block1268 position3)

	(at-z grass_block-block1268 position18)

	(block-present grass_block-block1268)
	(at-x grass_block-block1269 position10)

	(at-y grass_block-block1269 position3)

	(at-z grass_block-block1269 position19)

	(block-present grass_block-block1269)
	(at-x grass_block-block1270 position10)

	(at-y grass_block-block1270 position3)

	(at-z grass_block-block1270 position20)

	(block-present grass_block-block1270)
	(at-x grass_block-block1271 position11)

	(at-y grass_block-block1271 position3)

	(at-z grass_block-block1271 position-20)

	(block-present grass_block-block1271)
	(at-x grass_block-block1272 position11)

	(at-y grass_block-block1272 position3)

	(at-z grass_block-block1272 position-19)

	(block-present grass_block-block1272)
	(at-x grass_block-block1273 position11)

	(at-y grass_block-block1273 position3)

	(at-z grass_block-block1273 position-18)

	(block-present grass_block-block1273)
	(at-x grass_block-block1274 position11)

	(at-y grass_block-block1274 position3)

	(at-z grass_block-block1274 position-17)

	(block-present grass_block-block1274)
	(at-x grass_block-block1275 position11)

	(at-y grass_block-block1275 position3)

	(at-z grass_block-block1275 position-16)

	(block-present grass_block-block1275)
	(at-x grass_block-block1276 position11)

	(at-y grass_block-block1276 position3)

	(at-z grass_block-block1276 position-15)

	(block-present grass_block-block1276)
	(at-x grass_block-block1277 position11)

	(at-y grass_block-block1277 position3)

	(at-z grass_block-block1277 position-14)

	(block-present grass_block-block1277)
	(at-x grass_block-block1278 position11)

	(at-y grass_block-block1278 position3)

	(at-z grass_block-block1278 position-13)

	(block-present grass_block-block1278)
	(at-x grass_block-block1279 position11)

	(at-y grass_block-block1279 position3)

	(at-z grass_block-block1279 position-12)

	(block-present grass_block-block1279)
	(at-x grass_block-block1280 position11)

	(at-y grass_block-block1280 position3)

	(at-z grass_block-block1280 position-11)

	(block-present grass_block-block1280)
	(at-x grass_block-block1281 position11)

	(at-y grass_block-block1281 position3)

	(at-z grass_block-block1281 position-10)

	(block-present grass_block-block1281)
	(at-x grass_block-block1282 position11)

	(at-y grass_block-block1282 position3)

	(at-z grass_block-block1282 position-9)

	(block-present grass_block-block1282)
	(at-x grass_block-block1283 position11)

	(at-y grass_block-block1283 position3)

	(at-z grass_block-block1283 position-8)

	(block-present grass_block-block1283)
	(at-x grass_block-block1284 position11)

	(at-y grass_block-block1284 position3)

	(at-z grass_block-block1284 position-7)

	(block-present grass_block-block1284)
	(at-x grass_block-block1285 position11)

	(at-y grass_block-block1285 position3)

	(at-z grass_block-block1285 position-6)

	(block-present grass_block-block1285)
	(at-x grass_block-block1286 position11)

	(at-y grass_block-block1286 position3)

	(at-z grass_block-block1286 position-5)

	(block-present grass_block-block1286)
	(at-x grass_block-block1287 position11)

	(at-y grass_block-block1287 position3)

	(at-z grass_block-block1287 position-4)

	(block-present grass_block-block1287)
	(at-x grass_block-block1288 position11)

	(at-y grass_block-block1288 position3)

	(at-z grass_block-block1288 position-3)

	(block-present grass_block-block1288)
	(at-x grass_block-block1289 position11)

	(at-y grass_block-block1289 position3)

	(at-z grass_block-block1289 position-2)

	(block-present grass_block-block1289)
	(at-x grass_block-block1290 position11)

	(at-y grass_block-block1290 position3)

	(at-z grass_block-block1290 position-1)

	(block-present grass_block-block1290)
	(at-x grass_block-block1291 position11)

	(at-y grass_block-block1291 position3)

	(at-z grass_block-block1291 position0)

	(block-present grass_block-block1291)
	(at-x grass_block-block1292 position11)

	(at-y grass_block-block1292 position3)

	(at-z grass_block-block1292 position1)

	(block-present grass_block-block1292)
	(at-x grass_block-block1293 position11)

	(at-y grass_block-block1293 position3)

	(at-z grass_block-block1293 position2)

	(block-present grass_block-block1293)
	(at-x grass_block-block1294 position11)

	(at-y grass_block-block1294 position3)

	(at-z grass_block-block1294 position3)

	(block-present grass_block-block1294)
	(at-x grass_block-block1295 position11)

	(at-y grass_block-block1295 position3)

	(at-z grass_block-block1295 position4)

	(block-present grass_block-block1295)
	(at-x grass_block-block1296 position11)

	(at-y grass_block-block1296 position3)

	(at-z grass_block-block1296 position5)

	(block-present grass_block-block1296)
	(at-x grass_block-block1297 position11)

	(at-y grass_block-block1297 position3)

	(at-z grass_block-block1297 position6)

	(block-present grass_block-block1297)
	(at-x grass_block-block1298 position11)

	(at-y grass_block-block1298 position3)

	(at-z grass_block-block1298 position7)

	(block-present grass_block-block1298)
	(at-x grass_block-block1299 position11)

	(at-y grass_block-block1299 position3)

	(at-z grass_block-block1299 position8)

	(block-present grass_block-block1299)
	(at-x grass_block-block1300 position11)

	(at-y grass_block-block1300 position3)

	(at-z grass_block-block1300 position9)

	(block-present grass_block-block1300)
	(at-x grass_block-block1301 position11)

	(at-y grass_block-block1301 position3)

	(at-z grass_block-block1301 position10)

	(block-present grass_block-block1301)
	(at-x grass_block-block1302 position11)

	(at-y grass_block-block1302 position3)

	(at-z grass_block-block1302 position11)

	(block-present grass_block-block1302)
	(at-x grass_block-block1303 position11)

	(at-y grass_block-block1303 position3)

	(at-z grass_block-block1303 position12)

	(block-present grass_block-block1303)
	(at-x grass_block-block1304 position11)

	(at-y grass_block-block1304 position3)

	(at-z grass_block-block1304 position13)

	(block-present grass_block-block1304)
	(at-x grass_block-block1305 position11)

	(at-y grass_block-block1305 position3)

	(at-z grass_block-block1305 position14)

	(block-present grass_block-block1305)
	(at-x grass_block-block1306 position11)

	(at-y grass_block-block1306 position3)

	(at-z grass_block-block1306 position15)

	(block-present grass_block-block1306)
	(at-x grass_block-block1307 position11)

	(at-y grass_block-block1307 position3)

	(at-z grass_block-block1307 position16)

	(block-present grass_block-block1307)
	(at-x grass_block-block1308 position11)

	(at-y grass_block-block1308 position3)

	(at-z grass_block-block1308 position17)

	(block-present grass_block-block1308)
	(at-x grass_block-block1309 position11)

	(at-y grass_block-block1309 position3)

	(at-z grass_block-block1309 position18)

	(block-present grass_block-block1309)
	(at-x grass_block-block1310 position11)

	(at-y grass_block-block1310 position3)

	(at-z grass_block-block1310 position19)

	(block-present grass_block-block1310)
	(at-x grass_block-block1311 position11)

	(at-y grass_block-block1311 position3)

	(at-z grass_block-block1311 position20)

	(block-present grass_block-block1311)
	(at-x grass_block-block1312 position12)

	(at-y grass_block-block1312 position3)

	(at-z grass_block-block1312 position-20)

	(block-present grass_block-block1312)
	(at-x grass_block-block1313 position12)

	(at-y grass_block-block1313 position3)

	(at-z grass_block-block1313 position-19)

	(block-present grass_block-block1313)
	(at-x grass_block-block1314 position12)

	(at-y grass_block-block1314 position3)

	(at-z grass_block-block1314 position-18)

	(block-present grass_block-block1314)
	(at-x grass_block-block1315 position12)

	(at-y grass_block-block1315 position3)

	(at-z grass_block-block1315 position-17)

	(block-present grass_block-block1315)
	(at-x grass_block-block1316 position12)

	(at-y grass_block-block1316 position3)

	(at-z grass_block-block1316 position-16)

	(block-present grass_block-block1316)
	(at-x grass_block-block1317 position12)

	(at-y grass_block-block1317 position3)

	(at-z grass_block-block1317 position-15)

	(block-present grass_block-block1317)
	(at-x grass_block-block1318 position12)

	(at-y grass_block-block1318 position3)

	(at-z grass_block-block1318 position-14)

	(block-present grass_block-block1318)
	(at-x grass_block-block1319 position12)

	(at-y grass_block-block1319 position3)

	(at-z grass_block-block1319 position-13)

	(block-present grass_block-block1319)
	(at-x grass_block-block1320 position12)

	(at-y grass_block-block1320 position3)

	(at-z grass_block-block1320 position-12)

	(block-present grass_block-block1320)
	(at-x grass_block-block1321 position12)

	(at-y grass_block-block1321 position3)

	(at-z grass_block-block1321 position-11)

	(block-present grass_block-block1321)
	(at-x grass_block-block1322 position12)

	(at-y grass_block-block1322 position3)

	(at-z grass_block-block1322 position-10)

	(block-present grass_block-block1322)
	(at-x grass_block-block1323 position12)

	(at-y grass_block-block1323 position3)

	(at-z grass_block-block1323 position-9)

	(block-present grass_block-block1323)
	(at-x grass_block-block1324 position12)

	(at-y grass_block-block1324 position3)

	(at-z grass_block-block1324 position-8)

	(block-present grass_block-block1324)
	(at-x grass_block-block1325 position12)

	(at-y grass_block-block1325 position3)

	(at-z grass_block-block1325 position-7)

	(block-present grass_block-block1325)
	(at-x grass_block-block1326 position12)

	(at-y grass_block-block1326 position3)

	(at-z grass_block-block1326 position-6)

	(block-present grass_block-block1326)
	(at-x grass_block-block1327 position12)

	(at-y grass_block-block1327 position3)

	(at-z grass_block-block1327 position-5)

	(block-present grass_block-block1327)
	(at-x grass_block-block1328 position12)

	(at-y grass_block-block1328 position3)

	(at-z grass_block-block1328 position-4)

	(block-present grass_block-block1328)
	(at-x grass_block-block1329 position12)

	(at-y grass_block-block1329 position3)

	(at-z grass_block-block1329 position-3)

	(block-present grass_block-block1329)
	(at-x grass_block-block1330 position12)

	(at-y grass_block-block1330 position3)

	(at-z grass_block-block1330 position-2)

	(block-present grass_block-block1330)
	(at-x grass_block-block1331 position12)

	(at-y grass_block-block1331 position3)

	(at-z grass_block-block1331 position-1)

	(block-present grass_block-block1331)
	(at-x grass_block-block1332 position12)

	(at-y grass_block-block1332 position3)

	(at-z grass_block-block1332 position0)

	(block-present grass_block-block1332)
	(at-x grass_block-block1333 position12)

	(at-y grass_block-block1333 position3)

	(at-z grass_block-block1333 position1)

	(block-present grass_block-block1333)
	(at-x grass_block-block1334 position12)

	(at-y grass_block-block1334 position3)

	(at-z grass_block-block1334 position2)

	(block-present grass_block-block1334)
	(at-x grass_block-block1335 position12)

	(at-y grass_block-block1335 position3)

	(at-z grass_block-block1335 position3)

	(block-present grass_block-block1335)
	(at-x grass_block-block1336 position12)

	(at-y grass_block-block1336 position3)

	(at-z grass_block-block1336 position4)

	(block-present grass_block-block1336)
	(at-x grass_block-block1337 position12)

	(at-y grass_block-block1337 position3)

	(at-z grass_block-block1337 position5)

	(block-present grass_block-block1337)
	(at-x grass_block-block1338 position12)

	(at-y grass_block-block1338 position3)

	(at-z grass_block-block1338 position6)

	(block-present grass_block-block1338)
	(at-x grass_block-block1339 position12)

	(at-y grass_block-block1339 position3)

	(at-z grass_block-block1339 position7)

	(block-present grass_block-block1339)
	(at-x grass_block-block1340 position12)

	(at-y grass_block-block1340 position3)

	(at-z grass_block-block1340 position8)

	(block-present grass_block-block1340)
	(at-x grass_block-block1341 position12)

	(at-y grass_block-block1341 position3)

	(at-z grass_block-block1341 position9)

	(block-present grass_block-block1341)
	(at-x grass_block-block1342 position12)

	(at-y grass_block-block1342 position3)

	(at-z grass_block-block1342 position10)

	(block-present grass_block-block1342)
	(at-x grass_block-block1343 position12)

	(at-y grass_block-block1343 position3)

	(at-z grass_block-block1343 position11)

	(block-present grass_block-block1343)
	(at-x grass_block-block1344 position12)

	(at-y grass_block-block1344 position3)

	(at-z grass_block-block1344 position12)

	(block-present grass_block-block1344)
	(at-x grass_block-block1345 position12)

	(at-y grass_block-block1345 position3)

	(at-z grass_block-block1345 position13)

	(block-present grass_block-block1345)
	(at-x grass_block-block1346 position12)

	(at-y grass_block-block1346 position3)

	(at-z grass_block-block1346 position14)

	(block-present grass_block-block1346)
	(at-x grass_block-block1347 position12)

	(at-y grass_block-block1347 position3)

	(at-z grass_block-block1347 position15)

	(block-present grass_block-block1347)
	(at-x grass_block-block1348 position12)

	(at-y grass_block-block1348 position3)

	(at-z grass_block-block1348 position16)

	(block-present grass_block-block1348)
	(at-x grass_block-block1349 position12)

	(at-y grass_block-block1349 position3)

	(at-z grass_block-block1349 position17)

	(block-present grass_block-block1349)
	(at-x grass_block-block1350 position12)

	(at-y grass_block-block1350 position3)

	(at-z grass_block-block1350 position18)

	(block-present grass_block-block1350)
	(at-x grass_block-block1351 position12)

	(at-y grass_block-block1351 position3)

	(at-z grass_block-block1351 position19)

	(block-present grass_block-block1351)
	(at-x grass_block-block1352 position12)

	(at-y grass_block-block1352 position3)

	(at-z grass_block-block1352 position20)

	(block-present grass_block-block1352)
	(at-x grass_block-block1353 position13)

	(at-y grass_block-block1353 position3)

	(at-z grass_block-block1353 position-20)

	(block-present grass_block-block1353)
	(at-x grass_block-block1354 position13)

	(at-y grass_block-block1354 position3)

	(at-z grass_block-block1354 position-19)

	(block-present grass_block-block1354)
	(at-x grass_block-block1355 position13)

	(at-y grass_block-block1355 position3)

	(at-z grass_block-block1355 position-18)

	(block-present grass_block-block1355)
	(at-x grass_block-block1356 position13)

	(at-y grass_block-block1356 position3)

	(at-z grass_block-block1356 position-17)

	(block-present grass_block-block1356)
	(at-x grass_block-block1357 position13)

	(at-y grass_block-block1357 position3)

	(at-z grass_block-block1357 position-16)

	(block-present grass_block-block1357)
	(at-x grass_block-block1358 position13)

	(at-y grass_block-block1358 position3)

	(at-z grass_block-block1358 position-15)

	(block-present grass_block-block1358)
	(at-x grass_block-block1359 position13)

	(at-y grass_block-block1359 position3)

	(at-z grass_block-block1359 position-14)

	(block-present grass_block-block1359)
	(at-x grass_block-block1360 position13)

	(at-y grass_block-block1360 position3)

	(at-z grass_block-block1360 position-13)

	(block-present grass_block-block1360)
	(at-x grass_block-block1361 position13)

	(at-y grass_block-block1361 position3)

	(at-z grass_block-block1361 position-12)

	(block-present grass_block-block1361)
	(at-x grass_block-block1362 position13)

	(at-y grass_block-block1362 position3)

	(at-z grass_block-block1362 position-11)

	(block-present grass_block-block1362)
	(at-x grass_block-block1363 position13)

	(at-y grass_block-block1363 position3)

	(at-z grass_block-block1363 position-10)

	(block-present grass_block-block1363)
	(at-x grass_block-block1364 position13)

	(at-y grass_block-block1364 position3)

	(at-z grass_block-block1364 position-9)

	(block-present grass_block-block1364)
	(at-x grass_block-block1365 position13)

	(at-y grass_block-block1365 position3)

	(at-z grass_block-block1365 position-8)

	(block-present grass_block-block1365)
	(at-x grass_block-block1366 position13)

	(at-y grass_block-block1366 position3)

	(at-z grass_block-block1366 position-7)

	(block-present grass_block-block1366)
	(at-x grass_block-block1367 position13)

	(at-y grass_block-block1367 position3)

	(at-z grass_block-block1367 position-6)

	(block-present grass_block-block1367)
	(at-x grass_block-block1368 position13)

	(at-y grass_block-block1368 position3)

	(at-z grass_block-block1368 position-5)

	(block-present grass_block-block1368)
	(at-x grass_block-block1369 position13)

	(at-y grass_block-block1369 position3)

	(at-z grass_block-block1369 position-4)

	(block-present grass_block-block1369)
	(at-x grass_block-block1370 position13)

	(at-y grass_block-block1370 position3)

	(at-z grass_block-block1370 position-3)

	(block-present grass_block-block1370)
	(at-x grass_block-block1371 position13)

	(at-y grass_block-block1371 position3)

	(at-z grass_block-block1371 position-2)

	(block-present grass_block-block1371)
	(at-x grass_block-block1372 position13)

	(at-y grass_block-block1372 position3)

	(at-z grass_block-block1372 position-1)

	(block-present grass_block-block1372)
	(at-x grass_block-block1373 position13)

	(at-y grass_block-block1373 position3)

	(at-z grass_block-block1373 position0)

	(block-present grass_block-block1373)
	(at-x grass_block-block1374 position13)

	(at-y grass_block-block1374 position3)

	(at-z grass_block-block1374 position1)

	(block-present grass_block-block1374)
	(at-x grass_block-block1375 position13)

	(at-y grass_block-block1375 position3)

	(at-z grass_block-block1375 position2)

	(block-present grass_block-block1375)
	(at-x grass_block-block1376 position13)

	(at-y grass_block-block1376 position3)

	(at-z grass_block-block1376 position3)

	(block-present grass_block-block1376)
	(at-x grass_block-block1377 position13)

	(at-y grass_block-block1377 position3)

	(at-z grass_block-block1377 position4)

	(block-present grass_block-block1377)
	(at-x grass_block-block1378 position13)

	(at-y grass_block-block1378 position3)

	(at-z grass_block-block1378 position5)

	(block-present grass_block-block1378)
	(at-x grass_block-block1379 position13)

	(at-y grass_block-block1379 position3)

	(at-z grass_block-block1379 position6)

	(block-present grass_block-block1379)
	(at-x grass_block-block1380 position13)

	(at-y grass_block-block1380 position3)

	(at-z grass_block-block1380 position7)

	(block-present grass_block-block1380)
	(at-x grass_block-block1381 position13)

	(at-y grass_block-block1381 position3)

	(at-z grass_block-block1381 position8)

	(block-present grass_block-block1381)
	(at-x grass_block-block1382 position13)

	(at-y grass_block-block1382 position3)

	(at-z grass_block-block1382 position9)

	(block-present grass_block-block1382)
	(at-x grass_block-block1383 position13)

	(at-y grass_block-block1383 position3)

	(at-z grass_block-block1383 position10)

	(block-present grass_block-block1383)
	(at-x grass_block-block1384 position13)

	(at-y grass_block-block1384 position3)

	(at-z grass_block-block1384 position11)

	(block-present grass_block-block1384)
	(at-x grass_block-block1385 position13)

	(at-y grass_block-block1385 position3)

	(at-z grass_block-block1385 position12)

	(block-present grass_block-block1385)
	(at-x grass_block-block1386 position13)

	(at-y grass_block-block1386 position3)

	(at-z grass_block-block1386 position13)

	(block-present grass_block-block1386)
	(at-x grass_block-block1387 position13)

	(at-y grass_block-block1387 position3)

	(at-z grass_block-block1387 position14)

	(block-present grass_block-block1387)
	(at-x grass_block-block1388 position13)

	(at-y grass_block-block1388 position3)

	(at-z grass_block-block1388 position15)

	(block-present grass_block-block1388)
	(at-x grass_block-block1389 position13)

	(at-y grass_block-block1389 position3)

	(at-z grass_block-block1389 position16)

	(block-present grass_block-block1389)
	(at-x grass_block-block1390 position13)

	(at-y grass_block-block1390 position3)

	(at-z grass_block-block1390 position17)

	(block-present grass_block-block1390)
	(at-x grass_block-block1391 position13)

	(at-y grass_block-block1391 position3)

	(at-z grass_block-block1391 position18)

	(block-present grass_block-block1391)
	(at-x grass_block-block1392 position13)

	(at-y grass_block-block1392 position3)

	(at-z grass_block-block1392 position19)

	(block-present grass_block-block1392)
	(at-x grass_block-block1393 position13)

	(at-y grass_block-block1393 position3)

	(at-z grass_block-block1393 position20)

	(block-present grass_block-block1393)
	(at-x grass_block-block1394 position14)

	(at-y grass_block-block1394 position3)

	(at-z grass_block-block1394 position-20)

	(block-present grass_block-block1394)
	(at-x grass_block-block1395 position14)

	(at-y grass_block-block1395 position3)

	(at-z grass_block-block1395 position-19)

	(block-present grass_block-block1395)
	(at-x grass_block-block1396 position14)

	(at-y grass_block-block1396 position3)

	(at-z grass_block-block1396 position-18)

	(block-present grass_block-block1396)
	(at-x grass_block-block1397 position14)

	(at-y grass_block-block1397 position3)

	(at-z grass_block-block1397 position-17)

	(block-present grass_block-block1397)
	(at-x grass_block-block1398 position14)

	(at-y grass_block-block1398 position3)

	(at-z grass_block-block1398 position-16)

	(block-present grass_block-block1398)
	(at-x grass_block-block1399 position14)

	(at-y grass_block-block1399 position3)

	(at-z grass_block-block1399 position-15)

	(block-present grass_block-block1399)
	(at-x grass_block-block1400 position14)

	(at-y grass_block-block1400 position3)

	(at-z grass_block-block1400 position-14)

	(block-present grass_block-block1400)
	(at-x grass_block-block1401 position14)

	(at-y grass_block-block1401 position3)

	(at-z grass_block-block1401 position-13)

	(block-present grass_block-block1401)
	(at-x grass_block-block1402 position14)

	(at-y grass_block-block1402 position3)

	(at-z grass_block-block1402 position-12)

	(block-present grass_block-block1402)
	(at-x grass_block-block1403 position14)

	(at-y grass_block-block1403 position3)

	(at-z grass_block-block1403 position-11)

	(block-present grass_block-block1403)
	(at-x grass_block-block1404 position14)

	(at-y grass_block-block1404 position3)

	(at-z grass_block-block1404 position-10)

	(block-present grass_block-block1404)
	(at-x grass_block-block1405 position14)

	(at-y grass_block-block1405 position3)

	(at-z grass_block-block1405 position-9)

	(block-present grass_block-block1405)
	(at-x grass_block-block1406 position14)

	(at-y grass_block-block1406 position3)

	(at-z grass_block-block1406 position-8)

	(block-present grass_block-block1406)
	(at-x grass_block-block1407 position14)

	(at-y grass_block-block1407 position3)

	(at-z grass_block-block1407 position-7)

	(block-present grass_block-block1407)
	(at-x grass_block-block1408 position14)

	(at-y grass_block-block1408 position3)

	(at-z grass_block-block1408 position-6)

	(block-present grass_block-block1408)
	(at-x grass_block-block1409 position14)

	(at-y grass_block-block1409 position3)

	(at-z grass_block-block1409 position-5)

	(block-present grass_block-block1409)
	(at-x grass_block-block1410 position14)

	(at-y grass_block-block1410 position3)

	(at-z grass_block-block1410 position-4)

	(block-present grass_block-block1410)
	(at-x grass_block-block1411 position14)

	(at-y grass_block-block1411 position3)

	(at-z grass_block-block1411 position-3)

	(block-present grass_block-block1411)
	(at-x grass_block-block1412 position14)

	(at-y grass_block-block1412 position3)

	(at-z grass_block-block1412 position-2)

	(block-present grass_block-block1412)
	(at-x grass_block-block1413 position14)

	(at-y grass_block-block1413 position3)

	(at-z grass_block-block1413 position-1)

	(block-present grass_block-block1413)
	(at-x grass_block-block1414 position14)

	(at-y grass_block-block1414 position3)

	(at-z grass_block-block1414 position0)

	(block-present grass_block-block1414)
	(at-x grass_block-block1415 position14)

	(at-y grass_block-block1415 position3)

	(at-z grass_block-block1415 position1)

	(block-present grass_block-block1415)
	(at-x grass_block-block1416 position14)

	(at-y grass_block-block1416 position3)

	(at-z grass_block-block1416 position2)

	(block-present grass_block-block1416)
	(at-x grass_block-block1417 position14)

	(at-y grass_block-block1417 position3)

	(at-z grass_block-block1417 position3)

	(block-present grass_block-block1417)
	(at-x grass_block-block1418 position14)

	(at-y grass_block-block1418 position3)

	(at-z grass_block-block1418 position4)

	(block-present grass_block-block1418)
	(at-x grass_block-block1419 position14)

	(at-y grass_block-block1419 position3)

	(at-z grass_block-block1419 position5)

	(block-present grass_block-block1419)
	(at-x grass_block-block1420 position14)

	(at-y grass_block-block1420 position3)

	(at-z grass_block-block1420 position6)

	(block-present grass_block-block1420)
	(at-x grass_block-block1421 position14)

	(at-y grass_block-block1421 position3)

	(at-z grass_block-block1421 position7)

	(block-present grass_block-block1421)
	(at-x grass_block-block1422 position14)

	(at-y grass_block-block1422 position3)

	(at-z grass_block-block1422 position8)

	(block-present grass_block-block1422)
	(at-x grass_block-block1423 position14)

	(at-y grass_block-block1423 position3)

	(at-z grass_block-block1423 position9)

	(block-present grass_block-block1423)
	(at-x grass_block-block1424 position14)

	(at-y grass_block-block1424 position3)

	(at-z grass_block-block1424 position10)

	(block-present grass_block-block1424)
	(at-x grass_block-block1425 position14)

	(at-y grass_block-block1425 position3)

	(at-z grass_block-block1425 position11)

	(block-present grass_block-block1425)
	(at-x grass_block-block1426 position14)

	(at-y grass_block-block1426 position3)

	(at-z grass_block-block1426 position12)

	(block-present grass_block-block1426)
	(at-x grass_block-block1427 position14)

	(at-y grass_block-block1427 position3)

	(at-z grass_block-block1427 position13)

	(block-present grass_block-block1427)
	(at-x grass_block-block1428 position14)

	(at-y grass_block-block1428 position3)

	(at-z grass_block-block1428 position14)

	(block-present grass_block-block1428)
	(at-x grass_block-block1429 position14)

	(at-y grass_block-block1429 position3)

	(at-z grass_block-block1429 position15)

	(block-present grass_block-block1429)
	(at-x grass_block-block1430 position14)

	(at-y grass_block-block1430 position3)

	(at-z grass_block-block1430 position16)

	(block-present grass_block-block1430)
	(at-x grass_block-block1431 position14)

	(at-y grass_block-block1431 position3)

	(at-z grass_block-block1431 position17)

	(block-present grass_block-block1431)
	(at-x grass_block-block1432 position14)

	(at-y grass_block-block1432 position3)

	(at-z grass_block-block1432 position18)

	(block-present grass_block-block1432)
	(at-x grass_block-block1433 position14)

	(at-y grass_block-block1433 position3)

	(at-z grass_block-block1433 position19)

	(block-present grass_block-block1433)
	(at-x grass_block-block1434 position14)

	(at-y grass_block-block1434 position3)

	(at-z grass_block-block1434 position20)

	(block-present grass_block-block1434)
	(at-x grass_block-block1435 position15)

	(at-y grass_block-block1435 position3)

	(at-z grass_block-block1435 position-20)

	(block-present grass_block-block1435)
	(at-x grass_block-block1436 position15)

	(at-y grass_block-block1436 position3)

	(at-z grass_block-block1436 position-19)

	(block-present grass_block-block1436)
	(at-x grass_block-block1437 position15)

	(at-y grass_block-block1437 position3)

	(at-z grass_block-block1437 position-18)

	(block-present grass_block-block1437)
	(at-x grass_block-block1438 position15)

	(at-y grass_block-block1438 position3)

	(at-z grass_block-block1438 position-17)

	(block-present grass_block-block1438)
	(at-x grass_block-block1439 position15)

	(at-y grass_block-block1439 position3)

	(at-z grass_block-block1439 position-16)

	(block-present grass_block-block1439)
	(at-x grass_block-block1440 position15)

	(at-y grass_block-block1440 position3)

	(at-z grass_block-block1440 position-15)

	(block-present grass_block-block1440)
	(at-x grass_block-block1441 position15)

	(at-y grass_block-block1441 position3)

	(at-z grass_block-block1441 position-14)

	(block-present grass_block-block1441)
	(at-x grass_block-block1442 position15)

	(at-y grass_block-block1442 position3)

	(at-z grass_block-block1442 position-13)

	(block-present grass_block-block1442)
	(at-x grass_block-block1443 position15)

	(at-y grass_block-block1443 position3)

	(at-z grass_block-block1443 position-12)

	(block-present grass_block-block1443)
	(at-x grass_block-block1444 position15)

	(at-y grass_block-block1444 position3)

	(at-z grass_block-block1444 position-11)

	(block-present grass_block-block1444)
	(at-x grass_block-block1445 position15)

	(at-y grass_block-block1445 position3)

	(at-z grass_block-block1445 position-10)

	(block-present grass_block-block1445)
	(at-x grass_block-block1446 position15)

	(at-y grass_block-block1446 position3)

	(at-z grass_block-block1446 position-9)

	(block-present grass_block-block1446)
	(at-x grass_block-block1447 position15)

	(at-y grass_block-block1447 position3)

	(at-z grass_block-block1447 position-8)

	(block-present grass_block-block1447)
	(at-x grass_block-block1448 position15)

	(at-y grass_block-block1448 position3)

	(at-z grass_block-block1448 position-7)

	(block-present grass_block-block1448)
	(at-x grass_block-block1449 position15)

	(at-y grass_block-block1449 position3)

	(at-z grass_block-block1449 position-6)

	(block-present grass_block-block1449)
	(at-x grass_block-block1450 position15)

	(at-y grass_block-block1450 position3)

	(at-z grass_block-block1450 position-5)

	(block-present grass_block-block1450)
	(at-x grass_block-block1451 position15)

	(at-y grass_block-block1451 position3)

	(at-z grass_block-block1451 position-4)

	(block-present grass_block-block1451)
	(at-x grass_block-block1452 position15)

	(at-y grass_block-block1452 position3)

	(at-z grass_block-block1452 position-3)

	(block-present grass_block-block1452)
	(at-x grass_block-block1453 position15)

	(at-y grass_block-block1453 position3)

	(at-z grass_block-block1453 position-2)

	(block-present grass_block-block1453)
	(at-x grass_block-block1454 position15)

	(at-y grass_block-block1454 position3)

	(at-z grass_block-block1454 position-1)

	(block-present grass_block-block1454)
	(at-x grass_block-block1455 position15)

	(at-y grass_block-block1455 position3)

	(at-z grass_block-block1455 position0)

	(block-present grass_block-block1455)
	(at-x grass_block-block1456 position15)

	(at-y grass_block-block1456 position3)

	(at-z grass_block-block1456 position1)

	(block-present grass_block-block1456)
	(at-x grass_block-block1457 position15)

	(at-y grass_block-block1457 position3)

	(at-z grass_block-block1457 position2)

	(block-present grass_block-block1457)
	(at-x grass_block-block1458 position15)

	(at-y grass_block-block1458 position3)

	(at-z grass_block-block1458 position3)

	(block-present grass_block-block1458)
	(at-x grass_block-block1459 position15)

	(at-y grass_block-block1459 position3)

	(at-z grass_block-block1459 position4)

	(block-present grass_block-block1459)
	(at-x grass_block-block1460 position15)

	(at-y grass_block-block1460 position3)

	(at-z grass_block-block1460 position5)

	(block-present grass_block-block1460)
	(at-x grass_block-block1461 position15)

	(at-y grass_block-block1461 position3)

	(at-z grass_block-block1461 position6)

	(block-present grass_block-block1461)
	(at-x grass_block-block1462 position15)

	(at-y grass_block-block1462 position3)

	(at-z grass_block-block1462 position7)

	(block-present grass_block-block1462)
	(at-x grass_block-block1463 position15)

	(at-y grass_block-block1463 position3)

	(at-z grass_block-block1463 position8)

	(block-present grass_block-block1463)
	(at-x grass_block-block1464 position15)

	(at-y grass_block-block1464 position3)

	(at-z grass_block-block1464 position9)

	(block-present grass_block-block1464)
	(at-x grass_block-block1465 position15)

	(at-y grass_block-block1465 position3)

	(at-z grass_block-block1465 position10)

	(block-present grass_block-block1465)
	(at-x grass_block-block1466 position15)

	(at-y grass_block-block1466 position3)

	(at-z grass_block-block1466 position11)

	(block-present grass_block-block1466)
	(at-x grass_block-block1467 position15)

	(at-y grass_block-block1467 position3)

	(at-z grass_block-block1467 position12)

	(block-present grass_block-block1467)
	(at-x grass_block-block1468 position15)

	(at-y grass_block-block1468 position3)

	(at-z grass_block-block1468 position13)

	(block-present grass_block-block1468)
	(at-x grass_block-block1469 position15)

	(at-y grass_block-block1469 position3)

	(at-z grass_block-block1469 position14)

	(block-present grass_block-block1469)
	(at-x grass_block-block1470 position15)

	(at-y grass_block-block1470 position3)

	(at-z grass_block-block1470 position15)

	(block-present grass_block-block1470)
	(at-x grass_block-block1471 position15)

	(at-y grass_block-block1471 position3)

	(at-z grass_block-block1471 position16)

	(block-present grass_block-block1471)
	(at-x grass_block-block1472 position15)

	(at-y grass_block-block1472 position3)

	(at-z grass_block-block1472 position17)

	(block-present grass_block-block1472)
	(at-x grass_block-block1473 position15)

	(at-y grass_block-block1473 position3)

	(at-z grass_block-block1473 position18)

	(block-present grass_block-block1473)
	(at-x grass_block-block1474 position15)

	(at-y grass_block-block1474 position3)

	(at-z grass_block-block1474 position19)

	(block-present grass_block-block1474)
	(at-x grass_block-block1475 position15)

	(at-y grass_block-block1475 position3)

	(at-z grass_block-block1475 position20)

	(block-present grass_block-block1475)
	(at-x grass_block-block1476 position16)

	(at-y grass_block-block1476 position3)

	(at-z grass_block-block1476 position-20)

	(block-present grass_block-block1476)
	(at-x grass_block-block1477 position16)

	(at-y grass_block-block1477 position3)

	(at-z grass_block-block1477 position-19)

	(block-present grass_block-block1477)
	(at-x grass_block-block1478 position16)

	(at-y grass_block-block1478 position3)

	(at-z grass_block-block1478 position-18)

	(block-present grass_block-block1478)
	(at-x grass_block-block1479 position16)

	(at-y grass_block-block1479 position3)

	(at-z grass_block-block1479 position-17)

	(block-present grass_block-block1479)
	(at-x grass_block-block1480 position16)

	(at-y grass_block-block1480 position3)

	(at-z grass_block-block1480 position-16)

	(block-present grass_block-block1480)
	(at-x grass_block-block1481 position16)

	(at-y grass_block-block1481 position3)

	(at-z grass_block-block1481 position-15)

	(block-present grass_block-block1481)
	(at-x grass_block-block1482 position16)

	(at-y grass_block-block1482 position3)

	(at-z grass_block-block1482 position-14)

	(block-present grass_block-block1482)
	(at-x grass_block-block1483 position16)

	(at-y grass_block-block1483 position3)

	(at-z grass_block-block1483 position-13)

	(block-present grass_block-block1483)
	(at-x grass_block-block1484 position16)

	(at-y grass_block-block1484 position3)

	(at-z grass_block-block1484 position-12)

	(block-present grass_block-block1484)
	(at-x grass_block-block1485 position16)

	(at-y grass_block-block1485 position3)

	(at-z grass_block-block1485 position-11)

	(block-present grass_block-block1485)
	(at-x grass_block-block1486 position16)

	(at-y grass_block-block1486 position3)

	(at-z grass_block-block1486 position-10)

	(block-present grass_block-block1486)
	(at-x grass_block-block1487 position16)

	(at-y grass_block-block1487 position3)

	(at-z grass_block-block1487 position-9)

	(block-present grass_block-block1487)
	(at-x grass_block-block1488 position16)

	(at-y grass_block-block1488 position3)

	(at-z grass_block-block1488 position-8)

	(block-present grass_block-block1488)
	(at-x grass_block-block1489 position16)

	(at-y grass_block-block1489 position3)

	(at-z grass_block-block1489 position-7)

	(block-present grass_block-block1489)
	(at-x grass_block-block1490 position16)

	(at-y grass_block-block1490 position3)

	(at-z grass_block-block1490 position-6)

	(block-present grass_block-block1490)
	(at-x grass_block-block1491 position16)

	(at-y grass_block-block1491 position3)

	(at-z grass_block-block1491 position-5)

	(block-present grass_block-block1491)
	(at-x grass_block-block1492 position16)

	(at-y grass_block-block1492 position3)

	(at-z grass_block-block1492 position-4)

	(block-present grass_block-block1492)
	(at-x grass_block-block1493 position16)

	(at-y grass_block-block1493 position3)

	(at-z grass_block-block1493 position-3)

	(block-present grass_block-block1493)
	(at-x grass_block-block1494 position16)

	(at-y grass_block-block1494 position3)

	(at-z grass_block-block1494 position-2)

	(block-present grass_block-block1494)
	(at-x grass_block-block1495 position16)

	(at-y grass_block-block1495 position3)

	(at-z grass_block-block1495 position-1)

	(block-present grass_block-block1495)
	(at-x grass_block-block1496 position16)

	(at-y grass_block-block1496 position3)

	(at-z grass_block-block1496 position0)

	(block-present grass_block-block1496)
	(at-x grass_block-block1497 position16)

	(at-y grass_block-block1497 position3)

	(at-z grass_block-block1497 position1)

	(block-present grass_block-block1497)
	(at-x grass_block-block1498 position16)

	(at-y grass_block-block1498 position3)

	(at-z grass_block-block1498 position2)

	(block-present grass_block-block1498)
	(at-x grass_block-block1499 position16)

	(at-y grass_block-block1499 position3)

	(at-z grass_block-block1499 position3)

	(block-present grass_block-block1499)
	(at-x grass_block-block1500 position16)

	(at-y grass_block-block1500 position3)

	(at-z grass_block-block1500 position4)

	(block-present grass_block-block1500)
	(at-x grass_block-block1501 position16)

	(at-y grass_block-block1501 position3)

	(at-z grass_block-block1501 position5)

	(block-present grass_block-block1501)
	(at-x grass_block-block1502 position16)

	(at-y grass_block-block1502 position3)

	(at-z grass_block-block1502 position6)

	(block-present grass_block-block1502)
	(at-x grass_block-block1503 position16)

	(at-y grass_block-block1503 position3)

	(at-z grass_block-block1503 position7)

	(block-present grass_block-block1503)
	(at-x grass_block-block1504 position16)

	(at-y grass_block-block1504 position3)

	(at-z grass_block-block1504 position8)

	(block-present grass_block-block1504)
	(at-x grass_block-block1505 position16)

	(at-y grass_block-block1505 position3)

	(at-z grass_block-block1505 position9)

	(block-present grass_block-block1505)
	(at-x grass_block-block1506 position16)

	(at-y grass_block-block1506 position3)

	(at-z grass_block-block1506 position10)

	(block-present grass_block-block1506)
	(at-x grass_block-block1507 position16)

	(at-y grass_block-block1507 position3)

	(at-z grass_block-block1507 position11)

	(block-present grass_block-block1507)
	(at-x grass_block-block1508 position16)

	(at-y grass_block-block1508 position3)

	(at-z grass_block-block1508 position12)

	(block-present grass_block-block1508)
	(at-x grass_block-block1509 position16)

	(at-y grass_block-block1509 position3)

	(at-z grass_block-block1509 position13)

	(block-present grass_block-block1509)
	(at-x grass_block-block1510 position16)

	(at-y grass_block-block1510 position3)

	(at-z grass_block-block1510 position14)

	(block-present grass_block-block1510)
	(at-x grass_block-block1511 position16)

	(at-y grass_block-block1511 position3)

	(at-z grass_block-block1511 position15)

	(block-present grass_block-block1511)
	(at-x grass_block-block1512 position16)

	(at-y grass_block-block1512 position3)

	(at-z grass_block-block1512 position16)

	(block-present grass_block-block1512)
	(at-x grass_block-block1513 position16)

	(at-y grass_block-block1513 position3)

	(at-z grass_block-block1513 position17)

	(block-present grass_block-block1513)
	(at-x grass_block-block1514 position16)

	(at-y grass_block-block1514 position3)

	(at-z grass_block-block1514 position18)

	(block-present grass_block-block1514)
	(at-x grass_block-block1515 position16)

	(at-y grass_block-block1515 position3)

	(at-z grass_block-block1515 position19)

	(block-present grass_block-block1515)
	(at-x grass_block-block1516 position16)

	(at-y grass_block-block1516 position3)

	(at-z grass_block-block1516 position20)

	(block-present grass_block-block1516)
	(at-x grass_block-block1517 position17)

	(at-y grass_block-block1517 position3)

	(at-z grass_block-block1517 position-20)

	(block-present grass_block-block1517)
	(at-x grass_block-block1518 position17)

	(at-y grass_block-block1518 position3)

	(at-z grass_block-block1518 position-19)

	(block-present grass_block-block1518)
	(at-x grass_block-block1519 position17)

	(at-y grass_block-block1519 position3)

	(at-z grass_block-block1519 position-18)

	(block-present grass_block-block1519)
	(at-x grass_block-block1520 position17)

	(at-y grass_block-block1520 position3)

	(at-z grass_block-block1520 position-17)

	(block-present grass_block-block1520)
	(at-x grass_block-block1521 position17)

	(at-y grass_block-block1521 position3)

	(at-z grass_block-block1521 position-16)

	(block-present grass_block-block1521)
	(at-x grass_block-block1522 position17)

	(at-y grass_block-block1522 position3)

	(at-z grass_block-block1522 position-15)

	(block-present grass_block-block1522)
	(at-x grass_block-block1523 position17)

	(at-y grass_block-block1523 position3)

	(at-z grass_block-block1523 position-14)

	(block-present grass_block-block1523)
	(at-x grass_block-block1524 position17)

	(at-y grass_block-block1524 position3)

	(at-z grass_block-block1524 position-13)

	(block-present grass_block-block1524)
	(at-x grass_block-block1525 position17)

	(at-y grass_block-block1525 position3)

	(at-z grass_block-block1525 position-12)

	(block-present grass_block-block1525)
	(at-x grass_block-block1526 position17)

	(at-y grass_block-block1526 position3)

	(at-z grass_block-block1526 position-11)

	(block-present grass_block-block1526)
	(at-x grass_block-block1527 position17)

	(at-y grass_block-block1527 position3)

	(at-z grass_block-block1527 position-10)

	(block-present grass_block-block1527)
	(at-x grass_block-block1528 position17)

	(at-y grass_block-block1528 position3)

	(at-z grass_block-block1528 position-9)

	(block-present grass_block-block1528)
	(at-x grass_block-block1529 position17)

	(at-y grass_block-block1529 position3)

	(at-z grass_block-block1529 position-8)

	(block-present grass_block-block1529)
	(at-x grass_block-block1530 position17)

	(at-y grass_block-block1530 position3)

	(at-z grass_block-block1530 position-7)

	(block-present grass_block-block1530)
	(at-x grass_block-block1531 position17)

	(at-y grass_block-block1531 position3)

	(at-z grass_block-block1531 position-6)

	(block-present grass_block-block1531)
	(at-x grass_block-block1532 position17)

	(at-y grass_block-block1532 position3)

	(at-z grass_block-block1532 position-5)

	(block-present grass_block-block1532)
	(at-x grass_block-block1533 position17)

	(at-y grass_block-block1533 position3)

	(at-z grass_block-block1533 position-4)

	(block-present grass_block-block1533)
	(at-x grass_block-block1534 position17)

	(at-y grass_block-block1534 position3)

	(at-z grass_block-block1534 position-3)

	(block-present grass_block-block1534)
	(at-x grass_block-block1535 position17)

	(at-y grass_block-block1535 position3)

	(at-z grass_block-block1535 position-2)

	(block-present grass_block-block1535)
	(at-x grass_block-block1536 position17)

	(at-y grass_block-block1536 position3)

	(at-z grass_block-block1536 position-1)

	(block-present grass_block-block1536)
	(at-x grass_block-block1537 position17)

	(at-y grass_block-block1537 position3)

	(at-z grass_block-block1537 position0)

	(block-present grass_block-block1537)
	(at-x grass_block-block1538 position17)

	(at-y grass_block-block1538 position3)

	(at-z grass_block-block1538 position1)

	(block-present grass_block-block1538)
	(at-x grass_block-block1539 position17)

	(at-y grass_block-block1539 position3)

	(at-z grass_block-block1539 position2)

	(block-present grass_block-block1539)
	(at-x grass_block-block1540 position17)

	(at-y grass_block-block1540 position3)

	(at-z grass_block-block1540 position3)

	(block-present grass_block-block1540)
	(at-x grass_block-block1541 position17)

	(at-y grass_block-block1541 position3)

	(at-z grass_block-block1541 position4)

	(block-present grass_block-block1541)
	(at-x grass_block-block1542 position17)

	(at-y grass_block-block1542 position3)

	(at-z grass_block-block1542 position5)

	(block-present grass_block-block1542)
	(at-x grass_block-block1543 position17)

	(at-y grass_block-block1543 position3)

	(at-z grass_block-block1543 position6)

	(block-present grass_block-block1543)
	(at-x grass_block-block1544 position17)

	(at-y grass_block-block1544 position3)

	(at-z grass_block-block1544 position7)

	(block-present grass_block-block1544)
	(at-x grass_block-block1545 position17)

	(at-y grass_block-block1545 position3)

	(at-z grass_block-block1545 position8)

	(block-present grass_block-block1545)
	(at-x grass_block-block1546 position17)

	(at-y grass_block-block1546 position3)

	(at-z grass_block-block1546 position9)

	(block-present grass_block-block1546)
	(at-x grass_block-block1547 position17)

	(at-y grass_block-block1547 position3)

	(at-z grass_block-block1547 position10)

	(block-present grass_block-block1547)
	(at-x grass_block-block1548 position17)

	(at-y grass_block-block1548 position3)

	(at-z grass_block-block1548 position11)

	(block-present grass_block-block1548)
	(at-x grass_block-block1549 position17)

	(at-y grass_block-block1549 position3)

	(at-z grass_block-block1549 position12)

	(block-present grass_block-block1549)
	(at-x grass_block-block1550 position17)

	(at-y grass_block-block1550 position3)

	(at-z grass_block-block1550 position13)

	(block-present grass_block-block1550)
	(at-x grass_block-block1551 position17)

	(at-y grass_block-block1551 position3)

	(at-z grass_block-block1551 position14)

	(block-present grass_block-block1551)
	(at-x grass_block-block1552 position17)

	(at-y grass_block-block1552 position3)

	(at-z grass_block-block1552 position15)

	(block-present grass_block-block1552)
	(at-x grass_block-block1553 position17)

	(at-y grass_block-block1553 position3)

	(at-z grass_block-block1553 position16)

	(block-present grass_block-block1553)
	(at-x grass_block-block1554 position17)

	(at-y grass_block-block1554 position3)

	(at-z grass_block-block1554 position17)

	(block-present grass_block-block1554)
	(at-x grass_block-block1555 position17)

	(at-y grass_block-block1555 position3)

	(at-z grass_block-block1555 position18)

	(block-present grass_block-block1555)
	(at-x grass_block-block1556 position17)

	(at-y grass_block-block1556 position3)

	(at-z grass_block-block1556 position19)

	(block-present grass_block-block1556)
	(at-x grass_block-block1557 position17)

	(at-y grass_block-block1557 position3)

	(at-z grass_block-block1557 position20)

	(block-present grass_block-block1557)
	(at-x grass_block-block1558 position18)

	(at-y grass_block-block1558 position3)

	(at-z grass_block-block1558 position-20)

	(block-present grass_block-block1558)
	(at-x grass_block-block1559 position18)

	(at-y grass_block-block1559 position3)

	(at-z grass_block-block1559 position-19)

	(block-present grass_block-block1559)
	(at-x grass_block-block1560 position18)

	(at-y grass_block-block1560 position3)

	(at-z grass_block-block1560 position-18)

	(block-present grass_block-block1560)
	(at-x grass_block-block1561 position18)

	(at-y grass_block-block1561 position3)

	(at-z grass_block-block1561 position-17)

	(block-present grass_block-block1561)
	(at-x grass_block-block1562 position18)

	(at-y grass_block-block1562 position3)

	(at-z grass_block-block1562 position-16)

	(block-present grass_block-block1562)
	(at-x grass_block-block1563 position18)

	(at-y grass_block-block1563 position3)

	(at-z grass_block-block1563 position-15)

	(block-present grass_block-block1563)
	(at-x grass_block-block1564 position18)

	(at-y grass_block-block1564 position3)

	(at-z grass_block-block1564 position-14)

	(block-present grass_block-block1564)
	(at-x grass_block-block1565 position18)

	(at-y grass_block-block1565 position3)

	(at-z grass_block-block1565 position-13)

	(block-present grass_block-block1565)
	(at-x grass_block-block1566 position18)

	(at-y grass_block-block1566 position3)

	(at-z grass_block-block1566 position-12)

	(block-present grass_block-block1566)
	(at-x grass_block-block1567 position18)

	(at-y grass_block-block1567 position3)

	(at-z grass_block-block1567 position-11)

	(block-present grass_block-block1567)
	(at-x grass_block-block1568 position18)

	(at-y grass_block-block1568 position3)

	(at-z grass_block-block1568 position-10)

	(block-present grass_block-block1568)
	(at-x grass_block-block1569 position18)

	(at-y grass_block-block1569 position3)

	(at-z grass_block-block1569 position-9)

	(block-present grass_block-block1569)
	(at-x grass_block-block1570 position18)

	(at-y grass_block-block1570 position3)

	(at-z grass_block-block1570 position-8)

	(block-present grass_block-block1570)
	(at-x grass_block-block1571 position18)

	(at-y grass_block-block1571 position3)

	(at-z grass_block-block1571 position-7)

	(block-present grass_block-block1571)
	(at-x grass_block-block1572 position18)

	(at-y grass_block-block1572 position3)

	(at-z grass_block-block1572 position-6)

	(block-present grass_block-block1572)
	(at-x grass_block-block1573 position18)

	(at-y grass_block-block1573 position3)

	(at-z grass_block-block1573 position-5)

	(block-present grass_block-block1573)
	(at-x grass_block-block1574 position18)

	(at-y grass_block-block1574 position3)

	(at-z grass_block-block1574 position-4)

	(block-present grass_block-block1574)
	(at-x grass_block-block1575 position18)

	(at-y grass_block-block1575 position3)

	(at-z grass_block-block1575 position-3)

	(block-present grass_block-block1575)
	(at-x grass_block-block1576 position18)

	(at-y grass_block-block1576 position3)

	(at-z grass_block-block1576 position-2)

	(block-present grass_block-block1576)
	(at-x grass_block-block1577 position18)

	(at-y grass_block-block1577 position3)

	(at-z grass_block-block1577 position-1)

	(block-present grass_block-block1577)
	(at-x grass_block-block1578 position18)

	(at-y grass_block-block1578 position3)

	(at-z grass_block-block1578 position0)

	(block-present grass_block-block1578)
	(at-x grass_block-block1579 position18)

	(at-y grass_block-block1579 position3)

	(at-z grass_block-block1579 position1)

	(block-present grass_block-block1579)
	(at-x grass_block-block1580 position18)

	(at-y grass_block-block1580 position3)

	(at-z grass_block-block1580 position2)

	(block-present grass_block-block1580)
	(at-x grass_block-block1581 position18)

	(at-y grass_block-block1581 position3)

	(at-z grass_block-block1581 position3)

	(block-present grass_block-block1581)
	(at-x grass_block-block1582 position18)

	(at-y grass_block-block1582 position3)

	(at-z grass_block-block1582 position4)

	(block-present grass_block-block1582)
	(at-x grass_block-block1583 position18)

	(at-y grass_block-block1583 position3)

	(at-z grass_block-block1583 position5)

	(block-present grass_block-block1583)
	(at-x grass_block-block1584 position18)

	(at-y grass_block-block1584 position3)

	(at-z grass_block-block1584 position6)

	(block-present grass_block-block1584)
	(at-x grass_block-block1585 position18)

	(at-y grass_block-block1585 position3)

	(at-z grass_block-block1585 position7)

	(block-present grass_block-block1585)
	(at-x grass_block-block1586 position18)

	(at-y grass_block-block1586 position3)

	(at-z grass_block-block1586 position8)

	(block-present grass_block-block1586)
	(at-x grass_block-block1587 position18)

	(at-y grass_block-block1587 position3)

	(at-z grass_block-block1587 position9)

	(block-present grass_block-block1587)
	(at-x grass_block-block1588 position18)

	(at-y grass_block-block1588 position3)

	(at-z grass_block-block1588 position10)

	(block-present grass_block-block1588)
	(at-x grass_block-block1589 position18)

	(at-y grass_block-block1589 position3)

	(at-z grass_block-block1589 position11)

	(block-present grass_block-block1589)
	(at-x grass_block-block1590 position18)

	(at-y grass_block-block1590 position3)

	(at-z grass_block-block1590 position12)

	(block-present grass_block-block1590)
	(at-x grass_block-block1591 position18)

	(at-y grass_block-block1591 position3)

	(at-z grass_block-block1591 position13)

	(block-present grass_block-block1591)
	(at-x grass_block-block1592 position18)

	(at-y grass_block-block1592 position3)

	(at-z grass_block-block1592 position14)

	(block-present grass_block-block1592)
	(at-x grass_block-block1593 position18)

	(at-y grass_block-block1593 position3)

	(at-z grass_block-block1593 position15)

	(block-present grass_block-block1593)
	(at-x grass_block-block1594 position18)

	(at-y grass_block-block1594 position3)

	(at-z grass_block-block1594 position16)

	(block-present grass_block-block1594)
	(at-x grass_block-block1595 position18)

	(at-y grass_block-block1595 position3)

	(at-z grass_block-block1595 position17)

	(block-present grass_block-block1595)
	(at-x grass_block-block1596 position18)

	(at-y grass_block-block1596 position3)

	(at-z grass_block-block1596 position18)

	(block-present grass_block-block1596)
	(at-x grass_block-block1597 position18)

	(at-y grass_block-block1597 position3)

	(at-z grass_block-block1597 position19)

	(block-present grass_block-block1597)
	(at-x grass_block-block1598 position18)

	(at-y grass_block-block1598 position3)

	(at-z grass_block-block1598 position20)

	(block-present grass_block-block1598)
	(at-x grass_block-block1599 position19)

	(at-y grass_block-block1599 position3)

	(at-z grass_block-block1599 position-20)

	(block-present grass_block-block1599)
	(at-x grass_block-block1600 position19)

	(at-y grass_block-block1600 position3)

	(at-z grass_block-block1600 position-19)

	(block-present grass_block-block1600)
	(at-x grass_block-block1601 position19)

	(at-y grass_block-block1601 position3)

	(at-z grass_block-block1601 position-18)

	(block-present grass_block-block1601)
	(at-x grass_block-block1602 position19)

	(at-y grass_block-block1602 position3)

	(at-z grass_block-block1602 position-17)

	(block-present grass_block-block1602)
	(at-x grass_block-block1603 position19)

	(at-y grass_block-block1603 position3)

	(at-z grass_block-block1603 position-16)

	(block-present grass_block-block1603)
	(at-x grass_block-block1604 position19)

	(at-y grass_block-block1604 position3)

	(at-z grass_block-block1604 position-15)

	(block-present grass_block-block1604)
	(at-x grass_block-block1605 position19)

	(at-y grass_block-block1605 position3)

	(at-z grass_block-block1605 position-14)

	(block-present grass_block-block1605)
	(at-x grass_block-block1606 position19)

	(at-y grass_block-block1606 position3)

	(at-z grass_block-block1606 position-13)

	(block-present grass_block-block1606)
	(at-x grass_block-block1607 position19)

	(at-y grass_block-block1607 position3)

	(at-z grass_block-block1607 position-12)

	(block-present grass_block-block1607)
	(at-x grass_block-block1608 position19)

	(at-y grass_block-block1608 position3)

	(at-z grass_block-block1608 position-11)

	(block-present grass_block-block1608)
	(at-x grass_block-block1609 position19)

	(at-y grass_block-block1609 position3)

	(at-z grass_block-block1609 position-10)

	(block-present grass_block-block1609)
	(at-x grass_block-block1610 position19)

	(at-y grass_block-block1610 position3)

	(at-z grass_block-block1610 position-9)

	(block-present grass_block-block1610)
	(at-x grass_block-block1611 position19)

	(at-y grass_block-block1611 position3)

	(at-z grass_block-block1611 position-8)

	(block-present grass_block-block1611)
	(at-x grass_block-block1612 position19)

	(at-y grass_block-block1612 position3)

	(at-z grass_block-block1612 position-7)

	(block-present grass_block-block1612)
	(at-x grass_block-block1613 position19)

	(at-y grass_block-block1613 position3)

	(at-z grass_block-block1613 position-6)

	(block-present grass_block-block1613)
	(at-x grass_block-block1614 position19)

	(at-y grass_block-block1614 position3)

	(at-z grass_block-block1614 position-5)

	(block-present grass_block-block1614)
	(at-x grass_block-block1615 position19)

	(at-y grass_block-block1615 position3)

	(at-z grass_block-block1615 position-4)

	(block-present grass_block-block1615)
	(at-x grass_block-block1616 position19)

	(at-y grass_block-block1616 position3)

	(at-z grass_block-block1616 position-3)

	(block-present grass_block-block1616)
	(at-x grass_block-block1617 position19)

	(at-y grass_block-block1617 position3)

	(at-z grass_block-block1617 position-2)

	(block-present grass_block-block1617)
	(at-x grass_block-block1618 position19)

	(at-y grass_block-block1618 position3)

	(at-z grass_block-block1618 position-1)

	(block-present grass_block-block1618)
	(at-x grass_block-block1619 position19)

	(at-y grass_block-block1619 position3)

	(at-z grass_block-block1619 position0)

	(block-present grass_block-block1619)
	(at-x grass_block-block1620 position19)

	(at-y grass_block-block1620 position3)

	(at-z grass_block-block1620 position1)

	(block-present grass_block-block1620)
	(at-x grass_block-block1621 position19)

	(at-y grass_block-block1621 position3)

	(at-z grass_block-block1621 position2)

	(block-present grass_block-block1621)
	(at-x grass_block-block1622 position19)

	(at-y grass_block-block1622 position3)

	(at-z grass_block-block1622 position3)

	(block-present grass_block-block1622)
	(at-x grass_block-block1623 position19)

	(at-y grass_block-block1623 position3)

	(at-z grass_block-block1623 position4)

	(block-present grass_block-block1623)
	(at-x grass_block-block1624 position19)

	(at-y grass_block-block1624 position3)

	(at-z grass_block-block1624 position5)

	(block-present grass_block-block1624)
	(at-x grass_block-block1625 position19)

	(at-y grass_block-block1625 position3)

	(at-z grass_block-block1625 position6)

	(block-present grass_block-block1625)
	(at-x grass_block-block1626 position19)

	(at-y grass_block-block1626 position3)

	(at-z grass_block-block1626 position7)

	(block-present grass_block-block1626)
	(at-x grass_block-block1627 position19)

	(at-y grass_block-block1627 position3)

	(at-z grass_block-block1627 position8)

	(block-present grass_block-block1627)
	(at-x grass_block-block1628 position19)

	(at-y grass_block-block1628 position3)

	(at-z grass_block-block1628 position9)

	(block-present grass_block-block1628)
	(at-x grass_block-block1629 position19)

	(at-y grass_block-block1629 position3)

	(at-z grass_block-block1629 position10)

	(block-present grass_block-block1629)
	(at-x grass_block-block1630 position19)

	(at-y grass_block-block1630 position3)

	(at-z grass_block-block1630 position11)

	(block-present grass_block-block1630)
	(at-x grass_block-block1631 position19)

	(at-y grass_block-block1631 position3)

	(at-z grass_block-block1631 position12)

	(block-present grass_block-block1631)
	(at-x grass_block-block1632 position19)

	(at-y grass_block-block1632 position3)

	(at-z grass_block-block1632 position13)

	(block-present grass_block-block1632)
	(at-x grass_block-block1633 position19)

	(at-y grass_block-block1633 position3)

	(at-z grass_block-block1633 position14)

	(block-present grass_block-block1633)
	(at-x grass_block-block1634 position19)

	(at-y grass_block-block1634 position3)

	(at-z grass_block-block1634 position15)

	(block-present grass_block-block1634)
	(at-x grass_block-block1635 position19)

	(at-y grass_block-block1635 position3)

	(at-z grass_block-block1635 position16)

	(block-present grass_block-block1635)
	(at-x grass_block-block1636 position19)

	(at-y grass_block-block1636 position3)

	(at-z grass_block-block1636 position17)

	(block-present grass_block-block1636)
	(at-x grass_block-block1637 position19)

	(at-y grass_block-block1637 position3)

	(at-z grass_block-block1637 position18)

	(block-present grass_block-block1637)
	(at-x grass_block-block1638 position19)

	(at-y grass_block-block1638 position3)

	(at-z grass_block-block1638 position19)

	(block-present grass_block-block1638)
	(at-x grass_block-block1639 position19)

	(at-y grass_block-block1639 position3)

	(at-z grass_block-block1639 position20)

	(block-present grass_block-block1639)
	(at-x grass_block-block1640 position20)

	(at-y grass_block-block1640 position3)

	(at-z grass_block-block1640 position-20)

	(block-present grass_block-block1640)
	(at-x grass_block-block1641 position20)

	(at-y grass_block-block1641 position3)

	(at-z grass_block-block1641 position-19)

	(block-present grass_block-block1641)
	(at-x grass_block-block1642 position20)

	(at-y grass_block-block1642 position3)

	(at-z grass_block-block1642 position-18)

	(block-present grass_block-block1642)
	(at-x grass_block-block1643 position20)

	(at-y grass_block-block1643 position3)

	(at-z grass_block-block1643 position-17)

	(block-present grass_block-block1643)
	(at-x grass_block-block1644 position20)

	(at-y grass_block-block1644 position3)

	(at-z grass_block-block1644 position-16)

	(block-present grass_block-block1644)
	(at-x grass_block-block1645 position20)

	(at-y grass_block-block1645 position3)

	(at-z grass_block-block1645 position-15)

	(block-present grass_block-block1645)
	(at-x grass_block-block1646 position20)

	(at-y grass_block-block1646 position3)

	(at-z grass_block-block1646 position-14)

	(block-present grass_block-block1646)
	(at-x grass_block-block1647 position20)

	(at-y grass_block-block1647 position3)

	(at-z grass_block-block1647 position-13)

	(block-present grass_block-block1647)
	(at-x grass_block-block1648 position20)

	(at-y grass_block-block1648 position3)

	(at-z grass_block-block1648 position-12)

	(block-present grass_block-block1648)
	(at-x grass_block-block1649 position20)

	(at-y grass_block-block1649 position3)

	(at-z grass_block-block1649 position-11)

	(block-present grass_block-block1649)
	(at-x grass_block-block1650 position20)

	(at-y grass_block-block1650 position3)

	(at-z grass_block-block1650 position-10)

	(block-present grass_block-block1650)
	(at-x grass_block-block1651 position20)

	(at-y grass_block-block1651 position3)

	(at-z grass_block-block1651 position-9)

	(block-present grass_block-block1651)
	(at-x grass_block-block1652 position20)

	(at-y grass_block-block1652 position3)

	(at-z grass_block-block1652 position-8)

	(block-present grass_block-block1652)
	(at-x grass_block-block1653 position20)

	(at-y grass_block-block1653 position3)

	(at-z grass_block-block1653 position-7)

	(block-present grass_block-block1653)
	(at-x grass_block-block1654 position20)

	(at-y grass_block-block1654 position3)

	(at-z grass_block-block1654 position-6)

	(block-present grass_block-block1654)
	(at-x grass_block-block1655 position20)

	(at-y grass_block-block1655 position3)

	(at-z grass_block-block1655 position-5)

	(block-present grass_block-block1655)
	(at-x grass_block-block1656 position20)

	(at-y grass_block-block1656 position3)

	(at-z grass_block-block1656 position-4)

	(block-present grass_block-block1656)
	(at-x grass_block-block1657 position20)

	(at-y grass_block-block1657 position3)

	(at-z grass_block-block1657 position-3)

	(block-present grass_block-block1657)
	(at-x grass_block-block1658 position20)

	(at-y grass_block-block1658 position3)

	(at-z grass_block-block1658 position-2)

	(block-present grass_block-block1658)
	(at-x grass_block-block1659 position20)

	(at-y grass_block-block1659 position3)

	(at-z grass_block-block1659 position-1)

	(block-present grass_block-block1659)
	(at-x grass_block-block1660 position20)

	(at-y grass_block-block1660 position3)

	(at-z grass_block-block1660 position0)

	(block-present grass_block-block1660)
	(at-x grass_block-block1661 position20)

	(at-y grass_block-block1661 position3)

	(at-z grass_block-block1661 position1)

	(block-present grass_block-block1661)
	(at-x grass_block-block1662 position20)

	(at-y grass_block-block1662 position3)

	(at-z grass_block-block1662 position2)

	(block-present grass_block-block1662)
	(at-x grass_block-block1663 position20)

	(at-y grass_block-block1663 position3)

	(at-z grass_block-block1663 position3)

	(block-present grass_block-block1663)
	(at-x grass_block-block1664 position20)

	(at-y grass_block-block1664 position3)

	(at-z grass_block-block1664 position4)

	(block-present grass_block-block1664)
	(at-x grass_block-block1665 position20)

	(at-y grass_block-block1665 position3)

	(at-z grass_block-block1665 position5)

	(block-present grass_block-block1665)
	(at-x grass_block-block1666 position20)

	(at-y grass_block-block1666 position3)

	(at-z grass_block-block1666 position6)

	(block-present grass_block-block1666)
	(at-x grass_block-block1667 position20)

	(at-y grass_block-block1667 position3)

	(at-z grass_block-block1667 position7)

	(block-present grass_block-block1667)
	(at-x grass_block-block1668 position20)

	(at-y grass_block-block1668 position3)

	(at-z grass_block-block1668 position8)

	(block-present grass_block-block1668)
	(at-x grass_block-block1669 position20)

	(at-y grass_block-block1669 position3)

	(at-z grass_block-block1669 position9)

	(block-present grass_block-block1669)
	(at-x grass_block-block1670 position20)

	(at-y grass_block-block1670 position3)

	(at-z grass_block-block1670 position10)

	(block-present grass_block-block1670)
	(at-x grass_block-block1671 position20)

	(at-y grass_block-block1671 position3)

	(at-z grass_block-block1671 position11)

	(block-present grass_block-block1671)
	(at-x grass_block-block1672 position20)

	(at-y grass_block-block1672 position3)

	(at-z grass_block-block1672 position12)

	(block-present grass_block-block1672)
	(at-x grass_block-block1673 position20)

	(at-y grass_block-block1673 position3)

	(at-z grass_block-block1673 position13)

	(block-present grass_block-block1673)
	(at-x grass_block-block1674 position20)

	(at-y grass_block-block1674 position3)

	(at-z grass_block-block1674 position14)

	(block-present grass_block-block1674)
	(at-x grass_block-block1675 position20)

	(at-y grass_block-block1675 position3)

	(at-z grass_block-block1675 position15)

	(block-present grass_block-block1675)
	(at-x grass_block-block1676 position20)

	(at-y grass_block-block1676 position3)

	(at-z grass_block-block1676 position16)

	(block-present grass_block-block1676)
	(at-x grass_block-block1677 position20)

	(at-y grass_block-block1677 position3)

	(at-z grass_block-block1677 position17)

	(block-present grass_block-block1677)
	(at-x grass_block-block1678 position20)

	(at-y grass_block-block1678 position3)

	(at-z grass_block-block1678 position18)

	(block-present grass_block-block1678)
	(at-x grass_block-block1679 position20)

	(at-y grass_block-block1679 position3)

	(at-z grass_block-block1679 position19)

	(block-present grass_block-block1679)
	(at-x grass_block-block1680 position20)

	(at-y grass_block-block1680 position3)

	(at-z grass_block-block1680 position20)

	(block-present grass_block-block1680)
	(at-x leaves-block0 position-3)

	(at-y leaves-block0 position7)

	(at-z leaves-block0 position4)

	(block-present leaves-block0)
	(at-x leaves-block1 position-3)

	(at-y leaves-block1 position7)

	(at-z leaves-block1 position5)

	(block-present leaves-block1)
	(at-x leaves-block2 position-3)

	(at-y leaves-block2 position7)

	(at-z leaves-block2 position6)

	(block-present leaves-block2)
	(at-x leaves-block3 position-3)

	(at-y leaves-block3 position9)

	(at-z leaves-block3 position4)

	(block-present leaves-block3)
	(at-x leaves-block4 position-3)

	(at-y leaves-block4 position9)

	(at-z leaves-block4 position5)

	(block-present leaves-block4)
	(at-x leaves-block5 position-3)

	(at-y leaves-block5 position9)

	(at-z leaves-block5 position6)

	(block-present leaves-block5)
	(at-x leaves-block6 position-2)

	(at-y leaves-block6 position6)

	(at-z leaves-block6 position5)

	(block-present leaves-block6)
	(at-x leaves-block7 position-2)

	(at-y leaves-block7 position7)

	(at-z leaves-block7 position3)

	(block-present leaves-block7)
	(at-x leaves-block8 position-2)

	(at-y leaves-block8 position7)

	(at-z leaves-block8 position4)

	(block-present leaves-block8)
	(at-x leaves-block9 position-2)

	(at-y leaves-block9 position7)

	(at-z leaves-block9 position5)

	(block-present leaves-block9)
	(at-x leaves-block10 position-2)

	(at-y leaves-block10 position7)

	(at-z leaves-block10 position6)

	(block-present leaves-block10)
	(at-x leaves-block11 position-2)

	(at-y leaves-block11 position7)

	(at-z leaves-block11 position7)

	(block-present leaves-block11)
	(at-x leaves-block12 position-2)

	(at-y leaves-block12 position8)

	(at-z leaves-block12 position5)

	(block-present leaves-block12)
	(at-x leaves-block13 position-2)

	(at-y leaves-block13 position9)

	(at-z leaves-block13 position3)

	(block-present leaves-block13)
	(at-x leaves-block14 position-2)

	(at-y leaves-block14 position9)

	(at-z leaves-block14 position4)

	(block-present leaves-block14)
	(at-x leaves-block15 position-2)

	(at-y leaves-block15 position9)

	(at-z leaves-block15 position5)

	(block-present leaves-block15)
	(at-x leaves-block16 position-2)

	(at-y leaves-block16 position9)

	(at-z leaves-block16 position6)

	(block-present leaves-block16)
	(at-x leaves-block17 position-2)

	(at-y leaves-block17 position9)

	(at-z leaves-block17 position7)

	(block-present leaves-block17)
	(at-x leaves-block18 position-2)

	(at-y leaves-block18 position10)

	(at-z leaves-block18 position4)

	(block-present leaves-block18)
	(at-x leaves-block19 position-2)

	(at-y leaves-block19 position10)

	(at-z leaves-block19 position5)

	(block-present leaves-block19)
	(at-x leaves-block20 position-2)

	(at-y leaves-block20 position10)

	(at-z leaves-block20 position6)

	(block-present leaves-block20)
	(at-x leaves-block21 position-2)

	(at-y leaves-block21 position11)

	(at-z leaves-block21 position5)

	(block-present leaves-block21)
	(at-x leaves-block22 position-2)

	(at-y leaves-block22 position13)

	(at-z leaves-block22 position5)

	(block-present leaves-block22)
	(at-x leaves-block23 position-1)

	(at-y leaves-block23 position6)

	(at-z leaves-block23 position4)

	(block-present leaves-block23)
	(at-x leaves-block24 position-1)

	(at-y leaves-block24 position6)

	(at-z leaves-block24 position6)

	(block-present leaves-block24)
	(at-x leaves-block25 position-1)

	(at-y leaves-block25 position7)

	(at-z leaves-block25 position3)

	(block-present leaves-block25)
	(at-x leaves-block26 position-1)

	(at-y leaves-block26 position7)

	(at-z leaves-block26 position4)

	(block-present leaves-block26)
	(at-x leaves-block27 position-1)

	(at-y leaves-block27 position7)

	(at-z leaves-block27 position6)

	(block-present leaves-block27)
	(at-x leaves-block28 position-1)

	(at-y leaves-block28 position7)

	(at-z leaves-block28 position7)

	(block-present leaves-block28)
	(at-x leaves-block29 position-1)

	(at-y leaves-block29 position8)

	(at-z leaves-block29 position4)

	(block-present leaves-block29)
	(at-x leaves-block30 position-1)

	(at-y leaves-block30 position8)

	(at-z leaves-block30 position6)

	(block-present leaves-block30)
	(at-x leaves-block31 position-1)

	(at-y leaves-block31 position9)

	(at-z leaves-block31 position3)

	(block-present leaves-block31)
	(at-x leaves-block32 position-1)

	(at-y leaves-block32 position9)

	(at-z leaves-block32 position4)

	(block-present leaves-block32)
	(at-x leaves-block33 position-1)

	(at-y leaves-block33 position9)

	(at-z leaves-block33 position6)

	(block-present leaves-block33)
	(at-x leaves-block34 position-1)

	(at-y leaves-block34 position9)

	(at-z leaves-block34 position7)

	(block-present leaves-block34)
	(at-x leaves-block35 position-1)

	(at-y leaves-block35 position10)

	(at-z leaves-block35 position4)

	(block-present leaves-block35)
	(at-x leaves-block36 position-1)

	(at-y leaves-block36 position10)

	(at-z leaves-block36 position6)

	(block-present leaves-block36)
	(at-x leaves-block37 position-1)

	(at-y leaves-block37 position11)

	(at-z leaves-block37 position4)

	(block-present leaves-block37)
	(at-x leaves-block38 position-1)

	(at-y leaves-block38 position11)

	(at-z leaves-block38 position6)

	(block-present leaves-block38)
	(at-x leaves-block39 position-1)

	(at-y leaves-block39 position13)

	(at-z leaves-block39 position4)

	(block-present leaves-block39)
	(at-x leaves-block40 position-1)

	(at-y leaves-block40 position13)

	(at-z leaves-block40 position6)

	(block-present leaves-block40)
	(at-x leaves-block41 position-1)

	(at-y leaves-block41 position14)

	(at-z leaves-block41 position5)

	(block-present leaves-block41)
	(at-x leaves-block42 position0)

	(at-y leaves-block42 position6)

	(at-z leaves-block42 position5)

	(block-present leaves-block42)
	(at-x leaves-block43 position0)

	(at-y leaves-block43 position7)

	(at-z leaves-block43 position3)

	(block-present leaves-block43)
	(at-x leaves-block44 position0)

	(at-y leaves-block44 position7)

	(at-z leaves-block44 position4)

	(block-present leaves-block44)
	(at-x leaves-block45 position0)

	(at-y leaves-block45 position7)

	(at-z leaves-block45 position5)

	(block-present leaves-block45)
	(at-x leaves-block46 position0)

	(at-y leaves-block46 position7)

	(at-z leaves-block46 position6)

	(block-present leaves-block46)
	(at-x leaves-block47 position0)

	(at-y leaves-block47 position7)

	(at-z leaves-block47 position7)

	(block-present leaves-block47)
	(at-x leaves-block48 position0)

	(at-y leaves-block48 position8)

	(at-z leaves-block48 position5)

	(block-present leaves-block48)
	(at-x leaves-block49 position0)

	(at-y leaves-block49 position9)

	(at-z leaves-block49 position3)

	(block-present leaves-block49)
	(at-x leaves-block50 position0)

	(at-y leaves-block50 position9)

	(at-z leaves-block50 position4)

	(block-present leaves-block50)
	(at-x leaves-block51 position0)

	(at-y leaves-block51 position9)

	(at-z leaves-block51 position5)

	(block-present leaves-block51)
	(at-x leaves-block52 position0)

	(at-y leaves-block52 position9)

	(at-z leaves-block52 position6)

	(block-present leaves-block52)
	(at-x leaves-block53 position0)

	(at-y leaves-block53 position9)

	(at-z leaves-block53 position7)

	(block-present leaves-block53)
	(at-x leaves-block54 position0)

	(at-y leaves-block54 position10)

	(at-z leaves-block54 position4)

	(block-present leaves-block54)
	(at-x leaves-block55 position0)

	(at-y leaves-block55 position10)

	(at-z leaves-block55 position5)

	(block-present leaves-block55)
	(at-x leaves-block56 position0)

	(at-y leaves-block56 position10)

	(at-z leaves-block56 position6)

	(block-present leaves-block56)
	(at-x leaves-block57 position0)

	(at-y leaves-block57 position11)

	(at-z leaves-block57 position5)

	(block-present leaves-block57)
	(at-x leaves-block58 position0)

	(at-y leaves-block58 position13)

	(at-z leaves-block58 position5)

	(block-present leaves-block58)
	(at-x leaves-block59 position1)

	(at-y leaves-block59 position7)

	(at-z leaves-block59 position4)

	(block-present leaves-block59)
	(at-x leaves-block60 position1)

	(at-y leaves-block60 position7)

	(at-z leaves-block60 position5)

	(block-present leaves-block60)
	(at-x leaves-block61 position1)

	(at-y leaves-block61 position7)

	(at-z leaves-block61 position6)

	(block-present leaves-block61)
	(at-x leaves-block62 position1)

	(at-y leaves-block62 position9)

	(at-z leaves-block62 position4)

	(block-present leaves-block62)
	(at-x leaves-block63 position1)

	(at-y leaves-block63 position9)

	(at-z leaves-block63 position5)

	(block-present leaves-block63)
	(at-x leaves-block64 position1)

	(at-y leaves-block64 position9)

	(at-z leaves-block64 position6)

	(block-present leaves-block64)
	(at-x log-block0 position-1)

	(at-y log-block0 position4)

	(at-z log-block0 position5)

	(block-present log-block0)
	(at-x log-block1 position-1)

	(at-y log-block1 position5)

	(at-z log-block1 position5)

	(block-present log-block1)
	(at-x log-block2 position-1)

	(at-y log-block2 position6)

	(at-z log-block2 position5)

	(block-present log-block2)
	(at-x log-block3 position-1)

	(at-y log-block3 position7)

	(at-z log-block3 position5)

	(block-present log-block3)
	(at-x log-block4 position-1)

	(at-y log-block4 position8)

	(at-z log-block4 position5)

	(block-present log-block4)
	(at-x log-block5 position-1)

	(at-y log-block5 position9)

	(at-z log-block5 position5)

	(block-present log-block5)
	(at-x log-block6 position-1)

	(at-y log-block6 position10)

	(at-z log-block6 position5)

	(block-present log-block6)
	(at-x log-block7 position-1)

	(at-y log-block7 position11)

	(at-z log-block7 position5)

	(block-present log-block7)
	(at-x log-block8 position-1)

	(at-y log-block8 position12)

	(at-z log-block8 position5)

	(block-present log-block8)
	(at-x log-block9 position-1)

	(at-y log-block9 position13)

	(at-z log-block9 position5)

	(block-present log-block9)
	(at-x cobblestone0 position0)

	(at-y cobblestone0 position4)

	(at-z cobblestone0 position0)

)
(:goal
	(and (goal-achieved steve))
		
)
)
