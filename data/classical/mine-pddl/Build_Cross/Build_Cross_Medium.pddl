(define (problem Build_Cross_Medium_problem)
	(:domain Build_Cross_Medium)

(:init
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
	(agent-has-n-grass_block steve count0)

	(agent-has-n-stone steve count0)

	(agent-has-n-planks steve count0)

	(agent-has-n-wool steve count0)

	(at-x grass_block-block0 position-10)

	(at-y grass_block-block0 position3)

	(at-z grass_block-block0 position-10)

	(block-present grass_block-block0)
	(at-x grass_block-block1 position-10)

	(at-y grass_block-block1 position3)

	(at-z grass_block-block1 position-9)

	(block-present grass_block-block1)
	(at-x grass_block-block2 position-10)

	(at-y grass_block-block2 position3)

	(at-z grass_block-block2 position-8)

	(block-present grass_block-block2)
	(at-x grass_block-block3 position-10)

	(at-y grass_block-block3 position3)

	(at-z grass_block-block3 position-7)

	(block-present grass_block-block3)
	(at-x grass_block-block4 position-10)

	(at-y grass_block-block4 position3)

	(at-z grass_block-block4 position-6)

	(block-present grass_block-block4)
	(at-x grass_block-block5 position-10)

	(at-y grass_block-block5 position3)

	(at-z grass_block-block5 position-5)

	(block-present grass_block-block5)
	(at-x grass_block-block6 position-10)

	(at-y grass_block-block6 position3)

	(at-z grass_block-block6 position-4)

	(block-present grass_block-block6)
	(at-x grass_block-block7 position-10)

	(at-y grass_block-block7 position3)

	(at-z grass_block-block7 position-3)

	(block-present grass_block-block7)
	(at-x grass_block-block8 position-10)

	(at-y grass_block-block8 position3)

	(at-z grass_block-block8 position-2)

	(block-present grass_block-block8)
	(at-x grass_block-block9 position-10)

	(at-y grass_block-block9 position3)

	(at-z grass_block-block9 position-1)

	(block-present grass_block-block9)
	(at-x grass_block-block10 position-10)

	(at-y grass_block-block10 position3)

	(at-z grass_block-block10 position0)

	(block-present grass_block-block10)
	(at-x grass_block-block11 position-10)

	(at-y grass_block-block11 position3)

	(at-z grass_block-block11 position1)

	(block-present grass_block-block11)
	(at-x grass_block-block12 position-10)

	(at-y grass_block-block12 position3)

	(at-z grass_block-block12 position2)

	(block-present grass_block-block12)
	(at-x grass_block-block13 position-10)

	(at-y grass_block-block13 position3)

	(at-z grass_block-block13 position3)

	(block-present grass_block-block13)
	(at-x grass_block-block14 position-10)

	(at-y grass_block-block14 position3)

	(at-z grass_block-block14 position4)

	(block-present grass_block-block14)
	(at-x grass_block-block15 position-10)

	(at-y grass_block-block15 position3)

	(at-z grass_block-block15 position5)

	(block-present grass_block-block15)
	(at-x grass_block-block16 position-10)

	(at-y grass_block-block16 position3)

	(at-z grass_block-block16 position6)

	(block-present grass_block-block16)
	(at-x grass_block-block17 position-10)

	(at-y grass_block-block17 position3)

	(at-z grass_block-block17 position7)

	(block-present grass_block-block17)
	(at-x grass_block-block18 position-10)

	(at-y grass_block-block18 position3)

	(at-z grass_block-block18 position8)

	(block-present grass_block-block18)
	(at-x grass_block-block19 position-10)

	(at-y grass_block-block19 position3)

	(at-z grass_block-block19 position9)

	(block-present grass_block-block19)
	(at-x grass_block-block20 position-10)

	(at-y grass_block-block20 position3)

	(at-z grass_block-block20 position10)

	(block-present grass_block-block20)
	(at-x grass_block-block21 position-9)

	(at-y grass_block-block21 position3)

	(at-z grass_block-block21 position-10)

	(block-present grass_block-block21)
	(at-x grass_block-block22 position-9)

	(at-y grass_block-block22 position3)

	(at-z grass_block-block22 position-9)

	(block-present grass_block-block22)
	(at-x grass_block-block23 position-9)

	(at-y grass_block-block23 position3)

	(at-z grass_block-block23 position-8)

	(block-present grass_block-block23)
	(at-x grass_block-block24 position-9)

	(at-y grass_block-block24 position3)

	(at-z grass_block-block24 position-7)

	(block-present grass_block-block24)
	(at-x grass_block-block25 position-9)

	(at-y grass_block-block25 position3)

	(at-z grass_block-block25 position-6)

	(block-present grass_block-block25)
	(at-x grass_block-block26 position-9)

	(at-y grass_block-block26 position3)

	(at-z grass_block-block26 position-5)

	(block-present grass_block-block26)
	(at-x grass_block-block27 position-9)

	(at-y grass_block-block27 position3)

	(at-z grass_block-block27 position-4)

	(block-present grass_block-block27)
	(at-x grass_block-block28 position-9)

	(at-y grass_block-block28 position3)

	(at-z grass_block-block28 position-3)

	(block-present grass_block-block28)
	(at-x grass_block-block29 position-9)

	(at-y grass_block-block29 position3)

	(at-z grass_block-block29 position-2)

	(block-present grass_block-block29)
	(at-x grass_block-block30 position-9)

	(at-y grass_block-block30 position3)

	(at-z grass_block-block30 position-1)

	(block-present grass_block-block30)
	(at-x grass_block-block31 position-9)

	(at-y grass_block-block31 position3)

	(at-z grass_block-block31 position0)

	(block-present grass_block-block31)
	(at-x grass_block-block32 position-9)

	(at-y grass_block-block32 position3)

	(at-z grass_block-block32 position1)

	(block-present grass_block-block32)
	(at-x grass_block-block33 position-9)

	(at-y grass_block-block33 position3)

	(at-z grass_block-block33 position2)

	(block-present grass_block-block33)
	(at-x grass_block-block34 position-9)

	(at-y grass_block-block34 position3)

	(at-z grass_block-block34 position3)

	(block-present grass_block-block34)
	(at-x grass_block-block35 position-9)

	(at-y grass_block-block35 position3)

	(at-z grass_block-block35 position4)

	(block-present grass_block-block35)
	(at-x grass_block-block36 position-9)

	(at-y grass_block-block36 position3)

	(at-z grass_block-block36 position5)

	(block-present grass_block-block36)
	(at-x grass_block-block37 position-9)

	(at-y grass_block-block37 position3)

	(at-z grass_block-block37 position6)

	(block-present grass_block-block37)
	(at-x grass_block-block38 position-9)

	(at-y grass_block-block38 position3)

	(at-z grass_block-block38 position7)

	(block-present grass_block-block38)
	(at-x grass_block-block39 position-9)

	(at-y grass_block-block39 position3)

	(at-z grass_block-block39 position8)

	(block-present grass_block-block39)
	(at-x grass_block-block40 position-9)

	(at-y grass_block-block40 position3)

	(at-z grass_block-block40 position9)

	(block-present grass_block-block40)
	(at-x grass_block-block41 position-9)

	(at-y grass_block-block41 position3)

	(at-z grass_block-block41 position10)

	(block-present grass_block-block41)
	(at-x grass_block-block42 position-8)

	(at-y grass_block-block42 position3)

	(at-z grass_block-block42 position-10)

	(block-present grass_block-block42)
	(at-x grass_block-block43 position-8)

	(at-y grass_block-block43 position3)

	(at-z grass_block-block43 position-9)

	(block-present grass_block-block43)
	(at-x grass_block-block44 position-8)

	(at-y grass_block-block44 position3)

	(at-z grass_block-block44 position-8)

	(block-present grass_block-block44)
	(at-x grass_block-block45 position-8)

	(at-y grass_block-block45 position3)

	(at-z grass_block-block45 position-7)

	(block-present grass_block-block45)
	(at-x grass_block-block46 position-8)

	(at-y grass_block-block46 position3)

	(at-z grass_block-block46 position-6)

	(block-present grass_block-block46)
	(at-x grass_block-block47 position-8)

	(at-y grass_block-block47 position3)

	(at-z grass_block-block47 position-5)

	(block-present grass_block-block47)
	(at-x grass_block-block48 position-8)

	(at-y grass_block-block48 position3)

	(at-z grass_block-block48 position-4)

	(block-present grass_block-block48)
	(at-x grass_block-block49 position-8)

	(at-y grass_block-block49 position3)

	(at-z grass_block-block49 position-3)

	(block-present grass_block-block49)
	(at-x grass_block-block50 position-8)

	(at-y grass_block-block50 position3)

	(at-z grass_block-block50 position-2)

	(block-present grass_block-block50)
	(at-x grass_block-block51 position-8)

	(at-y grass_block-block51 position3)

	(at-z grass_block-block51 position-1)

	(block-present grass_block-block51)
	(at-x grass_block-block52 position-8)

	(at-y grass_block-block52 position3)

	(at-z grass_block-block52 position0)

	(block-present grass_block-block52)
	(at-x grass_block-block53 position-8)

	(at-y grass_block-block53 position3)

	(at-z grass_block-block53 position1)

	(block-present grass_block-block53)
	(at-x grass_block-block54 position-8)

	(at-y grass_block-block54 position3)

	(at-z grass_block-block54 position2)

	(block-present grass_block-block54)
	(at-x grass_block-block55 position-8)

	(at-y grass_block-block55 position3)

	(at-z grass_block-block55 position3)

	(block-present grass_block-block55)
	(at-x grass_block-block56 position-8)

	(at-y grass_block-block56 position3)

	(at-z grass_block-block56 position4)

	(block-present grass_block-block56)
	(at-x grass_block-block57 position-8)

	(at-y grass_block-block57 position3)

	(at-z grass_block-block57 position5)

	(block-present grass_block-block57)
	(at-x grass_block-block58 position-8)

	(at-y grass_block-block58 position3)

	(at-z grass_block-block58 position6)

	(block-present grass_block-block58)
	(at-x grass_block-block59 position-8)

	(at-y grass_block-block59 position3)

	(at-z grass_block-block59 position7)

	(block-present grass_block-block59)
	(at-x grass_block-block60 position-8)

	(at-y grass_block-block60 position3)

	(at-z grass_block-block60 position8)

	(block-present grass_block-block60)
	(at-x grass_block-block61 position-8)

	(at-y grass_block-block61 position3)

	(at-z grass_block-block61 position9)

	(block-present grass_block-block61)
	(at-x grass_block-block62 position-8)

	(at-y grass_block-block62 position3)

	(at-z grass_block-block62 position10)

	(block-present grass_block-block62)
	(at-x grass_block-block63 position-7)

	(at-y grass_block-block63 position3)

	(at-z grass_block-block63 position-10)

	(block-present grass_block-block63)
	(at-x grass_block-block64 position-7)

	(at-y grass_block-block64 position3)

	(at-z grass_block-block64 position-9)

	(block-present grass_block-block64)
	(at-x grass_block-block65 position-7)

	(at-y grass_block-block65 position3)

	(at-z grass_block-block65 position-8)

	(block-present grass_block-block65)
	(at-x grass_block-block66 position-7)

	(at-y grass_block-block66 position3)

	(at-z grass_block-block66 position-7)

	(block-present grass_block-block66)
	(at-x grass_block-block67 position-7)

	(at-y grass_block-block67 position3)

	(at-z grass_block-block67 position-6)

	(block-present grass_block-block67)
	(at-x grass_block-block68 position-7)

	(at-y grass_block-block68 position3)

	(at-z grass_block-block68 position-5)

	(block-present grass_block-block68)
	(at-x grass_block-block69 position-7)

	(at-y grass_block-block69 position3)

	(at-z grass_block-block69 position-4)

	(block-present grass_block-block69)
	(at-x grass_block-block70 position-7)

	(at-y grass_block-block70 position3)

	(at-z grass_block-block70 position-3)

	(block-present grass_block-block70)
	(at-x grass_block-block71 position-7)

	(at-y grass_block-block71 position3)

	(at-z grass_block-block71 position-2)

	(block-present grass_block-block71)
	(at-x grass_block-block72 position-7)

	(at-y grass_block-block72 position3)

	(at-z grass_block-block72 position-1)

	(block-present grass_block-block72)
	(at-x grass_block-block73 position-7)

	(at-y grass_block-block73 position3)

	(at-z grass_block-block73 position0)

	(block-present grass_block-block73)
	(at-x grass_block-block74 position-7)

	(at-y grass_block-block74 position3)

	(at-z grass_block-block74 position1)

	(block-present grass_block-block74)
	(at-x grass_block-block75 position-7)

	(at-y grass_block-block75 position3)

	(at-z grass_block-block75 position2)

	(block-present grass_block-block75)
	(at-x grass_block-block76 position-7)

	(at-y grass_block-block76 position3)

	(at-z grass_block-block76 position3)

	(block-present grass_block-block76)
	(at-x grass_block-block77 position-7)

	(at-y grass_block-block77 position3)

	(at-z grass_block-block77 position4)

	(block-present grass_block-block77)
	(at-x grass_block-block78 position-7)

	(at-y grass_block-block78 position3)

	(at-z grass_block-block78 position5)

	(block-present grass_block-block78)
	(at-x grass_block-block79 position-7)

	(at-y grass_block-block79 position3)

	(at-z grass_block-block79 position6)

	(block-present grass_block-block79)
	(at-x grass_block-block80 position-7)

	(at-y grass_block-block80 position3)

	(at-z grass_block-block80 position7)

	(block-present grass_block-block80)
	(at-x grass_block-block81 position-7)

	(at-y grass_block-block81 position3)

	(at-z grass_block-block81 position8)

	(block-present grass_block-block81)
	(at-x grass_block-block82 position-7)

	(at-y grass_block-block82 position3)

	(at-z grass_block-block82 position9)

	(block-present grass_block-block82)
	(at-x grass_block-block83 position-7)

	(at-y grass_block-block83 position3)

	(at-z grass_block-block83 position10)

	(block-present grass_block-block83)
	(at-x grass_block-block84 position-6)

	(at-y grass_block-block84 position3)

	(at-z grass_block-block84 position-10)

	(block-present grass_block-block84)
	(at-x grass_block-block85 position-6)

	(at-y grass_block-block85 position3)

	(at-z grass_block-block85 position-9)

	(block-present grass_block-block85)
	(at-x grass_block-block86 position-6)

	(at-y grass_block-block86 position3)

	(at-z grass_block-block86 position-8)

	(block-present grass_block-block86)
	(at-x grass_block-block87 position-6)

	(at-y grass_block-block87 position3)

	(at-z grass_block-block87 position-7)

	(block-present grass_block-block87)
	(at-x grass_block-block88 position-6)

	(at-y grass_block-block88 position3)

	(at-z grass_block-block88 position-6)

	(block-present grass_block-block88)
	(at-x grass_block-block89 position-6)

	(at-y grass_block-block89 position3)

	(at-z grass_block-block89 position-5)

	(block-present grass_block-block89)
	(at-x grass_block-block90 position-6)

	(at-y grass_block-block90 position3)

	(at-z grass_block-block90 position-4)

	(block-present grass_block-block90)
	(at-x grass_block-block91 position-6)

	(at-y grass_block-block91 position3)

	(at-z grass_block-block91 position-3)

	(block-present grass_block-block91)
	(at-x grass_block-block92 position-6)

	(at-y grass_block-block92 position3)

	(at-z grass_block-block92 position-2)

	(block-present grass_block-block92)
	(at-x grass_block-block93 position-6)

	(at-y grass_block-block93 position3)

	(at-z grass_block-block93 position-1)

	(block-present grass_block-block93)
	(at-x grass_block-block94 position-6)

	(at-y grass_block-block94 position3)

	(at-z grass_block-block94 position0)

	(block-present grass_block-block94)
	(at-x grass_block-block95 position-6)

	(at-y grass_block-block95 position3)

	(at-z grass_block-block95 position1)

	(block-present grass_block-block95)
	(at-x grass_block-block96 position-6)

	(at-y grass_block-block96 position3)

	(at-z grass_block-block96 position2)

	(block-present grass_block-block96)
	(at-x grass_block-block97 position-6)

	(at-y grass_block-block97 position3)

	(at-z grass_block-block97 position3)

	(block-present grass_block-block97)
	(at-x grass_block-block98 position-6)

	(at-y grass_block-block98 position3)

	(at-z grass_block-block98 position4)

	(block-present grass_block-block98)
	(at-x grass_block-block99 position-6)

	(at-y grass_block-block99 position3)

	(at-z grass_block-block99 position5)

	(block-present grass_block-block99)
	(at-x grass_block-block100 position-6)

	(at-y grass_block-block100 position3)

	(at-z grass_block-block100 position6)

	(block-present grass_block-block100)
	(at-x grass_block-block101 position-6)

	(at-y grass_block-block101 position3)

	(at-z grass_block-block101 position7)

	(block-present grass_block-block101)
	(at-x grass_block-block102 position-6)

	(at-y grass_block-block102 position3)

	(at-z grass_block-block102 position8)

	(block-present grass_block-block102)
	(at-x grass_block-block103 position-6)

	(at-y grass_block-block103 position3)

	(at-z grass_block-block103 position9)

	(block-present grass_block-block103)
	(at-x grass_block-block104 position-6)

	(at-y grass_block-block104 position3)

	(at-z grass_block-block104 position10)

	(block-present grass_block-block104)
	(at-x grass_block-block105 position-5)

	(at-y grass_block-block105 position3)

	(at-z grass_block-block105 position-10)

	(block-present grass_block-block105)
	(at-x grass_block-block106 position-5)

	(at-y grass_block-block106 position3)

	(at-z grass_block-block106 position-9)

	(block-present grass_block-block106)
	(at-x grass_block-block107 position-5)

	(at-y grass_block-block107 position3)

	(at-z grass_block-block107 position-8)

	(block-present grass_block-block107)
	(at-x grass_block-block108 position-5)

	(at-y grass_block-block108 position3)

	(at-z grass_block-block108 position-7)

	(block-present grass_block-block108)
	(at-x grass_block-block109 position-5)

	(at-y grass_block-block109 position3)

	(at-z grass_block-block109 position-6)

	(block-present grass_block-block109)
	(at-x grass_block-block110 position-5)

	(at-y grass_block-block110 position3)

	(at-z grass_block-block110 position-5)

	(block-present grass_block-block110)
	(at-x grass_block-block111 position-5)

	(at-y grass_block-block111 position3)

	(at-z grass_block-block111 position-4)

	(block-present grass_block-block111)
	(at-x grass_block-block112 position-5)

	(at-y grass_block-block112 position3)

	(at-z grass_block-block112 position-3)

	(block-present grass_block-block112)
	(at-x grass_block-block113 position-5)

	(at-y grass_block-block113 position3)

	(at-z grass_block-block113 position-2)

	(block-present grass_block-block113)
	(at-x grass_block-block114 position-5)

	(at-y grass_block-block114 position3)

	(at-z grass_block-block114 position-1)

	(block-present grass_block-block114)
	(at-x grass_block-block115 position-5)

	(at-y grass_block-block115 position3)

	(at-z grass_block-block115 position0)

	(block-present grass_block-block115)
	(at-x grass_block-block116 position-5)

	(at-y grass_block-block116 position3)

	(at-z grass_block-block116 position1)

	(block-present grass_block-block116)
	(at-x grass_block-block117 position-5)

	(at-y grass_block-block117 position3)

	(at-z grass_block-block117 position2)

	(block-present grass_block-block117)
	(at-x grass_block-block118 position-5)

	(at-y grass_block-block118 position3)

	(at-z grass_block-block118 position3)

	(block-present grass_block-block118)
	(at-x grass_block-block119 position-5)

	(at-y grass_block-block119 position3)

	(at-z grass_block-block119 position4)

	(block-present grass_block-block119)
	(at-x grass_block-block120 position-5)

	(at-y grass_block-block120 position3)

	(at-z grass_block-block120 position5)

	(block-present grass_block-block120)
	(at-x grass_block-block121 position-5)

	(at-y grass_block-block121 position3)

	(at-z grass_block-block121 position6)

	(block-present grass_block-block121)
	(at-x grass_block-block122 position-5)

	(at-y grass_block-block122 position3)

	(at-z grass_block-block122 position7)

	(block-present grass_block-block122)
	(at-x grass_block-block123 position-5)

	(at-y grass_block-block123 position3)

	(at-z grass_block-block123 position8)

	(block-present grass_block-block123)
	(at-x grass_block-block124 position-5)

	(at-y grass_block-block124 position3)

	(at-z grass_block-block124 position9)

	(block-present grass_block-block124)
	(at-x grass_block-block125 position-5)

	(at-y grass_block-block125 position3)

	(at-z grass_block-block125 position10)

	(block-present grass_block-block125)
	(at-x grass_block-block126 position-4)

	(at-y grass_block-block126 position3)

	(at-z grass_block-block126 position-10)

	(block-present grass_block-block126)
	(at-x grass_block-block127 position-4)

	(at-y grass_block-block127 position3)

	(at-z grass_block-block127 position-9)

	(block-present grass_block-block127)
	(at-x grass_block-block128 position-4)

	(at-y grass_block-block128 position3)

	(at-z grass_block-block128 position-8)

	(block-present grass_block-block128)
	(at-x grass_block-block129 position-4)

	(at-y grass_block-block129 position3)

	(at-z grass_block-block129 position-7)

	(block-present grass_block-block129)
	(at-x grass_block-block130 position-4)

	(at-y grass_block-block130 position3)

	(at-z grass_block-block130 position-6)

	(block-present grass_block-block130)
	(at-x grass_block-block131 position-4)

	(at-y grass_block-block131 position3)

	(at-z grass_block-block131 position-5)

	(block-present grass_block-block131)
	(at-x grass_block-block132 position-4)

	(at-y grass_block-block132 position3)

	(at-z grass_block-block132 position-4)

	(block-present grass_block-block132)
	(at-x grass_block-block133 position-4)

	(at-y grass_block-block133 position3)

	(at-z grass_block-block133 position-3)

	(block-present grass_block-block133)
	(at-x grass_block-block134 position-4)

	(at-y grass_block-block134 position3)

	(at-z grass_block-block134 position-2)

	(block-present grass_block-block134)
	(at-x grass_block-block135 position-4)

	(at-y grass_block-block135 position3)

	(at-z grass_block-block135 position-1)

	(block-present grass_block-block135)
	(at-x grass_block-block136 position-4)

	(at-y grass_block-block136 position3)

	(at-z grass_block-block136 position0)

	(block-present grass_block-block136)
	(at-x grass_block-block137 position-4)

	(at-y grass_block-block137 position3)

	(at-z grass_block-block137 position1)

	(block-present grass_block-block137)
	(at-x grass_block-block138 position-4)

	(at-y grass_block-block138 position3)

	(at-z grass_block-block138 position2)

	(block-present grass_block-block138)
	(at-x grass_block-block139 position-4)

	(at-y grass_block-block139 position3)

	(at-z grass_block-block139 position3)

	(block-present grass_block-block139)
	(at-x grass_block-block140 position-4)

	(at-y grass_block-block140 position3)

	(at-z grass_block-block140 position4)

	(block-present grass_block-block140)
	(at-x grass_block-block141 position-4)

	(at-y grass_block-block141 position3)

	(at-z grass_block-block141 position5)

	(block-present grass_block-block141)
	(at-x grass_block-block142 position-4)

	(at-y grass_block-block142 position3)

	(at-z grass_block-block142 position6)

	(block-present grass_block-block142)
	(at-x grass_block-block143 position-4)

	(at-y grass_block-block143 position3)

	(at-z grass_block-block143 position7)

	(block-present grass_block-block143)
	(at-x grass_block-block144 position-4)

	(at-y grass_block-block144 position3)

	(at-z grass_block-block144 position8)

	(block-present grass_block-block144)
	(at-x grass_block-block145 position-4)

	(at-y grass_block-block145 position3)

	(at-z grass_block-block145 position9)

	(block-present grass_block-block145)
	(at-x grass_block-block146 position-4)

	(at-y grass_block-block146 position3)

	(at-z grass_block-block146 position10)

	(block-present grass_block-block146)
	(at-x grass_block-block147 position-3)

	(at-y grass_block-block147 position3)

	(at-z grass_block-block147 position-10)

	(block-present grass_block-block147)
	(at-x grass_block-block148 position-3)

	(at-y grass_block-block148 position3)

	(at-z grass_block-block148 position-9)

	(block-present grass_block-block148)
	(at-x grass_block-block149 position-3)

	(at-y grass_block-block149 position3)

	(at-z grass_block-block149 position-8)

	(block-present grass_block-block149)
	(at-x grass_block-block150 position-3)

	(at-y grass_block-block150 position3)

	(at-z grass_block-block150 position-7)

	(block-present grass_block-block150)
	(at-x grass_block-block151 position-3)

	(at-y grass_block-block151 position3)

	(at-z grass_block-block151 position-6)

	(block-present grass_block-block151)
	(at-x grass_block-block152 position-3)

	(at-y grass_block-block152 position3)

	(at-z grass_block-block152 position-5)

	(block-present grass_block-block152)
	(at-x grass_block-block153 position-3)

	(at-y grass_block-block153 position3)

	(at-z grass_block-block153 position-4)

	(block-present grass_block-block153)
	(at-x grass_block-block154 position-3)

	(at-y grass_block-block154 position3)

	(at-z grass_block-block154 position-3)

	(block-present grass_block-block154)
	(at-x grass_block-block155 position-3)

	(at-y grass_block-block155 position3)

	(at-z grass_block-block155 position-2)

	(block-present grass_block-block155)
	(at-x grass_block-block156 position-3)

	(at-y grass_block-block156 position3)

	(at-z grass_block-block156 position-1)

	(block-present grass_block-block156)
	(at-x grass_block-block157 position-3)

	(at-y grass_block-block157 position3)

	(at-z grass_block-block157 position0)

	(block-present grass_block-block157)
	(at-x grass_block-block158 position-3)

	(at-y grass_block-block158 position3)

	(at-z grass_block-block158 position1)

	(block-present grass_block-block158)
	(at-x grass_block-block159 position-3)

	(at-y grass_block-block159 position3)

	(at-z grass_block-block159 position2)

	(block-present grass_block-block159)
	(at-x grass_block-block160 position-3)

	(at-y grass_block-block160 position3)

	(at-z grass_block-block160 position3)

	(block-present grass_block-block160)
	(at-x grass_block-block161 position-3)

	(at-y grass_block-block161 position3)

	(at-z grass_block-block161 position4)

	(block-present grass_block-block161)
	(at-x grass_block-block162 position-3)

	(at-y grass_block-block162 position3)

	(at-z grass_block-block162 position5)

	(block-present grass_block-block162)
	(at-x grass_block-block163 position-3)

	(at-y grass_block-block163 position3)

	(at-z grass_block-block163 position6)

	(block-present grass_block-block163)
	(at-x grass_block-block164 position-3)

	(at-y grass_block-block164 position3)

	(at-z grass_block-block164 position7)

	(block-present grass_block-block164)
	(at-x grass_block-block165 position-3)

	(at-y grass_block-block165 position3)

	(at-z grass_block-block165 position8)

	(block-present grass_block-block165)
	(at-x grass_block-block166 position-3)

	(at-y grass_block-block166 position3)

	(at-z grass_block-block166 position9)

	(block-present grass_block-block166)
	(at-x grass_block-block167 position-3)

	(at-y grass_block-block167 position3)

	(at-z grass_block-block167 position10)

	(block-present grass_block-block167)
	(at-x grass_block-block168 position-2)

	(at-y grass_block-block168 position3)

	(at-z grass_block-block168 position-10)

	(block-present grass_block-block168)
	(at-x grass_block-block169 position-2)

	(at-y grass_block-block169 position3)

	(at-z grass_block-block169 position-9)

	(block-present grass_block-block169)
	(at-x grass_block-block170 position-2)

	(at-y grass_block-block170 position3)

	(at-z grass_block-block170 position-8)

	(block-present grass_block-block170)
	(at-x grass_block-block171 position-2)

	(at-y grass_block-block171 position3)

	(at-z grass_block-block171 position-7)

	(block-present grass_block-block171)
	(at-x grass_block-block172 position-2)

	(at-y grass_block-block172 position3)

	(at-z grass_block-block172 position-6)

	(block-present grass_block-block172)
	(at-x grass_block-block173 position-2)

	(at-y grass_block-block173 position3)

	(at-z grass_block-block173 position-5)

	(block-present grass_block-block173)
	(at-x grass_block-block174 position-2)

	(at-y grass_block-block174 position3)

	(at-z grass_block-block174 position-4)

	(block-present grass_block-block174)
	(at-x grass_block-block175 position-2)

	(at-y grass_block-block175 position3)

	(at-z grass_block-block175 position-3)

	(block-present grass_block-block175)
	(at-x grass_block-block176 position-2)

	(at-y grass_block-block176 position3)

	(at-z grass_block-block176 position-2)

	(block-present grass_block-block176)
	(at-x grass_block-block177 position-2)

	(at-y grass_block-block177 position3)

	(at-z grass_block-block177 position-1)

	(block-present grass_block-block177)
	(at-x grass_block-block178 position-2)

	(at-y grass_block-block178 position3)

	(at-z grass_block-block178 position0)

	(block-present grass_block-block178)
	(at-x grass_block-block179 position-2)

	(at-y grass_block-block179 position3)

	(at-z grass_block-block179 position1)

	(block-present grass_block-block179)
	(at-x grass_block-block180 position-2)

	(at-y grass_block-block180 position3)

	(at-z grass_block-block180 position2)

	(block-present grass_block-block180)
	(at-x grass_block-block181 position-2)

	(at-y grass_block-block181 position3)

	(at-z grass_block-block181 position3)

	(block-present grass_block-block181)
	(at-x grass_block-block182 position-2)

	(at-y grass_block-block182 position3)

	(at-z grass_block-block182 position4)

	(block-present grass_block-block182)
	(at-x grass_block-block183 position-2)

	(at-y grass_block-block183 position3)

	(at-z grass_block-block183 position5)

	(block-present grass_block-block183)
	(at-x grass_block-block184 position-2)

	(at-y grass_block-block184 position3)

	(at-z grass_block-block184 position6)

	(block-present grass_block-block184)
	(at-x grass_block-block185 position-2)

	(at-y grass_block-block185 position3)

	(at-z grass_block-block185 position7)

	(block-present grass_block-block185)
	(at-x grass_block-block186 position-2)

	(at-y grass_block-block186 position3)

	(at-z grass_block-block186 position8)

	(block-present grass_block-block186)
	(at-x grass_block-block187 position-2)

	(at-y grass_block-block187 position3)

	(at-z grass_block-block187 position9)

	(block-present grass_block-block187)
	(at-x grass_block-block188 position-2)

	(at-y grass_block-block188 position3)

	(at-z grass_block-block188 position10)

	(block-present grass_block-block188)
	(at-x grass_block-block189 position-1)

	(at-y grass_block-block189 position3)

	(at-z grass_block-block189 position-10)

	(block-present grass_block-block189)
	(at-x grass_block-block190 position-1)

	(at-y grass_block-block190 position3)

	(at-z grass_block-block190 position-9)

	(block-present grass_block-block190)
	(at-x grass_block-block191 position-1)

	(at-y grass_block-block191 position3)

	(at-z grass_block-block191 position-8)

	(block-present grass_block-block191)
	(at-x grass_block-block192 position-1)

	(at-y grass_block-block192 position3)

	(at-z grass_block-block192 position-7)

	(block-present grass_block-block192)
	(at-x grass_block-block193 position-1)

	(at-y grass_block-block193 position3)

	(at-z grass_block-block193 position-6)

	(block-present grass_block-block193)
	(at-x grass_block-block194 position-1)

	(at-y grass_block-block194 position3)

	(at-z grass_block-block194 position-5)

	(block-present grass_block-block194)
	(at-x grass_block-block195 position-1)

	(at-y grass_block-block195 position3)

	(at-z grass_block-block195 position-4)

	(block-present grass_block-block195)
	(at-x grass_block-block196 position-1)

	(at-y grass_block-block196 position3)

	(at-z grass_block-block196 position-3)

	(block-present grass_block-block196)
	(at-x grass_block-block197 position-1)

	(at-y grass_block-block197 position3)

	(at-z grass_block-block197 position-2)

	(block-present grass_block-block197)
	(at-x grass_block-block198 position-1)

	(at-y grass_block-block198 position3)

	(at-z grass_block-block198 position-1)

	(block-present grass_block-block198)
	(at-x grass_block-block199 position-1)

	(at-y grass_block-block199 position3)

	(at-z grass_block-block199 position0)

	(block-present grass_block-block199)
	(at-x grass_block-block200 position-1)

	(at-y grass_block-block200 position3)

	(at-z grass_block-block200 position1)

	(block-present grass_block-block200)
	(at-x grass_block-block201 position-1)

	(at-y grass_block-block201 position3)

	(at-z grass_block-block201 position2)

	(block-present grass_block-block201)
	(at-x grass_block-block202 position-1)

	(at-y grass_block-block202 position3)

	(at-z grass_block-block202 position3)

	(block-present grass_block-block202)
	(at-x grass_block-block203 position-1)

	(at-y grass_block-block203 position3)

	(at-z grass_block-block203 position4)

	(block-present grass_block-block203)
	(at-x grass_block-block204 position-1)

	(at-y grass_block-block204 position3)

	(at-z grass_block-block204 position5)

	(block-present grass_block-block204)
	(at-x grass_block-block205 position-1)

	(at-y grass_block-block205 position3)

	(at-z grass_block-block205 position6)

	(block-present grass_block-block205)
	(at-x grass_block-block206 position-1)

	(at-y grass_block-block206 position3)

	(at-z grass_block-block206 position7)

	(block-present grass_block-block206)
	(at-x grass_block-block207 position-1)

	(at-y grass_block-block207 position3)

	(at-z grass_block-block207 position8)

	(block-present grass_block-block207)
	(at-x grass_block-block208 position-1)

	(at-y grass_block-block208 position3)

	(at-z grass_block-block208 position9)

	(block-present grass_block-block208)
	(at-x grass_block-block209 position-1)

	(at-y grass_block-block209 position3)

	(at-z grass_block-block209 position10)

	(block-present grass_block-block209)
	(at-x grass_block-block210 position0)

	(at-y grass_block-block210 position3)

	(at-z grass_block-block210 position-10)

	(block-present grass_block-block210)
	(at-x grass_block-block211 position0)

	(at-y grass_block-block211 position3)

	(at-z grass_block-block211 position-9)

	(block-present grass_block-block211)
	(at-x grass_block-block212 position0)

	(at-y grass_block-block212 position3)

	(at-z grass_block-block212 position-8)

	(block-present grass_block-block212)
	(at-x grass_block-block213 position0)

	(at-y grass_block-block213 position3)

	(at-z grass_block-block213 position-7)

	(block-present grass_block-block213)
	(at-x grass_block-block214 position0)

	(at-y grass_block-block214 position3)

	(at-z grass_block-block214 position-6)

	(block-present grass_block-block214)
	(at-x grass_block-block215 position0)

	(at-y grass_block-block215 position3)

	(at-z grass_block-block215 position-5)

	(block-present grass_block-block215)
	(at-x grass_block-block216 position0)

	(at-y grass_block-block216 position3)

	(at-z grass_block-block216 position-4)

	(block-present grass_block-block216)
	(at-x grass_block-block217 position0)

	(at-y grass_block-block217 position3)

	(at-z grass_block-block217 position-3)

	(block-present grass_block-block217)
	(at-x grass_block-block218 position0)

	(at-y grass_block-block218 position3)

	(at-z grass_block-block218 position-2)

	(block-present grass_block-block218)
	(at-x grass_block-block219 position0)

	(at-y grass_block-block219 position3)

	(at-z grass_block-block219 position-1)

	(block-present grass_block-block219)
	(at-x grass_block-block220 position0)

	(at-y grass_block-block220 position3)

	(at-z grass_block-block220 position0)

	(block-present grass_block-block220)
	(at-x grass_block-block221 position0)

	(at-y grass_block-block221 position3)

	(at-z grass_block-block221 position1)

	(block-present grass_block-block221)
	(at-x grass_block-block222 position0)

	(at-y grass_block-block222 position3)

	(at-z grass_block-block222 position2)

	(block-present grass_block-block222)
	(at-x grass_block-block223 position0)

	(at-y grass_block-block223 position3)

	(at-z grass_block-block223 position3)

	(block-present grass_block-block223)
	(at-x grass_block-block224 position0)

	(at-y grass_block-block224 position3)

	(at-z grass_block-block224 position4)

	(block-present grass_block-block224)
	(at-x grass_block-block225 position0)

	(at-y grass_block-block225 position3)

	(at-z grass_block-block225 position5)

	(block-present grass_block-block225)
	(at-x grass_block-block226 position0)

	(at-y grass_block-block226 position3)

	(at-z grass_block-block226 position6)

	(block-present grass_block-block226)
	(at-x grass_block-block227 position0)

	(at-y grass_block-block227 position3)

	(at-z grass_block-block227 position7)

	(block-present grass_block-block227)
	(at-x grass_block-block228 position0)

	(at-y grass_block-block228 position3)

	(at-z grass_block-block228 position8)

	(block-present grass_block-block228)
	(at-x grass_block-block229 position0)

	(at-y grass_block-block229 position3)

	(at-z grass_block-block229 position9)

	(block-present grass_block-block229)
	(at-x grass_block-block230 position0)

	(at-y grass_block-block230 position3)

	(at-z grass_block-block230 position10)

	(block-present grass_block-block230)
	(at-x grass_block-block231 position1)

	(at-y grass_block-block231 position3)

	(at-z grass_block-block231 position-10)

	(block-present grass_block-block231)
	(at-x grass_block-block232 position1)

	(at-y grass_block-block232 position3)

	(at-z grass_block-block232 position-9)

	(block-present grass_block-block232)
	(at-x grass_block-block233 position1)

	(at-y grass_block-block233 position3)

	(at-z grass_block-block233 position-8)

	(block-present grass_block-block233)
	(at-x grass_block-block234 position1)

	(at-y grass_block-block234 position3)

	(at-z grass_block-block234 position-7)

	(block-present grass_block-block234)
	(at-x grass_block-block235 position1)

	(at-y grass_block-block235 position3)

	(at-z grass_block-block235 position-6)

	(block-present grass_block-block235)
	(at-x grass_block-block236 position1)

	(at-y grass_block-block236 position3)

	(at-z grass_block-block236 position-5)

	(block-present grass_block-block236)
	(at-x grass_block-block237 position1)

	(at-y grass_block-block237 position3)

	(at-z grass_block-block237 position-4)

	(block-present grass_block-block237)
	(at-x grass_block-block238 position1)

	(at-y grass_block-block238 position3)

	(at-z grass_block-block238 position-3)

	(block-present grass_block-block238)
	(at-x grass_block-block239 position1)

	(at-y grass_block-block239 position3)

	(at-z grass_block-block239 position-2)

	(block-present grass_block-block239)
	(at-x grass_block-block240 position1)

	(at-y grass_block-block240 position3)

	(at-z grass_block-block240 position-1)

	(block-present grass_block-block240)
	(at-x grass_block-block241 position1)

	(at-y grass_block-block241 position3)

	(at-z grass_block-block241 position0)

	(block-present grass_block-block241)
	(at-x grass_block-block242 position1)

	(at-y grass_block-block242 position3)

	(at-z grass_block-block242 position1)

	(block-present grass_block-block242)
	(at-x grass_block-block243 position1)

	(at-y grass_block-block243 position3)

	(at-z grass_block-block243 position2)

	(block-present grass_block-block243)
	(at-x grass_block-block244 position1)

	(at-y grass_block-block244 position3)

	(at-z grass_block-block244 position3)

	(block-present grass_block-block244)
	(at-x grass_block-block245 position1)

	(at-y grass_block-block245 position3)

	(at-z grass_block-block245 position4)

	(block-present grass_block-block245)
	(at-x grass_block-block246 position1)

	(at-y grass_block-block246 position3)

	(at-z grass_block-block246 position5)

	(block-present grass_block-block246)
	(at-x grass_block-block247 position1)

	(at-y grass_block-block247 position3)

	(at-z grass_block-block247 position6)

	(block-present grass_block-block247)
	(at-x grass_block-block248 position1)

	(at-y grass_block-block248 position3)

	(at-z grass_block-block248 position7)

	(block-present grass_block-block248)
	(at-x grass_block-block249 position1)

	(at-y grass_block-block249 position3)

	(at-z grass_block-block249 position8)

	(block-present grass_block-block249)
	(at-x grass_block-block250 position1)

	(at-y grass_block-block250 position3)

	(at-z grass_block-block250 position9)

	(block-present grass_block-block250)
	(at-x grass_block-block251 position1)

	(at-y grass_block-block251 position3)

	(at-z grass_block-block251 position10)

	(block-present grass_block-block251)
	(at-x grass_block-block252 position2)

	(at-y grass_block-block252 position3)

	(at-z grass_block-block252 position-10)

	(block-present grass_block-block252)
	(at-x grass_block-block253 position2)

	(at-y grass_block-block253 position3)

	(at-z grass_block-block253 position-9)

	(block-present grass_block-block253)
	(at-x grass_block-block254 position2)

	(at-y grass_block-block254 position3)

	(at-z grass_block-block254 position-8)

	(block-present grass_block-block254)
	(at-x grass_block-block255 position2)

	(at-y grass_block-block255 position3)

	(at-z grass_block-block255 position-7)

	(block-present grass_block-block255)
	(at-x grass_block-block256 position2)

	(at-y grass_block-block256 position3)

	(at-z grass_block-block256 position-6)

	(block-present grass_block-block256)
	(at-x grass_block-block257 position2)

	(at-y grass_block-block257 position3)

	(at-z grass_block-block257 position-5)

	(block-present grass_block-block257)
	(at-x grass_block-block258 position2)

	(at-y grass_block-block258 position3)

	(at-z grass_block-block258 position-4)

	(block-present grass_block-block258)
	(at-x grass_block-block259 position2)

	(at-y grass_block-block259 position3)

	(at-z grass_block-block259 position-3)

	(block-present grass_block-block259)
	(at-x grass_block-block260 position2)

	(at-y grass_block-block260 position3)

	(at-z grass_block-block260 position-2)

	(block-present grass_block-block260)
	(at-x grass_block-block261 position2)

	(at-y grass_block-block261 position3)

	(at-z grass_block-block261 position-1)

	(block-present grass_block-block261)
	(at-x grass_block-block262 position2)

	(at-y grass_block-block262 position3)

	(at-z grass_block-block262 position0)

	(block-present grass_block-block262)
	(at-x grass_block-block263 position2)

	(at-y grass_block-block263 position3)

	(at-z grass_block-block263 position1)

	(block-present grass_block-block263)
	(at-x grass_block-block264 position2)

	(at-y grass_block-block264 position3)

	(at-z grass_block-block264 position2)

	(block-present grass_block-block264)
	(at-x grass_block-block265 position2)

	(at-y grass_block-block265 position3)

	(at-z grass_block-block265 position3)

	(block-present grass_block-block265)
	(at-x grass_block-block266 position2)

	(at-y grass_block-block266 position3)

	(at-z grass_block-block266 position4)

	(block-present grass_block-block266)
	(at-x grass_block-block267 position2)

	(at-y grass_block-block267 position3)

	(at-z grass_block-block267 position5)

	(block-present grass_block-block267)
	(at-x grass_block-block268 position2)

	(at-y grass_block-block268 position3)

	(at-z grass_block-block268 position6)

	(block-present grass_block-block268)
	(at-x grass_block-block269 position2)

	(at-y grass_block-block269 position3)

	(at-z grass_block-block269 position7)

	(block-present grass_block-block269)
	(at-x grass_block-block270 position2)

	(at-y grass_block-block270 position3)

	(at-z grass_block-block270 position8)

	(block-present grass_block-block270)
	(at-x grass_block-block271 position2)

	(at-y grass_block-block271 position3)

	(at-z grass_block-block271 position9)

	(block-present grass_block-block271)
	(at-x grass_block-block272 position2)

	(at-y grass_block-block272 position3)

	(at-z grass_block-block272 position10)

	(block-present grass_block-block272)
	(at-x grass_block-block273 position3)

	(at-y grass_block-block273 position3)

	(at-z grass_block-block273 position-10)

	(block-present grass_block-block273)
	(at-x grass_block-block274 position3)

	(at-y grass_block-block274 position3)

	(at-z grass_block-block274 position-9)

	(block-present grass_block-block274)
	(at-x grass_block-block275 position3)

	(at-y grass_block-block275 position3)

	(at-z grass_block-block275 position-8)

	(block-present grass_block-block275)
	(at-x grass_block-block276 position3)

	(at-y grass_block-block276 position3)

	(at-z grass_block-block276 position-7)

	(block-present grass_block-block276)
	(at-x grass_block-block277 position3)

	(at-y grass_block-block277 position3)

	(at-z grass_block-block277 position-6)

	(block-present grass_block-block277)
	(at-x grass_block-block278 position3)

	(at-y grass_block-block278 position3)

	(at-z grass_block-block278 position-5)

	(block-present grass_block-block278)
	(at-x grass_block-block279 position3)

	(at-y grass_block-block279 position3)

	(at-z grass_block-block279 position-4)

	(block-present grass_block-block279)
	(at-x grass_block-block280 position3)

	(at-y grass_block-block280 position3)

	(at-z grass_block-block280 position-3)

	(block-present grass_block-block280)
	(at-x grass_block-block281 position3)

	(at-y grass_block-block281 position3)

	(at-z grass_block-block281 position-2)

	(block-present grass_block-block281)
	(at-x grass_block-block282 position3)

	(at-y grass_block-block282 position3)

	(at-z grass_block-block282 position-1)

	(block-present grass_block-block282)
	(at-x grass_block-block283 position3)

	(at-y grass_block-block283 position3)

	(at-z grass_block-block283 position0)

	(block-present grass_block-block283)
	(at-x grass_block-block284 position3)

	(at-y grass_block-block284 position3)

	(at-z grass_block-block284 position1)

	(block-present grass_block-block284)
	(at-x grass_block-block285 position3)

	(at-y grass_block-block285 position3)

	(at-z grass_block-block285 position2)

	(block-present grass_block-block285)
	(at-x grass_block-block286 position3)

	(at-y grass_block-block286 position3)

	(at-z grass_block-block286 position3)

	(block-present grass_block-block286)
	(at-x grass_block-block287 position3)

	(at-y grass_block-block287 position3)

	(at-z grass_block-block287 position4)

	(block-present grass_block-block287)
	(at-x grass_block-block288 position3)

	(at-y grass_block-block288 position3)

	(at-z grass_block-block288 position5)

	(block-present grass_block-block288)
	(at-x grass_block-block289 position3)

	(at-y grass_block-block289 position3)

	(at-z grass_block-block289 position6)

	(block-present grass_block-block289)
	(at-x grass_block-block290 position3)

	(at-y grass_block-block290 position3)

	(at-z grass_block-block290 position7)

	(block-present grass_block-block290)
	(at-x grass_block-block291 position3)

	(at-y grass_block-block291 position3)

	(at-z grass_block-block291 position8)

	(block-present grass_block-block291)
	(at-x grass_block-block292 position3)

	(at-y grass_block-block292 position3)

	(at-z grass_block-block292 position9)

	(block-present grass_block-block292)
	(at-x grass_block-block293 position3)

	(at-y grass_block-block293 position3)

	(at-z grass_block-block293 position10)

	(block-present grass_block-block293)
	(at-x grass_block-block294 position4)

	(at-y grass_block-block294 position3)

	(at-z grass_block-block294 position-10)

	(block-present grass_block-block294)
	(at-x grass_block-block295 position4)

	(at-y grass_block-block295 position3)

	(at-z grass_block-block295 position-9)

	(block-present grass_block-block295)
	(at-x grass_block-block296 position4)

	(at-y grass_block-block296 position3)

	(at-z grass_block-block296 position-8)

	(block-present grass_block-block296)
	(at-x grass_block-block297 position4)

	(at-y grass_block-block297 position3)

	(at-z grass_block-block297 position-7)

	(block-present grass_block-block297)
	(at-x grass_block-block298 position4)

	(at-y grass_block-block298 position3)

	(at-z grass_block-block298 position-6)

	(block-present grass_block-block298)
	(at-x grass_block-block299 position4)

	(at-y grass_block-block299 position3)

	(at-z grass_block-block299 position-5)

	(block-present grass_block-block299)
	(at-x grass_block-block300 position4)

	(at-y grass_block-block300 position3)

	(at-z grass_block-block300 position-4)

	(block-present grass_block-block300)
	(at-x grass_block-block301 position4)

	(at-y grass_block-block301 position3)

	(at-z grass_block-block301 position-3)

	(block-present grass_block-block301)
	(at-x grass_block-block302 position4)

	(at-y grass_block-block302 position3)

	(at-z grass_block-block302 position-2)

	(block-present grass_block-block302)
	(at-x grass_block-block303 position4)

	(at-y grass_block-block303 position3)

	(at-z grass_block-block303 position-1)

	(block-present grass_block-block303)
	(at-x grass_block-block304 position4)

	(at-y grass_block-block304 position3)

	(at-z grass_block-block304 position0)

	(block-present grass_block-block304)
	(at-x grass_block-block305 position4)

	(at-y grass_block-block305 position3)

	(at-z grass_block-block305 position1)

	(block-present grass_block-block305)
	(at-x grass_block-block306 position4)

	(at-y grass_block-block306 position3)

	(at-z grass_block-block306 position2)

	(block-present grass_block-block306)
	(at-x grass_block-block307 position4)

	(at-y grass_block-block307 position3)

	(at-z grass_block-block307 position3)

	(block-present grass_block-block307)
	(at-x grass_block-block308 position4)

	(at-y grass_block-block308 position3)

	(at-z grass_block-block308 position4)

	(block-present grass_block-block308)
	(at-x grass_block-block309 position4)

	(at-y grass_block-block309 position3)

	(at-z grass_block-block309 position5)

	(block-present grass_block-block309)
	(at-x grass_block-block310 position4)

	(at-y grass_block-block310 position3)

	(at-z grass_block-block310 position6)

	(block-present grass_block-block310)
	(at-x grass_block-block311 position4)

	(at-y grass_block-block311 position3)

	(at-z grass_block-block311 position7)

	(block-present grass_block-block311)
	(at-x grass_block-block312 position4)

	(at-y grass_block-block312 position3)

	(at-z grass_block-block312 position8)

	(block-present grass_block-block312)
	(at-x grass_block-block313 position4)

	(at-y grass_block-block313 position3)

	(at-z grass_block-block313 position9)

	(block-present grass_block-block313)
	(at-x grass_block-block314 position4)

	(at-y grass_block-block314 position3)

	(at-z grass_block-block314 position10)

	(block-present grass_block-block314)
	(at-x grass_block-block315 position5)

	(at-y grass_block-block315 position3)

	(at-z grass_block-block315 position-10)

	(block-present grass_block-block315)
	(at-x grass_block-block316 position5)

	(at-y grass_block-block316 position3)

	(at-z grass_block-block316 position-9)

	(block-present grass_block-block316)
	(at-x grass_block-block317 position5)

	(at-y grass_block-block317 position3)

	(at-z grass_block-block317 position-8)

	(block-present grass_block-block317)
	(at-x grass_block-block318 position5)

	(at-y grass_block-block318 position3)

	(at-z grass_block-block318 position-7)

	(block-present grass_block-block318)
	(at-x grass_block-block319 position5)

	(at-y grass_block-block319 position3)

	(at-z grass_block-block319 position-6)

	(block-present grass_block-block319)
	(at-x grass_block-block320 position5)

	(at-y grass_block-block320 position3)

	(at-z grass_block-block320 position-5)

	(block-present grass_block-block320)
	(at-x grass_block-block321 position5)

	(at-y grass_block-block321 position3)

	(at-z grass_block-block321 position-4)

	(block-present grass_block-block321)
	(at-x grass_block-block322 position5)

	(at-y grass_block-block322 position3)

	(at-z grass_block-block322 position-3)

	(block-present grass_block-block322)
	(at-x grass_block-block323 position5)

	(at-y grass_block-block323 position3)

	(at-z grass_block-block323 position-2)

	(block-present grass_block-block323)
	(at-x grass_block-block324 position5)

	(at-y grass_block-block324 position3)

	(at-z grass_block-block324 position-1)

	(block-present grass_block-block324)
	(at-x grass_block-block325 position5)

	(at-y grass_block-block325 position3)

	(at-z grass_block-block325 position0)

	(block-present grass_block-block325)
	(at-x grass_block-block326 position5)

	(at-y grass_block-block326 position3)

	(at-z grass_block-block326 position1)

	(block-present grass_block-block326)
	(at-x grass_block-block327 position5)

	(at-y grass_block-block327 position3)

	(at-z grass_block-block327 position2)

	(block-present grass_block-block327)
	(at-x grass_block-block328 position5)

	(at-y grass_block-block328 position3)

	(at-z grass_block-block328 position3)

	(block-present grass_block-block328)
	(at-x grass_block-block329 position5)

	(at-y grass_block-block329 position3)

	(at-z grass_block-block329 position4)

	(block-present grass_block-block329)
	(at-x grass_block-block330 position5)

	(at-y grass_block-block330 position3)

	(at-z grass_block-block330 position5)

	(block-present grass_block-block330)
	(at-x grass_block-block331 position5)

	(at-y grass_block-block331 position3)

	(at-z grass_block-block331 position6)

	(block-present grass_block-block331)
	(at-x grass_block-block332 position5)

	(at-y grass_block-block332 position3)

	(at-z grass_block-block332 position7)

	(block-present grass_block-block332)
	(at-x grass_block-block333 position5)

	(at-y grass_block-block333 position3)

	(at-z grass_block-block333 position8)

	(block-present grass_block-block333)
	(at-x grass_block-block334 position5)

	(at-y grass_block-block334 position3)

	(at-z grass_block-block334 position9)

	(block-present grass_block-block334)
	(at-x grass_block-block335 position5)

	(at-y grass_block-block335 position3)

	(at-z grass_block-block335 position10)

	(block-present grass_block-block335)
	(at-x grass_block-block336 position6)

	(at-y grass_block-block336 position3)

	(at-z grass_block-block336 position-10)

	(block-present grass_block-block336)
	(at-x grass_block-block337 position6)

	(at-y grass_block-block337 position3)

	(at-z grass_block-block337 position-9)

	(block-present grass_block-block337)
	(at-x grass_block-block338 position6)

	(at-y grass_block-block338 position3)

	(at-z grass_block-block338 position-8)

	(block-present grass_block-block338)
	(at-x grass_block-block339 position6)

	(at-y grass_block-block339 position3)

	(at-z grass_block-block339 position-7)

	(block-present grass_block-block339)
	(at-x grass_block-block340 position6)

	(at-y grass_block-block340 position3)

	(at-z grass_block-block340 position-6)

	(block-present grass_block-block340)
	(at-x grass_block-block341 position6)

	(at-y grass_block-block341 position3)

	(at-z grass_block-block341 position-5)

	(block-present grass_block-block341)
	(at-x grass_block-block342 position6)

	(at-y grass_block-block342 position3)

	(at-z grass_block-block342 position-4)

	(block-present grass_block-block342)
	(at-x grass_block-block343 position6)

	(at-y grass_block-block343 position3)

	(at-z grass_block-block343 position-3)

	(block-present grass_block-block343)
	(at-x grass_block-block344 position6)

	(at-y grass_block-block344 position3)

	(at-z grass_block-block344 position-2)

	(block-present grass_block-block344)
	(at-x grass_block-block345 position6)

	(at-y grass_block-block345 position3)

	(at-z grass_block-block345 position-1)

	(block-present grass_block-block345)
	(at-x grass_block-block346 position6)

	(at-y grass_block-block346 position3)

	(at-z grass_block-block346 position0)

	(block-present grass_block-block346)
	(at-x grass_block-block347 position6)

	(at-y grass_block-block347 position3)

	(at-z grass_block-block347 position1)

	(block-present grass_block-block347)
	(at-x grass_block-block348 position6)

	(at-y grass_block-block348 position3)

	(at-z grass_block-block348 position2)

	(block-present grass_block-block348)
	(at-x grass_block-block349 position6)

	(at-y grass_block-block349 position3)

	(at-z grass_block-block349 position3)

	(block-present grass_block-block349)
	(at-x grass_block-block350 position6)

	(at-y grass_block-block350 position3)

	(at-z grass_block-block350 position4)

	(block-present grass_block-block350)
	(at-x grass_block-block351 position6)

	(at-y grass_block-block351 position3)

	(at-z grass_block-block351 position5)

	(block-present grass_block-block351)
	(at-x grass_block-block352 position6)

	(at-y grass_block-block352 position3)

	(at-z grass_block-block352 position6)

	(block-present grass_block-block352)
	(at-x grass_block-block353 position6)

	(at-y grass_block-block353 position3)

	(at-z grass_block-block353 position7)

	(block-present grass_block-block353)
	(at-x grass_block-block354 position6)

	(at-y grass_block-block354 position3)

	(at-z grass_block-block354 position8)

	(block-present grass_block-block354)
	(at-x grass_block-block355 position6)

	(at-y grass_block-block355 position3)

	(at-z grass_block-block355 position9)

	(block-present grass_block-block355)
	(at-x grass_block-block356 position6)

	(at-y grass_block-block356 position3)

	(at-z grass_block-block356 position10)

	(block-present grass_block-block356)
	(at-x grass_block-block357 position7)

	(at-y grass_block-block357 position3)

	(at-z grass_block-block357 position-10)

	(block-present grass_block-block357)
	(at-x grass_block-block358 position7)

	(at-y grass_block-block358 position3)

	(at-z grass_block-block358 position-9)

	(block-present grass_block-block358)
	(at-x grass_block-block359 position7)

	(at-y grass_block-block359 position3)

	(at-z grass_block-block359 position-8)

	(block-present grass_block-block359)
	(at-x grass_block-block360 position7)

	(at-y grass_block-block360 position3)

	(at-z grass_block-block360 position-7)

	(block-present grass_block-block360)
	(at-x grass_block-block361 position7)

	(at-y grass_block-block361 position3)

	(at-z grass_block-block361 position-6)

	(block-present grass_block-block361)
	(at-x grass_block-block362 position7)

	(at-y grass_block-block362 position3)

	(at-z grass_block-block362 position-5)

	(block-present grass_block-block362)
	(at-x grass_block-block363 position7)

	(at-y grass_block-block363 position3)

	(at-z grass_block-block363 position-4)

	(block-present grass_block-block363)
	(at-x grass_block-block364 position7)

	(at-y grass_block-block364 position3)

	(at-z grass_block-block364 position-3)

	(block-present grass_block-block364)
	(at-x grass_block-block365 position7)

	(at-y grass_block-block365 position3)

	(at-z grass_block-block365 position-2)

	(block-present grass_block-block365)
	(at-x grass_block-block366 position7)

	(at-y grass_block-block366 position3)

	(at-z grass_block-block366 position-1)

	(block-present grass_block-block366)
	(at-x grass_block-block367 position7)

	(at-y grass_block-block367 position3)

	(at-z grass_block-block367 position0)

	(block-present grass_block-block367)
	(at-x grass_block-block368 position7)

	(at-y grass_block-block368 position3)

	(at-z grass_block-block368 position1)

	(block-present grass_block-block368)
	(at-x grass_block-block369 position7)

	(at-y grass_block-block369 position3)

	(at-z grass_block-block369 position2)

	(block-present grass_block-block369)
	(at-x grass_block-block370 position7)

	(at-y grass_block-block370 position3)

	(at-z grass_block-block370 position3)

	(block-present grass_block-block370)
	(at-x grass_block-block371 position7)

	(at-y grass_block-block371 position3)

	(at-z grass_block-block371 position4)

	(block-present grass_block-block371)
	(at-x grass_block-block372 position7)

	(at-y grass_block-block372 position3)

	(at-z grass_block-block372 position5)

	(block-present grass_block-block372)
	(at-x grass_block-block373 position7)

	(at-y grass_block-block373 position3)

	(at-z grass_block-block373 position6)

	(block-present grass_block-block373)
	(at-x grass_block-block374 position7)

	(at-y grass_block-block374 position3)

	(at-z grass_block-block374 position7)

	(block-present grass_block-block374)
	(at-x grass_block-block375 position7)

	(at-y grass_block-block375 position3)

	(at-z grass_block-block375 position8)

	(block-present grass_block-block375)
	(at-x grass_block-block376 position7)

	(at-y grass_block-block376 position3)

	(at-z grass_block-block376 position9)

	(block-present grass_block-block376)
	(at-x grass_block-block377 position7)

	(at-y grass_block-block377 position3)

	(at-z grass_block-block377 position10)

	(block-present grass_block-block377)
	(at-x grass_block-block378 position8)

	(at-y grass_block-block378 position3)

	(at-z grass_block-block378 position-10)

	(block-present grass_block-block378)
	(at-x grass_block-block379 position8)

	(at-y grass_block-block379 position3)

	(at-z grass_block-block379 position-9)

	(block-present grass_block-block379)
	(at-x grass_block-block380 position8)

	(at-y grass_block-block380 position3)

	(at-z grass_block-block380 position-8)

	(block-present grass_block-block380)
	(at-x grass_block-block381 position8)

	(at-y grass_block-block381 position3)

	(at-z grass_block-block381 position-7)

	(block-present grass_block-block381)
	(at-x grass_block-block382 position8)

	(at-y grass_block-block382 position3)

	(at-z grass_block-block382 position-6)

	(block-present grass_block-block382)
	(at-x grass_block-block383 position8)

	(at-y grass_block-block383 position3)

	(at-z grass_block-block383 position-5)

	(block-present grass_block-block383)
	(at-x grass_block-block384 position8)

	(at-y grass_block-block384 position3)

	(at-z grass_block-block384 position-4)

	(block-present grass_block-block384)
	(at-x grass_block-block385 position8)

	(at-y grass_block-block385 position3)

	(at-z grass_block-block385 position-3)

	(block-present grass_block-block385)
	(at-x grass_block-block386 position8)

	(at-y grass_block-block386 position3)

	(at-z grass_block-block386 position-2)

	(block-present grass_block-block386)
	(at-x grass_block-block387 position8)

	(at-y grass_block-block387 position3)

	(at-z grass_block-block387 position-1)

	(block-present grass_block-block387)
	(at-x grass_block-block388 position8)

	(at-y grass_block-block388 position3)

	(at-z grass_block-block388 position0)

	(block-present grass_block-block388)
	(at-x grass_block-block389 position8)

	(at-y grass_block-block389 position3)

	(at-z grass_block-block389 position1)

	(block-present grass_block-block389)
	(at-x grass_block-block390 position8)

	(at-y grass_block-block390 position3)

	(at-z grass_block-block390 position2)

	(block-present grass_block-block390)
	(at-x grass_block-block391 position8)

	(at-y grass_block-block391 position3)

	(at-z grass_block-block391 position3)

	(block-present grass_block-block391)
	(at-x grass_block-block392 position8)

	(at-y grass_block-block392 position3)

	(at-z grass_block-block392 position4)

	(block-present grass_block-block392)
	(at-x grass_block-block393 position8)

	(at-y grass_block-block393 position3)

	(at-z grass_block-block393 position5)

	(block-present grass_block-block393)
	(at-x grass_block-block394 position8)

	(at-y grass_block-block394 position3)

	(at-z grass_block-block394 position6)

	(block-present grass_block-block394)
	(at-x grass_block-block395 position8)

	(at-y grass_block-block395 position3)

	(at-z grass_block-block395 position7)

	(block-present grass_block-block395)
	(at-x grass_block-block396 position8)

	(at-y grass_block-block396 position3)

	(at-z grass_block-block396 position8)

	(block-present grass_block-block396)
	(at-x grass_block-block397 position8)

	(at-y grass_block-block397 position3)

	(at-z grass_block-block397 position9)

	(block-present grass_block-block397)
	(at-x grass_block-block398 position8)

	(at-y grass_block-block398 position3)

	(at-z grass_block-block398 position10)

	(block-present grass_block-block398)
	(at-x grass_block-block399 position9)

	(at-y grass_block-block399 position3)

	(at-z grass_block-block399 position-10)

	(block-present grass_block-block399)
	(at-x grass_block-block400 position9)

	(at-y grass_block-block400 position3)

	(at-z grass_block-block400 position-9)

	(block-present grass_block-block400)
	(at-x grass_block-block401 position9)

	(at-y grass_block-block401 position3)

	(at-z grass_block-block401 position-8)

	(block-present grass_block-block401)
	(at-x grass_block-block402 position9)

	(at-y grass_block-block402 position3)

	(at-z grass_block-block402 position-7)

	(block-present grass_block-block402)
	(at-x grass_block-block403 position9)

	(at-y grass_block-block403 position3)

	(at-z grass_block-block403 position-6)

	(block-present grass_block-block403)
	(at-x grass_block-block404 position9)

	(at-y grass_block-block404 position3)

	(at-z grass_block-block404 position-5)

	(block-present grass_block-block404)
	(at-x grass_block-block405 position9)

	(at-y grass_block-block405 position3)

	(at-z grass_block-block405 position-4)

	(block-present grass_block-block405)
	(at-x grass_block-block406 position9)

	(at-y grass_block-block406 position3)

	(at-z grass_block-block406 position-3)

	(block-present grass_block-block406)
	(at-x grass_block-block407 position9)

	(at-y grass_block-block407 position3)

	(at-z grass_block-block407 position-2)

	(block-present grass_block-block407)
	(at-x grass_block-block408 position9)

	(at-y grass_block-block408 position3)

	(at-z grass_block-block408 position-1)

	(block-present grass_block-block408)
	(at-x grass_block-block409 position9)

	(at-y grass_block-block409 position3)

	(at-z grass_block-block409 position0)

	(block-present grass_block-block409)
	(at-x grass_block-block410 position9)

	(at-y grass_block-block410 position3)

	(at-z grass_block-block410 position1)

	(block-present grass_block-block410)
	(at-x grass_block-block411 position9)

	(at-y grass_block-block411 position3)

	(at-z grass_block-block411 position2)

	(block-present grass_block-block411)
	(at-x grass_block-block412 position9)

	(at-y grass_block-block412 position3)

	(at-z grass_block-block412 position3)

	(block-present grass_block-block412)
	(at-x grass_block-block413 position9)

	(at-y grass_block-block413 position3)

	(at-z grass_block-block413 position4)

	(block-present grass_block-block413)
	(at-x grass_block-block414 position9)

	(at-y grass_block-block414 position3)

	(at-z grass_block-block414 position5)

	(block-present grass_block-block414)
	(at-x grass_block-block415 position9)

	(at-y grass_block-block415 position3)

	(at-z grass_block-block415 position6)

	(block-present grass_block-block415)
	(at-x grass_block-block416 position9)

	(at-y grass_block-block416 position3)

	(at-z grass_block-block416 position7)

	(block-present grass_block-block416)
	(at-x grass_block-block417 position9)

	(at-y grass_block-block417 position3)

	(at-z grass_block-block417 position8)

	(block-present grass_block-block417)
	(at-x grass_block-block418 position9)

	(at-y grass_block-block418 position3)

	(at-z grass_block-block418 position9)

	(block-present grass_block-block418)
	(at-x grass_block-block419 position9)

	(at-y grass_block-block419 position3)

	(at-z grass_block-block419 position10)

	(block-present grass_block-block419)
	(at-x grass_block-block420 position10)

	(at-y grass_block-block420 position3)

	(at-z grass_block-block420 position-10)

	(block-present grass_block-block420)
	(at-x grass_block-block421 position10)

	(at-y grass_block-block421 position3)

	(at-z grass_block-block421 position-9)

	(block-present grass_block-block421)
	(at-x grass_block-block422 position10)

	(at-y grass_block-block422 position3)

	(at-z grass_block-block422 position-8)

	(block-present grass_block-block422)
	(at-x grass_block-block423 position10)

	(at-y grass_block-block423 position3)

	(at-z grass_block-block423 position-7)

	(block-present grass_block-block423)
	(at-x grass_block-block424 position10)

	(at-y grass_block-block424 position3)

	(at-z grass_block-block424 position-6)

	(block-present grass_block-block424)
	(at-x grass_block-block425 position10)

	(at-y grass_block-block425 position3)

	(at-z grass_block-block425 position-5)

	(block-present grass_block-block425)
	(at-x grass_block-block426 position10)

	(at-y grass_block-block426 position3)

	(at-z grass_block-block426 position-4)

	(block-present grass_block-block426)
	(at-x grass_block-block427 position10)

	(at-y grass_block-block427 position3)

	(at-z grass_block-block427 position-3)

	(block-present grass_block-block427)
	(at-x grass_block-block428 position10)

	(at-y grass_block-block428 position3)

	(at-z grass_block-block428 position-2)

	(block-present grass_block-block428)
	(at-x grass_block-block429 position10)

	(at-y grass_block-block429 position3)

	(at-z grass_block-block429 position-1)

	(block-present grass_block-block429)
	(at-x grass_block-block430 position10)

	(at-y grass_block-block430 position3)

	(at-z grass_block-block430 position0)

	(block-present grass_block-block430)
	(at-x grass_block-block431 position10)

	(at-y grass_block-block431 position3)

	(at-z grass_block-block431 position1)

	(block-present grass_block-block431)
	(at-x grass_block-block432 position10)

	(at-y grass_block-block432 position3)

	(at-z grass_block-block432 position2)

	(block-present grass_block-block432)
	(at-x grass_block-block433 position10)

	(at-y grass_block-block433 position3)

	(at-z grass_block-block433 position3)

	(block-present grass_block-block433)
	(at-x grass_block-block434 position10)

	(at-y grass_block-block434 position3)

	(at-z grass_block-block434 position4)

	(block-present grass_block-block434)
	(at-x grass_block-block435 position10)

	(at-y grass_block-block435 position3)

	(at-z grass_block-block435 position5)

	(block-present grass_block-block435)
	(at-x grass_block-block436 position10)

	(at-y grass_block-block436 position3)

	(at-z grass_block-block436 position6)

	(block-present grass_block-block436)
	(at-x grass_block-block437 position10)

	(at-y grass_block-block437 position3)

	(at-z grass_block-block437 position7)

	(block-present grass_block-block437)
	(at-x grass_block-block438 position10)

	(at-y grass_block-block438 position3)

	(at-z grass_block-block438 position8)

	(block-present grass_block-block438)
	(at-x grass_block-block439 position10)

	(at-y grass_block-block439 position3)

	(at-z grass_block-block439 position9)

	(block-present grass_block-block439)
	(at-x grass_block-block440 position10)

	(at-y grass_block-block440 position3)

	(at-z grass_block-block440 position10)

	(block-present grass_block-block440)
	(at-x stone-block0 position-4)

	(at-y stone-block0 position4)

	(at-z stone-block0 position-1)

	(block-present stone-block0)
	(at-x stone-block1 position6)

	(at-y stone-block1 position4)

	(at-z stone-block1 position0)

	(block-present stone-block1)
	(at-x stone-block2 position6)

	(at-y stone-block2 position5)

	(at-z stone-block2 position-3)

	(block-present stone-block2)
	(at-x planks-block0 position-3)

	(at-y planks-block0 position4)

	(at-z planks-block0 position0)

	(block-present planks-block0)
	(at-x planks-block1 position-2)

	(at-y planks-block1 position4)

	(at-z planks-block1 position-4)

	(block-present planks-block1)
	(at-x planks-block2 position0)

	(at-y planks-block2 position4)

	(at-z planks-block2 position5)

	(block-present planks-block2)
	(at-x planks-block3 position2)

	(at-y planks-block3 position4)

	(at-z planks-block3 position1)

	(block-present planks-block3)
	(at-x planks-block4 position6)

	(at-y planks-block4 position4)

	(at-z planks-block4 position-3)

	(block-present planks-block4)
	(at-x wool-block0 position-3)

	(at-y wool-block0 position5)

	(at-z wool-block0 position0)

	(block-present wool-block0)
	(at-x wool-block1 position2)

	(at-y wool-block1 position4)

	(at-z wool-block1 position0)

	(block-present wool-block1)
)
(:goal
	(and (goal-achieved steve))
		
)
)
