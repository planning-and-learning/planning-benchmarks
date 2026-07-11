(define
	(problem beluga-problem_266_s309_j83_r7_oc80_f35)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 36, 40}
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
		n31 - num
		n32 - num
		n33 - num
		n36 - num
		n40 - num
		; trailers:
		beluga_trailer_1 - trailer
		factory_trailer_1 - trailer
		; Racks:
		rack00 - rack
		rack01 - rack
		rack02 - rack
		rack03 - rack
		rack04 - rack
		rack05 - rack
		rack06 - rack
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
		beluga35 - beluga
		; Slots for outgoing flights:
		slot0 - slot
		slot1 - slot
		slot2 - slot
		slot3 - slot
		slot4 - slot
		slot5 - slot
		slot6 - slot
		slot7 - slot
		slot8 - slot
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
		(fit  n18  n04  n22 rack01)
		(fit  n14  n08  n22 rack01)
		(fit  n13  n09  n22 rack01)
		(fit  n11  n11  n22 rack01)
		(fit  n04  n18  n22 rack01)
		(fit  n20  n04  n24 rack01)
		(fit  n16  n08  n24 rack01)
		(fit  n15  n09  n24 rack01)
		(fit  n13  n11  n24 rack01)
		(fit  n06  n18  n24 rack01)
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
		(fit  n01  n32  n33 rack01)
		(fit  n29  n04  n33 rack01)
		(fit  n25  n08  n33 rack01)
		(fit  n24  n09  n33 rack01)
		(fit  n22  n11  n33 rack01)
		(fit  n15  n18  n33 rack01)
		(fit  n08  n25  n33 rack01)
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
		(fit  n23  n04  n27 rack02)
		(fit  n19  n08  n27 rack02)
		(fit  n18  n09  n27 rack02)
		(fit  n16  n11  n27 rack02)
		(fit  n09  n18  n27 rack02)
		(fit  n02  n25  n27 rack02)
		(fit  n27  n04  n31 rack02)
		(fit  n23  n08  n31 rack02)
		(fit  n22  n09  n31 rack02)
		(fit  n20  n11  n31 rack02)
		(fit  n13  n18  n31 rack02)
		(fit  n06  n25  n31 rack02)
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
		(fit  n13  n04  n17 rack03)
		(fit  n09  n08  n17 rack03)
		(fit  n08  n09  n17 rack03)
		(fit  n06  n11  n17 rack03)
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
		(fit  n22  n04  n26 rack03)
		(fit  n18  n08  n26 rack03)
		(fit  n17  n09  n26 rack03)
		(fit  n15  n11  n26 rack03)
		(fit  n08  n18  n26 rack03)
		(fit  n01  n25  n26 rack03)
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
		(fit  n20  n04  n24 rack04)
		(fit  n16  n08  n24 rack04)
		(fit  n15  n09  n24 rack04)
		(fit  n13  n11  n24 rack04)
		(fit  n06  n18  n24 rack04)
		(fit  n21  n04  n25 rack04)
		(fit  n17  n08  n25 rack04)
		(fit  n16  n09  n25 rack04)
		(fit  n14  n11  n25 rack04)
		(fit  n07  n18  n25 rack04)
		(fit  n00  n25  n25 rack04)
		(fit  n23  n04  n27 rack04)
		(fit  n19  n08  n27 rack04)
		(fit  n18  n09  n27 rack04)
		(fit  n16  n11  n27 rack04)
		(fit  n09  n18  n27 rack04)
		(fit  n02  n25  n27 rack04)
		(fit  n24  n04  n28 rack04)
		(fit  n20  n08  n28 rack04)
		(fit  n19  n09  n28 rack04)
		(fit  n17  n11  n28 rack04)
		(fit  n10  n18  n28 rack04)
		(fit  n03  n25  n28 rack04)
		(fit  n25  n04  n29 rack04)
		(fit  n21  n08  n29 rack04)
		(fit  n20  n09  n29 rack04)
		(fit  n18  n11  n29 rack04)
		(fit  n11  n18  n29 rack04)
		(fit  n04  n25  n29 rack04)
		(fit  n27  n04  n31 rack04)
		(fit  n23  n08  n31 rack04)
		(fit  n22  n09  n31 rack04)
		(fit  n20  n11  n31 rack04)
		(fit  n13  n18  n31 rack04)
		(fit  n06  n25  n31 rack04)
		(fit  n00  n32  n32 rack04)
		(fit  n28  n04  n32 rack04)
		(fit  n24  n08  n32 rack04)
		(fit  n23  n09  n32 rack04)
		(fit  n21  n11  n32 rack04)
		(fit  n14  n18  n32 rack04)
		(fit  n07  n25  n32 rack04)
		(fit  n04  n32  n36 rack04)
		(fit  n32  n04  n36 rack04)
		(fit  n28  n08  n36 rack04)
		(fit  n27  n09  n36 rack04)
		(fit  n25  n11  n36 rack04)
		(fit  n18  n18  n36 rack04)
		(fit  n11  n25  n36 rack04)
		(fit  n08  n32  n40 rack04)
		(fit  n36  n04  n40 rack04)
		(fit  n32  n08  n40 rack04)
		(fit  n31  n09  n40 rack04)
		(fit  n29  n11  n40 rack04)
		(fit  n22  n18  n40 rack04)
		(fit  n15  n25  n40 rack04)
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
		(fit  n11  n04  n15 rack05)
		(fit  n07  n08  n15 rack05)
		(fit  n06  n09  n15 rack05)
		(fit  n04  n11  n15 rack05)
		(fit  n12  n04  n16 rack05)
		(fit  n08  n08  n16 rack05)
		(fit  n07  n09  n16 rack05)
		(fit  n05  n11  n16 rack05)
		(fit  n16  n04  n20 rack05)
		(fit  n12  n08  n20 rack05)
		(fit  n11  n09  n20 rack05)
		(fit  n09  n11  n20 rack05)
		(fit  n02  n18  n20 rack05)
		(fit  n20  n04  n24 rack05)
		(fit  n16  n08  n24 rack05)
		(fit  n15  n09  n24 rack05)
		(fit  n13  n11  n24 rack05)
		(fit  n06  n18  n24 rack05)
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
		(fit  n06  n04  n10 rack06)
		(fit  n02  n08  n10 rack06)
		(fit  n01  n09  n10 rack06)
		(fit  n07  n04  n11 rack06)
		(fit  n03  n08  n11 rack06)
		(fit  n02  n09  n11 rack06)
		(fit  n00  n11  n11 rack06)
		(fit  n09  n04  n13 rack06)
		(fit  n05  n08  n13 rack06)
		(fit  n04  n09  n13 rack06)
		(fit  n02  n11  n13 rack06)
		(fit  n10  n04  n14 rack06)
		(fit  n06  n08  n14 rack06)
		(fit  n05  n09  n14 rack06)
		(fit  n03  n11  n14 rack06)
		(fit  n11  n04  n15 rack06)
		(fit  n07  n08  n15 rack06)
		(fit  n06  n09  n15 rack06)
		(fit  n04  n11  n15 rack06)
		(fit  n13  n04  n17 rack06)
		(fit  n09  n08  n17 rack06)
		(fit  n08  n09  n17 rack06)
		(fit  n06  n11  n17 rack06)
		(fit  n14  n04  n18 rack06)
		(fit  n10  n08  n18 rack06)
		(fit  n09  n09  n18 rack06)
		(fit  n07  n11  n18 rack06)
		(fit  n00  n18  n18 rack06)
		(fit  n18  n04  n22 rack06)
		(fit  n14  n08  n22 rack06)
		(fit  n13  n09  n22 rack06)
		(fit  n11  n11  n22 rack06)
		(fit  n04  n18  n22 rack06)
		(fit  n22  n04  n26 rack06)
		(fit  n18  n08  n26 rack06)
		(fit  n17  n09  n26 rack06)
		(fit  n15  n11  n26 rack06)
		(fit  n08  n18  n26 rack06)
		(fit  n01  n25  n26 rack06)
		; trailers (Beluga side):
		(empty beluga_trailer_1)
		(at-side beluga_trailer_1 bside)
		; trailers (Factory side):
		(empty factory_trailer_1)
		(at-side factory_trailer_1 fside)
		; Racks 7
		; Rack:rack00
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n06)
		(in jig0011 rack00)
		(clear jig0011 bside)
		(next-to jig0011 jig0012 bside)
		(next-to jig0012 jig0011 fside)
		(in jig0012 rack00)
		(clear jig0012 fside)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n06)
		(in jig0008 rack01)
		(clear jig0008 bside)
		(next-to jig0008 jig0002 bside)
		(next-to jig0002 jig0008 fside)
		(in jig0002 rack01)
		(clear jig0002 fside)
		; Rack:rack02
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n02)
		(in jig0003 rack02)
		(clear jig0003 bside)
		(next-to jig0003 jig0009 bside)
		(next-to jig0009 jig0003 fside)
		(in jig0009 rack02)
		(clear jig0009 fside)
		; Rack:rack03
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n06)
		(in jig0006 rack03)
		(clear jig0006 bside)
		(next-to jig0006 jig0007 bside)
		(next-to jig0007 jig0006 fside)
		(in jig0007 rack03)
		(clear jig0007 fside)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n04)
		(in jig0001 rack04)
		(clear jig0001 bside)
		(next-to jig0001 jig0005 bside)
		(next-to jig0005 jig0001 fside)
		(in jig0005 rack04)
		(clear jig0005 fside)
		; Rack:rack05
		(at-side rack05 bside)
		(at-side rack05 fside)
		(free-space rack05 n06)
		(in jig0004 rack05)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack06
		(at-side rack06 bside)
		(at-side rack06 fside)
		(free-space rack06 n08)
		(in jig0010 rack06)
		(clear jig0010 bside)
		(clear jig0010 fside)
		; Jigs (size):
		(is_type jig0001 typeB)
		(size jig0001 n11)
		(empty-size jig0001 n08)
		(is_type jig0002 typeC)
		(size jig0002 n18)
		(empty-size jig0002 n09)
		(is_type jig0003 typeB)
		(size jig0003 n11)
		(empty-size jig0003 n08)
		(is_type jig0004 typeC)
		(size jig0004 n18)
		(empty-size jig0004 n09)
		(is_type jig0005 typeD)
		(size jig0005 n25)
		(empty-size jig0005 n18)
		(is_type jig0006 typeC)
		(size jig0006 n09)
		(empty-size jig0006 n09)
		(empty jig0006)
		(is_type jig0007 typeB)
		(size jig0007 n11)
		(empty-size jig0007 n08)
		(is_type jig0008 typeC)
		(size jig0008 n09)
		(empty-size jig0008 n09)
		(empty jig0008)
		(is_type jig0009 typeC)
		(size jig0009 n18)
		(empty-size jig0009 n09)
		(is_type jig0010 typeC)
		(size jig0010 n18)
		(empty-size jig0010 n09)
		(is_type jig0011 typeB)
		(size jig0011 n08)
		(empty-size jig0011 n08)
		(empty jig0011)
		(is_type jig0012 typeB)
		(size jig0012 n11)
		(empty-size jig0012 n08)
		(is_type jig0013 typeC)
		(size jig0013 n18)
		(empty-size jig0013 n09)
		(is_type jig0014 typeD)
		(size jig0014 n25)
		(empty-size jig0014 n18)
		(is_type jig0015 typeD)
		(size jig0015 n25)
		(empty-size jig0015 n18)
		(is_type jig0016 typeC)
		(size jig0016 n18)
		(empty-size jig0016 n09)
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
		(is_type jig0028 typeB)
		(size jig0028 n11)
		(empty-size jig0028 n08)
		(is_type jig0029 typeB)
		(size jig0029 n11)
		(empty-size jig0029 n08)
		(is_type jig0030 typeD)
		(size jig0030 n25)
		(empty-size jig0030 n18)
		(is_type jig0031 typeC)
		(size jig0031 n18)
		(empty-size jig0031 n09)
		(is_type jig0032 typeB)
		(size jig0032 n11)
		(empty-size jig0032 n08)
		(is_type jig0033 typeB)
		(size jig0033 n11)
		(empty-size jig0033 n08)
		(is_type jig0034 typeA)
		(size jig0034 n04)
		(empty-size jig0034 n04)
		(is_type jig0035 typeA)
		(size jig0035 n04)
		(empty-size jig0035 n04)
		(is_type jig0036 typeA)
		(size jig0036 n04)
		(empty-size jig0036 n04)
		(is_type jig0037 typeB)
		(size jig0037 n11)
		(empty-size jig0037 n08)
		(is_type jig0038 typeB)
		(size jig0038 n11)
		(empty-size jig0038 n08)
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
		(is_type jig0047 typeB)
		(size jig0047 n11)
		(empty-size jig0047 n08)
		(is_type jig0048 typeB)
		(size jig0048 n11)
		(empty-size jig0048 n08)
		(is_type jig0049 typeB)
		(size jig0049 n11)
		(empty-size jig0049 n08)
		(is_type jig0050 typeA)
		(size jig0050 n04)
		(empty-size jig0050 n04)
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
		(is_type jig0056 typeB)
		(size jig0056 n11)
		(empty-size jig0056 n08)
		(is_type jig0057 typeD)
		(size jig0057 n25)
		(empty-size jig0057 n18)
		(is_type jig0058 typeA)
		(size jig0058 n04)
		(empty-size jig0058 n04)
		(is_type jig0059 typeA)
		(size jig0059 n04)
		(empty-size jig0059 n04)
		(is_type jig0060 typeA)
		(size jig0060 n04)
		(empty-size jig0060 n04)
		(is_type jig0061 typeA)
		(size jig0061 n04)
		(empty-size jig0061 n04)
		(is_type jig0062 typeA)
		(size jig0062 n04)
		(empty-size jig0062 n04)
		(is_type jig0063 typeA)
		(size jig0063 n04)
		(empty-size jig0063 n04)
		(is_type jig0064 typeA)
		(size jig0064 n04)
		(empty-size jig0064 n04)
		(is_type jig0065 typeA)
		(size jig0065 n04)
		(empty-size jig0065 n04)
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
		(is_type jig0076 typeA)
		(size jig0076 n04)
		(empty-size jig0076 n04)
		(is_type jig0077 typeA)
		(size jig0077 n04)
		(empty-size jig0077 n04)
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
		(is_type jig0083 typeB)
		(size jig0083 n11)
		(empty-size jig0083 n08)
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
		(next-flight-to-process beluga34 beluga35)
		; Number of flights: 35
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; No jigs
		(to_unload dummy-jig beluga1)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0013
		(to_unload jig0013 beluga2)
		(in jig0013 beluga2)
		(next_unload jig0013 dummy-jig)
		; Flight: beluga3
		; 0: jig0014
		(to_unload jig0014 beluga3)
		(in jig0014 beluga3)
		(next_unload jig0014 dummy-jig)
		; Flight: beluga4
		; No jigs
		(to_unload dummy-jig beluga4)
		; Flight: beluga5
		; No jigs
		(to_unload dummy-jig beluga5)
		; Flight: beluga6
		; No jigs
		(to_unload dummy-jig beluga6)
		; Flight: beluga7
		; 0: jig0015
		(to_unload jig0015 beluga7)
		(in jig0015 beluga7)
		(next_unload jig0015 dummy-jig)
		; Flight: beluga8
		; 0: jig0016 1: jig0017
		(to_unload jig0016 beluga8)
		(in jig0016 beluga8)
		(next_unload jig0016 jig0017)
		(in jig0017 beluga8)
		(next_unload jig0017 dummy-jig)
		; Flight: beluga9
		; 0: jig0018 1: jig0019 2: jig0020 3: jig0021 4: jig0022 5: jig0023 6: jig0024 7: jig0025 8: jig0026 9: jig0027
		(to_unload jig0018 beluga9)
		(in jig0018 beluga9)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga9)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga9)
		(next_unload jig0020 jig0021)
		(in jig0021 beluga9)
		(next_unload jig0021 jig0022)
		(in jig0022 beluga9)
		(next_unload jig0022 jig0023)
		(in jig0023 beluga9)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga9)
		(next_unload jig0024 jig0025)
		(in jig0025 beluga9)
		(next_unload jig0025 jig0026)
		(in jig0026 beluga9)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga9)
		(next_unload jig0027 dummy-jig)
		; Flight: beluga10
		; 0: jig0028 1: jig0029
		(to_unload jig0028 beluga10)
		(in jig0028 beluga10)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga10)
		(next_unload jig0029 dummy-jig)
		; Flight: beluga11
		; No jigs
		(to_unload dummy-jig beluga11)
		; Flight: beluga12
		; No jigs
		(to_unload dummy-jig beluga12)
		; Flight: beluga13
		; 0: jig0030
		(to_unload jig0030 beluga13)
		(in jig0030 beluga13)
		(next_unload jig0030 dummy-jig)
		; Flight: beluga14
		; 0: jig0031
		(to_unload jig0031 beluga14)
		(in jig0031 beluga14)
		(next_unload jig0031 dummy-jig)
		; Flight: beluga15
		; 0: jig0032 1: jig0033
		(to_unload jig0032 beluga15)
		(in jig0032 beluga15)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga15)
		(next_unload jig0033 dummy-jig)
		; Flight: beluga16
		; 0: jig0034 1: jig0035
		(to_unload jig0034 beluga16)
		(in jig0034 beluga16)
		(next_unload jig0034 jig0035)
		(in jig0035 beluga16)
		(next_unload jig0035 dummy-jig)
		; Flight: beluga17
		; 0: jig0036
		(to_unload jig0036 beluga17)
		(in jig0036 beluga17)
		(next_unload jig0036 dummy-jig)
		; Flight: beluga18
		; 0: jig0037 1: jig0038
		(to_unload jig0037 beluga18)
		(in jig0037 beluga18)
		(next_unload jig0037 jig0038)
		(in jig0038 beluga18)
		(next_unload jig0038 dummy-jig)
		; Flight: beluga19
		; No jigs
		(to_unload dummy-jig beluga19)
		; Flight: beluga20
		; 0: jig0039 1: jig0040 2: jig0041 3: jig0042 4: jig0043 5: jig0044 6: jig0045 7: jig0046
		(to_unload jig0039 beluga20)
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
		(next_unload jig0045 jig0046)
		(in jig0046 beluga20)
		(next_unload jig0046 dummy-jig)
		; Flight: beluga21
		; No jigs
		(to_unload dummy-jig beluga21)
		; Flight: beluga22
		; 0: jig0047 1: jig0048 2: jig0049
		(to_unload jig0047 beluga22)
		(in jig0047 beluga22)
		(next_unload jig0047 jig0048)
		(in jig0048 beluga22)
		(next_unload jig0048 jig0049)
		(in jig0049 beluga22)
		(next_unload jig0049 dummy-jig)
		; Flight: beluga23
		; 0: jig0050 1: jig0051 2: jig0052 3: jig0053 4: jig0054 5: jig0055
		(to_unload jig0050 beluga23)
		(in jig0050 beluga23)
		(next_unload jig0050 jig0051)
		(in jig0051 beluga23)
		(next_unload jig0051 jig0052)
		(in jig0052 beluga23)
		(next_unload jig0052 jig0053)
		(in jig0053 beluga23)
		(next_unload jig0053 jig0054)
		(in jig0054 beluga23)
		(next_unload jig0054 jig0055)
		(in jig0055 beluga23)
		(next_unload jig0055 dummy-jig)
		; Flight: beluga24
		; 0: jig0056
		(to_unload jig0056 beluga24)
		(in jig0056 beluga24)
		(next_unload jig0056 dummy-jig)
		; Flight: beluga25
		; No jigs
		(to_unload dummy-jig beluga25)
		; Flight: beluga26
		; 0: jig0057
		(to_unload jig0057 beluga26)
		(in jig0057 beluga26)
		(next_unload jig0057 dummy-jig)
		; Flight: beluga27
		; No jigs
		(to_unload dummy-jig beluga27)
		; Flight: beluga28
		; 0: jig0058 1: jig0059 2: jig0060 3: jig0061 4: jig0062 5: jig0063 6: jig0064 7: jig0065 8: jig0066 9: jig0067
		(to_unload jig0058 beluga28)
		(in jig0058 beluga28)
		(next_unload jig0058 jig0059)
		(in jig0059 beluga28)
		(next_unload jig0059 jig0060)
		(in jig0060 beluga28)
		(next_unload jig0060 jig0061)
		(in jig0061 beluga28)
		(next_unload jig0061 jig0062)
		(in jig0062 beluga28)
		(next_unload jig0062 jig0063)
		(in jig0063 beluga28)
		(next_unload jig0063 jig0064)
		(in jig0064 beluga28)
		(next_unload jig0064 jig0065)
		(in jig0065 beluga28)
		(next_unload jig0065 jig0066)
		(in jig0066 beluga28)
		(next_unload jig0066 jig0067)
		(in jig0067 beluga28)
		(next_unload jig0067 dummy-jig)
		; Flight: beluga29
		; 0: jig0068 1: jig0069 2: jig0070 3: jig0071 4: jig0072 5: jig0073 6: jig0074 7: jig0075 8: jig0076 9: jig0077
		(to_unload jig0068 beluga29)
		(in jig0068 beluga29)
		(next_unload jig0068 jig0069)
		(in jig0069 beluga29)
		(next_unload jig0069 jig0070)
		(in jig0070 beluga29)
		(next_unload jig0070 jig0071)
		(in jig0071 beluga29)
		(next_unload jig0071 jig0072)
		(in jig0072 beluga29)
		(next_unload jig0072 jig0073)
		(in jig0073 beluga29)
		(next_unload jig0073 jig0074)
		(in jig0074 beluga29)
		(next_unload jig0074 jig0075)
		(in jig0075 beluga29)
		(next_unload jig0075 jig0076)
		(in jig0076 beluga29)
		(next_unload jig0076 jig0077)
		(in jig0077 beluga29)
		(next_unload jig0077 dummy-jig)
		; Flight: beluga30
		; 0: jig0078 1: jig0079 2: jig0080
		(to_unload jig0078 beluga30)
		(in jig0078 beluga30)
		(next_unload jig0078 jig0079)
		(in jig0079 beluga30)
		(next_unload jig0079 jig0080)
		(in jig0080 beluga30)
		(next_unload jig0080 dummy-jig)
		; Flight: beluga31
		; 0: jig0081
		(to_unload jig0081 beluga31)
		(in jig0081 beluga31)
		(next_unload jig0081 dummy-jig)
		; Flight: beluga32
		; No jigs
		(to_unload dummy-jig beluga32)
		; Flight: beluga33
		; 0: jig0082
		(to_unload jig0082 beluga33)
		(in jig0082 beluga33)
		(next_unload jig0082 dummy-jig)
		; Flight: beluga34
		; 0: jig0083
		(to_unload jig0083 beluga34)
		(in jig0083 beluga34)
		(next_unload jig0083 dummy-jig)
		; Flight: beluga35
		; No jigs
		(to_unload dummy-jig beluga35)
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
		; 0: typeB
		(to_load typeB slot0 beluga3)
		(next_load dummy-type slot0 dummy-slot beluga3)
		; 0: typeC
		(to_load typeC slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; 0: typeD
		(to_load typeD slot0 beluga5)
		(next_load dummy-type slot0 dummy-slot beluga5)
		; 0: typeC
		(to_load typeC slot0 beluga6)
		(next_load dummy-type slot0 dummy-slot beluga6)
		; 0: typeD
		(to_load typeD slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; No jigs
		(to_load dummy-type dummy-slot beluga8)
		; 0: typeC
		(to_load typeC slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeB
		(to_load typeB slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeA
		(to_load typeA slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeC
		(to_load typeC slot0 beluga12)
		(next_load dummy-type slot0 dummy-slot beluga12)
		; 0: typeB
		(to_load typeB slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeC
		(to_load typeC slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeA
		(to_load typeA slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeA
		(to_load typeA slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga17)
		(next_load typeB slot0 slot1 beluga17)
		(next_load dummy-type slot1 dummy-slot beluga17)
		; 0: typeD
		(to_load typeD slot0 beluga18)
		(next_load dummy-type slot0 dummy-slot beluga18)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga19)
		(next_load typeA slot0 slot1 beluga19)
		(next_load typeA slot1 slot2 beluga19)
		(next_load typeA slot2 slot3 beluga19)
		(next_load dummy-type slot3 dummy-slot beluga19)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga20)
		(next_load typeA slot0 slot1 beluga20)
		(next_load dummy-type slot1 dummy-slot beluga20)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga21)
		(next_load typeB slot0 slot1 beluga21)
		(next_load dummy-type slot1 dummy-slot beluga21)
		; 0: typeD
		(to_load typeD slot0 beluga22)
		(next_load dummy-type slot0 dummy-slot beluga22)
		; 0: typeB
		(to_load typeB slot0 beluga23)
		(next_load dummy-type slot0 dummy-slot beluga23)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga24)
		(next_load typeB slot0 slot1 beluga24)
		(next_load dummy-type slot1 dummy-slot beluga24)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga25)
		(next_load typeC slot0 slot1 beluga25)
		(next_load dummy-type slot1 dummy-slot beluga25)
		; 0: typeC
		(to_load typeC slot0 beluga26)
		(next_load dummy-type slot0 dummy-slot beluga26)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA 7: typeA 8: typeA
		(to_load typeA slot0 beluga27)
		(next_load typeA slot0 slot1 beluga27)
		(next_load typeA slot1 slot2 beluga27)
		(next_load typeA slot2 slot3 beluga27)
		(next_load typeA slot3 slot4 beluga27)
		(next_load typeA slot4 slot5 beluga27)
		(next_load typeA slot5 slot6 beluga27)
		(next_load typeA slot6 slot7 beluga27)
		(next_load typeA slot7 slot8 beluga27)
		(next_load dummy-type slot8 dummy-slot beluga27)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga28)
		(next_load typeB slot0 slot1 beluga28)
		(next_load dummy-type slot1 dummy-slot beluga28)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga29)
		(next_load typeA slot0 slot1 beluga29)
		(next_load typeA slot1 slot2 beluga29)
		(next_load typeA slot2 slot3 beluga29)
		(next_load dummy-type slot3 dummy-slot beluga29)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga30)
		(next_load typeA slot0 slot1 beluga30)
		(next_load dummy-type slot1 dummy-slot beluga30)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga31)
		(next_load typeA slot0 slot1 beluga31)
		(next_load dummy-type slot1 dummy-slot beluga31)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga32)
		(next_load typeA slot0 slot1 beluga32)
		(next_load dummy-type slot1 dummy-slot beluga32)
		; 0: typeB
		(to_load typeB slot0 beluga33)
		(next_load dummy-type slot0 dummy-slot beluga33)
		; 0: typeB
		(to_load typeB slot0 beluga34)
		(next_load dummy-type slot0 dummy-slot beluga34)
		; 0: typeD
		(to_load typeD slot0 beluga35)
		(next_load dummy-type slot0 dummy-slot beluga35)
		; Production schedule:
		; Production line: pl0
		; 0: jig0001 1: jig0010 2: jig0014 3: jig0012 4: jig0004 5: jig0009 6: jig0029 7: jig0015 8: jig0018 9: jig0025 10: jig0021 11: jig0024 12: jig0037 13: jig0017 14: jig0038 15: jig0028 16: jig0044 17: jig0046 18: jig0043 19: jig0049 20: jig0034 21: jig0050 22: jig0040 23: jig0035 24: jig0042 25: jig0041 26: jig0048 27: jig0057 28: jig0064 29: jig0067 30: jig0071 31: jig0078 32: jig0060 33: jig0082
		(to_deliver jig0001 pl0)
		(next_deliver jig0001 jig0010)
		(next_deliver jig0010 jig0014)
		(next_deliver jig0014 jig0012)
		(next_deliver jig0012 jig0004)
		(next_deliver jig0004 jig0009)
		(next_deliver jig0009 jig0029)
		(next_deliver jig0029 jig0015)
		(next_deliver jig0015 jig0018)
		(next_deliver jig0018 jig0025)
		(next_deliver jig0025 jig0021)
		(next_deliver jig0021 jig0024)
		(next_deliver jig0024 jig0037)
		(next_deliver jig0037 jig0017)
		(next_deliver jig0017 jig0038)
		(next_deliver jig0038 jig0028)
		(next_deliver jig0028 jig0044)
		(next_deliver jig0044 jig0046)
		(next_deliver jig0046 jig0043)
		(next_deliver jig0043 jig0049)
		(next_deliver jig0049 jig0034)
		(next_deliver jig0034 jig0050)
		(next_deliver jig0050 jig0040)
		(next_deliver jig0040 jig0035)
		(next_deliver jig0035 jig0042)
		(next_deliver jig0042 jig0041)
		(next_deliver jig0041 jig0048)
		(next_deliver jig0048 jig0057)
		(next_deliver jig0057 jig0064)
		(next_deliver jig0064 jig0067)
		(next_deliver jig0067 jig0071)
		(next_deliver jig0071 jig0078)
		(next_deliver jig0078 jig0060)
		(next_deliver jig0060 jig0082)
		(next_deliver jig0082 dummy-jig)
		; Production line: pl1
		; 0: jig0005 1: jig0002 2: jig0013 3: jig0026 4: jig0007 5: jig0023 6: jig0003 7: jig0022 8: jig0020 9: jig0032 10: jig0030 11: jig0027 12: jig0016 13: jig0019 14: jig0039 15: jig0033 16: jig0045 17: jig0036 18: jig0031 19: jig0054 20: jig0047 21: jig0055 22: jig0053 23: jig0052 24: jig0063 25: jig0051 26: jig0056 27: jig0058 28: jig0065 29: jig0059 30: jig0076 31: jig0079 32: jig0081
		(to_deliver jig0005 pl1)
		(next_deliver jig0005 jig0002)
		(next_deliver jig0002 jig0013)
		(next_deliver jig0013 jig0026)
		(next_deliver jig0026 jig0007)
		(next_deliver jig0007 jig0023)
		(next_deliver jig0023 jig0003)
		(next_deliver jig0003 jig0022)
		(next_deliver jig0022 jig0020)
		(next_deliver jig0020 jig0032)
		(next_deliver jig0032 jig0030)
		(next_deliver jig0030 jig0027)
		(next_deliver jig0027 jig0016)
		(next_deliver jig0016 jig0019)
		(next_deliver jig0019 jig0039)
		(next_deliver jig0039 jig0033)
		(next_deliver jig0033 jig0045)
		(next_deliver jig0045 jig0036)
		(next_deliver jig0036 jig0031)
		(next_deliver jig0031 jig0054)
		(next_deliver jig0054 jig0047)
		(next_deliver jig0047 jig0055)
		(next_deliver jig0055 jig0053)
		(next_deliver jig0053 jig0052)
		(next_deliver jig0052 jig0063)
		(next_deliver jig0063 jig0051)
		(next_deliver jig0051 jig0056)
		(next_deliver jig0056 jig0058)
		(next_deliver jig0058 jig0065)
		(next_deliver jig0065 jig0059)
		(next_deliver jig0059 jig0076)
		(next_deliver jig0076 jig0079)
		(next_deliver jig0079 jig0081)
		(next_deliver jig0081 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0001)
		(empty jig0010)
		(empty jig0014)
		(empty jig0012)
		(empty jig0004)
		(empty jig0009)
		(empty jig0029)
		(empty jig0015)
		(empty jig0018)
		(empty jig0025)
		(empty jig0021)
		(empty jig0024)
		(empty jig0037)
		(empty jig0017)
		(empty jig0038)
		(empty jig0028)
		(empty jig0044)
		(empty jig0046)
		(empty jig0043)
		(empty jig0049)
		(empty jig0034)
		(empty jig0050)
		(empty jig0040)
		(empty jig0035)
		(empty jig0042)
		(empty jig0041)
		(empty jig0048)
		(empty jig0057)
		(empty jig0064)
		(empty jig0067)
		(empty jig0071)
		(empty jig0078)
		(empty jig0060)
		(empty jig0082)
		(empty jig0005)
		(empty jig0002)
		(empty jig0013)
		(empty jig0026)
		(empty jig0007)
		(empty jig0023)
		(empty jig0003)
		(empty jig0022)
		(empty jig0020)
		(empty jig0032)
		(empty jig0030)
		(empty jig0027)
		(empty jig0016)
		(empty jig0019)
		(empty jig0039)
		(empty jig0033)
		(empty jig0045)
		(empty jig0036)
		(empty jig0031)
		(empty jig0054)
		(empty jig0047)
		(empty jig0055)
		(empty jig0053)
		(empty jig0052)
		(empty jig0063)
		(empty jig0051)
		(empty jig0056)
		(empty jig0058)
		(empty jig0065)
		(empty jig0059)
		(empty jig0076)
		(empty jig0079)
		(empty jig0081)
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
	))
  (:metric minimize (total-cost))
)