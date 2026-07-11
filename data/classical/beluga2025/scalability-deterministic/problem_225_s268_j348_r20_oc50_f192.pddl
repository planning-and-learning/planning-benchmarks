(define
	(problem beluga-problem_225_s268_j348_r20_oc50_f192)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 38}
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
		n35 - num
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
		rack04 - rack
		rack05 - rack
		rack06 - rack
		rack07 - rack
		rack08 - rack
		rack09 - rack
		rack10 - rack
		rack11 - rack
		rack12 - rack
		rack13 - rack
		rack14 - rack
		rack15 - rack
		rack16 - rack
		rack17 - rack
		rack18 - rack
		rack19 - rack
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
		jig0093 - jig
		jig0094 - jig
		jig0095 - jig
		jig0096 - jig
		jig0097 - jig
		jig0098 - jig
		jig0099 - jig
		jig0100 - jig
		jig0101 - jig
		jig0102 - jig
		jig0103 - jig
		jig0104 - jig
		jig0105 - jig
		jig0106 - jig
		jig0107 - jig
		jig0108 - jig
		jig0109 - jig
		jig0110 - jig
		jig0111 - jig
		jig0112 - jig
		jig0113 - jig
		jig0114 - jig
		jig0115 - jig
		jig0116 - jig
		jig0117 - jig
		jig0118 - jig
		jig0119 - jig
		jig0120 - jig
		jig0121 - jig
		jig0122 - jig
		jig0123 - jig
		jig0124 - jig
		jig0125 - jig
		jig0126 - jig
		jig0127 - jig
		jig0128 - jig
		jig0129 - jig
		jig0130 - jig
		jig0131 - jig
		jig0132 - jig
		jig0133 - jig
		jig0134 - jig
		jig0135 - jig
		jig0136 - jig
		jig0137 - jig
		jig0138 - jig
		jig0139 - jig
		jig0140 - jig
		jig0141 - jig
		jig0142 - jig
		jig0143 - jig
		jig0144 - jig
		jig0145 - jig
		jig0146 - jig
		jig0147 - jig
		jig0148 - jig
		jig0149 - jig
		jig0150 - jig
		jig0151 - jig
		jig0152 - jig
		jig0153 - jig
		jig0154 - jig
		jig0155 - jig
		jig0156 - jig
		jig0157 - jig
		jig0158 - jig
		jig0159 - jig
		jig0160 - jig
		jig0161 - jig
		jig0162 - jig
		jig0163 - jig
		jig0164 - jig
		jig0165 - jig
		jig0166 - jig
		jig0167 - jig
		jig0168 - jig
		jig0169 - jig
		jig0170 - jig
		jig0171 - jig
		jig0172 - jig
		jig0173 - jig
		jig0174 - jig
		jig0175 - jig
		jig0176 - jig
		jig0177 - jig
		jig0178 - jig
		jig0179 - jig
		jig0180 - jig
		jig0181 - jig
		jig0182 - jig
		jig0183 - jig
		jig0184 - jig
		jig0185 - jig
		jig0186 - jig
		jig0187 - jig
		jig0188 - jig
		jig0189 - jig
		jig0190 - jig
		jig0191 - jig
		jig0192 - jig
		jig0193 - jig
		jig0194 - jig
		jig0195 - jig
		jig0196 - jig
		jig0197 - jig
		jig0198 - jig
		jig0199 - jig
		jig0200 - jig
		jig0201 - jig
		jig0202 - jig
		jig0203 - jig
		jig0204 - jig
		jig0205 - jig
		jig0206 - jig
		jig0207 - jig
		jig0208 - jig
		jig0209 - jig
		jig0210 - jig
		jig0211 - jig
		jig0212 - jig
		jig0213 - jig
		jig0214 - jig
		jig0215 - jig
		jig0216 - jig
		jig0217 - jig
		jig0218 - jig
		jig0219 - jig
		jig0220 - jig
		jig0221 - jig
		jig0222 - jig
		jig0223 - jig
		jig0224 - jig
		jig0225 - jig
		jig0226 - jig
		jig0227 - jig
		jig0228 - jig
		jig0229 - jig
		jig0230 - jig
		jig0231 - jig
		jig0232 - jig
		jig0233 - jig
		jig0234 - jig
		jig0235 - jig
		jig0236 - jig
		jig0237 - jig
		jig0238 - jig
		jig0239 - jig
		jig0240 - jig
		jig0241 - jig
		jig0242 - jig
		jig0243 - jig
		jig0244 - jig
		jig0245 - jig
		jig0246 - jig
		jig0247 - jig
		jig0248 - jig
		jig0249 - jig
		jig0250 - jig
		jig0251 - jig
		jig0252 - jig
		jig0253 - jig
		jig0254 - jig
		jig0255 - jig
		jig0256 - jig
		jig0257 - jig
		jig0258 - jig
		jig0259 - jig
		jig0260 - jig
		jig0261 - jig
		jig0262 - jig
		jig0263 - jig
		jig0264 - jig
		jig0265 - jig
		jig0266 - jig
		jig0267 - jig
		jig0268 - jig
		jig0269 - jig
		jig0270 - jig
		jig0271 - jig
		jig0272 - jig
		jig0273 - jig
		jig0274 - jig
		jig0275 - jig
		jig0276 - jig
		jig0277 - jig
		jig0278 - jig
		jig0279 - jig
		jig0280 - jig
		jig0281 - jig
		jig0282 - jig
		jig0283 - jig
		jig0284 - jig
		jig0285 - jig
		jig0286 - jig
		jig0287 - jig
		jig0288 - jig
		jig0289 - jig
		jig0290 - jig
		jig0291 - jig
		jig0292 - jig
		jig0293 - jig
		jig0294 - jig
		jig0295 - jig
		jig0296 - jig
		jig0297 - jig
		jig0298 - jig
		jig0299 - jig
		jig0300 - jig
		jig0301 - jig
		jig0302 - jig
		jig0303 - jig
		jig0304 - jig
		jig0305 - jig
		jig0306 - jig
		jig0307 - jig
		jig0308 - jig
		jig0309 - jig
		jig0310 - jig
		jig0311 - jig
		jig0312 - jig
		jig0313 - jig
		jig0314 - jig
		jig0315 - jig
		jig0316 - jig
		jig0317 - jig
		jig0318 - jig
		jig0319 - jig
		jig0320 - jig
		jig0321 - jig
		jig0322 - jig
		jig0323 - jig
		jig0324 - jig
		jig0325 - jig
		jig0326 - jig
		jig0327 - jig
		jig0328 - jig
		jig0329 - jig
		jig0330 - jig
		jig0331 - jig
		jig0332 - jig
		jig0333 - jig
		jig0334 - jig
		jig0335 - jig
		jig0336 - jig
		jig0337 - jig
		jig0338 - jig
		jig0339 - jig
		jig0340 - jig
		jig0341 - jig
		jig0342 - jig
		jig0343 - jig
		jig0344 - jig
		jig0345 - jig
		jig0346 - jig
		jig0347 - jig
		jig0348 - jig
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
		beluga59 - beluga
		beluga60 - beluga
		beluga61 - beluga
		beluga62 - beluga
		beluga63 - beluga
		beluga64 - beluga
		beluga65 - beluga
		beluga66 - beluga
		beluga67 - beluga
		beluga68 - beluga
		beluga69 - beluga
		beluga70 - beluga
		beluga71 - beluga
		beluga72 - beluga
		beluga73 - beluga
		beluga74 - beluga
		beluga75 - beluga
		beluga76 - beluga
		beluga77 - beluga
		beluga78 - beluga
		beluga79 - beluga
		beluga80 - beluga
		beluga81 - beluga
		beluga82 - beluga
		beluga83 - beluga
		beluga84 - beluga
		beluga85 - beluga
		beluga86 - beluga
		beluga87 - beluga
		beluga88 - beluga
		beluga89 - beluga
		beluga90 - beluga
		beluga91 - beluga
		beluga92 - beluga
		beluga93 - beluga
		beluga94 - beluga
		beluga95 - beluga
		beluga96 - beluga
		beluga97 - beluga
		beluga98 - beluga
		beluga99 - beluga
		beluga100 - beluga
		beluga101 - beluga
		beluga102 - beluga
		beluga103 - beluga
		beluga104 - beluga
		beluga105 - beluga
		beluga106 - beluga
		beluga107 - beluga
		beluga108 - beluga
		beluga109 - beluga
		beluga110 - beluga
		beluga111 - beluga
		beluga112 - beluga
		beluga113 - beluga
		beluga114 - beluga
		beluga115 - beluga
		beluga116 - beluga
		beluga117 - beluga
		beluga118 - beluga
		beluga119 - beluga
		beluga120 - beluga
		beluga121 - beluga
		beluga122 - beluga
		beluga123 - beluga
		beluga124 - beluga
		beluga125 - beluga
		beluga126 - beluga
		beluga127 - beluga
		beluga128 - beluga
		beluga129 - beluga
		beluga130 - beluga
		beluga131 - beluga
		beluga132 - beluga
		beluga133 - beluga
		beluga134 - beluga
		beluga135 - beluga
		beluga136 - beluga
		beluga137 - beluga
		beluga138 - beluga
		beluga139 - beluga
		beluga140 - beluga
		beluga141 - beluga
		beluga142 - beluga
		beluga143 - beluga
		beluga144 - beluga
		beluga145 - beluga
		beluga146 - beluga
		beluga147 - beluga
		beluga148 - beluga
		beluga149 - beluga
		beluga150 - beluga
		beluga151 - beluga
		beluga152 - beluga
		beluga153 - beluga
		beluga154 - beluga
		beluga155 - beluga
		beluga156 - beluga
		beluga157 - beluga
		beluga158 - beluga
		beluga159 - beluga
		beluga160 - beluga
		beluga161 - beluga
		beluga162 - beluga
		beluga163 - beluga
		beluga164 - beluga
		beluga165 - beluga
		beluga166 - beluga
		beluga167 - beluga
		beluga168 - beluga
		beluga169 - beluga
		beluga170 - beluga
		beluga171 - beluga
		beluga172 - beluga
		beluga173 - beluga
		beluga174 - beluga
		beluga175 - beluga
		beluga176 - beluga
		beluga177 - beluga
		beluga178 - beluga
		beluga179 - beluga
		beluga180 - beluga
		beluga181 - beluga
		beluga182 - beluga
		beluga183 - beluga
		beluga184 - beluga
		beluga185 - beluga
		beluga186 - beluga
		beluga187 - beluga
		beluga188 - beluga
		beluga189 - beluga
		beluga190 - beluga
		beluga191 - beluga
		beluga192 - beluga
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
		slot9 - slot
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
		(fit  n23  n04  n27 rack00)
		(fit  n19  n08  n27 rack00)
		(fit  n18  n09  n27 rack00)
		(fit  n16  n11  n27 rack00)
		(fit  n09  n18  n27 rack00)
		(fit  n02  n25  n27 rack00)
		(fit  n25  n04  n29 rack00)
		(fit  n21  n08  n29 rack00)
		(fit  n20  n09  n29 rack00)
		(fit  n18  n11  n29 rack00)
		(fit  n11  n18  n29 rack00)
		(fit  n04  n25  n29 rack00)
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
		(fit  n06  n32  n38 rack00)
		(fit  n34  n04  n38 rack00)
		(fit  n30  n08  n38 rack00)
		(fit  n29  n09  n38 rack00)
		(fit  n27  n11  n38 rack00)
		(fit  n20  n18  n38 rack00)
		(fit  n13  n25  n38 rack00)
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
		(fit  n19  n04  n23 rack01)
		(fit  n15  n08  n23 rack01)
		(fit  n14  n09  n23 rack01)
		(fit  n12  n11  n23 rack01)
		(fit  n05  n18  n23 rack01)
		(fit  n21  n04  n25 rack01)
		(fit  n17  n08  n25 rack01)
		(fit  n16  n09  n25 rack01)
		(fit  n14  n11  n25 rack01)
		(fit  n07  n18  n25 rack01)
		(fit  n00  n25  n25 rack01)
		(fit  n22  n04  n26 rack01)
		(fit  n18  n08  n26 rack01)
		(fit  n17  n09  n26 rack01)
		(fit  n15  n11  n26 rack01)
		(fit  n08  n18  n26 rack01)
		(fit  n01  n25  n26 rack01)
		(fit  n26  n04  n30 rack01)
		(fit  n22  n08  n30 rack01)
		(fit  n21  n09  n30 rack01)
		(fit  n19  n11  n30 rack01)
		(fit  n12  n18  n30 rack01)
		(fit  n05  n25  n30 rack01)
		(fit  n02  n32  n34 rack01)
		(fit  n30  n04  n34 rack01)
		(fit  n26  n08  n34 rack01)
		(fit  n25  n09  n34 rack01)
		(fit  n23  n11  n34 rack01)
		(fit  n16  n18  n34 rack01)
		(fit  n09  n25  n34 rack01)
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
		(fit  n12  n04  n16 rack04)
		(fit  n08  n08  n16 rack04)
		(fit  n07  n09  n16 rack04)
		(fit  n05  n11  n16 rack04)
		(fit  n13  n04  n17 rack04)
		(fit  n09  n08  n17 rack04)
		(fit  n08  n09  n17 rack04)
		(fit  n06  n11  n17 rack04)
		(fit  n17  n04  n21 rack04)
		(fit  n13  n08  n21 rack04)
		(fit  n12  n09  n21 rack04)
		(fit  n10  n11  n21 rack04)
		(fit  n03  n18  n21 rack04)
		(fit  n21  n04  n25 rack04)
		(fit  n17  n08  n25 rack04)
		(fit  n16  n09  n25 rack04)
		(fit  n14  n11  n25 rack04)
		(fit  n07  n18  n25 rack04)
		(fit  n00  n25  n25 rack04)
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
		(fit  n19  n04  n23 rack05)
		(fit  n15  n08  n23 rack05)
		(fit  n14  n09  n23 rack05)
		(fit  n12  n11  n23 rack05)
		(fit  n05  n18  n23 rack05)
		(fit  n23  n04  n27 rack05)
		(fit  n19  n08  n27 rack05)
		(fit  n18  n09  n27 rack05)
		(fit  n16  n11  n27 rack05)
		(fit  n09  n18  n27 rack05)
		(fit  n02  n25  n27 rack05)
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
		(fit  n08  n04  n12 rack06)
		(fit  n04  n08  n12 rack06)
		(fit  n03  n09  n12 rack06)
		(fit  n01  n11  n12 rack06)
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
		(fit  n15  n04  n19 rack06)
		(fit  n11  n08  n19 rack06)
		(fit  n10  n09  n19 rack06)
		(fit  n08  n11  n19 rack06)
		(fit  n01  n18  n19 rack06)
		(fit  n17  n04  n21 rack06)
		(fit  n13  n08  n21 rack06)
		(fit  n12  n09  n21 rack06)
		(fit  n10  n11  n21 rack06)
		(fit  n03  n18  n21 rack06)
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
		(fit  n26  n04  n30 rack06)
		(fit  n22  n08  n30 rack06)
		(fit  n21  n09  n30 rack06)
		(fit  n19  n11  n30 rack06)
		(fit  n12  n18  n30 rack06)
		(fit  n05  n25  n30 rack06)
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
		(fit  n12  n04  n16 rack07)
		(fit  n08  n08  n16 rack07)
		(fit  n07  n09  n16 rack07)
		(fit  n05  n11  n16 rack07)
		(fit  n13  n04  n17 rack07)
		(fit  n09  n08  n17 rack07)
		(fit  n08  n09  n17 rack07)
		(fit  n06  n11  n17 rack07)
		(fit  n14  n04  n18 rack07)
		(fit  n10  n08  n18 rack07)
		(fit  n09  n09  n18 rack07)
		(fit  n07  n11  n18 rack07)
		(fit  n00  n18  n18 rack07)
		(fit  n16  n04  n20 rack07)
		(fit  n12  n08  n20 rack07)
		(fit  n11  n09  n20 rack07)
		(fit  n09  n11  n20 rack07)
		(fit  n02  n18  n20 rack07)
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
		(fit  n20  n04  n24 rack07)
		(fit  n16  n08  n24 rack07)
		(fit  n15  n09  n24 rack07)
		(fit  n13  n11  n24 rack07)
		(fit  n06  n18  n24 rack07)
		(fit  n21  n04  n25 rack07)
		(fit  n17  n08  n25 rack07)
		(fit  n16  n09  n25 rack07)
		(fit  n14  n11  n25 rack07)
		(fit  n07  n18  n25 rack07)
		(fit  n00  n25  n25 rack07)
		(fit  n25  n04  n29 rack07)
		(fit  n21  n08  n29 rack07)
		(fit  n20  n09  n29 rack07)
		(fit  n18  n11  n29 rack07)
		(fit  n11  n18  n29 rack07)
		(fit  n04  n25  n29 rack07)
		(fit  n01  n32  n33 rack07)
		(fit  n29  n04  n33 rack07)
		(fit  n25  n08  n33 rack07)
		(fit  n24  n09  n33 rack07)
		(fit  n22  n11  n33 rack07)
		(fit  n15  n18  n33 rack07)
		(fit  n08  n25  n33 rack07)
		; Sizes fitting rack: rack08
		(fit  n00  n04  n04 rack08)
		(fit  n01  n04  n05 rack08)
		(fit  n02  n04  n06 rack08)
		(fit  n03  n04  n07 rack08)
		(fit  n05  n04  n09 rack08)
		(fit  n01  n08  n09 rack08)
		(fit  n00  n09  n09 rack08)
		(fit  n06  n04  n10 rack08)
		(fit  n02  n08  n10 rack08)
		(fit  n01  n09  n10 rack08)
		(fit  n07  n04  n11 rack08)
		(fit  n03  n08  n11 rack08)
		(fit  n02  n09  n11 rack08)
		(fit  n00  n11  n11 rack08)
		(fit  n09  n04  n13 rack08)
		(fit  n05  n08  n13 rack08)
		(fit  n04  n09  n13 rack08)
		(fit  n02  n11  n13 rack08)
		(fit  n10  n04  n14 rack08)
		(fit  n06  n08  n14 rack08)
		(fit  n05  n09  n14 rack08)
		(fit  n03  n11  n14 rack08)
		(fit  n14  n04  n18 rack08)
		(fit  n10  n08  n18 rack08)
		(fit  n09  n09  n18 rack08)
		(fit  n07  n11  n18 rack08)
		(fit  n00  n18  n18 rack08)
		(fit  n18  n04  n22 rack08)
		(fit  n14  n08  n22 rack08)
		(fit  n13  n09  n22 rack08)
		(fit  n11  n11  n22 rack08)
		(fit  n04  n18  n22 rack08)
		; Sizes fitting rack: rack09
		(fit  n00  n04  n04 rack09)
		(fit  n01  n04  n05 rack09)
		(fit  n02  n04  n06 rack09)
		(fit  n03  n04  n07 rack09)
		(fit  n05  n04  n09 rack09)
		(fit  n01  n08  n09 rack09)
		(fit  n00  n09  n09 rack09)
		(fit  n06  n04  n10 rack09)
		(fit  n02  n08  n10 rack09)
		(fit  n01  n09  n10 rack09)
		(fit  n07  n04  n11 rack09)
		(fit  n03  n08  n11 rack09)
		(fit  n02  n09  n11 rack09)
		(fit  n00  n11  n11 rack09)
		(fit  n09  n04  n13 rack09)
		(fit  n05  n08  n13 rack09)
		(fit  n04  n09  n13 rack09)
		(fit  n02  n11  n13 rack09)
		(fit  n10  n04  n14 rack09)
		(fit  n06  n08  n14 rack09)
		(fit  n05  n09  n14 rack09)
		(fit  n03  n11  n14 rack09)
		(fit  n14  n04  n18 rack09)
		(fit  n10  n08  n18 rack09)
		(fit  n09  n09  n18 rack09)
		(fit  n07  n11  n18 rack09)
		(fit  n00  n18  n18 rack09)
		(fit  n18  n04  n22 rack09)
		(fit  n14  n08  n22 rack09)
		(fit  n13  n09  n22 rack09)
		(fit  n11  n11  n22 rack09)
		(fit  n04  n18  n22 rack09)
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
		(fit  n18  n04  n22 rack10)
		(fit  n14  n08  n22 rack10)
		(fit  n13  n09  n22 rack10)
		(fit  n11  n11  n22 rack10)
		(fit  n04  n18  n22 rack10)
		(fit  n19  n04  n23 rack10)
		(fit  n15  n08  n23 rack10)
		(fit  n14  n09  n23 rack10)
		(fit  n12  n11  n23 rack10)
		(fit  n05  n18  n23 rack10)
		(fit  n23  n04  n27 rack10)
		(fit  n19  n08  n27 rack10)
		(fit  n18  n09  n27 rack10)
		(fit  n16  n11  n27 rack10)
		(fit  n09  n18  n27 rack10)
		(fit  n02  n25  n27 rack10)
		(fit  n27  n04  n31 rack10)
		(fit  n23  n08  n31 rack10)
		(fit  n22  n09  n31 rack10)
		(fit  n20  n11  n31 rack10)
		(fit  n13  n18  n31 rack10)
		(fit  n06  n25  n31 rack10)
		; Sizes fitting rack: rack11
		(fit  n00  n04  n04 rack11)
		(fit  n01  n04  n05 rack11)
		(fit  n02  n04  n06 rack11)
		(fit  n03  n04  n07 rack11)
		(fit  n04  n04  n08 rack11)
		(fit  n00  n08  n08 rack11)
		(fit  n05  n04  n09 rack11)
		(fit  n01  n08  n09 rack11)
		(fit  n00  n09  n09 rack11)
		(fit  n06  n04  n10 rack11)
		(fit  n02  n08  n10 rack11)
		(fit  n01  n09  n10 rack11)
		(fit  n07  n04  n11 rack11)
		(fit  n03  n08  n11 rack11)
		(fit  n02  n09  n11 rack11)
		(fit  n00  n11  n11 rack11)
		(fit  n08  n04  n12 rack11)
		(fit  n04  n08  n12 rack11)
		(fit  n03  n09  n12 rack11)
		(fit  n01  n11  n12 rack11)
		(fit  n09  n04  n13 rack11)
		(fit  n05  n08  n13 rack11)
		(fit  n04  n09  n13 rack11)
		(fit  n02  n11  n13 rack11)
		(fit  n10  n04  n14 rack11)
		(fit  n06  n08  n14 rack11)
		(fit  n05  n09  n14 rack11)
		(fit  n03  n11  n14 rack11)
		(fit  n12  n04  n16 rack11)
		(fit  n08  n08  n16 rack11)
		(fit  n07  n09  n16 rack11)
		(fit  n05  n11  n16 rack11)
		(fit  n13  n04  n17 rack11)
		(fit  n09  n08  n17 rack11)
		(fit  n08  n09  n17 rack11)
		(fit  n06  n11  n17 rack11)
		(fit  n14  n04  n18 rack11)
		(fit  n10  n08  n18 rack11)
		(fit  n09  n09  n18 rack11)
		(fit  n07  n11  n18 rack11)
		(fit  n00  n18  n18 rack11)
		(fit  n16  n04  n20 rack11)
		(fit  n12  n08  n20 rack11)
		(fit  n11  n09  n20 rack11)
		(fit  n09  n11  n20 rack11)
		(fit  n02  n18  n20 rack11)
		(fit  n17  n04  n21 rack11)
		(fit  n13  n08  n21 rack11)
		(fit  n12  n09  n21 rack11)
		(fit  n10  n11  n21 rack11)
		(fit  n03  n18  n21 rack11)
		(fit  n21  n04  n25 rack11)
		(fit  n17  n08  n25 rack11)
		(fit  n16  n09  n25 rack11)
		(fit  n14  n11  n25 rack11)
		(fit  n07  n18  n25 rack11)
		(fit  n00  n25  n25 rack11)
		(fit  n25  n04  n29 rack11)
		(fit  n21  n08  n29 rack11)
		(fit  n20  n09  n29 rack11)
		(fit  n18  n11  n29 rack11)
		(fit  n11  n18  n29 rack11)
		(fit  n04  n25  n29 rack11)
		; Sizes fitting rack: rack12
		(fit  n00  n04  n04 rack12)
		(fit  n01  n04  n05 rack12)
		(fit  n02  n04  n06 rack12)
		(fit  n03  n04  n07 rack12)
		(fit  n04  n04  n08 rack12)
		(fit  n00  n08  n08 rack12)
		(fit  n06  n04  n10 rack12)
		(fit  n02  n08  n10 rack12)
		(fit  n01  n09  n10 rack12)
		(fit  n07  n04  n11 rack12)
		(fit  n03  n08  n11 rack12)
		(fit  n02  n09  n11 rack12)
		(fit  n00  n11  n11 rack12)
		(fit  n08  n04  n12 rack12)
		(fit  n04  n08  n12 rack12)
		(fit  n03  n09  n12 rack12)
		(fit  n01  n11  n12 rack12)
		(fit  n10  n04  n14 rack12)
		(fit  n06  n08  n14 rack12)
		(fit  n05  n09  n14 rack12)
		(fit  n03  n11  n14 rack12)
		(fit  n11  n04  n15 rack12)
		(fit  n07  n08  n15 rack12)
		(fit  n06  n09  n15 rack12)
		(fit  n04  n11  n15 rack12)
		(fit  n15  n04  n19 rack12)
		(fit  n11  n08  n19 rack12)
		(fit  n10  n09  n19 rack12)
		(fit  n08  n11  n19 rack12)
		(fit  n01  n18  n19 rack12)
		(fit  n19  n04  n23 rack12)
		(fit  n15  n08  n23 rack12)
		(fit  n14  n09  n23 rack12)
		(fit  n12  n11  n23 rack12)
		(fit  n05  n18  n23 rack12)
		; Sizes fitting rack: rack13
		(fit  n00  n04  n04 rack13)
		(fit  n01  n04  n05 rack13)
		(fit  n02  n04  n06 rack13)
		(fit  n03  n04  n07 rack13)
		(fit  n04  n04  n08 rack13)
		(fit  n00  n08  n08 rack13)
		(fit  n05  n04  n09 rack13)
		(fit  n01  n08  n09 rack13)
		(fit  n00  n09  n09 rack13)
		(fit  n06  n04  n10 rack13)
		(fit  n02  n08  n10 rack13)
		(fit  n01  n09  n10 rack13)
		(fit  n07  n04  n11 rack13)
		(fit  n03  n08  n11 rack13)
		(fit  n02  n09  n11 rack13)
		(fit  n00  n11  n11 rack13)
		(fit  n09  n04  n13 rack13)
		(fit  n05  n08  n13 rack13)
		(fit  n04  n09  n13 rack13)
		(fit  n02  n11  n13 rack13)
		(fit  n10  n04  n14 rack13)
		(fit  n06  n08  n14 rack13)
		(fit  n05  n09  n14 rack13)
		(fit  n03  n11  n14 rack13)
		(fit  n11  n04  n15 rack13)
		(fit  n07  n08  n15 rack13)
		(fit  n06  n09  n15 rack13)
		(fit  n04  n11  n15 rack13)
		(fit  n13  n04  n17 rack13)
		(fit  n09  n08  n17 rack13)
		(fit  n08  n09  n17 rack13)
		(fit  n06  n11  n17 rack13)
		(fit  n14  n04  n18 rack13)
		(fit  n10  n08  n18 rack13)
		(fit  n09  n09  n18 rack13)
		(fit  n07  n11  n18 rack13)
		(fit  n00  n18  n18 rack13)
		(fit  n18  n04  n22 rack13)
		(fit  n14  n08  n22 rack13)
		(fit  n13  n09  n22 rack13)
		(fit  n11  n11  n22 rack13)
		(fit  n04  n18  n22 rack13)
		(fit  n22  n04  n26 rack13)
		(fit  n18  n08  n26 rack13)
		(fit  n17  n09  n26 rack13)
		(fit  n15  n11  n26 rack13)
		(fit  n08  n18  n26 rack13)
		(fit  n01  n25  n26 rack13)
		; Sizes fitting rack: rack14
		(fit  n00  n04  n04 rack14)
		(fit  n01  n04  n05 rack14)
		(fit  n02  n04  n06 rack14)
		(fit  n03  n04  n07 rack14)
		(fit  n04  n04  n08 rack14)
		(fit  n00  n08  n08 rack14)
		(fit  n05  n04  n09 rack14)
		(fit  n01  n08  n09 rack14)
		(fit  n00  n09  n09 rack14)
		(fit  n06  n04  n10 rack14)
		(fit  n02  n08  n10 rack14)
		(fit  n01  n09  n10 rack14)
		(fit  n07  n04  n11 rack14)
		(fit  n03  n08  n11 rack14)
		(fit  n02  n09  n11 rack14)
		(fit  n00  n11  n11 rack14)
		(fit  n08  n04  n12 rack14)
		(fit  n04  n08  n12 rack14)
		(fit  n03  n09  n12 rack14)
		(fit  n01  n11  n12 rack14)
		(fit  n09  n04  n13 rack14)
		(fit  n05  n08  n13 rack14)
		(fit  n04  n09  n13 rack14)
		(fit  n02  n11  n13 rack14)
		(fit  n10  n04  n14 rack14)
		(fit  n06  n08  n14 rack14)
		(fit  n05  n09  n14 rack14)
		(fit  n03  n11  n14 rack14)
		(fit  n11  n04  n15 rack14)
		(fit  n07  n08  n15 rack14)
		(fit  n06  n09  n15 rack14)
		(fit  n04  n11  n15 rack14)
		(fit  n12  n04  n16 rack14)
		(fit  n08  n08  n16 rack14)
		(fit  n07  n09  n16 rack14)
		(fit  n05  n11  n16 rack14)
		(fit  n13  n04  n17 rack14)
		(fit  n09  n08  n17 rack14)
		(fit  n08  n09  n17 rack14)
		(fit  n06  n11  n17 rack14)
		(fit  n14  n04  n18 rack14)
		(fit  n10  n08  n18 rack14)
		(fit  n09  n09  n18 rack14)
		(fit  n07  n11  n18 rack14)
		(fit  n00  n18  n18 rack14)
		(fit  n16  n04  n20 rack14)
		(fit  n12  n08  n20 rack14)
		(fit  n11  n09  n20 rack14)
		(fit  n09  n11  n20 rack14)
		(fit  n02  n18  n20 rack14)
		(fit  n17  n04  n21 rack14)
		(fit  n13  n08  n21 rack14)
		(fit  n12  n09  n21 rack14)
		(fit  n10  n11  n21 rack14)
		(fit  n03  n18  n21 rack14)
		(fit  n18  n04  n22 rack14)
		(fit  n14  n08  n22 rack14)
		(fit  n13  n09  n22 rack14)
		(fit  n11  n11  n22 rack14)
		(fit  n04  n18  n22 rack14)
		(fit  n20  n04  n24 rack14)
		(fit  n16  n08  n24 rack14)
		(fit  n15  n09  n24 rack14)
		(fit  n13  n11  n24 rack14)
		(fit  n06  n18  n24 rack14)
		(fit  n21  n04  n25 rack14)
		(fit  n17  n08  n25 rack14)
		(fit  n16  n09  n25 rack14)
		(fit  n14  n11  n25 rack14)
		(fit  n07  n18  n25 rack14)
		(fit  n00  n25  n25 rack14)
		(fit  n25  n04  n29 rack14)
		(fit  n21  n08  n29 rack14)
		(fit  n20  n09  n29 rack14)
		(fit  n18  n11  n29 rack14)
		(fit  n11  n18  n29 rack14)
		(fit  n04  n25  n29 rack14)
		(fit  n01  n32  n33 rack14)
		(fit  n29  n04  n33 rack14)
		(fit  n25  n08  n33 rack14)
		(fit  n24  n09  n33 rack14)
		(fit  n22  n11  n33 rack14)
		(fit  n15  n18  n33 rack14)
		(fit  n08  n25  n33 rack14)
		; Sizes fitting rack: rack15
		(fit  n00  n04  n04 rack15)
		(fit  n01  n04  n05 rack15)
		(fit  n02  n04  n06 rack15)
		(fit  n03  n04  n07 rack15)
		(fit  n04  n04  n08 rack15)
		(fit  n00  n08  n08 rack15)
		(fit  n05  n04  n09 rack15)
		(fit  n01  n08  n09 rack15)
		(fit  n00  n09  n09 rack15)
		(fit  n06  n04  n10 rack15)
		(fit  n02  n08  n10 rack15)
		(fit  n01  n09  n10 rack15)
		(fit  n07  n04  n11 rack15)
		(fit  n03  n08  n11 rack15)
		(fit  n02  n09  n11 rack15)
		(fit  n00  n11  n11 rack15)
		(fit  n08  n04  n12 rack15)
		(fit  n04  n08  n12 rack15)
		(fit  n03  n09  n12 rack15)
		(fit  n01  n11  n12 rack15)
		(fit  n09  n04  n13 rack15)
		(fit  n05  n08  n13 rack15)
		(fit  n04  n09  n13 rack15)
		(fit  n02  n11  n13 rack15)
		(fit  n10  n04  n14 rack15)
		(fit  n06  n08  n14 rack15)
		(fit  n05  n09  n14 rack15)
		(fit  n03  n11  n14 rack15)
		(fit  n11  n04  n15 rack15)
		(fit  n07  n08  n15 rack15)
		(fit  n06  n09  n15 rack15)
		(fit  n04  n11  n15 rack15)
		(fit  n12  n04  n16 rack15)
		(fit  n08  n08  n16 rack15)
		(fit  n07  n09  n16 rack15)
		(fit  n05  n11  n16 rack15)
		(fit  n13  n04  n17 rack15)
		(fit  n09  n08  n17 rack15)
		(fit  n08  n09  n17 rack15)
		(fit  n06  n11  n17 rack15)
		(fit  n14  n04  n18 rack15)
		(fit  n10  n08  n18 rack15)
		(fit  n09  n09  n18 rack15)
		(fit  n07  n11  n18 rack15)
		(fit  n00  n18  n18 rack15)
		(fit  n15  n04  n19 rack15)
		(fit  n11  n08  n19 rack15)
		(fit  n10  n09  n19 rack15)
		(fit  n08  n11  n19 rack15)
		(fit  n01  n18  n19 rack15)
		(fit  n17  n04  n21 rack15)
		(fit  n13  n08  n21 rack15)
		(fit  n12  n09  n21 rack15)
		(fit  n10  n11  n21 rack15)
		(fit  n03  n18  n21 rack15)
		(fit  n18  n04  n22 rack15)
		(fit  n14  n08  n22 rack15)
		(fit  n13  n09  n22 rack15)
		(fit  n11  n11  n22 rack15)
		(fit  n04  n18  n22 rack15)
		(fit  n19  n04  n23 rack15)
		(fit  n15  n08  n23 rack15)
		(fit  n14  n09  n23 rack15)
		(fit  n12  n11  n23 rack15)
		(fit  n05  n18  n23 rack15)
		(fit  n21  n04  n25 rack15)
		(fit  n17  n08  n25 rack15)
		(fit  n16  n09  n25 rack15)
		(fit  n14  n11  n25 rack15)
		(fit  n07  n18  n25 rack15)
		(fit  n00  n25  n25 rack15)
		(fit  n22  n04  n26 rack15)
		(fit  n18  n08  n26 rack15)
		(fit  n17  n09  n26 rack15)
		(fit  n15  n11  n26 rack15)
		(fit  n08  n18  n26 rack15)
		(fit  n01  n25  n26 rack15)
		(fit  n26  n04  n30 rack15)
		(fit  n22  n08  n30 rack15)
		(fit  n21  n09  n30 rack15)
		(fit  n19  n11  n30 rack15)
		(fit  n12  n18  n30 rack15)
		(fit  n05  n25  n30 rack15)
		(fit  n02  n32  n34 rack15)
		(fit  n30  n04  n34 rack15)
		(fit  n26  n08  n34 rack15)
		(fit  n25  n09  n34 rack15)
		(fit  n23  n11  n34 rack15)
		(fit  n16  n18  n34 rack15)
		(fit  n09  n25  n34 rack15)
		; Sizes fitting rack: rack16
		(fit  n00  n04  n04 rack16)
		(fit  n01  n04  n05 rack16)
		(fit  n02  n04  n06 rack16)
		(fit  n03  n04  n07 rack16)
		(fit  n04  n04  n08 rack16)
		(fit  n00  n08  n08 rack16)
		(fit  n05  n04  n09 rack16)
		(fit  n01  n08  n09 rack16)
		(fit  n00  n09  n09 rack16)
		(fit  n07  n04  n11 rack16)
		(fit  n03  n08  n11 rack16)
		(fit  n02  n09  n11 rack16)
		(fit  n00  n11  n11 rack16)
		(fit  n08  n04  n12 rack16)
		(fit  n04  n08  n12 rack16)
		(fit  n03  n09  n12 rack16)
		(fit  n01  n11  n12 rack16)
		(fit  n09  n04  n13 rack16)
		(fit  n05  n08  n13 rack16)
		(fit  n04  n09  n13 rack16)
		(fit  n02  n11  n13 rack16)
		(fit  n11  n04  n15 rack16)
		(fit  n07  n08  n15 rack16)
		(fit  n06  n09  n15 rack16)
		(fit  n04  n11  n15 rack16)
		(fit  n12  n04  n16 rack16)
		(fit  n08  n08  n16 rack16)
		(fit  n07  n09  n16 rack16)
		(fit  n05  n11  n16 rack16)
		(fit  n16  n04  n20 rack16)
		(fit  n12  n08  n20 rack16)
		(fit  n11  n09  n20 rack16)
		(fit  n09  n11  n20 rack16)
		(fit  n02  n18  n20 rack16)
		(fit  n20  n04  n24 rack16)
		(fit  n16  n08  n24 rack16)
		(fit  n15  n09  n24 rack16)
		(fit  n13  n11  n24 rack16)
		(fit  n06  n18  n24 rack16)
		; Sizes fitting rack: rack17
		(fit  n00  n04  n04 rack17)
		(fit  n01  n04  n05 rack17)
		(fit  n02  n04  n06 rack17)
		(fit  n03  n04  n07 rack17)
		(fit  n04  n04  n08 rack17)
		(fit  n00  n08  n08 rack17)
		(fit  n05  n04  n09 rack17)
		(fit  n01  n08  n09 rack17)
		(fit  n00  n09  n09 rack17)
		(fit  n06  n04  n10 rack17)
		(fit  n02  n08  n10 rack17)
		(fit  n01  n09  n10 rack17)
		(fit  n07  n04  n11 rack17)
		(fit  n03  n08  n11 rack17)
		(fit  n02  n09  n11 rack17)
		(fit  n00  n11  n11 rack17)
		(fit  n08  n04  n12 rack17)
		(fit  n04  n08  n12 rack17)
		(fit  n03  n09  n12 rack17)
		(fit  n01  n11  n12 rack17)
		(fit  n09  n04  n13 rack17)
		(fit  n05  n08  n13 rack17)
		(fit  n04  n09  n13 rack17)
		(fit  n02  n11  n13 rack17)
		(fit  n10  n04  n14 rack17)
		(fit  n06  n08  n14 rack17)
		(fit  n05  n09  n14 rack17)
		(fit  n03  n11  n14 rack17)
		(fit  n11  n04  n15 rack17)
		(fit  n07  n08  n15 rack17)
		(fit  n06  n09  n15 rack17)
		(fit  n04  n11  n15 rack17)
		(fit  n12  n04  n16 rack17)
		(fit  n08  n08  n16 rack17)
		(fit  n07  n09  n16 rack17)
		(fit  n05  n11  n16 rack17)
		(fit  n13  n04  n17 rack17)
		(fit  n09  n08  n17 rack17)
		(fit  n08  n09  n17 rack17)
		(fit  n06  n11  n17 rack17)
		(fit  n14  n04  n18 rack17)
		(fit  n10  n08  n18 rack17)
		(fit  n09  n09  n18 rack17)
		(fit  n07  n11  n18 rack17)
		(fit  n00  n18  n18 rack17)
		(fit  n15  n04  n19 rack17)
		(fit  n11  n08  n19 rack17)
		(fit  n10  n09  n19 rack17)
		(fit  n08  n11  n19 rack17)
		(fit  n01  n18  n19 rack17)
		(fit  n16  n04  n20 rack17)
		(fit  n12  n08  n20 rack17)
		(fit  n11  n09  n20 rack17)
		(fit  n09  n11  n20 rack17)
		(fit  n02  n18  n20 rack17)
		(fit  n18  n04  n22 rack17)
		(fit  n14  n08  n22 rack17)
		(fit  n13  n09  n22 rack17)
		(fit  n11  n11  n22 rack17)
		(fit  n04  n18  n22 rack17)
		(fit  n19  n04  n23 rack17)
		(fit  n15  n08  n23 rack17)
		(fit  n14  n09  n23 rack17)
		(fit  n12  n11  n23 rack17)
		(fit  n05  n18  n23 rack17)
		(fit  n20  n04  n24 rack17)
		(fit  n16  n08  n24 rack17)
		(fit  n15  n09  n24 rack17)
		(fit  n13  n11  n24 rack17)
		(fit  n06  n18  n24 rack17)
		(fit  n22  n04  n26 rack17)
		(fit  n18  n08  n26 rack17)
		(fit  n17  n09  n26 rack17)
		(fit  n15  n11  n26 rack17)
		(fit  n08  n18  n26 rack17)
		(fit  n01  n25  n26 rack17)
		(fit  n23  n04  n27 rack17)
		(fit  n19  n08  n27 rack17)
		(fit  n18  n09  n27 rack17)
		(fit  n16  n11  n27 rack17)
		(fit  n09  n18  n27 rack17)
		(fit  n02  n25  n27 rack17)
		(fit  n27  n04  n31 rack17)
		(fit  n23  n08  n31 rack17)
		(fit  n22  n09  n31 rack17)
		(fit  n20  n11  n31 rack17)
		(fit  n13  n18  n31 rack17)
		(fit  n06  n25  n31 rack17)
		(fit  n03  n32  n35 rack17)
		(fit  n31  n04  n35 rack17)
		(fit  n27  n08  n35 rack17)
		(fit  n26  n09  n35 rack17)
		(fit  n24  n11  n35 rack17)
		(fit  n17  n18  n35 rack17)
		(fit  n10  n25  n35 rack17)
		; Sizes fitting rack: rack18
		(fit  n00  n04  n04 rack18)
		(fit  n01  n04  n05 rack18)
		(fit  n02  n04  n06 rack18)
		(fit  n03  n04  n07 rack18)
		(fit  n04  n04  n08 rack18)
		(fit  n00  n08  n08 rack18)
		(fit  n05  n04  n09 rack18)
		(fit  n01  n08  n09 rack18)
		(fit  n00  n09  n09 rack18)
		(fit  n07  n04  n11 rack18)
		(fit  n03  n08  n11 rack18)
		(fit  n02  n09  n11 rack18)
		(fit  n00  n11  n11 rack18)
		(fit  n08  n04  n12 rack18)
		(fit  n04  n08  n12 rack18)
		(fit  n03  n09  n12 rack18)
		(fit  n01  n11  n12 rack18)
		(fit  n09  n04  n13 rack18)
		(fit  n05  n08  n13 rack18)
		(fit  n04  n09  n13 rack18)
		(fit  n02  n11  n13 rack18)
		(fit  n11  n04  n15 rack18)
		(fit  n07  n08  n15 rack18)
		(fit  n06  n09  n15 rack18)
		(fit  n04  n11  n15 rack18)
		(fit  n12  n04  n16 rack18)
		(fit  n08  n08  n16 rack18)
		(fit  n07  n09  n16 rack18)
		(fit  n05  n11  n16 rack18)
		(fit  n16  n04  n20 rack18)
		(fit  n12  n08  n20 rack18)
		(fit  n11  n09  n20 rack18)
		(fit  n09  n11  n20 rack18)
		(fit  n02  n18  n20 rack18)
		(fit  n20  n04  n24 rack18)
		(fit  n16  n08  n24 rack18)
		(fit  n15  n09  n24 rack18)
		(fit  n13  n11  n24 rack18)
		(fit  n06  n18  n24 rack18)
		; Sizes fitting rack: rack19
		(fit  n00  n04  n04 rack19)
		(fit  n01  n04  n05 rack19)
		(fit  n02  n04  n06 rack19)
		(fit  n03  n04  n07 rack19)
		(fit  n04  n04  n08 rack19)
		(fit  n00  n08  n08 rack19)
		(fit  n05  n04  n09 rack19)
		(fit  n01  n08  n09 rack19)
		(fit  n00  n09  n09 rack19)
		(fit  n06  n04  n10 rack19)
		(fit  n02  n08  n10 rack19)
		(fit  n01  n09  n10 rack19)
		(fit  n07  n04  n11 rack19)
		(fit  n03  n08  n11 rack19)
		(fit  n02  n09  n11 rack19)
		(fit  n00  n11  n11 rack19)
		(fit  n08  n04  n12 rack19)
		(fit  n04  n08  n12 rack19)
		(fit  n03  n09  n12 rack19)
		(fit  n01  n11  n12 rack19)
		(fit  n09  n04  n13 rack19)
		(fit  n05  n08  n13 rack19)
		(fit  n04  n09  n13 rack19)
		(fit  n02  n11  n13 rack19)
		(fit  n10  n04  n14 rack19)
		(fit  n06  n08  n14 rack19)
		(fit  n05  n09  n14 rack19)
		(fit  n03  n11  n14 rack19)
		(fit  n11  n04  n15 rack19)
		(fit  n07  n08  n15 rack19)
		(fit  n06  n09  n15 rack19)
		(fit  n04  n11  n15 rack19)
		(fit  n12  n04  n16 rack19)
		(fit  n08  n08  n16 rack19)
		(fit  n07  n09  n16 rack19)
		(fit  n05  n11  n16 rack19)
		(fit  n13  n04  n17 rack19)
		(fit  n09  n08  n17 rack19)
		(fit  n08  n09  n17 rack19)
		(fit  n06  n11  n17 rack19)
		(fit  n14  n04  n18 rack19)
		(fit  n10  n08  n18 rack19)
		(fit  n09  n09  n18 rack19)
		(fit  n07  n11  n18 rack19)
		(fit  n00  n18  n18 rack19)
		(fit  n15  n04  n19 rack19)
		(fit  n11  n08  n19 rack19)
		(fit  n10  n09  n19 rack19)
		(fit  n08  n11  n19 rack19)
		(fit  n01  n18  n19 rack19)
		(fit  n16  n04  n20 rack19)
		(fit  n12  n08  n20 rack19)
		(fit  n11  n09  n20 rack19)
		(fit  n09  n11  n20 rack19)
		(fit  n02  n18  n20 rack19)
		(fit  n18  n04  n22 rack19)
		(fit  n14  n08  n22 rack19)
		(fit  n13  n09  n22 rack19)
		(fit  n11  n11  n22 rack19)
		(fit  n04  n18  n22 rack19)
		(fit  n19  n04  n23 rack19)
		(fit  n15  n08  n23 rack19)
		(fit  n14  n09  n23 rack19)
		(fit  n12  n11  n23 rack19)
		(fit  n05  n18  n23 rack19)
		(fit  n20  n04  n24 rack19)
		(fit  n16  n08  n24 rack19)
		(fit  n15  n09  n24 rack19)
		(fit  n13  n11  n24 rack19)
		(fit  n06  n18  n24 rack19)
		(fit  n22  n04  n26 rack19)
		(fit  n18  n08  n26 rack19)
		(fit  n17  n09  n26 rack19)
		(fit  n15  n11  n26 rack19)
		(fit  n08  n18  n26 rack19)
		(fit  n01  n25  n26 rack19)
		(fit  n23  n04  n27 rack19)
		(fit  n19  n08  n27 rack19)
		(fit  n18  n09  n27 rack19)
		(fit  n16  n11  n27 rack19)
		(fit  n09  n18  n27 rack19)
		(fit  n02  n25  n27 rack19)
		(fit  n27  n04  n31 rack19)
		(fit  n23  n08  n31 rack19)
		(fit  n22  n09  n31 rack19)
		(fit  n20  n11  n31 rack19)
		(fit  n13  n18  n31 rack19)
		(fit  n06  n25  n31 rack19)
		(fit  n03  n32  n35 rack19)
		(fit  n31  n04  n35 rack19)
		(fit  n27  n08  n35 rack19)
		(fit  n26  n09  n35 rack19)
		(fit  n24  n11  n35 rack19)
		(fit  n17  n18  n35 rack19)
		(fit  n10  n25  n35 rack19)
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
		; Racks 20
		; Rack:rack00
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n06)
		(in jig0007 rack00)
		(clear jig0007 bside)
		(clear jig0007 fside)
		; Rack:rack01
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n02)
		(in jig0011 rack01)
		(clear jig0011 bside)
		(clear jig0011 fside)
		; Rack:rack02
		(empty rack02)
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n31)
		; Rack:rack03
		(empty rack03)
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n23)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n00)
		(in jig0010 rack04)
		(clear jig0010 bside)
		(clear jig0010 fside)
		; Rack:rack05
		(at-side rack05 bside)
		(at-side rack05 fside)
		(free-space rack05 n09)
		(in jig0009 rack05)
		(clear jig0009 bside)
		(clear jig0009 fside)
		; Rack:rack06
		(at-side rack06 bside)
		(at-side rack06 fside)
		(free-space rack06 n12)
		(in jig0006 rack06)
		(clear jig0006 bside)
		(clear jig0006 fside)
		; Rack:rack07
		(at-side rack07 bside)
		(at-side rack07 fside)
		(free-space rack07 n01)
		(in jig0008 rack07)
		(clear jig0008 bside)
		(clear jig0008 fside)
		; Rack:rack08
		(empty rack08)
		(at-side rack08 bside)
		(at-side rack08 fside)
		(free-space rack08 n22)
		; Rack:rack09
		(empty rack09)
		(at-side rack09 bside)
		(at-side rack09 fside)
		(free-space rack09 n22)
		; Rack:rack10
		(empty rack10)
		(at-side rack10 bside)
		(at-side rack10 fside)
		(free-space rack10 n31)
		; Rack:rack11
		(at-side rack11 bside)
		(at-side rack11 fside)
		(free-space rack11 n11)
		(in jig0002 rack11)
		(clear jig0002 bside)
		(clear jig0002 fside)
		; Rack:rack12
		(empty rack12)
		(at-side rack12 bside)
		(at-side rack12 fside)
		(free-space rack12 n23)
		; Rack:rack13
		(at-side rack13 bside)
		(at-side rack13 fside)
		(free-space rack13 n01)
		(in jig0013 rack13)
		(clear jig0013 bside)
		(clear jig0013 fside)
		; Rack:rack14
		(at-side rack14 bside)
		(at-side rack14 fside)
		(free-space rack14 n01)
		(in jig0001 rack14)
		(clear jig0001 bside)
		(clear jig0001 fside)
		; Rack:rack15
		(at-side rack15 bside)
		(at-side rack15 fside)
		(free-space rack15 n02)
		(in jig0004 rack15)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack16
		(empty rack16)
		(at-side rack16 bside)
		(at-side rack16 fside)
		(free-space rack16 n24)
		; Rack:rack17
		(at-side rack17 bside)
		(at-side rack17 fside)
		(free-space rack17 n09)
		(in jig0005 rack17)
		(clear jig0005 bside)
		(next-to jig0005 jig0012 bside)
		(next-to jig0012 jig0005 fside)
		(in jig0012 rack17)
		(clear jig0012 fside)
		; Rack:rack18
		(empty rack18)
		(at-side rack18 bside)
		(at-side rack18 fside)
		(free-space rack18 n24)
		; Rack:rack19
		(at-side rack19 bside)
		(at-side rack19 fside)
		(free-space rack19 n03)
		(in jig0003 rack19)
		(clear jig0003 bside)
		(clear jig0003 fside)
		; Jigs (size):
		(is_type jig0001 typeE)
		(size jig0001 n32)
		(empty-size jig0001 n32)
		(is_type jig0002 typeC)
		(size jig0002 n18)
		(empty-size jig0002 n09)
		(is_type jig0003 typeE)
		(size jig0003 n32)
		(empty-size jig0003 n32)
		(is_type jig0004 typeE)
		(size jig0004 n32)
		(empty-size jig0004 n32)
		(empty jig0004)
		(is_type jig0005 typeB)
		(size jig0005 n08)
		(empty-size jig0005 n08)
		(empty jig0005)
		(is_type jig0006 typeD)
		(size jig0006 n18)
		(empty-size jig0006 n18)
		(empty jig0006)
		(is_type jig0007 typeE)
		(size jig0007 n32)
		(empty-size jig0007 n32)
		(is_type jig0008 typeE)
		(size jig0008 n32)
		(empty-size jig0008 n32)
		(is_type jig0009 typeD)
		(size jig0009 n18)
		(empty-size jig0009 n18)
		(empty jig0009)
		(is_type jig0010 typeD)
		(size jig0010 n25)
		(empty-size jig0010 n18)
		(is_type jig0011 typeE)
		(size jig0011 n32)
		(empty-size jig0011 n32)
		(is_type jig0012 typeC)
		(size jig0012 n18)
		(empty-size jig0012 n09)
		(is_type jig0013 typeD)
		(size jig0013 n25)
		(empty-size jig0013 n18)
		(is_type jig0014 typeC)
		(size jig0014 n18)
		(empty-size jig0014 n09)
		(is_type jig0015 typeC)
		(size jig0015 n18)
		(empty-size jig0015 n09)
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
		(is_type jig0020 typeB)
		(size jig0020 n11)
		(empty-size jig0020 n08)
		(is_type jig0021 typeB)
		(size jig0021 n11)
		(empty-size jig0021 n08)
		(is_type jig0022 typeB)
		(size jig0022 n11)
		(empty-size jig0022 n08)
		(is_type jig0023 typeC)
		(size jig0023 n18)
		(empty-size jig0023 n09)
		(is_type jig0024 typeC)
		(size jig0024 n18)
		(empty-size jig0024 n09)
		(is_type jig0025 typeE)
		(size jig0025 n32)
		(empty-size jig0025 n32)
		(is_type jig0026 typeB)
		(size jig0026 n11)
		(empty-size jig0026 n08)
		(is_type jig0027 typeB)
		(size jig0027 n11)
		(empty-size jig0027 n08)
		(is_type jig0028 typeB)
		(size jig0028 n11)
		(empty-size jig0028 n08)
		(is_type jig0029 typeC)
		(size jig0029 n18)
		(empty-size jig0029 n09)
		(is_type jig0030 typeC)
		(size jig0030 n18)
		(empty-size jig0030 n09)
		(is_type jig0031 typeC)
		(size jig0031 n18)
		(empty-size jig0031 n09)
		(is_type jig0032 typeC)
		(size jig0032 n18)
		(empty-size jig0032 n09)
		(is_type jig0033 typeE)
		(size jig0033 n32)
		(empty-size jig0033 n32)
		(is_type jig0034 typeE)
		(size jig0034 n32)
		(empty-size jig0034 n32)
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
		(is_type jig0045 typeE)
		(size jig0045 n32)
		(empty-size jig0045 n32)
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
		(is_type jig0066 typeD)
		(size jig0066 n25)
		(empty-size jig0066 n18)
		(is_type jig0067 typeD)
		(size jig0067 n25)
		(empty-size jig0067 n18)
		(is_type jig0068 typeB)
		(size jig0068 n11)
		(empty-size jig0068 n08)
		(is_type jig0069 typeB)
		(size jig0069 n11)
		(empty-size jig0069 n08)
		(is_type jig0070 typeB)
		(size jig0070 n11)
		(empty-size jig0070 n08)
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
		(is_type jig0078 typeA)
		(size jig0078 n04)
		(empty-size jig0078 n04)
		(is_type jig0079 typeA)
		(size jig0079 n04)
		(empty-size jig0079 n04)
		(is_type jig0080 typeA)
		(size jig0080 n04)
		(empty-size jig0080 n04)
		(is_type jig0081 typeB)
		(size jig0081 n11)
		(empty-size jig0081 n08)
		(is_type jig0082 typeC)
		(size jig0082 n18)
		(empty-size jig0082 n09)
		(is_type jig0083 typeD)
		(size jig0083 n25)
		(empty-size jig0083 n18)
		(is_type jig0084 typeC)
		(size jig0084 n18)
		(empty-size jig0084 n09)
		(is_type jig0085 typeC)
		(size jig0085 n18)
		(empty-size jig0085 n09)
		(is_type jig0086 typeC)
		(size jig0086 n18)
		(empty-size jig0086 n09)
		(is_type jig0087 typeE)
		(size jig0087 n32)
		(empty-size jig0087 n32)
		(is_type jig0088 typeD)
		(size jig0088 n25)
		(empty-size jig0088 n18)
		(is_type jig0089 typeC)
		(size jig0089 n18)
		(empty-size jig0089 n09)
		(is_type jig0090 typeC)
		(size jig0090 n18)
		(empty-size jig0090 n09)
		(is_type jig0091 typeB)
		(size jig0091 n11)
		(empty-size jig0091 n08)
		(is_type jig0092 typeB)
		(size jig0092 n11)
		(empty-size jig0092 n08)
		(is_type jig0093 typeB)
		(size jig0093 n11)
		(empty-size jig0093 n08)
		(is_type jig0094 typeC)
		(size jig0094 n18)
		(empty-size jig0094 n09)
		(is_type jig0095 typeC)
		(size jig0095 n18)
		(empty-size jig0095 n09)
		(is_type jig0096 typeA)
		(size jig0096 n04)
		(empty-size jig0096 n04)
		(is_type jig0097 typeA)
		(size jig0097 n04)
		(empty-size jig0097 n04)
		(is_type jig0098 typeA)
		(size jig0098 n04)
		(empty-size jig0098 n04)
		(is_type jig0099 typeA)
		(size jig0099 n04)
		(empty-size jig0099 n04)
		(is_type jig0100 typeA)
		(size jig0100 n04)
		(empty-size jig0100 n04)
		(is_type jig0101 typeA)
		(size jig0101 n04)
		(empty-size jig0101 n04)
		(is_type jig0102 typeA)
		(size jig0102 n04)
		(empty-size jig0102 n04)
		(is_type jig0103 typeA)
		(size jig0103 n04)
		(empty-size jig0103 n04)
		(is_type jig0104 typeA)
		(size jig0104 n04)
		(empty-size jig0104 n04)
		(is_type jig0105 typeA)
		(size jig0105 n04)
		(empty-size jig0105 n04)
		(is_type jig0106 typeC)
		(size jig0106 n18)
		(empty-size jig0106 n09)
		(is_type jig0107 typeD)
		(size jig0107 n25)
		(empty-size jig0107 n18)
		(is_type jig0108 typeC)
		(size jig0108 n18)
		(empty-size jig0108 n09)
		(is_type jig0109 typeD)
		(size jig0109 n25)
		(empty-size jig0109 n18)
		(is_type jig0110 typeC)
		(size jig0110 n18)
		(empty-size jig0110 n09)
		(is_type jig0111 typeC)
		(size jig0111 n18)
		(empty-size jig0111 n09)
		(is_type jig0112 typeC)
		(size jig0112 n18)
		(empty-size jig0112 n09)
		(is_type jig0113 typeC)
		(size jig0113 n18)
		(empty-size jig0113 n09)
		(is_type jig0114 typeE)
		(size jig0114 n32)
		(empty-size jig0114 n32)
		(is_type jig0115 typeE)
		(size jig0115 n32)
		(empty-size jig0115 n32)
		(is_type jig0116 typeC)
		(size jig0116 n18)
		(empty-size jig0116 n09)
		(is_type jig0117 typeC)
		(size jig0117 n18)
		(empty-size jig0117 n09)
		(is_type jig0118 typeC)
		(size jig0118 n18)
		(empty-size jig0118 n09)
		(is_type jig0119 typeA)
		(size jig0119 n04)
		(empty-size jig0119 n04)
		(is_type jig0120 typeA)
		(size jig0120 n04)
		(empty-size jig0120 n04)
		(is_type jig0121 typeA)
		(size jig0121 n04)
		(empty-size jig0121 n04)
		(is_type jig0122 typeA)
		(size jig0122 n04)
		(empty-size jig0122 n04)
		(is_type jig0123 typeA)
		(size jig0123 n04)
		(empty-size jig0123 n04)
		(is_type jig0124 typeA)
		(size jig0124 n04)
		(empty-size jig0124 n04)
		(is_type jig0125 typeA)
		(size jig0125 n04)
		(empty-size jig0125 n04)
		(is_type jig0126 typeA)
		(size jig0126 n04)
		(empty-size jig0126 n04)
		(is_type jig0127 typeA)
		(size jig0127 n04)
		(empty-size jig0127 n04)
		(is_type jig0128 typeA)
		(size jig0128 n04)
		(empty-size jig0128 n04)
		(is_type jig0129 typeD)
		(size jig0129 n25)
		(empty-size jig0129 n18)
		(is_type jig0130 typeC)
		(size jig0130 n18)
		(empty-size jig0130 n09)
		(is_type jig0131 typeC)
		(size jig0131 n18)
		(empty-size jig0131 n09)
		(is_type jig0132 typeE)
		(size jig0132 n32)
		(empty-size jig0132 n32)
		(is_type jig0133 typeE)
		(size jig0133 n32)
		(empty-size jig0133 n32)
		(is_type jig0134 typeC)
		(size jig0134 n18)
		(empty-size jig0134 n09)
		(is_type jig0135 typeC)
		(size jig0135 n18)
		(empty-size jig0135 n09)
		(is_type jig0136 typeB)
		(size jig0136 n11)
		(empty-size jig0136 n08)
		(is_type jig0137 typeB)
		(size jig0137 n11)
		(empty-size jig0137 n08)
		(is_type jig0138 typeB)
		(size jig0138 n11)
		(empty-size jig0138 n08)
		(is_type jig0139 typeC)
		(size jig0139 n18)
		(empty-size jig0139 n09)
		(is_type jig0140 typeB)
		(size jig0140 n11)
		(empty-size jig0140 n08)
		(is_type jig0141 typeB)
		(size jig0141 n11)
		(empty-size jig0141 n08)
		(is_type jig0142 typeC)
		(size jig0142 n18)
		(empty-size jig0142 n09)
		(is_type jig0143 typeC)
		(size jig0143 n18)
		(empty-size jig0143 n09)
		(is_type jig0144 typeD)
		(size jig0144 n25)
		(empty-size jig0144 n18)
		(is_type jig0145 typeD)
		(size jig0145 n25)
		(empty-size jig0145 n18)
		(is_type jig0146 typeE)
		(size jig0146 n32)
		(empty-size jig0146 n32)
		(is_type jig0147 typeB)
		(size jig0147 n11)
		(empty-size jig0147 n08)
		(is_type jig0148 typeB)
		(size jig0148 n11)
		(empty-size jig0148 n08)
		(is_type jig0149 typeB)
		(size jig0149 n11)
		(empty-size jig0149 n08)
		(is_type jig0150 typeE)
		(size jig0150 n32)
		(empty-size jig0150 n32)
		(is_type jig0151 typeD)
		(size jig0151 n25)
		(empty-size jig0151 n18)
		(is_type jig0152 typeE)
		(size jig0152 n32)
		(empty-size jig0152 n32)
		(is_type jig0153 typeD)
		(size jig0153 n25)
		(empty-size jig0153 n18)
		(is_type jig0154 typeD)
		(size jig0154 n25)
		(empty-size jig0154 n18)
		(is_type jig0155 typeB)
		(size jig0155 n11)
		(empty-size jig0155 n08)
		(is_type jig0156 typeB)
		(size jig0156 n11)
		(empty-size jig0156 n08)
		(is_type jig0157 typeB)
		(size jig0157 n11)
		(empty-size jig0157 n08)
		(is_type jig0158 typeD)
		(size jig0158 n25)
		(empty-size jig0158 n18)
		(is_type jig0159 typeD)
		(size jig0159 n25)
		(empty-size jig0159 n18)
		(is_type jig0160 typeC)
		(size jig0160 n18)
		(empty-size jig0160 n09)
		(is_type jig0161 typeC)
		(size jig0161 n18)
		(empty-size jig0161 n09)
		(is_type jig0162 typeE)
		(size jig0162 n32)
		(empty-size jig0162 n32)
		(is_type jig0163 typeD)
		(size jig0163 n25)
		(empty-size jig0163 n18)
		(is_type jig0164 typeC)
		(size jig0164 n18)
		(empty-size jig0164 n09)
		(is_type jig0165 typeC)
		(size jig0165 n18)
		(empty-size jig0165 n09)
		(is_type jig0166 typeD)
		(size jig0166 n25)
		(empty-size jig0166 n18)
		(is_type jig0167 typeC)
		(size jig0167 n18)
		(empty-size jig0167 n09)
		(is_type jig0168 typeC)
		(size jig0168 n18)
		(empty-size jig0168 n09)
		(is_type jig0169 typeE)
		(size jig0169 n32)
		(empty-size jig0169 n32)
		(is_type jig0170 typeC)
		(size jig0170 n18)
		(empty-size jig0170 n09)
		(is_type jig0171 typeC)
		(size jig0171 n18)
		(empty-size jig0171 n09)
		(is_type jig0172 typeC)
		(size jig0172 n18)
		(empty-size jig0172 n09)
		(is_type jig0173 typeC)
		(size jig0173 n18)
		(empty-size jig0173 n09)
		(is_type jig0174 typeB)
		(size jig0174 n11)
		(empty-size jig0174 n08)
		(is_type jig0175 typeB)
		(size jig0175 n11)
		(empty-size jig0175 n08)
		(is_type jig0176 typeB)
		(size jig0176 n11)
		(empty-size jig0176 n08)
		(is_type jig0177 typeA)
		(size jig0177 n04)
		(empty-size jig0177 n04)
		(is_type jig0178 typeA)
		(size jig0178 n04)
		(empty-size jig0178 n04)
		(is_type jig0179 typeA)
		(size jig0179 n04)
		(empty-size jig0179 n04)
		(is_type jig0180 typeA)
		(size jig0180 n04)
		(empty-size jig0180 n04)
		(is_type jig0181 typeA)
		(size jig0181 n04)
		(empty-size jig0181 n04)
		(is_type jig0182 typeA)
		(size jig0182 n04)
		(empty-size jig0182 n04)
		(is_type jig0183 typeA)
		(size jig0183 n04)
		(empty-size jig0183 n04)
		(is_type jig0184 typeA)
		(size jig0184 n04)
		(empty-size jig0184 n04)
		(is_type jig0185 typeA)
		(size jig0185 n04)
		(empty-size jig0185 n04)
		(is_type jig0186 typeA)
		(size jig0186 n04)
		(empty-size jig0186 n04)
		(is_type jig0187 typeE)
		(size jig0187 n32)
		(empty-size jig0187 n32)
		(is_type jig0188 typeB)
		(size jig0188 n11)
		(empty-size jig0188 n08)
		(is_type jig0189 typeB)
		(size jig0189 n11)
		(empty-size jig0189 n08)
		(is_type jig0190 typeB)
		(size jig0190 n11)
		(empty-size jig0190 n08)
		(is_type jig0191 typeE)
		(size jig0191 n32)
		(empty-size jig0191 n32)
		(is_type jig0192 typeD)
		(size jig0192 n25)
		(empty-size jig0192 n18)
		(is_type jig0193 typeD)
		(size jig0193 n25)
		(empty-size jig0193 n18)
		(is_type jig0194 typeE)
		(size jig0194 n32)
		(empty-size jig0194 n32)
		(is_type jig0195 typeB)
		(size jig0195 n11)
		(empty-size jig0195 n08)
		(is_type jig0196 typeB)
		(size jig0196 n11)
		(empty-size jig0196 n08)
		(is_type jig0197 typeB)
		(size jig0197 n11)
		(empty-size jig0197 n08)
		(is_type jig0198 typeD)
		(size jig0198 n25)
		(empty-size jig0198 n18)
		(is_type jig0199 typeB)
		(size jig0199 n11)
		(empty-size jig0199 n08)
		(is_type jig0200 typeB)
		(size jig0200 n11)
		(empty-size jig0200 n08)
		(is_type jig0201 typeB)
		(size jig0201 n11)
		(empty-size jig0201 n08)
		(is_type jig0202 typeC)
		(size jig0202 n18)
		(empty-size jig0202 n09)
		(is_type jig0203 typeC)
		(size jig0203 n18)
		(empty-size jig0203 n09)
		(is_type jig0204 typeA)
		(size jig0204 n04)
		(empty-size jig0204 n04)
		(is_type jig0205 typeA)
		(size jig0205 n04)
		(empty-size jig0205 n04)
		(is_type jig0206 typeA)
		(size jig0206 n04)
		(empty-size jig0206 n04)
		(is_type jig0207 typeA)
		(size jig0207 n04)
		(empty-size jig0207 n04)
		(is_type jig0208 typeA)
		(size jig0208 n04)
		(empty-size jig0208 n04)
		(is_type jig0209 typeA)
		(size jig0209 n04)
		(empty-size jig0209 n04)
		(is_type jig0210 typeA)
		(size jig0210 n04)
		(empty-size jig0210 n04)
		(is_type jig0211 typeA)
		(size jig0211 n04)
		(empty-size jig0211 n04)
		(is_type jig0212 typeA)
		(size jig0212 n04)
		(empty-size jig0212 n04)
		(is_type jig0213 typeA)
		(size jig0213 n04)
		(empty-size jig0213 n04)
		(is_type jig0214 typeE)
		(size jig0214 n32)
		(empty-size jig0214 n32)
		(is_type jig0215 typeC)
		(size jig0215 n18)
		(empty-size jig0215 n09)
		(is_type jig0216 typeA)
		(size jig0216 n04)
		(empty-size jig0216 n04)
		(is_type jig0217 typeA)
		(size jig0217 n04)
		(empty-size jig0217 n04)
		(is_type jig0218 typeA)
		(size jig0218 n04)
		(empty-size jig0218 n04)
		(is_type jig0219 typeA)
		(size jig0219 n04)
		(empty-size jig0219 n04)
		(is_type jig0220 typeA)
		(size jig0220 n04)
		(empty-size jig0220 n04)
		(is_type jig0221 typeA)
		(size jig0221 n04)
		(empty-size jig0221 n04)
		(is_type jig0222 typeA)
		(size jig0222 n04)
		(empty-size jig0222 n04)
		(is_type jig0223 typeB)
		(size jig0223 n11)
		(empty-size jig0223 n08)
		(is_type jig0224 typeB)
		(size jig0224 n11)
		(empty-size jig0224 n08)
		(is_type jig0225 typeB)
		(size jig0225 n11)
		(empty-size jig0225 n08)
		(is_type jig0226 typeB)
		(size jig0226 n11)
		(empty-size jig0226 n08)
		(is_type jig0227 typeE)
		(size jig0227 n32)
		(empty-size jig0227 n32)
		(is_type jig0228 typeA)
		(size jig0228 n04)
		(empty-size jig0228 n04)
		(is_type jig0229 typeA)
		(size jig0229 n04)
		(empty-size jig0229 n04)
		(is_type jig0230 typeA)
		(size jig0230 n04)
		(empty-size jig0230 n04)
		(is_type jig0231 typeC)
		(size jig0231 n18)
		(empty-size jig0231 n09)
		(is_type jig0232 typeC)
		(size jig0232 n18)
		(empty-size jig0232 n09)
		(is_type jig0233 typeD)
		(size jig0233 n25)
		(empty-size jig0233 n18)
		(is_type jig0234 typeB)
		(size jig0234 n11)
		(empty-size jig0234 n08)
		(is_type jig0235 typeB)
		(size jig0235 n11)
		(empty-size jig0235 n08)
		(is_type jig0236 typeB)
		(size jig0236 n11)
		(empty-size jig0236 n08)
		(is_type jig0237 typeD)
		(size jig0237 n25)
		(empty-size jig0237 n18)
		(is_type jig0238 typeC)
		(size jig0238 n18)
		(empty-size jig0238 n09)
		(is_type jig0239 typeC)
		(size jig0239 n18)
		(empty-size jig0239 n09)
		(is_type jig0240 typeD)
		(size jig0240 n25)
		(empty-size jig0240 n18)
		(is_type jig0241 typeB)
		(size jig0241 n11)
		(empty-size jig0241 n08)
		(is_type jig0242 typeB)
		(size jig0242 n11)
		(empty-size jig0242 n08)
		(is_type jig0243 typeB)
		(size jig0243 n11)
		(empty-size jig0243 n08)
		(is_type jig0244 typeE)
		(size jig0244 n32)
		(empty-size jig0244 n32)
		(is_type jig0245 typeE)
		(size jig0245 n32)
		(empty-size jig0245 n32)
		(is_type jig0246 typeE)
		(size jig0246 n32)
		(empty-size jig0246 n32)
		(is_type jig0247 typeC)
		(size jig0247 n18)
		(empty-size jig0247 n09)
		(is_type jig0248 typeC)
		(size jig0248 n18)
		(empty-size jig0248 n09)
		(is_type jig0249 typeD)
		(size jig0249 n25)
		(empty-size jig0249 n18)
		(is_type jig0250 typeA)
		(size jig0250 n04)
		(empty-size jig0250 n04)
		(is_type jig0251 typeA)
		(size jig0251 n04)
		(empty-size jig0251 n04)
		(is_type jig0252 typeA)
		(size jig0252 n04)
		(empty-size jig0252 n04)
		(is_type jig0253 typeA)
		(size jig0253 n04)
		(empty-size jig0253 n04)
		(is_type jig0254 typeA)
		(size jig0254 n04)
		(empty-size jig0254 n04)
		(is_type jig0255 typeA)
		(size jig0255 n04)
		(empty-size jig0255 n04)
		(is_type jig0256 typeA)
		(size jig0256 n04)
		(empty-size jig0256 n04)
		(is_type jig0257 typeA)
		(size jig0257 n04)
		(empty-size jig0257 n04)
		(is_type jig0258 typeA)
		(size jig0258 n04)
		(empty-size jig0258 n04)
		(is_type jig0259 typeA)
		(size jig0259 n04)
		(empty-size jig0259 n04)
		(is_type jig0260 typeD)
		(size jig0260 n25)
		(empty-size jig0260 n18)
		(is_type jig0261 typeD)
		(size jig0261 n25)
		(empty-size jig0261 n18)
		(is_type jig0262 typeE)
		(size jig0262 n32)
		(empty-size jig0262 n32)
		(is_type jig0263 typeE)
		(size jig0263 n32)
		(empty-size jig0263 n32)
		(is_type jig0264 typeD)
		(size jig0264 n25)
		(empty-size jig0264 n18)
		(is_type jig0265 typeC)
		(size jig0265 n18)
		(empty-size jig0265 n09)
		(is_type jig0266 typeC)
		(size jig0266 n18)
		(empty-size jig0266 n09)
		(is_type jig0267 typeB)
		(size jig0267 n11)
		(empty-size jig0267 n08)
		(is_type jig0268 typeB)
		(size jig0268 n11)
		(empty-size jig0268 n08)
		(is_type jig0269 typeB)
		(size jig0269 n11)
		(empty-size jig0269 n08)
		(is_type jig0270 typeE)
		(size jig0270 n32)
		(empty-size jig0270 n32)
		(is_type jig0271 typeB)
		(size jig0271 n11)
		(empty-size jig0271 n08)
		(is_type jig0272 typeB)
		(size jig0272 n11)
		(empty-size jig0272 n08)
		(is_type jig0273 typeB)
		(size jig0273 n11)
		(empty-size jig0273 n08)
		(is_type jig0274 typeA)
		(size jig0274 n04)
		(empty-size jig0274 n04)
		(is_type jig0275 typeA)
		(size jig0275 n04)
		(empty-size jig0275 n04)
		(is_type jig0276 typeA)
		(size jig0276 n04)
		(empty-size jig0276 n04)
		(is_type jig0277 typeA)
		(size jig0277 n04)
		(empty-size jig0277 n04)
		(is_type jig0278 typeA)
		(size jig0278 n04)
		(empty-size jig0278 n04)
		(is_type jig0279 typeA)
		(size jig0279 n04)
		(empty-size jig0279 n04)
		(is_type jig0280 typeA)
		(size jig0280 n04)
		(empty-size jig0280 n04)
		(is_type jig0281 typeA)
		(size jig0281 n04)
		(empty-size jig0281 n04)
		(is_type jig0282 typeA)
		(size jig0282 n04)
		(empty-size jig0282 n04)
		(is_type jig0283 typeA)
		(size jig0283 n04)
		(empty-size jig0283 n04)
		(is_type jig0284 typeA)
		(size jig0284 n04)
		(empty-size jig0284 n04)
		(is_type jig0285 typeA)
		(size jig0285 n04)
		(empty-size jig0285 n04)
		(is_type jig0286 typeA)
		(size jig0286 n04)
		(empty-size jig0286 n04)
		(is_type jig0287 typeA)
		(size jig0287 n04)
		(empty-size jig0287 n04)
		(is_type jig0288 typeA)
		(size jig0288 n04)
		(empty-size jig0288 n04)
		(is_type jig0289 typeA)
		(size jig0289 n04)
		(empty-size jig0289 n04)
		(is_type jig0290 typeA)
		(size jig0290 n04)
		(empty-size jig0290 n04)
		(is_type jig0291 typeA)
		(size jig0291 n04)
		(empty-size jig0291 n04)
		(is_type jig0292 typeA)
		(size jig0292 n04)
		(empty-size jig0292 n04)
		(is_type jig0293 typeA)
		(size jig0293 n04)
		(empty-size jig0293 n04)
		(is_type jig0294 typeC)
		(size jig0294 n18)
		(empty-size jig0294 n09)
		(is_type jig0295 typeC)
		(size jig0295 n18)
		(empty-size jig0295 n09)
		(is_type jig0296 typeC)
		(size jig0296 n18)
		(empty-size jig0296 n09)
		(is_type jig0297 typeC)
		(size jig0297 n18)
		(empty-size jig0297 n09)
		(is_type jig0298 typeC)
		(size jig0298 n18)
		(empty-size jig0298 n09)
		(is_type jig0299 typeC)
		(size jig0299 n18)
		(empty-size jig0299 n09)
		(is_type jig0300 typeB)
		(size jig0300 n11)
		(empty-size jig0300 n08)
		(is_type jig0301 typeB)
		(size jig0301 n11)
		(empty-size jig0301 n08)
		(is_type jig0302 typeB)
		(size jig0302 n11)
		(empty-size jig0302 n08)
		(is_type jig0303 typeC)
		(size jig0303 n18)
		(empty-size jig0303 n09)
		(is_type jig0304 typeC)
		(size jig0304 n18)
		(empty-size jig0304 n09)
		(is_type jig0305 typeD)
		(size jig0305 n25)
		(empty-size jig0305 n18)
		(is_type jig0306 typeD)
		(size jig0306 n25)
		(empty-size jig0306 n18)
		(is_type jig0307 typeC)
		(size jig0307 n18)
		(empty-size jig0307 n09)
		(is_type jig0308 typeC)
		(size jig0308 n18)
		(empty-size jig0308 n09)
		(is_type jig0309 typeB)
		(size jig0309 n11)
		(empty-size jig0309 n08)
		(is_type jig0310 typeB)
		(size jig0310 n11)
		(empty-size jig0310 n08)
		(is_type jig0311 typeB)
		(size jig0311 n11)
		(empty-size jig0311 n08)
		(is_type jig0312 typeD)
		(size jig0312 n25)
		(empty-size jig0312 n18)
		(is_type jig0313 typeC)
		(size jig0313 n18)
		(empty-size jig0313 n09)
		(is_type jig0314 typeC)
		(size jig0314 n18)
		(empty-size jig0314 n09)
		(is_type jig0315 typeA)
		(size jig0315 n04)
		(empty-size jig0315 n04)
		(is_type jig0316 typeA)
		(size jig0316 n04)
		(empty-size jig0316 n04)
		(is_type jig0317 typeA)
		(size jig0317 n04)
		(empty-size jig0317 n04)
		(is_type jig0318 typeA)
		(size jig0318 n04)
		(empty-size jig0318 n04)
		(is_type jig0319 typeA)
		(size jig0319 n04)
		(empty-size jig0319 n04)
		(is_type jig0320 typeA)
		(size jig0320 n04)
		(empty-size jig0320 n04)
		(is_type jig0321 typeA)
		(size jig0321 n04)
		(empty-size jig0321 n04)
		(is_type jig0322 typeA)
		(size jig0322 n04)
		(empty-size jig0322 n04)
		(is_type jig0323 typeA)
		(size jig0323 n04)
		(empty-size jig0323 n04)
		(is_type jig0324 typeA)
		(size jig0324 n04)
		(empty-size jig0324 n04)
		(is_type jig0325 typeE)
		(size jig0325 n32)
		(empty-size jig0325 n32)
		(is_type jig0326 typeD)
		(size jig0326 n25)
		(empty-size jig0326 n18)
		(is_type jig0327 typeC)
		(size jig0327 n18)
		(empty-size jig0327 n09)
		(is_type jig0328 typeC)
		(size jig0328 n18)
		(empty-size jig0328 n09)
		(is_type jig0329 typeA)
		(size jig0329 n04)
		(empty-size jig0329 n04)
		(is_type jig0330 typeA)
		(size jig0330 n04)
		(empty-size jig0330 n04)
		(is_type jig0331 typeA)
		(size jig0331 n04)
		(empty-size jig0331 n04)
		(is_type jig0332 typeA)
		(size jig0332 n04)
		(empty-size jig0332 n04)
		(is_type jig0333 typeA)
		(size jig0333 n04)
		(empty-size jig0333 n04)
		(is_type jig0334 typeA)
		(size jig0334 n04)
		(empty-size jig0334 n04)
		(is_type jig0335 typeA)
		(size jig0335 n04)
		(empty-size jig0335 n04)
		(is_type jig0336 typeA)
		(size jig0336 n04)
		(empty-size jig0336 n04)
		(is_type jig0337 typeA)
		(size jig0337 n04)
		(empty-size jig0337 n04)
		(is_type jig0338 typeA)
		(size jig0338 n04)
		(empty-size jig0338 n04)
		(is_type jig0339 typeE)
		(size jig0339 n32)
		(empty-size jig0339 n32)
		(is_type jig0340 typeC)
		(size jig0340 n18)
		(empty-size jig0340 n09)
		(is_type jig0341 typeC)
		(size jig0341 n18)
		(empty-size jig0341 n09)
		(is_type jig0342 typeD)
		(size jig0342 n25)
		(empty-size jig0342 n18)
		(is_type jig0343 typeC)
		(size jig0343 n18)
		(empty-size jig0343 n09)
		(is_type jig0344 typeC)
		(size jig0344 n18)
		(empty-size jig0344 n09)
		(is_type jig0345 typeD)
		(size jig0345 n25)
		(empty-size jig0345 n18)
		(is_type jig0346 typeD)
		(size jig0346 n25)
		(empty-size jig0346 n18)
		(is_type jig0347 typeE)
		(size jig0347 n32)
		(empty-size jig0347 n32)
		(is_type jig0348 typeE)
		(size jig0348 n32)
		(empty-size jig0348 n32)
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
		(next-flight-to-process beluga58 beluga59)
		(next-flight-to-process beluga59 beluga60)
		(next-flight-to-process beluga60 beluga61)
		(next-flight-to-process beluga61 beluga62)
		(next-flight-to-process beluga62 beluga63)
		(next-flight-to-process beluga63 beluga64)
		(next-flight-to-process beluga64 beluga65)
		(next-flight-to-process beluga65 beluga66)
		(next-flight-to-process beluga66 beluga67)
		(next-flight-to-process beluga67 beluga68)
		(next-flight-to-process beluga68 beluga69)
		(next-flight-to-process beluga69 beluga70)
		(next-flight-to-process beluga70 beluga71)
		(next-flight-to-process beluga71 beluga72)
		(next-flight-to-process beluga72 beluga73)
		(next-flight-to-process beluga73 beluga74)
		(next-flight-to-process beluga74 beluga75)
		(next-flight-to-process beluga75 beluga76)
		(next-flight-to-process beluga76 beluga77)
		(next-flight-to-process beluga77 beluga78)
		(next-flight-to-process beluga78 beluga79)
		(next-flight-to-process beluga79 beluga80)
		(next-flight-to-process beluga80 beluga81)
		(next-flight-to-process beluga81 beluga82)
		(next-flight-to-process beluga82 beluga83)
		(next-flight-to-process beluga83 beluga84)
		(next-flight-to-process beluga84 beluga85)
		(next-flight-to-process beluga85 beluga86)
		(next-flight-to-process beluga86 beluga87)
		(next-flight-to-process beluga87 beluga88)
		(next-flight-to-process beluga88 beluga89)
		(next-flight-to-process beluga89 beluga90)
		(next-flight-to-process beluga90 beluga91)
		(next-flight-to-process beluga91 beluga92)
		(next-flight-to-process beluga92 beluga93)
		(next-flight-to-process beluga93 beluga94)
		(next-flight-to-process beluga94 beluga95)
		(next-flight-to-process beluga95 beluga96)
		(next-flight-to-process beluga96 beluga97)
		(next-flight-to-process beluga97 beluga98)
		(next-flight-to-process beluga98 beluga99)
		(next-flight-to-process beluga99 beluga100)
		(next-flight-to-process beluga100 beluga101)
		(next-flight-to-process beluga101 beluga102)
		(next-flight-to-process beluga102 beluga103)
		(next-flight-to-process beluga103 beluga104)
		(next-flight-to-process beluga104 beluga105)
		(next-flight-to-process beluga105 beluga106)
		(next-flight-to-process beluga106 beluga107)
		(next-flight-to-process beluga107 beluga108)
		(next-flight-to-process beluga108 beluga109)
		(next-flight-to-process beluga109 beluga110)
		(next-flight-to-process beluga110 beluga111)
		(next-flight-to-process beluga111 beluga112)
		(next-flight-to-process beluga112 beluga113)
		(next-flight-to-process beluga113 beluga114)
		(next-flight-to-process beluga114 beluga115)
		(next-flight-to-process beluga115 beluga116)
		(next-flight-to-process beluga116 beluga117)
		(next-flight-to-process beluga117 beluga118)
		(next-flight-to-process beluga118 beluga119)
		(next-flight-to-process beluga119 beluga120)
		(next-flight-to-process beluga120 beluga121)
		(next-flight-to-process beluga121 beluga122)
		(next-flight-to-process beluga122 beluga123)
		(next-flight-to-process beluga123 beluga124)
		(next-flight-to-process beluga124 beluga125)
		(next-flight-to-process beluga125 beluga126)
		(next-flight-to-process beluga126 beluga127)
		(next-flight-to-process beluga127 beluga128)
		(next-flight-to-process beluga128 beluga129)
		(next-flight-to-process beluga129 beluga130)
		(next-flight-to-process beluga130 beluga131)
		(next-flight-to-process beluga131 beluga132)
		(next-flight-to-process beluga132 beluga133)
		(next-flight-to-process beluga133 beluga134)
		(next-flight-to-process beluga134 beluga135)
		(next-flight-to-process beluga135 beluga136)
		(next-flight-to-process beluga136 beluga137)
		(next-flight-to-process beluga137 beluga138)
		(next-flight-to-process beluga138 beluga139)
		(next-flight-to-process beluga139 beluga140)
		(next-flight-to-process beluga140 beluga141)
		(next-flight-to-process beluga141 beluga142)
		(next-flight-to-process beluga142 beluga143)
		(next-flight-to-process beluga143 beluga144)
		(next-flight-to-process beluga144 beluga145)
		(next-flight-to-process beluga145 beluga146)
		(next-flight-to-process beluga146 beluga147)
		(next-flight-to-process beluga147 beluga148)
		(next-flight-to-process beluga148 beluga149)
		(next-flight-to-process beluga149 beluga150)
		(next-flight-to-process beluga150 beluga151)
		(next-flight-to-process beluga151 beluga152)
		(next-flight-to-process beluga152 beluga153)
		(next-flight-to-process beluga153 beluga154)
		(next-flight-to-process beluga154 beluga155)
		(next-flight-to-process beluga155 beluga156)
		(next-flight-to-process beluga156 beluga157)
		(next-flight-to-process beluga157 beluga158)
		(next-flight-to-process beluga158 beluga159)
		(next-flight-to-process beluga159 beluga160)
		(next-flight-to-process beluga160 beluga161)
		(next-flight-to-process beluga161 beluga162)
		(next-flight-to-process beluga162 beluga163)
		(next-flight-to-process beluga163 beluga164)
		(next-flight-to-process beluga164 beluga165)
		(next-flight-to-process beluga165 beluga166)
		(next-flight-to-process beluga166 beluga167)
		(next-flight-to-process beluga167 beluga168)
		(next-flight-to-process beluga168 beluga169)
		(next-flight-to-process beluga169 beluga170)
		(next-flight-to-process beluga170 beluga171)
		(next-flight-to-process beluga171 beluga172)
		(next-flight-to-process beluga172 beluga173)
		(next-flight-to-process beluga173 beluga174)
		(next-flight-to-process beluga174 beluga175)
		(next-flight-to-process beluga175 beluga176)
		(next-flight-to-process beluga176 beluga177)
		(next-flight-to-process beluga177 beluga178)
		(next-flight-to-process beluga178 beluga179)
		(next-flight-to-process beluga179 beluga180)
		(next-flight-to-process beluga180 beluga181)
		(next-flight-to-process beluga181 beluga182)
		(next-flight-to-process beluga182 beluga183)
		(next-flight-to-process beluga183 beluga184)
		(next-flight-to-process beluga184 beluga185)
		(next-flight-to-process beluga185 beluga186)
		(next-flight-to-process beluga186 beluga187)
		(next-flight-to-process beluga187 beluga188)
		(next-flight-to-process beluga188 beluga189)
		(next-flight-to-process beluga189 beluga190)
		(next-flight-to-process beluga190 beluga191)
		(next-flight-to-process beluga191 beluga192)
		; Number of flights: 192
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; No jigs
		(to_unload dummy-jig beluga1)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0014 1: jig0015
		(to_unload jig0014 beluga2)
		(in jig0014 beluga2)
		(next_unload jig0014 jig0015)
		(in jig0015 beluga2)
		(next_unload jig0015 dummy-jig)
		; Flight: beluga3
		; No jigs
		(to_unload dummy-jig beluga3)
		; Flight: beluga4
		; 0: jig0016
		(to_unload jig0016 beluga4)
		(in jig0016 beluga4)
		(next_unload jig0016 dummy-jig)
		; Flight: beluga5
		; 0: jig0017 1: jig0018 2: jig0019
		(to_unload jig0017 beluga5)
		(in jig0017 beluga5)
		(next_unload jig0017 jig0018)
		(in jig0018 beluga5)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga5)
		(next_unload jig0019 dummy-jig)
		; Flight: beluga6
		; 0: jig0020 1: jig0021 2: jig0022
		(to_unload jig0020 beluga6)
		(in jig0020 beluga6)
		(next_unload jig0020 jig0021)
		(in jig0021 beluga6)
		(next_unload jig0021 jig0022)
		(in jig0022 beluga6)
		(next_unload jig0022 dummy-jig)
		; Flight: beluga7
		; 0: jig0023 1: jig0024
		(to_unload jig0023 beluga7)
		(in jig0023 beluga7)
		(next_unload jig0023 jig0024)
		(in jig0024 beluga7)
		(next_unload jig0024 dummy-jig)
		; Flight: beluga8
		; 0: jig0025
		(to_unload jig0025 beluga8)
		(in jig0025 beluga8)
		(next_unload jig0025 dummy-jig)
		; Flight: beluga9
		; 0: jig0026 1: jig0027 2: jig0028
		(to_unload jig0026 beluga9)
		(in jig0026 beluga9)
		(next_unload jig0026 jig0027)
		(in jig0027 beluga9)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga9)
		(next_unload jig0028 dummy-jig)
		; Flight: beluga10
		; 0: jig0029 1: jig0030
		(to_unload jig0029 beluga10)
		(in jig0029 beluga10)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga10)
		(next_unload jig0030 dummy-jig)
		; Flight: beluga11
		; 0: jig0031 1: jig0032
		(to_unload jig0031 beluga11)
		(in jig0031 beluga11)
		(next_unload jig0031 jig0032)
		(in jig0032 beluga11)
		(next_unload jig0032 dummy-jig)
		; Flight: beluga12
		; 0: jig0033
		(to_unload jig0033 beluga12)
		(in jig0033 beluga12)
		(next_unload jig0033 dummy-jig)
		; Flight: beluga13
		; 0: jig0034
		(to_unload jig0034 beluga13)
		(in jig0034 beluga13)
		(next_unload jig0034 dummy-jig)
		; Flight: beluga14
		; 0: jig0035 1: jig0036 2: jig0037 3: jig0038 4: jig0039 5: jig0040 6: jig0041 7: jig0042 8: jig0043 9: jig0044
		(to_unload jig0035 beluga14)
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
		(next_unload jig0040 jig0041)
		(in jig0041 beluga14)
		(next_unload jig0041 jig0042)
		(in jig0042 beluga14)
		(next_unload jig0042 jig0043)
		(in jig0043 beluga14)
		(next_unload jig0043 jig0044)
		(in jig0044 beluga14)
		(next_unload jig0044 dummy-jig)
		; Flight: beluga15
		; 0: jig0045
		(to_unload jig0045 beluga15)
		(in jig0045 beluga15)
		(next_unload jig0045 dummy-jig)
		; Flight: beluga16
		; 0: jig0046 1: jig0047 2: jig0048 3: jig0049 4: jig0050 5: jig0051 6: jig0052 7: jig0053 8: jig0054 9: jig0055
		(to_unload jig0046 beluga16)
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
		(next_unload jig0052 jig0053)
		(in jig0053 beluga16)
		(next_unload jig0053 jig0054)
		(in jig0054 beluga16)
		(next_unload jig0054 jig0055)
		(in jig0055 beluga16)
		(next_unload jig0055 dummy-jig)
		; Flight: beluga17
		; 0: jig0056 1: jig0057 2: jig0058 3: jig0059 4: jig0060 5: jig0061 6: jig0062 7: jig0063 8: jig0064 9: jig0065
		(to_unload jig0056 beluga17)
		(in jig0056 beluga17)
		(next_unload jig0056 jig0057)
		(in jig0057 beluga17)
		(next_unload jig0057 jig0058)
		(in jig0058 beluga17)
		(next_unload jig0058 jig0059)
		(in jig0059 beluga17)
		(next_unload jig0059 jig0060)
		(in jig0060 beluga17)
		(next_unload jig0060 jig0061)
		(in jig0061 beluga17)
		(next_unload jig0061 jig0062)
		(in jig0062 beluga17)
		(next_unload jig0062 jig0063)
		(in jig0063 beluga17)
		(next_unload jig0063 jig0064)
		(in jig0064 beluga17)
		(next_unload jig0064 jig0065)
		(in jig0065 beluga17)
		(next_unload jig0065 dummy-jig)
		; Flight: beluga18
		; 0: jig0066
		(to_unload jig0066 beluga18)
		(in jig0066 beluga18)
		(next_unload jig0066 dummy-jig)
		; Flight: beluga19
		; 0: jig0067
		(to_unload jig0067 beluga19)
		(in jig0067 beluga19)
		(next_unload jig0067 dummy-jig)
		; Flight: beluga20
		; 0: jig0068 1: jig0069 2: jig0070
		(to_unload jig0068 beluga20)
		(in jig0068 beluga20)
		(next_unload jig0068 jig0069)
		(in jig0069 beluga20)
		(next_unload jig0069 jig0070)
		(in jig0070 beluga20)
		(next_unload jig0070 dummy-jig)
		; Flight: beluga21
		; 0: jig0071 1: jig0072 2: jig0073 3: jig0074 4: jig0075 5: jig0076 6: jig0077 7: jig0078 8: jig0079 9: jig0080
		(to_unload jig0071 beluga21)
		(in jig0071 beluga21)
		(next_unload jig0071 jig0072)
		(in jig0072 beluga21)
		(next_unload jig0072 jig0073)
		(in jig0073 beluga21)
		(next_unload jig0073 jig0074)
		(in jig0074 beluga21)
		(next_unload jig0074 jig0075)
		(in jig0075 beluga21)
		(next_unload jig0075 jig0076)
		(in jig0076 beluga21)
		(next_unload jig0076 jig0077)
		(in jig0077 beluga21)
		(next_unload jig0077 jig0078)
		(in jig0078 beluga21)
		(next_unload jig0078 jig0079)
		(in jig0079 beluga21)
		(next_unload jig0079 jig0080)
		(in jig0080 beluga21)
		(next_unload jig0080 dummy-jig)
		; Flight: beluga22
		; 0: jig0081
		(to_unload jig0081 beluga22)
		(in jig0081 beluga22)
		(next_unload jig0081 dummy-jig)
		; Flight: beluga23
		; 0: jig0082
		(to_unload jig0082 beluga23)
		(in jig0082 beluga23)
		(next_unload jig0082 dummy-jig)
		; Flight: beluga24
		; 0: jig0083
		(to_unload jig0083 beluga24)
		(in jig0083 beluga24)
		(next_unload jig0083 dummy-jig)
		; Flight: beluga25
		; 0: jig0084 1: jig0085
		(to_unload jig0084 beluga25)
		(in jig0084 beluga25)
		(next_unload jig0084 jig0085)
		(in jig0085 beluga25)
		(next_unload jig0085 dummy-jig)
		; Flight: beluga26
		; 0: jig0086
		(to_unload jig0086 beluga26)
		(in jig0086 beluga26)
		(next_unload jig0086 dummy-jig)
		; Flight: beluga27
		; 0: jig0087
		(to_unload jig0087 beluga27)
		(in jig0087 beluga27)
		(next_unload jig0087 dummy-jig)
		; Flight: beluga28
		; No jigs
		(to_unload dummy-jig beluga28)
		; Flight: beluga29
		; 0: jig0088
		(to_unload jig0088 beluga29)
		(in jig0088 beluga29)
		(next_unload jig0088 dummy-jig)
		; Flight: beluga30
		; 0: jig0089 1: jig0090
		(to_unload jig0089 beluga30)
		(in jig0089 beluga30)
		(next_unload jig0089 jig0090)
		(in jig0090 beluga30)
		(next_unload jig0090 dummy-jig)
		; Flight: beluga31
		; 0: jig0091 1: jig0092 2: jig0093
		(to_unload jig0091 beluga31)
		(in jig0091 beluga31)
		(next_unload jig0091 jig0092)
		(in jig0092 beluga31)
		(next_unload jig0092 jig0093)
		(in jig0093 beluga31)
		(next_unload jig0093 dummy-jig)
		; Flight: beluga32
		; 0: jig0094 1: jig0095
		(to_unload jig0094 beluga32)
		(in jig0094 beluga32)
		(next_unload jig0094 jig0095)
		(in jig0095 beluga32)
		(next_unload jig0095 dummy-jig)
		; Flight: beluga33
		; 0: jig0096 1: jig0097 2: jig0098 3: jig0099 4: jig0100 5: jig0101 6: jig0102 7: jig0103 8: jig0104 9: jig0105
		(to_unload jig0096 beluga33)
		(in jig0096 beluga33)
		(next_unload jig0096 jig0097)
		(in jig0097 beluga33)
		(next_unload jig0097 jig0098)
		(in jig0098 beluga33)
		(next_unload jig0098 jig0099)
		(in jig0099 beluga33)
		(next_unload jig0099 jig0100)
		(in jig0100 beluga33)
		(next_unload jig0100 jig0101)
		(in jig0101 beluga33)
		(next_unload jig0101 jig0102)
		(in jig0102 beluga33)
		(next_unload jig0102 jig0103)
		(in jig0103 beluga33)
		(next_unload jig0103 jig0104)
		(in jig0104 beluga33)
		(next_unload jig0104 jig0105)
		(in jig0105 beluga33)
		(next_unload jig0105 dummy-jig)
		; Flight: beluga34
		; 0: jig0106
		(to_unload jig0106 beluga34)
		(in jig0106 beluga34)
		(next_unload jig0106 dummy-jig)
		; Flight: beluga35
		; No jigs
		(to_unload dummy-jig beluga35)
		; Flight: beluga36
		; 0: jig0107
		(to_unload jig0107 beluga36)
		(in jig0107 beluga36)
		(next_unload jig0107 dummy-jig)
		; Flight: beluga37
		; 0: jig0108
		(to_unload jig0108 beluga37)
		(in jig0108 beluga37)
		(next_unload jig0108 dummy-jig)
		; Flight: beluga38
		; 0: jig0109
		(to_unload jig0109 beluga38)
		(in jig0109 beluga38)
		(next_unload jig0109 dummy-jig)
		; Flight: beluga39
		; No jigs
		(to_unload dummy-jig beluga39)
		; Flight: beluga40
		; 0: jig0110 1: jig0111
		(to_unload jig0110 beluga40)
		(in jig0110 beluga40)
		(next_unload jig0110 jig0111)
		(in jig0111 beluga40)
		(next_unload jig0111 dummy-jig)
		; Flight: beluga41
		; 0: jig0112 1: jig0113
		(to_unload jig0112 beluga41)
		(in jig0112 beluga41)
		(next_unload jig0112 jig0113)
		(in jig0113 beluga41)
		(next_unload jig0113 dummy-jig)
		; Flight: beluga42
		; 0: jig0114
		(to_unload jig0114 beluga42)
		(in jig0114 beluga42)
		(next_unload jig0114 dummy-jig)
		; Flight: beluga43
		; No jigs
		(to_unload dummy-jig beluga43)
		; Flight: beluga44
		; No jigs
		(to_unload dummy-jig beluga44)
		; Flight: beluga45
		; 0: jig0115
		(to_unload jig0115 beluga45)
		(in jig0115 beluga45)
		(next_unload jig0115 dummy-jig)
		; Flight: beluga46
		; No jigs
		(to_unload dummy-jig beluga46)
		; Flight: beluga47
		; 0: jig0116 1: jig0117
		(to_unload jig0116 beluga47)
		(in jig0116 beluga47)
		(next_unload jig0116 jig0117)
		(in jig0117 beluga47)
		(next_unload jig0117 dummy-jig)
		; Flight: beluga48
		; 0: jig0118
		(to_unload jig0118 beluga48)
		(in jig0118 beluga48)
		(next_unload jig0118 dummy-jig)
		; Flight: beluga49
		; 0: jig0119 1: jig0120 2: jig0121 3: jig0122 4: jig0123 5: jig0124 6: jig0125 7: jig0126 8: jig0127 9: jig0128
		(to_unload jig0119 beluga49)
		(in jig0119 beluga49)
		(next_unload jig0119 jig0120)
		(in jig0120 beluga49)
		(next_unload jig0120 jig0121)
		(in jig0121 beluga49)
		(next_unload jig0121 jig0122)
		(in jig0122 beluga49)
		(next_unload jig0122 jig0123)
		(in jig0123 beluga49)
		(next_unload jig0123 jig0124)
		(in jig0124 beluga49)
		(next_unload jig0124 jig0125)
		(in jig0125 beluga49)
		(next_unload jig0125 jig0126)
		(in jig0126 beluga49)
		(next_unload jig0126 jig0127)
		(in jig0127 beluga49)
		(next_unload jig0127 jig0128)
		(in jig0128 beluga49)
		(next_unload jig0128 dummy-jig)
		; Flight: beluga50
		; 0: jig0129
		(to_unload jig0129 beluga50)
		(in jig0129 beluga50)
		(next_unload jig0129 dummy-jig)
		; Flight: beluga51
		; 0: jig0130 1: jig0131
		(to_unload jig0130 beluga51)
		(in jig0130 beluga51)
		(next_unload jig0130 jig0131)
		(in jig0131 beluga51)
		(next_unload jig0131 dummy-jig)
		; Flight: beluga52
		; 0: jig0132
		(to_unload jig0132 beluga52)
		(in jig0132 beluga52)
		(next_unload jig0132 dummy-jig)
		; Flight: beluga53
		; 0: jig0133
		(to_unload jig0133 beluga53)
		(in jig0133 beluga53)
		(next_unload jig0133 dummy-jig)
		; Flight: beluga54
		; 0: jig0134 1: jig0135
		(to_unload jig0134 beluga54)
		(in jig0134 beluga54)
		(next_unload jig0134 jig0135)
		(in jig0135 beluga54)
		(next_unload jig0135 dummy-jig)
		; Flight: beluga55
		; 0: jig0136 1: jig0137
		(to_unload jig0136 beluga55)
		(in jig0136 beluga55)
		(next_unload jig0136 jig0137)
		(in jig0137 beluga55)
		(next_unload jig0137 dummy-jig)
		; Flight: beluga56
		; 0: jig0138
		(to_unload jig0138 beluga56)
		(in jig0138 beluga56)
		(next_unload jig0138 dummy-jig)
		; Flight: beluga57
		; 0: jig0139
		(to_unload jig0139 beluga57)
		(in jig0139 beluga57)
		(next_unload jig0139 dummy-jig)
		; Flight: beluga58
		; 0: jig0140 1: jig0141
		(to_unload jig0140 beluga58)
		(in jig0140 beluga58)
		(next_unload jig0140 jig0141)
		(in jig0141 beluga58)
		(next_unload jig0141 dummy-jig)
		; Flight: beluga59
		; No jigs
		(to_unload dummy-jig beluga59)
		; Flight: beluga60
		; No jigs
		(to_unload dummy-jig beluga60)
		; Flight: beluga61
		; 0: jig0142 1: jig0143
		(to_unload jig0142 beluga61)
		(in jig0142 beluga61)
		(next_unload jig0142 jig0143)
		(in jig0143 beluga61)
		(next_unload jig0143 dummy-jig)
		; Flight: beluga62
		; 0: jig0144
		(to_unload jig0144 beluga62)
		(in jig0144 beluga62)
		(next_unload jig0144 dummy-jig)
		; Flight: beluga63
		; 0: jig0145
		(to_unload jig0145 beluga63)
		(in jig0145 beluga63)
		(next_unload jig0145 dummy-jig)
		; Flight: beluga64
		; 0: jig0146
		(to_unload jig0146 beluga64)
		(in jig0146 beluga64)
		(next_unload jig0146 dummy-jig)
		; Flight: beluga65
		; No jigs
		(to_unload dummy-jig beluga65)
		; Flight: beluga66
		; 0: jig0147 1: jig0148 2: jig0149
		(to_unload jig0147 beluga66)
		(in jig0147 beluga66)
		(next_unload jig0147 jig0148)
		(in jig0148 beluga66)
		(next_unload jig0148 jig0149)
		(in jig0149 beluga66)
		(next_unload jig0149 dummy-jig)
		; Flight: beluga67
		; No jigs
		(to_unload dummy-jig beluga67)
		; Flight: beluga68
		; 0: jig0150
		(to_unload jig0150 beluga68)
		(in jig0150 beluga68)
		(next_unload jig0150 dummy-jig)
		; Flight: beluga69
		; No jigs
		(to_unload dummy-jig beluga69)
		; Flight: beluga70
		; 0: jig0151
		(to_unload jig0151 beluga70)
		(in jig0151 beluga70)
		(next_unload jig0151 dummy-jig)
		; Flight: beluga71
		; 0: jig0152
		(to_unload jig0152 beluga71)
		(in jig0152 beluga71)
		(next_unload jig0152 dummy-jig)
		; Flight: beluga72
		; 0: jig0153
		(to_unload jig0153 beluga72)
		(in jig0153 beluga72)
		(next_unload jig0153 dummy-jig)
		; Flight: beluga73
		; No jigs
		(to_unload dummy-jig beluga73)
		; Flight: beluga74
		; No jigs
		(to_unload dummy-jig beluga74)
		; Flight: beluga75
		; 0: jig0154
		(to_unload jig0154 beluga75)
		(in jig0154 beluga75)
		(next_unload jig0154 dummy-jig)
		; Flight: beluga76
		; No jigs
		(to_unload dummy-jig beluga76)
		; Flight: beluga77
		; 0: jig0155 1: jig0156 2: jig0157
		(to_unload jig0155 beluga77)
		(in jig0155 beluga77)
		(next_unload jig0155 jig0156)
		(in jig0156 beluga77)
		(next_unload jig0156 jig0157)
		(in jig0157 beluga77)
		(next_unload jig0157 dummy-jig)
		; Flight: beluga78
		; 0: jig0158
		(to_unload jig0158 beluga78)
		(in jig0158 beluga78)
		(next_unload jig0158 dummy-jig)
		; Flight: beluga79
		; 0: jig0159
		(to_unload jig0159 beluga79)
		(in jig0159 beluga79)
		(next_unload jig0159 dummy-jig)
		; Flight: beluga80
		; 0: jig0160 1: jig0161
		(to_unload jig0160 beluga80)
		(in jig0160 beluga80)
		(next_unload jig0160 jig0161)
		(in jig0161 beluga80)
		(next_unload jig0161 dummy-jig)
		; Flight: beluga81
		; 0: jig0162
		(to_unload jig0162 beluga81)
		(in jig0162 beluga81)
		(next_unload jig0162 dummy-jig)
		; Flight: beluga82
		; 0: jig0163
		(to_unload jig0163 beluga82)
		(in jig0163 beluga82)
		(next_unload jig0163 dummy-jig)
		; Flight: beluga83
		; No jigs
		(to_unload dummy-jig beluga83)
		; Flight: beluga84
		; 0: jig0164 1: jig0165
		(to_unload jig0164 beluga84)
		(in jig0164 beluga84)
		(next_unload jig0164 jig0165)
		(in jig0165 beluga84)
		(next_unload jig0165 dummy-jig)
		; Flight: beluga85
		; No jigs
		(to_unload dummy-jig beluga85)
		; Flight: beluga86
		; 0: jig0166
		(to_unload jig0166 beluga86)
		(in jig0166 beluga86)
		(next_unload jig0166 dummy-jig)
		; Flight: beluga87
		; 0: jig0167 1: jig0168
		(to_unload jig0167 beluga87)
		(in jig0167 beluga87)
		(next_unload jig0167 jig0168)
		(in jig0168 beluga87)
		(next_unload jig0168 dummy-jig)
		; Flight: beluga88
		; 0: jig0169
		(to_unload jig0169 beluga88)
		(in jig0169 beluga88)
		(next_unload jig0169 dummy-jig)
		; Flight: beluga89
		; No jigs
		(to_unload dummy-jig beluga89)
		; Flight: beluga90
		; No jigs
		(to_unload dummy-jig beluga90)
		; Flight: beluga91
		; 0: jig0170 1: jig0171
		(to_unload jig0170 beluga91)
		(in jig0170 beluga91)
		(next_unload jig0170 jig0171)
		(in jig0171 beluga91)
		(next_unload jig0171 dummy-jig)
		; Flight: beluga92
		; 0: jig0172 1: jig0173
		(to_unload jig0172 beluga92)
		(in jig0172 beluga92)
		(next_unload jig0172 jig0173)
		(in jig0173 beluga92)
		(next_unload jig0173 dummy-jig)
		; Flight: beluga93
		; 0: jig0174 1: jig0175 2: jig0176
		(to_unload jig0174 beluga93)
		(in jig0174 beluga93)
		(next_unload jig0174 jig0175)
		(in jig0175 beluga93)
		(next_unload jig0175 jig0176)
		(in jig0176 beluga93)
		(next_unload jig0176 dummy-jig)
		; Flight: beluga94
		; 0: jig0177 1: jig0178 2: jig0179 3: jig0180 4: jig0181 5: jig0182 6: jig0183 7: jig0184 8: jig0185 9: jig0186
		(to_unload jig0177 beluga94)
		(in jig0177 beluga94)
		(next_unload jig0177 jig0178)
		(in jig0178 beluga94)
		(next_unload jig0178 jig0179)
		(in jig0179 beluga94)
		(next_unload jig0179 jig0180)
		(in jig0180 beluga94)
		(next_unload jig0180 jig0181)
		(in jig0181 beluga94)
		(next_unload jig0181 jig0182)
		(in jig0182 beluga94)
		(next_unload jig0182 jig0183)
		(in jig0183 beluga94)
		(next_unload jig0183 jig0184)
		(in jig0184 beluga94)
		(next_unload jig0184 jig0185)
		(in jig0185 beluga94)
		(next_unload jig0185 jig0186)
		(in jig0186 beluga94)
		(next_unload jig0186 dummy-jig)
		; Flight: beluga95
		; 0: jig0187
		(to_unload jig0187 beluga95)
		(in jig0187 beluga95)
		(next_unload jig0187 dummy-jig)
		; Flight: beluga96
		; 0: jig0188 1: jig0189 2: jig0190
		(to_unload jig0188 beluga96)
		(in jig0188 beluga96)
		(next_unload jig0188 jig0189)
		(in jig0189 beluga96)
		(next_unload jig0189 jig0190)
		(in jig0190 beluga96)
		(next_unload jig0190 dummy-jig)
		; Flight: beluga97
		; 0: jig0191
		(to_unload jig0191 beluga97)
		(in jig0191 beluga97)
		(next_unload jig0191 dummy-jig)
		; Flight: beluga98
		; 0: jig0192
		(to_unload jig0192 beluga98)
		(in jig0192 beluga98)
		(next_unload jig0192 dummy-jig)
		; Flight: beluga99
		; 0: jig0193
		(to_unload jig0193 beluga99)
		(in jig0193 beluga99)
		(next_unload jig0193 dummy-jig)
		; Flight: beluga100
		; 0: jig0194
		(to_unload jig0194 beluga100)
		(in jig0194 beluga100)
		(next_unload jig0194 dummy-jig)
		; Flight: beluga101
		; No jigs
		(to_unload dummy-jig beluga101)
		; Flight: beluga102
		; 0: jig0195 1: jig0196 2: jig0197
		(to_unload jig0195 beluga102)
		(in jig0195 beluga102)
		(next_unload jig0195 jig0196)
		(in jig0196 beluga102)
		(next_unload jig0196 jig0197)
		(in jig0197 beluga102)
		(next_unload jig0197 dummy-jig)
		; Flight: beluga103
		; 0: jig0198
		(to_unload jig0198 beluga103)
		(in jig0198 beluga103)
		(next_unload jig0198 dummy-jig)
		; Flight: beluga104
		; 0: jig0199 1: jig0200 2: jig0201
		(to_unload jig0199 beluga104)
		(in jig0199 beluga104)
		(next_unload jig0199 jig0200)
		(in jig0200 beluga104)
		(next_unload jig0200 jig0201)
		(in jig0201 beluga104)
		(next_unload jig0201 dummy-jig)
		; Flight: beluga105
		; 0: jig0202 1: jig0203
		(to_unload jig0202 beluga105)
		(in jig0202 beluga105)
		(next_unload jig0202 jig0203)
		(in jig0203 beluga105)
		(next_unload jig0203 dummy-jig)
		; Flight: beluga106
		; 0: jig0204 1: jig0205 2: jig0206 3: jig0207 4: jig0208 5: jig0209 6: jig0210 7: jig0211 8: jig0212 9: jig0213
		(to_unload jig0204 beluga106)
		(in jig0204 beluga106)
		(next_unload jig0204 jig0205)
		(in jig0205 beluga106)
		(next_unload jig0205 jig0206)
		(in jig0206 beluga106)
		(next_unload jig0206 jig0207)
		(in jig0207 beluga106)
		(next_unload jig0207 jig0208)
		(in jig0208 beluga106)
		(next_unload jig0208 jig0209)
		(in jig0209 beluga106)
		(next_unload jig0209 jig0210)
		(in jig0210 beluga106)
		(next_unload jig0210 jig0211)
		(in jig0211 beluga106)
		(next_unload jig0211 jig0212)
		(in jig0212 beluga106)
		(next_unload jig0212 jig0213)
		(in jig0213 beluga106)
		(next_unload jig0213 dummy-jig)
		; Flight: beluga107
		; 0: jig0214
		(to_unload jig0214 beluga107)
		(in jig0214 beluga107)
		(next_unload jig0214 dummy-jig)
		; Flight: beluga108
		; 0: jig0215
		(to_unload jig0215 beluga108)
		(in jig0215 beluga108)
		(next_unload jig0215 dummy-jig)
		; Flight: beluga109
		; 0: jig0216 1: jig0217 2: jig0218 3: jig0219 4: jig0220 5: jig0221 6: jig0222
		(to_unload jig0216 beluga109)
		(in jig0216 beluga109)
		(next_unload jig0216 jig0217)
		(in jig0217 beluga109)
		(next_unload jig0217 jig0218)
		(in jig0218 beluga109)
		(next_unload jig0218 jig0219)
		(in jig0219 beluga109)
		(next_unload jig0219 jig0220)
		(in jig0220 beluga109)
		(next_unload jig0220 jig0221)
		(in jig0221 beluga109)
		(next_unload jig0221 jig0222)
		(in jig0222 beluga109)
		(next_unload jig0222 dummy-jig)
		; Flight: beluga110
		; 0: jig0223
		(to_unload jig0223 beluga110)
		(in jig0223 beluga110)
		(next_unload jig0223 dummy-jig)
		; Flight: beluga111
		; 0: jig0224 1: jig0225
		(to_unload jig0224 beluga111)
		(in jig0224 beluga111)
		(next_unload jig0224 jig0225)
		(in jig0225 beluga111)
		(next_unload jig0225 dummy-jig)
		; Flight: beluga112
		; 0: jig0226
		(to_unload jig0226 beluga112)
		(in jig0226 beluga112)
		(next_unload jig0226 dummy-jig)
		; Flight: beluga113
		; No jigs
		(to_unload dummy-jig beluga113)
		; Flight: beluga114
		; 0: jig0227
		(to_unload jig0227 beluga114)
		(in jig0227 beluga114)
		(next_unload jig0227 dummy-jig)
		; Flight: beluga115
		; 0: jig0228 1: jig0229 2: jig0230
		(to_unload jig0228 beluga115)
		(in jig0228 beluga115)
		(next_unload jig0228 jig0229)
		(in jig0229 beluga115)
		(next_unload jig0229 jig0230)
		(in jig0230 beluga115)
		(next_unload jig0230 dummy-jig)
		; Flight: beluga116
		; No jigs
		(to_unload dummy-jig beluga116)
		; Flight: beluga117
		; No jigs
		(to_unload dummy-jig beluga117)
		; Flight: beluga118
		; 0: jig0231 1: jig0232
		(to_unload jig0231 beluga118)
		(in jig0231 beluga118)
		(next_unload jig0231 jig0232)
		(in jig0232 beluga118)
		(next_unload jig0232 dummy-jig)
		; Flight: beluga119
		; No jigs
		(to_unload dummy-jig beluga119)
		; Flight: beluga120
		; No jigs
		(to_unload dummy-jig beluga120)
		; Flight: beluga121
		; 0: jig0233
		(to_unload jig0233 beluga121)
		(in jig0233 beluga121)
		(next_unload jig0233 dummy-jig)
		; Flight: beluga122
		; No jigs
		(to_unload dummy-jig beluga122)
		; Flight: beluga123
		; 0: jig0234 1: jig0235 2: jig0236
		(to_unload jig0234 beluga123)
		(in jig0234 beluga123)
		(next_unload jig0234 jig0235)
		(in jig0235 beluga123)
		(next_unload jig0235 jig0236)
		(in jig0236 beluga123)
		(next_unload jig0236 dummy-jig)
		; Flight: beluga124
		; 0: jig0237
		(to_unload jig0237 beluga124)
		(in jig0237 beluga124)
		(next_unload jig0237 dummy-jig)
		; Flight: beluga125
		; No jigs
		(to_unload dummy-jig beluga125)
		; Flight: beluga126
		; No jigs
		(to_unload dummy-jig beluga126)
		; Flight: beluga127
		; 0: jig0238 1: jig0239
		(to_unload jig0238 beluga127)
		(in jig0238 beluga127)
		(next_unload jig0238 jig0239)
		(in jig0239 beluga127)
		(next_unload jig0239 dummy-jig)
		; Flight: beluga128
		; No jigs
		(to_unload dummy-jig beluga128)
		; Flight: beluga129
		; 0: jig0240
		(to_unload jig0240 beluga129)
		(in jig0240 beluga129)
		(next_unload jig0240 dummy-jig)
		; Flight: beluga130
		; No jigs
		(to_unload dummy-jig beluga130)
		; Flight: beluga131
		; No jigs
		(to_unload dummy-jig beluga131)
		; Flight: beluga132
		; 0: jig0241 1: jig0242 2: jig0243
		(to_unload jig0241 beluga132)
		(in jig0241 beluga132)
		(next_unload jig0241 jig0242)
		(in jig0242 beluga132)
		(next_unload jig0242 jig0243)
		(in jig0243 beluga132)
		(next_unload jig0243 dummy-jig)
		; Flight: beluga133
		; 0: jig0244
		(to_unload jig0244 beluga133)
		(in jig0244 beluga133)
		(next_unload jig0244 dummy-jig)
		; Flight: beluga134
		; 0: jig0245
		(to_unload jig0245 beluga134)
		(in jig0245 beluga134)
		(next_unload jig0245 dummy-jig)
		; Flight: beluga135
		; No jigs
		(to_unload dummy-jig beluga135)
		; Flight: beluga136
		; 0: jig0246
		(to_unload jig0246 beluga136)
		(in jig0246 beluga136)
		(next_unload jig0246 dummy-jig)
		; Flight: beluga137
		; 0: jig0247 1: jig0248
		(to_unload jig0247 beluga137)
		(in jig0247 beluga137)
		(next_unload jig0247 jig0248)
		(in jig0248 beluga137)
		(next_unload jig0248 dummy-jig)
		; Flight: beluga138
		; No jigs
		(to_unload dummy-jig beluga138)
		; Flight: beluga139
		; 0: jig0249
		(to_unload jig0249 beluga139)
		(in jig0249 beluga139)
		(next_unload jig0249 dummy-jig)
		; Flight: beluga140
		; No jigs
		(to_unload dummy-jig beluga140)
		; Flight: beluga141
		; No jigs
		(to_unload dummy-jig beluga141)
		; Flight: beluga142
		; No jigs
		(to_unload dummy-jig beluga142)
		; Flight: beluga143
		; 0: jig0250 1: jig0251 2: jig0252 3: jig0253 4: jig0254 5: jig0255 6: jig0256 7: jig0257 8: jig0258 9: jig0259
		(to_unload jig0250 beluga143)
		(in jig0250 beluga143)
		(next_unload jig0250 jig0251)
		(in jig0251 beluga143)
		(next_unload jig0251 jig0252)
		(in jig0252 beluga143)
		(next_unload jig0252 jig0253)
		(in jig0253 beluga143)
		(next_unload jig0253 jig0254)
		(in jig0254 beluga143)
		(next_unload jig0254 jig0255)
		(in jig0255 beluga143)
		(next_unload jig0255 jig0256)
		(in jig0256 beluga143)
		(next_unload jig0256 jig0257)
		(in jig0257 beluga143)
		(next_unload jig0257 jig0258)
		(in jig0258 beluga143)
		(next_unload jig0258 jig0259)
		(in jig0259 beluga143)
		(next_unload jig0259 dummy-jig)
		; Flight: beluga144
		; 0: jig0260
		(to_unload jig0260 beluga144)
		(in jig0260 beluga144)
		(next_unload jig0260 dummy-jig)
		; Flight: beluga145
		; 0: jig0261
		(to_unload jig0261 beluga145)
		(in jig0261 beluga145)
		(next_unload jig0261 dummy-jig)
		; Flight: beluga146
		; 0: jig0262
		(to_unload jig0262 beluga146)
		(in jig0262 beluga146)
		(next_unload jig0262 dummy-jig)
		; Flight: beluga147
		; 0: jig0263
		(to_unload jig0263 beluga147)
		(in jig0263 beluga147)
		(next_unload jig0263 dummy-jig)
		; Flight: beluga148
		; 0: jig0264
		(to_unload jig0264 beluga148)
		(in jig0264 beluga148)
		(next_unload jig0264 dummy-jig)
		; Flight: beluga149
		; 0: jig0265 1: jig0266
		(to_unload jig0265 beluga149)
		(in jig0265 beluga149)
		(next_unload jig0265 jig0266)
		(in jig0266 beluga149)
		(next_unload jig0266 dummy-jig)
		; Flight: beluga150
		; No jigs
		(to_unload dummy-jig beluga150)
		; Flight: beluga151
		; 0: jig0267 1: jig0268 2: jig0269
		(to_unload jig0267 beluga151)
		(in jig0267 beluga151)
		(next_unload jig0267 jig0268)
		(in jig0268 beluga151)
		(next_unload jig0268 jig0269)
		(in jig0269 beluga151)
		(next_unload jig0269 dummy-jig)
		; Flight: beluga152
		; 0: jig0270
		(to_unload jig0270 beluga152)
		(in jig0270 beluga152)
		(next_unload jig0270 dummy-jig)
		; Flight: beluga153
		; 0: jig0271 1: jig0272 2: jig0273
		(to_unload jig0271 beluga153)
		(in jig0271 beluga153)
		(next_unload jig0271 jig0272)
		(in jig0272 beluga153)
		(next_unload jig0272 jig0273)
		(in jig0273 beluga153)
		(next_unload jig0273 dummy-jig)
		; Flight: beluga154
		; 0: jig0274 1: jig0275 2: jig0276 3: jig0277 4: jig0278 5: jig0279 6: jig0280 7: jig0281 8: jig0282 9: jig0283
		(to_unload jig0274 beluga154)
		(in jig0274 beluga154)
		(next_unload jig0274 jig0275)
		(in jig0275 beluga154)
		(next_unload jig0275 jig0276)
		(in jig0276 beluga154)
		(next_unload jig0276 jig0277)
		(in jig0277 beluga154)
		(next_unload jig0277 jig0278)
		(in jig0278 beluga154)
		(next_unload jig0278 jig0279)
		(in jig0279 beluga154)
		(next_unload jig0279 jig0280)
		(in jig0280 beluga154)
		(next_unload jig0280 jig0281)
		(in jig0281 beluga154)
		(next_unload jig0281 jig0282)
		(in jig0282 beluga154)
		(next_unload jig0282 jig0283)
		(in jig0283 beluga154)
		(next_unload jig0283 dummy-jig)
		; Flight: beluga155
		; 0: jig0284 1: jig0285 2: jig0286 3: jig0287 4: jig0288 5: jig0289 6: jig0290 7: jig0291 8: jig0292 9: jig0293
		(to_unload jig0284 beluga155)
		(in jig0284 beluga155)
		(next_unload jig0284 jig0285)
		(in jig0285 beluga155)
		(next_unload jig0285 jig0286)
		(in jig0286 beluga155)
		(next_unload jig0286 jig0287)
		(in jig0287 beluga155)
		(next_unload jig0287 jig0288)
		(in jig0288 beluga155)
		(next_unload jig0288 jig0289)
		(in jig0289 beluga155)
		(next_unload jig0289 jig0290)
		(in jig0290 beluga155)
		(next_unload jig0290 jig0291)
		(in jig0291 beluga155)
		(next_unload jig0291 jig0292)
		(in jig0292 beluga155)
		(next_unload jig0292 jig0293)
		(in jig0293 beluga155)
		(next_unload jig0293 dummy-jig)
		; Flight: beluga156
		; 0: jig0294 1: jig0295
		(to_unload jig0294 beluga156)
		(in jig0294 beluga156)
		(next_unload jig0294 jig0295)
		(in jig0295 beluga156)
		(next_unload jig0295 dummy-jig)
		; Flight: beluga157
		; 0: jig0296 1: jig0297
		(to_unload jig0296 beluga157)
		(in jig0296 beluga157)
		(next_unload jig0296 jig0297)
		(in jig0297 beluga157)
		(next_unload jig0297 dummy-jig)
		; Flight: beluga158
		; 0: jig0298 1: jig0299
		(to_unload jig0298 beluga158)
		(in jig0298 beluga158)
		(next_unload jig0298 jig0299)
		(in jig0299 beluga158)
		(next_unload jig0299 dummy-jig)
		; Flight: beluga159
		; 0: jig0300 1: jig0301 2: jig0302
		(to_unload jig0300 beluga159)
		(in jig0300 beluga159)
		(next_unload jig0300 jig0301)
		(in jig0301 beluga159)
		(next_unload jig0301 jig0302)
		(in jig0302 beluga159)
		(next_unload jig0302 dummy-jig)
		; Flight: beluga160
		; 0: jig0303 1: jig0304
		(to_unload jig0303 beluga160)
		(in jig0303 beluga160)
		(next_unload jig0303 jig0304)
		(in jig0304 beluga160)
		(next_unload jig0304 dummy-jig)
		; Flight: beluga161
		; 0: jig0305
		(to_unload jig0305 beluga161)
		(in jig0305 beluga161)
		(next_unload jig0305 dummy-jig)
		; Flight: beluga162
		; No jigs
		(to_unload dummy-jig beluga162)
		; Flight: beluga163
		; No jigs
		(to_unload dummy-jig beluga163)
		; Flight: beluga164
		; No jigs
		(to_unload dummy-jig beluga164)
		; Flight: beluga165
		; 0: jig0306
		(to_unload jig0306 beluga165)
		(in jig0306 beluga165)
		(next_unload jig0306 dummy-jig)
		; Flight: beluga166
		; 0: jig0307 1: jig0308
		(to_unload jig0307 beluga166)
		(in jig0307 beluga166)
		(next_unload jig0307 jig0308)
		(in jig0308 beluga166)
		(next_unload jig0308 dummy-jig)
		; Flight: beluga167
		; 0: jig0309 1: jig0310 2: jig0311
		(to_unload jig0309 beluga167)
		(in jig0309 beluga167)
		(next_unload jig0309 jig0310)
		(in jig0310 beluga167)
		(next_unload jig0310 jig0311)
		(in jig0311 beluga167)
		(next_unload jig0311 dummy-jig)
		; Flight: beluga168
		; No jigs
		(to_unload dummy-jig beluga168)
		; Flight: beluga169
		; 0: jig0312
		(to_unload jig0312 beluga169)
		(in jig0312 beluga169)
		(next_unload jig0312 dummy-jig)
		; Flight: beluga170
		; 0: jig0313 1: jig0314
		(to_unload jig0313 beluga170)
		(in jig0313 beluga170)
		(next_unload jig0313 jig0314)
		(in jig0314 beluga170)
		(next_unload jig0314 dummy-jig)
		; Flight: beluga171
		; No jigs
		(to_unload dummy-jig beluga171)
		; Flight: beluga172
		; 0: jig0315 1: jig0316 2: jig0317 3: jig0318 4: jig0319 5: jig0320 6: jig0321 7: jig0322 8: jig0323 9: jig0324
		(to_unload jig0315 beluga172)
		(in jig0315 beluga172)
		(next_unload jig0315 jig0316)
		(in jig0316 beluga172)
		(next_unload jig0316 jig0317)
		(in jig0317 beluga172)
		(next_unload jig0317 jig0318)
		(in jig0318 beluga172)
		(next_unload jig0318 jig0319)
		(in jig0319 beluga172)
		(next_unload jig0319 jig0320)
		(in jig0320 beluga172)
		(next_unload jig0320 jig0321)
		(in jig0321 beluga172)
		(next_unload jig0321 jig0322)
		(in jig0322 beluga172)
		(next_unload jig0322 jig0323)
		(in jig0323 beluga172)
		(next_unload jig0323 jig0324)
		(in jig0324 beluga172)
		(next_unload jig0324 dummy-jig)
		; Flight: beluga173
		; 0: jig0325
		(to_unload jig0325 beluga173)
		(in jig0325 beluga173)
		(next_unload jig0325 dummy-jig)
		; Flight: beluga174
		; 0: jig0326
		(to_unload jig0326 beluga174)
		(in jig0326 beluga174)
		(next_unload jig0326 dummy-jig)
		; Flight: beluga175
		; 0: jig0327 1: jig0328
		(to_unload jig0327 beluga175)
		(in jig0327 beluga175)
		(next_unload jig0327 jig0328)
		(in jig0328 beluga175)
		(next_unload jig0328 dummy-jig)
		; Flight: beluga176
		; 0: jig0329 1: jig0330 2: jig0331 3: jig0332 4: jig0333 5: jig0334 6: jig0335 7: jig0336 8: jig0337 9: jig0338
		(to_unload jig0329 beluga176)
		(in jig0329 beluga176)
		(next_unload jig0329 jig0330)
		(in jig0330 beluga176)
		(next_unload jig0330 jig0331)
		(in jig0331 beluga176)
		(next_unload jig0331 jig0332)
		(in jig0332 beluga176)
		(next_unload jig0332 jig0333)
		(in jig0333 beluga176)
		(next_unload jig0333 jig0334)
		(in jig0334 beluga176)
		(next_unload jig0334 jig0335)
		(in jig0335 beluga176)
		(next_unload jig0335 jig0336)
		(in jig0336 beluga176)
		(next_unload jig0336 jig0337)
		(in jig0337 beluga176)
		(next_unload jig0337 jig0338)
		(in jig0338 beluga176)
		(next_unload jig0338 dummy-jig)
		; Flight: beluga177
		; 0: jig0339
		(to_unload jig0339 beluga177)
		(in jig0339 beluga177)
		(next_unload jig0339 dummy-jig)
		; Flight: beluga178
		; No jigs
		(to_unload dummy-jig beluga178)
		; Flight: beluga179
		; 0: jig0340 1: jig0341
		(to_unload jig0340 beluga179)
		(in jig0340 beluga179)
		(next_unload jig0340 jig0341)
		(in jig0341 beluga179)
		(next_unload jig0341 dummy-jig)
		; Flight: beluga180
		; 0: jig0342
		(to_unload jig0342 beluga180)
		(in jig0342 beluga180)
		(next_unload jig0342 dummy-jig)
		; Flight: beluga181
		; No jigs
		(to_unload dummy-jig beluga181)
		; Flight: beluga182
		; 0: jig0343 1: jig0344
		(to_unload jig0343 beluga182)
		(in jig0343 beluga182)
		(next_unload jig0343 jig0344)
		(in jig0344 beluga182)
		(next_unload jig0344 dummy-jig)
		; Flight: beluga183
		; No jigs
		(to_unload dummy-jig beluga183)
		; Flight: beluga184
		; 0: jig0345
		(to_unload jig0345 beluga184)
		(in jig0345 beluga184)
		(next_unload jig0345 dummy-jig)
		; Flight: beluga185
		; No jigs
		(to_unload dummy-jig beluga185)
		; Flight: beluga186
		; 0: jig0346
		(to_unload jig0346 beluga186)
		(in jig0346 beluga186)
		(next_unload jig0346 dummy-jig)
		; Flight: beluga187
		; 0: jig0347
		(to_unload jig0347 beluga187)
		(in jig0347 beluga187)
		(next_unload jig0347 dummy-jig)
		; Flight: beluga188
		; No jigs
		(to_unload dummy-jig beluga188)
		; Flight: beluga189
		; No jigs
		(to_unload dummy-jig beluga189)
		; Flight: beluga190
		; 0: jig0348
		(to_unload jig0348 beluga190)
		(in jig0348 beluga190)
		(next_unload jig0348 dummy-jig)
		; Flight: beluga191
		; No jigs
		(to_unload dummy-jig beluga191)
		; Flight: beluga192
		; No jigs
		(to_unload dummy-jig beluga192)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeB)
		(to_load typeB slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga2)
		(next_load typeD slot0 slot1 beluga2)
		(next_load dummy-type slot1 dummy-slot beluga2)
		; 0: typeC
		(to_load typeC slot0 beluga3)
		(next_load dummy-type slot0 dummy-slot beluga3)
		; 0: typeC
		(to_load typeC slot0 beluga4)
		(next_load dummy-type slot0 dummy-slot beluga4)
		; 0: typeE
		(to_load typeE slot0 beluga5)
		(next_load dummy-type slot0 dummy-slot beluga5)
		; 0: typeE
		(to_load typeE slot0 beluga6)
		(next_load dummy-type slot0 dummy-slot beluga6)
		; 0: typeD
		(to_load typeD slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; 0: typeD
		(to_load typeD slot0 beluga8)
		(next_load dummy-type slot0 dummy-slot beluga8)
		; 0: typeC
		(to_load typeC slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeE
		(to_load typeE slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeE
		(to_load typeE slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeE
		(to_load typeE slot0 beluga12)
		(next_load dummy-type slot0 dummy-slot beluga12)
		; 0: typeB
		(to_load typeB slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeE
		(to_load typeE slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeC
		(to_load typeC slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeE
		(to_load typeE slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; 0: typeB
		(to_load typeB slot0 beluga17)
		(next_load dummy-type slot0 dummy-slot beluga17)
		; 0: typeA
		(to_load typeA slot0 beluga18)
		(next_load dummy-type slot0 dummy-slot beluga18)
		; 0: typeA
		(to_load typeA slot0 beluga19)
		(next_load dummy-type slot0 dummy-slot beluga19)
		; 0: typeB
		(to_load typeB slot0 beluga20)
		(next_load dummy-type slot0 dummy-slot beluga20)
		; 0: typeB
		(to_load typeB slot0 beluga21)
		(next_load dummy-type slot0 dummy-slot beluga21)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga22)
		(next_load typeA slot0 slot1 beluga22)
		(next_load typeA slot1 slot2 beluga22)
		(next_load typeA slot2 slot3 beluga22)
		(next_load typeA slot3 slot4 beluga22)
		(next_load dummy-type slot4 dummy-slot beluga22)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga23)
		(next_load typeB slot0 slot1 beluga23)
		(next_load typeB slot1 slot2 beluga23)
		(next_load dummy-type slot2 dummy-slot beluga23)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga24)
		(next_load typeC slot0 slot1 beluga24)
		(next_load dummy-type slot1 dummy-slot beluga24)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA
		(to_load typeA slot0 beluga25)
		(next_load typeA slot0 slot1 beluga25)
		(next_load typeA slot1 slot2 beluga25)
		(next_load typeA slot2 slot3 beluga25)
		(next_load typeA slot3 slot4 beluga25)
		(next_load typeA slot4 slot5 beluga25)
		(next_load dummy-type slot5 dummy-slot beluga25)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga26)
		(next_load typeA slot0 slot1 beluga26)
		(next_load typeA slot1 slot2 beluga26)
		(next_load typeA slot2 slot3 beluga26)
		(next_load dummy-type slot3 dummy-slot beluga26)
		; 0: typeD
		(to_load typeD slot0 beluga27)
		(next_load dummy-type slot0 dummy-slot beluga27)
		; 0: typeC 1: typeC 2: typeC 3: typeC
		(to_load typeC slot0 beluga28)
		(next_load typeC slot0 slot1 beluga28)
		(next_load typeC slot1 slot2 beluga28)
		(next_load typeC slot2 slot3 beluga28)
		(next_load dummy-type slot3 dummy-slot beluga28)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga29)
		(next_load typeB slot0 slot1 beluga29)
		(next_load typeB slot1 slot2 beluga29)
		(next_load typeB slot2 slot3 beluga29)
		(next_load dummy-type slot3 dummy-slot beluga29)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga30)
		(next_load typeA slot0 slot1 beluga30)
		(next_load typeA slot1 slot2 beluga30)
		(next_load typeA slot2 slot3 beluga30)
		(next_load typeA slot3 slot4 beluga30)
		(next_load dummy-type slot4 dummy-slot beluga30)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga31)
		(next_load typeA slot0 slot1 beluga31)
		(next_load dummy-type slot1 dummy-slot beluga31)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga32)
		(next_load typeA slot0 slot1 beluga32)
		(next_load dummy-type slot1 dummy-slot beluga32)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga33)
		(next_load typeA slot0 slot1 beluga33)
		(next_load dummy-type slot1 dummy-slot beluga33)
		; 0: typeB
		(to_load typeB slot0 beluga34)
		(next_load dummy-type slot0 dummy-slot beluga34)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga35)
		(next_load typeC slot0 slot1 beluga35)
		(next_load dummy-type slot1 dummy-slot beluga35)
		; 0: typeC
		(to_load typeC slot0 beluga36)
		(next_load dummy-type slot0 dummy-slot beluga36)
		; 0: typeB
		(to_load typeB slot0 beluga37)
		(next_load dummy-type slot0 dummy-slot beluga37)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga38)
		(next_load typeC slot0 slot1 beluga38)
		(next_load dummy-type slot1 dummy-slot beluga38)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga39)
		(next_load typeD slot0 slot1 beluga39)
		(next_load dummy-type slot1 dummy-slot beluga39)
		; 0: typeC
		(to_load typeC slot0 beluga40)
		(next_load dummy-type slot0 dummy-slot beluga40)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga41)
		(next_load typeB slot0 slot1 beluga41)
		(next_load dummy-type slot1 dummy-slot beluga41)
		; 0: typeC
		(to_load typeC slot0 beluga42)
		(next_load dummy-type slot0 dummy-slot beluga42)
		; 0: typeD
		(to_load typeD slot0 beluga43)
		(next_load dummy-type slot0 dummy-slot beluga43)
		; 0: typeC
		(to_load typeC slot0 beluga44)
		(next_load dummy-type slot0 dummy-slot beluga44)
		; 0: typeC
		(to_load typeC slot0 beluga45)
		(next_load dummy-type slot0 dummy-slot beluga45)
		; 0: typeB
		(to_load typeB slot0 beluga46)
		(next_load dummy-type slot0 dummy-slot beluga46)
		; 0: typeD
		(to_load typeD slot0 beluga47)
		(next_load dummy-type slot0 dummy-slot beluga47)
		; 0: typeE
		(to_load typeE slot0 beluga48)
		(next_load dummy-type slot0 dummy-slot beluga48)
		; 0: typeE
		(to_load typeE slot0 beluga49)
		(next_load dummy-type slot0 dummy-slot beluga49)
		; 0: typeC
		(to_load typeC slot0 beluga50)
		(next_load dummy-type slot0 dummy-slot beluga50)
		; 0: typeE
		(to_load typeE slot0 beluga51)
		(next_load dummy-type slot0 dummy-slot beluga51)
		; 0: typeC
		(to_load typeC slot0 beluga52)
		(next_load dummy-type slot0 dummy-slot beluga52)
		; 0: typeD
		(to_load typeD slot0 beluga53)
		(next_load dummy-type slot0 dummy-slot beluga53)
		; 0: typeC
		(to_load typeC slot0 beluga54)
		(next_load dummy-type slot0 dummy-slot beluga54)
		; 0: typeC
		(to_load typeC slot0 beluga55)
		(next_load dummy-type slot0 dummy-slot beluga55)
		; 0: typeC
		(to_load typeC slot0 beluga56)
		(next_load dummy-type slot0 dummy-slot beluga56)
		; 0: typeC
		(to_load typeC slot0 beluga57)
		(next_load dummy-type slot0 dummy-slot beluga57)
		; 0: typeD
		(to_load typeD slot0 beluga58)
		(next_load dummy-type slot0 dummy-slot beluga58)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga59)
		(next_load typeC slot0 slot1 beluga59)
		(next_load dummy-type slot1 dummy-slot beluga59)
		; 0: typeE
		(to_load typeE slot0 beluga60)
		(next_load dummy-type slot0 dummy-slot beluga60)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA 7: typeA 8: typeA 9: typeA
		(to_load typeA slot0 beluga61)
		(next_load typeA slot0 slot1 beluga61)
		(next_load typeA slot1 slot2 beluga61)
		(next_load typeA slot2 slot3 beluga61)
		(next_load typeA slot3 slot4 beluga61)
		(next_load typeA slot4 slot5 beluga61)
		(next_load typeA slot5 slot6 beluga61)
		(next_load typeA slot6 slot7 beluga61)
		(next_load typeA slot7 slot8 beluga61)
		(next_load typeA slot8 slot9 beluga61)
		(next_load dummy-type slot9 dummy-slot beluga61)
		; 0: typeC
		(to_load typeC slot0 beluga62)
		(next_load dummy-type slot0 dummy-slot beluga62)
		; 0: typeE
		(to_load typeE slot0 beluga63)
		(next_load dummy-type slot0 dummy-slot beluga63)
		; 0: typeB
		(to_load typeB slot0 beluga64)
		(next_load dummy-type slot0 dummy-slot beluga64)
		; 0: typeB
		(to_load typeB slot0 beluga65)
		(next_load dummy-type slot0 dummy-slot beluga65)
		; 0: typeC
		(to_load typeC slot0 beluga66)
		(next_load dummy-type slot0 dummy-slot beluga66)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA 7: typeA 8: typeA 9: typeA
		(to_load typeA slot0 beluga67)
		(next_load typeA slot0 slot1 beluga67)
		(next_load typeA slot1 slot2 beluga67)
		(next_load typeA slot2 slot3 beluga67)
		(next_load typeA slot3 slot4 beluga67)
		(next_load typeA slot4 slot5 beluga67)
		(next_load typeA slot5 slot6 beluga67)
		(next_load typeA slot6 slot7 beluga67)
		(next_load typeA slot7 slot8 beluga67)
		(next_load typeA slot8 slot9 beluga67)
		(next_load dummy-type slot9 dummy-slot beluga67)
		; 0: typeB
		(to_load typeB slot0 beluga68)
		(next_load dummy-type slot0 dummy-slot beluga68)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA 7: typeA 8: typeA
		(to_load typeA slot0 beluga69)
		(next_load typeA slot0 slot1 beluga69)
		(next_load typeA slot1 slot2 beluga69)
		(next_load typeA slot2 slot3 beluga69)
		(next_load typeA slot3 slot4 beluga69)
		(next_load typeA slot4 slot5 beluga69)
		(next_load typeA slot5 slot6 beluga69)
		(next_load typeA slot6 slot7 beluga69)
		(next_load typeA slot7 slot8 beluga69)
		(next_load dummy-type slot8 dummy-slot beluga69)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga70)
		(next_load typeC slot0 slot1 beluga70)
		(next_load dummy-type slot1 dummy-slot beluga70)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga71)
		(next_load typeA slot0 slot1 beluga71)
		(next_load dummy-type slot1 dummy-slot beluga71)
		; 0: typeC
		(to_load typeC slot0 beluga72)
		(next_load dummy-type slot0 dummy-slot beluga72)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga73)
		(next_load typeB slot0 slot1 beluga73)
		(next_load dummy-type slot1 dummy-slot beluga73)
		; 0: typeD
		(to_load typeD slot0 beluga74)
		(next_load dummy-type slot0 dummy-slot beluga74)
		; 0: typeB
		(to_load typeB slot0 beluga75)
		(next_load dummy-type slot0 dummy-slot beluga75)
		; 0: typeC
		(to_load typeC slot0 beluga76)
		(next_load dummy-type slot0 dummy-slot beluga76)
		; 0: typeA
		(to_load typeA slot0 beluga77)
		(next_load dummy-type slot0 dummy-slot beluga77)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga78)
		(next_load typeD slot0 slot1 beluga78)
		(next_load dummy-type slot1 dummy-slot beluga78)
		; 0: typeE
		(to_load typeE slot0 beluga79)
		(next_load dummy-type slot0 dummy-slot beluga79)
		; 0: typeC
		(to_load typeC slot0 beluga80)
		(next_load dummy-type slot0 dummy-slot beluga80)
		; 0: typeD
		(to_load typeD slot0 beluga81)
		(next_load dummy-type slot0 dummy-slot beluga81)
		; 0: typeB
		(to_load typeB slot0 beluga82)
		(next_load dummy-type slot0 dummy-slot beluga82)
		; 0: typeD
		(to_load typeD slot0 beluga83)
		(next_load dummy-type slot0 dummy-slot beluga83)
		; 0: typeB
		(to_load typeB slot0 beluga84)
		(next_load dummy-type slot0 dummy-slot beluga84)
		; 0: typeB
		(to_load typeB slot0 beluga85)
		(next_load dummy-type slot0 dummy-slot beluga85)
		; 0: typeE
		(to_load typeE slot0 beluga86)
		(next_load dummy-type slot0 dummy-slot beluga86)
		; 0: typeC
		(to_load typeC slot0 beluga87)
		(next_load dummy-type slot0 dummy-slot beluga87)
		; 0: typeD
		(to_load typeD slot0 beluga88)
		(next_load dummy-type slot0 dummy-slot beluga88)
		; 0: typeB
		(to_load typeB slot0 beluga89)
		(next_load dummy-type slot0 dummy-slot beluga89)
		; 0: typeC
		(to_load typeC slot0 beluga90)
		(next_load dummy-type slot0 dummy-slot beluga90)
		; 0: typeC
		(to_load typeC slot0 beluga91)
		(next_load dummy-type slot0 dummy-slot beluga91)
		; 0: typeD
		(to_load typeD slot0 beluga92)
		(next_load dummy-type slot0 dummy-slot beluga92)
		; 0: typeC
		(to_load typeC slot0 beluga93)
		(next_load dummy-type slot0 dummy-slot beluga93)
		; 0: typeE
		(to_load typeE slot0 beluga94)
		(next_load dummy-type slot0 dummy-slot beluga94)
		; 0: typeE
		(to_load typeE slot0 beluga95)
		(next_load dummy-type slot0 dummy-slot beluga95)
		; 0: typeE
		(to_load typeE slot0 beluga96)
		(next_load dummy-type slot0 dummy-slot beluga96)
		; 0: typeE
		(to_load typeE slot0 beluga97)
		(next_load dummy-type slot0 dummy-slot beluga97)
		; 0: typeE
		(to_load typeE slot0 beluga98)
		(next_load dummy-type slot0 dummy-slot beluga98)
		; 0: typeB
		(to_load typeB slot0 beluga99)
		(next_load dummy-type slot0 dummy-slot beluga99)
		; 0: typeC
		(to_load typeC slot0 beluga100)
		(next_load dummy-type slot0 dummy-slot beluga100)
		; 0: typeA
		(to_load typeA slot0 beluga101)
		(next_load dummy-type slot0 dummy-slot beluga101)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga102)
		(next_load typeC slot0 slot1 beluga102)
		(next_load dummy-type slot1 dummy-slot beluga102)
		; 0: typeB
		(to_load typeB slot0 beluga103)
		(next_load dummy-type slot0 dummy-slot beluga103)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga104)
		(next_load typeA slot0 slot1 beluga104)
		(next_load typeA slot1 slot2 beluga104)
		(next_load typeA slot2 slot3 beluga104)
		(next_load dummy-type slot3 dummy-slot beluga104)
		; 0: typeC
		(to_load typeC slot0 beluga105)
		(next_load dummy-type slot0 dummy-slot beluga105)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga106)
		(next_load typeB slot0 slot1 beluga106)
		(next_load dummy-type slot1 dummy-slot beluga106)
		; 0: typeC
		(to_load typeC slot0 beluga107)
		(next_load dummy-type slot0 dummy-slot beluga107)
		; 0: typeC
		(to_load typeC slot0 beluga108)
		(next_load dummy-type slot0 dummy-slot beluga108)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga109)
		(next_load typeA slot0 slot1 beluga109)
		(next_load typeA slot1 slot2 beluga109)
		(next_load dummy-type slot2 dummy-slot beluga109)
		; 0: typeE
		(to_load typeE slot0 beluga110)
		(next_load dummy-type slot0 dummy-slot beluga110)
		; 0: typeB
		(to_load typeB slot0 beluga111)
		(next_load dummy-type slot0 dummy-slot beluga111)
		; 0: typeB
		(to_load typeB slot0 beluga112)
		(next_load dummy-type slot0 dummy-slot beluga112)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga113)
		(next_load typeA slot0 slot1 beluga113)
		(next_load typeA slot1 slot2 beluga113)
		(next_load typeA slot2 slot3 beluga113)
		(next_load typeA slot3 slot4 beluga113)
		(next_load dummy-type slot4 dummy-slot beluga113)
		; 0: typeB
		(to_load typeB slot0 beluga114)
		(next_load dummy-type slot0 dummy-slot beluga114)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga115)
		(next_load typeB slot0 slot1 beluga115)
		(next_load typeB slot1 slot2 beluga115)
		(next_load dummy-type slot2 dummy-slot beluga115)
		; 0: typeC
		(to_load typeC slot0 beluga116)
		(next_load dummy-type slot0 dummy-slot beluga116)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga117)
		(next_load typeA slot0 slot1 beluga117)
		(next_load typeA slot1 slot2 beluga117)
		(next_load typeA slot2 slot3 beluga117)
		(next_load dummy-type slot3 dummy-slot beluga117)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga118)
		(next_load typeA slot0 slot1 beluga118)
		(next_load dummy-type slot1 dummy-slot beluga118)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga119)
		(next_load typeB slot0 slot1 beluga119)
		(next_load dummy-type slot1 dummy-slot beluga119)
		; 0: typeE
		(to_load typeE slot0 beluga120)
		(next_load dummy-type slot0 dummy-slot beluga120)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga121)
		(next_load typeA slot0 slot1 beluga121)
		(next_load typeA slot1 slot2 beluga121)
		(next_load dummy-type slot2 dummy-slot beluga121)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga122)
		(next_load typeB slot0 slot1 beluga122)
		(next_load dummy-type slot1 dummy-slot beluga122)
		; 0: typeA
		(to_load typeA slot0 beluga123)
		(next_load dummy-type slot0 dummy-slot beluga123)
		; 0: typeB
		(to_load typeB slot0 beluga124)
		(next_load dummy-type slot0 dummy-slot beluga124)
		; 0: typeC
		(to_load typeC slot0 beluga125)
		(next_load dummy-type slot0 dummy-slot beluga125)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga126)
		(next_load typeA slot0 slot1 beluga126)
		(next_load dummy-type slot1 dummy-slot beluga126)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga127)
		(next_load typeB slot0 slot1 beluga127)
		(next_load dummy-type slot1 dummy-slot beluga127)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga128)
		(next_load typeC slot0 slot1 beluga128)
		(next_load dummy-type slot1 dummy-slot beluga128)
		; 0: typeC
		(to_load typeC slot0 beluga129)
		(next_load dummy-type slot0 dummy-slot beluga129)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga130)
		(next_load typeA slot0 slot1 beluga130)
		(next_load typeA slot1 slot2 beluga130)
		(next_load typeA slot2 slot3 beluga130)
		(next_load dummy-type slot3 dummy-slot beluga130)
		; 0: typeB
		(to_load typeB slot0 beluga131)
		(next_load dummy-type slot0 dummy-slot beluga131)
		; 0: typeE
		(to_load typeE slot0 beluga132)
		(next_load dummy-type slot0 dummy-slot beluga132)
		; 0: typeE
		(to_load typeE slot0 beluga133)
		(next_load dummy-type slot0 dummy-slot beluga133)
		; 0: typeA
		(to_load typeA slot0 beluga134)
		(next_load dummy-type slot0 dummy-slot beluga134)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga135)
		(next_load typeD slot0 slot1 beluga135)
		(next_load dummy-type slot1 dummy-slot beluga135)
		; 0: typeB
		(to_load typeB slot0 beluga136)
		(next_load dummy-type slot0 dummy-slot beluga136)
		; 0: typeB
		(to_load typeB slot0 beluga137)
		(next_load dummy-type slot0 dummy-slot beluga137)
		; 0: typeC
		(to_load typeC slot0 beluga138)
		(next_load dummy-type slot0 dummy-slot beluga138)
		; 0: typeB
		(to_load typeB slot0 beluga139)
		(next_load dummy-type slot0 dummy-slot beluga139)
		; 0: typeB
		(to_load typeB slot0 beluga140)
		(next_load dummy-type slot0 dummy-slot beluga140)
		; 0: typeE
		(to_load typeE slot0 beluga141)
		(next_load dummy-type slot0 dummy-slot beluga141)
		; 0: typeC
		(to_load typeC slot0 beluga142)
		(next_load dummy-type slot0 dummy-slot beluga142)
		; 0: typeE
		(to_load typeE slot0 beluga143)
		(next_load dummy-type slot0 dummy-slot beluga143)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga144)
		(next_load typeD slot0 slot1 beluga144)
		(next_load dummy-type slot1 dummy-slot beluga144)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga145)
		(next_load typeD slot0 slot1 beluga145)
		(next_load dummy-type slot1 dummy-slot beluga145)
		; 0: typeA
		(to_load typeA slot0 beluga146)
		(next_load dummy-type slot0 dummy-slot beluga146)
		; 0: typeC
		(to_load typeC slot0 beluga147)
		(next_load dummy-type slot0 dummy-slot beluga147)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga148)
		(next_load typeA slot0 slot1 beluga148)
		(next_load dummy-type slot1 dummy-slot beluga148)
		; 0: typeE
		(to_load typeE slot0 beluga149)
		(next_load dummy-type slot0 dummy-slot beluga149)
		; 0: typeE
		(to_load typeE slot0 beluga150)
		(next_load dummy-type slot0 dummy-slot beluga150)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga151)
		(next_load typeD slot0 slot1 beluga151)
		(next_load dummy-type slot1 dummy-slot beluga151)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga152)
		(next_load typeD slot0 slot1 beluga152)
		(next_load dummy-type slot1 dummy-slot beluga152)
		; 0: typeD
		(to_load typeD slot0 beluga153)
		(next_load dummy-type slot0 dummy-slot beluga153)
		; 0: typeC
		(to_load typeC slot0 beluga154)
		(next_load dummy-type slot0 dummy-slot beluga154)
		; 0: typeA
		(to_load typeA slot0 beluga155)
		(next_load dummy-type slot0 dummy-slot beluga155)
		; 0: typeB
		(to_load typeB slot0 beluga156)
		(next_load dummy-type slot0 dummy-slot beluga156)
		; 0: typeC
		(to_load typeC slot0 beluga157)
		(next_load dummy-type slot0 dummy-slot beluga157)
		; 0: typeD
		(to_load typeD slot0 beluga158)
		(next_load dummy-type slot0 dummy-slot beluga158)
		; 0: typeC
		(to_load typeC slot0 beluga159)
		(next_load dummy-type slot0 dummy-slot beluga159)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga160)
		(next_load typeB slot0 slot1 beluga160)
		(next_load dummy-type slot1 dummy-slot beluga160)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA
		(to_load typeA slot0 beluga161)
		(next_load typeA slot0 slot1 beluga161)
		(next_load typeA slot1 slot2 beluga161)
		(next_load typeA slot2 slot3 beluga161)
		(next_load typeA slot3 slot4 beluga161)
		(next_load typeA slot4 slot5 beluga161)
		(next_load typeA slot5 slot6 beluga161)
		(next_load dummy-type slot6 dummy-slot beluga161)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga162)
		(next_load typeA slot0 slot1 beluga162)
		(next_load dummy-type slot1 dummy-slot beluga162)
		; 0: typeA
		(to_load typeA slot0 beluga163)
		(next_load dummy-type slot0 dummy-slot beluga163)
		; 0: typeC
		(to_load typeC slot0 beluga164)
		(next_load dummy-type slot0 dummy-slot beluga164)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga165)
		(next_load typeA slot0 slot1 beluga165)
		(next_load typeA slot1 slot2 beluga165)
		(next_load typeA slot2 slot3 beluga165)
		(next_load dummy-type slot3 dummy-slot beluga165)
		; 0: typeA
		(to_load typeA slot0 beluga166)
		(next_load dummy-type slot0 dummy-slot beluga166)
		; 0: typeA
		(to_load typeA slot0 beluga167)
		(next_load dummy-type slot0 dummy-slot beluga167)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga168)
		(next_load typeC slot0 slot1 beluga168)
		(next_load typeC slot1 slot2 beluga168)
		(next_load dummy-type slot2 dummy-slot beluga168)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga169)
		(next_load typeB slot0 slot1 beluga169)
		(next_load typeB slot1 slot2 beluga169)
		(next_load typeB slot2 slot3 beluga169)
		(next_load dummy-type slot3 dummy-slot beluga169)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga170)
		(next_load typeA slot0 slot1 beluga170)
		(next_load typeA slot1 slot2 beluga170)
		(next_load dummy-type slot2 dummy-slot beluga170)
		; 0: typeC
		(to_load typeC slot0 beluga171)
		(next_load dummy-type slot0 dummy-slot beluga171)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga172)
		(next_load typeD slot0 slot1 beluga172)
		(next_load dummy-type slot1 dummy-slot beluga172)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga173)
		(next_load typeA slot0 slot1 beluga173)
		(next_load dummy-type slot1 dummy-slot beluga173)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga174)
		(next_load typeC slot0 slot1 beluga174)
		(next_load dummy-type slot1 dummy-slot beluga174)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga175)
		(next_load typeB slot0 slot1 beluga175)
		(next_load typeB slot1 slot2 beluga175)
		(next_load dummy-type slot2 dummy-slot beluga175)
		; 0: typeB
		(to_load typeB slot0 beluga176)
		(next_load dummy-type slot0 dummy-slot beluga176)
		; 0: typeB
		(to_load typeB slot0 beluga177)
		(next_load dummy-type slot0 dummy-slot beluga177)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga178)
		(next_load typeC slot0 slot1 beluga178)
		(next_load typeC slot1 slot2 beluga178)
		(next_load dummy-type slot2 dummy-slot beluga178)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA
		(to_load typeA slot0 beluga179)
		(next_load typeA slot0 slot1 beluga179)
		(next_load typeA slot1 slot2 beluga179)
		(next_load typeA slot2 slot3 beluga179)
		(next_load typeA slot3 slot4 beluga179)
		(next_load typeA slot4 slot5 beluga179)
		(next_load dummy-type slot5 dummy-slot beluga179)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga180)
		(next_load typeA slot0 slot1 beluga180)
		(next_load typeA slot1 slot2 beluga180)
		(next_load dummy-type slot2 dummy-slot beluga180)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga181)
		(next_load typeA slot0 slot1 beluga181)
		(next_load dummy-type slot1 dummy-slot beluga181)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga182)
		(next_load typeC slot0 slot1 beluga182)
		(next_load dummy-type slot1 dummy-slot beluga182)
		; 0: typeD
		(to_load typeD slot0 beluga183)
		(next_load dummy-type slot0 dummy-slot beluga183)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga184)
		(next_load typeA slot0 slot1 beluga184)
		(next_load typeA slot1 slot2 beluga184)
		(next_load typeA slot2 slot3 beluga184)
		(next_load dummy-type slot3 dummy-slot beluga184)
		; 0: typeE
		(to_load typeE slot0 beluga185)
		(next_load dummy-type slot0 dummy-slot beluga185)
		; 0: typeE
		(to_load typeE slot0 beluga186)
		(next_load dummy-type slot0 dummy-slot beluga186)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga187)
		(next_load typeA slot0 slot1 beluga187)
		(next_load dummy-type slot1 dummy-slot beluga187)
		; 0: typeA
		(to_load typeA slot0 beluga188)
		(next_load dummy-type slot0 dummy-slot beluga188)
		; 0: typeC
		(to_load typeC slot0 beluga189)
		(next_load dummy-type slot0 dummy-slot beluga189)
		; 0: typeA
		(to_load typeA slot0 beluga190)
		(next_load dummy-type slot0 dummy-slot beluga190)
		; 0: typeC 1: typeC 2: typeC 3: typeC
		(to_load typeC slot0 beluga191)
		(next_load typeC slot0 slot1 beluga191)
		(next_load typeC slot1 slot2 beluga191)
		(next_load typeC slot2 slot3 beluga191)
		(next_load dummy-type slot3 dummy-slot beluga191)
		; 0: typeB
		(to_load typeB slot0 beluga192)
		(next_load dummy-type slot0 dummy-slot beluga192)
		; Production schedule:
		; Production line: pl0
		; 0: jig0001 1: jig0007 2: jig0003 3: jig0008 4: jig0015 5: jig0026 6: jig0011 7: jig0043 8: jig0038 9: jig0025 10: jig0041 11: jig0028 12: jig0056 13: jig0017 14: jig0022 15: jig0040 16: jig0032 17: jig0039 18: jig0030 19: jig0058 20: jig0068 21: jig0073 22: jig0048 23: jig0080 24: jig0046 25: jig0052 26: jig0053 27: jig0084 28: jig0054 29: jig0078 30: jig0065 31: jig0050 32: jig0044 33: jig0092 34: jig0060 35: jig0085 36: jig0096 37: jig0035 38: jig0072 39: jig0079 40: jig0106 41: jig0094 42: jig0081 43: jig0075 44: jig0082 45: jig0097 46: jig0089 47: jig0103 48: jig0070 49: jig0083 50: jig0102 51: jig0110 52: jig0125 53: jig0109 54: jig0122 55: jig0112 56: jig0129 57: jig0114 58: jig0135 59: jig0131 60: jig0121 61: jig0111 62: jig0136 63: jig0142 64: jig0118 65: jig0132 66: jig0140 67: jig0120 68: jig0123 69: jig0146 70: jig0143 71: jig0153 72: jig0154 73: jig0150 74: jig0157 75: jig0165 76: jig0151 77: jig0169 78: jig0158 79: jig0152 80: jig0162 81: jig0160 82: jig0180 83: jig0170 84: jig0181 85: jig0192 86: jig0172 87: jig0185 88: jig0179 89: jig0173 90: jig0194 91: jig0187 92: jig0199 93: jig0212 94: jig0189 95: jig0215 96: jig0177 97: jig0175 98: jig0195 99: jig0213 100: jig0221 101: jig0222 102: jig0214 103: jig0196 104: jig0207 105: jig0230 106: jig0209 107: jig0223 108: jig0210 109: jig0228 110: jig0235 111: jig0220 112: jig0231 113: jig0217 114: jig0233 115: jig0216 116: jig0243 117: jig0242 118: jig0239 119: jig0237 120: jig0252 121: jig0260 122: jig0262 123: jig0249 124: jig0261 125: jig0266 126: jig0256 127: jig0280 128: jig0245 129: jig0285 130: jig0269 131: jig0277 132: jig0263 133: jig0253 134: jig0278 135: jig0292 136: jig0271 137: jig0284 138: jig0302 139: jig0254 140: jig0304 141: jig0283 142: jig0282 143: jig0296 144: jig0293 145: jig0306 146: jig0268 147: jig0301 148: jig0275 149: jig0267 150: jig0308 151: jig0323 152: jig0297 153: jig0332 154: jig0290 155: jig0298 156: jig0334 157: jig0340 158: jig0342 159: jig0333 160: jig0325 161: jig0343 162: jig0317 163: jig0312 164: jig0320 165: jig0328 166: jig0309 167: jig0331
		(to_deliver jig0001 pl0)
		(next_deliver jig0001 jig0007)
		(next_deliver jig0007 jig0003)
		(next_deliver jig0003 jig0008)
		(next_deliver jig0008 jig0015)
		(next_deliver jig0015 jig0026)
		(next_deliver jig0026 jig0011)
		(next_deliver jig0011 jig0043)
		(next_deliver jig0043 jig0038)
		(next_deliver jig0038 jig0025)
		(next_deliver jig0025 jig0041)
		(next_deliver jig0041 jig0028)
		(next_deliver jig0028 jig0056)
		(next_deliver jig0056 jig0017)
		(next_deliver jig0017 jig0022)
		(next_deliver jig0022 jig0040)
		(next_deliver jig0040 jig0032)
		(next_deliver jig0032 jig0039)
		(next_deliver jig0039 jig0030)
		(next_deliver jig0030 jig0058)
		(next_deliver jig0058 jig0068)
		(next_deliver jig0068 jig0073)
		(next_deliver jig0073 jig0048)
		(next_deliver jig0048 jig0080)
		(next_deliver jig0080 jig0046)
		(next_deliver jig0046 jig0052)
		(next_deliver jig0052 jig0053)
		(next_deliver jig0053 jig0084)
		(next_deliver jig0084 jig0054)
		(next_deliver jig0054 jig0078)
		(next_deliver jig0078 jig0065)
		(next_deliver jig0065 jig0050)
		(next_deliver jig0050 jig0044)
		(next_deliver jig0044 jig0092)
		(next_deliver jig0092 jig0060)
		(next_deliver jig0060 jig0085)
		(next_deliver jig0085 jig0096)
		(next_deliver jig0096 jig0035)
		(next_deliver jig0035 jig0072)
		(next_deliver jig0072 jig0079)
		(next_deliver jig0079 jig0106)
		(next_deliver jig0106 jig0094)
		(next_deliver jig0094 jig0081)
		(next_deliver jig0081 jig0075)
		(next_deliver jig0075 jig0082)
		(next_deliver jig0082 jig0097)
		(next_deliver jig0097 jig0089)
		(next_deliver jig0089 jig0103)
		(next_deliver jig0103 jig0070)
		(next_deliver jig0070 jig0083)
		(next_deliver jig0083 jig0102)
		(next_deliver jig0102 jig0110)
		(next_deliver jig0110 jig0125)
		(next_deliver jig0125 jig0109)
		(next_deliver jig0109 jig0122)
		(next_deliver jig0122 jig0112)
		(next_deliver jig0112 jig0129)
		(next_deliver jig0129 jig0114)
		(next_deliver jig0114 jig0135)
		(next_deliver jig0135 jig0131)
		(next_deliver jig0131 jig0121)
		(next_deliver jig0121 jig0111)
		(next_deliver jig0111 jig0136)
		(next_deliver jig0136 jig0142)
		(next_deliver jig0142 jig0118)
		(next_deliver jig0118 jig0132)
		(next_deliver jig0132 jig0140)
		(next_deliver jig0140 jig0120)
		(next_deliver jig0120 jig0123)
		(next_deliver jig0123 jig0146)
		(next_deliver jig0146 jig0143)
		(next_deliver jig0143 jig0153)
		(next_deliver jig0153 jig0154)
		(next_deliver jig0154 jig0150)
		(next_deliver jig0150 jig0157)
		(next_deliver jig0157 jig0165)
		(next_deliver jig0165 jig0151)
		(next_deliver jig0151 jig0169)
		(next_deliver jig0169 jig0158)
		(next_deliver jig0158 jig0152)
		(next_deliver jig0152 jig0162)
		(next_deliver jig0162 jig0160)
		(next_deliver jig0160 jig0180)
		(next_deliver jig0180 jig0170)
		(next_deliver jig0170 jig0181)
		(next_deliver jig0181 jig0192)
		(next_deliver jig0192 jig0172)
		(next_deliver jig0172 jig0185)
		(next_deliver jig0185 jig0179)
		(next_deliver jig0179 jig0173)
		(next_deliver jig0173 jig0194)
		(next_deliver jig0194 jig0187)
		(next_deliver jig0187 jig0199)
		(next_deliver jig0199 jig0212)
		(next_deliver jig0212 jig0189)
		(next_deliver jig0189 jig0215)
		(next_deliver jig0215 jig0177)
		(next_deliver jig0177 jig0175)
		(next_deliver jig0175 jig0195)
		(next_deliver jig0195 jig0213)
		(next_deliver jig0213 jig0221)
		(next_deliver jig0221 jig0222)
		(next_deliver jig0222 jig0214)
		(next_deliver jig0214 jig0196)
		(next_deliver jig0196 jig0207)
		(next_deliver jig0207 jig0230)
		(next_deliver jig0230 jig0209)
		(next_deliver jig0209 jig0223)
		(next_deliver jig0223 jig0210)
		(next_deliver jig0210 jig0228)
		(next_deliver jig0228 jig0235)
		(next_deliver jig0235 jig0220)
		(next_deliver jig0220 jig0231)
		(next_deliver jig0231 jig0217)
		(next_deliver jig0217 jig0233)
		(next_deliver jig0233 jig0216)
		(next_deliver jig0216 jig0243)
		(next_deliver jig0243 jig0242)
		(next_deliver jig0242 jig0239)
		(next_deliver jig0239 jig0237)
		(next_deliver jig0237 jig0252)
		(next_deliver jig0252 jig0260)
		(next_deliver jig0260 jig0262)
		(next_deliver jig0262 jig0249)
		(next_deliver jig0249 jig0261)
		(next_deliver jig0261 jig0266)
		(next_deliver jig0266 jig0256)
		(next_deliver jig0256 jig0280)
		(next_deliver jig0280 jig0245)
		(next_deliver jig0245 jig0285)
		(next_deliver jig0285 jig0269)
		(next_deliver jig0269 jig0277)
		(next_deliver jig0277 jig0263)
		(next_deliver jig0263 jig0253)
		(next_deliver jig0253 jig0278)
		(next_deliver jig0278 jig0292)
		(next_deliver jig0292 jig0271)
		(next_deliver jig0271 jig0284)
		(next_deliver jig0284 jig0302)
		(next_deliver jig0302 jig0254)
		(next_deliver jig0254 jig0304)
		(next_deliver jig0304 jig0283)
		(next_deliver jig0283 jig0282)
		(next_deliver jig0282 jig0296)
		(next_deliver jig0296 jig0293)
		(next_deliver jig0293 jig0306)
		(next_deliver jig0306 jig0268)
		(next_deliver jig0268 jig0301)
		(next_deliver jig0301 jig0275)
		(next_deliver jig0275 jig0267)
		(next_deliver jig0267 jig0308)
		(next_deliver jig0308 jig0323)
		(next_deliver jig0323 jig0297)
		(next_deliver jig0297 jig0332)
		(next_deliver jig0332 jig0290)
		(next_deliver jig0290 jig0298)
		(next_deliver jig0298 jig0334)
		(next_deliver jig0334 jig0340)
		(next_deliver jig0340 jig0342)
		(next_deliver jig0342 jig0333)
		(next_deliver jig0333 jig0325)
		(next_deliver jig0325 jig0343)
		(next_deliver jig0343 jig0317)
		(next_deliver jig0317 jig0312)
		(next_deliver jig0312 jig0320)
		(next_deliver jig0320 jig0328)
		(next_deliver jig0328 jig0309)
		(next_deliver jig0309 jig0331)
		(next_deliver jig0331 dummy-jig)
		; Production line: pl1
		; 0: jig0002 1: jig0012 2: jig0010 3: jig0013 4: jig0016 5: jig0023 6: jig0018 7: jig0034 8: jig0045 9: jig0027 10: jig0062 11: jig0064 12: jig0059 13: jig0019 14: jig0029 15: jig0067 16: jig0033 17: jig0024 18: jig0055 19: jig0063 20: jig0069 21: jig0036 22: jig0061 23: jig0020 24: jig0047 25: jig0014 26: jig0066 27: jig0021 28: jig0049 29: jig0057 30: jig0042 31: jig0031 32: jig0090 33: jig0037 34: jig0074 35: jig0093 36: jig0104 37: jig0071 38: jig0076 39: jig0086 40: jig0107 41: jig0051 42: jig0091 43: jig0077 44: jig0088 45: jig0087 46: jig0099 47: jig0095 48: jig0101 49: jig0098 50: jig0105 51: jig0100 52: jig0108 53: jig0113 54: jig0127 55: jig0117 56: jig0130 57: jig0115 58: jig0128 59: jig0119 60: jig0126 61: jig0137 62: jig0116 63: jig0148 64: jig0124 65: jig0133 66: jig0145 67: jig0139 68: jig0147 69: jig0138 70: jig0144 71: jig0134 72: jig0141 73: jig0159 74: jig0156 75: jig0149 76: jig0161 77: jig0168 78: jig0167 79: jig0155 80: jig0191 81: jig0164 82: jig0163 83: jig0178 84: jig0188 85: jig0166 86: jig0182 87: jig0174 88: jig0190 89: jig0171 90: jig0183 91: jig0211 92: jig0208 93: jig0186 94: jig0206 95: jig0176 96: jig0204 97: jig0184 98: jig0197 99: jig0201 100: jig0205 101: jig0226 102: jig0227 103: jig0198 104: jig0218 105: jig0200 106: jig0193 107: jig0203 108: jig0225 109: jig0232 110: jig0219 111: jig0229 112: jig0202 113: jig0224 114: jig0240 115: jig0234 116: jig0238 117: jig0236 118: jig0244 119: jig0247 120: jig0251 121: jig0257 122: jig0246 123: jig0265 124: jig0259 125: jig0241 126: jig0264 127: jig0274 128: jig0248 129: jig0255 130: jig0273 131: jig0287 132: jig0250 133: jig0272 134: jig0300 135: jig0295 136: jig0276 137: jig0288 138: jig0258 139: jig0294 140: jig0305 141: jig0303 142: jig0289 143: jig0281 144: jig0299 145: jig0310 146: jig0270 147: jig0307 148: jig0311 149: jig0291 150: jig0321 151: jig0286 152: jig0314 153: jig0279 154: jig0324 155: jig0319 156: jig0329 157: jig0318 158: jig0330 159: jig0316 160: jig0336 161: jig0338 162: jig0344 163: jig0313 164: jig0326 165: jig0341 166: jig0315 167: jig0335
		(to_deliver jig0002 pl1)
		(next_deliver jig0002 jig0012)
		(next_deliver jig0012 jig0010)
		(next_deliver jig0010 jig0013)
		(next_deliver jig0013 jig0016)
		(next_deliver jig0016 jig0023)
		(next_deliver jig0023 jig0018)
		(next_deliver jig0018 jig0034)
		(next_deliver jig0034 jig0045)
		(next_deliver jig0045 jig0027)
		(next_deliver jig0027 jig0062)
		(next_deliver jig0062 jig0064)
		(next_deliver jig0064 jig0059)
		(next_deliver jig0059 jig0019)
		(next_deliver jig0019 jig0029)
		(next_deliver jig0029 jig0067)
		(next_deliver jig0067 jig0033)
		(next_deliver jig0033 jig0024)
		(next_deliver jig0024 jig0055)
		(next_deliver jig0055 jig0063)
		(next_deliver jig0063 jig0069)
		(next_deliver jig0069 jig0036)
		(next_deliver jig0036 jig0061)
		(next_deliver jig0061 jig0020)
		(next_deliver jig0020 jig0047)
		(next_deliver jig0047 jig0014)
		(next_deliver jig0014 jig0066)
		(next_deliver jig0066 jig0021)
		(next_deliver jig0021 jig0049)
		(next_deliver jig0049 jig0057)
		(next_deliver jig0057 jig0042)
		(next_deliver jig0042 jig0031)
		(next_deliver jig0031 jig0090)
		(next_deliver jig0090 jig0037)
		(next_deliver jig0037 jig0074)
		(next_deliver jig0074 jig0093)
		(next_deliver jig0093 jig0104)
		(next_deliver jig0104 jig0071)
		(next_deliver jig0071 jig0076)
		(next_deliver jig0076 jig0086)
		(next_deliver jig0086 jig0107)
		(next_deliver jig0107 jig0051)
		(next_deliver jig0051 jig0091)
		(next_deliver jig0091 jig0077)
		(next_deliver jig0077 jig0088)
		(next_deliver jig0088 jig0087)
		(next_deliver jig0087 jig0099)
		(next_deliver jig0099 jig0095)
		(next_deliver jig0095 jig0101)
		(next_deliver jig0101 jig0098)
		(next_deliver jig0098 jig0105)
		(next_deliver jig0105 jig0100)
		(next_deliver jig0100 jig0108)
		(next_deliver jig0108 jig0113)
		(next_deliver jig0113 jig0127)
		(next_deliver jig0127 jig0117)
		(next_deliver jig0117 jig0130)
		(next_deliver jig0130 jig0115)
		(next_deliver jig0115 jig0128)
		(next_deliver jig0128 jig0119)
		(next_deliver jig0119 jig0126)
		(next_deliver jig0126 jig0137)
		(next_deliver jig0137 jig0116)
		(next_deliver jig0116 jig0148)
		(next_deliver jig0148 jig0124)
		(next_deliver jig0124 jig0133)
		(next_deliver jig0133 jig0145)
		(next_deliver jig0145 jig0139)
		(next_deliver jig0139 jig0147)
		(next_deliver jig0147 jig0138)
		(next_deliver jig0138 jig0144)
		(next_deliver jig0144 jig0134)
		(next_deliver jig0134 jig0141)
		(next_deliver jig0141 jig0159)
		(next_deliver jig0159 jig0156)
		(next_deliver jig0156 jig0149)
		(next_deliver jig0149 jig0161)
		(next_deliver jig0161 jig0168)
		(next_deliver jig0168 jig0167)
		(next_deliver jig0167 jig0155)
		(next_deliver jig0155 jig0191)
		(next_deliver jig0191 jig0164)
		(next_deliver jig0164 jig0163)
		(next_deliver jig0163 jig0178)
		(next_deliver jig0178 jig0188)
		(next_deliver jig0188 jig0166)
		(next_deliver jig0166 jig0182)
		(next_deliver jig0182 jig0174)
		(next_deliver jig0174 jig0190)
		(next_deliver jig0190 jig0171)
		(next_deliver jig0171 jig0183)
		(next_deliver jig0183 jig0211)
		(next_deliver jig0211 jig0208)
		(next_deliver jig0208 jig0186)
		(next_deliver jig0186 jig0206)
		(next_deliver jig0206 jig0176)
		(next_deliver jig0176 jig0204)
		(next_deliver jig0204 jig0184)
		(next_deliver jig0184 jig0197)
		(next_deliver jig0197 jig0201)
		(next_deliver jig0201 jig0205)
		(next_deliver jig0205 jig0226)
		(next_deliver jig0226 jig0227)
		(next_deliver jig0227 jig0198)
		(next_deliver jig0198 jig0218)
		(next_deliver jig0218 jig0200)
		(next_deliver jig0200 jig0193)
		(next_deliver jig0193 jig0203)
		(next_deliver jig0203 jig0225)
		(next_deliver jig0225 jig0232)
		(next_deliver jig0232 jig0219)
		(next_deliver jig0219 jig0229)
		(next_deliver jig0229 jig0202)
		(next_deliver jig0202 jig0224)
		(next_deliver jig0224 jig0240)
		(next_deliver jig0240 jig0234)
		(next_deliver jig0234 jig0238)
		(next_deliver jig0238 jig0236)
		(next_deliver jig0236 jig0244)
		(next_deliver jig0244 jig0247)
		(next_deliver jig0247 jig0251)
		(next_deliver jig0251 jig0257)
		(next_deliver jig0257 jig0246)
		(next_deliver jig0246 jig0265)
		(next_deliver jig0265 jig0259)
		(next_deliver jig0259 jig0241)
		(next_deliver jig0241 jig0264)
		(next_deliver jig0264 jig0274)
		(next_deliver jig0274 jig0248)
		(next_deliver jig0248 jig0255)
		(next_deliver jig0255 jig0273)
		(next_deliver jig0273 jig0287)
		(next_deliver jig0287 jig0250)
		(next_deliver jig0250 jig0272)
		(next_deliver jig0272 jig0300)
		(next_deliver jig0300 jig0295)
		(next_deliver jig0295 jig0276)
		(next_deliver jig0276 jig0288)
		(next_deliver jig0288 jig0258)
		(next_deliver jig0258 jig0294)
		(next_deliver jig0294 jig0305)
		(next_deliver jig0305 jig0303)
		(next_deliver jig0303 jig0289)
		(next_deliver jig0289 jig0281)
		(next_deliver jig0281 jig0299)
		(next_deliver jig0299 jig0310)
		(next_deliver jig0310 jig0270)
		(next_deliver jig0270 jig0307)
		(next_deliver jig0307 jig0311)
		(next_deliver jig0311 jig0291)
		(next_deliver jig0291 jig0321)
		(next_deliver jig0321 jig0286)
		(next_deliver jig0286 jig0314)
		(next_deliver jig0314 jig0279)
		(next_deliver jig0279 jig0324)
		(next_deliver jig0324 jig0319)
		(next_deliver jig0319 jig0329)
		(next_deliver jig0329 jig0318)
		(next_deliver jig0318 jig0330)
		(next_deliver jig0330 jig0316)
		(next_deliver jig0316 jig0336)
		(next_deliver jig0336 jig0338)
		(next_deliver jig0338 jig0344)
		(next_deliver jig0344 jig0313)
		(next_deliver jig0313 jig0326)
		(next_deliver jig0326 jig0341)
		(next_deliver jig0341 jig0315)
		(next_deliver jig0315 jig0335)
		(next_deliver jig0335 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0001)
		(empty jig0007)
		(empty jig0003)
		(empty jig0008)
		(empty jig0015)
		(empty jig0026)
		(empty jig0011)
		(empty jig0043)
		(empty jig0038)
		(empty jig0025)
		(empty jig0041)
		(empty jig0028)
		(empty jig0056)
		(empty jig0017)
		(empty jig0022)
		(empty jig0040)
		(empty jig0032)
		(empty jig0039)
		(empty jig0030)
		(empty jig0058)
		(empty jig0068)
		(empty jig0073)
		(empty jig0048)
		(empty jig0080)
		(empty jig0046)
		(empty jig0052)
		(empty jig0053)
		(empty jig0084)
		(empty jig0054)
		(empty jig0078)
		(empty jig0065)
		(empty jig0050)
		(empty jig0044)
		(empty jig0092)
		(empty jig0060)
		(empty jig0085)
		(empty jig0096)
		(empty jig0035)
		(empty jig0072)
		(empty jig0079)
		(empty jig0106)
		(empty jig0094)
		(empty jig0081)
		(empty jig0075)
		(empty jig0082)
		(empty jig0097)
		(empty jig0089)
		(empty jig0103)
		(empty jig0070)
		(empty jig0083)
		(empty jig0102)
		(empty jig0110)
		(empty jig0125)
		(empty jig0109)
		(empty jig0122)
		(empty jig0112)
		(empty jig0129)
		(empty jig0114)
		(empty jig0135)
		(empty jig0131)
		(empty jig0121)
		(empty jig0111)
		(empty jig0136)
		(empty jig0142)
		(empty jig0118)
		(empty jig0132)
		(empty jig0140)
		(empty jig0120)
		(empty jig0123)
		(empty jig0146)
		(empty jig0143)
		(empty jig0153)
		(empty jig0154)
		(empty jig0150)
		(empty jig0157)
		(empty jig0165)
		(empty jig0151)
		(empty jig0169)
		(empty jig0158)
		(empty jig0152)
		(empty jig0162)
		(empty jig0160)
		(empty jig0180)
		(empty jig0170)
		(empty jig0181)
		(empty jig0192)
		(empty jig0172)
		(empty jig0185)
		(empty jig0179)
		(empty jig0173)
		(empty jig0194)
		(empty jig0187)
		(empty jig0199)
		(empty jig0212)
		(empty jig0189)
		(empty jig0215)
		(empty jig0177)
		(empty jig0175)
		(empty jig0195)
		(empty jig0213)
		(empty jig0221)
		(empty jig0222)
		(empty jig0214)
		(empty jig0196)
		(empty jig0207)
		(empty jig0230)
		(empty jig0209)
		(empty jig0223)
		(empty jig0210)
		(empty jig0228)
		(empty jig0235)
		(empty jig0220)
		(empty jig0231)
		(empty jig0217)
		(empty jig0233)
		(empty jig0216)
		(empty jig0243)
		(empty jig0242)
		(empty jig0239)
		(empty jig0237)
		(empty jig0252)
		(empty jig0260)
		(empty jig0262)
		(empty jig0249)
		(empty jig0261)
		(empty jig0266)
		(empty jig0256)
		(empty jig0280)
		(empty jig0245)
		(empty jig0285)
		(empty jig0269)
		(empty jig0277)
		(empty jig0263)
		(empty jig0253)
		(empty jig0278)
		(empty jig0292)
		(empty jig0271)
		(empty jig0284)
		(empty jig0302)
		(empty jig0254)
		(empty jig0304)
		(empty jig0283)
		(empty jig0282)
		(empty jig0296)
		(empty jig0293)
		(empty jig0306)
		(empty jig0268)
		(empty jig0301)
		(empty jig0275)
		(empty jig0267)
		(empty jig0308)
		(empty jig0323)
		(empty jig0297)
		(empty jig0332)
		(empty jig0290)
		(empty jig0298)
		(empty jig0334)
		(empty jig0340)
		(empty jig0342)
		(empty jig0333)
		(empty jig0325)
		(empty jig0343)
		(empty jig0317)
		(empty jig0312)
		(empty jig0320)
		(empty jig0328)
		(empty jig0309)
		(empty jig0331)
		(empty jig0002)
		(empty jig0012)
		(empty jig0010)
		(empty jig0013)
		(empty jig0016)
		(empty jig0023)
		(empty jig0018)
		(empty jig0034)
		(empty jig0045)
		(empty jig0027)
		(empty jig0062)
		(empty jig0064)
		(empty jig0059)
		(empty jig0019)
		(empty jig0029)
		(empty jig0067)
		(empty jig0033)
		(empty jig0024)
		(empty jig0055)
		(empty jig0063)
		(empty jig0069)
		(empty jig0036)
		(empty jig0061)
		(empty jig0020)
		(empty jig0047)
		(empty jig0014)
		(empty jig0066)
		(empty jig0021)
		(empty jig0049)
		(empty jig0057)
		(empty jig0042)
		(empty jig0031)
		(empty jig0090)
		(empty jig0037)
		(empty jig0074)
		(empty jig0093)
		(empty jig0104)
		(empty jig0071)
		(empty jig0076)
		(empty jig0086)
		(empty jig0107)
		(empty jig0051)
		(empty jig0091)
		(empty jig0077)
		(empty jig0088)
		(empty jig0087)
		(empty jig0099)
		(empty jig0095)
		(empty jig0101)
		(empty jig0098)
		(empty jig0105)
		(empty jig0100)
		(empty jig0108)
		(empty jig0113)
		(empty jig0127)
		(empty jig0117)
		(empty jig0130)
		(empty jig0115)
		(empty jig0128)
		(empty jig0119)
		(empty jig0126)
		(empty jig0137)
		(empty jig0116)
		(empty jig0148)
		(empty jig0124)
		(empty jig0133)
		(empty jig0145)
		(empty jig0139)
		(empty jig0147)
		(empty jig0138)
		(empty jig0144)
		(empty jig0134)
		(empty jig0141)
		(empty jig0159)
		(empty jig0156)
		(empty jig0149)
		(empty jig0161)
		(empty jig0168)
		(empty jig0167)
		(empty jig0155)
		(empty jig0191)
		(empty jig0164)
		(empty jig0163)
		(empty jig0178)
		(empty jig0188)
		(empty jig0166)
		(empty jig0182)
		(empty jig0174)
		(empty jig0190)
		(empty jig0171)
		(empty jig0183)
		(empty jig0211)
		(empty jig0208)
		(empty jig0186)
		(empty jig0206)
		(empty jig0176)
		(empty jig0204)
		(empty jig0184)
		(empty jig0197)
		(empty jig0201)
		(empty jig0205)
		(empty jig0226)
		(empty jig0227)
		(empty jig0198)
		(empty jig0218)
		(empty jig0200)
		(empty jig0193)
		(empty jig0203)
		(empty jig0225)
		(empty jig0232)
		(empty jig0219)
		(empty jig0229)
		(empty jig0202)
		(empty jig0224)
		(empty jig0240)
		(empty jig0234)
		(empty jig0238)
		(empty jig0236)
		(empty jig0244)
		(empty jig0247)
		(empty jig0251)
		(empty jig0257)
		(empty jig0246)
		(empty jig0265)
		(empty jig0259)
		(empty jig0241)
		(empty jig0264)
		(empty jig0274)
		(empty jig0248)
		(empty jig0255)
		(empty jig0273)
		(empty jig0287)
		(empty jig0250)
		(empty jig0272)
		(empty jig0300)
		(empty jig0295)
		(empty jig0276)
		(empty jig0288)
		(empty jig0258)
		(empty jig0294)
		(empty jig0305)
		(empty jig0303)
		(empty jig0289)
		(empty jig0281)
		(empty jig0299)
		(empty jig0310)
		(empty jig0270)
		(empty jig0307)
		(empty jig0311)
		(empty jig0291)
		(empty jig0321)
		(empty jig0286)
		(empty jig0314)
		(empty jig0279)
		(empty jig0324)
		(empty jig0319)
		(empty jig0329)
		(empty jig0318)
		(empty jig0330)
		(empty jig0316)
		(empty jig0336)
		(empty jig0338)
		(empty jig0344)
		(empty jig0313)
		(empty jig0326)
		(empty jig0341)
		(empty jig0315)
		(empty jig0335)
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
		(to_unload dummy-jig beluga59)
		(to_unload dummy-jig beluga60)
		(to_unload dummy-jig beluga61)
		(to_unload dummy-jig beluga62)
		(to_unload dummy-jig beluga63)
		(to_unload dummy-jig beluga64)
		(to_unload dummy-jig beluga65)
		(to_unload dummy-jig beluga66)
		(to_unload dummy-jig beluga67)
		(to_unload dummy-jig beluga68)
		(to_unload dummy-jig beluga69)
		(to_unload dummy-jig beluga70)
		(to_unload dummy-jig beluga71)
		(to_unload dummy-jig beluga72)
		(to_unload dummy-jig beluga73)
		(to_unload dummy-jig beluga74)
		(to_unload dummy-jig beluga75)
		(to_unload dummy-jig beluga76)
		(to_unload dummy-jig beluga77)
		(to_unload dummy-jig beluga78)
		(to_unload dummy-jig beluga79)
		(to_unload dummy-jig beluga80)
		(to_unload dummy-jig beluga81)
		(to_unload dummy-jig beluga82)
		(to_unload dummy-jig beluga83)
		(to_unload dummy-jig beluga84)
		(to_unload dummy-jig beluga85)
		(to_unload dummy-jig beluga86)
		(to_unload dummy-jig beluga87)
		(to_unload dummy-jig beluga88)
		(to_unload dummy-jig beluga89)
		(to_unload dummy-jig beluga90)
		(to_unload dummy-jig beluga91)
		(to_unload dummy-jig beluga92)
		(to_unload dummy-jig beluga93)
		(to_unload dummy-jig beluga94)
		(to_unload dummy-jig beluga95)
		(to_unload dummy-jig beluga96)
		(to_unload dummy-jig beluga97)
		(to_unload dummy-jig beluga98)
		(to_unload dummy-jig beluga99)
		(to_unload dummy-jig beluga100)
		(to_unload dummy-jig beluga101)
		(to_unload dummy-jig beluga102)
		(to_unload dummy-jig beluga103)
		(to_unload dummy-jig beluga104)
		(to_unload dummy-jig beluga105)
		(to_unload dummy-jig beluga106)
		(to_unload dummy-jig beluga107)
		(to_unload dummy-jig beluga108)
		(to_unload dummy-jig beluga109)
		(to_unload dummy-jig beluga110)
		(to_unload dummy-jig beluga111)
		(to_unload dummy-jig beluga112)
		(to_unload dummy-jig beluga113)
		(to_unload dummy-jig beluga114)
		(to_unload dummy-jig beluga115)
		(to_unload dummy-jig beluga116)
		(to_unload dummy-jig beluga117)
		(to_unload dummy-jig beluga118)
		(to_unload dummy-jig beluga119)
		(to_unload dummy-jig beluga120)
		(to_unload dummy-jig beluga121)
		(to_unload dummy-jig beluga122)
		(to_unload dummy-jig beluga123)
		(to_unload dummy-jig beluga124)
		(to_unload dummy-jig beluga125)
		(to_unload dummy-jig beluga126)
		(to_unload dummy-jig beluga127)
		(to_unload dummy-jig beluga128)
		(to_unload dummy-jig beluga129)
		(to_unload dummy-jig beluga130)
		(to_unload dummy-jig beluga131)
		(to_unload dummy-jig beluga132)
		(to_unload dummy-jig beluga133)
		(to_unload dummy-jig beluga134)
		(to_unload dummy-jig beluga135)
		(to_unload dummy-jig beluga136)
		(to_unload dummy-jig beluga137)
		(to_unload dummy-jig beluga138)
		(to_unload dummy-jig beluga139)
		(to_unload dummy-jig beluga140)
		(to_unload dummy-jig beluga141)
		(to_unload dummy-jig beluga142)
		(to_unload dummy-jig beluga143)
		(to_unload dummy-jig beluga144)
		(to_unload dummy-jig beluga145)
		(to_unload dummy-jig beluga146)
		(to_unload dummy-jig beluga147)
		(to_unload dummy-jig beluga148)
		(to_unload dummy-jig beluga149)
		(to_unload dummy-jig beluga150)
		(to_unload dummy-jig beluga151)
		(to_unload dummy-jig beluga152)
		(to_unload dummy-jig beluga153)
		(to_unload dummy-jig beluga154)
		(to_unload dummy-jig beluga155)
		(to_unload dummy-jig beluga156)
		(to_unload dummy-jig beluga157)
		(to_unload dummy-jig beluga158)
		(to_unload dummy-jig beluga159)
		(to_unload dummy-jig beluga160)
		(to_unload dummy-jig beluga161)
		(to_unload dummy-jig beluga162)
		(to_unload dummy-jig beluga163)
		(to_unload dummy-jig beluga164)
		(to_unload dummy-jig beluga165)
		(to_unload dummy-jig beluga166)
		(to_unload dummy-jig beluga167)
		(to_unload dummy-jig beluga168)
		(to_unload dummy-jig beluga169)
		(to_unload dummy-jig beluga170)
		(to_unload dummy-jig beluga171)
		(to_unload dummy-jig beluga172)
		(to_unload dummy-jig beluga173)
		(to_unload dummy-jig beluga174)
		(to_unload dummy-jig beluga175)
		(to_unload dummy-jig beluga176)
		(to_unload dummy-jig beluga177)
		(to_unload dummy-jig beluga178)
		(to_unload dummy-jig beluga179)
		(to_unload dummy-jig beluga180)
		(to_unload dummy-jig beluga181)
		(to_unload dummy-jig beluga182)
		(to_unload dummy-jig beluga183)
		(to_unload dummy-jig beluga184)
		(to_unload dummy-jig beluga185)
		(to_unload dummy-jig beluga186)
		(to_unload dummy-jig beluga187)
		(to_unload dummy-jig beluga188)
		(to_unload dummy-jig beluga189)
		(to_unload dummy-jig beluga190)
		(to_unload dummy-jig beluga191)
		(to_unload dummy-jig beluga192)
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
		(to_load dummy-type dummy-slot beluga59)
		(to_load dummy-type dummy-slot beluga60)
		(to_load dummy-type dummy-slot beluga61)
		(to_load dummy-type dummy-slot beluga62)
		(to_load dummy-type dummy-slot beluga63)
		(to_load dummy-type dummy-slot beluga64)
		(to_load dummy-type dummy-slot beluga65)
		(to_load dummy-type dummy-slot beluga66)
		(to_load dummy-type dummy-slot beluga67)
		(to_load dummy-type dummy-slot beluga68)
		(to_load dummy-type dummy-slot beluga69)
		(to_load dummy-type dummy-slot beluga70)
		(to_load dummy-type dummy-slot beluga71)
		(to_load dummy-type dummy-slot beluga72)
		(to_load dummy-type dummy-slot beluga73)
		(to_load dummy-type dummy-slot beluga74)
		(to_load dummy-type dummy-slot beluga75)
		(to_load dummy-type dummy-slot beluga76)
		(to_load dummy-type dummy-slot beluga77)
		(to_load dummy-type dummy-slot beluga78)
		(to_load dummy-type dummy-slot beluga79)
		(to_load dummy-type dummy-slot beluga80)
		(to_load dummy-type dummy-slot beluga81)
		(to_load dummy-type dummy-slot beluga82)
		(to_load dummy-type dummy-slot beluga83)
		(to_load dummy-type dummy-slot beluga84)
		(to_load dummy-type dummy-slot beluga85)
		(to_load dummy-type dummy-slot beluga86)
		(to_load dummy-type dummy-slot beluga87)
		(to_load dummy-type dummy-slot beluga88)
		(to_load dummy-type dummy-slot beluga89)
		(to_load dummy-type dummy-slot beluga90)
		(to_load dummy-type dummy-slot beluga91)
		(to_load dummy-type dummy-slot beluga92)
		(to_load dummy-type dummy-slot beluga93)
		(to_load dummy-type dummy-slot beluga94)
		(to_load dummy-type dummy-slot beluga95)
		(to_load dummy-type dummy-slot beluga96)
		(to_load dummy-type dummy-slot beluga97)
		(to_load dummy-type dummy-slot beluga98)
		(to_load dummy-type dummy-slot beluga99)
		(to_load dummy-type dummy-slot beluga100)
		(to_load dummy-type dummy-slot beluga101)
		(to_load dummy-type dummy-slot beluga102)
		(to_load dummy-type dummy-slot beluga103)
		(to_load dummy-type dummy-slot beluga104)
		(to_load dummy-type dummy-slot beluga105)
		(to_load dummy-type dummy-slot beluga106)
		(to_load dummy-type dummy-slot beluga107)
		(to_load dummy-type dummy-slot beluga108)
		(to_load dummy-type dummy-slot beluga109)
		(to_load dummy-type dummy-slot beluga110)
		(to_load dummy-type dummy-slot beluga111)
		(to_load dummy-type dummy-slot beluga112)
		(to_load dummy-type dummy-slot beluga113)
		(to_load dummy-type dummy-slot beluga114)
		(to_load dummy-type dummy-slot beluga115)
		(to_load dummy-type dummy-slot beluga116)
		(to_load dummy-type dummy-slot beluga117)
		(to_load dummy-type dummy-slot beluga118)
		(to_load dummy-type dummy-slot beluga119)
		(to_load dummy-type dummy-slot beluga120)
		(to_load dummy-type dummy-slot beluga121)
		(to_load dummy-type dummy-slot beluga122)
		(to_load dummy-type dummy-slot beluga123)
		(to_load dummy-type dummy-slot beluga124)
		(to_load dummy-type dummy-slot beluga125)
		(to_load dummy-type dummy-slot beluga126)
		(to_load dummy-type dummy-slot beluga127)
		(to_load dummy-type dummy-slot beluga128)
		(to_load dummy-type dummy-slot beluga129)
		(to_load dummy-type dummy-slot beluga130)
		(to_load dummy-type dummy-slot beluga131)
		(to_load dummy-type dummy-slot beluga132)
		(to_load dummy-type dummy-slot beluga133)
		(to_load dummy-type dummy-slot beluga134)
		(to_load dummy-type dummy-slot beluga135)
		(to_load dummy-type dummy-slot beluga136)
		(to_load dummy-type dummy-slot beluga137)
		(to_load dummy-type dummy-slot beluga138)
		(to_load dummy-type dummy-slot beluga139)
		(to_load dummy-type dummy-slot beluga140)
		(to_load dummy-type dummy-slot beluga141)
		(to_load dummy-type dummy-slot beluga142)
		(to_load dummy-type dummy-slot beluga143)
		(to_load dummy-type dummy-slot beluga144)
		(to_load dummy-type dummy-slot beluga145)
		(to_load dummy-type dummy-slot beluga146)
		(to_load dummy-type dummy-slot beluga147)
		(to_load dummy-type dummy-slot beluga148)
		(to_load dummy-type dummy-slot beluga149)
		(to_load dummy-type dummy-slot beluga150)
		(to_load dummy-type dummy-slot beluga151)
		(to_load dummy-type dummy-slot beluga152)
		(to_load dummy-type dummy-slot beluga153)
		(to_load dummy-type dummy-slot beluga154)
		(to_load dummy-type dummy-slot beluga155)
		(to_load dummy-type dummy-slot beluga156)
		(to_load dummy-type dummy-slot beluga157)
		(to_load dummy-type dummy-slot beluga158)
		(to_load dummy-type dummy-slot beluga159)
		(to_load dummy-type dummy-slot beluga160)
		(to_load dummy-type dummy-slot beluga161)
		(to_load dummy-type dummy-slot beluga162)
		(to_load dummy-type dummy-slot beluga163)
		(to_load dummy-type dummy-slot beluga164)
		(to_load dummy-type dummy-slot beluga165)
		(to_load dummy-type dummy-slot beluga166)
		(to_load dummy-type dummy-slot beluga167)
		(to_load dummy-type dummy-slot beluga168)
		(to_load dummy-type dummy-slot beluga169)
		(to_load dummy-type dummy-slot beluga170)
		(to_load dummy-type dummy-slot beluga171)
		(to_load dummy-type dummy-slot beluga172)
		(to_load dummy-type dummy-slot beluga173)
		(to_load dummy-type dummy-slot beluga174)
		(to_load dummy-type dummy-slot beluga175)
		(to_load dummy-type dummy-slot beluga176)
		(to_load dummy-type dummy-slot beluga177)
		(to_load dummy-type dummy-slot beluga178)
		(to_load dummy-type dummy-slot beluga179)
		(to_load dummy-type dummy-slot beluga180)
		(to_load dummy-type dummy-slot beluga181)
		(to_load dummy-type dummy-slot beluga182)
		(to_load dummy-type dummy-slot beluga183)
		(to_load dummy-type dummy-slot beluga184)
		(to_load dummy-type dummy-slot beluga185)
		(to_load dummy-type dummy-slot beluga186)
		(to_load dummy-type dummy-slot beluga187)
		(to_load dummy-type dummy-slot beluga188)
		(to_load dummy-type dummy-slot beluga189)
		(to_load dummy-type dummy-slot beluga190)
		(to_load dummy-type dummy-slot beluga191)
		(to_load dummy-type dummy-slot beluga192)
	))
  (:metric minimize (total-cost))
)