(define
	(problem beluga-problem_102_s144_j92_r11_oc84_f58)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 35, 36, 39}
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
		n35 - num
		n36 - num
		n39 - num
		; trailers:
		beluga_trailer_1 - trailer
		beluga_trailer_2 - trailer
		beluga_trailer_3 - trailer
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
		rack08 - rack
		rack09 - rack
		rack10 - rack
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
		jig0070 - jig
		jig0071 - jig
		jig0072 - jig
		jig0073 - jig
		jig0074 - jig
		jig0075 - jig
		jig0076 - jig
		jig0077 - jig
		jig0078 - jig
		jig0079 - jig
		jig0080 - jig
		jig0081 - jig
		jig0082 - jig
		jig0083 - jig
		jig0084 - jig
		jig0085 - jig
		jig0086 - jig
		jig0087 - jig
		jig0088 - jig
		jig0089 - jig
		jig0090 - jig
		jig0091 - jig
		jig0092 - jig
		typeE - type
		typeD - type
		typeC - type
		typeB - type
		typeA - type
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
		beluga44 - beluga
		beluga45 - beluga
		beluga46 - beluga
		beluga47 - beluga
		beluga48 - beluga
		beluga49 - beluga
		beluga50 - beluga
		beluga51 - beluga
		beluga52 - beluga
		beluga53 - beluga
		beluga54 - beluga
		beluga55 - beluga
		beluga56 - beluga
		beluga57 - beluga
		beluga58 - beluga
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
		(fit  n06  n04  n10 rack00)
		(fit  n02  n08  n10 rack00)
		(fit  n01  n09  n10 rack00)
		(fit  n07  n04  n11 rack00)
		(fit  n03  n08  n11 rack00)
		(fit  n02  n09  n11 rack00)
		(fit  n00  n11  n11 rack00)
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
		; Sizes fitting rack: rack01
		(fit  n00  n04  n04 rack01)
		(fit  n01  n04  n05 rack01)
		(fit  n02  n04  n06 rack01)
		(fit  n04  n04  n08 rack01)
		(fit  n00  n08  n08 rack01)
		(fit  n05  n04  n09 rack01)
		(fit  n01  n08  n09 rack01)
		(fit  n00  n09  n09 rack01)
		(fit  n06  n04  n10 rack01)
		(fit  n02  n08  n10 rack01)
		(fit  n01  n09  n10 rack01)
		(fit  n08  n04  n12 rack01)
		(fit  n04  n08  n12 rack01)
		(fit  n03  n09  n12 rack01)
		(fit  n01  n11  n12 rack01)
		(fit  n09  n04  n13 rack01)
		(fit  n05  n08  n13 rack01)
		(fit  n04  n09  n13 rack01)
		(fit  n02  n11  n13 rack01)
		(fit  n13  n04  n17 rack01)
		(fit  n09  n08  n17 rack01)
		(fit  n08  n09  n17 rack01)
		(fit  n06  n11  n17 rack01)
		(fit  n17  n04  n21 rack01)
		(fit  n13  n08  n21 rack01)
		(fit  n12  n09  n21 rack01)
		(fit  n10  n11  n21 rack01)
		(fit  n03  n18  n21 rack01)
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
		(fit  n18  n04  n22 rack02)
		(fit  n14  n08  n22 rack02)
		(fit  n13  n09  n22 rack02)
		(fit  n11  n11  n22 rack02)
		(fit  n04  n18  n22 rack02)
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
		(fit  n22  n04  n26 rack02)
		(fit  n18  n08  n26 rack02)
		(fit  n17  n09  n26 rack02)
		(fit  n15  n11  n26 rack02)
		(fit  n08  n18  n26 rack02)
		(fit  n01  n25  n26 rack02)
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
		(fit  n26  n04  n30 rack02)
		(fit  n22  n08  n30 rack02)
		(fit  n21  n09  n30 rack02)
		(fit  n19  n11  n30 rack02)
		(fit  n12  n18  n30 rack02)
		(fit  n05  n25  n30 rack02)
		(fit  n27  n04  n31 rack02)
		(fit  n23  n08  n31 rack02)
		(fit  n22  n09  n31 rack02)
		(fit  n20  n11  n31 rack02)
		(fit  n13  n18  n31 rack02)
		(fit  n06  n25  n31 rack02)
		(fit  n03  n32  n35 rack02)
		(fit  n31  n04  n35 rack02)
		(fit  n27  n08  n35 rack02)
		(fit  n26  n09  n35 rack02)
		(fit  n24  n11  n35 rack02)
		(fit  n17  n18  n35 rack02)
		(fit  n10  n25  n35 rack02)
		(fit  n07  n32  n39 rack02)
		(fit  n35  n04  n39 rack02)
		(fit  n31  n08  n39 rack02)
		(fit  n30  n09  n39 rack02)
		(fit  n28  n11  n39 rack02)
		(fit  n21  n18  n39 rack02)
		(fit  n14  n25  n39 rack02)
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
		(fit  n19  n04  n23 rack03)
		(fit  n15  n08  n23 rack03)
		(fit  n14  n09  n23 rack03)
		(fit  n12  n11  n23 rack03)
		(fit  n05  n18  n23 rack03)
		(fit  n20  n04  n24 rack03)
		(fit  n16  n08  n24 rack03)
		(fit  n15  n09  n24 rack03)
		(fit  n13  n11  n24 rack03)
		(fit  n06  n18  n24 rack03)
		(fit  n21  n04  n25 rack03)
		(fit  n17  n08  n25 rack03)
		(fit  n16  n09  n25 rack03)
		(fit  n14  n11  n25 rack03)
		(fit  n07  n18  n25 rack03)
		(fit  n00  n25  n25 rack03)
		(fit  n23  n04  n27 rack03)
		(fit  n19  n08  n27 rack03)
		(fit  n18  n09  n27 rack03)
		(fit  n16  n11  n27 rack03)
		(fit  n09  n18  n27 rack03)
		(fit  n02  n25  n27 rack03)
		(fit  n24  n04  n28 rack03)
		(fit  n20  n08  n28 rack03)
		(fit  n19  n09  n28 rack03)
		(fit  n17  n11  n28 rack03)
		(fit  n10  n18  n28 rack03)
		(fit  n03  n25  n28 rack03)
		(fit  n00  n32  n32 rack03)
		(fit  n28  n04  n32 rack03)
		(fit  n24  n08  n32 rack03)
		(fit  n23  n09  n32 rack03)
		(fit  n21  n11  n32 rack03)
		(fit  n14  n18  n32 rack03)
		(fit  n07  n25  n32 rack03)
		(fit  n04  n32  n36 rack03)
		(fit  n32  n04  n36 rack03)
		(fit  n28  n08  n36 rack03)
		(fit  n27  n09  n36 rack03)
		(fit  n25  n11  n36 rack03)
		(fit  n18  n18  n36 rack03)
		(fit  n11  n25  n36 rack03)
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
		(fit  n22  n04  n26 rack04)
		(fit  n18  n08  n26 rack04)
		(fit  n17  n09  n26 rack04)
		(fit  n15  n11  n26 rack04)
		(fit  n08  n18  n26 rack04)
		(fit  n01  n25  n26 rack04)
		(fit  n26  n04  n30 rack04)
		(fit  n22  n08  n30 rack04)
		(fit  n21  n09  n30 rack04)
		(fit  n19  n11  n30 rack04)
		(fit  n12  n18  n30 rack04)
		(fit  n05  n25  n30 rack04)
		; Sizes fitting rack: rack05
		(fit  n00  n04  n04 rack05)
		(fit  n01  n04  n05 rack05)
		(fit  n02  n04  n06 rack05)
		(fit  n03  n04  n07 rack05)
		(fit  n04  n04  n08 rack05)
		(fit  n00  n08  n08 rack05)
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
		(fit  n10  n04  n14 rack05)
		(fit  n06  n08  n14 rack05)
		(fit  n05  n09  n14 rack05)
		(fit  n03  n11  n14 rack05)
		(fit  n11  n04  n15 rack05)
		(fit  n07  n08  n15 rack05)
		(fit  n06  n09  n15 rack05)
		(fit  n04  n11  n15 rack05)
		(fit  n15  n04  n19 rack05)
		(fit  n11  n08  n19 rack05)
		(fit  n10  n09  n19 rack05)
		(fit  n08  n11  n19 rack05)
		(fit  n01  n18  n19 rack05)
		(fit  n19  n04  n23 rack05)
		(fit  n15  n08  n23 rack05)
		(fit  n14  n09  n23 rack05)
		(fit  n12  n11  n23 rack05)
		(fit  n05  n18  n23 rack05)
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
		(fit  n02  n04  n06 rack07)
		(fit  n03  n04  n07 rack07)
		(fit  n04  n04  n08 rack07)
		(fit  n00  n08  n08 rack07)
		(fit  n05  n04  n09 rack07)
		(fit  n01  n08  n09 rack07)
		(fit  n00  n09  n09 rack07)
		(fit  n06  n04  n10 rack07)
		(fit  n02  n08  n10 rack07)
		(fit  n01  n09  n10 rack07)
		(fit  n07  n04  n11 rack07)
		(fit  n03  n08  n11 rack07)
		(fit  n02  n09  n11 rack07)
		(fit  n00  n11  n11 rack07)
		(fit  n08  n04  n12 rack07)
		(fit  n04  n08  n12 rack07)
		(fit  n03  n09  n12 rack07)
		(fit  n01  n11  n12 rack07)
		(fit  n09  n04  n13 rack07)
		(fit  n05  n08  n13 rack07)
		(fit  n04  n09  n13 rack07)
		(fit  n02  n11  n13 rack07)
		(fit  n10  n04  n14 rack07)
		(fit  n06  n08  n14 rack07)
		(fit  n05  n09  n14 rack07)
		(fit  n03  n11  n14 rack07)
		(fit  n11  n04  n15 rack07)
		(fit  n07  n08  n15 rack07)
		(fit  n06  n09  n15 rack07)
		(fit  n04  n11  n15 rack07)
		(fit  n13  n04  n17 rack07)
		(fit  n09  n08  n17 rack07)
		(fit  n08  n09  n17 rack07)
		(fit  n06  n11  n17 rack07)
		(fit  n14  n04  n18 rack07)
		(fit  n10  n08  n18 rack07)
		(fit  n09  n09  n18 rack07)
		(fit  n07  n11  n18 rack07)
		(fit  n00  n18  n18 rack07)
		(fit  n15  n04  n19 rack07)
		(fit  n11  n08  n19 rack07)
		(fit  n10  n09  n19 rack07)
		(fit  n08  n11  n19 rack07)
		(fit  n01  n18  n19 rack07)
		(fit  n17  n04  n21 rack07)
		(fit  n13  n08  n21 rack07)
		(fit  n12  n09  n21 rack07)
		(fit  n10  n11  n21 rack07)
		(fit  n03  n18  n21 rack07)
		(fit  n18  n04  n22 rack07)
		(fit  n14  n08  n22 rack07)
		(fit  n13  n09  n22 rack07)
		(fit  n11  n11  n22 rack07)
		(fit  n04  n18  n22 rack07)
		(fit  n22  n04  n26 rack07)
		(fit  n18  n08  n26 rack07)
		(fit  n17  n09  n26 rack07)
		(fit  n15  n11  n26 rack07)
		(fit  n08  n18  n26 rack07)
		(fit  n01  n25  n26 rack07)
		(fit  n26  n04  n30 rack07)
		(fit  n22  n08  n30 rack07)
		(fit  n21  n09  n30 rack07)
		(fit  n19  n11  n30 rack07)
		(fit  n12  n18  n30 rack07)
		(fit  n05  n25  n30 rack07)
		; Sizes fitting rack: rack08
		(fit  n00  n04  n04 rack08)
		(fit  n01  n04  n05 rack08)
		(fit  n02  n04  n06 rack08)
		(fit  n03  n04  n07 rack08)
		(fit  n04  n04  n08 rack08)
		(fit  n00  n08  n08 rack08)
		(fit  n06  n04  n10 rack08)
		(fit  n02  n08  n10 rack08)
		(fit  n01  n09  n10 rack08)
		(fit  n07  n04  n11 rack08)
		(fit  n03  n08  n11 rack08)
		(fit  n02  n09  n11 rack08)
		(fit  n00  n11  n11 rack08)
		(fit  n08  n04  n12 rack08)
		(fit  n04  n08  n12 rack08)
		(fit  n03  n09  n12 rack08)
		(fit  n01  n11  n12 rack08)
		(fit  n10  n04  n14 rack08)
		(fit  n06  n08  n14 rack08)
		(fit  n05  n09  n14 rack08)
		(fit  n03  n11  n14 rack08)
		(fit  n11  n04  n15 rack08)
		(fit  n07  n08  n15 rack08)
		(fit  n06  n09  n15 rack08)
		(fit  n04  n11  n15 rack08)
		(fit  n15  n04  n19 rack08)
		(fit  n11  n08  n19 rack08)
		(fit  n10  n09  n19 rack08)
		(fit  n08  n11  n19 rack08)
		(fit  n01  n18  n19 rack08)
		(fit  n19  n04  n23 rack08)
		(fit  n15  n08  n23 rack08)
		(fit  n14  n09  n23 rack08)
		(fit  n12  n11  n23 rack08)
		(fit  n05  n18  n23 rack08)
		; Sizes fitting rack: rack09
		(fit  n00  n04  n04 rack09)
		(fit  n01  n04  n05 rack09)
		(fit  n02  n04  n06 rack09)
		(fit  n04  n04  n08 rack09)
		(fit  n00  n08  n08 rack09)
		(fit  n05  n04  n09 rack09)
		(fit  n01  n08  n09 rack09)
		(fit  n00  n09  n09 rack09)
		(fit  n06  n04  n10 rack09)
		(fit  n02  n08  n10 rack09)
		(fit  n01  n09  n10 rack09)
		(fit  n08  n04  n12 rack09)
		(fit  n04  n08  n12 rack09)
		(fit  n03  n09  n12 rack09)
		(fit  n01  n11  n12 rack09)
		(fit  n09  n04  n13 rack09)
		(fit  n05  n08  n13 rack09)
		(fit  n04  n09  n13 rack09)
		(fit  n02  n11  n13 rack09)
		(fit  n13  n04  n17 rack09)
		(fit  n09  n08  n17 rack09)
		(fit  n08  n09  n17 rack09)
		(fit  n06  n11  n17 rack09)
		(fit  n17  n04  n21 rack09)
		(fit  n13  n08  n21 rack09)
		(fit  n12  n09  n21 rack09)
		(fit  n10  n11  n21 rack09)
		(fit  n03  n18  n21 rack09)
		; Sizes fitting rack: rack10
		(fit  n00  n04  n04 rack10)
		(fit  n01  n04  n05 rack10)
		(fit  n02  n04  n06 rack10)
		(fit  n03  n04  n07 rack10)
		(fit  n04  n04  n08 rack10)
		(fit  n00  n08  n08 rack10)
		(fit  n05  n04  n09 rack10)
		(fit  n01  n08  n09 rack10)
		(fit  n00  n09  n09 rack10)
		(fit  n06  n04  n10 rack10)
		(fit  n02  n08  n10 rack10)
		(fit  n01  n09  n10 rack10)
		(fit  n07  n04  n11 rack10)
		(fit  n03  n08  n11 rack10)
		(fit  n02  n09  n11 rack10)
		(fit  n00  n11  n11 rack10)
		(fit  n08  n04  n12 rack10)
		(fit  n04  n08  n12 rack10)
		(fit  n03  n09  n12 rack10)
		(fit  n01  n11  n12 rack10)
		(fit  n09  n04  n13 rack10)
		(fit  n05  n08  n13 rack10)
		(fit  n04  n09  n13 rack10)
		(fit  n02  n11  n13 rack10)
		(fit  n10  n04  n14 rack10)
		(fit  n06  n08  n14 rack10)
		(fit  n05  n09  n14 rack10)
		(fit  n03  n11  n14 rack10)
		(fit  n11  n04  n15 rack10)
		(fit  n07  n08  n15 rack10)
		(fit  n06  n09  n15 rack10)
		(fit  n04  n11  n15 rack10)
		(fit  n12  n04  n16 rack10)
		(fit  n08  n08  n16 rack10)
		(fit  n07  n09  n16 rack10)
		(fit  n05  n11  n16 rack10)
		(fit  n13  n04  n17 rack10)
		(fit  n09  n08  n17 rack10)
		(fit  n08  n09  n17 rack10)
		(fit  n06  n11  n17 rack10)
		(fit  n14  n04  n18 rack10)
		(fit  n10  n08  n18 rack10)
		(fit  n09  n09  n18 rack10)
		(fit  n07  n11  n18 rack10)
		(fit  n00  n18  n18 rack10)
		(fit  n15  n04  n19 rack10)
		(fit  n11  n08  n19 rack10)
		(fit  n10  n09  n19 rack10)
		(fit  n08  n11  n19 rack10)
		(fit  n01  n18  n19 rack10)
		(fit  n16  n04  n20 rack10)
		(fit  n12  n08  n20 rack10)
		(fit  n11  n09  n20 rack10)
		(fit  n09  n11  n20 rack10)
		(fit  n02  n18  n20 rack10)
		(fit  n17  n04  n21 rack10)
		(fit  n13  n08  n21 rack10)
		(fit  n12  n09  n21 rack10)
		(fit  n10  n11  n21 rack10)
		(fit  n03  n18  n21 rack10)
		(fit  n19  n04  n23 rack10)
		(fit  n15  n08  n23 rack10)
		(fit  n14  n09  n23 rack10)
		(fit  n12  n11  n23 rack10)
		(fit  n05  n18  n23 rack10)
		(fit  n20  n04  n24 rack10)
		(fit  n16  n08  n24 rack10)
		(fit  n15  n09  n24 rack10)
		(fit  n13  n11  n24 rack10)
		(fit  n06  n18  n24 rack10)
		(fit  n21  n04  n25 rack10)
		(fit  n17  n08  n25 rack10)
		(fit  n16  n09  n25 rack10)
		(fit  n14  n11  n25 rack10)
		(fit  n07  n18  n25 rack10)
		(fit  n00  n25  n25 rack10)
		(fit  n23  n04  n27 rack10)
		(fit  n19  n08  n27 rack10)
		(fit  n18  n09  n27 rack10)
		(fit  n16  n11  n27 rack10)
		(fit  n09  n18  n27 rack10)
		(fit  n02  n25  n27 rack10)
		(fit  n24  n04  n28 rack10)
		(fit  n20  n08  n28 rack10)
		(fit  n19  n09  n28 rack10)
		(fit  n17  n11  n28 rack10)
		(fit  n10  n18  n28 rack10)
		(fit  n03  n25  n28 rack10)
		(fit  n00  n32  n32 rack10)
		(fit  n28  n04  n32 rack10)
		(fit  n24  n08  n32 rack10)
		(fit  n23  n09  n32 rack10)
		(fit  n21  n11  n32 rack10)
		(fit  n14  n18  n32 rack10)
		(fit  n07  n25  n32 rack10)
		(fit  n04  n32  n36 rack10)
		(fit  n32  n04  n36 rack10)
		(fit  n28  n08  n36 rack10)
		(fit  n27  n09  n36 rack10)
		(fit  n25  n11  n36 rack10)
		(fit  n18  n18  n36 rack10)
		(fit  n11  n25  n36 rack10)
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
		; Racks 11
		; Rack:rack00
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n01)
		(in jig0008 rack00)
		(clear jig0008 bside)
		(clear jig0008 fside)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n03)
		(in jig0018 rack01)
		(clear jig0018 bside)
		(clear jig0018 fside)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n07)
		(in jig0004 rack02)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack03
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n04)
		(in jig0009 rack03)
		(clear jig0009 bside)
		(clear jig0009 fside)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n04)
		(in jig0014 rack04)
		(clear jig0014 bside)
		(next-to jig0014 jig0011 bside)
		(next-to jig0011 jig0014 fside)
		(in jig0011 rack04)
		(next-to jig0011 jig0010 bside)
		(next-to jig0010 jig0011 fside)
		(in jig0010 rack04)
		(clear jig0010 fside)
		; Rack:rack05
		(at-side rack05 bside)
		(at-side rack05 fside)
		(free-space rack05 n05)
		(in jig0016 rack05)
		(clear jig0016 bside)
		(next-to jig0016 jig0015 bside)
		(next-to jig0015 jig0016 fside)
		(in jig0015 rack05)
		(clear jig0015 fside)
		; Rack:rack06
		(at-side rack06 bside)
		(at-side rack06 fside)
		(free-space rack06 n05)
		(in jig0002 rack06)
		(clear jig0002 bside)
		(next-to jig0002 jig0005 bside)
		(next-to jig0005 jig0002 fside)
		(in jig0005 rack06)
		(clear jig0005 fside)
		; Rack:rack07
		(at-side rack07 bside)
		(at-side rack07 fside)
		(free-space rack07 n00)
		(in jig0012 rack07)
		(clear jig0012 bside)
		(next-to jig0012 jig0003 bside)
		(next-to jig0003 jig0012 fside)
		(in jig0003 rack07)
		(next-to jig0003 jig0013 bside)
		(next-to jig0013 jig0003 fside)
		(in jig0013 rack07)
		(clear jig0013 fside)
		; Rack:rack08
		(at-side rack08 bside)
		(at-side rack08 fside)
		(free-space rack08 n01)
		(in jig0001 rack08)
		(clear jig0001 bside)
		(next-to jig0001 jig0006 bside)
		(next-to jig0006 jig0001 fside)
		(in jig0006 rack08)
		(clear jig0006 fside)
		; Rack:rack09
		(at-side rack09 bside)
		(at-side rack09 fside)
		(free-space rack09 n12)
		(in jig0017 rack09)
		(clear jig0017 bside)
		(clear jig0017 fside)
		; Rack:rack10
		(at-side rack10 bside)
		(at-side rack10 fside)
		(free-space rack10 n04)
		(in jig0007 rack10)
		(clear jig0007 bside)
		(clear jig0007 fside)
		; Jigs (size):
		(is_type jig0001 typeD)
		(size jig0001 n18)
		(empty-size jig0001 n18)
		(empty jig0001)
		(is_type jig0002 typeB)
		(size jig0002 n08)
		(empty-size jig0002 n08)
		(empty jig0002)
		(is_type jig0003 typeB)
		(size jig0003 n11)
		(empty-size jig0003 n08)
		(is_type jig0004 typeE)
		(size jig0004 n32)
		(empty-size jig0004 n32)
		(empty jig0004)
		(is_type jig0005 typeB)
		(size jig0005 n11)
		(empty-size jig0005 n08)
		(is_type jig0006 typeA)
		(size jig0006 n04)
		(empty-size jig0006 n04)
		(is_type jig0007 typeE)
		(size jig0007 n32)
		(empty-size jig0007 n32)
		(empty jig0007)
		(is_type jig0008 typeD)
		(size jig0008 n25)
		(empty-size jig0008 n18)
		(is_type jig0009 typeE)
		(size jig0009 n32)
		(empty-size jig0009 n32)
		(is_type jig0010 typeB)
		(size jig0010 n08)
		(empty-size jig0010 n08)
		(empty jig0010)
		(is_type jig0011 typeC)
		(size jig0011 n09)
		(empty-size jig0011 n09)
		(empty jig0011)
		(is_type jig0012 typeB)
		(size jig0012 n08)
		(empty-size jig0012 n08)
		(empty jig0012)
		(is_type jig0013 typeB)
		(size jig0013 n11)
		(empty-size jig0013 n08)
		(is_type jig0014 typeC)
		(size jig0014 n09)
		(empty-size jig0014 n09)
		(empty jig0014)
		(is_type jig0015 typeC)
		(size jig0015 n09)
		(empty-size jig0015 n09)
		(empty jig0015)
		(is_type jig0016 typeC)
		(size jig0016 n09)
		(empty-size jig0016 n09)
		(empty jig0016)
		(is_type jig0017 typeC)
		(size jig0017 n09)
		(empty-size jig0017 n09)
		(empty jig0017)
		(is_type jig0018 typeC)
		(size jig0018 n18)
		(empty-size jig0018 n09)
		(is_type jig0019 typeC)
		(size jig0019 n18)
		(empty-size jig0019 n09)
		(is_type jig0020 typeC)
		(size jig0020 n18)
		(empty-size jig0020 n09)
		(is_type jig0021 typeC)
		(size jig0021 n18)
		(empty-size jig0021 n09)
		(is_type jig0022 typeC)
		(size jig0022 n18)
		(empty-size jig0022 n09)
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
		(is_type jig0028 typeE)
		(size jig0028 n32)
		(empty-size jig0028 n32)
		(is_type jig0029 typeD)
		(size jig0029 n25)
		(empty-size jig0029 n18)
		(is_type jig0030 typeC)
		(size jig0030 n18)
		(empty-size jig0030 n09)
		(is_type jig0031 typeC)
		(size jig0031 n18)
		(empty-size jig0031 n09)
		(is_type jig0032 typeB)
		(size jig0032 n11)
		(empty-size jig0032 n08)
		(is_type jig0033 typeB)
		(size jig0033 n11)
		(empty-size jig0033 n08)
		(is_type jig0034 typeB)
		(size jig0034 n11)
		(empty-size jig0034 n08)
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
		(is_type jig0045 typeB)
		(size jig0045 n11)
		(empty-size jig0045 n08)
		(is_type jig0046 typeB)
		(size jig0046 n11)
		(empty-size jig0046 n08)
		(is_type jig0047 typeB)
		(size jig0047 n11)
		(empty-size jig0047 n08)
		(is_type jig0048 typeB)
		(size jig0048 n11)
		(empty-size jig0048 n08)
		(is_type jig0049 typeB)
		(size jig0049 n11)
		(empty-size jig0049 n08)
		(is_type jig0050 typeB)
		(size jig0050 n11)
		(empty-size jig0050 n08)
		(is_type jig0051 typeD)
		(size jig0051 n25)
		(empty-size jig0051 n18)
		(is_type jig0052 typeE)
		(size jig0052 n32)
		(empty-size jig0052 n32)
		(is_type jig0053 typeC)
		(size jig0053 n18)
		(empty-size jig0053 n09)
		(is_type jig0054 typeC)
		(size jig0054 n18)
		(empty-size jig0054 n09)
		(is_type jig0055 typeB)
		(size jig0055 n11)
		(empty-size jig0055 n08)
		(is_type jig0056 typeB)
		(size jig0056 n11)
		(empty-size jig0056 n08)
		(is_type jig0057 typeB)
		(size jig0057 n11)
		(empty-size jig0057 n08)
		(is_type jig0058 typeC)
		(size jig0058 n18)
		(empty-size jig0058 n09)
		(is_type jig0059 typeC)
		(size jig0059 n18)
		(empty-size jig0059 n09)
		(is_type jig0060 typeC)
		(size jig0060 n18)
		(empty-size jig0060 n09)
		(is_type jig0061 typeB)
		(size jig0061 n11)
		(empty-size jig0061 n08)
		(is_type jig0062 typeC)
		(size jig0062 n18)
		(empty-size jig0062 n09)
		(is_type jig0063 typeC)
		(size jig0063 n18)
		(empty-size jig0063 n09)
		(is_type jig0064 typeC)
		(size jig0064 n18)
		(empty-size jig0064 n09)
		(is_type jig0065 typeE)
		(size jig0065 n32)
		(empty-size jig0065 n32)
		(is_type jig0066 typeA)
		(size jig0066 n04)
		(empty-size jig0066 n04)
		(is_type jig0067 typeA)
		(size jig0067 n04)
		(empty-size jig0067 n04)
		(is_type jig0068 typeA)
		(size jig0068 n04)
		(empty-size jig0068 n04)
		(is_type jig0069 typeA)
		(size jig0069 n04)
		(empty-size jig0069 n04)
		(is_type jig0070 typeA)
		(size jig0070 n04)
		(empty-size jig0070 n04)
		(is_type jig0071 typeA)
		(size jig0071 n04)
		(empty-size jig0071 n04)
		(is_type jig0072 typeA)
		(size jig0072 n04)
		(empty-size jig0072 n04)
		(is_type jig0073 typeA)
		(size jig0073 n04)
		(empty-size jig0073 n04)
		(is_type jig0074 typeA)
		(size jig0074 n04)
		(empty-size jig0074 n04)
		(is_type jig0075 typeA)
		(size jig0075 n04)
		(empty-size jig0075 n04)
		(is_type jig0076 typeB)
		(size jig0076 n11)
		(empty-size jig0076 n08)
		(is_type jig0077 typeB)
		(size jig0077 n11)
		(empty-size jig0077 n08)
		(is_type jig0078 typeB)
		(size jig0078 n11)
		(empty-size jig0078 n08)
		(is_type jig0079 typeB)
		(size jig0079 n11)
		(empty-size jig0079 n08)
		(is_type jig0080 typeB)
		(size jig0080 n11)
		(empty-size jig0080 n08)
		(is_type jig0081 typeB)
		(size jig0081 n11)
		(empty-size jig0081 n08)
		(is_type jig0082 typeC)
		(size jig0082 n18)
		(empty-size jig0082 n09)
		(is_type jig0083 typeC)
		(size jig0083 n18)
		(empty-size jig0083 n09)
		(is_type jig0084 typeE)
		(size jig0084 n32)
		(empty-size jig0084 n32)
		(is_type jig0085 typeB)
		(size jig0085 n11)
		(empty-size jig0085 n08)
		(is_type jig0086 typeB)
		(size jig0086 n11)
		(empty-size jig0086 n08)
		(is_type jig0087 typeB)
		(size jig0087 n11)
		(empty-size jig0087 n08)
		(is_type jig0088 typeD)
		(size jig0088 n25)
		(empty-size jig0088 n18)
		(is_type jig0089 typeB)
		(size jig0089 n11)
		(empty-size jig0089 n08)
		(is_type jig0090 typeB)
		(size jig0090 n11)
		(empty-size jig0090 n08)
		(is_type jig0091 typeB)
		(size jig0091 n11)
		(empty-size jig0091 n08)
		(is_type jig0092 typeB)
		(size jig0092 n11)
		(empty-size jig0092 n08)
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
		(next-flight-to-process beluga43 beluga44)
		(next-flight-to-process beluga44 beluga45)
		(next-flight-to-process beluga45 beluga46)
		(next-flight-to-process beluga46 beluga47)
		(next-flight-to-process beluga47 beluga48)
		(next-flight-to-process beluga48 beluga49)
		(next-flight-to-process beluga49 beluga50)
		(next-flight-to-process beluga50 beluga51)
		(next-flight-to-process beluga51 beluga52)
		(next-flight-to-process beluga52 beluga53)
		(next-flight-to-process beluga53 beluga54)
		(next-flight-to-process beluga54 beluga55)
		(next-flight-to-process beluga55 beluga56)
		(next-flight-to-process beluga56 beluga57)
		(next-flight-to-process beluga57 beluga58)
		; Number of flights: 58
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; No jigs
		(to_unload dummy-jig beluga1)
		; To Process Flights
		; Flight: beluga2
		; No jigs
		(to_unload dummy-jig beluga2)
		; Flight: beluga3
		; 0: jig0019 1: jig0020
		(to_unload jig0019 beluga3)
		(in jig0019 beluga3)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga3)
		(next_unload jig0020 dummy-jig)
		; Flight: beluga4
		; 0: jig0021 1: jig0022
		(to_unload jig0021 beluga4)
		(in jig0021 beluga4)
		(next_unload jig0021 jig0022)
		(in jig0022 beluga4)
		(next_unload jig0022 dummy-jig)
		; Flight: beluga5
		; 0: jig0023 1: jig0024 2: jig0025
		(to_unload jig0023 beluga5)
		(in jig0023 beluga5)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga5)
		(next_unload jig0024 jig0025)
		(in jig0025 beluga5)
		(next_unload jig0025 dummy-jig)
		; Flight: beluga6
		; 0: jig0026 1: jig0027
		(to_unload jig0026 beluga6)
		(in jig0026 beluga6)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga6)
		(next_unload jig0027 dummy-jig)
		; Flight: beluga7
		; 0: jig0028
		(to_unload jig0028 beluga7)
		(in jig0028 beluga7)
		(next_unload jig0028 dummy-jig)
		; Flight: beluga8
		; No jigs
		(to_unload dummy-jig beluga8)
		; Flight: beluga9
		; No jigs
		(to_unload dummy-jig beluga9)
		; Flight: beluga10
		; No jigs
		(to_unload dummy-jig beluga10)
		; Flight: beluga11
		; No jigs
		(to_unload dummy-jig beluga11)
		; Flight: beluga12
		; 0: jig0029
		(to_unload jig0029 beluga12)
		(in jig0029 beluga12)
		(next_unload jig0029 dummy-jig)
		; Flight: beluga13
		; 0: jig0030 1: jig0031
		(to_unload jig0030 beluga13)
		(in jig0030 beluga13)
		(next_unload jig0030 jig0031)
		(in jig0031 beluga13)
		(next_unload jig0031 dummy-jig)
		; Flight: beluga14
		; No jigs
		(to_unload dummy-jig beluga14)
		; Flight: beluga15
		; No jigs
		(to_unload dummy-jig beluga15)
		; Flight: beluga16
		; 0: jig0032 1: jig0033 2: jig0034
		(to_unload jig0032 beluga16)
		(in jig0032 beluga16)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga16)
		(next_unload jig0033 jig0034)
		(in jig0034 beluga16)
		(next_unload jig0034 dummy-jig)
		; Flight: beluga17
		; 0: jig0035 1: jig0036 2: jig0037 3: jig0038 4: jig0039 5: jig0040 6: jig0041 7: jig0042 8: jig0043 9: jig0044
		(to_unload jig0035 beluga17)
		(in jig0035 beluga17)
		(next_unload jig0035 jig0036)
		(in jig0036 beluga17)
		(next_unload jig0036 jig0037)
		(in jig0037 beluga17)
		(next_unload jig0037 jig0038)
		(in jig0038 beluga17)
		(next_unload jig0038 jig0039)
		(in jig0039 beluga17)
		(next_unload jig0039 jig0040)
		(in jig0040 beluga17)
		(next_unload jig0040 jig0041)
		(in jig0041 beluga17)
		(next_unload jig0041 jig0042)
		(in jig0042 beluga17)
		(next_unload jig0042 jig0043)
		(in jig0043 beluga17)
		(next_unload jig0043 jig0044)
		(in jig0044 beluga17)
		(next_unload jig0044 dummy-jig)
		; Flight: beluga18
		; 0: jig0045 1: jig0046 2: jig0047
		(to_unload jig0045 beluga18)
		(in jig0045 beluga18)
		(next_unload jig0045 jig0046)
		(in jig0046 beluga18)
		(next_unload jig0046 jig0047)
		(in jig0047 beluga18)
		(next_unload jig0047 dummy-jig)
		; Flight: beluga19
		; 0: jig0048 1: jig0049 2: jig0050
		(to_unload jig0048 beluga19)
		(in jig0048 beluga19)
		(next_unload jig0048 jig0049)
		(in jig0049 beluga19)
		(next_unload jig0049 jig0050)
		(in jig0050 beluga19)
		(next_unload jig0050 dummy-jig)
		; Flight: beluga20
		; 0: jig0051
		(to_unload jig0051 beluga20)
		(in jig0051 beluga20)
		(next_unload jig0051 dummy-jig)
		; Flight: beluga21
		; No jigs
		(to_unload dummy-jig beluga21)
		; Flight: beluga22
		; No jigs
		(to_unload dummy-jig beluga22)
		; Flight: beluga23
		; 0: jig0052
		(to_unload jig0052 beluga23)
		(in jig0052 beluga23)
		(next_unload jig0052 dummy-jig)
		; Flight: beluga24
		; No jigs
		(to_unload dummy-jig beluga24)
		; Flight: beluga25
		; No jigs
		(to_unload dummy-jig beluga25)
		; Flight: beluga26
		; 0: jig0053 1: jig0054
		(to_unload jig0053 beluga26)
		(in jig0053 beluga26)
		(next_unload jig0053 jig0054)
		(in jig0054 beluga26)
		(next_unload jig0054 dummy-jig)
		; Flight: beluga27
		; 0: jig0055 1: jig0056 2: jig0057
		(to_unload jig0055 beluga27)
		(in jig0055 beluga27)
		(next_unload jig0055 jig0056)
		(in jig0056 beluga27)
		(next_unload jig0056 jig0057)
		(in jig0057 beluga27)
		(next_unload jig0057 dummy-jig)
		; Flight: beluga28
		; 0: jig0058
		(to_unload jig0058 beluga28)
		(in jig0058 beluga28)
		(next_unload jig0058 dummy-jig)
		; Flight: beluga29
		; 0: jig0059 1: jig0060
		(to_unload jig0059 beluga29)
		(in jig0059 beluga29)
		(next_unload jig0059 jig0060)
		(in jig0060 beluga29)
		(next_unload jig0060 dummy-jig)
		; Flight: beluga30
		; 0: jig0061
		(to_unload jig0061 beluga30)
		(in jig0061 beluga30)
		(next_unload jig0061 dummy-jig)
		; Flight: beluga31
		; No jigs
		(to_unload dummy-jig beluga31)
		; Flight: beluga32
		; No jigs
		(to_unload dummy-jig beluga32)
		; Flight: beluga33
		; 0: jig0062 1: jig0063
		(to_unload jig0062 beluga33)
		(in jig0062 beluga33)
		(next_unload jig0062 jig0063)
		(in jig0063 beluga33)
		(next_unload jig0063 dummy-jig)
		; Flight: beluga34
		; 0: jig0064
		(to_unload jig0064 beluga34)
		(in jig0064 beluga34)
		(next_unload jig0064 dummy-jig)
		; Flight: beluga35
		; No jigs
		(to_unload dummy-jig beluga35)
		; Flight: beluga36
		; 0: jig0065
		(to_unload jig0065 beluga36)
		(in jig0065 beluga36)
		(next_unload jig0065 dummy-jig)
		; Flight: beluga37
		; No jigs
		(to_unload dummy-jig beluga37)
		; Flight: beluga38
		; No jigs
		(to_unload dummy-jig beluga38)
		; Flight: beluga39
		; No jigs
		(to_unload dummy-jig beluga39)
		; Flight: beluga40
		; 0: jig0066 1: jig0067 2: jig0068 3: jig0069 4: jig0070 5: jig0071 6: jig0072 7: jig0073 8: jig0074 9: jig0075
		(to_unload jig0066 beluga40)
		(in jig0066 beluga40)
		(next_unload jig0066 jig0067)
		(in jig0067 beluga40)
		(next_unload jig0067 jig0068)
		(in jig0068 beluga40)
		(next_unload jig0068 jig0069)
		(in jig0069 beluga40)
		(next_unload jig0069 jig0070)
		(in jig0070 beluga40)
		(next_unload jig0070 jig0071)
		(in jig0071 beluga40)
		(next_unload jig0071 jig0072)
		(in jig0072 beluga40)
		(next_unload jig0072 jig0073)
		(in jig0073 beluga40)
		(next_unload jig0073 jig0074)
		(in jig0074 beluga40)
		(next_unload jig0074 jig0075)
		(in jig0075 beluga40)
		(next_unload jig0075 dummy-jig)
		; Flight: beluga41
		; No jigs
		(to_unload dummy-jig beluga41)
		; Flight: beluga42
		; 0: jig0076 1: jig0077 2: jig0078
		(to_unload jig0076 beluga42)
		(in jig0076 beluga42)
		(next_unload jig0076 jig0077)
		(in jig0077 beluga42)
		(next_unload jig0077 jig0078)
		(in jig0078 beluga42)
		(next_unload jig0078 dummy-jig)
		; Flight: beluga43
		; No jigs
		(to_unload dummy-jig beluga43)
		; Flight: beluga44
		; 0: jig0079 1: jig0080 2: jig0081
		(to_unload jig0079 beluga44)
		(in jig0079 beluga44)
		(next_unload jig0079 jig0080)
		(in jig0080 beluga44)
		(next_unload jig0080 jig0081)
		(in jig0081 beluga44)
		(next_unload jig0081 dummy-jig)
		; Flight: beluga45
		; No jigs
		(to_unload dummy-jig beluga45)
		; Flight: beluga46
		; 0: jig0082 1: jig0083
		(to_unload jig0082 beluga46)
		(in jig0082 beluga46)
		(next_unload jig0082 jig0083)
		(in jig0083 beluga46)
		(next_unload jig0083 dummy-jig)
		; Flight: beluga47
		; 0: jig0084
		(to_unload jig0084 beluga47)
		(in jig0084 beluga47)
		(next_unload jig0084 dummy-jig)
		; Flight: beluga48
		; No jigs
		(to_unload dummy-jig beluga48)
		; Flight: beluga49
		; No jigs
		(to_unload dummy-jig beluga49)
		; Flight: beluga50
		; 0: jig0085 1: jig0086 2: jig0087
		(to_unload jig0085 beluga50)
		(in jig0085 beluga50)
		(next_unload jig0085 jig0086)
		(in jig0086 beluga50)
		(next_unload jig0086 jig0087)
		(in jig0087 beluga50)
		(next_unload jig0087 dummy-jig)
		; Flight: beluga51
		; 0: jig0088
		(to_unload jig0088 beluga51)
		(in jig0088 beluga51)
		(next_unload jig0088 dummy-jig)
		; Flight: beluga52
		; 0: jig0089 1: jig0090 2: jig0091
		(to_unload jig0089 beluga52)
		(in jig0089 beluga52)
		(next_unload jig0089 jig0090)
		(in jig0090 beluga52)
		(next_unload jig0090 jig0091)
		(in jig0091 beluga52)
		(next_unload jig0091 dummy-jig)
		; Flight: beluga53
		; No jigs
		(to_unload dummy-jig beluga53)
		; Flight: beluga54
		; 0: jig0092
		(to_unload jig0092 beluga54)
		(in jig0092 beluga54)
		(next_unload jig0092 dummy-jig)
		; Flight: beluga55
		; No jigs
		(to_unload dummy-jig beluga55)
		; Flight: beluga56
		; No jigs
		(to_unload dummy-jig beluga56)
		; Flight: beluga57
		; No jigs
		(to_unload dummy-jig beluga57)
		; Flight: beluga58
		; No jigs
		(to_unload dummy-jig beluga58)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeB) (1: typeB) (2: typeB)
		(to_load typeB slot0 beluga1)
		(next_load typeB slot0 slot1 beluga1)
		(next_load typeB slot1 slot2 beluga1)
		(next_load dummy-type slot2 dummy-slot beluga1)
		; To Process Flights
		; 0: typeD
		(to_load typeD slot0 beluga2)
		(next_load dummy-type slot0 dummy-slot beluga2)
		; 0: typeE
		(to_load typeE slot0 beluga3)
		(next_load dummy-type slot0 dummy-slot beluga3)
		; 0: typeE
		(to_load typeE slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; 0: typeE
		(to_load typeE slot0 beluga5)
		(next_load dummy-type slot0 dummy-slot beluga5)
		; 0: typeC 1: typeC 2: typeC 3: typeC
		(to_load typeC slot0 beluga6)
		(next_load typeC slot0 slot1 beluga6)
		(next_load typeC slot1 slot2 beluga6)
		(next_load typeC slot2 slot3 beluga6)
		(next_load dummy-type slot3 dummy-slot beluga6)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga7)
		(next_load typeC slot0 slot1 beluga7)
		(next_load dummy-type slot1 dummy-slot beluga7)
		; 0: typeA
		(to_load typeA slot0 beluga8)
		(next_load dummy-type slot0 dummy-slot beluga8)
		; 0: typeC
		(to_load typeC slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeB
		(to_load typeB slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeB
		(to_load typeB slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga12)
		(next_load typeB slot0 slot1 beluga12)
		(next_load dummy-type slot1 dummy-slot beluga12)
		; 0: typeC
		(to_load typeC slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeB
		(to_load typeB slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeC
		(to_load typeC slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeD
		(to_load typeD slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; 0: typeC
		(to_load typeC slot0 beluga17)
		(next_load dummy-type slot0 dummy-slot beluga17)
		; 0: typeD
		(to_load typeD slot0 beluga18)
		(next_load dummy-type slot0 dummy-slot beluga18)
		; No jigs
		(to_load dummy-type dummy-slot beluga19)
		; 0: typeB
		(to_load typeB slot0 beluga20)
		(next_load dummy-type slot0 dummy-slot beluga20)
		; 0: typeC
		(to_load typeC slot0 beluga21)
		(next_load dummy-type slot0 dummy-slot beluga21)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga22)
		(next_load typeB slot0 slot1 beluga22)
		(next_load typeB slot1 slot2 beluga22)
		(next_load typeB slot2 slot3 beluga22)
		(next_load dummy-type slot3 dummy-slot beluga22)
		; 0: typeC
		(to_load typeC slot0 beluga23)
		(next_load dummy-type slot0 dummy-slot beluga23)
		; 0: typeC
		(to_load typeC slot0 beluga24)
		(next_load dummy-type slot0 dummy-slot beluga24)
		; 0: typeB
		(to_load typeB slot0 beluga25)
		(next_load dummy-type slot0 dummy-slot beluga25)
		; 0: typeB
		(to_load typeB slot0 beluga26)
		(next_load dummy-type slot0 dummy-slot beluga26)
		; 0: typeB
		(to_load typeB slot0 beluga27)
		(next_load dummy-type slot0 dummy-slot beluga27)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga28)
		(next_load typeA slot0 slot1 beluga28)
		(next_load typeA slot1 slot2 beluga28)
		(next_load typeA slot2 slot3 beluga28)
		(next_load dummy-type slot3 dummy-slot beluga28)
		; 0: typeC
		(to_load typeC slot0 beluga29)
		(next_load dummy-type slot0 dummy-slot beluga29)
		; 0: typeA
		(to_load typeA slot0 beluga30)
		(next_load dummy-type slot0 dummy-slot beluga30)
		; 0: typeA
		(to_load typeA slot0 beluga31)
		(next_load dummy-type slot0 dummy-slot beluga31)
		; 0: typeE
		(to_load typeE slot0 beluga32)
		(next_load dummy-type slot0 dummy-slot beluga32)
		; 0: typeC
		(to_load typeC slot0 beluga33)
		(next_load dummy-type slot0 dummy-slot beluga33)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga34)
		(next_load typeB slot0 slot1 beluga34)
		(next_load dummy-type slot1 dummy-slot beluga34)
		; 0: typeA
		(to_load typeA slot0 beluga35)
		(next_load dummy-type slot0 dummy-slot beluga35)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga36)
		(next_load typeC slot0 slot1 beluga36)
		(next_load dummy-type slot1 dummy-slot beluga36)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga37)
		(next_load typeC slot0 slot1 beluga37)
		(next_load dummy-type slot1 dummy-slot beluga37)
		; 0: typeA
		(to_load typeA slot0 beluga38)
		(next_load dummy-type slot0 dummy-slot beluga38)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga39)
		(next_load typeA slot0 slot1 beluga39)
		(next_load dummy-type slot1 dummy-slot beluga39)
		; 0: typeB
		(to_load typeB slot0 beluga40)
		(next_load dummy-type slot0 dummy-slot beluga40)
		; 0: typeC
		(to_load typeC slot0 beluga41)
		(next_load dummy-type slot0 dummy-slot beluga41)
		; No jigs
		(to_load dummy-type dummy-slot beluga42)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga43)
		(next_load typeB slot0 slot1 beluga43)
		(next_load dummy-type slot1 dummy-slot beluga43)
		; 0: typeD
		(to_load typeD slot0 beluga44)
		(next_load dummy-type slot0 dummy-slot beluga44)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga45)
		(next_load typeC slot0 slot1 beluga45)
		(next_load dummy-type slot1 dummy-slot beluga45)
		; 0: typeB
		(to_load typeB slot0 beluga46)
		(next_load dummy-type slot0 dummy-slot beluga46)
		; 0: typeB
		(to_load typeB slot0 beluga47)
		(next_load dummy-type slot0 dummy-slot beluga47)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga48)
		(next_load typeA slot0 slot1 beluga48)
		(next_load dummy-type slot1 dummy-slot beluga48)
		; 0: typeE
		(to_load typeE slot0 beluga49)
		(next_load dummy-type slot0 dummy-slot beluga49)
		; 0: typeC
		(to_load typeC slot0 beluga50)
		(next_load dummy-type slot0 dummy-slot beluga50)
		; No jigs
		(to_load dummy-type dummy-slot beluga51)
		; No jigs
		(to_load dummy-type dummy-slot beluga52)
		; 0: typeA
		(to_load typeA slot0 beluga53)
		(next_load dummy-type slot0 dummy-slot beluga53)
		; 0: typeA
		(to_load typeA slot0 beluga54)
		(next_load dummy-type slot0 dummy-slot beluga54)
		; 0: typeB 1: typeB 2: typeB 3: typeB 4: typeB
		(to_load typeB slot0 beluga55)
		(next_load typeB slot0 slot1 beluga55)
		(next_load typeB slot1 slot2 beluga55)
		(next_load typeB slot2 slot3 beluga55)
		(next_load typeB slot3 slot4 beluga55)
		(next_load dummy-type slot4 dummy-slot beluga55)
		; 0: typeA
		(to_load typeA slot0 beluga56)
		(next_load dummy-type slot0 dummy-slot beluga56)
		; 0: typeA
		(to_load typeA slot0 beluga57)
		(next_load dummy-type slot0 dummy-slot beluga57)
		; 0: typeE
		(to_load typeE slot0 beluga58)
		(next_load dummy-type slot0 dummy-slot beluga58)
		; Production schedule:
		; Production line: pl0
		; 0: jig0009 1: jig0019 2: jig0006 3: jig0023 4: jig0027 5: jig0003 6: jig0005 7: jig0013 8: jig0022 9: jig0018 10: jig0024 11: jig0008 12: jig0020 13: jig0029 14: jig0034 15: jig0030 16: jig0045 17: jig0047 18: jig0048 19: jig0050 20: jig0025 21: jig0026 22: jig0021 23: jig0028 24: jig0042 25: jig0031 26: jig0036 27: jig0044 28: jig0046 29: jig0032 30: jig0035 31: jig0039 32: jig0038 33: jig0058 34: jig0033 35: jig0041 36: jig0056 37: jig0053 38: jig0062 39: jig0063 40: jig0064 41: jig0040 42: jig0037 43: jig0043 44: jig0054 45: jig0057 46: jig0049 47: jig0051 48: jig0055 49: jig0059 50: jig0060 51: jig0061 52: jig0052 53: jig0068 54: jig0078 55: jig0072 56: jig0083 57: jig0066 58: jig0071 59: jig0086 60: jig0065 61: jig0067 62: jig0079 63: jig0080 64: jig0081 65: jig0085 66: jig0069 67: jig0088 68: jig0070 69: jig0075
		(to_deliver jig0009 pl0)
		(next_deliver jig0009 jig0019)
		(next_deliver jig0019 jig0006)
		(next_deliver jig0006 jig0023)
		(next_deliver jig0023 jig0027)
		(next_deliver jig0027 jig0003)
		(next_deliver jig0003 jig0005)
		(next_deliver jig0005 jig0013)
		(next_deliver jig0013 jig0022)
		(next_deliver jig0022 jig0018)
		(next_deliver jig0018 jig0024)
		(next_deliver jig0024 jig0008)
		(next_deliver jig0008 jig0020)
		(next_deliver jig0020 jig0029)
		(next_deliver jig0029 jig0034)
		(next_deliver jig0034 jig0030)
		(next_deliver jig0030 jig0045)
		(next_deliver jig0045 jig0047)
		(next_deliver jig0047 jig0048)
		(next_deliver jig0048 jig0050)
		(next_deliver jig0050 jig0025)
		(next_deliver jig0025 jig0026)
		(next_deliver jig0026 jig0021)
		(next_deliver jig0021 jig0028)
		(next_deliver jig0028 jig0042)
		(next_deliver jig0042 jig0031)
		(next_deliver jig0031 jig0036)
		(next_deliver jig0036 jig0044)
		(next_deliver jig0044 jig0046)
		(next_deliver jig0046 jig0032)
		(next_deliver jig0032 jig0035)
		(next_deliver jig0035 jig0039)
		(next_deliver jig0039 jig0038)
		(next_deliver jig0038 jig0058)
		(next_deliver jig0058 jig0033)
		(next_deliver jig0033 jig0041)
		(next_deliver jig0041 jig0056)
		(next_deliver jig0056 jig0053)
		(next_deliver jig0053 jig0062)
		(next_deliver jig0062 jig0063)
		(next_deliver jig0063 jig0064)
		(next_deliver jig0064 jig0040)
		(next_deliver jig0040 jig0037)
		(next_deliver jig0037 jig0043)
		(next_deliver jig0043 jig0054)
		(next_deliver jig0054 jig0057)
		(next_deliver jig0057 jig0049)
		(next_deliver jig0049 jig0051)
		(next_deliver jig0051 jig0055)
		(next_deliver jig0055 jig0059)
		(next_deliver jig0059 jig0060)
		(next_deliver jig0060 jig0061)
		(next_deliver jig0061 jig0052)
		(next_deliver jig0052 jig0068)
		(next_deliver jig0068 jig0078)
		(next_deliver jig0078 jig0072)
		(next_deliver jig0072 jig0083)
		(next_deliver jig0083 jig0066)
		(next_deliver jig0066 jig0071)
		(next_deliver jig0071 jig0086)
		(next_deliver jig0086 jig0065)
		(next_deliver jig0065 jig0067)
		(next_deliver jig0067 jig0079)
		(next_deliver jig0079 jig0080)
		(next_deliver jig0080 jig0081)
		(next_deliver jig0081 jig0085)
		(next_deliver jig0085 jig0069)
		(next_deliver jig0069 jig0088)
		(next_deliver jig0088 jig0070)
		(next_deliver jig0070 jig0075)
		(next_deliver jig0075 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0009)
		(empty jig0019)
		(empty jig0006)
		(empty jig0023)
		(empty jig0027)
		(empty jig0003)
		(empty jig0005)
		(empty jig0013)
		(empty jig0022)
		(empty jig0018)
		(empty jig0024)
		(empty jig0008)
		(empty jig0020)
		(empty jig0029)
		(empty jig0034)
		(empty jig0030)
		(empty jig0045)
		(empty jig0047)
		(empty jig0048)
		(empty jig0050)
		(empty jig0025)
		(empty jig0026)
		(empty jig0021)
		(empty jig0028)
		(empty jig0042)
		(empty jig0031)
		(empty jig0036)
		(empty jig0044)
		(empty jig0046)
		(empty jig0032)
		(empty jig0035)
		(empty jig0039)
		(empty jig0038)
		(empty jig0058)
		(empty jig0033)
		(empty jig0041)
		(empty jig0056)
		(empty jig0053)
		(empty jig0062)
		(empty jig0063)
		(empty jig0064)
		(empty jig0040)
		(empty jig0037)
		(empty jig0043)
		(empty jig0054)
		(empty jig0057)
		(empty jig0049)
		(empty jig0051)
		(empty jig0055)
		(empty jig0059)
		(empty jig0060)
		(empty jig0061)
		(empty jig0052)
		(empty jig0068)
		(empty jig0078)
		(empty jig0072)
		(empty jig0083)
		(empty jig0066)
		(empty jig0071)
		(empty jig0086)
		(empty jig0065)
		(empty jig0067)
		(empty jig0079)
		(empty jig0080)
		(empty jig0081)
		(empty jig0085)
		(empty jig0069)
		(empty jig0088)
		(empty jig0070)
		(empty jig0075)
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
		(to_unload dummy-jig beluga44)
		(to_unload dummy-jig beluga45)
		(to_unload dummy-jig beluga46)
		(to_unload dummy-jig beluga47)
		(to_unload dummy-jig beluga48)
		(to_unload dummy-jig beluga49)
		(to_unload dummy-jig beluga50)
		(to_unload dummy-jig beluga51)
		(to_unload dummy-jig beluga52)
		(to_unload dummy-jig beluga53)
		(to_unload dummy-jig beluga54)
		(to_unload dummy-jig beluga55)
		(to_unload dummy-jig beluga56)
		(to_unload dummy-jig beluga57)
		(to_unload dummy-jig beluga58)
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
		(to_load dummy-type dummy-slot beluga44)
		(to_load dummy-type dummy-slot beluga45)
		(to_load dummy-type dummy-slot beluga46)
		(to_load dummy-type dummy-slot beluga47)
		(to_load dummy-type dummy-slot beluga48)
		(to_load dummy-type dummy-slot beluga49)
		(to_load dummy-type dummy-slot beluga50)
		(to_load dummy-type dummy-slot beluga51)
		(to_load dummy-type dummy-slot beluga52)
		(to_load dummy-type dummy-slot beluga53)
		(to_load dummy-type dummy-slot beluga54)
		(to_load dummy-type dummy-slot beluga55)
		(to_load dummy-type dummy-slot beluga56)
		(to_load dummy-type dummy-slot beluga57)
		(to_load dummy-type dummy-slot beluga58)
	))
  (:metric minimize (total-cost))
)