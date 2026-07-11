(define
	(problem beluga-problem_138_s180_j53_r3_oc81_f17)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 31, 32}
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
		n22 - num
		n23 - num
		n24 - num
		n25 - num
		n26 - num
		n27 - num
		n31 - num
		n32 - num
		; trailers:
		beluga_trailer_1 - trailer
		beluga_trailer_2 - trailer
		factory_trailer_1 - trailer
		factory_trailer_2 - trailer
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
		typeA - type
		typeB - type
		typeC - type
		typeD - type
		typeE - type
		; hangars:
		hangar1 - hangar
		hangar2 - hangar
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
		; Slots for outgoing flights:
		slot0 - slot
		slot1 - slot
		slot2 - slot
		slot3 - slot
		slot4 - slot
		; Production lines:
		pl0 - production-line
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
		(fit  n11  n04  n15 rack00)
		(fit  n07  n08  n15 rack00)
		(fit  n06  n09  n15 rack00)
		(fit  n04  n11  n15 rack00)
		(fit  n12  n04  n16 rack00)
		(fit  n08  n08  n16 rack00)
		(fit  n07  n09  n16 rack00)
		(fit  n05  n11  n16 rack00)
		(fit  n16  n04  n20 rack00)
		(fit  n12  n08  n20 rack00)
		(fit  n11  n09  n20 rack00)
		(fit  n09  n11  n20 rack00)
		(fit  n02  n18  n20 rack00)
		(fit  n20  n04  n24 rack00)
		(fit  n16  n08  n24 rack00)
		(fit  n15  n09  n24 rack00)
		(fit  n13  n11  n24 rack00)
		(fit  n06  n18  n24 rack00)
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
		; Racks 3
		; Rack:rack00
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n05)
		(in jig0005 rack00)
		(clear jig0005 bside)
		(next-to jig0005 jig0004 bside)
		(next-to jig0004 jig0005 fside)
		(in jig0004 rack00)
		(next-to jig0004 jig0007 bside)
		(next-to jig0007 jig0004 fside)
		(in jig0007 rack00)
		(clear jig0007 fside)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n02)
		(in jig0006 rack01)
		(clear jig0006 bside)
		(next-to jig0006 jig0002 bside)
		(next-to jig0002 jig0006 fside)
		(in jig0002 rack01)
		(clear jig0002 fside)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n07)
		(in jig0003 rack02)
		(clear jig0003 bside)
		(next-to jig0003 jig0001 bside)
		(next-to jig0001 jig0003 fside)
		(in jig0001 rack02)
		(next-to jig0001 jig0008 bside)
		(next-to jig0008 jig0001 fside)
		(in jig0008 rack02)
		(clear jig0008 fside)
		; Jigs (size):
		(is_type jig0001 typeB)
		(size jig0001 n11)
		(empty-size jig0001 n08)
		(is_type jig0002 typeD)
		(size jig0002 n25)
		(empty-size jig0002 n18)
		(is_type jig0003 typeA)
		(size jig0003 n04)
		(empty-size jig0003 n04)
		(empty jig0003)
		(is_type jig0004 typeB)
		(size jig0004 n11)
		(empty-size jig0004 n08)
		(is_type jig0005 typeA)
		(size jig0005 n04)
		(empty-size jig0005 n04)
		(empty jig0005)
		(is_type jig0006 typeA)
		(size jig0006 n04)
		(empty-size jig0006 n04)
		(empty jig0006)
		(is_type jig0007 typeA)
		(size jig0007 n04)
		(empty-size jig0007 n04)
		(is_type jig0008 typeA)
		(size jig0008 n04)
		(empty-size jig0008 n04)
		(is_type jig0009 typeA)
		(size jig0009 n04)
		(empty-size jig0009 n04)
		(is_type jig0010 typeA)
		(size jig0010 n04)
		(empty-size jig0010 n04)
		(is_type jig0011 typeB)
		(size jig0011 n11)
		(empty-size jig0011 n08)
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
		(is_type jig0040 typeB)
		(size jig0040 n11)
		(empty-size jig0040 n08)
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
		(is_type jig0050 typeA)
		(size jig0050 n04)
		(empty-size jig0050 n04)
		(is_type jig0051 typeA)
		(size jig0051 n04)
		(empty-size jig0051 n04)
		(is_type jig0052 typeA)
		(size jig0052 n04)
		(empty-size jig0052 n04)
		(is_type jig0053 typeB)
		(size jig0053 n11)
		(empty-size jig0053 n08)
		; hangars:
		(empty hangar1)
		(empty hangar2)
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
		; Number of flights: 17
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0009 1: jig0010
		(to_unload jig0009 beluga1)
		(in jig0009 beluga1)
		(next_unload jig0009 jig0010)
		(in jig0010 beluga1)
		(next_unload jig0010 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0011
		(to_unload jig0011 beluga2)
		(in jig0011 beluga2)
		(next_unload jig0011 dummy-jig)
		; Flight: beluga3
		; No jigs
		(to_unload dummy-jig beluga3)
		; Flight: beluga4
		; 0: jig0012 1: jig0013
		(to_unload jig0012 beluga4)
		(in jig0012 beluga4)
		(next_unload jig0012 jig0013)
		(in jig0013 beluga4)
		(next_unload jig0013 dummy-jig)
		; Flight: beluga5
		; No jigs
		(to_unload dummy-jig beluga5)
		; Flight: beluga6
		; 0: jig0014 1: jig0015 2: jig0016 3: jig0017 4: jig0018 5: jig0019 6: jig0020
		(to_unload jig0014 beluga6)
		(in jig0014 beluga6)
		(next_unload jig0014 jig0015)
		(in jig0015 beluga6)
		(next_unload jig0015 jig0016)
		(in jig0016 beluga6)
		(next_unload jig0016 jig0017)
		(in jig0017 beluga6)
		(next_unload jig0017 jig0018)
		(in jig0018 beluga6)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga6)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga6)
		(next_unload jig0020 dummy-jig)
		; Flight: beluga7
		; 0: jig0021 1: jig0022 2: jig0023 3: jig0024 4: jig0025 5: jig0026
		(to_unload jig0021 beluga7)
		(in jig0021 beluga7)
		(next_unload jig0021 jig0022)
		(in jig0022 beluga7)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga7)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga7)
		(next_unload jig0024 jig0025)
		(in jig0025 beluga7)
		(next_unload jig0025 jig0026)
		(in jig0026 beluga7)
		(next_unload jig0026 dummy-jig)
		; Flight: beluga8
		; No jigs
		(to_unload dummy-jig beluga8)
		; Flight: beluga9
		; 0: jig0027 1: jig0028 2: jig0029 3: jig0030 4: jig0031 5: jig0032 6: jig0033
		(to_unload jig0027 beluga9)
		(in jig0027 beluga9)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga9)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga9)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga9)
		(next_unload jig0030 jig0031)
		(in jig0031 beluga9)
		(next_unload jig0031 jig0032)
		(in jig0032 beluga9)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga9)
		(next_unload jig0033 dummy-jig)
		; Flight: beluga10
		; No jigs
		(to_unload dummy-jig beluga10)
		; Flight: beluga11
		; 0: jig0034 1: jig0035 2: jig0036 3: jig0037 4: jig0038 5: jig0039
		(to_unload jig0034 beluga11)
		(in jig0034 beluga11)
		(next_unload jig0034 jig0035)
		(in jig0035 beluga11)
		(next_unload jig0035 jig0036)
		(in jig0036 beluga11)
		(next_unload jig0036 jig0037)
		(in jig0037 beluga11)
		(next_unload jig0037 jig0038)
		(in jig0038 beluga11)
		(next_unload jig0038 jig0039)
		(in jig0039 beluga11)
		(next_unload jig0039 dummy-jig)
		; Flight: beluga12
		; 0: jig0040
		(to_unload jig0040 beluga12)
		(in jig0040 beluga12)
		(next_unload jig0040 dummy-jig)
		; Flight: beluga13
		; 0: jig0041 1: jig0042 2: jig0043 3: jig0044
		(to_unload jig0041 beluga13)
		(in jig0041 beluga13)
		(next_unload jig0041 jig0042)
		(in jig0042 beluga13)
		(next_unload jig0042 jig0043)
		(in jig0043 beluga13)
		(next_unload jig0043 jig0044)
		(in jig0044 beluga13)
		(next_unload jig0044 dummy-jig)
		; Flight: beluga14
		; No jigs
		(to_unload dummy-jig beluga14)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0045 1: jig0046 2: jig0047 3: jig0048 4: jig0049 5: jig0050 6: jig0051 7: jig0052
		(to_unload jig0045 beluga16)
		(in jig0045 beluga16)
		(next_unload jig0045 jig0046)
		(in jig0046 beluga16)
		(next_unload jig0046 jig0047)
		(in jig0047 beluga16)
		(next_unload jig0047 jig0048)
		(in jig0048 beluga16)
		(next_unload jig0048 jig0049)
		(in jig0049 beluga16)
		(next_unload jig0049 jig0050)
		(in jig0050 beluga16)
		(next_unload jig0050 jig0051)
		(in jig0051 beluga16)
		(next_unload jig0051 jig0052)
		(in jig0052 beluga16)
		(next_unload jig0052 dummy-jig)
		; Flight: beluga17
		; 0: jig0053
		(to_unload jig0053 beluga17)
		(in jig0053 beluga17)
		(next_unload jig0053 dummy-jig)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeA) (1: typeA) (2: typeA)
		(to_load typeA slot0 beluga1)
		(next_load typeA slot0 slot1 beluga1)
		(next_load typeA slot1 slot2 beluga1)
		(next_load dummy-type slot2 dummy-slot beluga1)
		; To Process Flights
		; No jigs
		(to_load dummy-type dummy-slot beluga2)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga3)
		(next_load typeA slot0 slot1 beluga3)
		(next_load dummy-type slot1 dummy-slot beluga3)
		; 0: typeA
		(to_load typeA slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga5)
		(next_load typeB slot0 slot1 beluga5)
		(next_load dummy-type slot1 dummy-slot beluga5)
		; 0: typeD
		(to_load typeD slot0 beluga6)
		(next_load dummy-type slot0 dummy-slot beluga6)
		; 0: typeB
		(to_load typeB slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga8)
		(next_load typeA slot0 slot1 beluga8)
		(next_load typeA slot1 slot2 beluga8)
		(next_load typeA slot2 slot3 beluga8)
		(next_load dummy-type slot3 dummy-slot beluga8)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga9)
		(next_load typeA slot0 slot1 beluga9)
		(next_load dummy-type slot1 dummy-slot beluga9)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga10)
		(next_load typeA slot0 slot1 beluga10)
		(next_load typeA slot1 slot2 beluga10)
		(next_load typeA slot2 slot3 beluga10)
		(next_load dummy-type slot3 dummy-slot beluga10)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga11)
		(next_load typeA slot0 slot1 beluga11)
		(next_load typeA slot1 slot2 beluga11)
		(next_load dummy-type slot2 dummy-slot beluga11)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga12)
		(next_load typeA slot0 slot1 beluga12)
		(next_load typeA slot1 slot2 beluga12)
		(next_load typeA slot2 slot3 beluga12)
		(next_load dummy-type slot3 dummy-slot beluga12)
		; No jigs
		(to_load dummy-type dummy-slot beluga13)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga14)
		(next_load typeA slot0 slot1 beluga14)
		(next_load typeA slot1 slot2 beluga14)
		(next_load typeA slot2 slot3 beluga14)
		(next_load dummy-type slot3 dummy-slot beluga14)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga15)
		(next_load typeA slot0 slot1 beluga15)
		(next_load typeA slot1 slot2 beluga15)
		(next_load dummy-type slot2 dummy-slot beluga15)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga16)
		(next_load typeA slot0 slot1 beluga16)
		(next_load typeA slot1 slot2 beluga16)
		(next_load typeA slot2 slot3 beluga16)
		(next_load typeA slot3 slot4 beluga16)
		(next_load dummy-type slot4 dummy-slot beluga16)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga17)
		(next_load typeA slot0 slot1 beluga17)
		(next_load dummy-type slot1 dummy-slot beluga17)
		; Production schedule:
		; Production line: pl0
		; 0: jig0007 1: jig0010 2: jig0001 3: jig0004 4: jig0009 5: jig0002 6: jig0011 7: jig0008 8: jig0013 9: jig0012 10: jig0018 11: jig0017 12: jig0024 13: jig0014 14: jig0019 15: jig0023 16: jig0025 17: jig0016 18: jig0020 19: jig0021 20: jig0015 21: jig0028 22: jig0030 23: jig0033 24: jig0022 25: jig0027 26: jig0032 27: jig0038 28: jig0029 29: jig0034 30: jig0037 31: jig0026 32: jig0036 33: jig0041 34: jig0043 35: jig0044 36: jig0031 37: jig0039 38: jig0035 39: jig0042
		(to_deliver jig0007 pl0)
		(next_deliver jig0007 jig0010)
		(next_deliver jig0010 jig0001)
		(next_deliver jig0001 jig0004)
		(next_deliver jig0004 jig0009)
		(next_deliver jig0009 jig0002)
		(next_deliver jig0002 jig0011)
		(next_deliver jig0011 jig0008)
		(next_deliver jig0008 jig0013)
		(next_deliver jig0013 jig0012)
		(next_deliver jig0012 jig0018)
		(next_deliver jig0018 jig0017)
		(next_deliver jig0017 jig0024)
		(next_deliver jig0024 jig0014)
		(next_deliver jig0014 jig0019)
		(next_deliver jig0019 jig0023)
		(next_deliver jig0023 jig0025)
		(next_deliver jig0025 jig0016)
		(next_deliver jig0016 jig0020)
		(next_deliver jig0020 jig0021)
		(next_deliver jig0021 jig0015)
		(next_deliver jig0015 jig0028)
		(next_deliver jig0028 jig0030)
		(next_deliver jig0030 jig0033)
		(next_deliver jig0033 jig0022)
		(next_deliver jig0022 jig0027)
		(next_deliver jig0027 jig0032)
		(next_deliver jig0032 jig0038)
		(next_deliver jig0038 jig0029)
		(next_deliver jig0029 jig0034)
		(next_deliver jig0034 jig0037)
		(next_deliver jig0037 jig0026)
		(next_deliver jig0026 jig0036)
		(next_deliver jig0036 jig0041)
		(next_deliver jig0041 jig0043)
		(next_deliver jig0043 jig0044)
		(next_deliver jig0044 jig0031)
		(next_deliver jig0031 jig0039)
		(next_deliver jig0039 jig0035)
		(next_deliver jig0035 jig0042)
		(next_deliver jig0042 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0007)
		(empty jig0010)
		(empty jig0001)
		(empty jig0004)
		(empty jig0009)
		(empty jig0002)
		(empty jig0011)
		(empty jig0008)
		(empty jig0013)
		(empty jig0012)
		(empty jig0018)
		(empty jig0017)
		(empty jig0024)
		(empty jig0014)
		(empty jig0019)
		(empty jig0023)
		(empty jig0025)
		(empty jig0016)
		(empty jig0020)
		(empty jig0021)
		(empty jig0015)
		(empty jig0028)
		(empty jig0030)
		(empty jig0033)
		(empty jig0022)
		(empty jig0027)
		(empty jig0032)
		(empty jig0038)
		(empty jig0029)
		(empty jig0034)
		(empty jig0037)
		(empty jig0026)
		(empty jig0036)
		(empty jig0041)
		(empty jig0043)
		(empty jig0044)
		(empty jig0031)
		(empty jig0039)
		(empty jig0035)
		(empty jig0042)
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
	))
  (:metric minimize (total-cost))
)