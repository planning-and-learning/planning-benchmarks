(define
	(problem beluga-problem_66_s108_j28_r4_oc21_f23)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 29, 30, 32, 34, 38}
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
		n25 - num
		n26 - num
		n27 - num
		n29 - num
		n30 - num
		n32 - num
		n34 - num
		n38 - num
		; trailers:
		beluga_trailer_1 - trailer
		beluga_trailer_2 - trailer
		beluga_trailer_3 - trailer
		factory_trailer_1 - trailer
		factory_trailer_2 - trailer
		; Racks:
		rack00 - rack
		rack01 - rack
		rack02 - rack
		rack03 - rack
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
		(fit  n12  n04  n16 rack00)
		(fit  n08  n08  n16 rack00)
		(fit  n07  n09  n16 rack00)
		(fit  n05  n11  n16 rack00)
		(fit  n13  n04  n17 rack00)
		(fit  n09  n08  n17 rack00)
		(fit  n08  n09  n17 rack00)
		(fit  n06  n11  n17 rack00)
		(fit  n17  n04  n21 rack00)
		(fit  n13  n08  n21 rack00)
		(fit  n12  n09  n21 rack00)
		(fit  n10  n11  n21 rack00)
		(fit  n03  n18  n21 rack00)
		(fit  n21  n04  n25 rack00)
		(fit  n17  n08  n25 rack00)
		(fit  n16  n09  n25 rack00)
		(fit  n14  n11  n25 rack00)
		(fit  n07  n18  n25 rack00)
		(fit  n00  n25  n25 rack00)
		; Sizes fitting rack: rack01
		(fit  n00  n04  n04 rack01)
		(fit  n01  n04  n05 rack01)
		(fit  n02  n04  n06 rack01)
		(fit  n03  n04  n07 rack01)
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
		(fit  n09  n04  n13 rack01)
		(fit  n05  n08  n13 rack01)
		(fit  n04  n09  n13 rack01)
		(fit  n02  n11  n13 rack01)
		(fit  n10  n04  n14 rack01)
		(fit  n06  n08  n14 rack01)
		(fit  n05  n09  n14 rack01)
		(fit  n03  n11  n14 rack01)
		(fit  n14  n04  n18 rack01)
		(fit  n10  n08  n18 rack01)
		(fit  n09  n09  n18 rack01)
		(fit  n07  n11  n18 rack01)
		(fit  n00  n18  n18 rack01)
		(fit  n18  n04  n22 rack01)
		(fit  n14  n08  n22 rack01)
		(fit  n13  n09  n22 rack01)
		(fit  n11  n11  n22 rack01)
		(fit  n04  n18  n22 rack01)
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
		(fit  n22  n04  n26 rack02)
		(fit  n18  n08  n26 rack02)
		(fit  n17  n09  n26 rack02)
		(fit  n15  n11  n26 rack02)
		(fit  n08  n18  n26 rack02)
		(fit  n01  n25  n26 rack02)
		(fit  n26  n04  n30 rack02)
		(fit  n22  n08  n30 rack02)
		(fit  n21  n09  n30 rack02)
		(fit  n19  n11  n30 rack02)
		(fit  n12  n18  n30 rack02)
		(fit  n05  n25  n30 rack02)
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
		(fit  n13  n04  n17 rack03)
		(fit  n09  n08  n17 rack03)
		(fit  n08  n09  n17 rack03)
		(fit  n06  n11  n17 rack03)
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
		(fit  n17  n04  n21 rack03)
		(fit  n13  n08  n21 rack03)
		(fit  n12  n09  n21 rack03)
		(fit  n10  n11  n21 rack03)
		(fit  n03  n18  n21 rack03)
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
		(fit  n21  n04  n25 rack03)
		(fit  n17  n08  n25 rack03)
		(fit  n16  n09  n25 rack03)
		(fit  n14  n11  n25 rack03)
		(fit  n07  n18  n25 rack03)
		(fit  n00  n25  n25 rack03)
		(fit  n22  n04  n26 rack03)
		(fit  n18  n08  n26 rack03)
		(fit  n17  n09  n26 rack03)
		(fit  n15  n11  n26 rack03)
		(fit  n08  n18  n26 rack03)
		(fit  n01  n25  n26 rack03)
		(fit  n23  n04  n27 rack03)
		(fit  n19  n08  n27 rack03)
		(fit  n18  n09  n27 rack03)
		(fit  n16  n11  n27 rack03)
		(fit  n09  n18  n27 rack03)
		(fit  n02  n25  n27 rack03)
		(fit  n25  n04  n29 rack03)
		(fit  n21  n08  n29 rack03)
		(fit  n20  n09  n29 rack03)
		(fit  n18  n11  n29 rack03)
		(fit  n11  n18  n29 rack03)
		(fit  n04  n25  n29 rack03)
		(fit  n26  n04  n30 rack03)
		(fit  n22  n08  n30 rack03)
		(fit  n21  n09  n30 rack03)
		(fit  n19  n11  n30 rack03)
		(fit  n12  n18  n30 rack03)
		(fit  n05  n25  n30 rack03)
		(fit  n02  n32  n34 rack03)
		(fit  n30  n04  n34 rack03)
		(fit  n26  n08  n34 rack03)
		(fit  n25  n09  n34 rack03)
		(fit  n23  n11  n34 rack03)
		(fit  n16  n18  n34 rack03)
		(fit  n09  n25  n34 rack03)
		(fit  n06  n32  n38 rack03)
		(fit  n34  n04  n38 rack03)
		(fit  n30  n08  n38 rack03)
		(fit  n29  n09  n38 rack03)
		(fit  n27  n11  n38 rack03)
		(fit  n20  n18  n38 rack03)
		(fit  n13  n25  n38 rack03)
		; trailers (Beluga side):
		(empty beluga_trailer_1)
		(at-side beluga_trailer_1 bside)
		(empty beluga_trailer_2)
		(at-side beluga_trailer_2 bside)
		(empty beluga_trailer_3)
		(at-side beluga_trailer_3 bside)
		; trailers (Factory side):
		(empty factory_trailer_1)
		(at-side factory_trailer_1 fside)
		(empty factory_trailer_2)
		(at-side factory_trailer_2 fside)
		; Racks 4
		; Rack:rack00
		(empty rack00)
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n25)
		; Rack:rack01
		(empty rack01)
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n22)
		; Rack:rack02
		(empty rack02)
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n30)
		; Rack:rack03
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n06)
		(in jig0001 rack03)
		(clear jig0001 bside)
		(clear jig0001 fside)
		; Jigs (size):
		(is_type jig0001 typeE)
		(size jig0001 n32)
		(empty-size jig0001 n32)
		(empty jig0001)
		(is_type jig0002 typeD)
		(size jig0002 n25)
		(empty-size jig0002 n18)
		(is_type jig0003 typeC)
		(size jig0003 n18)
		(empty-size jig0003 n09)
		(is_type jig0004 typeC)
		(size jig0004 n18)
		(empty-size jig0004 n09)
		(is_type jig0005 typeD)
		(size jig0005 n25)
		(empty-size jig0005 n18)
		(is_type jig0006 typeB)
		(size jig0006 n11)
		(empty-size jig0006 n08)
		(is_type jig0007 typeB)
		(size jig0007 n11)
		(empty-size jig0007 n08)
		(is_type jig0008 typeB)
		(size jig0008 n11)
		(empty-size jig0008 n08)
		(is_type jig0009 typeB)
		(size jig0009 n11)
		(empty-size jig0009 n08)
		(is_type jig0010 typeB)
		(size jig0010 n11)
		(empty-size jig0010 n08)
		(is_type jig0011 typeC)
		(size jig0011 n18)
		(empty-size jig0011 n09)
		(is_type jig0012 typeC)
		(size jig0012 n18)
		(empty-size jig0012 n09)
		(is_type jig0013 typeB)
		(size jig0013 n11)
		(empty-size jig0013 n08)
		(is_type jig0014 typeB)
		(size jig0014 n11)
		(empty-size jig0014 n08)
		(is_type jig0015 typeD)
		(size jig0015 n25)
		(empty-size jig0015 n18)
		(is_type jig0016 typeB)
		(size jig0016 n11)
		(empty-size jig0016 n08)
		(is_type jig0017 typeB)
		(size jig0017 n11)
		(empty-size jig0017 n08)
		(is_type jig0018 typeA)
		(size jig0018 n04)
		(empty-size jig0018 n04)
		(is_type jig0019 typeA)
		(size jig0019 n04)
		(empty-size jig0019 n04)
		(is_type jig0020 typeA)
		(size jig0020 n04)
		(empty-size jig0020 n04)
		(is_type jig0021 typeD)
		(size jig0021 n25)
		(empty-size jig0021 n18)
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
		(is_type jig0026 typeB)
		(size jig0026 n11)
		(empty-size jig0026 n08)
		(is_type jig0027 typeC)
		(size jig0027 n18)
		(empty-size jig0027 n09)
		(is_type jig0028 typeC)
		(size jig0028 n18)
		(empty-size jig0028 n09)
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
		; Number of flights: 23
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0002
		(to_unload jig0002 beluga1)
		(in jig0002 beluga1)
		(next_unload jig0002 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0003 1: jig0004
		(to_unload jig0003 beluga2)
		(in jig0003 beluga2)
		(next_unload jig0003 jig0004)
		(in jig0004 beluga2)
		(next_unload jig0004 dummy-jig)
		; Flight: beluga3
		; 0: jig0005
		(to_unload jig0005 beluga3)
		(in jig0005 beluga3)
		(next_unload jig0005 dummy-jig)
		; Flight: beluga4
		; 0: jig0006 1: jig0007
		(to_unload jig0006 beluga4)
		(in jig0006 beluga4)
		(next_unload jig0006 jig0007)
		(in jig0007 beluga4)
		(next_unload jig0007 dummy-jig)
		; Flight: beluga5
		; No jigs
		(to_unload dummy-jig beluga5)
		; Flight: beluga6
		; 0: jig0008 1: jig0009 2: jig0010
		(to_unload jig0008 beluga6)
		(in jig0008 beluga6)
		(next_unload jig0008 jig0009)
		(in jig0009 beluga6)
		(next_unload jig0009 jig0010)
		(in jig0010 beluga6)
		(next_unload jig0010 dummy-jig)
		; Flight: beluga7
		; 0: jig0011 1: jig0012
		(to_unload jig0011 beluga7)
		(in jig0011 beluga7)
		(next_unload jig0011 jig0012)
		(in jig0012 beluga7)
		(next_unload jig0012 dummy-jig)
		; Flight: beluga8
		; 0: jig0013 1: jig0014
		(to_unload jig0013 beluga8)
		(in jig0013 beluga8)
		(next_unload jig0013 jig0014)
		(in jig0014 beluga8)
		(next_unload jig0014 dummy-jig)
		; Flight: beluga9
		; No jigs
		(to_unload dummy-jig beluga9)
		; Flight: beluga10
		; No jigs
		(to_unload dummy-jig beluga10)
		; Flight: beluga11
		; 0: jig0015
		(to_unload jig0015 beluga11)
		(in jig0015 beluga11)
		(next_unload jig0015 dummy-jig)
		; Flight: beluga12
		; 0: jig0016 1: jig0017
		(to_unload jig0016 beluga12)
		(in jig0016 beluga12)
		(next_unload jig0016 jig0017)
		(in jig0017 beluga12)
		(next_unload jig0017 dummy-jig)
		; Flight: beluga13
		; 0: jig0018 1: jig0019 2: jig0020
		(to_unload jig0018 beluga13)
		(in jig0018 beluga13)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga13)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga13)
		(next_unload jig0020 dummy-jig)
		; Flight: beluga14
		; No jigs
		(to_unload dummy-jig beluga14)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0021
		(to_unload jig0021 beluga16)
		(in jig0021 beluga16)
		(next_unload jig0021 dummy-jig)
		; Flight: beluga17
		; 0: jig0022 1: jig0023 2: jig0024
		(to_unload jig0022 beluga17)
		(in jig0022 beluga17)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga17)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga17)
		(next_unload jig0024 dummy-jig)
		; Flight: beluga18
		; No jigs
		(to_unload dummy-jig beluga18)
		; Flight: beluga19
		; No jigs
		(to_unload dummy-jig beluga19)
		; Flight: beluga20
		; No jigs
		(to_unload dummy-jig beluga20)
		; Flight: beluga21
		; 0: jig0025 1: jig0026
		(to_unload jig0025 beluga21)
		(in jig0025 beluga21)
		(next_unload jig0025 jig0026)
		(in jig0026 beluga21)
		(next_unload jig0026 dummy-jig)
		; Flight: beluga22
		; 0: jig0027 1: jig0028
		(to_unload jig0027 beluga22)
		(in jig0027 beluga22)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga22)
		(next_unload jig0028 dummy-jig)
		; Flight: beluga23
		; No jigs
		(to_unload dummy-jig beluga23)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeE)
		(to_load typeE slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; No jigs
		(to_load dummy-type dummy-slot beluga2)
		; No jigs
		(to_load dummy-type dummy-slot beluga3)
		; No jigs
		(to_load dummy-type dummy-slot beluga4)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga5)
		(next_load typeD slot0 slot1 beluga5)
		(next_load dummy-type slot1 dummy-slot beluga5)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga6)
		(next_load typeC slot0 slot1 beluga6)
		(next_load dummy-type slot1 dummy-slot beluga6)
		; 0: typeB
		(to_load typeB slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; No jigs
		(to_load dummy-type dummy-slot beluga8)
		; 0: typeB
		(to_load typeB slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeC
		(to_load typeC slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga11)
		(next_load typeB slot0 slot1 beluga11)
		(next_load dummy-type slot1 dummy-slot beluga11)
		; No jigs
		(to_load dummy-type dummy-slot beluga12)
		; 0: typeB
		(to_load typeB slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeC
		(to_load typeC slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga15)
		(next_load typeB slot0 slot1 beluga15)
		(next_load dummy-type slot1 dummy-slot beluga15)
		; 0: typeA
		(to_load typeA slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; No jigs
		(to_load dummy-type dummy-slot beluga17)
		; 0: typeA
		(to_load typeA slot0 beluga18)
		(next_load dummy-type slot0 dummy-slot beluga18)
		; 0: typeB
		(to_load typeB slot0 beluga19)
		(next_load dummy-type slot0 dummy-slot beluga19)
		; 0: typeD
		(to_load typeD slot0 beluga20)
		(next_load dummy-type slot0 dummy-slot beluga20)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga21)
		(next_load typeB slot0 slot1 beluga21)
		(next_load typeB slot1 slot2 beluga21)
		(next_load dummy-type slot2 dummy-slot beluga21)
		; 0: typeB
		(to_load typeB slot0 beluga22)
		(next_load dummy-type slot0 dummy-slot beluga22)
		; 0: typeA
		(to_load typeA slot0 beluga23)
		(next_load dummy-type slot0 dummy-slot beluga23)
		; Production schedule:
		; Production line: pl0
		; 0: jig0002 1: jig0004 2: jig0006 3: jig0012 4: jig0014 5: jig0007 6: jig0013 7: jig0015 8: jig0018 9: jig0017 10: jig0021 11: jig0024
		(to_deliver jig0002 pl0)
		(next_deliver jig0002 jig0004)
		(next_deliver jig0004 jig0006)
		(next_deliver jig0006 jig0012)
		(next_deliver jig0012 jig0014)
		(next_deliver jig0014 jig0007)
		(next_deliver jig0007 jig0013)
		(next_deliver jig0013 jig0015)
		(next_deliver jig0015 jig0018)
		(next_deliver jig0018 jig0017)
		(next_deliver jig0017 jig0021)
		(next_deliver jig0021 jig0024)
		(next_deliver jig0024 dummy-jig)
		; Production line: pl1
		; 0: jig0003 1: jig0005 2: jig0009 3: jig0008 4: jig0010 5: jig0011 6: jig0019 7: jig0016 8: jig0022 9: jig0020 10: jig0023 11: jig0025
		(to_deliver jig0003 pl1)
		(next_deliver jig0003 jig0005)
		(next_deliver jig0005 jig0009)
		(next_deliver jig0009 jig0008)
		(next_deliver jig0008 jig0010)
		(next_deliver jig0010 jig0011)
		(next_deliver jig0011 jig0019)
		(next_deliver jig0019 jig0016)
		(next_deliver jig0016 jig0022)
		(next_deliver jig0022 jig0020)
		(next_deliver jig0020 jig0023)
		(next_deliver jig0023 jig0025)
		(next_deliver jig0025 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0002)
		(empty jig0004)
		(empty jig0006)
		(empty jig0012)
		(empty jig0014)
		(empty jig0007)
		(empty jig0013)
		(empty jig0015)
		(empty jig0018)
		(empty jig0017)
		(empty jig0021)
		(empty jig0024)
		(empty jig0003)
		(empty jig0005)
		(empty jig0009)
		(empty jig0008)
		(empty jig0010)
		(empty jig0011)
		(empty jig0019)
		(empty jig0016)
		(empty jig0022)
		(empty jig0020)
		(empty jig0023)
		(empty jig0025)
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
	))
  (:metric minimize (total-cost))
)