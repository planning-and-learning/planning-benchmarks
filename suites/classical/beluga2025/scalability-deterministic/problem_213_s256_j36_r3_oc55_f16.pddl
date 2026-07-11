(define
	(problem beluga-problem_213_s256_j36_r3_oc55_f16)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 23, 24, 25, 27, 32}
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
		n18 - num
		n19 - num
		n20 - num
		n23 - num
		n24 - num
		n25 - num
		n27 - num
		n32 - num
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
		(fit  n10  n04  n14 rack00)
		(fit  n06  n08  n14 rack00)
		(fit  n05  n09  n14 rack00)
		(fit  n03  n11  n14 rack00)
		(fit  n11  n04  n15 rack00)
		(fit  n07  n08  n15 rack00)
		(fit  n06  n09  n15 rack00)
		(fit  n04  n11  n15 rack00)
		(fit  n15  n04  n19 rack00)
		(fit  n11  n08  n19 rack00)
		(fit  n10  n09  n19 rack00)
		(fit  n08  n11  n19 rack00)
		(fit  n01  n18  n19 rack00)
		(fit  n19  n04  n23 rack00)
		(fit  n15  n08  n23 rack00)
		(fit  n14  n09  n23 rack00)
		(fit  n12  n11  n23 rack00)
		(fit  n05  n18  n23 rack00)
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
		(fit  n19  n04  n23 rack01)
		(fit  n15  n08  n23 rack01)
		(fit  n14  n09  n23 rack01)
		(fit  n12  n11  n23 rack01)
		(fit  n05  n18  n23 rack01)
		(fit  n23  n04  n27 rack01)
		(fit  n19  n08  n27 rack01)
		(fit  n18  n09  n27 rack01)
		(fit  n16  n11  n27 rack01)
		(fit  n09  n18  n27 rack01)
		(fit  n02  n25  n27 rack01)
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
		(fit  n11  n04  n15 rack02)
		(fit  n07  n08  n15 rack02)
		(fit  n06  n09  n15 rack02)
		(fit  n04  n11  n15 rack02)
		(fit  n12  n04  n16 rack02)
		(fit  n08  n08  n16 rack02)
		(fit  n07  n09  n16 rack02)
		(fit  n05  n11  n16 rack02)
		(fit  n16  n04  n20 rack02)
		(fit  n12  n08  n20 rack02)
		(fit  n11  n09  n20 rack02)
		(fit  n09  n11  n20 rack02)
		(fit  n02  n18  n20 rack02)
		(fit  n20  n04  n24 rack02)
		(fit  n16  n08  n24 rack02)
		(fit  n15  n09  n24 rack02)
		(fit  n13  n11  n24 rack02)
		(fit  n06  n18  n24 rack02)
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
		; Racks 3
		; Rack:rack00
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n19)
		(in jig0006 rack00)
		(clear jig0006 bside)
		(clear jig0006 fside)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n04)
		(in jig0004 rack01)
		(clear jig0004 bside)
		(next-to jig0004 jig0001 bside)
		(next-to jig0001 jig0004 fside)
		(in jig0001 rack01)
		(next-to jig0001 jig0003 bside)
		(next-to jig0003 jig0001 fside)
		(in jig0003 rack01)
		(clear jig0003 fside)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n09)
		(in jig0005 rack02)
		(clear jig0005 bside)
		(next-to jig0005 jig0002 bside)
		(next-to jig0002 jig0005 fside)
		(in jig0002 rack02)
		(clear jig0002 fside)
		; Jigs (size):
		(is_type jig0001 typeA)
		(size jig0001 n04)
		(empty-size jig0001 n04)
		(is_type jig0002 typeB)
		(size jig0002 n11)
		(empty-size jig0002 n08)
		(is_type jig0003 typeB)
		(size jig0003 n11)
		(empty-size jig0003 n08)
		(is_type jig0004 typeB)
		(size jig0004 n08)
		(empty-size jig0004 n08)
		(empty jig0004)
		(is_type jig0005 typeA)
		(size jig0005 n04)
		(empty-size jig0005 n04)
		(empty jig0005)
		(is_type jig0006 typeA)
		(size jig0006 n04)
		(empty-size jig0006 n04)
		(empty jig0006)
		(is_type jig0007 typeB)
		(size jig0007 n11)
		(empty-size jig0007 n08)
		(is_type jig0008 typeB)
		(size jig0008 n11)
		(empty-size jig0008 n08)
		(is_type jig0009 typeC)
		(size jig0009 n18)
		(empty-size jig0009 n09)
		(is_type jig0010 typeA)
		(size jig0010 n04)
		(empty-size jig0010 n04)
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
		(is_type jig0017 typeC)
		(size jig0017 n18)
		(empty-size jig0017 n09)
		(is_type jig0018 typeA)
		(size jig0018 n04)
		(empty-size jig0018 n04)
		(is_type jig0019 typeA)
		(size jig0019 n04)
		(empty-size jig0019 n04)
		(is_type jig0020 typeA)
		(size jig0020 n04)
		(empty-size jig0020 n04)
		(is_type jig0021 typeA)
		(size jig0021 n04)
		(empty-size jig0021 n04)
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
		(is_type jig0032 typeA)
		(size jig0032 n04)
		(empty-size jig0032 n04)
		(is_type jig0033 typeA)
		(size jig0033 n04)
		(empty-size jig0033 n04)
		(is_type jig0034 typeA)
		(size jig0034 n04)
		(empty-size jig0034 n04)
		(is_type jig0035 typeB)
		(size jig0035 n11)
		(empty-size jig0035 n08)
		(is_type jig0036 typeC)
		(size jig0036 n18)
		(empty-size jig0036 n09)
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
		; Number of flights: 16
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0007 1: jig0008
		(to_unload jig0007 beluga1)
		(in jig0007 beluga1)
		(next_unload jig0007 jig0008)
		(in jig0008 beluga1)
		(next_unload jig0008 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; No jigs
		(to_unload dummy-jig beluga2)
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
		; 0: jig0010 1: jig0011 2: jig0012 3: jig0013 4: jig0014 5: jig0015 6: jig0016
		(to_unload jig0010 beluga6)
		(in jig0010 beluga6)
		(next_unload jig0010 jig0011)
		(in jig0011 beluga6)
		(next_unload jig0011 jig0012)
		(in jig0012 beluga6)
		(next_unload jig0012 jig0013)
		(in jig0013 beluga6)
		(next_unload jig0013 jig0014)
		(in jig0014 beluga6)
		(next_unload jig0014 jig0015)
		(in jig0015 beluga6)
		(next_unload jig0015 jig0016)
		(in jig0016 beluga6)
		(next_unload jig0016 dummy-jig)
		; Flight: beluga7
		; 0: jig0017
		(to_unload jig0017 beluga7)
		(in jig0017 beluga7)
		(next_unload jig0017 dummy-jig)
		; Flight: beluga8
		; 0: jig0018 1: jig0019 2: jig0020 3: jig0021
		(to_unload jig0018 beluga8)
		(in jig0018 beluga8)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga8)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga8)
		(next_unload jig0020 jig0021)
		(in jig0021 beluga8)
		(next_unload jig0021 dummy-jig)
		; Flight: beluga9
		; 0: jig0022 1: jig0023 2: jig0024
		(to_unload jig0022 beluga9)
		(in jig0022 beluga9)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga9)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga9)
		(next_unload jig0024 dummy-jig)
		; Flight: beluga10
		; No jigs
		(to_unload dummy-jig beluga10)
		; Flight: beluga11
		; No jigs
		(to_unload dummy-jig beluga11)
		; Flight: beluga12
		; 0: jig0025 1: jig0026 2: jig0027 3: jig0028 4: jig0029 5: jig0030 6: jig0031 7: jig0032 8: jig0033 9: jig0034
		(to_unload jig0025 beluga12)
		(in jig0025 beluga12)
		(next_unload jig0025 jig0026)
		(in jig0026 beluga12)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga12)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga12)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga12)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga12)
		(next_unload jig0030 jig0031)
		(in jig0031 beluga12)
		(next_unload jig0031 jig0032)
		(in jig0032 beluga12)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga12)
		(next_unload jig0033 jig0034)
		(in jig0034 beluga12)
		(next_unload jig0034 dummy-jig)
		; Flight: beluga13
		; No jigs
		(to_unload dummy-jig beluga13)
		; Flight: beluga14
		; 0: jig0035
		(to_unload jig0035 beluga14)
		(in jig0035 beluga14)
		(next_unload jig0035 dummy-jig)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0036
		(to_unload jig0036 beluga16)
		(in jig0036 beluga16)
		(next_unload jig0036 dummy-jig)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeB)
		(to_load typeB slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga2)
		(next_load typeA slot0 slot1 beluga2)
		(next_load dummy-type slot1 dummy-slot beluga2)
		; 0: typeB
		(to_load typeB slot0 beluga3)
		(next_load dummy-type slot0 dummy-slot beluga3)
		; 0: typeB
		(to_load typeB slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; No jigs
		(to_load dummy-type dummy-slot beluga5)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga6)
		(next_load typeB slot0 slot1 beluga6)
		(next_load dummy-type slot1 dummy-slot beluga6)
		; 0: typeC
		(to_load typeC slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga8)
		(next_load typeA slot0 slot1 beluga8)
		(next_load dummy-type slot1 dummy-slot beluga8)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga9)
		(next_load typeA slot0 slot1 beluga9)
		(next_load dummy-type slot1 dummy-slot beluga9)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga10)
		(next_load typeA slot0 slot1 beluga10)
		(next_load typeA slot1 slot2 beluga10)
		(next_load typeA slot2 slot3 beluga10)
		(next_load typeA slot3 slot4 beluga10)
		(next_load dummy-type slot4 dummy-slot beluga10)
		; 0: typeC
		(to_load typeC slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeA
		(to_load typeA slot0 beluga12)
		(next_load dummy-type slot0 dummy-slot beluga12)
		; 0: typeA
		(to_load typeA slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; No jigs
		(to_load dummy-type dummy-slot beluga14)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga15)
		(next_load typeA slot0 slot1 beluga15)
		(next_load typeA slot1 slot2 beluga15)
		(next_load typeA slot2 slot3 beluga15)
		(next_load typeA slot3 slot4 beluga15)
		(next_load dummy-type slot4 dummy-slot beluga15)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga16)
		(next_load typeA slot0 slot1 beluga16)
		(next_load typeA slot1 slot2 beluga16)
		(next_load typeA slot2 slot3 beluga16)
		(next_load dummy-type slot3 dummy-slot beluga16)
		; Production schedule:
		; Production line: pl0
		; 0: jig0003 1: jig0002 2: jig0009 3: jig0015 4: jig0016 5: jig0012 6: jig0014 7: jig0017 8: jig0018 9: jig0023 10: jig0027 11: jig0021 12: jig0033 13: jig0028
		(to_deliver jig0003 pl0)
		(next_deliver jig0003 jig0002)
		(next_deliver jig0002 jig0009)
		(next_deliver jig0009 jig0015)
		(next_deliver jig0015 jig0016)
		(next_deliver jig0016 jig0012)
		(next_deliver jig0012 jig0014)
		(next_deliver jig0014 jig0017)
		(next_deliver jig0017 jig0018)
		(next_deliver jig0018 jig0023)
		(next_deliver jig0023 jig0027)
		(next_deliver jig0027 jig0021)
		(next_deliver jig0021 jig0033)
		(next_deliver jig0033 jig0028)
		(next_deliver jig0028 dummy-jig)
		; Production line: pl1
		; 0: jig0008 1: jig0007 2: jig0010 3: jig0001 4: jig0011 5: jig0013 6: jig0022 7: jig0019 8: jig0020 9: jig0024 10: jig0029 11: jig0025 12: jig0034 13: jig0031
		(to_deliver jig0008 pl1)
		(next_deliver jig0008 jig0007)
		(next_deliver jig0007 jig0010)
		(next_deliver jig0010 jig0001)
		(next_deliver jig0001 jig0011)
		(next_deliver jig0011 jig0013)
		(next_deliver jig0013 jig0022)
		(next_deliver jig0022 jig0019)
		(next_deliver jig0019 jig0020)
		(next_deliver jig0020 jig0024)
		(next_deliver jig0024 jig0029)
		(next_deliver jig0029 jig0025)
		(next_deliver jig0025 jig0034)
		(next_deliver jig0034 jig0031)
		(next_deliver jig0031 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0003)
		(empty jig0002)
		(empty jig0009)
		(empty jig0015)
		(empty jig0016)
		(empty jig0012)
		(empty jig0014)
		(empty jig0017)
		(empty jig0018)
		(empty jig0023)
		(empty jig0027)
		(empty jig0021)
		(empty jig0033)
		(empty jig0028)
		(empty jig0008)
		(empty jig0007)
		(empty jig0010)
		(empty jig0001)
		(empty jig0011)
		(empty jig0013)
		(empty jig0022)
		(empty jig0019)
		(empty jig0020)
		(empty jig0024)
		(empty jig0029)
		(empty jig0025)
		(empty jig0034)
		(empty jig0031)
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
	))
  (:metric minimize (total-cost))
)