(define
	(problem beluga-problem_108_s150_j55_r6_oc31_f34)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 34, 35, 36}
		n00 - num
		n01 - num
		n02 - num
		n03 - num
		n04 - num
		n05 - num
		n06 - num
		n07 - num
		n08 - num
		n09 - num
		n10 - num
		n11 - num
		n12 - num
		n13 - num
		n14 - num
		n15 - num
		n16 - num
		n17 - num
		n18 - num
		n19 - num
		n20 - num
		n21 - num
		n22 - num
		n23 - num
		n24 - num
		n25 - num
		n26 - num
		n27 - num
		n28 - num
		n30 - num
		n31 - num
		n32 - num
		n34 - num
		n35 - num
		n36 - num
		; trailers:
		beluga_trailer_1 - trailer
		factory_trailer_1 - trailer
		factory_trailer_2 - trailer
		factory_trailer_3 - trailer
		; Racks:
		rack00 - rack
		rack01 - rack
		rack02 - rack
		rack03 - rack
		rack04 - rack
		rack05 - rack
		; Jigs:
		jig0001 - jig
		jig0002 - jig
		jig0003 - jig
		jig0004 - jig
		jig0005 - jig
		jig0006 - jig
		jig0007 - jig
		jig0008 - jig
		jig0009 - jig
		jig0010 - jig
		jig0011 - jig
		jig0012 - jig
		jig0013 - jig
		jig0014 - jig
		jig0015 - jig
		jig0016 - jig
		jig0017 - jig
		jig0018 - jig
		jig0019 - jig
		jig0020 - jig
		jig0021 - jig
		jig0022 - jig
		jig0023 - jig
		jig0024 - jig
		jig0025 - jig
		jig0026 - jig
		jig0027 - jig
		jig0028 - jig
		jig0029 - jig
		jig0030 - jig
		jig0031 - jig
		jig0032 - jig
		jig0033 - jig
		jig0034 - jig
		jig0035 - jig
		jig0036 - jig
		jig0037 - jig
		jig0038 - jig
		jig0039 - jig
		jig0040 - jig
		jig0041 - jig
		jig0042 - jig
		jig0043 - jig
		jig0044 - jig
		jig0045 - jig
		jig0046 - jig
		jig0047 - jig
		jig0048 - jig
		jig0049 - jig
		jig0050 - jig
		jig0051 - jig
		jig0052 - jig
		jig0053 - jig
		jig0054 - jig
		jig0055 - jig
		typeE - type
		typeD - type
		typeC - type
		typeB - type
		typeA - type
		; hangars:
		hangar1 - hangar
		hangar2 - hangar
		hangar3 - hangar
		; Beluga flights:
		beluga1 - beluga
		beluga2 - beluga
		beluga3 - beluga
		beluga4 - beluga
		beluga5 - beluga
		beluga6 - beluga
		beluga7 - beluga
		beluga8 - beluga
		beluga9 - beluga
		beluga10 - beluga
		beluga11 - beluga
		beluga12 - beluga
		beluga13 - beluga
		beluga14 - beluga
		beluga15 - beluga
		beluga16 - beluga
		beluga17 - beluga
		beluga18 - beluga
		beluga19 - beluga
		beluga20 - beluga
		beluga21 - beluga
		beluga22 - beluga
		beluga23 - beluga
		beluga24 - beluga
		beluga25 - beluga
		beluga26 - beluga
		beluga27 - beluga
		beluga28 - beluga
		beluga29 - beluga
		beluga30 - beluga
		beluga31 - beluga
		beluga32 - beluga
		beluga33 - beluga
		beluga34 - beluga
		; Slots for outgoing flights:
		slot0 - slot
		slot1 - slot
		slot2 - slot
		slot3 - slot
		slot4 - slot
		; Production lines:
		pl0 - production-line
		pl1 - production-line
	)
  (:init
		; Number encoding
		; Sizes fitting rack: rack00
		(fit  n00  n04  n04 rack00)
		(fit  n01  n04  n05 rack00)
		(fit  n02  n04  n06 rack00)
		(fit  n03  n04  n07 rack00)
		(fit  n04  n04  n08 rack00)
		(fit  n00  n08  n08 rack00)
		(fit  n05  n04  n09 rack00)
		(fit  n01  n08  n09 rack00)
		(fit  n00  n09  n09 rack00)
		(fit  n06  n04  n10 rack00)
		(fit  n02  n08  n10 rack00)
		(fit  n01  n09  n10 rack00)
		(fit  n07  n04  n11 rack00)
		(fit  n03  n08  n11 rack00)
		(fit  n02  n09  n11 rack00)
		(fit  n00  n11  n11 rack00)
		(fit  n08  n04  n12 rack00)
		(fit  n04  n08  n12 rack00)
		(fit  n03  n09  n12 rack00)
		(fit  n01  n11  n12 rack00)
		(fit  n09  n04  n13 rack00)
		(fit  n05  n08  n13 rack00)
		(fit  n04  n09  n13 rack00)
		(fit  n02  n11  n13 rack00)
		(fit  n10  n04  n14 rack00)
		(fit  n06  n08  n14 rack00)
		(fit  n05  n09  n14 rack00)
		(fit  n03  n11  n14 rack00)
		(fit  n11  n04  n15 rack00)
		(fit  n07  n08  n15 rack00)
		(fit  n06  n09  n15 rack00)
		(fit  n04  n11  n15 rack00)
		(fit  n12  n04  n16 rack00)
		(fit  n08  n08  n16 rack00)
		(fit  n07  n09  n16 rack00)
		(fit  n05  n11  n16 rack00)
		(fit  n13  n04  n17 rack00)
		(fit  n09  n08  n17 rack00)
		(fit  n08  n09  n17 rack00)
		(fit  n06  n11  n17 rack00)
		(fit  n14  n04  n18 rack00)
		(fit  n10  n08  n18 rack00)
		(fit  n09  n09  n18 rack00)
		(fit  n07  n11  n18 rack00)
		(fit  n00  n18  n18 rack00)
		(fit  n15  n04  n19 rack00)
		(fit  n11  n08  n19 rack00)
		(fit  n10  n09  n19 rack00)
		(fit  n08  n11  n19 rack00)
		(fit  n01  n18  n19 rack00)
		(fit  n17  n04  n21 rack00)
		(fit  n13  n08  n21 rack00)
		(fit  n12  n09  n21 rack00)
		(fit  n10  n11  n21 rack00)
		(fit  n03  n18  n21 rack00)
		(fit  n18  n04  n22 rack00)
		(fit  n14  n08  n22 rack00)
		(fit  n13  n09  n22 rack00)
		(fit  n11  n11  n22 rack00)
		(fit  n04  n18  n22 rack00)
		(fit  n19  n04  n23 rack00)
		(fit  n15  n08  n23 rack00)
		(fit  n14  n09  n23 rack00)
		(fit  n12  n11  n23 rack00)
		(fit  n05  n18  n23 rack00)
		(fit  n21  n04  n25 rack00)
		(fit  n17  n08  n25 rack00)
		(fit  n16  n09  n25 rack00)
		(fit  n14  n11  n25 rack00)
		(fit  n07  n18  n25 rack00)
		(fit  n00  n25  n25 rack00)
		(fit  n22  n04  n26 rack00)
		(fit  n18  n08  n26 rack00)
		(fit  n17  n09  n26 rack00)
		(fit  n15  n11  n26 rack00)
		(fit  n08  n18  n26 rack00)
		(fit  n01  n25  n26 rack00)
		(fit  n26  n04  n30 rack00)
		(fit  n22  n08  n30 rack00)
		(fit  n21  n09  n30 rack00)
		(fit  n19  n11  n30 rack00)
		(fit  n12  n18  n30 rack00)
		(fit  n05  n25  n30 rack00)
		(fit  n02  n32  n34 rack00)
		(fit  n30  n04  n34 rack00)
		(fit  n26  n08  n34 rack00)
		(fit  n25  n09  n34 rack00)
		(fit  n23  n11  n34 rack00)
		(fit  n16  n18  n34 rack00)
		(fit  n09  n25  n34 rack00)
		; Sizes fitting rack: rack01
		(fit  n00  n04  n04 rack01)
		(fit  n01  n04  n05 rack01)
		(fit  n02  n04  n06 rack01)
		(fit  n03  n04  n07 rack01)
		(fit  n04  n04  n08 rack01)
		(fit  n00  n08  n08 rack01)
		(fit  n05  n04  n09 rack01)
		(fit  n01  n08  n09 rack01)
		(fit  n00  n09  n09 rack01)
		(fit  n06  n04  n10 rack01)
		(fit  n02  n08  n10 rack01)
		(fit  n01  n09  n10 rack01)
		(fit  n07  n04  n11 rack01)
		(fit  n03  n08  n11 rack01)
		(fit  n02  n09  n11 rack01)
		(fit  n00  n11  n11 rack01)
		(fit  n08  n04  n12 rack01)
		(fit  n04  n08  n12 rack01)
		(fit  n03  n09  n12 rack01)
		(fit  n01  n11  n12 rack01)
		(fit  n09  n04  n13 rack01)
		(fit  n05  n08  n13 rack01)
		(fit  n04  n09  n13 rack01)
		(fit  n02  n11  n13 rack01)
		(fit  n10  n04  n14 rack01)
		(fit  n06  n08  n14 rack01)
		(fit  n05  n09  n14 rack01)
		(fit  n03  n11  n14 rack01)
		(fit  n11  n04  n15 rack01)
		(fit  n07  n08  n15 rack01)
		(fit  n06  n09  n15 rack01)
		(fit  n04  n11  n15 rack01)
		(fit  n12  n04  n16 rack01)
		(fit  n08  n08  n16 rack01)
		(fit  n07  n09  n16 rack01)
		(fit  n05  n11  n16 rack01)
		(fit  n13  n04  n17 rack01)
		(fit  n09  n08  n17 rack01)
		(fit  n08  n09  n17 rack01)
		(fit  n06  n11  n17 rack01)
		(fit  n14  n04  n18 rack01)
		(fit  n10  n08  n18 rack01)
		(fit  n09  n09  n18 rack01)
		(fit  n07  n11  n18 rack01)
		(fit  n00  n18  n18 rack01)
		(fit  n15  n04  n19 rack01)
		(fit  n11  n08  n19 rack01)
		(fit  n10  n09  n19 rack01)
		(fit  n08  n11  n19 rack01)
		(fit  n01  n18  n19 rack01)
		(fit  n16  n04  n20 rack01)
		(fit  n12  n08  n20 rack01)
		(fit  n11  n09  n20 rack01)
		(fit  n09  n11  n20 rack01)
		(fit  n02  n18  n20 rack01)
		(fit  n18  n04  n22 rack01)
		(fit  n14  n08  n22 rack01)
		(fit  n13  n09  n22 rack01)
		(fit  n11  n11  n22 rack01)
		(fit  n04  n18  n22 rack01)
		(fit  n19  n04  n23 rack01)
		(fit  n15  n08  n23 rack01)
		(fit  n14  n09  n23 rack01)
		(fit  n12  n11  n23 rack01)
		(fit  n05  n18  n23 rack01)
		(fit  n20  n04  n24 rack01)
		(fit  n16  n08  n24 rack01)
		(fit  n15  n09  n24 rack01)
		(fit  n13  n11  n24 rack01)
		(fit  n06  n18  n24 rack01)
		(fit  n22  n04  n26 rack01)
		(fit  n18  n08  n26 rack01)
		(fit  n17  n09  n26 rack01)
		(fit  n15  n11  n26 rack01)
		(fit  n08  n18  n26 rack01)
		(fit  n01  n25  n26 rack01)
		(fit  n23  n04  n27 rack01)
		(fit  n19  n08  n27 rack01)
		(fit  n18  n09  n27 rack01)
		(fit  n16  n11  n27 rack01)
		(fit  n09  n18  n27 rack01)
		(fit  n02  n25  n27 rack01)
		(fit  n27  n04  n31 rack01)
		(fit  n23  n08  n31 rack01)
		(fit  n22  n09  n31 rack01)
		(fit  n20  n11  n31 rack01)
		(fit  n13  n18  n31 rack01)
		(fit  n06  n25  n31 rack01)
		(fit  n03  n32  n35 rack01)
		(fit  n31  n04  n35 rack01)
		(fit  n27  n08  n35 rack01)
		(fit  n26  n09  n35 rack01)
		(fit  n24  n11  n35 rack01)
		(fit  n17  n18  n35 rack01)
		(fit  n10  n25  n35 rack01)
		; Sizes fitting rack: rack02
		(fit  n00  n04  n04 rack02)
		(fit  n01  n04  n05 rack02)
		(fit  n02  n04  n06 rack02)
		(fit  n03  n04  n07 rack02)
		(fit  n04  n04  n08 rack02)
		(fit  n00  n08  n08 rack02)
		(fit  n05  n04  n09 rack02)
		(fit  n01  n08  n09 rack02)
		(fit  n00  n09  n09 rack02)
		(fit  n06  n04  n10 rack02)
		(fit  n02  n08  n10 rack02)
		(fit  n01  n09  n10 rack02)
		(fit  n07  n04  n11 rack02)
		(fit  n03  n08  n11 rack02)
		(fit  n02  n09  n11 rack02)
		(fit  n00  n11  n11 rack02)
		(fit  n08  n04  n12 rack02)
		(fit  n04  n08  n12 rack02)
		(fit  n03  n09  n12 rack02)
		(fit  n01  n11  n12 rack02)
		(fit  n09  n04  n13 rack02)
		(fit  n05  n08  n13 rack02)
		(fit  n04  n09  n13 rack02)
		(fit  n02  n11  n13 rack02)
		(fit  n10  n04  n14 rack02)
		(fit  n06  n08  n14 rack02)
		(fit  n05  n09  n14 rack02)
		(fit  n03  n11  n14 rack02)
		(fit  n11  n04  n15 rack02)
		(fit  n07  n08  n15 rack02)
		(fit  n06  n09  n15 rack02)
		(fit  n04  n11  n15 rack02)
		(fit  n12  n04  n16 rack02)
		(fit  n08  n08  n16 rack02)
		(fit  n07  n09  n16 rack02)
		(fit  n05  n11  n16 rack02)
		(fit  n13  n04  n17 rack02)
		(fit  n09  n08  n17 rack02)
		(fit  n08  n09  n17 rack02)
		(fit  n06  n11  n17 rack02)
		(fit  n14  n04  n18 rack02)
		(fit  n10  n08  n18 rack02)
		(fit  n09  n09  n18 rack02)
		(fit  n07  n11  n18 rack02)
		(fit  n00  n18  n18 rack02)
		(fit  n15  n04  n19 rack02)
		(fit  n11  n08  n19 rack02)
		(fit  n10  n09  n19 rack02)
		(fit  n08  n11  n19 rack02)
		(fit  n01  n18  n19 rack02)
		(fit  n16  n04  n20 rack02)
		(fit  n12  n08  n20 rack02)
		(fit  n11  n09  n20 rack02)
		(fit  n09  n11  n20 rack02)
		(fit  n02  n18  n20 rack02)
		(fit  n17  n04  n21 rack02)
		(fit  n13  n08  n21 rack02)
		(fit  n12  n09  n21 rack02)
		(fit  n10  n11  n21 rack02)
		(fit  n03  n18  n21 rack02)
		(fit  n19  n04  n23 rack02)
		(fit  n15  n08  n23 rack02)
		(fit  n14  n09  n23 rack02)
		(fit  n12  n11  n23 rack02)
		(fit  n05  n18  n23 rack02)
		(fit  n20  n04  n24 rack02)
		(fit  n16  n08  n24 rack02)
		(fit  n15  n09  n24 rack02)
		(fit  n13  n11  n24 rack02)
		(fit  n06  n18  n24 rack02)
		(fit  n21  n04  n25 rack02)
		(fit  n17  n08  n25 rack02)
		(fit  n16  n09  n25 rack02)
		(fit  n14  n11  n25 rack02)
		(fit  n07  n18  n25 rack02)
		(fit  n00  n25  n25 rack02)
		(fit  n23  n04  n27 rack02)
		(fit  n19  n08  n27 rack02)
		(fit  n18  n09  n27 rack02)
		(fit  n16  n11  n27 rack02)
		(fit  n09  n18  n27 rack02)
		(fit  n02  n25  n27 rack02)
		(fit  n24  n04  n28 rack02)
		(fit  n20  n08  n28 rack02)
		(fit  n19  n09  n28 rack02)
		(fit  n17  n11  n28 rack02)
		(fit  n10  n18  n28 rack02)
		(fit  n03  n25  n28 rack02)
		(fit  n00  n32  n32 rack02)
		(fit  n28  n04  n32 rack02)
		(fit  n24  n08  n32 rack02)
		(fit  n23  n09  n32 rack02)
		(fit  n21  n11  n32 rack02)
		(fit  n14  n18  n32 rack02)
		(fit  n07  n25  n32 rack02)
		(fit  n04  n32  n36 rack02)
		(fit  n32  n04  n36 rack02)
		(fit  n28  n08  n36 rack02)
		(fit  n27  n09  n36 rack02)
		(fit  n25  n11  n36 rack02)
		(fit  n18  n18  n36 rack02)
		(fit  n11  n25  n36 rack02)
		; Sizes fitting rack: rack03
		(fit  n00  n04  n04 rack03)
		(fit  n01  n04  n05 rack03)
		(fit  n02  n04  n06 rack03)
		(fit  n03  n04  n07 rack03)
		(fit  n05  n04  n09 rack03)
		(fit  n01  n08  n09 rack03)
		(fit  n00  n09  n09 rack03)
		(fit  n06  n04  n10 rack03)
		(fit  n02  n08  n10 rack03)
		(fit  n01  n09  n10 rack03)
		(fit  n07  n04  n11 rack03)
		(fit  n03  n08  n11 rack03)
		(fit  n02  n09  n11 rack03)
		(fit  n00  n11  n11 rack03)
		(fit  n09  n04  n13 rack03)
		(fit  n05  n08  n13 rack03)
		(fit  n04  n09  n13 rack03)
		(fit  n02  n11  n13 rack03)
		(fit  n10  n04  n14 rack03)
		(fit  n06  n08  n14 rack03)
		(fit  n05  n09  n14 rack03)
		(fit  n03  n11  n14 rack03)
		(fit  n14  n04  n18 rack03)
		(fit  n10  n08  n18 rack03)
		(fit  n09  n09  n18 rack03)
		(fit  n07  n11  n18 rack03)
		(fit  n00  n18  n18 rack03)
		(fit  n18  n04  n22 rack03)
		(fit  n14  n08  n22 rack03)
		(fit  n13  n09  n22 rack03)
		(fit  n11  n11  n22 rack03)
		(fit  n04  n18  n22 rack03)
		; Sizes fitting rack: rack04
		(fit  n00  n04  n04 rack04)
		(fit  n01  n04  n05 rack04)
		(fit  n02  n04  n06 rack04)
		(fit  n03  n04  n07 rack04)
		(fit  n04  n04  n08 rack04)
		(fit  n00  n08  n08 rack04)
		(fit  n05  n04  n09 rack04)
		(fit  n01  n08  n09 rack04)
		(fit  n00  n09  n09 rack04)
		(fit  n06  n04  n10 rack04)
		(fit  n02  n08  n10 rack04)
		(fit  n01  n09  n10 rack04)
		(fit  n07  n04  n11 rack04)
		(fit  n03  n08  n11 rack04)
		(fit  n02  n09  n11 rack04)
		(fit  n00  n11  n11 rack04)
		(fit  n09  n04  n13 rack04)
		(fit  n05  n08  n13 rack04)
		(fit  n04  n09  n13 rack04)
		(fit  n02  n11  n13 rack04)
		(fit  n10  n04  n14 rack04)
		(fit  n06  n08  n14 rack04)
		(fit  n05  n09  n14 rack04)
		(fit  n03  n11  n14 rack04)
		(fit  n11  n04  n15 rack04)
		(fit  n07  n08  n15 rack04)
		(fit  n06  n09  n15 rack04)
		(fit  n04  n11  n15 rack04)
		(fit  n13  n04  n17 rack04)
		(fit  n09  n08  n17 rack04)
		(fit  n08  n09  n17 rack04)
		(fit  n06  n11  n17 rack04)
		(fit  n14  n04  n18 rack04)
		(fit  n10  n08  n18 rack04)
		(fit  n09  n09  n18 rack04)
		(fit  n07  n11  n18 rack04)
		(fit  n00  n18  n18 rack04)
		(fit  n18  n04  n22 rack04)
		(fit  n14  n08  n22 rack04)
		(fit  n13  n09  n22 rack04)
		(fit  n11  n11  n22 rack04)
		(fit  n04  n18  n22 rack04)
		(fit  n22  n04  n26 rack04)
		(fit  n18  n08  n26 rack04)
		(fit  n17  n09  n26 rack04)
		(fit  n15  n11  n26 rack04)
		(fit  n08  n18  n26 rack04)
		(fit  n01  n25  n26 rack04)
		; Sizes fitting rack: rack05
		(fit  n00  n04  n04 rack05)
		(fit  n01  n04  n05 rack05)
		(fit  n02  n04  n06 rack05)
		(fit  n03  n04  n07 rack05)
		(fit  n04  n04  n08 rack05)
		(fit  n00  n08  n08 rack05)
		(fit  n05  n04  n09 rack05)
		(fit  n01  n08  n09 rack05)
		(fit  n00  n09  n09 rack05)
		(fit  n06  n04  n10 rack05)
		(fit  n02  n08  n10 rack05)
		(fit  n01  n09  n10 rack05)
		(fit  n07  n04  n11 rack05)
		(fit  n03  n08  n11 rack05)
		(fit  n02  n09  n11 rack05)
		(fit  n00  n11  n11 rack05)
		(fit  n09  n04  n13 rack05)
		(fit  n05  n08  n13 rack05)
		(fit  n04  n09  n13 rack05)
		(fit  n02  n11  n13 rack05)
		(fit  n10  n04  n14 rack05)
		(fit  n06  n08  n14 rack05)
		(fit  n05  n09  n14 rack05)
		(fit  n03  n11  n14 rack05)
		(fit  n11  n04  n15 rack05)
		(fit  n07  n08  n15 rack05)
		(fit  n06  n09  n15 rack05)
		(fit  n04  n11  n15 rack05)
		(fit  n13  n04  n17 rack05)
		(fit  n09  n08  n17 rack05)
		(fit  n08  n09  n17 rack05)
		(fit  n06  n11  n17 rack05)
		(fit  n14  n04  n18 rack05)
		(fit  n10  n08  n18 rack05)
		(fit  n09  n09  n18 rack05)
		(fit  n07  n11  n18 rack05)
		(fit  n00  n18  n18 rack05)
		(fit  n18  n04  n22 rack05)
		(fit  n14  n08  n22 rack05)
		(fit  n13  n09  n22 rack05)
		(fit  n11  n11  n22 rack05)
		(fit  n04  n18  n22 rack05)
		(fit  n22  n04  n26 rack05)
		(fit  n18  n08  n26 rack05)
		(fit  n17  n09  n26 rack05)
		(fit  n15  n11  n26 rack05)
		(fit  n08  n18  n26 rack05)
		(fit  n01  n25  n26 rack05)
		; trailers (Beluga side):
		(empty beluga_trailer_1)
		(at-side beluga_trailer_1 bside)
		; trailers (Factory side):
		(empty factory_trailer_1)
		(at-side factory_trailer_1 fside)
		(empty factory_trailer_2)
		(at-side factory_trailer_2 fside)
		(empty factory_trailer_3)
		(at-side factory_trailer_3 fside)
		; Racks 6
		; Rack:rack00
		(empty rack00)
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n34)
		; Rack:rack01
		(empty rack01)
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n35)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n07)
		(in jig0001 rack02)
		(clear jig0001 bside)
		(next-to jig0001 jig0002 bside)
		(next-to jig0002 jig0001 fside)
		(in jig0002 rack02)
		(clear jig0002 fside)
		; Rack:rack03
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n14)
		(in jig0003 rack03)
		(clear jig0003 bside)
		(clear jig0003 fside)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n08)
		(in jig0004 rack04)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack05
		(empty rack05)
		(at-side rack05 bside)
		(at-side rack05 fside)
		(free-space rack05 n26)
		; Jigs (size):
		(is_type jig0001 typeD)
		(size jig0001 n25)
		(empty-size jig0001 n18)
		(is_type jig0002 typeA)
		(size jig0002 n04)
		(empty-size jig0002 n04)
		(is_type jig0003 typeB)
		(size jig0003 n08)
		(empty-size jig0003 n08)
		(empty jig0003)
		(is_type jig0004 typeC)
		(size jig0004 n18)
		(empty-size jig0004 n09)
		(is_type jig0005 typeC)
		(size jig0005 n18)
		(empty-size jig0005 n09)
		(is_type jig0006 typeC)
		(size jig0006 n18)
		(empty-size jig0006 n09)
		(is_type jig0007 typeB)
		(size jig0007 n11)
		(empty-size jig0007 n08)
		(is_type jig0008 typeB)
		(size jig0008 n11)
		(empty-size jig0008 n08)
		(is_type jig0009 typeB)
		(size jig0009 n11)
		(empty-size jig0009 n08)
		(is_type jig0010 typeD)
		(size jig0010 n25)
		(empty-size jig0010 n18)
		(is_type jig0011 typeA)
		(size jig0011 n04)
		(empty-size jig0011 n04)
		(is_type jig0012 typeA)
		(size jig0012 n04)
		(empty-size jig0012 n04)
		(is_type jig0013 typeA)
		(size jig0013 n04)
		(empty-size jig0013 n04)
		(is_type jig0014 typeA)
		(size jig0014 n04)
		(empty-size jig0014 n04)
		(is_type jig0015 typeA)
		(size jig0015 n04)
		(empty-size jig0015 n04)
		(is_type jig0016 typeA)
		(size jig0016 n04)
		(empty-size jig0016 n04)
		(is_type jig0017 typeA)
		(size jig0017 n04)
		(empty-size jig0017 n04)
		(is_type jig0018 typeA)
		(size jig0018 n04)
		(empty-size jig0018 n04)
		(is_type jig0019 typeD)
		(size jig0019 n25)
		(empty-size jig0019 n18)
		(is_type jig0020 typeD)
		(size jig0020 n25)
		(empty-size jig0020 n18)
		(is_type jig0021 typeB)
		(size jig0021 n11)
		(empty-size jig0021 n08)
		(is_type jig0022 typeB)
		(size jig0022 n11)
		(empty-size jig0022 n08)
		(is_type jig0023 typeB)
		(size jig0023 n11)
		(empty-size jig0023 n08)
		(is_type jig0024 typeC)
		(size jig0024 n18)
		(empty-size jig0024 n09)
		(is_type jig0025 typeD)
		(size jig0025 n25)
		(empty-size jig0025 n18)
		(is_type jig0026 typeA)
		(size jig0026 n04)
		(empty-size jig0026 n04)
		(is_type jig0027 typeA)
		(size jig0027 n04)
		(empty-size jig0027 n04)
		(is_type jig0028 typeA)
		(size jig0028 n04)
		(empty-size jig0028 n04)
		(is_type jig0029 typeA)
		(size jig0029 n04)
		(empty-size jig0029 n04)
		(is_type jig0030 typeA)
		(size jig0030 n04)
		(empty-size jig0030 n04)
		(is_type jig0031 typeA)
		(size jig0031 n04)
		(empty-size jig0031 n04)
		(is_type jig0032 typeA)
		(size jig0032 n04)
		(empty-size jig0032 n04)
		(is_type jig0033 typeA)
		(size jig0033 n04)
		(empty-size jig0033 n04)
		(is_type jig0034 typeA)
		(size jig0034 n04)
		(empty-size jig0034 n04)
		(is_type jig0035 typeA)
		(size jig0035 n04)
		(empty-size jig0035 n04)
		(is_type jig0036 typeA)
		(size jig0036 n04)
		(empty-size jig0036 n04)
		(is_type jig0037 typeA)
		(size jig0037 n04)
		(empty-size jig0037 n04)
		(is_type jig0038 typeA)
		(size jig0038 n04)
		(empty-size jig0038 n04)
		(is_type jig0039 typeA)
		(size jig0039 n04)
		(empty-size jig0039 n04)
		(is_type jig0040 typeA)
		(size jig0040 n04)
		(empty-size jig0040 n04)
		(is_type jig0041 typeA)
		(size jig0041 n04)
		(empty-size jig0041 n04)
		(is_type jig0042 typeA)
		(size jig0042 n04)
		(empty-size jig0042 n04)
		(is_type jig0043 typeA)
		(size jig0043 n04)
		(empty-size jig0043 n04)
		(is_type jig0044 typeA)
		(size jig0044 n04)
		(empty-size jig0044 n04)
		(is_type jig0045 typeA)
		(size jig0045 n04)
		(empty-size jig0045 n04)
		(is_type jig0046 typeA)
		(size jig0046 n04)
		(empty-size jig0046 n04)
		(is_type jig0047 typeA)
		(size jig0047 n04)
		(empty-size jig0047 n04)
		(is_type jig0048 typeA)
		(size jig0048 n04)
		(empty-size jig0048 n04)
		(is_type jig0049 typeA)
		(size jig0049 n04)
		(empty-size jig0049 n04)
		(is_type jig0050 typeD)
		(size jig0050 n25)
		(empty-size jig0050 n18)
		(is_type jig0051 typeD)
		(size jig0051 n25)
		(empty-size jig0051 n18)
		(is_type jig0052 typeC)
		(size jig0052 n18)
		(empty-size jig0052 n09)
		(is_type jig0053 typeC)
		(size jig0053 n18)
		(empty-size jig0053 n09)
		(is_type jig0054 typeD)
		(size jig0054 n25)
		(empty-size jig0054 n18)
		(is_type jig0055 typeD)
		(size jig0055 n25)
		(empty-size jig0055 n18)
		; hangars:
		(empty hangar1)
		(empty hangar2)
		(empty hangar3)
		; Flight schedule initial phase:
		(processed-flight beluga1)
		; Flight order:
		(next-flight-to-process beluga1 beluga2)
		(next-flight-to-process beluga2 beluga3)
		(next-flight-to-process beluga3 beluga4)
		(next-flight-to-process beluga4 beluga5)
		(next-flight-to-process beluga5 beluga6)
		(next-flight-to-process beluga6 beluga7)
		(next-flight-to-process beluga7 beluga8)
		(next-flight-to-process beluga8 beluga9)
		(next-flight-to-process beluga9 beluga10)
		(next-flight-to-process beluga10 beluga11)
		(next-flight-to-process beluga11 beluga12)
		(next-flight-to-process beluga12 beluga13)
		(next-flight-to-process beluga13 beluga14)
		(next-flight-to-process beluga14 beluga15)
		(next-flight-to-process beluga15 beluga16)
		(next-flight-to-process beluga16 beluga17)
		(next-flight-to-process beluga17 beluga18)
		(next-flight-to-process beluga18 beluga19)
		(next-flight-to-process beluga19 beluga20)
		(next-flight-to-process beluga20 beluga21)
		(next-flight-to-process beluga21 beluga22)
		(next-flight-to-process beluga22 beluga23)
		(next-flight-to-process beluga23 beluga24)
		(next-flight-to-process beluga24 beluga25)
		(next-flight-to-process beluga25 beluga26)
		(next-flight-to-process beluga26 beluga27)
		(next-flight-to-process beluga27 beluga28)
		(next-flight-to-process beluga28 beluga29)
		(next-flight-to-process beluga29 beluga30)
		(next-flight-to-process beluga30 beluga31)
		(next-flight-to-process beluga31 beluga32)
		(next-flight-to-process beluga32 beluga33)
		(next-flight-to-process beluga33 beluga34)
		; Number of flights: 34
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0005 1: jig0006
		(to_unload jig0005 beluga1)
		(in jig0005 beluga1)
		(next_unload jig0005 jig0006)
		(in jig0006 beluga1)
		(next_unload jig0006 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0007 1: jig0008 2: jig0009
		(to_unload jig0007 beluga2)
		(in jig0007 beluga2)
		(next_unload jig0007 jig0008)
		(in jig0008 beluga2)
		(next_unload jig0008 jig0009)
		(in jig0009 beluga2)
		(next_unload jig0009 dummy-jig)
		; Flight: beluga3
		; 0: jig0010
		(to_unload jig0010 beluga3)
		(in jig0010 beluga3)
		(next_unload jig0010 dummy-jig)
		; Flight: beluga4
		; 0: jig0011 1: jig0012 2: jig0013 3: jig0014 4: jig0015 5: jig0016 6: jig0017 7: jig0018
		(to_unload jig0011 beluga4)
		(in jig0011 beluga4)
		(next_unload jig0011 jig0012)
		(in jig0012 beluga4)
		(next_unload jig0012 jig0013)
		(in jig0013 beluga4)
		(next_unload jig0013 jig0014)
		(in jig0014 beluga4)
		(next_unload jig0014 jig0015)
		(in jig0015 beluga4)
		(next_unload jig0015 jig0016)
		(in jig0016 beluga4)
		(next_unload jig0016 jig0017)
		(in jig0017 beluga4)
		(next_unload jig0017 jig0018)
		(in jig0018 beluga4)
		(next_unload jig0018 dummy-jig)
		; Flight: beluga5
		; No jigs
		(to_unload dummy-jig beluga5)
		; Flight: beluga6
		; 0: jig0019
		(to_unload jig0019 beluga6)
		(in jig0019 beluga6)
		(next_unload jig0019 dummy-jig)
		; Flight: beluga7
		; No jigs
		(to_unload dummy-jig beluga7)
		; Flight: beluga8
		; No jigs
		(to_unload dummy-jig beluga8)
		; Flight: beluga9
		; No jigs
		(to_unload dummy-jig beluga9)
		; Flight: beluga10
		; 0: jig0020
		(to_unload jig0020 beluga10)
		(in jig0020 beluga10)
		(next_unload jig0020 dummy-jig)
		; Flight: beluga11
		; No jigs
		(to_unload dummy-jig beluga11)
		; Flight: beluga12
		; 0: jig0021 1: jig0022 2: jig0023
		(to_unload jig0021 beluga12)
		(in jig0021 beluga12)
		(next_unload jig0021 jig0022)
		(in jig0022 beluga12)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga12)
		(next_unload jig0023 dummy-jig)
		; Flight: beluga13
		; No jigs
		(to_unload dummy-jig beluga13)
		; Flight: beluga14
		; 0: jig0024
		(to_unload jig0024 beluga14)
		(in jig0024 beluga14)
		(next_unload jig0024 dummy-jig)
		; Flight: beluga15
		; 0: jig0025
		(to_unload jig0025 beluga15)
		(in jig0025 beluga15)
		(next_unload jig0025 dummy-jig)
		; Flight: beluga16
		; No jigs
		(to_unload dummy-jig beluga16)
		; Flight: beluga17
		; No jigs
		(to_unload dummy-jig beluga17)
		; Flight: beluga18
		; 0: jig0026 1: jig0027 2: jig0028 3: jig0029 4: jig0030 5: jig0031 6: jig0032 7: jig0033 8: jig0034 9: jig0035
		(to_unload jig0026 beluga18)
		(in jig0026 beluga18)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga18)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga18)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga18)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga18)
		(next_unload jig0030 jig0031)
		(in jig0031 beluga18)
		(next_unload jig0031 jig0032)
		(in jig0032 beluga18)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga18)
		(next_unload jig0033 jig0034)
		(in jig0034 beluga18)
		(next_unload jig0034 jig0035)
		(in jig0035 beluga18)
		(next_unload jig0035 dummy-jig)
		; Flight: beluga19
		; No jigs
		(to_unload dummy-jig beluga19)
		; Flight: beluga20
		; 0: jig0036 1: jig0037 2: jig0038 3: jig0039 4: jig0040 5: jig0041 6: jig0042 7: jig0043 8: jig0044 9: jig0045
		(to_unload jig0036 beluga20)
		(in jig0036 beluga20)
		(next_unload jig0036 jig0037)
		(in jig0037 beluga20)
		(next_unload jig0037 jig0038)
		(in jig0038 beluga20)
		(next_unload jig0038 jig0039)
		(in jig0039 beluga20)
		(next_unload jig0039 jig0040)
		(in jig0040 beluga20)
		(next_unload jig0040 jig0041)
		(in jig0041 beluga20)
		(next_unload jig0041 jig0042)
		(in jig0042 beluga20)
		(next_unload jig0042 jig0043)
		(in jig0043 beluga20)
		(next_unload jig0043 jig0044)
		(in jig0044 beluga20)
		(next_unload jig0044 jig0045)
		(in jig0045 beluga20)
		(next_unload jig0045 dummy-jig)
		; Flight: beluga21
		; 0: jig0046 1: jig0047 2: jig0048 3: jig0049
		(to_unload jig0046 beluga21)
		(in jig0046 beluga21)
		(next_unload jig0046 jig0047)
		(in jig0047 beluga21)
		(next_unload jig0047 jig0048)
		(in jig0048 beluga21)
		(next_unload jig0048 jig0049)
		(in jig0049 beluga21)
		(next_unload jig0049 dummy-jig)
		; Flight: beluga22
		; No jigs
		(to_unload dummy-jig beluga22)
		; Flight: beluga23
		; No jigs
		(to_unload dummy-jig beluga23)
		; Flight: beluga24
		; No jigs
		(to_unload dummy-jig beluga24)
		; Flight: beluga25
		; No jigs
		(to_unload dummy-jig beluga25)
		; Flight: beluga26
		; 0: jig0050
		(to_unload jig0050 beluga26)
		(in jig0050 beluga26)
		(next_unload jig0050 dummy-jig)
		; Flight: beluga27
		; 0: jig0051
		(to_unload jig0051 beluga27)
		(in jig0051 beluga27)
		(next_unload jig0051 dummy-jig)
		; Flight: beluga28
		; 0: jig0052 1: jig0053
		(to_unload jig0052 beluga28)
		(in jig0052 beluga28)
		(next_unload jig0052 jig0053)
		(in jig0053 beluga28)
		(next_unload jig0053 dummy-jig)
		; Flight: beluga29
		; No jigs
		(to_unload dummy-jig beluga29)
		; Flight: beluga30
		; 0: jig0054
		(to_unload jig0054 beluga30)
		(in jig0054 beluga30)
		(next_unload jig0054 dummy-jig)
		; Flight: beluga31
		; No jigs
		(to_unload dummy-jig beluga31)
		; Flight: beluga32
		; No jigs
		(to_unload dummy-jig beluga32)
		; Flight: beluga33
		; No jigs
		(to_unload dummy-jig beluga33)
		; Flight: beluga34
		; 0: jig0055
		(to_unload jig0055 beluga34)
		(in jig0055 beluga34)
		(next_unload jig0055 dummy-jig)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeB)
		(to_load typeB slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; No jigs
		(to_load dummy-type dummy-slot beluga2)
		; No jigs
		(to_load dummy-type dummy-slot beluga3)
		; 0: typeC
		(to_load typeC slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; 0: typeB
		(to_load typeB slot0 beluga5)
		(next_load dummy-type slot0 dummy-slot beluga5)
		; 0: typeB
		(to_load typeB slot0 beluga6)
		(next_load dummy-type slot0 dummy-slot beluga6)
		; 0: typeA
		(to_load typeA slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; 0: typeA
		(to_load typeA slot0 beluga8)
		(next_load dummy-type slot0 dummy-slot beluga8)
		; 0: typeC
		(to_load typeC slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeA
		(to_load typeA slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeD
		(to_load typeD slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga12)
		(next_load typeA slot0 slot1 beluga12)
		(next_load dummy-type slot1 dummy-slot beluga12)
		; 0: typeC
		(to_load typeC slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeD
		(to_load typeD slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeD
		(to_load typeD slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeB
		(to_load typeB slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; 0: typeA
		(to_load typeA slot0 beluga17)
		(next_load dummy-type slot0 dummy-slot beluga17)
		; 0: typeA
		(to_load typeA slot0 beluga18)
		(next_load dummy-type slot0 dummy-slot beluga18)
		; 0: typeD
		(to_load typeD slot0 beluga19)
		(next_load dummy-type slot0 dummy-slot beluga19)
		; 0: typeB
		(to_load typeB slot0 beluga20)
		(next_load dummy-type slot0 dummy-slot beluga20)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga21)
		(next_load typeA slot0 slot1 beluga21)
		(next_load dummy-type slot1 dummy-slot beluga21)
		; 0: typeB
		(to_load typeB slot0 beluga22)
		(next_load dummy-type slot0 dummy-slot beluga22)
		; 0: typeB
		(to_load typeB slot0 beluga23)
		(next_load dummy-type slot0 dummy-slot beluga23)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga24)
		(next_load typeA slot0 slot1 beluga24)
		(next_load typeA slot1 slot2 beluga24)
		(next_load dummy-type slot2 dummy-slot beluga24)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga25)
		(next_load typeA slot0 slot1 beluga25)
		(next_load typeA slot1 slot2 beluga25)
		(next_load dummy-type slot2 dummy-slot beluga25)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga26)
		(next_load typeA slot0 slot1 beluga26)
		(next_load dummy-type slot1 dummy-slot beluga26)
		; 0: typeD
		(to_load typeD slot0 beluga27)
		(next_load dummy-type slot0 dummy-slot beluga27)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga28)
		(next_load typeA slot0 slot1 beluga28)
		(next_load typeA slot1 slot2 beluga28)
		(next_load typeA slot2 slot3 beluga28)
		(next_load typeA slot3 slot4 beluga28)
		(next_load dummy-type slot4 dummy-slot beluga28)
		; 0: typeC
		(to_load typeC slot0 beluga29)
		(next_load dummy-type slot0 dummy-slot beluga29)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga30)
		(next_load typeA slot0 slot1 beluga30)
		(next_load dummy-type slot1 dummy-slot beluga30)
		; 0: typeA
		(to_load typeA slot0 beluga31)
		(next_load dummy-type slot0 dummy-slot beluga31)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga32)
		(next_load typeA slot0 slot1 beluga32)
		(next_load dummy-type slot1 dummy-slot beluga32)
		; 0: typeC
		(to_load typeC slot0 beluga33)
		(next_load dummy-type slot0 dummy-slot beluga33)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga34)
		(next_load typeA slot0 slot1 beluga34)
		(next_load typeA slot1 slot2 beluga34)
		(next_load dummy-type slot2 dummy-slot beluga34)
		; Production schedule:
		; Production line: pl0
		; 0: jig0008 1: jig0016 2: jig0004 3: jig0013 4: jig0011 5: jig0009 6: jig0001 7: jig0015 8: jig0019 9: jig0017 10: jig0031 11: jig0040 12: jig0036 13: jig0046 14: jig0029 15: jig0026 16: jig0024 17: jig0041 18: jig0034 19: jig0035 20: jig0042 21: jig0044 22: jig0045 23: jig0049
		(to_deliver jig0008 pl0)
		(next_deliver jig0008 jig0016)
		(next_deliver jig0016 jig0004)
		(next_deliver jig0004 jig0013)
		(next_deliver jig0013 jig0011)
		(next_deliver jig0011 jig0009)
		(next_deliver jig0009 jig0001)
		(next_deliver jig0001 jig0015)
		(next_deliver jig0015 jig0019)
		(next_deliver jig0019 jig0017)
		(next_deliver jig0017 jig0031)
		(next_deliver jig0031 jig0040)
		(next_deliver jig0040 jig0036)
		(next_deliver jig0036 jig0046)
		(next_deliver jig0046 jig0029)
		(next_deliver jig0029 jig0026)
		(next_deliver jig0026 jig0024)
		(next_deliver jig0024 jig0041)
		(next_deliver jig0041 jig0034)
		(next_deliver jig0034 jig0035)
		(next_deliver jig0035 jig0042)
		(next_deliver jig0042 jig0044)
		(next_deliver jig0044 jig0045)
		(next_deliver jig0045 jig0049)
		(next_deliver jig0049 dummy-jig)
		; Production line: pl1
		; 0: jig0005 1: jig0007 2: jig0012 3: jig0010 4: jig0002 5: jig0006 6: jig0014 7: jig0020 8: jig0021 9: jig0018 10: jig0022 11: jig0023 12: jig0043 13: jig0038 14: jig0025 15: jig0032 16: jig0027 17: jig0037 18: jig0047 19: jig0048 20: jig0028 21: jig0030 22: jig0053 23: jig0033
		(to_deliver jig0005 pl1)
		(next_deliver jig0005 jig0007)
		(next_deliver jig0007 jig0012)
		(next_deliver jig0012 jig0010)
		(next_deliver jig0010 jig0002)
		(next_deliver jig0002 jig0006)
		(next_deliver jig0006 jig0014)
		(next_deliver jig0014 jig0020)
		(next_deliver jig0020 jig0021)
		(next_deliver jig0021 jig0018)
		(next_deliver jig0018 jig0022)
		(next_deliver jig0022 jig0023)
		(next_deliver jig0023 jig0043)
		(next_deliver jig0043 jig0038)
		(next_deliver jig0038 jig0025)
		(next_deliver jig0025 jig0032)
		(next_deliver jig0032 jig0027)
		(next_deliver jig0027 jig0037)
		(next_deliver jig0037 jig0047)
		(next_deliver jig0047 jig0048)
		(next_deliver jig0048 jig0028)
		(next_deliver jig0028 jig0030)
		(next_deliver jig0030 jig0053)
		(next_deliver jig0053 jig0033)
		(next_deliver jig0033 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0008)
		(empty jig0016)
		(empty jig0004)
		(empty jig0013)
		(empty jig0011)
		(empty jig0009)
		(empty jig0001)
		(empty jig0015)
		(empty jig0019)
		(empty jig0017)
		(empty jig0031)
		(empty jig0040)
		(empty jig0036)
		(empty jig0046)
		(empty jig0029)
		(empty jig0026)
		(empty jig0024)
		(empty jig0041)
		(empty jig0034)
		(empty jig0035)
		(empty jig0042)
		(empty jig0044)
		(empty jig0045)
		(empty jig0049)
		(empty jig0005)
		(empty jig0007)
		(empty jig0012)
		(empty jig0010)
		(empty jig0002)
		(empty jig0006)
		(empty jig0014)
		(empty jig0020)
		(empty jig0021)
		(empty jig0018)
		(empty jig0022)
		(empty jig0023)
		(empty jig0043)
		(empty jig0038)
		(empty jig0025)
		(empty jig0032)
		(empty jig0027)
		(empty jig0037)
		(empty jig0047)
		(empty jig0048)
		(empty jig0028)
		(empty jig0030)
		(empty jig0053)
		(empty jig0033)
		; all Belugas fully unloaded:
		(to_unload dummy-jig beluga1)
		(to_unload dummy-jig beluga2)
		(to_unload dummy-jig beluga3)
		(to_unload dummy-jig beluga4)
		(to_unload dummy-jig beluga5)
		(to_unload dummy-jig beluga6)
		(to_unload dummy-jig beluga7)
		(to_unload dummy-jig beluga8)
		(to_unload dummy-jig beluga9)
		(to_unload dummy-jig beluga10)
		(to_unload dummy-jig beluga11)
		(to_unload dummy-jig beluga12)
		(to_unload dummy-jig beluga13)
		(to_unload dummy-jig beluga14)
		(to_unload dummy-jig beluga15)
		(to_unload dummy-jig beluga16)
		(to_unload dummy-jig beluga17)
		(to_unload dummy-jig beluga18)
		(to_unload dummy-jig beluga19)
		(to_unload dummy-jig beluga20)
		(to_unload dummy-jig beluga21)
		(to_unload dummy-jig beluga22)
		(to_unload dummy-jig beluga23)
		(to_unload dummy-jig beluga24)
		(to_unload dummy-jig beluga25)
		(to_unload dummy-jig beluga26)
		(to_unload dummy-jig beluga27)
		(to_unload dummy-jig beluga28)
		(to_unload dummy-jig beluga29)
		(to_unload dummy-jig beluga30)
		(to_unload dummy-jig beluga31)
		(to_unload dummy-jig beluga32)
		(to_unload dummy-jig beluga33)
		(to_unload dummy-jig beluga34)
		; all Belugas fully loaded:
		(to_load dummy-type dummy-slot beluga1)
		(to_load dummy-type dummy-slot beluga2)
		(to_load dummy-type dummy-slot beluga3)
		(to_load dummy-type dummy-slot beluga4)
		(to_load dummy-type dummy-slot beluga5)
		(to_load dummy-type dummy-slot beluga6)
		(to_load dummy-type dummy-slot beluga7)
		(to_load dummy-type dummy-slot beluga8)
		(to_load dummy-type dummy-slot beluga9)
		(to_load dummy-type dummy-slot beluga10)
		(to_load dummy-type dummy-slot beluga11)
		(to_load dummy-type dummy-slot beluga12)
		(to_load dummy-type dummy-slot beluga13)
		(to_load dummy-type dummy-slot beluga14)
		(to_load dummy-type dummy-slot beluga15)
		(to_load dummy-type dummy-slot beluga16)
		(to_load dummy-type dummy-slot beluga17)
		(to_load dummy-type dummy-slot beluga18)
		(to_load dummy-type dummy-slot beluga19)
		(to_load dummy-type dummy-slot beluga20)
		(to_load dummy-type dummy-slot beluga21)
		(to_load dummy-type dummy-slot beluga22)
		(to_load dummy-type dummy-slot beluga23)
		(to_load dummy-type dummy-slot beluga24)
		(to_load dummy-type dummy-slot beluga25)
		(to_load dummy-type dummy-slot beluga26)
		(to_load dummy-type dummy-slot beluga27)
		(to_load dummy-type dummy-slot beluga28)
		(to_load dummy-type dummy-slot beluga29)
		(to_load dummy-type dummy-slot beluga30)
		(to_load dummy-type dummy-slot beluga31)
		(to_load dummy-type dummy-slot beluga32)
		(to_load dummy-type dummy-slot beluga33)
		(to_load dummy-type dummy-slot beluga34)
	))
  (:metric minimize (total-cost))
)