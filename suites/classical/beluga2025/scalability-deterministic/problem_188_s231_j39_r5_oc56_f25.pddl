(define
	(problem beluga-problem_188_s231_j39_r5_oc56_f25)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 38}
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
		n29 - num
		n30 - num
		n31 - num
		n32 - num
		n33 - num
		n34 - num
		n38 - num
		; trailers:
		beluga_trailer_1 - trailer
		beluga_trailer_2 - trailer
		factory_trailer_1 - trailer
		factory_trailer_2 - trailer
		factory_trailer_3 - trailer
		; Racks:
		rack00 - rack
		rack01 - rack
		rack02 - rack
		rack03 - rack
		rack04 - rack
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
		typeE - type
		typeD - type
		typeC - type
		typeB - type
		typeA - type
		; hangars:
		hangar1 - hangar
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
		; Slots for outgoing flights:
		slot0 - slot
		slot1 - slot
		slot2 - slot
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
		(fit  n16  n04  n20 rack00)
		(fit  n12  n08  n20 rack00)
		(fit  n11  n09  n20 rack00)
		(fit  n09  n11  n20 rack00)
		(fit  n02  n18  n20 rack00)
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
		(fit  n23  n04  n27 rack00)
		(fit  n19  n08  n27 rack00)
		(fit  n18  n09  n27 rack00)
		(fit  n16  n11  n27 rack00)
		(fit  n09  n18  n27 rack00)
		(fit  n02  n25  n27 rack00)
		(fit  n27  n04  n31 rack00)
		(fit  n23  n08  n31 rack00)
		(fit  n22  n09  n31 rack00)
		(fit  n20  n11  n31 rack00)
		(fit  n13  n18  n31 rack00)
		(fit  n06  n25  n31 rack00)
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
		(fit  n16  n04  n20 rack01)
		(fit  n12  n08  n20 rack01)
		(fit  n11  n09  n20 rack01)
		(fit  n09  n11  n20 rack01)
		(fit  n02  n18  n20 rack01)
		(fit  n17  n04  n21 rack01)
		(fit  n13  n08  n21 rack01)
		(fit  n12  n09  n21 rack01)
		(fit  n10  n11  n21 rack01)
		(fit  n03  n18  n21 rack01)
		(fit  n21  n04  n25 rack01)
		(fit  n17  n08  n25 rack01)
		(fit  n16  n09  n25 rack01)
		(fit  n14  n11  n25 rack01)
		(fit  n07  n18  n25 rack01)
		(fit  n00  n25  n25 rack01)
		(fit  n25  n04  n29 rack01)
		(fit  n21  n08  n29 rack01)
		(fit  n20  n09  n29 rack01)
		(fit  n18  n11  n29 rack01)
		(fit  n11  n18  n29 rack01)
		(fit  n04  n25  n29 rack01)
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
		(fit  n18  n04  n22 rack02)
		(fit  n14  n08  n22 rack02)
		(fit  n13  n09  n22 rack02)
		(fit  n11  n11  n22 rack02)
		(fit  n04  n18  n22 rack02)
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
		(fit  n25  n04  n29 rack02)
		(fit  n21  n08  n29 rack02)
		(fit  n20  n09  n29 rack02)
		(fit  n18  n11  n29 rack02)
		(fit  n11  n18  n29 rack02)
		(fit  n04  n25  n29 rack02)
		(fit  n01  n32  n33 rack02)
		(fit  n29  n04  n33 rack02)
		(fit  n25  n08  n33 rack02)
		(fit  n24  n09  n33 rack02)
		(fit  n22  n11  n33 rack02)
		(fit  n15  n18  n33 rack02)
		(fit  n08  n25  n33 rack02)
		; Sizes fitting rack: rack03
		(fit  n00  n04  n04 rack03)
		(fit  n01  n04  n05 rack03)
		(fit  n02  n04  n06 rack03)
		(fit  n03  n04  n07 rack03)
		(fit  n04  n04  n08 rack03)
		(fit  n00  n08  n08 rack03)
		(fit  n06  n04  n10 rack03)
		(fit  n02  n08  n10 rack03)
		(fit  n01  n09  n10 rack03)
		(fit  n07  n04  n11 rack03)
		(fit  n03  n08  n11 rack03)
		(fit  n02  n09  n11 rack03)
		(fit  n00  n11  n11 rack03)
		(fit  n08  n04  n12 rack03)
		(fit  n04  n08  n12 rack03)
		(fit  n03  n09  n12 rack03)
		(fit  n01  n11  n12 rack03)
		(fit  n10  n04  n14 rack03)
		(fit  n06  n08  n14 rack03)
		(fit  n05  n09  n14 rack03)
		(fit  n03  n11  n14 rack03)
		(fit  n11  n04  n15 rack03)
		(fit  n07  n08  n15 rack03)
		(fit  n06  n09  n15 rack03)
		(fit  n04  n11  n15 rack03)
		(fit  n15  n04  n19 rack03)
		(fit  n11  n08  n19 rack03)
		(fit  n10  n09  n19 rack03)
		(fit  n08  n11  n19 rack03)
		(fit  n01  n18  n19 rack03)
		(fit  n19  n04  n23 rack03)
		(fit  n15  n08  n23 rack03)
		(fit  n14  n09  n23 rack03)
		(fit  n12  n11  n23 rack03)
		(fit  n05  n18  n23 rack03)
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
		(fit  n08  n04  n12 rack04)
		(fit  n04  n08  n12 rack04)
		(fit  n03  n09  n12 rack04)
		(fit  n01  n11  n12 rack04)
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
		(fit  n12  n04  n16 rack04)
		(fit  n08  n08  n16 rack04)
		(fit  n07  n09  n16 rack04)
		(fit  n05  n11  n16 rack04)
		(fit  n13  n04  n17 rack04)
		(fit  n09  n08  n17 rack04)
		(fit  n08  n09  n17 rack04)
		(fit  n06  n11  n17 rack04)
		(fit  n14  n04  n18 rack04)
		(fit  n10  n08  n18 rack04)
		(fit  n09  n09  n18 rack04)
		(fit  n07  n11  n18 rack04)
		(fit  n00  n18  n18 rack04)
		(fit  n15  n04  n19 rack04)
		(fit  n11  n08  n19 rack04)
		(fit  n10  n09  n19 rack04)
		(fit  n08  n11  n19 rack04)
		(fit  n01  n18  n19 rack04)
		(fit  n16  n04  n20 rack04)
		(fit  n12  n08  n20 rack04)
		(fit  n11  n09  n20 rack04)
		(fit  n09  n11  n20 rack04)
		(fit  n02  n18  n20 rack04)
		(fit  n17  n04  n21 rack04)
		(fit  n13  n08  n21 rack04)
		(fit  n12  n09  n21 rack04)
		(fit  n10  n11  n21 rack04)
		(fit  n03  n18  n21 rack04)
		(fit  n18  n04  n22 rack04)
		(fit  n14  n08  n22 rack04)
		(fit  n13  n09  n22 rack04)
		(fit  n11  n11  n22 rack04)
		(fit  n04  n18  n22 rack04)
		(fit  n19  n04  n23 rack04)
		(fit  n15  n08  n23 rack04)
		(fit  n14  n09  n23 rack04)
		(fit  n12  n11  n23 rack04)
		(fit  n05  n18  n23 rack04)
		(fit  n21  n04  n25 rack04)
		(fit  n17  n08  n25 rack04)
		(fit  n16  n09  n25 rack04)
		(fit  n14  n11  n25 rack04)
		(fit  n07  n18  n25 rack04)
		(fit  n00  n25  n25 rack04)
		(fit  n22  n04  n26 rack04)
		(fit  n18  n08  n26 rack04)
		(fit  n17  n09  n26 rack04)
		(fit  n15  n11  n26 rack04)
		(fit  n08  n18  n26 rack04)
		(fit  n01  n25  n26 rack04)
		(fit  n23  n04  n27 rack04)
		(fit  n19  n08  n27 rack04)
		(fit  n18  n09  n27 rack04)
		(fit  n16  n11  n27 rack04)
		(fit  n09  n18  n27 rack04)
		(fit  n02  n25  n27 rack04)
		(fit  n25  n04  n29 rack04)
		(fit  n21  n08  n29 rack04)
		(fit  n20  n09  n29 rack04)
		(fit  n18  n11  n29 rack04)
		(fit  n11  n18  n29 rack04)
		(fit  n04  n25  n29 rack04)
		(fit  n26  n04  n30 rack04)
		(fit  n22  n08  n30 rack04)
		(fit  n21  n09  n30 rack04)
		(fit  n19  n11  n30 rack04)
		(fit  n12  n18  n30 rack04)
		(fit  n05  n25  n30 rack04)
		(fit  n02  n32  n34 rack04)
		(fit  n30  n04  n34 rack04)
		(fit  n26  n08  n34 rack04)
		(fit  n25  n09  n34 rack04)
		(fit  n23  n11  n34 rack04)
		(fit  n16  n18  n34 rack04)
		(fit  n09  n25  n34 rack04)
		(fit  n06  n32  n38 rack04)
		(fit  n34  n04  n38 rack04)
		(fit  n30  n08  n38 rack04)
		(fit  n29  n09  n38 rack04)
		(fit  n27  n11  n38 rack04)
		(fit  n20  n18  n38 rack04)
		(fit  n13  n25  n38 rack04)
		; trailers (Beluga side):
		(empty beluga_trailer_1)
		(at-side beluga_trailer_1 bside)
		(empty beluga_trailer_2)
		(at-side beluga_trailer_2 bside)
		; trailers (Factory side):
		(empty factory_trailer_1)
		(at-side factory_trailer_1 fside)
		(empty factory_trailer_2)
		(at-side factory_trailer_2 fside)
		(empty factory_trailer_3)
		(at-side factory_trailer_3 fside)
		; Racks 5
		; Rack:rack00
		(empty rack00)
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n31)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n04)
		(in jig0002 rack01)
		(clear jig0002 bside)
		(clear jig0002 fside)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n00)
		(in jig0001 rack02)
		(clear jig0001 bside)
		(next-to jig0001 jig0003 bside)
		(next-to jig0003 jig0001 fside)
		(in jig0003 rack02)
		(clear jig0003 fside)
		; Rack:rack03
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n12)
		(in jig0004 rack03)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n20)
		(in jig0005 rack04)
		(clear jig0005 bside)
		(clear jig0005 fside)
		; Jigs (size):
		(is_type jig0001 typeB)
		(size jig0001 n08)
		(empty-size jig0001 n08)
		(empty jig0001)
		(is_type jig0002 typeD)
		(size jig0002 n25)
		(empty-size jig0002 n18)
		(is_type jig0003 typeD)
		(size jig0003 n25)
		(empty-size jig0003 n18)
		(is_type jig0004 typeB)
		(size jig0004 n11)
		(empty-size jig0004 n08)
		(is_type jig0005 typeC)
		(size jig0005 n18)
		(empty-size jig0005 n09)
		(is_type jig0006 typeC)
		(size jig0006 n18)
		(empty-size jig0006 n09)
		(is_type jig0007 typeC)
		(size jig0007 n18)
		(empty-size jig0007 n09)
		(is_type jig0008 typeB)
		(size jig0008 n11)
		(empty-size jig0008 n08)
		(is_type jig0009 typeB)
		(size jig0009 n11)
		(empty-size jig0009 n08)
		(is_type jig0010 typeB)
		(size jig0010 n11)
		(empty-size jig0010 n08)
		(is_type jig0011 typeE)
		(size jig0011 n32)
		(empty-size jig0011 n32)
		(is_type jig0012 typeB)
		(size jig0012 n11)
		(empty-size jig0012 n08)
		(is_type jig0013 typeB)
		(size jig0013 n11)
		(empty-size jig0013 n08)
		(is_type jig0014 typeB)
		(size jig0014 n11)
		(empty-size jig0014 n08)
		(is_type jig0015 typeD)
		(size jig0015 n25)
		(empty-size jig0015 n18)
		(is_type jig0016 typeE)
		(size jig0016 n32)
		(empty-size jig0016 n32)
		(is_type jig0017 typeB)
		(size jig0017 n11)
		(empty-size jig0017 n08)
		(is_type jig0018 typeB)
		(size jig0018 n11)
		(empty-size jig0018 n08)
		(is_type jig0019 typeB)
		(size jig0019 n11)
		(empty-size jig0019 n08)
		(is_type jig0020 typeE)
		(size jig0020 n32)
		(empty-size jig0020 n32)
		(is_type jig0021 typeB)
		(size jig0021 n11)
		(empty-size jig0021 n08)
		(is_type jig0022 typeA)
		(size jig0022 n04)
		(empty-size jig0022 n04)
		(is_type jig0023 typeA)
		(size jig0023 n04)
		(empty-size jig0023 n04)
		(is_type jig0024 typeA)
		(size jig0024 n04)
		(empty-size jig0024 n04)
		(is_type jig0025 typeA)
		(size jig0025 n04)
		(empty-size jig0025 n04)
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
		(is_type jig0032 typeC)
		(size jig0032 n18)
		(empty-size jig0032 n09)
		(is_type jig0033 typeC)
		(size jig0033 n18)
		(empty-size jig0033 n09)
		(is_type jig0034 typeD)
		(size jig0034 n25)
		(empty-size jig0034 n18)
		(is_type jig0035 typeB)
		(size jig0035 n11)
		(empty-size jig0035 n08)
		(is_type jig0036 typeB)
		(size jig0036 n11)
		(empty-size jig0036 n08)
		(is_type jig0037 typeC)
		(size jig0037 n18)
		(empty-size jig0037 n09)
		(is_type jig0038 typeE)
		(size jig0038 n32)
		(empty-size jig0038 n32)
		(is_type jig0039 typeE)
		(size jig0039 n32)
		(empty-size jig0039 n32)
		; hangars:
		(empty hangar1)
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
		; Number of flights: 25
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0006 1: jig0007
		(to_unload jig0006 beluga1)
		(in jig0006 beluga1)
		(next_unload jig0006 jig0007)
		(in jig0007 beluga1)
		(next_unload jig0007 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; No jigs
		(to_unload dummy-jig beluga2)
		; Flight: beluga3
		; 0: jig0008 1: jig0009 2: jig0010
		(to_unload jig0008 beluga3)
		(in jig0008 beluga3)
		(next_unload jig0008 jig0009)
		(in jig0009 beluga3)
		(next_unload jig0009 jig0010)
		(in jig0010 beluga3)
		(next_unload jig0010 dummy-jig)
		; Flight: beluga4
		; 0: jig0011
		(to_unload jig0011 beluga4)
		(in jig0011 beluga4)
		(next_unload jig0011 dummy-jig)
		; Flight: beluga5
		; 0: jig0012 1: jig0013 2: jig0014
		(to_unload jig0012 beluga5)
		(in jig0012 beluga5)
		(next_unload jig0012 jig0013)
		(in jig0013 beluga5)
		(next_unload jig0013 jig0014)
		(in jig0014 beluga5)
		(next_unload jig0014 dummy-jig)
		; Flight: beluga6
		; 0: jig0015
		(to_unload jig0015 beluga6)
		(in jig0015 beluga6)
		(next_unload jig0015 dummy-jig)
		; Flight: beluga7
		; No jigs
		(to_unload dummy-jig beluga7)
		; Flight: beluga8
		; No jigs
		(to_unload dummy-jig beluga8)
		; Flight: beluga9
		; 0: jig0016
		(to_unload jig0016 beluga9)
		(in jig0016 beluga9)
		(next_unload jig0016 dummy-jig)
		; Flight: beluga10
		; 0: jig0017 1: jig0018 2: jig0019
		(to_unload jig0017 beluga10)
		(in jig0017 beluga10)
		(next_unload jig0017 jig0018)
		(in jig0018 beluga10)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga10)
		(next_unload jig0019 dummy-jig)
		; Flight: beluga11
		; 0: jig0020
		(to_unload jig0020 beluga11)
		(in jig0020 beluga11)
		(next_unload jig0020 dummy-jig)
		; Flight: beluga12
		; 0: jig0021
		(to_unload jig0021 beluga12)
		(in jig0021 beluga12)
		(next_unload jig0021 dummy-jig)
		; Flight: beluga13
		; No jigs
		(to_unload dummy-jig beluga13)
		; Flight: beluga14
		; No jigs
		(to_unload dummy-jig beluga14)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0022 1: jig0023 2: jig0024 3: jig0025 4: jig0026 5: jig0027 6: jig0028 7: jig0029 8: jig0030 9: jig0031
		(to_unload jig0022 beluga16)
		(in jig0022 beluga16)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga16)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga16)
		(next_unload jig0024 jig0025)
		(in jig0025 beluga16)
		(next_unload jig0025 jig0026)
		(in jig0026 beluga16)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga16)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga16)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga16)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga16)
		(next_unload jig0030 jig0031)
		(in jig0031 beluga16)
		(next_unload jig0031 dummy-jig)
		; Flight: beluga17
		; 0: jig0032 1: jig0033
		(to_unload jig0032 beluga17)
		(in jig0032 beluga17)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga17)
		(next_unload jig0033 dummy-jig)
		; Flight: beluga18
		; 0: jig0034
		(to_unload jig0034 beluga18)
		(in jig0034 beluga18)
		(next_unload jig0034 dummy-jig)
		; Flight: beluga19
		; 0: jig0035 1: jig0036
		(to_unload jig0035 beluga19)
		(in jig0035 beluga19)
		(next_unload jig0035 jig0036)
		(in jig0036 beluga19)
		(next_unload jig0036 dummy-jig)
		; Flight: beluga20
		; No jigs
		(to_unload dummy-jig beluga20)
		; Flight: beluga21
		; No jigs
		(to_unload dummy-jig beluga21)
		; Flight: beluga22
		; 0: jig0037
		(to_unload jig0037 beluga22)
		(in jig0037 beluga22)
		(next_unload jig0037 dummy-jig)
		; Flight: beluga23
		; 0: jig0038
		(to_unload jig0038 beluga23)
		(in jig0038 beluga23)
		(next_unload jig0038 dummy-jig)
		; Flight: beluga24
		; No jigs
		(to_unload dummy-jig beluga24)
		; Flight: beluga25
		; 0: jig0039
		(to_unload jig0039 beluga25)
		(in jig0039 beluga25)
		(next_unload jig0039 dummy-jig)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeB)
		(to_load typeB slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga2)
		(next_load typeC slot0 slot1 beluga2)
		(next_load dummy-type slot1 dummy-slot beluga2)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga3)
		(next_load typeD slot0 slot1 beluga3)
		(next_load dummy-type slot1 dummy-slot beluga3)
		; 0: typeC
		(to_load typeC slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; No jigs
		(to_load dummy-type dummy-slot beluga5)
		; No jigs
		(to_load dummy-type dummy-slot beluga6)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga7)
		(next_load typeB slot0 slot1 beluga7)
		(next_load dummy-type slot1 dummy-slot beluga7)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga8)
		(next_load typeB slot0 slot1 beluga8)
		(next_load typeB slot1 slot2 beluga8)
		(next_load dummy-type slot2 dummy-slot beluga8)
		; 0: typeE
		(to_load typeE slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeB
		(to_load typeB slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeB
		(to_load typeB slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeD
		(to_load typeD slot0 beluga12)
		(next_load dummy-type slot0 dummy-slot beluga12)
		; 0: typeB
		(to_load typeB slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeB
		(to_load typeB slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeE
		(to_load typeE slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeE
		(to_load typeE slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; No jigs
		(to_load dummy-type dummy-slot beluga17)
		; No jigs
		(to_load dummy-type dummy-slot beluga18)
		; No jigs
		(to_load dummy-type dummy-slot beluga19)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga20)
		(next_load typeA slot0 slot1 beluga20)
		(next_load dummy-type slot1 dummy-slot beluga20)
		; 0: typeD
		(to_load typeD slot0 beluga21)
		(next_load dummy-type slot0 dummy-slot beluga21)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga22)
		(next_load typeB slot0 slot1 beluga22)
		(next_load typeB slot1 slot2 beluga22)
		(next_load dummy-type slot2 dummy-slot beluga22)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga23)
		(next_load typeA slot0 slot1 beluga23)
		(next_load typeA slot1 slot2 beluga23)
		(next_load dummy-type slot2 dummy-slot beluga23)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga24)
		(next_load typeC slot0 slot1 beluga24)
		(next_load dummy-type slot1 dummy-slot beluga24)
		; 0: typeB
		(to_load typeB slot0 beluga25)
		(next_load dummy-type slot0 dummy-slot beluga25)
		; Production schedule:
		; Production line: pl0
		; 0: jig0006 1: jig0003 2: jig0004 3: jig0011 4: jig0013 5: jig0009 6: jig0015 7: jig0016 8: jig0020 9: jig0021 10: jig0030 11: jig0027 12: jig0034 13: jig0023 14: jig0022 15: jig0025 16: jig0031
		(to_deliver jig0006 pl0)
		(next_deliver jig0006 jig0003)
		(next_deliver jig0003 jig0004)
		(next_deliver jig0004 jig0011)
		(next_deliver jig0011 jig0013)
		(next_deliver jig0013 jig0009)
		(next_deliver jig0009 jig0015)
		(next_deliver jig0015 jig0016)
		(next_deliver jig0016 jig0020)
		(next_deliver jig0020 jig0021)
		(next_deliver jig0021 jig0030)
		(next_deliver jig0030 jig0027)
		(next_deliver jig0027 jig0034)
		(next_deliver jig0034 jig0023)
		(next_deliver jig0023 jig0022)
		(next_deliver jig0022 jig0025)
		(next_deliver jig0025 jig0031)
		(next_deliver jig0031 dummy-jig)
		; Production line: pl1
		; 0: jig0005 1: jig0002 2: jig0007 3: jig0008 4: jig0012 5: jig0014 6: jig0010 7: jig0018 8: jig0017 9: jig0019 10: jig0024 11: jig0026 12: jig0033 13: jig0036 14: jig0032 15: jig0028 16: jig0035
		(to_deliver jig0005 pl1)
		(next_deliver jig0005 jig0002)
		(next_deliver jig0002 jig0007)
		(next_deliver jig0007 jig0008)
		(next_deliver jig0008 jig0012)
		(next_deliver jig0012 jig0014)
		(next_deliver jig0014 jig0010)
		(next_deliver jig0010 jig0018)
		(next_deliver jig0018 jig0017)
		(next_deliver jig0017 jig0019)
		(next_deliver jig0019 jig0024)
		(next_deliver jig0024 jig0026)
		(next_deliver jig0026 jig0033)
		(next_deliver jig0033 jig0036)
		(next_deliver jig0036 jig0032)
		(next_deliver jig0032 jig0028)
		(next_deliver jig0028 jig0035)
		(next_deliver jig0035 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0006)
		(empty jig0003)
		(empty jig0004)
		(empty jig0011)
		(empty jig0013)
		(empty jig0009)
		(empty jig0015)
		(empty jig0016)
		(empty jig0020)
		(empty jig0021)
		(empty jig0030)
		(empty jig0027)
		(empty jig0034)
		(empty jig0023)
		(empty jig0022)
		(empty jig0025)
		(empty jig0031)
		(empty jig0005)
		(empty jig0002)
		(empty jig0007)
		(empty jig0008)
		(empty jig0012)
		(empty jig0014)
		(empty jig0010)
		(empty jig0018)
		(empty jig0017)
		(empty jig0019)
		(empty jig0024)
		(empty jig0026)
		(empty jig0033)
		(empty jig0036)
		(empty jig0032)
		(empty jig0028)
		(empty jig0035)
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
	))
  (:metric minimize (total-cost))
)