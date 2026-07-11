(define
	(problem beluga-problem_25_s67_j69_r8_oc27_f43)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 34, 38}
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
		n29 - num
		n30 - num
		n32 - num
		n34 - num
		n38 - num
		; trailers:
		beluga_trailer_1 - trailer
		beluga_trailer_2 - trailer
		factory_trailer_1 - trailer
		; Racks:
		rack00 - rack
		rack01 - rack
		rack02 - rack
		rack03 - rack
		rack04 - rack
		rack05 - rack
		rack06 - rack
		rack07 - rack
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
		jig0056 - jig
		jig0057 - jig
		jig0058 - jig
		jig0059 - jig
		jig0060 - jig
		jig0061 - jig
		jig0062 - jig
		jig0063 - jig
		jig0064 - jig
		jig0065 - jig
		jig0066 - jig
		jig0067 - jig
		jig0068 - jig
		jig0069 - jig
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
		beluga35 - beluga
		beluga36 - beluga
		beluga37 - beluga
		beluga38 - beluga
		beluga39 - beluga
		beluga40 - beluga
		beluga41 - beluga
		beluga42 - beluga
		beluga43 - beluga
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
		(fit  n13  n04  n17 rack00)
		(fit  n09  n08  n17 rack00)
		(fit  n08  n09  n17 rack00)
		(fit  n06  n11  n17 rack00)
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
		(fit  n17  n04  n21 rack00)
		(fit  n13  n08  n21 rack00)
		(fit  n12  n09  n21 rack00)
		(fit  n10  n11  n21 rack00)
		(fit  n03  n18  n21 rack00)
		(fit  n19  n04  n23 rack00)
		(fit  n15  n08  n23 rack00)
		(fit  n14  n09  n23 rack00)
		(fit  n12  n11  n23 rack00)
		(fit  n05  n18  n23 rack00)
		(fit  n20  n04  n24 rack00)
		(fit  n16  n08  n24 rack00)
		(fit  n15  n09  n24 rack00)
		(fit  n13  n11  n24 rack00)
		(fit  n06  n18  n24 rack00)
		(fit  n24  n04  n28 rack00)
		(fit  n20  n08  n28 rack00)
		(fit  n19  n09  n28 rack00)
		(fit  n17  n11  n28 rack00)
		(fit  n10  n18  n28 rack00)
		(fit  n03  n25  n28 rack00)
		(fit  n00  n32  n32 rack00)
		(fit  n28  n04  n32 rack00)
		(fit  n24  n08  n32 rack00)
		(fit  n23  n09  n32 rack00)
		(fit  n21  n11  n32 rack00)
		(fit  n14  n18  n32 rack00)
		(fit  n07  n25  n32 rack00)
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
		; Sizes fitting rack: rack04
		(fit  n00  n04  n04 rack04)
		(fit  n01  n04  n05 rack04)
		(fit  n02  n04  n06 rack04)
		(fit  n03  n04  n07 rack04)
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
		(fit  n08  n04  n12 rack05)
		(fit  n04  n08  n12 rack05)
		(fit  n03  n09  n12 rack05)
		(fit  n01  n11  n12 rack05)
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
		(fit  n12  n04  n16 rack05)
		(fit  n08  n08  n16 rack05)
		(fit  n07  n09  n16 rack05)
		(fit  n05  n11  n16 rack05)
		(fit  n13  n04  n17 rack05)
		(fit  n09  n08  n17 rack05)
		(fit  n08  n09  n17 rack05)
		(fit  n06  n11  n17 rack05)
		(fit  n14  n04  n18 rack05)
		(fit  n10  n08  n18 rack05)
		(fit  n09  n09  n18 rack05)
		(fit  n07  n11  n18 rack05)
		(fit  n00  n18  n18 rack05)
		(fit  n15  n04  n19 rack05)
		(fit  n11  n08  n19 rack05)
		(fit  n10  n09  n19 rack05)
		(fit  n08  n11  n19 rack05)
		(fit  n01  n18  n19 rack05)
		(fit  n16  n04  n20 rack05)
		(fit  n12  n08  n20 rack05)
		(fit  n11  n09  n20 rack05)
		(fit  n09  n11  n20 rack05)
		(fit  n02  n18  n20 rack05)
		(fit  n17  n04  n21 rack05)
		(fit  n13  n08  n21 rack05)
		(fit  n12  n09  n21 rack05)
		(fit  n10  n11  n21 rack05)
		(fit  n03  n18  n21 rack05)
		(fit  n18  n04  n22 rack05)
		(fit  n14  n08  n22 rack05)
		(fit  n13  n09  n22 rack05)
		(fit  n11  n11  n22 rack05)
		(fit  n04  n18  n22 rack05)
		(fit  n19  n04  n23 rack05)
		(fit  n15  n08  n23 rack05)
		(fit  n14  n09  n23 rack05)
		(fit  n12  n11  n23 rack05)
		(fit  n05  n18  n23 rack05)
		(fit  n21  n04  n25 rack05)
		(fit  n17  n08  n25 rack05)
		(fit  n16  n09  n25 rack05)
		(fit  n14  n11  n25 rack05)
		(fit  n07  n18  n25 rack05)
		(fit  n00  n25  n25 rack05)
		(fit  n22  n04  n26 rack05)
		(fit  n18  n08  n26 rack05)
		(fit  n17  n09  n26 rack05)
		(fit  n15  n11  n26 rack05)
		(fit  n08  n18  n26 rack05)
		(fit  n01  n25  n26 rack05)
		(fit  n23  n04  n27 rack05)
		(fit  n19  n08  n27 rack05)
		(fit  n18  n09  n27 rack05)
		(fit  n16  n11  n27 rack05)
		(fit  n09  n18  n27 rack05)
		(fit  n02  n25  n27 rack05)
		(fit  n25  n04  n29 rack05)
		(fit  n21  n08  n29 rack05)
		(fit  n20  n09  n29 rack05)
		(fit  n18  n11  n29 rack05)
		(fit  n11  n18  n29 rack05)
		(fit  n04  n25  n29 rack05)
		(fit  n26  n04  n30 rack05)
		(fit  n22  n08  n30 rack05)
		(fit  n21  n09  n30 rack05)
		(fit  n19  n11  n30 rack05)
		(fit  n12  n18  n30 rack05)
		(fit  n05  n25  n30 rack05)
		(fit  n02  n32  n34 rack05)
		(fit  n30  n04  n34 rack05)
		(fit  n26  n08  n34 rack05)
		(fit  n25  n09  n34 rack05)
		(fit  n23  n11  n34 rack05)
		(fit  n16  n18  n34 rack05)
		(fit  n09  n25  n34 rack05)
		(fit  n06  n32  n38 rack05)
		(fit  n34  n04  n38 rack05)
		(fit  n30  n08  n38 rack05)
		(fit  n29  n09  n38 rack05)
		(fit  n27  n11  n38 rack05)
		(fit  n20  n18  n38 rack05)
		(fit  n13  n25  n38 rack05)
		; Sizes fitting rack: rack06
		(fit  n00  n04  n04 rack06)
		(fit  n01  n04  n05 rack06)
		(fit  n02  n04  n06 rack06)
		(fit  n03  n04  n07 rack06)
		(fit  n04  n04  n08 rack06)
		(fit  n00  n08  n08 rack06)
		(fit  n05  n04  n09 rack06)
		(fit  n01  n08  n09 rack06)
		(fit  n00  n09  n09 rack06)
		(fit  n07  n04  n11 rack06)
		(fit  n03  n08  n11 rack06)
		(fit  n02  n09  n11 rack06)
		(fit  n00  n11  n11 rack06)
		(fit  n08  n04  n12 rack06)
		(fit  n04  n08  n12 rack06)
		(fit  n03  n09  n12 rack06)
		(fit  n01  n11  n12 rack06)
		(fit  n09  n04  n13 rack06)
		(fit  n05  n08  n13 rack06)
		(fit  n04  n09  n13 rack06)
		(fit  n02  n11  n13 rack06)
		(fit  n11  n04  n15 rack06)
		(fit  n07  n08  n15 rack06)
		(fit  n06  n09  n15 rack06)
		(fit  n04  n11  n15 rack06)
		(fit  n12  n04  n16 rack06)
		(fit  n08  n08  n16 rack06)
		(fit  n07  n09  n16 rack06)
		(fit  n05  n11  n16 rack06)
		(fit  n16  n04  n20 rack06)
		(fit  n12  n08  n20 rack06)
		(fit  n11  n09  n20 rack06)
		(fit  n09  n11  n20 rack06)
		(fit  n02  n18  n20 rack06)
		(fit  n20  n04  n24 rack06)
		(fit  n16  n08  n24 rack06)
		(fit  n15  n09  n24 rack06)
		(fit  n13  n11  n24 rack06)
		(fit  n06  n18  n24 rack06)
		; Sizes fitting rack: rack07
		(fit  n00  n04  n04 rack07)
		(fit  n01  n04  n05 rack07)
		(fit  n03  n04  n07 rack07)
		(fit  n04  n04  n08 rack07)
		(fit  n00  n08  n08 rack07)
		(fit  n05  n04  n09 rack07)
		(fit  n01  n08  n09 rack07)
		(fit  n00  n09  n09 rack07)
		(fit  n07  n04  n11 rack07)
		(fit  n03  n08  n11 rack07)
		(fit  n02  n09  n11 rack07)
		(fit  n00  n11  n11 rack07)
		(fit  n08  n04  n12 rack07)
		(fit  n04  n08  n12 rack07)
		(fit  n03  n09  n12 rack07)
		(fit  n01  n11  n12 rack07)
		(fit  n12  n04  n16 rack07)
		(fit  n08  n08  n16 rack07)
		(fit  n07  n09  n16 rack07)
		(fit  n05  n11  n16 rack07)
		(fit  n16  n04  n20 rack07)
		(fit  n12  n08  n20 rack07)
		(fit  n11  n09  n20 rack07)
		(fit  n09  n11  n20 rack07)
		(fit  n02  n18  n20 rack07)
		; trailers (Beluga side):
		(empty beluga_trailer_1)
		(at-side beluga_trailer_1 bside)
		(empty beluga_trailer_2)
		(at-side beluga_trailer_2 bside)
		; trailers (Factory side):
		(empty factory_trailer_1)
		(at-side factory_trailer_1 fside)
		; Racks 8
		; Rack:rack00
		(empty rack00)
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n32)
		; Rack:rack01
		(empty rack01)
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n29)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n07)
		(in jig0002 rack02)
		(clear jig0002 bside)
		(next-to jig0002 jig0003 bside)
		(next-to jig0003 jig0002 fside)
		(in jig0003 rack02)
		(clear jig0003 fside)
		; Rack:rack03
		(empty rack03)
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n27)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n04)
		(in jig0004 rack04)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack05
		(at-side rack05 bside)
		(at-side rack05 fside)
		(free-space rack05 n13)
		(in jig0001 rack05)
		(clear jig0001 bside)
		(clear jig0001 fside)
		; Rack:rack06
		(empty rack06)
		(at-side rack06 bside)
		(at-side rack06 fside)
		(free-space rack06 n24)
		; Rack:rack07
		(empty rack07)
		(at-side rack07 bside)
		(at-side rack07 fside)
		(free-space rack07 n20)
		; Jigs (size):
		(is_type jig0001 typeD)
		(size jig0001 n25)
		(empty-size jig0001 n18)
		(is_type jig0002 typeB)
		(size jig0002 n08)
		(empty-size jig0002 n08)
		(empty jig0002)
		(is_type jig0003 typeB)
		(size jig0003 n11)
		(empty-size jig0003 n08)
		(is_type jig0004 typeD)
		(size jig0004 n18)
		(empty-size jig0004 n18)
		(empty jig0004)
		(is_type jig0005 typeD)
		(size jig0005 n25)
		(empty-size jig0005 n18)
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
		(is_type jig0011 typeD)
		(size jig0011 n25)
		(empty-size jig0011 n18)
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
		(is_type jig0022 typeC)
		(size jig0022 n18)
		(empty-size jig0022 n09)
		(is_type jig0023 typeC)
		(size jig0023 n18)
		(empty-size jig0023 n09)
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
		(is_type jig0028 typeB)
		(size jig0028 n11)
		(empty-size jig0028 n08)
		(is_type jig0029 typeB)
		(size jig0029 n11)
		(empty-size jig0029 n08)
		(is_type jig0030 typeB)
		(size jig0030 n11)
		(empty-size jig0030 n08)
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
		(is_type jig0041 typeC)
		(size jig0041 n18)
		(empty-size jig0041 n09)
		(is_type jig0042 typeB)
		(size jig0042 n11)
		(empty-size jig0042 n08)
		(is_type jig0043 typeB)
		(size jig0043 n11)
		(empty-size jig0043 n08)
		(is_type jig0044 typeB)
		(size jig0044 n11)
		(empty-size jig0044 n08)
		(is_type jig0045 typeD)
		(size jig0045 n25)
		(empty-size jig0045 n18)
		(is_type jig0046 typeC)
		(size jig0046 n18)
		(empty-size jig0046 n09)
		(is_type jig0047 typeC)
		(size jig0047 n18)
		(empty-size jig0047 n09)
		(is_type jig0048 typeB)
		(size jig0048 n11)
		(empty-size jig0048 n08)
		(is_type jig0049 typeB)
		(size jig0049 n11)
		(empty-size jig0049 n08)
		(is_type jig0050 typeB)
		(size jig0050 n11)
		(empty-size jig0050 n08)
		(is_type jig0051 typeA)
		(size jig0051 n04)
		(empty-size jig0051 n04)
		(is_type jig0052 typeA)
		(size jig0052 n04)
		(empty-size jig0052 n04)
		(is_type jig0053 typeA)
		(size jig0053 n04)
		(empty-size jig0053 n04)
		(is_type jig0054 typeA)
		(size jig0054 n04)
		(empty-size jig0054 n04)
		(is_type jig0055 typeA)
		(size jig0055 n04)
		(empty-size jig0055 n04)
		(is_type jig0056 typeA)
		(size jig0056 n04)
		(empty-size jig0056 n04)
		(is_type jig0057 typeA)
		(size jig0057 n04)
		(empty-size jig0057 n04)
		(is_type jig0058 typeA)
		(size jig0058 n04)
		(empty-size jig0058 n04)
		(is_type jig0059 typeA)
		(size jig0059 n04)
		(empty-size jig0059 n04)
		(is_type jig0060 typeA)
		(size jig0060 n04)
		(empty-size jig0060 n04)
		(is_type jig0061 typeC)
		(size jig0061 n18)
		(empty-size jig0061 n09)
		(is_type jig0062 typeC)
		(size jig0062 n18)
		(empty-size jig0062 n09)
		(is_type jig0063 typeC)
		(size jig0063 n18)
		(empty-size jig0063 n09)
		(is_type jig0064 typeC)
		(size jig0064 n18)
		(empty-size jig0064 n09)
		(is_type jig0065 typeC)
		(size jig0065 n18)
		(empty-size jig0065 n09)
		(is_type jig0066 typeB)
		(size jig0066 n11)
		(empty-size jig0066 n08)
		(is_type jig0067 typeC)
		(size jig0067 n18)
		(empty-size jig0067 n09)
		(is_type jig0068 typeC)
		(size jig0068 n18)
		(empty-size jig0068 n09)
		(is_type jig0069 typeC)
		(size jig0069 n18)
		(empty-size jig0069 n09)
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
		(next-flight-to-process beluga34 beluga35)
		(next-flight-to-process beluga35 beluga36)
		(next-flight-to-process beluga36 beluga37)
		(next-flight-to-process beluga37 beluga38)
		(next-flight-to-process beluga38 beluga39)
		(next-flight-to-process beluga39 beluga40)
		(next-flight-to-process beluga40 beluga41)
		(next-flight-to-process beluga41 beluga42)
		(next-flight-to-process beluga42 beluga43)
		; Number of flights: 43
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0005
		(to_unload jig0005 beluga1)
		(in jig0005 beluga1)
		(next_unload jig0005 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0006 1: jig0007
		(to_unload jig0006 beluga2)
		(in jig0006 beluga2)
		(next_unload jig0006 jig0007)
		(in jig0007 beluga2)
		(next_unload jig0007 dummy-jig)
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
		; No jigs
		(to_unload dummy-jig beluga5)
		; Flight: beluga6
		; 0: jig0012 1: jig0013 2: jig0014 3: jig0015 4: jig0016 5: jig0017 6: jig0018 7: jig0019 8: jig0020 9: jig0021
		(to_unload jig0012 beluga6)
		(in jig0012 beluga6)
		(next_unload jig0012 jig0013)
		(in jig0013 beluga6)
		(next_unload jig0013 jig0014)
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
		(next_unload jig0020 jig0021)
		(in jig0021 beluga6)
		(next_unload jig0021 dummy-jig)
		; Flight: beluga7
		; 0: jig0022 1: jig0023
		(to_unload jig0022 beluga7)
		(in jig0022 beluga7)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga7)
		(next_unload jig0023 dummy-jig)
		; Flight: beluga8
		; No jigs
		(to_unload dummy-jig beluga8)
		; Flight: beluga9
		; No jigs
		(to_unload dummy-jig beluga9)
		; Flight: beluga10
		; 0: jig0024 1: jig0025 2: jig0026
		(to_unload jig0024 beluga10)
		(in jig0024 beluga10)
		(next_unload jig0024 jig0025)
		(in jig0025 beluga10)
		(next_unload jig0025 jig0026)
		(in jig0026 beluga10)
		(next_unload jig0026 dummy-jig)
		; Flight: beluga11
		; 0: jig0027
		(to_unload jig0027 beluga11)
		(in jig0027 beluga11)
		(next_unload jig0027 dummy-jig)
		; Flight: beluga12
		; No jigs
		(to_unload dummy-jig beluga12)
		; Flight: beluga13
		; 0: jig0028 1: jig0029 2: jig0030
		(to_unload jig0028 beluga13)
		(in jig0028 beluga13)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga13)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga13)
		(next_unload jig0030 dummy-jig)
		; Flight: beluga14
		; 0: jig0031 1: jig0032 2: jig0033 3: jig0034 4: jig0035 5: jig0036 6: jig0037 7: jig0038 8: jig0039 9: jig0040
		(to_unload jig0031 beluga14)
		(in jig0031 beluga14)
		(next_unload jig0031 jig0032)
		(in jig0032 beluga14)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga14)
		(next_unload jig0033 jig0034)
		(in jig0034 beluga14)
		(next_unload jig0034 jig0035)
		(in jig0035 beluga14)
		(next_unload jig0035 jig0036)
		(in jig0036 beluga14)
		(next_unload jig0036 jig0037)
		(in jig0037 beluga14)
		(next_unload jig0037 jig0038)
		(in jig0038 beluga14)
		(next_unload jig0038 jig0039)
		(in jig0039 beluga14)
		(next_unload jig0039 jig0040)
		(in jig0040 beluga14)
		(next_unload jig0040 dummy-jig)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0041
		(to_unload jig0041 beluga16)
		(in jig0041 beluga16)
		(next_unload jig0041 dummy-jig)
		; Flight: beluga17
		; No jigs
		(to_unload dummy-jig beluga17)
		; Flight: beluga18
		; No jigs
		(to_unload dummy-jig beluga18)
		; Flight: beluga19
		; 0: jig0042 1: jig0043 2: jig0044
		(to_unload jig0042 beluga19)
		(in jig0042 beluga19)
		(next_unload jig0042 jig0043)
		(in jig0043 beluga19)
		(next_unload jig0043 jig0044)
		(in jig0044 beluga19)
		(next_unload jig0044 dummy-jig)
		; Flight: beluga20
		; No jigs
		(to_unload dummy-jig beluga20)
		; Flight: beluga21
		; No jigs
		(to_unload dummy-jig beluga21)
		; Flight: beluga22
		; 0: jig0045
		(to_unload jig0045 beluga22)
		(in jig0045 beluga22)
		(next_unload jig0045 dummy-jig)
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
		; No jigs
		(to_unload dummy-jig beluga26)
		; Flight: beluga27
		; 0: jig0046 1: jig0047
		(to_unload jig0046 beluga27)
		(in jig0046 beluga27)
		(next_unload jig0046 jig0047)
		(in jig0047 beluga27)
		(next_unload jig0047 dummy-jig)
		; Flight: beluga28
		; No jigs
		(to_unload dummy-jig beluga28)
		; Flight: beluga29
		; 0: jig0048 1: jig0049 2: jig0050
		(to_unload jig0048 beluga29)
		(in jig0048 beluga29)
		(next_unload jig0048 jig0049)
		(in jig0049 beluga29)
		(next_unload jig0049 jig0050)
		(in jig0050 beluga29)
		(next_unload jig0050 dummy-jig)
		; Flight: beluga30
		; 0: jig0051 1: jig0052 2: jig0053 3: jig0054 4: jig0055 5: jig0056 6: jig0057 7: jig0058 8: jig0059 9: jig0060
		(to_unload jig0051 beluga30)
		(in jig0051 beluga30)
		(next_unload jig0051 jig0052)
		(in jig0052 beluga30)
		(next_unload jig0052 jig0053)
		(in jig0053 beluga30)
		(next_unload jig0053 jig0054)
		(in jig0054 beluga30)
		(next_unload jig0054 jig0055)
		(in jig0055 beluga30)
		(next_unload jig0055 jig0056)
		(in jig0056 beluga30)
		(next_unload jig0056 jig0057)
		(in jig0057 beluga30)
		(next_unload jig0057 jig0058)
		(in jig0058 beluga30)
		(next_unload jig0058 jig0059)
		(in jig0059 beluga30)
		(next_unload jig0059 jig0060)
		(in jig0060 beluga30)
		(next_unload jig0060 dummy-jig)
		; Flight: beluga31
		; 0: jig0061 1: jig0062
		(to_unload jig0061 beluga31)
		(in jig0061 beluga31)
		(next_unload jig0061 jig0062)
		(in jig0062 beluga31)
		(next_unload jig0062 dummy-jig)
		; Flight: beluga32
		; No jigs
		(to_unload dummy-jig beluga32)
		; Flight: beluga33
		; 0: jig0063
		(to_unload jig0063 beluga33)
		(in jig0063 beluga33)
		(next_unload jig0063 dummy-jig)
		; Flight: beluga34
		; 0: jig0064 1: jig0065
		(to_unload jig0064 beluga34)
		(in jig0064 beluga34)
		(next_unload jig0064 jig0065)
		(in jig0065 beluga34)
		(next_unload jig0065 dummy-jig)
		; Flight: beluga35
		; No jigs
		(to_unload dummy-jig beluga35)
		; Flight: beluga36
		; No jigs
		(to_unload dummy-jig beluga36)
		; Flight: beluga37
		; 0: jig0066
		(to_unload jig0066 beluga37)
		(in jig0066 beluga37)
		(next_unload jig0066 dummy-jig)
		; Flight: beluga38
		; No jigs
		(to_unload dummy-jig beluga38)
		; Flight: beluga39
		; No jigs
		(to_unload dummy-jig beluga39)
		; Flight: beluga40
		; 0: jig0067 1: jig0068
		(to_unload jig0067 beluga40)
		(in jig0067 beluga40)
		(next_unload jig0067 jig0068)
		(in jig0068 beluga40)
		(next_unload jig0068 dummy-jig)
		; Flight: beluga41
		; 0: jig0069
		(to_unload jig0069 beluga41)
		(in jig0069 beluga41)
		(next_unload jig0069 dummy-jig)
		; Flight: beluga42
		; No jigs
		(to_unload dummy-jig beluga42)
		; Flight: beluga43
		; No jigs
		(to_unload dummy-jig beluga43)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeB)
		(to_load typeB slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; 0: typeD
		(to_load typeD slot0 beluga2)
		(next_load dummy-type slot0 dummy-slot beluga2)
		; No jigs
		(to_load dummy-type dummy-slot beluga3)
		; No jigs
		(to_load dummy-type dummy-slot beluga4)
		; 0: typeD
		(to_load typeD slot0 beluga5)
		(next_load dummy-type slot0 dummy-slot beluga5)
		; No jigs
		(to_load dummy-type dummy-slot beluga6)
		; No jigs
		(to_load dummy-type dummy-slot beluga7)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga8)
		(next_load typeB slot0 slot1 beluga8)
		(next_load dummy-type slot1 dummy-slot beluga8)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga9)
		(next_load typeC slot0 slot1 beluga9)
		(next_load dummy-type slot1 dummy-slot beluga9)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga10)
		(next_load typeA slot0 slot1 beluga10)
		(next_load typeA slot1 slot2 beluga10)
		(next_load dummy-type slot2 dummy-slot beluga10)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga11)
		(next_load typeB slot0 slot1 beluga11)
		(next_load dummy-type slot1 dummy-slot beluga11)
		; 0: typeC
		(to_load typeC slot0 beluga12)
		(next_load dummy-type slot0 dummy-slot beluga12)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga13)
		(next_load typeA slot0 slot1 beluga13)
		(next_load typeA slot1 slot2 beluga13)
		(next_load dummy-type slot2 dummy-slot beluga13)
		; 0: typeA
		(to_load typeA slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeD
		(to_load typeD slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga16)
		(next_load typeA slot0 slot1 beluga16)
		(next_load dummy-type slot1 dummy-slot beluga16)
		; 0: typeA
		(to_load typeA slot0 beluga17)
		(next_load dummy-type slot0 dummy-slot beluga17)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga18)
		(next_load typeB slot0 slot1 beluga18)
		(next_load typeB slot1 slot2 beluga18)
		(next_load dummy-type slot2 dummy-slot beluga18)
		; 0: typeB
		(to_load typeB slot0 beluga19)
		(next_load dummy-type slot0 dummy-slot beluga19)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga20)
		(next_load typeA slot0 slot1 beluga20)
		(next_load dummy-type slot1 dummy-slot beluga20)
		; 0: typeD
		(to_load typeD slot0 beluga21)
		(next_load dummy-type slot0 dummy-slot beluga21)
		; 0: typeB
		(to_load typeB slot0 beluga22)
		(next_load dummy-type slot0 dummy-slot beluga22)
		; 0: typeC
		(to_load typeC slot0 beluga23)
		(next_load dummy-type slot0 dummy-slot beluga23)
		; 0: typeA
		(to_load typeA slot0 beluga24)
		(next_load dummy-type slot0 dummy-slot beluga24)
		; 0: typeC
		(to_load typeC slot0 beluga25)
		(next_load dummy-type slot0 dummy-slot beluga25)
		; 0: typeB
		(to_load typeB slot0 beluga26)
		(next_load dummy-type slot0 dummy-slot beluga26)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga27)
		(next_load typeA slot0 slot1 beluga27)
		(next_load typeA slot1 slot2 beluga27)
		(next_load dummy-type slot2 dummy-slot beluga27)
		; 0: typeA
		(to_load typeA slot0 beluga28)
		(next_load dummy-type slot0 dummy-slot beluga28)
		; 0: typeD
		(to_load typeD slot0 beluga29)
		(next_load dummy-type slot0 dummy-slot beluga29)
		; 0: typeA
		(to_load typeA slot0 beluga30)
		(next_load dummy-type slot0 dummy-slot beluga30)
		; 0: typeC
		(to_load typeC slot0 beluga31)
		(next_load dummy-type slot0 dummy-slot beluga31)
		; 0: typeA
		(to_load typeA slot0 beluga32)
		(next_load dummy-type slot0 dummy-slot beluga32)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga33)
		(next_load typeB slot0 slot1 beluga33)
		(next_load typeB slot1 slot2 beluga33)
		(next_load dummy-type slot2 dummy-slot beluga33)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga34)
		(next_load typeA slot0 slot1 beluga34)
		(next_load typeA slot1 slot2 beluga34)
		(next_load dummy-type slot2 dummy-slot beluga34)
		; 0: typeA
		(to_load typeA slot0 beluga35)
		(next_load dummy-type slot0 dummy-slot beluga35)
		; 0: typeB
		(to_load typeB slot0 beluga36)
		(next_load dummy-type slot0 dummy-slot beluga36)
		; 0: typeC
		(to_load typeC slot0 beluga37)
		(next_load dummy-type slot0 dummy-slot beluga37)
		; 0: typeC
		(to_load typeC slot0 beluga38)
		(next_load dummy-type slot0 dummy-slot beluga38)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga39)
		(next_load typeA slot0 slot1 beluga39)
		(next_load typeA slot1 slot2 beluga39)
		(next_load dummy-type slot2 dummy-slot beluga39)
		; 0: typeB
		(to_load typeB slot0 beluga40)
		(next_load dummy-type slot0 dummy-slot beluga40)
		; 0: typeA
		(to_load typeA slot0 beluga41)
		(next_load dummy-type slot0 dummy-slot beluga41)
		; 0: typeC
		(to_load typeC slot0 beluga42)
		(next_load dummy-type slot0 dummy-slot beluga42)
		; 0: typeB
		(to_load typeB slot0 beluga43)
		(next_load dummy-type slot0 dummy-slot beluga43)
		; Production schedule:
		; Production line: pl0
		; 0: jig0003 1: jig0006 2: jig0022 3: jig0021 4: jig0010 5: jig0012 6: jig0017 7: jig0001 8: jig0024 9: jig0037 10: jig0011 11: jig0014 12: jig0028 13: jig0019 14: jig0041 15: jig0026 16: jig0039 17: jig0045 18: jig0027 19: jig0049 20: jig0042 21: jig0058 22: jig0059 23: jig0060 24: jig0064 25: jig0051 26: jig0055 27: jig0066 28: jig0057
		(to_deliver jig0003 pl0)
		(next_deliver jig0003 jig0006)
		(next_deliver jig0006 jig0022)
		(next_deliver jig0022 jig0021)
		(next_deliver jig0021 jig0010)
		(next_deliver jig0010 jig0012)
		(next_deliver jig0012 jig0017)
		(next_deliver jig0017 jig0001)
		(next_deliver jig0001 jig0024)
		(next_deliver jig0024 jig0037)
		(next_deliver jig0037 jig0011)
		(next_deliver jig0011 jig0014)
		(next_deliver jig0014 jig0028)
		(next_deliver jig0028 jig0019)
		(next_deliver jig0019 jig0041)
		(next_deliver jig0041 jig0026)
		(next_deliver jig0026 jig0039)
		(next_deliver jig0039 jig0045)
		(next_deliver jig0045 jig0027)
		(next_deliver jig0027 jig0049)
		(next_deliver jig0049 jig0042)
		(next_deliver jig0042 jig0058)
		(next_deliver jig0058 jig0059)
		(next_deliver jig0059 jig0060)
		(next_deliver jig0060 jig0064)
		(next_deliver jig0064 jig0051)
		(next_deliver jig0051 jig0055)
		(next_deliver jig0055 jig0066)
		(next_deliver jig0066 jig0057)
		(next_deliver jig0057 dummy-jig)
		; Production line: pl1
		; 0: jig0005 1: jig0008 2: jig0020 3: jig0018 4: jig0009 5: jig0023 6: jig0013 7: jig0016 8: jig0025 9: jig0030 10: jig0040 11: jig0038 12: jig0007 13: jig0035 14: jig0029 15: jig0015 16: jig0032 17: jig0036 18: jig0033 19: jig0043 20: jig0031 21: jig0052 22: jig0050 23: jig0034 24: jig0054 25: jig0046 26: jig0044 27: jig0061 28: jig0056
		(to_deliver jig0005 pl1)
		(next_deliver jig0005 jig0008)
		(next_deliver jig0008 jig0020)
		(next_deliver jig0020 jig0018)
		(next_deliver jig0018 jig0009)
		(next_deliver jig0009 jig0023)
		(next_deliver jig0023 jig0013)
		(next_deliver jig0013 jig0016)
		(next_deliver jig0016 jig0025)
		(next_deliver jig0025 jig0030)
		(next_deliver jig0030 jig0040)
		(next_deliver jig0040 jig0038)
		(next_deliver jig0038 jig0007)
		(next_deliver jig0007 jig0035)
		(next_deliver jig0035 jig0029)
		(next_deliver jig0029 jig0015)
		(next_deliver jig0015 jig0032)
		(next_deliver jig0032 jig0036)
		(next_deliver jig0036 jig0033)
		(next_deliver jig0033 jig0043)
		(next_deliver jig0043 jig0031)
		(next_deliver jig0031 jig0052)
		(next_deliver jig0052 jig0050)
		(next_deliver jig0050 jig0034)
		(next_deliver jig0034 jig0054)
		(next_deliver jig0054 jig0046)
		(next_deliver jig0046 jig0044)
		(next_deliver jig0044 jig0061)
		(next_deliver jig0061 jig0056)
		(next_deliver jig0056 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0003)
		(empty jig0006)
		(empty jig0022)
		(empty jig0021)
		(empty jig0010)
		(empty jig0012)
		(empty jig0017)
		(empty jig0001)
		(empty jig0024)
		(empty jig0037)
		(empty jig0011)
		(empty jig0014)
		(empty jig0028)
		(empty jig0019)
		(empty jig0041)
		(empty jig0026)
		(empty jig0039)
		(empty jig0045)
		(empty jig0027)
		(empty jig0049)
		(empty jig0042)
		(empty jig0058)
		(empty jig0059)
		(empty jig0060)
		(empty jig0064)
		(empty jig0051)
		(empty jig0055)
		(empty jig0066)
		(empty jig0057)
		(empty jig0005)
		(empty jig0008)
		(empty jig0020)
		(empty jig0018)
		(empty jig0009)
		(empty jig0023)
		(empty jig0013)
		(empty jig0016)
		(empty jig0025)
		(empty jig0030)
		(empty jig0040)
		(empty jig0038)
		(empty jig0007)
		(empty jig0035)
		(empty jig0029)
		(empty jig0015)
		(empty jig0032)
		(empty jig0036)
		(empty jig0033)
		(empty jig0043)
		(empty jig0031)
		(empty jig0052)
		(empty jig0050)
		(empty jig0034)
		(empty jig0054)
		(empty jig0046)
		(empty jig0044)
		(empty jig0061)
		(empty jig0056)
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
		(to_unload dummy-jig beluga35)
		(to_unload dummy-jig beluga36)
		(to_unload dummy-jig beluga37)
		(to_unload dummy-jig beluga38)
		(to_unload dummy-jig beluga39)
		(to_unload dummy-jig beluga40)
		(to_unload dummy-jig beluga41)
		(to_unload dummy-jig beluga42)
		(to_unload dummy-jig beluga43)
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
		(to_load dummy-type dummy-slot beluga35)
		(to_load dummy-type dummy-slot beluga36)
		(to_load dummy-type dummy-slot beluga37)
		(to_load dummy-type dummy-slot beluga38)
		(to_load dummy-type dummy-slot beluga39)
		(to_load dummy-type dummy-slot beluga40)
		(to_load dummy-type dummy-slot beluga41)
		(to_load dummy-type dummy-slot beluga42)
		(to_load dummy-type dummy-slot beluga43)
	))
  (:metric minimize (total-cost))
)