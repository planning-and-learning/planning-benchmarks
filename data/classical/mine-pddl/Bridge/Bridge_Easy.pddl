(define (problem Bridge_Easy_problem)
	(:domain Bridge_Easy)

(:init
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
	(agent-has-n-planks steve count64)

	(agent-has-n-cobblestone steve count64)

	(agent-has-n-grass_block steve count0)

	(agent-has-n-water steve count0)

	(at-x grass_block-block0 position-6)

	(at-y grass_block-block0 position3)

	(at-z grass_block-block0 position-6)

	(block-present grass_block-block0)
	(at-x grass_block-block1 position-6)

	(at-y grass_block-block1 position3)

	(at-z grass_block-block1 position-5)

	(block-present grass_block-block1)
	(at-x grass_block-block2 position-6)

	(at-y grass_block-block2 position3)

	(at-z grass_block-block2 position-4)

	(block-present grass_block-block2)
	(at-x grass_block-block3 position-6)

	(at-y grass_block-block3 position3)

	(at-z grass_block-block3 position-3)

	(block-present grass_block-block3)
	(at-x grass_block-block4 position-6)

	(at-y grass_block-block4 position3)

	(at-z grass_block-block4 position-2)

	(block-present grass_block-block4)
	(at-x grass_block-block5 position-6)

	(at-y grass_block-block5 position3)

	(at-z grass_block-block5 position-1)

	(block-present grass_block-block5)
	(at-x grass_block-block6 position-6)

	(at-y grass_block-block6 position3)

	(at-z grass_block-block6 position0)

	(block-present grass_block-block6)
	(at-x grass_block-block7 position-6)

	(at-y grass_block-block7 position3)

	(at-z grass_block-block7 position1)

	(block-present grass_block-block7)
	(at-x grass_block-block8 position-6)

	(at-y grass_block-block8 position3)

	(at-z grass_block-block8 position2)

	(block-present grass_block-block8)
	(at-x grass_block-block9 position-6)

	(at-y grass_block-block9 position3)

	(at-z grass_block-block9 position4)

	(block-present grass_block-block9)
	(at-x grass_block-block10 position-6)

	(at-y grass_block-block10 position3)

	(at-z grass_block-block10 position5)

	(block-present grass_block-block10)
	(at-x grass_block-block11 position-6)

	(at-y grass_block-block11 position3)

	(at-z grass_block-block11 position6)

	(block-present grass_block-block11)
	(at-x grass_block-block12 position-5)

	(at-y grass_block-block12 position3)

	(at-z grass_block-block12 position-6)

	(block-present grass_block-block12)
	(at-x grass_block-block13 position-5)

	(at-y grass_block-block13 position3)

	(at-z grass_block-block13 position-5)

	(block-present grass_block-block13)
	(at-x grass_block-block14 position-5)

	(at-y grass_block-block14 position3)

	(at-z grass_block-block14 position-4)

	(block-present grass_block-block14)
	(at-x grass_block-block15 position-5)

	(at-y grass_block-block15 position3)

	(at-z grass_block-block15 position-3)

	(block-present grass_block-block15)
	(at-x grass_block-block16 position-5)

	(at-y grass_block-block16 position3)

	(at-z grass_block-block16 position-2)

	(block-present grass_block-block16)
	(at-x grass_block-block17 position-5)

	(at-y grass_block-block17 position3)

	(at-z grass_block-block17 position-1)

	(block-present grass_block-block17)
	(at-x grass_block-block18 position-5)

	(at-y grass_block-block18 position3)

	(at-z grass_block-block18 position0)

	(block-present grass_block-block18)
	(at-x grass_block-block19 position-5)

	(at-y grass_block-block19 position3)

	(at-z grass_block-block19 position1)

	(block-present grass_block-block19)
	(at-x grass_block-block20 position-5)

	(at-y grass_block-block20 position3)

	(at-z grass_block-block20 position2)

	(block-present grass_block-block20)
	(at-x grass_block-block21 position-5)

	(at-y grass_block-block21 position3)

	(at-z grass_block-block21 position4)

	(block-present grass_block-block21)
	(at-x grass_block-block22 position-5)

	(at-y grass_block-block22 position3)

	(at-z grass_block-block22 position5)

	(block-present grass_block-block22)
	(at-x grass_block-block23 position-5)

	(at-y grass_block-block23 position3)

	(at-z grass_block-block23 position6)

	(block-present grass_block-block23)
	(at-x grass_block-block24 position-4)

	(at-y grass_block-block24 position3)

	(at-z grass_block-block24 position-6)

	(block-present grass_block-block24)
	(at-x grass_block-block25 position-4)

	(at-y grass_block-block25 position3)

	(at-z grass_block-block25 position-5)

	(block-present grass_block-block25)
	(at-x grass_block-block26 position-4)

	(at-y grass_block-block26 position3)

	(at-z grass_block-block26 position-4)

	(block-present grass_block-block26)
	(at-x grass_block-block27 position-4)

	(at-y grass_block-block27 position3)

	(at-z grass_block-block27 position-3)

	(block-present grass_block-block27)
	(at-x grass_block-block28 position-4)

	(at-y grass_block-block28 position3)

	(at-z grass_block-block28 position-2)

	(block-present grass_block-block28)
	(at-x grass_block-block29 position-4)

	(at-y grass_block-block29 position3)

	(at-z grass_block-block29 position-1)

	(block-present grass_block-block29)
	(at-x grass_block-block30 position-4)

	(at-y grass_block-block30 position3)

	(at-z grass_block-block30 position0)

	(block-present grass_block-block30)
	(at-x grass_block-block31 position-4)

	(at-y grass_block-block31 position3)

	(at-z grass_block-block31 position1)

	(block-present grass_block-block31)
	(at-x grass_block-block32 position-4)

	(at-y grass_block-block32 position3)

	(at-z grass_block-block32 position2)

	(block-present grass_block-block32)
	(at-x grass_block-block33 position-4)

	(at-y grass_block-block33 position3)

	(at-z grass_block-block33 position4)

	(block-present grass_block-block33)
	(at-x grass_block-block34 position-4)

	(at-y grass_block-block34 position3)

	(at-z grass_block-block34 position5)

	(block-present grass_block-block34)
	(at-x grass_block-block35 position-4)

	(at-y grass_block-block35 position3)

	(at-z grass_block-block35 position6)

	(block-present grass_block-block35)
	(at-x grass_block-block36 position-3)

	(at-y grass_block-block36 position3)

	(at-z grass_block-block36 position-6)

	(block-present grass_block-block36)
	(at-x grass_block-block37 position-3)

	(at-y grass_block-block37 position3)

	(at-z grass_block-block37 position-5)

	(block-present grass_block-block37)
	(at-x grass_block-block38 position-3)

	(at-y grass_block-block38 position3)

	(at-z grass_block-block38 position-4)

	(block-present grass_block-block38)
	(at-x grass_block-block39 position-3)

	(at-y grass_block-block39 position3)

	(at-z grass_block-block39 position-3)

	(block-present grass_block-block39)
	(at-x grass_block-block40 position-3)

	(at-y grass_block-block40 position3)

	(at-z grass_block-block40 position-2)

	(block-present grass_block-block40)
	(at-x grass_block-block41 position-3)

	(at-y grass_block-block41 position3)

	(at-z grass_block-block41 position-1)

	(block-present grass_block-block41)
	(at-x grass_block-block42 position-3)

	(at-y grass_block-block42 position3)

	(at-z grass_block-block42 position0)

	(block-present grass_block-block42)
	(at-x grass_block-block43 position-3)

	(at-y grass_block-block43 position3)

	(at-z grass_block-block43 position1)

	(block-present grass_block-block43)
	(at-x grass_block-block44 position-3)

	(at-y grass_block-block44 position3)

	(at-z grass_block-block44 position2)

	(block-present grass_block-block44)
	(at-x grass_block-block45 position-3)

	(at-y grass_block-block45 position3)

	(at-z grass_block-block45 position4)

	(block-present grass_block-block45)
	(at-x grass_block-block46 position-3)

	(at-y grass_block-block46 position3)

	(at-z grass_block-block46 position5)

	(block-present grass_block-block46)
	(at-x grass_block-block47 position-3)

	(at-y grass_block-block47 position3)

	(at-z grass_block-block47 position6)

	(block-present grass_block-block47)
	(at-x grass_block-block48 position-2)

	(at-y grass_block-block48 position3)

	(at-z grass_block-block48 position-6)

	(block-present grass_block-block48)
	(at-x grass_block-block49 position-2)

	(at-y grass_block-block49 position3)

	(at-z grass_block-block49 position-5)

	(block-present grass_block-block49)
	(at-x grass_block-block50 position-2)

	(at-y grass_block-block50 position3)

	(at-z grass_block-block50 position-4)

	(block-present grass_block-block50)
	(at-x grass_block-block51 position-2)

	(at-y grass_block-block51 position3)

	(at-z grass_block-block51 position-3)

	(block-present grass_block-block51)
	(at-x grass_block-block52 position-2)

	(at-y grass_block-block52 position3)

	(at-z grass_block-block52 position-2)

	(block-present grass_block-block52)
	(at-x grass_block-block53 position-2)

	(at-y grass_block-block53 position3)

	(at-z grass_block-block53 position-1)

	(block-present grass_block-block53)
	(at-x grass_block-block54 position-2)

	(at-y grass_block-block54 position3)

	(at-z grass_block-block54 position0)

	(block-present grass_block-block54)
	(at-x grass_block-block55 position-2)

	(at-y grass_block-block55 position3)

	(at-z grass_block-block55 position1)

	(block-present grass_block-block55)
	(at-x grass_block-block56 position-2)

	(at-y grass_block-block56 position3)

	(at-z grass_block-block56 position2)

	(block-present grass_block-block56)
	(at-x grass_block-block57 position-2)

	(at-y grass_block-block57 position3)

	(at-z grass_block-block57 position4)

	(block-present grass_block-block57)
	(at-x grass_block-block58 position-2)

	(at-y grass_block-block58 position3)

	(at-z grass_block-block58 position5)

	(block-present grass_block-block58)
	(at-x grass_block-block59 position-2)

	(at-y grass_block-block59 position3)

	(at-z grass_block-block59 position6)

	(block-present grass_block-block59)
	(at-x grass_block-block60 position-1)

	(at-y grass_block-block60 position3)

	(at-z grass_block-block60 position-6)

	(block-present grass_block-block60)
	(at-x grass_block-block61 position-1)

	(at-y grass_block-block61 position3)

	(at-z grass_block-block61 position-5)

	(block-present grass_block-block61)
	(at-x grass_block-block62 position-1)

	(at-y grass_block-block62 position3)

	(at-z grass_block-block62 position-4)

	(block-present grass_block-block62)
	(at-x grass_block-block63 position-1)

	(at-y grass_block-block63 position3)

	(at-z grass_block-block63 position-3)

	(block-present grass_block-block63)
	(at-x grass_block-block64 position-1)

	(at-y grass_block-block64 position3)

	(at-z grass_block-block64 position-2)

	(block-present grass_block-block64)
	(at-x grass_block-block65 position-1)

	(at-y grass_block-block65 position3)

	(at-z grass_block-block65 position-1)

	(block-present grass_block-block65)
	(at-x grass_block-block66 position-1)

	(at-y grass_block-block66 position3)

	(at-z grass_block-block66 position0)

	(block-present grass_block-block66)
	(at-x grass_block-block67 position-1)

	(at-y grass_block-block67 position3)

	(at-z grass_block-block67 position1)

	(block-present grass_block-block67)
	(at-x grass_block-block68 position-1)

	(at-y grass_block-block68 position3)

	(at-z grass_block-block68 position2)

	(block-present grass_block-block68)
	(at-x grass_block-block69 position-1)

	(at-y grass_block-block69 position3)

	(at-z grass_block-block69 position4)

	(block-present grass_block-block69)
	(at-x grass_block-block70 position-1)

	(at-y grass_block-block70 position3)

	(at-z grass_block-block70 position5)

	(block-present grass_block-block70)
	(at-x grass_block-block71 position-1)

	(at-y grass_block-block71 position3)

	(at-z grass_block-block71 position6)

	(block-present grass_block-block71)
	(at-x grass_block-block72 position0)

	(at-y grass_block-block72 position3)

	(at-z grass_block-block72 position-6)

	(block-present grass_block-block72)
	(at-x grass_block-block73 position0)

	(at-y grass_block-block73 position3)

	(at-z grass_block-block73 position-5)

	(block-present grass_block-block73)
	(at-x grass_block-block74 position0)

	(at-y grass_block-block74 position3)

	(at-z grass_block-block74 position-4)

	(block-present grass_block-block74)
	(at-x grass_block-block75 position0)

	(at-y grass_block-block75 position3)

	(at-z grass_block-block75 position-3)

	(block-present grass_block-block75)
	(at-x grass_block-block76 position0)

	(at-y grass_block-block76 position3)

	(at-z grass_block-block76 position-2)

	(block-present grass_block-block76)
	(at-x grass_block-block77 position0)

	(at-y grass_block-block77 position3)

	(at-z grass_block-block77 position-1)

	(block-present grass_block-block77)
	(at-x grass_block-block78 position0)

	(at-y grass_block-block78 position3)

	(at-z grass_block-block78 position0)

	(block-present grass_block-block78)
	(at-x grass_block-block79 position0)

	(at-y grass_block-block79 position3)

	(at-z grass_block-block79 position1)

	(block-present grass_block-block79)
	(at-x grass_block-block80 position0)

	(at-y grass_block-block80 position3)

	(at-z grass_block-block80 position2)

	(block-present grass_block-block80)
	(at-x grass_block-block81 position0)

	(at-y grass_block-block81 position3)

	(at-z grass_block-block81 position4)

	(block-present grass_block-block81)
	(at-x grass_block-block82 position0)

	(at-y grass_block-block82 position3)

	(at-z grass_block-block82 position5)

	(block-present grass_block-block82)
	(at-x grass_block-block83 position0)

	(at-y grass_block-block83 position3)

	(at-z grass_block-block83 position6)

	(block-present grass_block-block83)
	(at-x grass_block-block84 position1)

	(at-y grass_block-block84 position3)

	(at-z grass_block-block84 position-6)

	(block-present grass_block-block84)
	(at-x grass_block-block85 position1)

	(at-y grass_block-block85 position3)

	(at-z grass_block-block85 position-5)

	(block-present grass_block-block85)
	(at-x grass_block-block86 position1)

	(at-y grass_block-block86 position3)

	(at-z grass_block-block86 position-4)

	(block-present grass_block-block86)
	(at-x grass_block-block87 position1)

	(at-y grass_block-block87 position3)

	(at-z grass_block-block87 position-3)

	(block-present grass_block-block87)
	(at-x grass_block-block88 position1)

	(at-y grass_block-block88 position3)

	(at-z grass_block-block88 position-2)

	(block-present grass_block-block88)
	(at-x grass_block-block89 position1)

	(at-y grass_block-block89 position3)

	(at-z grass_block-block89 position-1)

	(block-present grass_block-block89)
	(at-x grass_block-block90 position1)

	(at-y grass_block-block90 position3)

	(at-z grass_block-block90 position0)

	(block-present grass_block-block90)
	(at-x grass_block-block91 position1)

	(at-y grass_block-block91 position3)

	(at-z grass_block-block91 position1)

	(block-present grass_block-block91)
	(at-x grass_block-block92 position1)

	(at-y grass_block-block92 position3)

	(at-z grass_block-block92 position2)

	(block-present grass_block-block92)
	(at-x grass_block-block93 position1)

	(at-y grass_block-block93 position3)

	(at-z grass_block-block93 position4)

	(block-present grass_block-block93)
	(at-x grass_block-block94 position1)

	(at-y grass_block-block94 position3)

	(at-z grass_block-block94 position5)

	(block-present grass_block-block94)
	(at-x grass_block-block95 position1)

	(at-y grass_block-block95 position3)

	(at-z grass_block-block95 position6)

	(block-present grass_block-block95)
	(at-x grass_block-block96 position2)

	(at-y grass_block-block96 position3)

	(at-z grass_block-block96 position-6)

	(block-present grass_block-block96)
	(at-x grass_block-block97 position2)

	(at-y grass_block-block97 position3)

	(at-z grass_block-block97 position-5)

	(block-present grass_block-block97)
	(at-x grass_block-block98 position2)

	(at-y grass_block-block98 position3)

	(at-z grass_block-block98 position-4)

	(block-present grass_block-block98)
	(at-x grass_block-block99 position2)

	(at-y grass_block-block99 position3)

	(at-z grass_block-block99 position-3)

	(block-present grass_block-block99)
	(at-x grass_block-block100 position2)

	(at-y grass_block-block100 position3)

	(at-z grass_block-block100 position-2)

	(block-present grass_block-block100)
	(at-x grass_block-block101 position2)

	(at-y grass_block-block101 position3)

	(at-z grass_block-block101 position-1)

	(block-present grass_block-block101)
	(at-x grass_block-block102 position2)

	(at-y grass_block-block102 position3)

	(at-z grass_block-block102 position0)

	(block-present grass_block-block102)
	(at-x grass_block-block103 position2)

	(at-y grass_block-block103 position3)

	(at-z grass_block-block103 position1)

	(block-present grass_block-block103)
	(at-x grass_block-block104 position2)

	(at-y grass_block-block104 position3)

	(at-z grass_block-block104 position2)

	(block-present grass_block-block104)
	(at-x grass_block-block105 position2)

	(at-y grass_block-block105 position3)

	(at-z grass_block-block105 position4)

	(block-present grass_block-block105)
	(at-x grass_block-block106 position2)

	(at-y grass_block-block106 position3)

	(at-z grass_block-block106 position5)

	(block-present grass_block-block106)
	(at-x grass_block-block107 position2)

	(at-y grass_block-block107 position3)

	(at-z grass_block-block107 position6)

	(block-present grass_block-block107)
	(at-x grass_block-block108 position3)

	(at-y grass_block-block108 position3)

	(at-z grass_block-block108 position-6)

	(block-present grass_block-block108)
	(at-x grass_block-block109 position3)

	(at-y grass_block-block109 position3)

	(at-z grass_block-block109 position-5)

	(block-present grass_block-block109)
	(at-x grass_block-block110 position3)

	(at-y grass_block-block110 position3)

	(at-z grass_block-block110 position-4)

	(block-present grass_block-block110)
	(at-x grass_block-block111 position3)

	(at-y grass_block-block111 position3)

	(at-z grass_block-block111 position-3)

	(block-present grass_block-block111)
	(at-x grass_block-block112 position3)

	(at-y grass_block-block112 position3)

	(at-z grass_block-block112 position-2)

	(block-present grass_block-block112)
	(at-x grass_block-block113 position3)

	(at-y grass_block-block113 position3)

	(at-z grass_block-block113 position-1)

	(block-present grass_block-block113)
	(at-x grass_block-block114 position3)

	(at-y grass_block-block114 position3)

	(at-z grass_block-block114 position0)

	(block-present grass_block-block114)
	(at-x grass_block-block115 position3)

	(at-y grass_block-block115 position3)

	(at-z grass_block-block115 position1)

	(block-present grass_block-block115)
	(at-x grass_block-block116 position3)

	(at-y grass_block-block116 position3)

	(at-z grass_block-block116 position2)

	(block-present grass_block-block116)
	(at-x grass_block-block117 position3)

	(at-y grass_block-block117 position3)

	(at-z grass_block-block117 position4)

	(block-present grass_block-block117)
	(at-x grass_block-block118 position3)

	(at-y grass_block-block118 position3)

	(at-z grass_block-block118 position5)

	(block-present grass_block-block118)
	(at-x grass_block-block119 position3)

	(at-y grass_block-block119 position3)

	(at-z grass_block-block119 position6)

	(block-present grass_block-block119)
	(at-x grass_block-block120 position4)

	(at-y grass_block-block120 position3)

	(at-z grass_block-block120 position-6)

	(block-present grass_block-block120)
	(at-x grass_block-block121 position4)

	(at-y grass_block-block121 position3)

	(at-z grass_block-block121 position-5)

	(block-present grass_block-block121)
	(at-x grass_block-block122 position4)

	(at-y grass_block-block122 position3)

	(at-z grass_block-block122 position-4)

	(block-present grass_block-block122)
	(at-x grass_block-block123 position4)

	(at-y grass_block-block123 position3)

	(at-z grass_block-block123 position-3)

	(block-present grass_block-block123)
	(at-x grass_block-block124 position4)

	(at-y grass_block-block124 position3)

	(at-z grass_block-block124 position-2)

	(block-present grass_block-block124)
	(at-x grass_block-block125 position4)

	(at-y grass_block-block125 position3)

	(at-z grass_block-block125 position-1)

	(block-present grass_block-block125)
	(at-x grass_block-block126 position4)

	(at-y grass_block-block126 position3)

	(at-z grass_block-block126 position0)

	(block-present grass_block-block126)
	(at-x grass_block-block127 position4)

	(at-y grass_block-block127 position3)

	(at-z grass_block-block127 position1)

	(block-present grass_block-block127)
	(at-x grass_block-block128 position4)

	(at-y grass_block-block128 position3)

	(at-z grass_block-block128 position2)

	(block-present grass_block-block128)
	(at-x grass_block-block129 position4)

	(at-y grass_block-block129 position3)

	(at-z grass_block-block129 position4)

	(block-present grass_block-block129)
	(at-x grass_block-block130 position4)

	(at-y grass_block-block130 position3)

	(at-z grass_block-block130 position5)

	(block-present grass_block-block130)
	(at-x grass_block-block131 position4)

	(at-y grass_block-block131 position3)

	(at-z grass_block-block131 position6)

	(block-present grass_block-block131)
	(at-x grass_block-block132 position5)

	(at-y grass_block-block132 position3)

	(at-z grass_block-block132 position-6)

	(block-present grass_block-block132)
	(at-x grass_block-block133 position5)

	(at-y grass_block-block133 position3)

	(at-z grass_block-block133 position-5)

	(block-present grass_block-block133)
	(at-x grass_block-block134 position5)

	(at-y grass_block-block134 position3)

	(at-z grass_block-block134 position-4)

	(block-present grass_block-block134)
	(at-x grass_block-block135 position5)

	(at-y grass_block-block135 position3)

	(at-z grass_block-block135 position-3)

	(block-present grass_block-block135)
	(at-x grass_block-block136 position5)

	(at-y grass_block-block136 position3)

	(at-z grass_block-block136 position-2)

	(block-present grass_block-block136)
	(at-x grass_block-block137 position5)

	(at-y grass_block-block137 position3)

	(at-z grass_block-block137 position-1)

	(block-present grass_block-block137)
	(at-x grass_block-block138 position5)

	(at-y grass_block-block138 position3)

	(at-z grass_block-block138 position0)

	(block-present grass_block-block138)
	(at-x grass_block-block139 position5)

	(at-y grass_block-block139 position3)

	(at-z grass_block-block139 position1)

	(block-present grass_block-block139)
	(at-x grass_block-block140 position5)

	(at-y grass_block-block140 position3)

	(at-z grass_block-block140 position2)

	(block-present grass_block-block140)
	(at-x grass_block-block141 position5)

	(at-y grass_block-block141 position3)

	(at-z grass_block-block141 position4)

	(block-present grass_block-block141)
	(at-x grass_block-block142 position5)

	(at-y grass_block-block142 position3)

	(at-z grass_block-block142 position5)

	(block-present grass_block-block142)
	(at-x grass_block-block143 position5)

	(at-y grass_block-block143 position3)

	(at-z grass_block-block143 position6)

	(block-present grass_block-block143)
	(at-x grass_block-block144 position6)

	(at-y grass_block-block144 position3)

	(at-z grass_block-block144 position-6)

	(block-present grass_block-block144)
	(at-x grass_block-block145 position6)

	(at-y grass_block-block145 position3)

	(at-z grass_block-block145 position-5)

	(block-present grass_block-block145)
	(at-x grass_block-block146 position6)

	(at-y grass_block-block146 position3)

	(at-z grass_block-block146 position-4)

	(block-present grass_block-block146)
	(at-x grass_block-block147 position6)

	(at-y grass_block-block147 position3)

	(at-z grass_block-block147 position-3)

	(block-present grass_block-block147)
	(at-x grass_block-block148 position6)

	(at-y grass_block-block148 position3)

	(at-z grass_block-block148 position-2)

	(block-present grass_block-block148)
	(at-x grass_block-block149 position6)

	(at-y grass_block-block149 position3)

	(at-z grass_block-block149 position-1)

	(block-present grass_block-block149)
	(at-x grass_block-block150 position6)

	(at-y grass_block-block150 position3)

	(at-z grass_block-block150 position0)

	(block-present grass_block-block150)
	(at-x grass_block-block151 position6)

	(at-y grass_block-block151 position3)

	(at-z grass_block-block151 position1)

	(block-present grass_block-block151)
	(at-x grass_block-block152 position6)

	(at-y grass_block-block152 position3)

	(at-z grass_block-block152 position2)

	(block-present grass_block-block152)
	(at-x grass_block-block153 position6)

	(at-y grass_block-block153 position3)

	(at-z grass_block-block153 position4)

	(block-present grass_block-block153)
	(at-x grass_block-block154 position6)

	(at-y grass_block-block154 position3)

	(at-z grass_block-block154 position5)

	(block-present grass_block-block154)
	(at-x grass_block-block155 position6)

	(at-y grass_block-block155 position3)

	(at-z grass_block-block155 position6)

	(block-present grass_block-block155)
	(at-x water-block0 position-6)

	(at-y water-block0 position3)

	(at-z water-block0 position3)

	(block-present water-block0)
	(at-x water-block1 position-5)

	(at-y water-block1 position3)

	(at-z water-block1 position3)

	(block-present water-block1)
	(at-x water-block2 position-4)

	(at-y water-block2 position3)

	(at-z water-block2 position3)

	(block-present water-block2)
	(at-x water-block3 position-3)

	(at-y water-block3 position3)

	(at-z water-block3 position3)

	(block-present water-block3)
	(at-x water-block4 position-2)

	(at-y water-block4 position3)

	(at-z water-block4 position3)

	(block-present water-block4)
	(at-x water-block5 position-1)

	(at-y water-block5 position3)

	(at-z water-block5 position3)

	(block-present water-block5)
	(at-x water-block6 position0)

	(at-y water-block6 position3)

	(at-z water-block6 position3)

	(block-present water-block6)
	(at-x water-block7 position1)

	(at-y water-block7 position3)

	(at-z water-block7 position3)

	(block-present water-block7)
	(at-x water-block8 position2)

	(at-y water-block8 position3)

	(at-z water-block8 position3)

	(block-present water-block8)
	(at-x water-block9 position3)

	(at-y water-block9 position3)

	(at-z water-block9 position3)

	(block-present water-block9)
	(at-x water-block10 position4)

	(at-y water-block10 position3)

	(at-z water-block10 position3)

	(block-present water-block10)
	(at-x water-block11 position5)

	(at-y water-block11 position3)

	(at-z water-block11 position3)

	(block-present water-block11)
	(at-x water-block12 position6)

	(at-y water-block12 position3)

	(at-z water-block12 position3)

	(block-present water-block12)
	(at-x planks0 position0)

	(at-y planks0 position4)

	(at-z planks0 position0)

	(at-x cobblestone0 position0)

	(at-y cobblestone0 position4)

	(at-z cobblestone0 position0)

)
(:goal
	(and (goal-achieved steve))
		
)
)
