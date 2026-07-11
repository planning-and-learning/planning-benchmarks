(define
	(problem beluga-problem_74_s116_j43_r5_oc85_f28)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32}
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
		typeA - type
		typeB - type
		typeC - type
		typeD - type
		typeE - type
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
		; Slots for outgoing flights:
		slot0 - slot
		slot1 - slot
		slot2 - slot
		slot3 - slot
		; Production lines:
		pl0 - production-line
		pl1 - production-line
		pl2 - production-line
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
		(fit  n17  n04  n21 rack01)
		(fit  n13  n08  n21 rack01)
		(fit  n12  n09  n21 rack01)
		(fit  n10  n11  n21 rack01)
		(fit  n03  n18  n21 rack01)
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
		(fit  n24  n04  n28 rack01)
		(fit  n20  n08  n28 rack01)
		(fit  n19  n09  n28 rack01)
		(fit  n17  n11  n28 rack01)
		(fit  n10  n18  n28 rack01)
		(fit  n03  n25  n28 rack01)
		(fit  n00  n32  n32 rack01)
		(fit  n28  n04  n32 rack01)
		(fit  n24  n08  n32 rack01)
		(fit  n23  n09  n32 rack01)
		(fit  n21  n11  n32 rack01)
		(fit  n14  n18  n32 rack01)
		(fit  n07  n25  n32 rack01)
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
		(fit  n13  n04  n17 rack02)
		(fit  n09  n08  n17 rack02)
		(fit  n08  n09  n17 rack02)
		(fit  n06  n11  n17 rack02)
		(fit  n14  n04  n18 rack02)
		(fit  n10  n08  n18 rack02)
		(fit  n09  n09  n18 rack02)
		(fit  n07  n11  n18 rack02)
		(fit  n00  n18  n18 rack02)
		(fit  n18  n04  n22 rack02)
		(fit  n14  n08  n22 rack02)
		(fit  n13  n09  n22 rack02)
		(fit  n11  n11  n22 rack02)
		(fit  n04  n18  n22 rack02)
		(fit  n22  n04  n26 rack02)
		(fit  n18  n08  n26 rack02)
		(fit  n17  n09  n26 rack02)
		(fit  n15  n11  n26 rack02)
		(fit  n08  n18  n26 rack02)
		(fit  n01  n25  n26 rack02)
		; Sizes fitting rack: rack03
		(fit  n00  n04  n04 rack03)
		(fit  n01  n04  n05 rack03)
		(fit  n02  n04  n06 rack03)
		(fit  n03  n04  n07 rack03)
		(fit  n04  n04  n08 rack03)
		(fit  n00  n08  n08 rack03)
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
		(fit  n08  n04  n12 rack03)
		(fit  n04  n08  n12 rack03)
		(fit  n03  n09  n12 rack03)
		(fit  n01  n11  n12 rack03)
		(fit  n09  n04  n13 rack03)
		(fit  n05  n08  n13 rack03)
		(fit  n04  n09  n13 rack03)
		(fit  n02  n11  n13 rack03)
		(fit  n10  n04  n14 rack03)
		(fit  n06  n08  n14 rack03)
		(fit  n05  n09  n14 rack03)
		(fit  n03  n11  n14 rack03)
		(fit  n11  n04  n15 rack03)
		(fit  n07  n08  n15 rack03)
		(fit  n06  n09  n15 rack03)
		(fit  n04  n11  n15 rack03)
		(fit  n12  n04  n16 rack03)
		(fit  n08  n08  n16 rack03)
		(fit  n07  n09  n16 rack03)
		(fit  n05  n11  n16 rack03)
		(fit  n14  n04  n18 rack03)
		(fit  n10  n08  n18 rack03)
		(fit  n09  n09  n18 rack03)
		(fit  n07  n11  n18 rack03)
		(fit  n00  n18  n18 rack03)
		(fit  n15  n04  n19 rack03)
		(fit  n11  n08  n19 rack03)
		(fit  n10  n09  n19 rack03)
		(fit  n08  n11  n19 rack03)
		(fit  n01  n18  n19 rack03)
		(fit  n16  n04  n20 rack03)
		(fit  n12  n08  n20 rack03)
		(fit  n11  n09  n20 rack03)
		(fit  n09  n11  n20 rack03)
		(fit  n02  n18  n20 rack03)
		(fit  n18  n04  n22 rack03)
		(fit  n14  n08  n22 rack03)
		(fit  n13  n09  n22 rack03)
		(fit  n11  n11  n22 rack03)
		(fit  n04  n18  n22 rack03)
		(fit  n19  n04  n23 rack03)
		(fit  n15  n08  n23 rack03)
		(fit  n14  n09  n23 rack03)
		(fit  n12  n11  n23 rack03)
		(fit  n05  n18  n23 rack03)
		(fit  n23  n04  n27 rack03)
		(fit  n19  n08  n27 rack03)
		(fit  n18  n09  n27 rack03)
		(fit  n16  n11  n27 rack03)
		(fit  n09  n18  n27 rack03)
		(fit  n02  n25  n27 rack03)
		(fit  n27  n04  n31 rack03)
		(fit  n23  n08  n31 rack03)
		(fit  n22  n09  n31 rack03)
		(fit  n20  n11  n31 rack03)
		(fit  n13  n18  n31 rack03)
		(fit  n06  n25  n31 rack03)
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
		; Racks 5
		; Rack:rack00
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n05)
		(in jig0002 rack00)
		(clear jig0002 bside)
		(clear jig0002 fside)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n01)
		(in jig0005 rack01)
		(clear jig0005 bside)
		(next-to jig0005 jig0001 bside)
		(next-to jig0001 jig0005 fside)
		(in jig0001 rack01)
		(next-to jig0001 jig0004 bside)
		(next-to jig0004 jig0001 fside)
		(in jig0004 rack01)
		(clear jig0004 fside)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n08)
		(in jig0006 rack02)
		(clear jig0006 bside)
		(clear jig0006 fside)
		; Rack:rack03
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n06)
		(in jig0003 rack03)
		(clear jig0003 bside)
		(clear jig0003 fside)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n01)
		(in jig0007 rack04)
		(clear jig0007 bside)
		(clear jig0007 fside)
		; Jigs (size):
		(is_type jig0001 typeC)
		(size jig0001 n09)
		(empty-size jig0001 n09)
		(empty jig0001)
		(is_type jig0002 typeD)
		(size jig0002 n25)
		(empty-size jig0002 n18)
		(is_type jig0003 typeD)
		(size jig0003 n25)
		(empty-size jig0003 n18)
		(is_type jig0004 typeC)
		(size jig0004 n18)
		(empty-size jig0004 n09)
		(is_type jig0005 typeA)
		(size jig0005 n04)
		(empty-size jig0005 n04)
		(empty jig0005)
		(is_type jig0006 typeD)
		(size jig0006 n18)
		(empty-size jig0006 n18)
		(empty jig0006)
		(is_type jig0007 typeD)
		(size jig0007 n25)
		(empty-size jig0007 n18)
		(is_type jig0008 typeD)
		(size jig0008 n25)
		(empty-size jig0008 n18)
		(is_type jig0009 typeD)
		(size jig0009 n25)
		(empty-size jig0009 n18)
		(is_type jig0010 typeB)
		(size jig0010 n11)
		(empty-size jig0010 n08)
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
		(is_type jig0019 typeB)
		(size jig0019 n11)
		(empty-size jig0019 n08)
		(is_type jig0020 typeB)
		(size jig0020 n11)
		(empty-size jig0020 n08)
		(is_type jig0021 typeB)
		(size jig0021 n11)
		(empty-size jig0021 n08)
		(is_type jig0022 typeB)
		(size jig0022 n11)
		(empty-size jig0022 n08)
		(is_type jig0023 typeB)
		(size jig0023 n11)
		(empty-size jig0023 n08)
		(is_type jig0024 typeB)
		(size jig0024 n11)
		(empty-size jig0024 n08)
		(is_type jig0025 typeB)
		(size jig0025 n11)
		(empty-size jig0025 n08)
		(is_type jig0026 typeC)
		(size jig0026 n18)
		(empty-size jig0026 n09)
		(is_type jig0027 typeC)
		(size jig0027 n18)
		(empty-size jig0027 n09)
		(is_type jig0028 typeD)
		(size jig0028 n25)
		(empty-size jig0028 n18)
		(is_type jig0029 typeB)
		(size jig0029 n11)
		(empty-size jig0029 n08)
		(is_type jig0030 typeB)
		(size jig0030 n11)
		(empty-size jig0030 n08)
		(is_type jig0031 typeD)
		(size jig0031 n25)
		(empty-size jig0031 n18)
		(is_type jig0032 typeC)
		(size jig0032 n18)
		(empty-size jig0032 n09)
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
		(is_type jig0040 typeC)
		(size jig0040 n18)
		(empty-size jig0040 n09)
		(is_type jig0041 typeB)
		(size jig0041 n11)
		(empty-size jig0041 n08)
		(is_type jig0042 typeB)
		(size jig0042 n11)
		(empty-size jig0042 n08)
		(is_type jig0043 typeD)
		(size jig0043 n25)
		(empty-size jig0043 n18)
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
		; Number of flights: 28
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; No jigs
		(to_unload dummy-jig beluga1)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0008
		(to_unload jig0008 beluga2)
		(in jig0008 beluga2)
		(next_unload jig0008 dummy-jig)
		; Flight: beluga3
		; No jigs
		(to_unload dummy-jig beluga3)
		; Flight: beluga4
		; No jigs
		(to_unload dummy-jig beluga4)
		; Flight: beluga5
		; 0: jig0009
		(to_unload jig0009 beluga5)
		(in jig0009 beluga5)
		(next_unload jig0009 dummy-jig)
		; Flight: beluga6
		; 0: jig0010
		(to_unload jig0010 beluga6)
		(in jig0010 beluga6)
		(next_unload jig0010 dummy-jig)
		; Flight: beluga7
		; 0: jig0011 1: jig0012 2: jig0013 3: jig0014 4: jig0015 5: jig0016 6: jig0017 7: jig0018
		(to_unload jig0011 beluga7)
		(in jig0011 beluga7)
		(next_unload jig0011 jig0012)
		(in jig0012 beluga7)
		(next_unload jig0012 jig0013)
		(in jig0013 beluga7)
		(next_unload jig0013 jig0014)
		(in jig0014 beluga7)
		(next_unload jig0014 jig0015)
		(in jig0015 beluga7)
		(next_unload jig0015 jig0016)
		(in jig0016 beluga7)
		(next_unload jig0016 jig0017)
		(in jig0017 beluga7)
		(next_unload jig0017 jig0018)
		(in jig0018 beluga7)
		(next_unload jig0018 dummy-jig)
		; Flight: beluga8
		; No jigs
		(to_unload dummy-jig beluga8)
		; Flight: beluga9
		; 0: jig0019 1: jig0020 2: jig0021
		(to_unload jig0019 beluga9)
		(in jig0019 beluga9)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga9)
		(next_unload jig0020 jig0021)
		(in jig0021 beluga9)
		(next_unload jig0021 dummy-jig)
		; Flight: beluga10
		; 0: jig0022 1: jig0023 2: jig0024
		(to_unload jig0022 beluga10)
		(in jig0022 beluga10)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga10)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga10)
		(next_unload jig0024 dummy-jig)
		; Flight: beluga11
		; 0: jig0025
		(to_unload jig0025 beluga11)
		(in jig0025 beluga11)
		(next_unload jig0025 dummy-jig)
		; Flight: beluga12
		; No jigs
		(to_unload dummy-jig beluga12)
		; Flight: beluga13
		; No jigs
		(to_unload dummy-jig beluga13)
		; Flight: beluga14
		; 0: jig0026 1: jig0027
		(to_unload jig0026 beluga14)
		(in jig0026 beluga14)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga14)
		(next_unload jig0027 dummy-jig)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0028
		(to_unload jig0028 beluga16)
		(in jig0028 beluga16)
		(next_unload jig0028 dummy-jig)
		; Flight: beluga17
		; No jigs
		(to_unload dummy-jig beluga17)
		; Flight: beluga18
		; 0: jig0029 1: jig0030
		(to_unload jig0029 beluga18)
		(in jig0029 beluga18)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga18)
		(next_unload jig0030 dummy-jig)
		; Flight: beluga19
		; 0: jig0031
		(to_unload jig0031 beluga19)
		(in jig0031 beluga19)
		(next_unload jig0031 dummy-jig)
		; Flight: beluga20
		; 0: jig0032
		(to_unload jig0032 beluga20)
		(in jig0032 beluga20)
		(next_unload jig0032 dummy-jig)
		; Flight: beluga21
		; No jigs
		(to_unload dummy-jig beluga21)
		; Flight: beluga22
		; 0: jig0033 1: jig0034 2: jig0035 3: jig0036 4: jig0037 5: jig0038 6: jig0039
		(to_unload jig0033 beluga22)
		(in jig0033 beluga22)
		(next_unload jig0033 jig0034)
		(in jig0034 beluga22)
		(next_unload jig0034 jig0035)
		(in jig0035 beluga22)
		(next_unload jig0035 jig0036)
		(in jig0036 beluga22)
		(next_unload jig0036 jig0037)
		(in jig0037 beluga22)
		(next_unload jig0037 jig0038)
		(in jig0038 beluga22)
		(next_unload jig0038 jig0039)
		(in jig0039 beluga22)
		(next_unload jig0039 dummy-jig)
		; Flight: beluga23
		; 0: jig0040
		(to_unload jig0040 beluga23)
		(in jig0040 beluga23)
		(next_unload jig0040 dummy-jig)
		; Flight: beluga24
		; 0: jig0041 1: jig0042
		(to_unload jig0041 beluga24)
		(in jig0041 beluga24)
		(next_unload jig0041 jig0042)
		(in jig0042 beluga24)
		(next_unload jig0042 dummy-jig)
		; Flight: beluga25
		; No jigs
		(to_unload dummy-jig beluga25)
		; Flight: beluga26
		; No jigs
		(to_unload dummy-jig beluga26)
		; Flight: beluga27
		; No jigs
		(to_unload dummy-jig beluga27)
		; Flight: beluga28
		; 0: jig0043
		(to_unload jig0043 beluga28)
		(in jig0043 beluga28)
		(next_unload jig0043 dummy-jig)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeD)
		(to_load typeD slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; 0: typeA
		(to_load typeA slot0 beluga2)
		(next_load dummy-type slot0 dummy-slot beluga2)
		; 0: typeC
		(to_load typeC slot0 beluga3)
		(next_load dummy-type slot0 dummy-slot beluga3)
		; 0: typeD
		(to_load typeD slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; No jigs
		(to_load dummy-type dummy-slot beluga5)
		; 0: typeD
		(to_load typeD slot0 beluga6)
		(next_load dummy-type slot0 dummy-slot beluga6)
		; No jigs
		(to_load dummy-type dummy-slot beluga7)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga8)
		(next_load typeD slot0 slot1 beluga8)
		(next_load dummy-type slot1 dummy-slot beluga8)
		; 0: typeD
		(to_load typeD slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga10)
		(next_load typeA slot0 slot1 beluga10)
		(next_load typeA slot1 slot2 beluga10)
		(next_load typeA slot2 slot3 beluga10)
		(next_load dummy-type slot3 dummy-slot beluga10)
		; 0: typeC
		(to_load typeC slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeA
		(to_load typeA slot0 beluga12)
		(next_load dummy-type slot0 dummy-slot beluga12)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga13)
		(next_load typeB slot0 slot1 beluga13)
		(next_load typeB slot1 slot2 beluga13)
		(next_load typeB slot2 slot3 beluga13)
		(next_load dummy-type slot3 dummy-slot beluga13)
		; 0: typeA
		(to_load typeA slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeA
		(to_load typeA slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeC
		(to_load typeC slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; 0: typeA
		(to_load typeA slot0 beluga17)
		(next_load dummy-type slot0 dummy-slot beluga17)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga18)
		(next_load typeB slot0 slot1 beluga18)
		(next_load dummy-type slot1 dummy-slot beluga18)
		; No jigs
		(to_load dummy-type dummy-slot beluga19)
		; 0: typeB
		(to_load typeB slot0 beluga20)
		(next_load dummy-type slot0 dummy-slot beluga20)
		; 0: typeB
		(to_load typeB slot0 beluga21)
		(next_load dummy-type slot0 dummy-slot beluga21)
		; 0: typeD
		(to_load typeD slot0 beluga22)
		(next_load dummy-type slot0 dummy-slot beluga22)
		; 0: typeC
		(to_load typeC slot0 beluga23)
		(next_load dummy-type slot0 dummy-slot beluga23)
		; 0: typeA
		(to_load typeA slot0 beluga24)
		(next_load dummy-type slot0 dummy-slot beluga24)
		; 0: typeB
		(to_load typeB slot0 beluga25)
		(next_load dummy-type slot0 dummy-slot beluga25)
		; 0: typeA
		(to_load typeA slot0 beluga26)
		(next_load dummy-type slot0 dummy-slot beluga26)
		; 0: typeC
		(to_load typeC slot0 beluga27)
		(next_load dummy-type slot0 dummy-slot beluga27)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga28)
		(next_load typeB slot0 slot1 beluga28)
		(next_load dummy-type slot1 dummy-slot beluga28)
		; Production schedule:
		; Production line: pl0
		; 0: jig0007 1: jig0009 2: jig0010 3: jig0019 4: jig0021 5: jig0011 6: jig0024 7: jig0028 8: jig0030 9: jig0029 10: jig0031 11: jig0041
		(to_deliver jig0007 pl0)
		(next_deliver jig0007 jig0009)
		(next_deliver jig0009 jig0010)
		(next_deliver jig0010 jig0019)
		(next_deliver jig0019 jig0021)
		(next_deliver jig0021 jig0011)
		(next_deliver jig0011 jig0024)
		(next_deliver jig0024 jig0028)
		(next_deliver jig0028 jig0030)
		(next_deliver jig0030 jig0029)
		(next_deliver jig0029 jig0031)
		(next_deliver jig0031 jig0041)
		(next_deliver jig0041 dummy-jig)
		; Production line: pl1
		; 0: jig0003 1: jig0004 2: jig0016 3: jig0018 4: jig0022 5: jig0017 6: jig0026 7: jig0027 8: jig0042 9: jig0033 10: jig0037
		(to_deliver jig0003 pl1)
		(next_deliver jig0003 jig0004)
		(next_deliver jig0004 jig0016)
		(next_deliver jig0016 jig0018)
		(next_deliver jig0018 jig0022)
		(next_deliver jig0022 jig0017)
		(next_deliver jig0017 jig0026)
		(next_deliver jig0026 jig0027)
		(next_deliver jig0027 jig0042)
		(next_deliver jig0042 jig0033)
		(next_deliver jig0033 jig0037)
		(next_deliver jig0037 dummy-jig)
		; Production line: pl2
		; 0: jig0002 1: jig0008 2: jig0013 3: jig0012 4: jig0015 5: jig0014 6: jig0020 7: jig0023 8: jig0025 9: jig0035 10: jig0036 11: jig0040 12: jig0034
		(to_deliver jig0002 pl2)
		(next_deliver jig0002 jig0008)
		(next_deliver jig0008 jig0013)
		(next_deliver jig0013 jig0012)
		(next_deliver jig0012 jig0015)
		(next_deliver jig0015 jig0014)
		(next_deliver jig0014 jig0020)
		(next_deliver jig0020 jig0023)
		(next_deliver jig0023 jig0025)
		(next_deliver jig0025 jig0035)
		(next_deliver jig0035 jig0036)
		(next_deliver jig0036 jig0040)
		(next_deliver jig0040 jig0034)
		(next_deliver jig0034 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0007)
		(empty jig0009)
		(empty jig0010)
		(empty jig0019)
		(empty jig0021)
		(empty jig0011)
		(empty jig0024)
		(empty jig0028)
		(empty jig0030)
		(empty jig0029)
		(empty jig0031)
		(empty jig0041)
		(empty jig0003)
		(empty jig0004)
		(empty jig0016)
		(empty jig0018)
		(empty jig0022)
		(empty jig0017)
		(empty jig0026)
		(empty jig0027)
		(empty jig0042)
		(empty jig0033)
		(empty jig0037)
		(empty jig0002)
		(empty jig0008)
		(empty jig0013)
		(empty jig0012)
		(empty jig0015)
		(empty jig0014)
		(empty jig0020)
		(empty jig0023)
		(empty jig0025)
		(empty jig0035)
		(empty jig0036)
		(empty jig0040)
		(empty jig0034)
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
	))
  (:metric minimize (total-cost))
)