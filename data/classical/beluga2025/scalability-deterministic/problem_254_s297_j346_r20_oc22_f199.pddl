(define
	(problem beluga-problem_254_s297_j346_r20_oc22_f199)
	(:domain beluga)
  (:objects
		; Numbers: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 38, 40}
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
		n31 - num
		n32 - num
		n34 - num
		n35 - num
		n36 - num
		n38 - num
		n40 - num
		; trailers:
		beluga_trailer_1 - trailer
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
		beluga193 - beluga
		beluga194 - beluga
		beluga195 - beluga
		beluga196 - beluga
		beluga197 - beluga
		beluga198 - beluga
		beluga199 - beluga
		; Slots for outgoing flights:
		slot0 - slot
		slot1 - slot
		slot2 - slot
		slot3 - slot
		slot4 - slot
		slot5 - slot
		slot6 - slot
		slot7 - slot
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
		(fit  n21  n04  n25 rack02)
		(fit  n17  n08  n25 rack02)
		(fit  n16  n09  n25 rack02)
		(fit  n14  n11  n25 rack02)
		(fit  n07  n18  n25 rack02)
		(fit  n00  n25  n25 rack02)
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
		(fit  n25  n04  n29 rack02)
		(fit  n21  n08  n29 rack02)
		(fit  n20  n09  n29 rack02)
		(fit  n18  n11  n29 rack02)
		(fit  n11  n18  n29 rack02)
		(fit  n04  n25  n29 rack02)
		(fit  n26  n04  n30 rack02)
		(fit  n22  n08  n30 rack02)
		(fit  n21  n09  n30 rack02)
		(fit  n19  n11  n30 rack02)
		(fit  n12  n18  n30 rack02)
		(fit  n05  n25  n30 rack02)
		(fit  n02  n32  n34 rack02)
		(fit  n30  n04  n34 rack02)
		(fit  n26  n08  n34 rack02)
		(fit  n25  n09  n34 rack02)
		(fit  n23  n11  n34 rack02)
		(fit  n16  n18  n34 rack02)
		(fit  n09  n25  n34 rack02)
		(fit  n06  n32  n38 rack02)
		(fit  n34  n04  n38 rack02)
		(fit  n30  n08  n38 rack02)
		(fit  n29  n09  n38 rack02)
		(fit  n27  n11  n38 rack02)
		(fit  n20  n18  n38 rack02)
		(fit  n13  n25  n38 rack02)
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
		(fit  n22  n04  n26 rack03)
		(fit  n18  n08  n26 rack03)
		(fit  n17  n09  n26 rack03)
		(fit  n15  n11  n26 rack03)
		(fit  n08  n18  n26 rack03)
		(fit  n01  n25  n26 rack03)
		(fit  n26  n04  n30 rack03)
		(fit  n22  n08  n30 rack03)
		(fit  n21  n09  n30 rack03)
		(fit  n19  n11  n30 rack03)
		(fit  n12  n18  n30 rack03)
		(fit  n05  n25  n30 rack03)
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
		(fit  n19  n04  n23 rack05)
		(fit  n15  n08  n23 rack05)
		(fit  n14  n09  n23 rack05)
		(fit  n12  n11  n23 rack05)
		(fit  n05  n18  n23 rack05)
		(fit  n20  n04  n24 rack05)
		(fit  n16  n08  n24 rack05)
		(fit  n15  n09  n24 rack05)
		(fit  n13  n11  n24 rack05)
		(fit  n06  n18  n24 rack05)
		(fit  n21  n04  n25 rack05)
		(fit  n17  n08  n25 rack05)
		(fit  n16  n09  n25 rack05)
		(fit  n14  n11  n25 rack05)
		(fit  n07  n18  n25 rack05)
		(fit  n00  n25  n25 rack05)
		(fit  n23  n04  n27 rack05)
		(fit  n19  n08  n27 rack05)
		(fit  n18  n09  n27 rack05)
		(fit  n16  n11  n27 rack05)
		(fit  n09  n18  n27 rack05)
		(fit  n02  n25  n27 rack05)
		(fit  n24  n04  n28 rack05)
		(fit  n20  n08  n28 rack05)
		(fit  n19  n09  n28 rack05)
		(fit  n17  n11  n28 rack05)
		(fit  n10  n18  n28 rack05)
		(fit  n03  n25  n28 rack05)
		(fit  n00  n32  n32 rack05)
		(fit  n28  n04  n32 rack05)
		(fit  n24  n08  n32 rack05)
		(fit  n23  n09  n32 rack05)
		(fit  n21  n11  n32 rack05)
		(fit  n14  n18  n32 rack05)
		(fit  n07  n25  n32 rack05)
		(fit  n04  n32  n36 rack05)
		(fit  n32  n04  n36 rack05)
		(fit  n28  n08  n36 rack05)
		(fit  n27  n09  n36 rack05)
		(fit  n25  n11  n36 rack05)
		(fit  n18  n18  n36 rack05)
		(fit  n11  n25  n36 rack05)
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
		(fit  n09  n04  n13 rack07)
		(fit  n05  n08  n13 rack07)
		(fit  n04  n09  n13 rack07)
		(fit  n02  n11  n13 rack07)
		(fit  n10  n04  n14 rack07)
		(fit  n06  n08  n14 rack07)
		(fit  n05  n09  n14 rack07)
		(fit  n03  n11  n14 rack07)
		(fit  n14  n04  n18 rack07)
		(fit  n10  n08  n18 rack07)
		(fit  n09  n09  n18 rack07)
		(fit  n07  n11  n18 rack07)
		(fit  n00  n18  n18 rack07)
		(fit  n18  n04  n22 rack07)
		(fit  n14  n08  n22 rack07)
		(fit  n13  n09  n22 rack07)
		(fit  n11  n11  n22 rack07)
		(fit  n04  n18  n22 rack07)
		; Sizes fitting rack: rack08
		(fit  n00  n04  n04 rack08)
		(fit  n01  n04  n05 rack08)
		(fit  n02  n04  n06 rack08)
		(fit  n03  n04  n07 rack08)
		(fit  n04  n04  n08 rack08)
		(fit  n00  n08  n08 rack08)
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
		(fit  n08  n04  n12 rack08)
		(fit  n04  n08  n12 rack08)
		(fit  n03  n09  n12 rack08)
		(fit  n01  n11  n12 rack08)
		(fit  n09  n04  n13 rack08)
		(fit  n05  n08  n13 rack08)
		(fit  n04  n09  n13 rack08)
		(fit  n02  n11  n13 rack08)
		(fit  n11  n04  n15 rack08)
		(fit  n07  n08  n15 rack08)
		(fit  n06  n09  n15 rack08)
		(fit  n04  n11  n15 rack08)
		(fit  n12  n04  n16 rack08)
		(fit  n08  n08  n16 rack08)
		(fit  n07  n09  n16 rack08)
		(fit  n05  n11  n16 rack08)
		(fit  n13  n04  n17 rack08)
		(fit  n09  n08  n17 rack08)
		(fit  n08  n09  n17 rack08)
		(fit  n06  n11  n17 rack08)
		(fit  n15  n04  n19 rack08)
		(fit  n11  n08  n19 rack08)
		(fit  n10  n09  n19 rack08)
		(fit  n08  n11  n19 rack08)
		(fit  n01  n18  n19 rack08)
		(fit  n16  n04  n20 rack08)
		(fit  n12  n08  n20 rack08)
		(fit  n11  n09  n20 rack08)
		(fit  n09  n11  n20 rack08)
		(fit  n02  n18  n20 rack08)
		(fit  n20  n04  n24 rack08)
		(fit  n16  n08  n24 rack08)
		(fit  n15  n09  n24 rack08)
		(fit  n13  n11  n24 rack08)
		(fit  n06  n18  n24 rack08)
		(fit  n24  n04  n28 rack08)
		(fit  n20  n08  n28 rack08)
		(fit  n19  n09  n28 rack08)
		(fit  n17  n11  n28 rack08)
		(fit  n10  n18  n28 rack08)
		(fit  n03  n25  n28 rack08)
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
		(fit  n25  n04  n29 rack10)
		(fit  n21  n08  n29 rack10)
		(fit  n20  n09  n29 rack10)
		(fit  n18  n11  n29 rack10)
		(fit  n11  n18  n29 rack10)
		(fit  n04  n25  n29 rack10)
		(fit  n27  n04  n31 rack10)
		(fit  n23  n08  n31 rack10)
		(fit  n22  n09  n31 rack10)
		(fit  n20  n11  n31 rack10)
		(fit  n13  n18  n31 rack10)
		(fit  n06  n25  n31 rack10)
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
		(fit  n08  n32  n40 rack10)
		(fit  n36  n04  n40 rack10)
		(fit  n32  n08  n40 rack10)
		(fit  n31  n09  n40 rack10)
		(fit  n29  n11  n40 rack10)
		(fit  n22  n18  n40 rack10)
		(fit  n15  n25  n40 rack10)
		; Sizes fitting rack: rack11
		(fit  n00  n04  n04 rack11)
		(fit  n01  n04  n05 rack11)
		(fit  n03  n04  n07 rack11)
		(fit  n04  n04  n08 rack11)
		(fit  n00  n08  n08 rack11)
		(fit  n05  n04  n09 rack11)
		(fit  n01  n08  n09 rack11)
		(fit  n00  n09  n09 rack11)
		(fit  n07  n04  n11 rack11)
		(fit  n03  n08  n11 rack11)
		(fit  n02  n09  n11 rack11)
		(fit  n00  n11  n11 rack11)
		(fit  n08  n04  n12 rack11)
		(fit  n04  n08  n12 rack11)
		(fit  n03  n09  n12 rack11)
		(fit  n01  n11  n12 rack11)
		(fit  n12  n04  n16 rack11)
		(fit  n08  n08  n16 rack11)
		(fit  n07  n09  n16 rack11)
		(fit  n05  n11  n16 rack11)
		(fit  n16  n04  n20 rack11)
		(fit  n12  n08  n20 rack11)
		(fit  n11  n09  n20 rack11)
		(fit  n09  n11  n20 rack11)
		(fit  n02  n18  n20 rack11)
		; Sizes fitting rack: rack12
		(fit  n00  n04  n04 rack12)
		(fit  n01  n04  n05 rack12)
		(fit  n02  n04  n06 rack12)
		(fit  n03  n04  n07 rack12)
		(fit  n04  n04  n08 rack12)
		(fit  n00  n08  n08 rack12)
		(fit  n05  n04  n09 rack12)
		(fit  n01  n08  n09 rack12)
		(fit  n00  n09  n09 rack12)
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
		(fit  n09  n04  n13 rack12)
		(fit  n05  n08  n13 rack12)
		(fit  n04  n09  n13 rack12)
		(fit  n02  n11  n13 rack12)
		(fit  n11  n04  n15 rack12)
		(fit  n07  n08  n15 rack12)
		(fit  n06  n09  n15 rack12)
		(fit  n04  n11  n15 rack12)
		(fit  n12  n04  n16 rack12)
		(fit  n08  n08  n16 rack12)
		(fit  n07  n09  n16 rack12)
		(fit  n05  n11  n16 rack12)
		(fit  n13  n04  n17 rack12)
		(fit  n09  n08  n17 rack12)
		(fit  n08  n09  n17 rack12)
		(fit  n06  n11  n17 rack12)
		(fit  n15  n04  n19 rack12)
		(fit  n11  n08  n19 rack12)
		(fit  n10  n09  n19 rack12)
		(fit  n08  n11  n19 rack12)
		(fit  n01  n18  n19 rack12)
		(fit  n16  n04  n20 rack12)
		(fit  n12  n08  n20 rack12)
		(fit  n11  n09  n20 rack12)
		(fit  n09  n11  n20 rack12)
		(fit  n02  n18  n20 rack12)
		(fit  n20  n04  n24 rack12)
		(fit  n16  n08  n24 rack12)
		(fit  n15  n09  n24 rack12)
		(fit  n13  n11  n24 rack12)
		(fit  n06  n18  n24 rack12)
		(fit  n24  n04  n28 rack12)
		(fit  n20  n08  n28 rack12)
		(fit  n19  n09  n28 rack12)
		(fit  n17  n11  n28 rack12)
		(fit  n10  n18  n28 rack12)
		(fit  n03  n25  n28 rack12)
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
		(fit  n08  n04  n12 rack13)
		(fit  n04  n08  n12 rack13)
		(fit  n03  n09  n12 rack13)
		(fit  n01  n11  n12 rack13)
		(fit  n10  n04  n14 rack13)
		(fit  n06  n08  n14 rack13)
		(fit  n05  n09  n14 rack13)
		(fit  n03  n11  n14 rack13)
		(fit  n11  n04  n15 rack13)
		(fit  n07  n08  n15 rack13)
		(fit  n06  n09  n15 rack13)
		(fit  n04  n11  n15 rack13)
		(fit  n12  n04  n16 rack13)
		(fit  n08  n08  n16 rack13)
		(fit  n07  n09  n16 rack13)
		(fit  n05  n11  n16 rack13)
		(fit  n14  n04  n18 rack13)
		(fit  n10  n08  n18 rack13)
		(fit  n09  n09  n18 rack13)
		(fit  n07  n11  n18 rack13)
		(fit  n00  n18  n18 rack13)
		(fit  n15  n04  n19 rack13)
		(fit  n11  n08  n19 rack13)
		(fit  n10  n09  n19 rack13)
		(fit  n08  n11  n19 rack13)
		(fit  n01  n18  n19 rack13)
		(fit  n19  n04  n23 rack13)
		(fit  n15  n08  n23 rack13)
		(fit  n14  n09  n23 rack13)
		(fit  n12  n11  n23 rack13)
		(fit  n05  n18  n23 rack13)
		(fit  n23  n04  n27 rack13)
		(fit  n19  n08  n27 rack13)
		(fit  n18  n09  n27 rack13)
		(fit  n16  n11  n27 rack13)
		(fit  n09  n18  n27 rack13)
		(fit  n02  n25  n27 rack13)
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
		(fit  n11  n04  n15 rack14)
		(fit  n07  n08  n15 rack14)
		(fit  n06  n09  n15 rack14)
		(fit  n04  n11  n15 rack14)
		(fit  n12  n04  n16 rack14)
		(fit  n08  n08  n16 rack14)
		(fit  n07  n09  n16 rack14)
		(fit  n05  n11  n16 rack14)
		(fit  n16  n04  n20 rack14)
		(fit  n12  n08  n20 rack14)
		(fit  n11  n09  n20 rack14)
		(fit  n09  n11  n20 rack14)
		(fit  n02  n18  n20 rack14)
		(fit  n20  n04  n24 rack14)
		(fit  n16  n08  n24 rack14)
		(fit  n15  n09  n24 rack14)
		(fit  n13  n11  n24 rack14)
		(fit  n06  n18  n24 rack14)
		; Sizes fitting rack: rack15
		(fit  n00  n04  n04 rack15)
		(fit  n01  n04  n05 rack15)
		(fit  n02  n04  n06 rack15)
		(fit  n03  n04  n07 rack15)
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
		(fit  n09  n04  n13 rack15)
		(fit  n05  n08  n13 rack15)
		(fit  n04  n09  n13 rack15)
		(fit  n02  n11  n13 rack15)
		(fit  n10  n04  n14 rack15)
		(fit  n06  n08  n14 rack15)
		(fit  n05  n09  n14 rack15)
		(fit  n03  n11  n14 rack15)
		(fit  n14  n04  n18 rack15)
		(fit  n10  n08  n18 rack15)
		(fit  n09  n09  n18 rack15)
		(fit  n07  n11  n18 rack15)
		(fit  n00  n18  n18 rack15)
		(fit  n18  n04  n22 rack15)
		(fit  n14  n08  n22 rack15)
		(fit  n13  n09  n22 rack15)
		(fit  n11  n11  n22 rack15)
		(fit  n04  n18  n22 rack15)
		; Sizes fitting rack: rack16
		(fit  n00  n04  n04 rack16)
		(fit  n01  n04  n05 rack16)
		(fit  n02  n04  n06 rack16)
		(fit  n03  n04  n07 rack16)
		(fit  n04  n04  n08 rack16)
		(fit  n00  n08  n08 rack16)
		(fit  n06  n04  n10 rack16)
		(fit  n02  n08  n10 rack16)
		(fit  n01  n09  n10 rack16)
		(fit  n07  n04  n11 rack16)
		(fit  n03  n08  n11 rack16)
		(fit  n02  n09  n11 rack16)
		(fit  n00  n11  n11 rack16)
		(fit  n08  n04  n12 rack16)
		(fit  n04  n08  n12 rack16)
		(fit  n03  n09  n12 rack16)
		(fit  n01  n11  n12 rack16)
		(fit  n10  n04  n14 rack16)
		(fit  n06  n08  n14 rack16)
		(fit  n05  n09  n14 rack16)
		(fit  n03  n11  n14 rack16)
		(fit  n11  n04  n15 rack16)
		(fit  n07  n08  n15 rack16)
		(fit  n06  n09  n15 rack16)
		(fit  n04  n11  n15 rack16)
		(fit  n15  n04  n19 rack16)
		(fit  n11  n08  n19 rack16)
		(fit  n10  n09  n19 rack16)
		(fit  n08  n11  n19 rack16)
		(fit  n01  n18  n19 rack16)
		(fit  n19  n04  n23 rack16)
		(fit  n15  n08  n23 rack16)
		(fit  n14  n09  n23 rack16)
		(fit  n12  n11  n23 rack16)
		(fit  n05  n18  n23 rack16)
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
		(fit  n06  n04  n10 rack18)
		(fit  n02  n08  n10 rack18)
		(fit  n01  n09  n10 rack18)
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
		(fit  n10  n04  n14 rack18)
		(fit  n06  n08  n14 rack18)
		(fit  n05  n09  n14 rack18)
		(fit  n03  n11  n14 rack18)
		(fit  n11  n04  n15 rack18)
		(fit  n07  n08  n15 rack18)
		(fit  n06  n09  n15 rack18)
		(fit  n04  n11  n15 rack18)
		(fit  n12  n04  n16 rack18)
		(fit  n08  n08  n16 rack18)
		(fit  n07  n09  n16 rack18)
		(fit  n05  n11  n16 rack18)
		(fit  n14  n04  n18 rack18)
		(fit  n10  n08  n18 rack18)
		(fit  n09  n09  n18 rack18)
		(fit  n07  n11  n18 rack18)
		(fit  n00  n18  n18 rack18)
		(fit  n15  n04  n19 rack18)
		(fit  n11  n08  n19 rack18)
		(fit  n10  n09  n19 rack18)
		(fit  n08  n11  n19 rack18)
		(fit  n01  n18  n19 rack18)
		(fit  n16  n04  n20 rack18)
		(fit  n12  n08  n20 rack18)
		(fit  n11  n09  n20 rack18)
		(fit  n09  n11  n20 rack18)
		(fit  n02  n18  n20 rack18)
		(fit  n18  n04  n22 rack18)
		(fit  n14  n08  n22 rack18)
		(fit  n13  n09  n22 rack18)
		(fit  n11  n11  n22 rack18)
		(fit  n04  n18  n22 rack18)
		(fit  n19  n04  n23 rack18)
		(fit  n15  n08  n23 rack18)
		(fit  n14  n09  n23 rack18)
		(fit  n12  n11  n23 rack18)
		(fit  n05  n18  n23 rack18)
		(fit  n23  n04  n27 rack18)
		(fit  n19  n08  n27 rack18)
		(fit  n18  n09  n27 rack18)
		(fit  n16  n11  n27 rack18)
		(fit  n09  n18  n27 rack18)
		(fit  n02  n25  n27 rack18)
		(fit  n27  n04  n31 rack18)
		(fit  n23  n08  n31 rack18)
		(fit  n22  n09  n31 rack18)
		(fit  n20  n11  n31 rack18)
		(fit  n13  n18  n31 rack18)
		(fit  n06  n25  n31 rack18)
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
		(fit  n13  n04  n17 rack19)
		(fit  n09  n08  n17 rack19)
		(fit  n08  n09  n17 rack19)
		(fit  n06  n11  n17 rack19)
		(fit  n14  n04  n18 rack19)
		(fit  n10  n08  n18 rack19)
		(fit  n09  n09  n18 rack19)
		(fit  n07  n11  n18 rack19)
		(fit  n00  n18  n18 rack19)
		(fit  n18  n04  n22 rack19)
		(fit  n14  n08  n22 rack19)
		(fit  n13  n09  n22 rack19)
		(fit  n11  n11  n22 rack19)
		(fit  n04  n18  n22 rack19)
		(fit  n22  n04  n26 rack19)
		(fit  n18  n08  n26 rack19)
		(fit  n17  n09  n26 rack19)
		(fit  n15  n11  n26 rack19)
		(fit  n08  n18  n26 rack19)
		(fit  n01  n25  n26 rack19)
		; trailers (Beluga side):
		(empty beluga_trailer_1)
		(at-side beluga_trailer_1 bside)
		; trailers (Factory side):
		(empty factory_trailer_1)
		(at-side factory_trailer_1 fside)
		(empty factory_trailer_2)
		(at-side factory_trailer_2 fside)
		; Racks 20
		; Rack:rack00
		(empty rack00)
		(at-side rack00 bside)
		(at-side rack00 fside)
		(free-space rack00 n23)
		; Rack:rack01
		(empty rack01)
		(at-side rack01 bside)
		(at-side rack01 fside)
		(free-space rack01 n21)
		; Rack:rack02
		(empty rack02)
		(at-side rack02 bside)
		(at-side rack02 fside)
		(free-space rack02 n38)
		; Rack:rack03
		(empty rack03)
		(at-side rack03 bside)
		(at-side rack03 fside)
		(free-space rack03 n30)
		; Rack:rack04
		(at-side rack04 bside)
		(at-side rack04 fside)
		(free-space rack04 n06)
		(in jig0001 rack04)
		(clear jig0001 bside)
		(clear jig0001 fside)
		; Rack:rack05
		(at-side rack05 bside)
		(at-side rack05 fside)
		(free-space rack05 n11)
		(in jig0004 rack05)
		(clear jig0004 bside)
		(clear jig0004 fside)
		; Rack:rack06
		(empty rack06)
		(at-side rack06 bside)
		(at-side rack06 fside)
		(free-space rack06 n24)
		; Rack:rack07
		(empty rack07)
		(at-side rack07 bside)
		(at-side rack07 fside)
		(free-space rack07 n22)
		; Rack:rack08
		(empty rack08)
		(at-side rack08 bside)
		(at-side rack08 fside)
		(free-space rack08 n28)
		; Rack:rack09
		(empty rack09)
		(at-side rack09 bside)
		(at-side rack09 fside)
		(free-space rack09 n22)
		; Rack:rack10
		(at-side rack10 bside)
		(at-side rack10 fside)
		(free-space rack10 n08)
		(in jig0006 rack10)
		(clear jig0006 bside)
		(clear jig0006 fside)
		; Rack:rack11
		(empty rack11)
		(at-side rack11 bside)
		(at-side rack11 fside)
		(free-space rack11 n20)
		; Rack:rack12
		(empty rack12)
		(at-side rack12 bside)
		(at-side rack12 fside)
		(free-space rack12 n28)
		; Rack:rack13
		(at-side rack13 bside)
		(at-side rack13 fside)
		(free-space rack13 n05)
		(in jig0003 rack13)
		(clear jig0003 bside)
		(next-to jig0003 jig0005 bside)
		(next-to jig0005 jig0003 fside)
		(in jig0005 rack13)
		(clear jig0005 fside)
		; Rack:rack14
		(empty rack14)
		(at-side rack14 bside)
		(at-side rack14 fside)
		(free-space rack14 n24)
		; Rack:rack15
		(empty rack15)
		(at-side rack15 bside)
		(at-side rack15 fside)
		(free-space rack15 n22)
		; Rack:rack16
		(empty rack16)
		(at-side rack16 bside)
		(at-side rack16 fside)
		(free-space rack16 n23)
		; Rack:rack17
		(at-side rack17 bside)
		(at-side rack17 fside)
		(free-space rack17 n03)
		(in jig0007 rack17)
		(clear jig0007 bside)
		(clear jig0007 fside)
		; Rack:rack18
		(at-side rack18 bside)
		(at-side rack18 fside)
		(free-space rack18 n20)
		(in jig0002 rack18)
		(clear jig0002 bside)
		(clear jig0002 fside)
		; Rack:rack19
		(empty rack19)
		(at-side rack19 bside)
		(at-side rack19 fside)
		(free-space rack19 n26)
		; Jigs (size):
		(is_type jig0001 typeE)
		(size jig0001 n32)
		(empty-size jig0001 n32)
		(empty jig0001)
		(is_type jig0002 typeB)
		(size jig0002 n11)
		(empty-size jig0002 n08)
		(is_type jig0003 typeC)
		(size jig0003 n18)
		(empty-size jig0003 n09)
		(is_type jig0004 typeD)
		(size jig0004 n25)
		(empty-size jig0004 n18)
		(is_type jig0005 typeA)
		(size jig0005 n04)
		(empty-size jig0005 n04)
		(is_type jig0006 typeE)
		(size jig0006 n32)
		(empty-size jig0006 n32)
		(empty jig0006)
		(is_type jig0007 typeE)
		(size jig0007 n32)
		(empty-size jig0007 n32)
		(is_type jig0008 typeD)
		(size jig0008 n25)
		(empty-size jig0008 n18)
		(is_type jig0009 typeE)
		(size jig0009 n32)
		(empty-size jig0009 n32)
		(is_type jig0010 typeD)
		(size jig0010 n25)
		(empty-size jig0010 n18)
		(is_type jig0011 typeE)
		(size jig0011 n32)
		(empty-size jig0011 n32)
		(is_type jig0012 typeD)
		(size jig0012 n25)
		(empty-size jig0012 n18)
		(is_type jig0013 typeC)
		(size jig0013 n18)
		(empty-size jig0013 n09)
		(is_type jig0014 typeC)
		(size jig0014 n18)
		(empty-size jig0014 n09)
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
		(is_type jig0025 typeE)
		(size jig0025 n32)
		(empty-size jig0025 n32)
		(is_type jig0026 typeE)
		(size jig0026 n32)
		(empty-size jig0026 n32)
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
		(is_type jig0037 typeD)
		(size jig0037 n25)
		(empty-size jig0037 n18)
		(is_type jig0038 typeC)
		(size jig0038 n18)
		(empty-size jig0038 n09)
		(is_type jig0039 typeC)
		(size jig0039 n18)
		(empty-size jig0039 n09)
		(is_type jig0040 typeD)
		(size jig0040 n25)
		(empty-size jig0040 n18)
		(is_type jig0041 typeE)
		(size jig0041 n32)
		(empty-size jig0041 n32)
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
		(is_type jig0046 typeD)
		(size jig0046 n25)
		(empty-size jig0046 n18)
		(is_type jig0047 typeD)
		(size jig0047 n25)
		(empty-size jig0047 n18)
		(is_type jig0048 typeC)
		(size jig0048 n18)
		(empty-size jig0048 n09)
		(is_type jig0049 typeC)
		(size jig0049 n18)
		(empty-size jig0049 n09)
		(is_type jig0050 typeD)
		(size jig0050 n25)
		(empty-size jig0050 n18)
		(is_type jig0051 typeC)
		(size jig0051 n18)
		(empty-size jig0051 n09)
		(is_type jig0052 typeC)
		(size jig0052 n18)
		(empty-size jig0052 n09)
		(is_type jig0053 typeC)
		(size jig0053 n18)
		(empty-size jig0053 n09)
		(is_type jig0054 typeC)
		(size jig0054 n18)
		(empty-size jig0054 n09)
		(is_type jig0055 typeE)
		(size jig0055 n32)
		(empty-size jig0055 n32)
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
		(is_type jig0066 typeB)
		(size jig0066 n11)
		(empty-size jig0066 n08)
		(is_type jig0067 typeB)
		(size jig0067 n11)
		(empty-size jig0067 n08)
		(is_type jig0068 typeB)
		(size jig0068 n11)
		(empty-size jig0068 n08)
		(is_type jig0069 typeD)
		(size jig0069 n25)
		(empty-size jig0069 n18)
		(is_type jig0070 typeD)
		(size jig0070 n25)
		(empty-size jig0070 n18)
		(is_type jig0071 typeC)
		(size jig0071 n18)
		(empty-size jig0071 n09)
		(is_type jig0072 typeC)
		(size jig0072 n18)
		(empty-size jig0072 n09)
		(is_type jig0073 typeC)
		(size jig0073 n18)
		(empty-size jig0073 n09)
		(is_type jig0074 typeC)
		(size jig0074 n18)
		(empty-size jig0074 n09)
		(is_type jig0075 typeB)
		(size jig0075 n11)
		(empty-size jig0075 n08)
		(is_type jig0076 typeB)
		(size jig0076 n11)
		(empty-size jig0076 n08)
		(is_type jig0077 typeB)
		(size jig0077 n11)
		(empty-size jig0077 n08)
		(is_type jig0078 typeA)
		(size jig0078 n04)
		(empty-size jig0078 n04)
		(is_type jig0079 typeA)
		(size jig0079 n04)
		(empty-size jig0079 n04)
		(is_type jig0080 typeA)
		(size jig0080 n04)
		(empty-size jig0080 n04)
		(is_type jig0081 typeA)
		(size jig0081 n04)
		(empty-size jig0081 n04)
		(is_type jig0082 typeA)
		(size jig0082 n04)
		(empty-size jig0082 n04)
		(is_type jig0083 typeA)
		(size jig0083 n04)
		(empty-size jig0083 n04)
		(is_type jig0084 typeA)
		(size jig0084 n04)
		(empty-size jig0084 n04)
		(is_type jig0085 typeA)
		(size jig0085 n04)
		(empty-size jig0085 n04)
		(is_type jig0086 typeA)
		(size jig0086 n04)
		(empty-size jig0086 n04)
		(is_type jig0087 typeA)
		(size jig0087 n04)
		(empty-size jig0087 n04)
		(is_type jig0088 typeB)
		(size jig0088 n11)
		(empty-size jig0088 n08)
		(is_type jig0089 typeB)
		(size jig0089 n11)
		(empty-size jig0089 n08)
		(is_type jig0090 typeB)
		(size jig0090 n11)
		(empty-size jig0090 n08)
		(is_type jig0091 typeE)
		(size jig0091 n32)
		(empty-size jig0091 n32)
		(is_type jig0092 typeD)
		(size jig0092 n25)
		(empty-size jig0092 n18)
		(is_type jig0093 typeC)
		(size jig0093 n18)
		(empty-size jig0093 n09)
		(is_type jig0094 typeC)
		(size jig0094 n18)
		(empty-size jig0094 n09)
		(is_type jig0095 typeC)
		(size jig0095 n18)
		(empty-size jig0095 n09)
		(is_type jig0096 typeC)
		(size jig0096 n18)
		(empty-size jig0096 n09)
		(is_type jig0097 typeC)
		(size jig0097 n18)
		(empty-size jig0097 n09)
		(is_type jig0098 typeC)
		(size jig0098 n18)
		(empty-size jig0098 n09)
		(is_type jig0099 typeD)
		(size jig0099 n25)
		(empty-size jig0099 n18)
		(is_type jig0100 typeB)
		(size jig0100 n11)
		(empty-size jig0100 n08)
		(is_type jig0101 typeB)
		(size jig0101 n11)
		(empty-size jig0101 n08)
		(is_type jig0102 typeB)
		(size jig0102 n11)
		(empty-size jig0102 n08)
		(is_type jig0103 typeA)
		(size jig0103 n04)
		(empty-size jig0103 n04)
		(is_type jig0104 typeA)
		(size jig0104 n04)
		(empty-size jig0104 n04)
		(is_type jig0105 typeA)
		(size jig0105 n04)
		(empty-size jig0105 n04)
		(is_type jig0106 typeA)
		(size jig0106 n04)
		(empty-size jig0106 n04)
		(is_type jig0107 typeA)
		(size jig0107 n04)
		(empty-size jig0107 n04)
		(is_type jig0108 typeA)
		(size jig0108 n04)
		(empty-size jig0108 n04)
		(is_type jig0109 typeA)
		(size jig0109 n04)
		(empty-size jig0109 n04)
		(is_type jig0110 typeA)
		(size jig0110 n04)
		(empty-size jig0110 n04)
		(is_type jig0111 typeA)
		(size jig0111 n04)
		(empty-size jig0111 n04)
		(is_type jig0112 typeA)
		(size jig0112 n04)
		(empty-size jig0112 n04)
		(is_type jig0113 typeB)
		(size jig0113 n11)
		(empty-size jig0113 n08)
		(is_type jig0114 typeB)
		(size jig0114 n11)
		(empty-size jig0114 n08)
		(is_type jig0115 typeB)
		(size jig0115 n11)
		(empty-size jig0115 n08)
		(is_type jig0116 typeD)
		(size jig0116 n25)
		(empty-size jig0116 n18)
		(is_type jig0117 typeD)
		(size jig0117 n25)
		(empty-size jig0117 n18)
		(is_type jig0118 typeD)
		(size jig0118 n25)
		(empty-size jig0118 n18)
		(is_type jig0119 typeD)
		(size jig0119 n25)
		(empty-size jig0119 n18)
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
		(is_type jig0129 typeA)
		(size jig0129 n04)
		(empty-size jig0129 n04)
		(is_type jig0130 typeB)
		(size jig0130 n11)
		(empty-size jig0130 n08)
		(is_type jig0131 typeB)
		(size jig0131 n11)
		(empty-size jig0131 n08)
		(is_type jig0132 typeB)
		(size jig0132 n11)
		(empty-size jig0132 n08)
		(is_type jig0133 typeD)
		(size jig0133 n25)
		(empty-size jig0133 n18)
		(is_type jig0134 typeB)
		(size jig0134 n11)
		(empty-size jig0134 n08)
		(is_type jig0135 typeB)
		(size jig0135 n11)
		(empty-size jig0135 n08)
		(is_type jig0136 typeB)
		(size jig0136 n11)
		(empty-size jig0136 n08)
		(is_type jig0137 typeC)
		(size jig0137 n18)
		(empty-size jig0137 n09)
		(is_type jig0138 typeC)
		(size jig0138 n18)
		(empty-size jig0138 n09)
		(is_type jig0139 typeD)
		(size jig0139 n25)
		(empty-size jig0139 n18)
		(is_type jig0140 typeC)
		(size jig0140 n18)
		(empty-size jig0140 n09)
		(is_type jig0141 typeB)
		(size jig0141 n11)
		(empty-size jig0141 n08)
		(is_type jig0142 typeB)
		(size jig0142 n11)
		(empty-size jig0142 n08)
		(is_type jig0143 typeB)
		(size jig0143 n11)
		(empty-size jig0143 n08)
		(is_type jig0144 typeB)
		(size jig0144 n11)
		(empty-size jig0144 n08)
		(is_type jig0145 typeB)
		(size jig0145 n11)
		(empty-size jig0145 n08)
		(is_type jig0146 typeB)
		(size jig0146 n11)
		(empty-size jig0146 n08)
		(is_type jig0147 typeD)
		(size jig0147 n25)
		(empty-size jig0147 n18)
		(is_type jig0148 typeD)
		(size jig0148 n25)
		(empty-size jig0148 n18)
		(is_type jig0149 typeD)
		(size jig0149 n25)
		(empty-size jig0149 n18)
		(is_type jig0150 typeB)
		(size jig0150 n11)
		(empty-size jig0150 n08)
		(is_type jig0151 typeB)
		(size jig0151 n11)
		(empty-size jig0151 n08)
		(is_type jig0152 typeB)
		(size jig0152 n11)
		(empty-size jig0152 n08)
		(is_type jig0153 typeA)
		(size jig0153 n04)
		(empty-size jig0153 n04)
		(is_type jig0154 typeA)
		(size jig0154 n04)
		(empty-size jig0154 n04)
		(is_type jig0155 typeA)
		(size jig0155 n04)
		(empty-size jig0155 n04)
		(is_type jig0156 typeA)
		(size jig0156 n04)
		(empty-size jig0156 n04)
		(is_type jig0157 typeA)
		(size jig0157 n04)
		(empty-size jig0157 n04)
		(is_type jig0158 typeA)
		(size jig0158 n04)
		(empty-size jig0158 n04)
		(is_type jig0159 typeA)
		(size jig0159 n04)
		(empty-size jig0159 n04)
		(is_type jig0160 typeA)
		(size jig0160 n04)
		(empty-size jig0160 n04)
		(is_type jig0161 typeA)
		(size jig0161 n04)
		(empty-size jig0161 n04)
		(is_type jig0162 typeA)
		(size jig0162 n04)
		(empty-size jig0162 n04)
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
		(is_type jig0167 typeB)
		(size jig0167 n11)
		(empty-size jig0167 n08)
		(is_type jig0168 typeB)
		(size jig0168 n11)
		(empty-size jig0168 n08)
		(is_type jig0169 typeB)
		(size jig0169 n11)
		(empty-size jig0169 n08)
		(is_type jig0170 typeD)
		(size jig0170 n25)
		(empty-size jig0170 n18)
		(is_type jig0171 typeB)
		(size jig0171 n11)
		(empty-size jig0171 n08)
		(is_type jig0172 typeB)
		(size jig0172 n11)
		(empty-size jig0172 n08)
		(is_type jig0173 typeB)
		(size jig0173 n11)
		(empty-size jig0173 n08)
		(is_type jig0174 typeC)
		(size jig0174 n18)
		(empty-size jig0174 n09)
		(is_type jig0175 typeC)
		(size jig0175 n18)
		(empty-size jig0175 n09)
		(is_type jig0176 typeC)
		(size jig0176 n18)
		(empty-size jig0176 n09)
		(is_type jig0177 typeC)
		(size jig0177 n18)
		(empty-size jig0177 n09)
		(is_type jig0178 typeC)
		(size jig0178 n18)
		(empty-size jig0178 n09)
		(is_type jig0179 typeC)
		(size jig0179 n18)
		(empty-size jig0179 n09)
		(is_type jig0180 typeD)
		(size jig0180 n25)
		(empty-size jig0180 n18)
		(is_type jig0181 typeE)
		(size jig0181 n32)
		(empty-size jig0181 n32)
		(is_type jig0182 typeC)
		(size jig0182 n18)
		(empty-size jig0182 n09)
		(is_type jig0183 typeC)
		(size jig0183 n18)
		(empty-size jig0183 n09)
		(is_type jig0184 typeC)
		(size jig0184 n18)
		(empty-size jig0184 n09)
		(is_type jig0185 typeC)
		(size jig0185 n18)
		(empty-size jig0185 n09)
		(is_type jig0186 typeD)
		(size jig0186 n25)
		(empty-size jig0186 n18)
		(is_type jig0187 typeD)
		(size jig0187 n25)
		(empty-size jig0187 n18)
		(is_type jig0188 typeB)
		(size jig0188 n11)
		(empty-size jig0188 n08)
		(is_type jig0189 typeB)
		(size jig0189 n11)
		(empty-size jig0189 n08)
		(is_type jig0190 typeB)
		(size jig0190 n11)
		(empty-size jig0190 n08)
		(is_type jig0191 typeB)
		(size jig0191 n11)
		(empty-size jig0191 n08)
		(is_type jig0192 typeB)
		(size jig0192 n11)
		(empty-size jig0192 n08)
		(is_type jig0193 typeB)
		(size jig0193 n11)
		(empty-size jig0193 n08)
		(is_type jig0194 typeE)
		(size jig0194 n32)
		(empty-size jig0194 n32)
		(is_type jig0195 typeD)
		(size jig0195 n25)
		(empty-size jig0195 n18)
		(is_type jig0196 typeB)
		(size jig0196 n11)
		(empty-size jig0196 n08)
		(is_type jig0197 typeB)
		(size jig0197 n11)
		(empty-size jig0197 n08)
		(is_type jig0198 typeB)
		(size jig0198 n11)
		(empty-size jig0198 n08)
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
		(is_type jig0204 typeE)
		(size jig0204 n32)
		(empty-size jig0204 n32)
		(is_type jig0205 typeD)
		(size jig0205 n25)
		(empty-size jig0205 n18)
		(is_type jig0206 typeD)
		(size jig0206 n25)
		(empty-size jig0206 n18)
		(is_type jig0207 typeC)
		(size jig0207 n18)
		(empty-size jig0207 n09)
		(is_type jig0208 typeC)
		(size jig0208 n18)
		(empty-size jig0208 n09)
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
		(is_type jig0214 typeA)
		(size jig0214 n04)
		(empty-size jig0214 n04)
		(is_type jig0215 typeA)
		(size jig0215 n04)
		(empty-size jig0215 n04)
		(is_type jig0216 typeA)
		(size jig0216 n04)
		(empty-size jig0216 n04)
		(is_type jig0217 typeA)
		(size jig0217 n04)
		(empty-size jig0217 n04)
		(is_type jig0218 typeA)
		(size jig0218 n04)
		(empty-size jig0218 n04)
		(is_type jig0219 typeD)
		(size jig0219 n25)
		(empty-size jig0219 n18)
		(is_type jig0220 typeD)
		(size jig0220 n25)
		(empty-size jig0220 n18)
		(is_type jig0221 typeD)
		(size jig0221 n25)
		(empty-size jig0221 n18)
		(is_type jig0222 typeB)
		(size jig0222 n11)
		(empty-size jig0222 n08)
		(is_type jig0223 typeB)
		(size jig0223 n11)
		(empty-size jig0223 n08)
		(is_type jig0224 typeB)
		(size jig0224 n11)
		(empty-size jig0224 n08)
		(is_type jig0225 typeE)
		(size jig0225 n32)
		(empty-size jig0225 n32)
		(is_type jig0226 typeC)
		(size jig0226 n18)
		(empty-size jig0226 n09)
		(is_type jig0227 typeC)
		(size jig0227 n18)
		(empty-size jig0227 n09)
		(is_type jig0228 typeD)
		(size jig0228 n25)
		(empty-size jig0228 n18)
		(is_type jig0229 typeD)
		(size jig0229 n25)
		(empty-size jig0229 n18)
		(is_type jig0230 typeB)
		(size jig0230 n11)
		(empty-size jig0230 n08)
		(is_type jig0231 typeB)
		(size jig0231 n11)
		(empty-size jig0231 n08)
		(is_type jig0232 typeB)
		(size jig0232 n11)
		(empty-size jig0232 n08)
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
		(is_type jig0238 typeB)
		(size jig0238 n11)
		(empty-size jig0238 n08)
		(is_type jig0239 typeB)
		(size jig0239 n11)
		(empty-size jig0239 n08)
		(is_type jig0240 typeB)
		(size jig0240 n11)
		(empty-size jig0240 n08)
		(is_type jig0241 typeD)
		(size jig0241 n25)
		(empty-size jig0241 n18)
		(is_type jig0242 typeC)
		(size jig0242 n18)
		(empty-size jig0242 n09)
		(is_type jig0243 typeC)
		(size jig0243 n18)
		(empty-size jig0243 n09)
		(is_type jig0244 typeC)
		(size jig0244 n18)
		(empty-size jig0244 n09)
		(is_type jig0245 typeC)
		(size jig0245 n18)
		(empty-size jig0245 n09)
		(is_type jig0246 typeE)
		(size jig0246 n32)
		(empty-size jig0246 n32)
		(is_type jig0247 typeB)
		(size jig0247 n11)
		(empty-size jig0247 n08)
		(is_type jig0248 typeB)
		(size jig0248 n11)
		(empty-size jig0248 n08)
		(is_type jig0249 typeB)
		(size jig0249 n11)
		(empty-size jig0249 n08)
		(is_type jig0250 typeB)
		(size jig0250 n11)
		(empty-size jig0250 n08)
		(is_type jig0251 typeB)
		(size jig0251 n11)
		(empty-size jig0251 n08)
		(is_type jig0252 typeB)
		(size jig0252 n11)
		(empty-size jig0252 n08)
		(is_type jig0253 typeD)
		(size jig0253 n25)
		(empty-size jig0253 n18)
		(is_type jig0254 typeD)
		(size jig0254 n25)
		(empty-size jig0254 n18)
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
		(is_type jig0260 typeA)
		(size jig0260 n04)
		(empty-size jig0260 n04)
		(is_type jig0261 typeA)
		(size jig0261 n04)
		(empty-size jig0261 n04)
		(is_type jig0262 typeA)
		(size jig0262 n04)
		(empty-size jig0262 n04)
		(is_type jig0263 typeA)
		(size jig0263 n04)
		(empty-size jig0263 n04)
		(is_type jig0264 typeA)
		(size jig0264 n04)
		(empty-size jig0264 n04)
		(is_type jig0265 typeE)
		(size jig0265 n32)
		(empty-size jig0265 n32)
		(is_type jig0266 typeD)
		(size jig0266 n25)
		(empty-size jig0266 n18)
		(is_type jig0267 typeB)
		(size jig0267 n11)
		(empty-size jig0267 n08)
		(is_type jig0268 typeB)
		(size jig0268 n11)
		(empty-size jig0268 n08)
		(is_type jig0269 typeB)
		(size jig0269 n11)
		(empty-size jig0269 n08)
		(is_type jig0270 typeD)
		(size jig0270 n25)
		(empty-size jig0270 n18)
		(is_type jig0271 typeC)
		(size jig0271 n18)
		(empty-size jig0271 n09)
		(is_type jig0272 typeC)
		(size jig0272 n18)
		(empty-size jig0272 n09)
		(is_type jig0273 typeD)
		(size jig0273 n25)
		(empty-size jig0273 n18)
		(is_type jig0274 typeC)
		(size jig0274 n18)
		(empty-size jig0274 n09)
		(is_type jig0275 typeC)
		(size jig0275 n18)
		(empty-size jig0275 n09)
		(is_type jig0276 typeE)
		(size jig0276 n32)
		(empty-size jig0276 n32)
		(is_type jig0277 typeD)
		(size jig0277 n25)
		(empty-size jig0277 n18)
		(is_type jig0278 typeC)
		(size jig0278 n18)
		(empty-size jig0278 n09)
		(is_type jig0279 typeC)
		(size jig0279 n18)
		(empty-size jig0279 n09)
		(is_type jig0280 typeD)
		(size jig0280 n25)
		(empty-size jig0280 n18)
		(is_type jig0281 typeC)
		(size jig0281 n18)
		(empty-size jig0281 n09)
		(is_type jig0282 typeC)
		(size jig0282 n18)
		(empty-size jig0282 n09)
		(is_type jig0283 typeD)
		(size jig0283 n25)
		(empty-size jig0283 n18)
		(is_type jig0284 typeD)
		(size jig0284 n25)
		(empty-size jig0284 n18)
		(is_type jig0285 typeD)
		(size jig0285 n25)
		(empty-size jig0285 n18)
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
		(is_type jig0294 typeA)
		(size jig0294 n04)
		(empty-size jig0294 n04)
		(is_type jig0295 typeA)
		(size jig0295 n04)
		(empty-size jig0295 n04)
		(is_type jig0296 typeC)
		(size jig0296 n18)
		(empty-size jig0296 n09)
		(is_type jig0297 typeC)
		(size jig0297 n18)
		(empty-size jig0297 n09)
		(is_type jig0298 typeD)
		(size jig0298 n25)
		(empty-size jig0298 n18)
		(is_type jig0299 typeE)
		(size jig0299 n32)
		(empty-size jig0299 n32)
		(is_type jig0300 typeC)
		(size jig0300 n18)
		(empty-size jig0300 n09)
		(is_type jig0301 typeC)
		(size jig0301 n18)
		(empty-size jig0301 n09)
		(is_type jig0302 typeE)
		(size jig0302 n32)
		(empty-size jig0302 n32)
		(is_type jig0303 typeA)
		(size jig0303 n04)
		(empty-size jig0303 n04)
		(is_type jig0304 typeA)
		(size jig0304 n04)
		(empty-size jig0304 n04)
		(is_type jig0305 typeA)
		(size jig0305 n04)
		(empty-size jig0305 n04)
		(is_type jig0306 typeA)
		(size jig0306 n04)
		(empty-size jig0306 n04)
		(is_type jig0307 typeA)
		(size jig0307 n04)
		(empty-size jig0307 n04)
		(is_type jig0308 typeA)
		(size jig0308 n04)
		(empty-size jig0308 n04)
		(is_type jig0309 typeA)
		(size jig0309 n04)
		(empty-size jig0309 n04)
		(is_type jig0310 typeA)
		(size jig0310 n04)
		(empty-size jig0310 n04)
		(is_type jig0311 typeA)
		(size jig0311 n04)
		(empty-size jig0311 n04)
		(is_type jig0312 typeA)
		(size jig0312 n04)
		(empty-size jig0312 n04)
		(is_type jig0313 typeD)
		(size jig0313 n25)
		(empty-size jig0313 n18)
		(is_type jig0314 typeE)
		(size jig0314 n32)
		(empty-size jig0314 n32)
		(is_type jig0315 typeB)
		(size jig0315 n11)
		(empty-size jig0315 n08)
		(is_type jig0316 typeB)
		(size jig0316 n11)
		(empty-size jig0316 n08)
		(is_type jig0317 typeB)
		(size jig0317 n11)
		(empty-size jig0317 n08)
		(is_type jig0318 typeC)
		(size jig0318 n18)
		(empty-size jig0318 n09)
		(is_type jig0319 typeC)
		(size jig0319 n18)
		(empty-size jig0319 n09)
		(is_type jig0320 typeC)
		(size jig0320 n18)
		(empty-size jig0320 n09)
		(is_type jig0321 typeC)
		(size jig0321 n18)
		(empty-size jig0321 n09)
		(is_type jig0322 typeA)
		(size jig0322 n04)
		(empty-size jig0322 n04)
		(is_type jig0323 typeA)
		(size jig0323 n04)
		(empty-size jig0323 n04)
		(is_type jig0324 typeA)
		(size jig0324 n04)
		(empty-size jig0324 n04)
		(is_type jig0325 typeA)
		(size jig0325 n04)
		(empty-size jig0325 n04)
		(is_type jig0326 typeA)
		(size jig0326 n04)
		(empty-size jig0326 n04)
		(is_type jig0327 typeA)
		(size jig0327 n04)
		(empty-size jig0327 n04)
		(is_type jig0328 typeA)
		(size jig0328 n04)
		(empty-size jig0328 n04)
		(is_type jig0329 typeA)
		(size jig0329 n04)
		(empty-size jig0329 n04)
		(is_type jig0330 typeA)
		(size jig0330 n04)
		(empty-size jig0330 n04)
		(is_type jig0331 typeA)
		(size jig0331 n04)
		(empty-size jig0331 n04)
		(is_type jig0332 typeC)
		(size jig0332 n18)
		(empty-size jig0332 n09)
		(is_type jig0333 typeC)
		(size jig0333 n18)
		(empty-size jig0333 n09)
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
		(is_type jig0339 typeA)
		(size jig0339 n04)
		(empty-size jig0339 n04)
		(is_type jig0340 typeA)
		(size jig0340 n04)
		(empty-size jig0340 n04)
		(is_type jig0341 typeA)
		(size jig0341 n04)
		(empty-size jig0341 n04)
		(is_type jig0342 typeA)
		(size jig0342 n04)
		(empty-size jig0342 n04)
		(is_type jig0343 typeA)
		(size jig0343 n04)
		(empty-size jig0343 n04)
		(is_type jig0344 typeD)
		(size jig0344 n25)
		(empty-size jig0344 n18)
		(is_type jig0345 typeE)
		(size jig0345 n32)
		(empty-size jig0345 n32)
		(is_type jig0346 typeD)
		(size jig0346 n25)
		(empty-size jig0346 n18)
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
		(next-flight-to-process beluga192 beluga193)
		(next-flight-to-process beluga193 beluga194)
		(next-flight-to-process beluga194 beluga195)
		(next-flight-to-process beluga195 beluga196)
		(next-flight-to-process beluga196 beluga197)
		(next-flight-to-process beluga197 beluga198)
		(next-flight-to-process beluga198 beluga199)
		; Number of flights: 199
		; Incoming jigs unload order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; 0: jig0008
		(to_unload jig0008 beluga1)
		(in jig0008 beluga1)
		(next_unload jig0008 dummy-jig)
		; To Process Flights
		; Flight: beluga2
		; 0: jig0009
		(to_unload jig0009 beluga2)
		(in jig0009 beluga2)
		(next_unload jig0009 dummy-jig)
		; Flight: beluga3
		; 0: jig0010
		(to_unload jig0010 beluga3)
		(in jig0010 beluga3)
		(next_unload jig0010 dummy-jig)
		; Flight: beluga4
		; 0: jig0011
		(to_unload jig0011 beluga4)
		(in jig0011 beluga4)
		(next_unload jig0011 dummy-jig)
		; Flight: beluga5
		; 0: jig0012
		(to_unload jig0012 beluga5)
		(in jig0012 beluga5)
		(next_unload jig0012 dummy-jig)
		; Flight: beluga6
		; 0: jig0013 1: jig0014
		(to_unload jig0013 beluga6)
		(in jig0013 beluga6)
		(next_unload jig0013 jig0014)
		(in jig0014 beluga6)
		(next_unload jig0014 dummy-jig)
		; Flight: beluga7
		; 0: jig0015 1: jig0016 2: jig0017 3: jig0018 4: jig0019 5: jig0020 6: jig0021 7: jig0022 8: jig0023 9: jig0024
		(to_unload jig0015 beluga7)
		(in jig0015 beluga7)
		(next_unload jig0015 jig0016)
		(in jig0016 beluga7)
		(next_unload jig0016 jig0017)
		(in jig0017 beluga7)
		(next_unload jig0017 jig0018)
		(in jig0018 beluga7)
		(next_unload jig0018 jig0019)
		(in jig0019 beluga7)
		(next_unload jig0019 jig0020)
		(in jig0020 beluga7)
		(next_unload jig0020 jig0021)
		(in jig0021 beluga7)
		(next_unload jig0021 jig0022)
		(in jig0022 beluga7)
		(next_unload jig0022 jig0023)
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
		; 0: jig0026
		(to_unload jig0026 beluga9)
		(in jig0026 beluga9)
		(next_unload jig0026 dummy-jig)
		; Flight: beluga10
		; 0: jig0027 1: jig0028 2: jig0029 3: jig0030 4: jig0031 5: jig0032 6: jig0033 7: jig0034 8: jig0035 9: jig0036
		(to_unload jig0027 beluga10)
		(in jig0027 beluga10)
		(next_unload jig0027 jig0028)
		(in jig0028 beluga10)
		(next_unload jig0028 jig0029)
		(in jig0029 beluga10)
		(next_unload jig0029 jig0030)
		(in jig0030 beluga10)
		(next_unload jig0030 jig0031)
		(in jig0031 beluga10)
		(next_unload jig0031 jig0032)
		(in jig0032 beluga10)
		(next_unload jig0032 jig0033)
		(in jig0033 beluga10)
		(next_unload jig0033 jig0034)
		(in jig0034 beluga10)
		(next_unload jig0034 jig0035)
		(in jig0035 beluga10)
		(next_unload jig0035 jig0036)
		(in jig0036 beluga10)
		(next_unload jig0036 dummy-jig)
		; Flight: beluga11
		; 0: jig0037
		(to_unload jig0037 beluga11)
		(in jig0037 beluga11)
		(next_unload jig0037 dummy-jig)
		; Flight: beluga12
		; 0: jig0038 1: jig0039
		(to_unload jig0038 beluga12)
		(in jig0038 beluga12)
		(next_unload jig0038 jig0039)
		(in jig0039 beluga12)
		(next_unload jig0039 dummy-jig)
		; Flight: beluga13
		; 0: jig0040
		(to_unload jig0040 beluga13)
		(in jig0040 beluga13)
		(next_unload jig0040 dummy-jig)
		; Flight: beluga14
		; 0: jig0041
		(to_unload jig0041 beluga14)
		(in jig0041 beluga14)
		(next_unload jig0041 dummy-jig)
		; Flight: beluga15
		; 0: jig0042 1: jig0043 2: jig0044
		(to_unload jig0042 beluga15)
		(in jig0042 beluga15)
		(next_unload jig0042 jig0043)
		(in jig0043 beluga15)
		(next_unload jig0043 jig0044)
		(in jig0044 beluga15)
		(next_unload jig0044 dummy-jig)
		; Flight: beluga16
		; No jigs
		(to_unload dummy-jig beluga16)
		; Flight: beluga17
		; 0: jig0045
		(to_unload jig0045 beluga17)
		(in jig0045 beluga17)
		(next_unload jig0045 dummy-jig)
		; Flight: beluga18
		; 0: jig0046
		(to_unload jig0046 beluga18)
		(in jig0046 beluga18)
		(next_unload jig0046 dummy-jig)
		; Flight: beluga19
		; 0: jig0047
		(to_unload jig0047 beluga19)
		(in jig0047 beluga19)
		(next_unload jig0047 dummy-jig)
		; Flight: beluga20
		; No jigs
		(to_unload dummy-jig beluga20)
		; Flight: beluga21
		; 0: jig0048 1: jig0049
		(to_unload jig0048 beluga21)
		(in jig0048 beluga21)
		(next_unload jig0048 jig0049)
		(in jig0049 beluga21)
		(next_unload jig0049 dummy-jig)
		; Flight: beluga22
		; 0: jig0050
		(to_unload jig0050 beluga22)
		(in jig0050 beluga22)
		(next_unload jig0050 dummy-jig)
		; Flight: beluga23
		; 0: jig0051 1: jig0052
		(to_unload jig0051 beluga23)
		(in jig0051 beluga23)
		(next_unload jig0051 jig0052)
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
		; 0: jig0055
		(to_unload jig0055 beluga27)
		(in jig0055 beluga27)
		(next_unload jig0055 dummy-jig)
		; Flight: beluga28
		; No jigs
		(to_unload dummy-jig beluga28)
		; Flight: beluga29
		; No jigs
		(to_unload dummy-jig beluga29)
		; Flight: beluga30
		; No jigs
		(to_unload dummy-jig beluga30)
		; Flight: beluga31
		; 0: jig0056 1: jig0057 2: jig0058 3: jig0059 4: jig0060 5: jig0061 6: jig0062 7: jig0063 8: jig0064 9: jig0065
		(to_unload jig0056 beluga31)
		(in jig0056 beluga31)
		(next_unload jig0056 jig0057)
		(in jig0057 beluga31)
		(next_unload jig0057 jig0058)
		(in jig0058 beluga31)
		(next_unload jig0058 jig0059)
		(in jig0059 beluga31)
		(next_unload jig0059 jig0060)
		(in jig0060 beluga31)
		(next_unload jig0060 jig0061)
		(in jig0061 beluga31)
		(next_unload jig0061 jig0062)
		(in jig0062 beluga31)
		(next_unload jig0062 jig0063)
		(in jig0063 beluga31)
		(next_unload jig0063 jig0064)
		(in jig0064 beluga31)
		(next_unload jig0064 jig0065)
		(in jig0065 beluga31)
		(next_unload jig0065 dummy-jig)
		; Flight: beluga32
		; 0: jig0066 1: jig0067 2: jig0068
		(to_unload jig0066 beluga32)
		(in jig0066 beluga32)
		(next_unload jig0066 jig0067)
		(in jig0067 beluga32)
		(next_unload jig0067 jig0068)
		(in jig0068 beluga32)
		(next_unload jig0068 dummy-jig)
		; Flight: beluga33
		; 0: jig0069
		(to_unload jig0069 beluga33)
		(in jig0069 beluga33)
		(next_unload jig0069 dummy-jig)
		; Flight: beluga34
		; 0: jig0070
		(to_unload jig0070 beluga34)
		(in jig0070 beluga34)
		(next_unload jig0070 dummy-jig)
		; Flight: beluga35
		; No jigs
		(to_unload dummy-jig beluga35)
		; Flight: beluga36
		; 0: jig0071 1: jig0072
		(to_unload jig0071 beluga36)
		(in jig0071 beluga36)
		(next_unload jig0071 jig0072)
		(in jig0072 beluga36)
		(next_unload jig0072 dummy-jig)
		; Flight: beluga37
		; 0: jig0073 1: jig0074
		(to_unload jig0073 beluga37)
		(in jig0073 beluga37)
		(next_unload jig0073 jig0074)
		(in jig0074 beluga37)
		(next_unload jig0074 dummy-jig)
		; Flight: beluga38
		; 0: jig0075 1: jig0076 2: jig0077
		(to_unload jig0075 beluga38)
		(in jig0075 beluga38)
		(next_unload jig0075 jig0076)
		(in jig0076 beluga38)
		(next_unload jig0076 jig0077)
		(in jig0077 beluga38)
		(next_unload jig0077 dummy-jig)
		; Flight: beluga39
		; 0: jig0078 1: jig0079 2: jig0080 3: jig0081 4: jig0082 5: jig0083 6: jig0084 7: jig0085 8: jig0086 9: jig0087
		(to_unload jig0078 beluga39)
		(in jig0078 beluga39)
		(next_unload jig0078 jig0079)
		(in jig0079 beluga39)
		(next_unload jig0079 jig0080)
		(in jig0080 beluga39)
		(next_unload jig0080 jig0081)
		(in jig0081 beluga39)
		(next_unload jig0081 jig0082)
		(in jig0082 beluga39)
		(next_unload jig0082 jig0083)
		(in jig0083 beluga39)
		(next_unload jig0083 jig0084)
		(in jig0084 beluga39)
		(next_unload jig0084 jig0085)
		(in jig0085 beluga39)
		(next_unload jig0085 jig0086)
		(in jig0086 beluga39)
		(next_unload jig0086 jig0087)
		(in jig0087 beluga39)
		(next_unload jig0087 dummy-jig)
		; Flight: beluga40
		; 0: jig0088 1: jig0089 2: jig0090
		(to_unload jig0088 beluga40)
		(in jig0088 beluga40)
		(next_unload jig0088 jig0089)
		(in jig0089 beluga40)
		(next_unload jig0089 jig0090)
		(in jig0090 beluga40)
		(next_unload jig0090 dummy-jig)
		; Flight: beluga41
		; 0: jig0091
		(to_unload jig0091 beluga41)
		(in jig0091 beluga41)
		(next_unload jig0091 dummy-jig)
		; Flight: beluga42
		; 0: jig0092
		(to_unload jig0092 beluga42)
		(in jig0092 beluga42)
		(next_unload jig0092 dummy-jig)
		; Flight: beluga43
		; No jigs
		(to_unload dummy-jig beluga43)
		; Flight: beluga44
		; No jigs
		(to_unload dummy-jig beluga44)
		; Flight: beluga45
		; 0: jig0093 1: jig0094
		(to_unload jig0093 beluga45)
		(in jig0093 beluga45)
		(next_unload jig0093 jig0094)
		(in jig0094 beluga45)
		(next_unload jig0094 dummy-jig)
		; Flight: beluga46
		; 0: jig0095 1: jig0096
		(to_unload jig0095 beluga46)
		(in jig0095 beluga46)
		(next_unload jig0095 jig0096)
		(in jig0096 beluga46)
		(next_unload jig0096 dummy-jig)
		; Flight: beluga47
		; 0: jig0097 1: jig0098
		(to_unload jig0097 beluga47)
		(in jig0097 beluga47)
		(next_unload jig0097 jig0098)
		(in jig0098 beluga47)
		(next_unload jig0098 dummy-jig)
		; Flight: beluga48
		; 0: jig0099
		(to_unload jig0099 beluga48)
		(in jig0099 beluga48)
		(next_unload jig0099 dummy-jig)
		; Flight: beluga49
		; 0: jig0100 1: jig0101
		(to_unload jig0100 beluga49)
		(in jig0100 beluga49)
		(next_unload jig0100 jig0101)
		(in jig0101 beluga49)
		(next_unload jig0101 dummy-jig)
		; Flight: beluga50
		; 0: jig0102
		(to_unload jig0102 beluga50)
		(in jig0102 beluga50)
		(next_unload jig0102 dummy-jig)
		; Flight: beluga51
		; 0: jig0103 1: jig0104 2: jig0105 3: jig0106 4: jig0107 5: jig0108 6: jig0109 7: jig0110 8: jig0111 9: jig0112
		(to_unload jig0103 beluga51)
		(in jig0103 beluga51)
		(next_unload jig0103 jig0104)
		(in jig0104 beluga51)
		(next_unload jig0104 jig0105)
		(in jig0105 beluga51)
		(next_unload jig0105 jig0106)
		(in jig0106 beluga51)
		(next_unload jig0106 jig0107)
		(in jig0107 beluga51)
		(next_unload jig0107 jig0108)
		(in jig0108 beluga51)
		(next_unload jig0108 jig0109)
		(in jig0109 beluga51)
		(next_unload jig0109 jig0110)
		(in jig0110 beluga51)
		(next_unload jig0110 jig0111)
		(in jig0111 beluga51)
		(next_unload jig0111 jig0112)
		(in jig0112 beluga51)
		(next_unload jig0112 dummy-jig)
		; Flight: beluga52
		; No jigs
		(to_unload dummy-jig beluga52)
		; Flight: beluga53
		; No jigs
		(to_unload dummy-jig beluga53)
		; Flight: beluga54
		; 0: jig0113 1: jig0114 2: jig0115
		(to_unload jig0113 beluga54)
		(in jig0113 beluga54)
		(next_unload jig0113 jig0114)
		(in jig0114 beluga54)
		(next_unload jig0114 jig0115)
		(in jig0115 beluga54)
		(next_unload jig0115 dummy-jig)
		; Flight: beluga55
		; 0: jig0116
		(to_unload jig0116 beluga55)
		(in jig0116 beluga55)
		(next_unload jig0116 dummy-jig)
		; Flight: beluga56
		; No jigs
		(to_unload dummy-jig beluga56)
		; Flight: beluga57
		; No jigs
		(to_unload dummy-jig beluga57)
		; Flight: beluga58
		; 0: jig0117
		(to_unload jig0117 beluga58)
		(in jig0117 beluga58)
		(next_unload jig0117 dummy-jig)
		; Flight: beluga59
		; 0: jig0118
		(to_unload jig0118 beluga59)
		(in jig0118 beluga59)
		(next_unload jig0118 dummy-jig)
		; Flight: beluga60
		; 0: jig0119
		(to_unload jig0119 beluga60)
		(in jig0119 beluga60)
		(next_unload jig0119 dummy-jig)
		; Flight: beluga61
		; 0: jig0120 1: jig0121 2: jig0122 3: jig0123 4: jig0124 5: jig0125 6: jig0126 7: jig0127 8: jig0128 9: jig0129
		(to_unload jig0120 beluga61)
		(in jig0120 beluga61)
		(next_unload jig0120 jig0121)
		(in jig0121 beluga61)
		(next_unload jig0121 jig0122)
		(in jig0122 beluga61)
		(next_unload jig0122 jig0123)
		(in jig0123 beluga61)
		(next_unload jig0123 jig0124)
		(in jig0124 beluga61)
		(next_unload jig0124 jig0125)
		(in jig0125 beluga61)
		(next_unload jig0125 jig0126)
		(in jig0126 beluga61)
		(next_unload jig0126 jig0127)
		(in jig0127 beluga61)
		(next_unload jig0127 jig0128)
		(in jig0128 beluga61)
		(next_unload jig0128 jig0129)
		(in jig0129 beluga61)
		(next_unload jig0129 dummy-jig)
		; Flight: beluga62
		; No jigs
		(to_unload dummy-jig beluga62)
		; Flight: beluga63
		; 0: jig0130 1: jig0131 2: jig0132
		(to_unload jig0130 beluga63)
		(in jig0130 beluga63)
		(next_unload jig0130 jig0131)
		(in jig0131 beluga63)
		(next_unload jig0131 jig0132)
		(in jig0132 beluga63)
		(next_unload jig0132 dummy-jig)
		; Flight: beluga64
		; 0: jig0133
		(to_unload jig0133 beluga64)
		(in jig0133 beluga64)
		(next_unload jig0133 dummy-jig)
		; Flight: beluga65
		; 0: jig0134 1: jig0135 2: jig0136
		(to_unload jig0134 beluga65)
		(in jig0134 beluga65)
		(next_unload jig0134 jig0135)
		(in jig0135 beluga65)
		(next_unload jig0135 jig0136)
		(in jig0136 beluga65)
		(next_unload jig0136 dummy-jig)
		; Flight: beluga66
		; 0: jig0137 1: jig0138
		(to_unload jig0137 beluga66)
		(in jig0137 beluga66)
		(next_unload jig0137 jig0138)
		(in jig0138 beluga66)
		(next_unload jig0138 dummy-jig)
		; Flight: beluga67
		; 0: jig0139
		(to_unload jig0139 beluga67)
		(in jig0139 beluga67)
		(next_unload jig0139 dummy-jig)
		; Flight: beluga68
		; 0: jig0140
		(to_unload jig0140 beluga68)
		(in jig0140 beluga68)
		(next_unload jig0140 dummy-jig)
		; Flight: beluga69
		; No jigs
		(to_unload dummy-jig beluga69)
		; Flight: beluga70
		; 0: jig0141 1: jig0142 2: jig0143
		(to_unload jig0141 beluga70)
		(in jig0141 beluga70)
		(next_unload jig0141 jig0142)
		(in jig0142 beluga70)
		(next_unload jig0142 jig0143)
		(in jig0143 beluga70)
		(next_unload jig0143 dummy-jig)
		; Flight: beluga71
		; 0: jig0144 1: jig0145 2: jig0146
		(to_unload jig0144 beluga71)
		(in jig0144 beluga71)
		(next_unload jig0144 jig0145)
		(in jig0145 beluga71)
		(next_unload jig0145 jig0146)
		(in jig0146 beluga71)
		(next_unload jig0146 dummy-jig)
		; Flight: beluga72
		; 0: jig0147
		(to_unload jig0147 beluga72)
		(in jig0147 beluga72)
		(next_unload jig0147 dummy-jig)
		; Flight: beluga73
		; No jigs
		(to_unload dummy-jig beluga73)
		; Flight: beluga74
		; 0: jig0148
		(to_unload jig0148 beluga74)
		(in jig0148 beluga74)
		(next_unload jig0148 dummy-jig)
		; Flight: beluga75
		; No jigs
		(to_unload dummy-jig beluga75)
		; Flight: beluga76
		; 0: jig0149
		(to_unload jig0149 beluga76)
		(in jig0149 beluga76)
		(next_unload jig0149 dummy-jig)
		; Flight: beluga77
		; No jigs
		(to_unload dummy-jig beluga77)
		; Flight: beluga78
		; 0: jig0150 1: jig0151 2: jig0152
		(to_unload jig0150 beluga78)
		(in jig0150 beluga78)
		(next_unload jig0150 jig0151)
		(in jig0151 beluga78)
		(next_unload jig0151 jig0152)
		(in jig0152 beluga78)
		(next_unload jig0152 dummy-jig)
		; Flight: beluga79
		; No jigs
		(to_unload dummy-jig beluga79)
		; Flight: beluga80
		; 0: jig0153 1: jig0154 2: jig0155 3: jig0156 4: jig0157 5: jig0158 6: jig0159 7: jig0160 8: jig0161 9: jig0162
		(to_unload jig0153 beluga80)
		(in jig0153 beluga80)
		(next_unload jig0153 jig0154)
		(in jig0154 beluga80)
		(next_unload jig0154 jig0155)
		(in jig0155 beluga80)
		(next_unload jig0155 jig0156)
		(in jig0156 beluga80)
		(next_unload jig0156 jig0157)
		(in jig0157 beluga80)
		(next_unload jig0157 jig0158)
		(in jig0158 beluga80)
		(next_unload jig0158 jig0159)
		(in jig0159 beluga80)
		(next_unload jig0159 jig0160)
		(in jig0160 beluga80)
		(next_unload jig0160 jig0161)
		(in jig0161 beluga80)
		(next_unload jig0161 jig0162)
		(in jig0162 beluga80)
		(next_unload jig0162 dummy-jig)
		; Flight: beluga81
		; 0: jig0163
		(to_unload jig0163 beluga81)
		(in jig0163 beluga81)
		(next_unload jig0163 dummy-jig)
		; Flight: beluga82
		; 0: jig0164 1: jig0165
		(to_unload jig0164 beluga82)
		(in jig0164 beluga82)
		(next_unload jig0164 jig0165)
		(in jig0165 beluga82)
		(next_unload jig0165 dummy-jig)
		; Flight: beluga83
		; 0: jig0166
		(to_unload jig0166 beluga83)
		(in jig0166 beluga83)
		(next_unload jig0166 dummy-jig)
		; Flight: beluga84
		; 0: jig0167 1: jig0168 2: jig0169
		(to_unload jig0167 beluga84)
		(in jig0167 beluga84)
		(next_unload jig0167 jig0168)
		(in jig0168 beluga84)
		(next_unload jig0168 jig0169)
		(in jig0169 beluga84)
		(next_unload jig0169 dummy-jig)
		; Flight: beluga85
		; No jigs
		(to_unload dummy-jig beluga85)
		; Flight: beluga86
		; No jigs
		(to_unload dummy-jig beluga86)
		; Flight: beluga87
		; 0: jig0170
		(to_unload jig0170 beluga87)
		(in jig0170 beluga87)
		(next_unload jig0170 dummy-jig)
		; Flight: beluga88
		; No jigs
		(to_unload dummy-jig beluga88)
		; Flight: beluga89
		; No jigs
		(to_unload dummy-jig beluga89)
		; Flight: beluga90
		; 0: jig0171 1: jig0172 2: jig0173
		(to_unload jig0171 beluga90)
		(in jig0171 beluga90)
		(next_unload jig0171 jig0172)
		(in jig0172 beluga90)
		(next_unload jig0172 jig0173)
		(in jig0173 beluga90)
		(next_unload jig0173 dummy-jig)
		; Flight: beluga91
		; 0: jig0174 1: jig0175
		(to_unload jig0174 beluga91)
		(in jig0174 beluga91)
		(next_unload jig0174 jig0175)
		(in jig0175 beluga91)
		(next_unload jig0175 dummy-jig)
		; Flight: beluga92
		; 0: jig0176 1: jig0177
		(to_unload jig0176 beluga92)
		(in jig0176 beluga92)
		(next_unload jig0176 jig0177)
		(in jig0177 beluga92)
		(next_unload jig0177 dummy-jig)
		; Flight: beluga93
		; 0: jig0178 1: jig0179
		(to_unload jig0178 beluga93)
		(in jig0178 beluga93)
		(next_unload jig0178 jig0179)
		(in jig0179 beluga93)
		(next_unload jig0179 dummy-jig)
		; Flight: beluga94
		; 0: jig0180
		(to_unload jig0180 beluga94)
		(in jig0180 beluga94)
		(next_unload jig0180 dummy-jig)
		; Flight: beluga95
		; 0: jig0181
		(to_unload jig0181 beluga95)
		(in jig0181 beluga95)
		(next_unload jig0181 dummy-jig)
		; Flight: beluga96
		; No jigs
		(to_unload dummy-jig beluga96)
		; Flight: beluga97
		; No jigs
		(to_unload dummy-jig beluga97)
		; Flight: beluga98
		; No jigs
		(to_unload dummy-jig beluga98)
		; Flight: beluga99
		; 0: jig0182 1: jig0183
		(to_unload jig0182 beluga99)
		(in jig0182 beluga99)
		(next_unload jig0182 jig0183)
		(in jig0183 beluga99)
		(next_unload jig0183 dummy-jig)
		; Flight: beluga100
		; 0: jig0184 1: jig0185
		(to_unload jig0184 beluga100)
		(in jig0184 beluga100)
		(next_unload jig0184 jig0185)
		(in jig0185 beluga100)
		(next_unload jig0185 dummy-jig)
		; Flight: beluga101
		; 0: jig0186
		(to_unload jig0186 beluga101)
		(in jig0186 beluga101)
		(next_unload jig0186 dummy-jig)
		; Flight: beluga102
		; 0: jig0187
		(to_unload jig0187 beluga102)
		(in jig0187 beluga102)
		(next_unload jig0187 dummy-jig)
		; Flight: beluga103
		; 0: jig0188 1: jig0189 2: jig0190
		(to_unload jig0188 beluga103)
		(in jig0188 beluga103)
		(next_unload jig0188 jig0189)
		(in jig0189 beluga103)
		(next_unload jig0189 jig0190)
		(in jig0190 beluga103)
		(next_unload jig0190 dummy-jig)
		; Flight: beluga104
		; 0: jig0191 1: jig0192 2: jig0193
		(to_unload jig0191 beluga104)
		(in jig0191 beluga104)
		(next_unload jig0191 jig0192)
		(in jig0192 beluga104)
		(next_unload jig0192 jig0193)
		(in jig0193 beluga104)
		(next_unload jig0193 dummy-jig)
		; Flight: beluga105
		; 0: jig0194
		(to_unload jig0194 beluga105)
		(in jig0194 beluga105)
		(next_unload jig0194 dummy-jig)
		; Flight: beluga106
		; No jigs
		(to_unload dummy-jig beluga106)
		; Flight: beluga107
		; 0: jig0195
		(to_unload jig0195 beluga107)
		(in jig0195 beluga107)
		(next_unload jig0195 dummy-jig)
		; Flight: beluga108
		; No jigs
		(to_unload dummy-jig beluga108)
		; Flight: beluga109
		; 0: jig0196 1: jig0197 2: jig0198
		(to_unload jig0196 beluga109)
		(in jig0196 beluga109)
		(next_unload jig0196 jig0197)
		(in jig0197 beluga109)
		(next_unload jig0197 jig0198)
		(in jig0198 beluga109)
		(next_unload jig0198 dummy-jig)
		; Flight: beluga110
		; No jigs
		(to_unload dummy-jig beluga110)
		; Flight: beluga111
		; No jigs
		(to_unload dummy-jig beluga111)
		; Flight: beluga112
		; 0: jig0199 1: jig0200 2: jig0201
		(to_unload jig0199 beluga112)
		(in jig0199 beluga112)
		(next_unload jig0199 jig0200)
		(in jig0200 beluga112)
		(next_unload jig0200 jig0201)
		(in jig0201 beluga112)
		(next_unload jig0201 dummy-jig)
		; Flight: beluga113
		; 0: jig0202 1: jig0203
		(to_unload jig0202 beluga113)
		(in jig0202 beluga113)
		(next_unload jig0202 jig0203)
		(in jig0203 beluga113)
		(next_unload jig0203 dummy-jig)
		; Flight: beluga114
		; 0: jig0204
		(to_unload jig0204 beluga114)
		(in jig0204 beluga114)
		(next_unload jig0204 dummy-jig)
		; Flight: beluga115
		; 0: jig0205
		(to_unload jig0205 beluga115)
		(in jig0205 beluga115)
		(next_unload jig0205 dummy-jig)
		; Flight: beluga116
		; No jigs
		(to_unload dummy-jig beluga116)
		; Flight: beluga117
		; 0: jig0206
		(to_unload jig0206 beluga117)
		(in jig0206 beluga117)
		(next_unload jig0206 dummy-jig)
		; Flight: beluga118
		; 0: jig0207 1: jig0208
		(to_unload jig0207 beluga118)
		(in jig0207 beluga118)
		(next_unload jig0207 jig0208)
		(in jig0208 beluga118)
		(next_unload jig0208 dummy-jig)
		; Flight: beluga119
		; 0: jig0209 1: jig0210 2: jig0211 3: jig0212 4: jig0213 5: jig0214 6: jig0215 7: jig0216 8: jig0217 9: jig0218
		(to_unload jig0209 beluga119)
		(in jig0209 beluga119)
		(next_unload jig0209 jig0210)
		(in jig0210 beluga119)
		(next_unload jig0210 jig0211)
		(in jig0211 beluga119)
		(next_unload jig0211 jig0212)
		(in jig0212 beluga119)
		(next_unload jig0212 jig0213)
		(in jig0213 beluga119)
		(next_unload jig0213 jig0214)
		(in jig0214 beluga119)
		(next_unload jig0214 jig0215)
		(in jig0215 beluga119)
		(next_unload jig0215 jig0216)
		(in jig0216 beluga119)
		(next_unload jig0216 jig0217)
		(in jig0217 beluga119)
		(next_unload jig0217 jig0218)
		(in jig0218 beluga119)
		(next_unload jig0218 dummy-jig)
		; Flight: beluga120
		; 0: jig0219
		(to_unload jig0219 beluga120)
		(in jig0219 beluga120)
		(next_unload jig0219 dummy-jig)
		; Flight: beluga121
		; 0: jig0220
		(to_unload jig0220 beluga121)
		(in jig0220 beluga121)
		(next_unload jig0220 dummy-jig)
		; Flight: beluga122
		; No jigs
		(to_unload dummy-jig beluga122)
		; Flight: beluga123
		; 0: jig0221
		(to_unload jig0221 beluga123)
		(in jig0221 beluga123)
		(next_unload jig0221 dummy-jig)
		; Flight: beluga124
		; No jigs
		(to_unload dummy-jig beluga124)
		; Flight: beluga125
		; No jigs
		(to_unload dummy-jig beluga125)
		; Flight: beluga126
		; 0: jig0222 1: jig0223 2: jig0224
		(to_unload jig0222 beluga126)
		(in jig0222 beluga126)
		(next_unload jig0222 jig0223)
		(in jig0223 beluga126)
		(next_unload jig0223 jig0224)
		(in jig0224 beluga126)
		(next_unload jig0224 dummy-jig)
		; Flight: beluga127
		; 0: jig0225
		(to_unload jig0225 beluga127)
		(in jig0225 beluga127)
		(next_unload jig0225 dummy-jig)
		; Flight: beluga128
		; 0: jig0226 1: jig0227
		(to_unload jig0226 beluga128)
		(in jig0226 beluga128)
		(next_unload jig0226 jig0227)
		(in jig0227 beluga128)
		(next_unload jig0227 dummy-jig)
		; Flight: beluga129
		; 0: jig0228
		(to_unload jig0228 beluga129)
		(in jig0228 beluga129)
		(next_unload jig0228 dummy-jig)
		; Flight: beluga130
		; No jigs
		(to_unload dummy-jig beluga130)
		; Flight: beluga131
		; No jigs
		(to_unload dummy-jig beluga131)
		; Flight: beluga132
		; 0: jig0229
		(to_unload jig0229 beluga132)
		(in jig0229 beluga132)
		(next_unload jig0229 dummy-jig)
		; Flight: beluga133
		; No jigs
		(to_unload dummy-jig beluga133)
		; Flight: beluga134
		; 0: jig0230 1: jig0231 2: jig0232
		(to_unload jig0230 beluga134)
		(in jig0230 beluga134)
		(next_unload jig0230 jig0231)
		(in jig0231 beluga134)
		(next_unload jig0231 jig0232)
		(in jig0232 beluga134)
		(next_unload jig0232 dummy-jig)
		; Flight: beluga135
		; 0: jig0233
		(to_unload jig0233 beluga135)
		(in jig0233 beluga135)
		(next_unload jig0233 dummy-jig)
		; Flight: beluga136
		; 0: jig0234 1: jig0235 2: jig0236
		(to_unload jig0234 beluga136)
		(in jig0234 beluga136)
		(next_unload jig0234 jig0235)
		(in jig0235 beluga136)
		(next_unload jig0235 jig0236)
		(in jig0236 beluga136)
		(next_unload jig0236 dummy-jig)
		; Flight: beluga137
		; 0: jig0237
		(to_unload jig0237 beluga137)
		(in jig0237 beluga137)
		(next_unload jig0237 dummy-jig)
		; Flight: beluga138
		; 0: jig0238 1: jig0239 2: jig0240
		(to_unload jig0238 beluga138)
		(in jig0238 beluga138)
		(next_unload jig0238 jig0239)
		(in jig0239 beluga138)
		(next_unload jig0239 jig0240)
		(in jig0240 beluga138)
		(next_unload jig0240 dummy-jig)
		; Flight: beluga139
		; No jigs
		(to_unload dummy-jig beluga139)
		; Flight: beluga140
		; 0: jig0241
		(to_unload jig0241 beluga140)
		(in jig0241 beluga140)
		(next_unload jig0241 dummy-jig)
		; Flight: beluga141
		; 0: jig0242 1: jig0243
		(to_unload jig0242 beluga141)
		(in jig0242 beluga141)
		(next_unload jig0242 jig0243)
		(in jig0243 beluga141)
		(next_unload jig0243 dummy-jig)
		; Flight: beluga142
		; No jigs
		(to_unload dummy-jig beluga142)
		; Flight: beluga143
		; 0: jig0244 1: jig0245
		(to_unload jig0244 beluga143)
		(in jig0244 beluga143)
		(next_unload jig0244 jig0245)
		(in jig0245 beluga143)
		(next_unload jig0245 dummy-jig)
		; Flight: beluga144
		; No jigs
		(to_unload dummy-jig beluga144)
		; Flight: beluga145
		; No jigs
		(to_unload dummy-jig beluga145)
		; Flight: beluga146
		; No jigs
		(to_unload dummy-jig beluga146)
		; Flight: beluga147
		; 0: jig0246
		(to_unload jig0246 beluga147)
		(in jig0246 beluga147)
		(next_unload jig0246 dummy-jig)
		; Flight: beluga148
		; 0: jig0247 1: jig0248 2: jig0249
		(to_unload jig0247 beluga148)
		(in jig0247 beluga148)
		(next_unload jig0247 jig0248)
		(in jig0248 beluga148)
		(next_unload jig0248 jig0249)
		(in jig0249 beluga148)
		(next_unload jig0249 dummy-jig)
		; Flight: beluga149
		; 0: jig0250 1: jig0251 2: jig0252
		(to_unload jig0250 beluga149)
		(in jig0250 beluga149)
		(next_unload jig0250 jig0251)
		(in jig0251 beluga149)
		(next_unload jig0251 jig0252)
		(in jig0252 beluga149)
		(next_unload jig0252 dummy-jig)
		; Flight: beluga150
		; No jigs
		(to_unload dummy-jig beluga150)
		; Flight: beluga151
		; 0: jig0253
		(to_unload jig0253 beluga151)
		(in jig0253 beluga151)
		(next_unload jig0253 dummy-jig)
		; Flight: beluga152
		; No jigs
		(to_unload dummy-jig beluga152)
		; Flight: beluga153
		; 0: jig0254
		(to_unload jig0254 beluga153)
		(in jig0254 beluga153)
		(next_unload jig0254 dummy-jig)
		; Flight: beluga154
		; 0: jig0255 1: jig0256 2: jig0257 3: jig0258 4: jig0259 5: jig0260 6: jig0261 7: jig0262 8: jig0263 9: jig0264
		(to_unload jig0255 beluga154)
		(in jig0255 beluga154)
		(next_unload jig0255 jig0256)
		(in jig0256 beluga154)
		(next_unload jig0256 jig0257)
		(in jig0257 beluga154)
		(next_unload jig0257 jig0258)
		(in jig0258 beluga154)
		(next_unload jig0258 jig0259)
		(in jig0259 beluga154)
		(next_unload jig0259 jig0260)
		(in jig0260 beluga154)
		(next_unload jig0260 jig0261)
		(in jig0261 beluga154)
		(next_unload jig0261 jig0262)
		(in jig0262 beluga154)
		(next_unload jig0262 jig0263)
		(in jig0263 beluga154)
		(next_unload jig0263 jig0264)
		(in jig0264 beluga154)
		(next_unload jig0264 dummy-jig)
		; Flight: beluga155
		; 0: jig0265
		(to_unload jig0265 beluga155)
		(in jig0265 beluga155)
		(next_unload jig0265 dummy-jig)
		; Flight: beluga156
		; No jigs
		(to_unload dummy-jig beluga156)
		; Flight: beluga157
		; 0: jig0266
		(to_unload jig0266 beluga157)
		(in jig0266 beluga157)
		(next_unload jig0266 dummy-jig)
		; Flight: beluga158
		; 0: jig0267 1: jig0268 2: jig0269
		(to_unload jig0267 beluga158)
		(in jig0267 beluga158)
		(next_unload jig0267 jig0268)
		(in jig0268 beluga158)
		(next_unload jig0268 jig0269)
		(in jig0269 beluga158)
		(next_unload jig0269 dummy-jig)
		; Flight: beluga159
		; No jigs
		(to_unload dummy-jig beluga159)
		; Flight: beluga160
		; 0: jig0270
		(to_unload jig0270 beluga160)
		(in jig0270 beluga160)
		(next_unload jig0270 dummy-jig)
		; Flight: beluga161
		; No jigs
		(to_unload dummy-jig beluga161)
		; Flight: beluga162
		; No jigs
		(to_unload dummy-jig beluga162)
		; Flight: beluga163
		; 0: jig0271 1: jig0272
		(to_unload jig0271 beluga163)
		(in jig0271 beluga163)
		(next_unload jig0271 jig0272)
		(in jig0272 beluga163)
		(next_unload jig0272 dummy-jig)
		; Flight: beluga164
		; 0: jig0273
		(to_unload jig0273 beluga164)
		(in jig0273 beluga164)
		(next_unload jig0273 dummy-jig)
		; Flight: beluga165
		; 0: jig0274 1: jig0275
		(to_unload jig0274 beluga165)
		(in jig0274 beluga165)
		(next_unload jig0274 jig0275)
		(in jig0275 beluga165)
		(next_unload jig0275 dummy-jig)
		; Flight: beluga166
		; 0: jig0276
		(to_unload jig0276 beluga166)
		(in jig0276 beluga166)
		(next_unload jig0276 dummy-jig)
		; Flight: beluga167
		; 0: jig0277
		(to_unload jig0277 beluga167)
		(in jig0277 beluga167)
		(next_unload jig0277 dummy-jig)
		; Flight: beluga168
		; No jigs
		(to_unload dummy-jig beluga168)
		; Flight: beluga169
		; 0: jig0278 1: jig0279
		(to_unload jig0278 beluga169)
		(in jig0278 beluga169)
		(next_unload jig0278 jig0279)
		(in jig0279 beluga169)
		(next_unload jig0279 dummy-jig)
		; Flight: beluga170
		; 0: jig0280
		(to_unload jig0280 beluga170)
		(in jig0280 beluga170)
		(next_unload jig0280 dummy-jig)
		; Flight: beluga171
		; 0: jig0281 1: jig0282
		(to_unload jig0281 beluga171)
		(in jig0281 beluga171)
		(next_unload jig0281 jig0282)
		(in jig0282 beluga171)
		(next_unload jig0282 dummy-jig)
		; Flight: beluga172
		; 0: jig0283
		(to_unload jig0283 beluga172)
		(in jig0283 beluga172)
		(next_unload jig0283 dummy-jig)
		; Flight: beluga173
		; 0: jig0284
		(to_unload jig0284 beluga173)
		(in jig0284 beluga173)
		(next_unload jig0284 dummy-jig)
		; Flight: beluga174
		; 0: jig0285
		(to_unload jig0285 beluga174)
		(in jig0285 beluga174)
		(next_unload jig0285 dummy-jig)
		; Flight: beluga175
		; No jigs
		(to_unload dummy-jig beluga175)
		; Flight: beluga176
		; 0: jig0286 1: jig0287 2: jig0288 3: jig0289 4: jig0290 5: jig0291 6: jig0292 7: jig0293 8: jig0294 9: jig0295
		(to_unload jig0286 beluga176)
		(in jig0286 beluga176)
		(next_unload jig0286 jig0287)
		(in jig0287 beluga176)
		(next_unload jig0287 jig0288)
		(in jig0288 beluga176)
		(next_unload jig0288 jig0289)
		(in jig0289 beluga176)
		(next_unload jig0289 jig0290)
		(in jig0290 beluga176)
		(next_unload jig0290 jig0291)
		(in jig0291 beluga176)
		(next_unload jig0291 jig0292)
		(in jig0292 beluga176)
		(next_unload jig0292 jig0293)
		(in jig0293 beluga176)
		(next_unload jig0293 jig0294)
		(in jig0294 beluga176)
		(next_unload jig0294 jig0295)
		(in jig0295 beluga176)
		(next_unload jig0295 dummy-jig)
		; Flight: beluga177
		; No jigs
		(to_unload dummy-jig beluga177)
		; Flight: beluga178
		; 0: jig0296 1: jig0297
		(to_unload jig0296 beluga178)
		(in jig0296 beluga178)
		(next_unload jig0296 jig0297)
		(in jig0297 beluga178)
		(next_unload jig0297 dummy-jig)
		; Flight: beluga179
		; 0: jig0298
		(to_unload jig0298 beluga179)
		(in jig0298 beluga179)
		(next_unload jig0298 dummy-jig)
		; Flight: beluga180
		; 0: jig0299
		(to_unload jig0299 beluga180)
		(in jig0299 beluga180)
		(next_unload jig0299 dummy-jig)
		; Flight: beluga181
		; No jigs
		(to_unload dummy-jig beluga181)
		; Flight: beluga182
		; 0: jig0300 1: jig0301
		(to_unload jig0300 beluga182)
		(in jig0300 beluga182)
		(next_unload jig0300 jig0301)
		(in jig0301 beluga182)
		(next_unload jig0301 dummy-jig)
		; Flight: beluga183
		; 0: jig0302
		(to_unload jig0302 beluga183)
		(in jig0302 beluga183)
		(next_unload jig0302 dummy-jig)
		; Flight: beluga184
		; No jigs
		(to_unload dummy-jig beluga184)
		; Flight: beluga185
		; 0: jig0303 1: jig0304 2: jig0305 3: jig0306 4: jig0307 5: jig0308 6: jig0309 7: jig0310 8: jig0311 9: jig0312
		(to_unload jig0303 beluga185)
		(in jig0303 beluga185)
		(next_unload jig0303 jig0304)
		(in jig0304 beluga185)
		(next_unload jig0304 jig0305)
		(in jig0305 beluga185)
		(next_unload jig0305 jig0306)
		(in jig0306 beluga185)
		(next_unload jig0306 jig0307)
		(in jig0307 beluga185)
		(next_unload jig0307 jig0308)
		(in jig0308 beluga185)
		(next_unload jig0308 jig0309)
		(in jig0309 beluga185)
		(next_unload jig0309 jig0310)
		(in jig0310 beluga185)
		(next_unload jig0310 jig0311)
		(in jig0311 beluga185)
		(next_unload jig0311 jig0312)
		(in jig0312 beluga185)
		(next_unload jig0312 dummy-jig)
		; Flight: beluga186
		; 0: jig0313
		(to_unload jig0313 beluga186)
		(in jig0313 beluga186)
		(next_unload jig0313 dummy-jig)
		; Flight: beluga187
		; 0: jig0314
		(to_unload jig0314 beluga187)
		(in jig0314 beluga187)
		(next_unload jig0314 dummy-jig)
		; Flight: beluga188
		; No jigs
		(to_unload dummy-jig beluga188)
		; Flight: beluga189
		; 0: jig0315 1: jig0316 2: jig0317
		(to_unload jig0315 beluga189)
		(in jig0315 beluga189)
		(next_unload jig0315 jig0316)
		(in jig0316 beluga189)
		(next_unload jig0316 jig0317)
		(in jig0317 beluga189)
		(next_unload jig0317 dummy-jig)
		; Flight: beluga190
		; 0: jig0318 1: jig0319
		(to_unload jig0318 beluga190)
		(in jig0318 beluga190)
		(next_unload jig0318 jig0319)
		(in jig0319 beluga190)
		(next_unload jig0319 dummy-jig)
		; Flight: beluga191
		; 0: jig0320 1: jig0321
		(to_unload jig0320 beluga191)
		(in jig0320 beluga191)
		(next_unload jig0320 jig0321)
		(in jig0321 beluga191)
		(next_unload jig0321 dummy-jig)
		; Flight: beluga192
		; 0: jig0322 1: jig0323 2: jig0324 3: jig0325 4: jig0326 5: jig0327 6: jig0328 7: jig0329 8: jig0330 9: jig0331
		(to_unload jig0322 beluga192)
		(in jig0322 beluga192)
		(next_unload jig0322 jig0323)
		(in jig0323 beluga192)
		(next_unload jig0323 jig0324)
		(in jig0324 beluga192)
		(next_unload jig0324 jig0325)
		(in jig0325 beluga192)
		(next_unload jig0325 jig0326)
		(in jig0326 beluga192)
		(next_unload jig0326 jig0327)
		(in jig0327 beluga192)
		(next_unload jig0327 jig0328)
		(in jig0328 beluga192)
		(next_unload jig0328 jig0329)
		(in jig0329 beluga192)
		(next_unload jig0329 jig0330)
		(in jig0330 beluga192)
		(next_unload jig0330 jig0331)
		(in jig0331 beluga192)
		(next_unload jig0331 dummy-jig)
		; Flight: beluga193
		; 0: jig0332 1: jig0333
		(to_unload jig0332 beluga193)
		(in jig0332 beluga193)
		(next_unload jig0332 jig0333)
		(in jig0333 beluga193)
		(next_unload jig0333 dummy-jig)
		; Flight: beluga194
		; 0: jig0334 1: jig0335 2: jig0336 3: jig0337 4: jig0338 5: jig0339 6: jig0340 7: jig0341 8: jig0342 9: jig0343
		(to_unload jig0334 beluga194)
		(in jig0334 beluga194)
		(next_unload jig0334 jig0335)
		(in jig0335 beluga194)
		(next_unload jig0335 jig0336)
		(in jig0336 beluga194)
		(next_unload jig0336 jig0337)
		(in jig0337 beluga194)
		(next_unload jig0337 jig0338)
		(in jig0338 beluga194)
		(next_unload jig0338 jig0339)
		(in jig0339 beluga194)
		(next_unload jig0339 jig0340)
		(in jig0340 beluga194)
		(next_unload jig0340 jig0341)
		(in jig0341 beluga194)
		(next_unload jig0341 jig0342)
		(in jig0342 beluga194)
		(next_unload jig0342 jig0343)
		(in jig0343 beluga194)
		(next_unload jig0343 dummy-jig)
		; Flight: beluga195
		; 0: jig0344
		(to_unload jig0344 beluga195)
		(in jig0344 beluga195)
		(next_unload jig0344 dummy-jig)
		; Flight: beluga196
		; No jigs
		(to_unload dummy-jig beluga196)
		; Flight: beluga197
		; 0: jig0345
		(to_unload jig0345 beluga197)
		(in jig0345 beluga197)
		(next_unload jig0345 dummy-jig)
		; Flight: beluga198
		; No jigs
		(to_unload dummy-jig beluga198)
		; Flight: beluga199
		; 0: jig0346
		(to_unload jig0346 beluga199)
		(in jig0346 beluga199)
		(next_unload jig0346 dummy-jig)
		; Outgoing jigs load order:
		; Finished Flights
		; No already completely finished Flights
		; Current Flight: beluga1
		; (0: typeE)
		(to_load typeE slot0 beluga1)
		(next_load dummy-type slot0 dummy-slot beluga1)
		; To Process Flights
		; 0: typeE
		(to_load typeE slot0 beluga2)
		(next_load dummy-type slot0 dummy-slot beluga2)
		; No jigs
		(to_load dummy-type dummy-slot beluga3)
		; No jigs
		(to_load dummy-type dummy-slot beluga4)
		; No jigs
		(to_load dummy-type dummy-slot beluga5)
		; 0: typeE
		(to_load typeE slot0 beluga6)
		(next_load dummy-type slot0 dummy-slot beluga6)
		; 0: typeE
		(to_load typeE slot0 beluga7)
		(next_load dummy-type slot0 dummy-slot beluga7)
		; 0: typeD
		(to_load typeD slot0 beluga8)
		(next_load dummy-type slot0 dummy-slot beluga8)
		; 0: typeE
		(to_load typeE slot0 beluga9)
		(next_load dummy-type slot0 dummy-slot beluga9)
		; 0: typeD
		(to_load typeD slot0 beluga10)
		(next_load dummy-type slot0 dummy-slot beluga10)
		; 0: typeB
		(to_load typeB slot0 beluga11)
		(next_load dummy-type slot0 dummy-slot beluga11)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga12)
		(next_load typeA slot0 slot1 beluga12)
		(next_load typeA slot1 slot2 beluga12)
		(next_load typeA slot2 slot3 beluga12)
		(next_load dummy-type slot3 dummy-slot beluga12)
		; 0: typeA
		(to_load typeA slot0 beluga13)
		(next_load dummy-type slot0 dummy-slot beluga13)
		; 0: typeA
		(to_load typeA slot0 beluga14)
		(next_load dummy-type slot0 dummy-slot beluga14)
		; 0: typeA
		(to_load typeA slot0 beluga15)
		(next_load dummy-type slot0 dummy-slot beluga15)
		; 0: typeD
		(to_load typeD slot0 beluga16)
		(next_load dummy-type slot0 dummy-slot beluga16)
		; 0: typeB
		(to_load typeB slot0 beluga17)
		(next_load dummy-type slot0 dummy-slot beluga17)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga18)
		(next_load typeA slot0 slot1 beluga18)
		(next_load dummy-type slot1 dummy-slot beluga18)
		; 0: typeD
		(to_load typeD slot0 beluga19)
		(next_load dummy-type slot0 dummy-slot beluga19)
		; 0: typeA
		(to_load typeA slot0 beluga20)
		(next_load dummy-type slot0 dummy-slot beluga20)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga21)
		(next_load typeC slot0 slot1 beluga21)
		(next_load dummy-type slot1 dummy-slot beluga21)
		; 0: typeD
		(to_load typeD slot0 beluga22)
		(next_load dummy-type slot0 dummy-slot beluga22)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga23)
		(next_load typeA slot0 slot1 beluga23)
		(next_load typeA slot1 slot2 beluga23)
		(next_load dummy-type slot2 dummy-slot beluga23)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga24)
		(next_load typeC slot0 slot1 beluga24)
		(next_load dummy-type slot1 dummy-slot beluga24)
		; 0: typeD
		(to_load typeD slot0 beluga25)
		(next_load dummy-type slot0 dummy-slot beluga25)
		; 0: typeB
		(to_load typeB slot0 beluga26)
		(next_load dummy-type slot0 dummy-slot beluga26)
		; 0: typeC
		(to_load typeC slot0 beluga27)
		(next_load dummy-type slot0 dummy-slot beluga27)
		; 0: typeD
		(to_load typeD slot0 beluga28)
		(next_load dummy-type slot0 dummy-slot beluga28)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA
		(to_load typeA slot0 beluga29)
		(next_load typeA slot0 slot1 beluga29)
		(next_load typeA slot1 slot2 beluga29)
		(next_load typeA slot2 slot3 beluga29)
		(next_load typeA slot3 slot4 beluga29)
		(next_load typeA slot4 slot5 beluga29)
		(next_load dummy-type slot5 dummy-slot beluga29)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga30)
		(next_load typeC slot0 slot1 beluga30)
		(next_load dummy-type slot1 dummy-slot beluga30)
		; 0: typeB
		(to_load typeB slot0 beluga31)
		(next_load dummy-type slot0 dummy-slot beluga31)
		; 0: typeA
		(to_load typeA slot0 beluga32)
		(next_load dummy-type slot0 dummy-slot beluga32)
		; 0: typeD
		(to_load typeD slot0 beluga33)
		(next_load dummy-type slot0 dummy-slot beluga33)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga34)
		(next_load typeA slot0 slot1 beluga34)
		(next_load dummy-type slot1 dummy-slot beluga34)
		; 0: typeC
		(to_load typeC slot0 beluga35)
		(next_load dummy-type slot0 dummy-slot beluga35)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga36)
		(next_load typeD slot0 slot1 beluga36)
		(next_load dummy-type slot1 dummy-slot beluga36)
		; 0: typeA
		(to_load typeA slot0 beluga37)
		(next_load dummy-type slot0 dummy-slot beluga37)
		; 0: typeD
		(to_load typeD slot0 beluga38)
		(next_load dummy-type slot0 dummy-slot beluga38)
		; 0: typeB
		(to_load typeB slot0 beluga39)
		(next_load dummy-type slot0 dummy-slot beluga39)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga40)
		(next_load typeA slot0 slot1 beluga40)
		(next_load typeA slot1 slot2 beluga40)
		(next_load typeA slot2 slot3 beluga40)
		(next_load dummy-type slot3 dummy-slot beluga40)
		; 0: typeB
		(to_load typeB slot0 beluga41)
		(next_load dummy-type slot0 dummy-slot beluga41)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga42)
		(next_load typeA slot0 slot1 beluga42)
		(next_load typeA slot1 slot2 beluga42)
		(next_load dummy-type slot2 dummy-slot beluga42)
		; 0: typeB
		(to_load typeB slot0 beluga43)
		(next_load dummy-type slot0 dummy-slot beluga43)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga44)
		(next_load typeC slot0 slot1 beluga44)
		(next_load typeC slot1 slot2 beluga44)
		(next_load dummy-type slot2 dummy-slot beluga44)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga45)
		(next_load typeA slot0 slot1 beluga45)
		(next_load dummy-type slot1 dummy-slot beluga45)
		; 0: typeE
		(to_load typeE slot0 beluga46)
		(next_load dummy-type slot0 dummy-slot beluga46)
		; 0: typeA
		(to_load typeA slot0 beluga47)
		(next_load dummy-type slot0 dummy-slot beluga47)
		; 0: typeB
		(to_load typeB slot0 beluga48)
		(next_load dummy-type slot0 dummy-slot beluga48)
		; 0: typeC
		(to_load typeC slot0 beluga49)
		(next_load dummy-type slot0 dummy-slot beluga49)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga50)
		(next_load typeB slot0 slot1 beluga50)
		(next_load dummy-type slot1 dummy-slot beluga50)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga51)
		(next_load typeC slot0 slot1 beluga51)
		(next_load dummy-type slot1 dummy-slot beluga51)
		; 0: typeB
		(to_load typeB slot0 beluga52)
		(next_load dummy-type slot0 dummy-slot beluga52)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga53)
		(next_load typeB slot0 slot1 beluga53)
		(next_load typeB slot1 slot2 beluga53)
		(next_load dummy-type slot2 dummy-slot beluga53)
		; 0: typeC
		(to_load typeC slot0 beluga54)
		(next_load dummy-type slot0 dummy-slot beluga54)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA
		(to_load typeA slot0 beluga55)
		(next_load typeA slot0 slot1 beluga55)
		(next_load typeA slot1 slot2 beluga55)
		(next_load typeA slot2 slot3 beluga55)
		(next_load typeA slot3 slot4 beluga55)
		(next_load typeA slot4 slot5 beluga55)
		(next_load dummy-type slot5 dummy-slot beluga55)
		; 0: typeD
		(to_load typeD slot0 beluga56)
		(next_load dummy-type slot0 dummy-slot beluga56)
		; 0: typeB
		(to_load typeB slot0 beluga57)
		(next_load dummy-type slot0 dummy-slot beluga57)
		; 0: typeB
		(to_load typeB slot0 beluga58)
		(next_load dummy-type slot0 dummy-slot beluga58)
		; 0: typeD
		(to_load typeD slot0 beluga59)
		(next_load dummy-type slot0 dummy-slot beluga59)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga60)
		(next_load typeC slot0 slot1 beluga60)
		(next_load dummy-type slot1 dummy-slot beluga60)
		; 0: typeB
		(to_load typeB slot0 beluga61)
		(next_load dummy-type slot0 dummy-slot beluga61)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA 7: typeA
		(to_load typeA slot0 beluga62)
		(next_load typeA slot0 slot1 beluga62)
		(next_load typeA slot1 slot2 beluga62)
		(next_load typeA slot2 slot3 beluga62)
		(next_load typeA slot3 slot4 beluga62)
		(next_load typeA slot4 slot5 beluga62)
		(next_load typeA slot5 slot6 beluga62)
		(next_load typeA slot6 slot7 beluga62)
		(next_load dummy-type slot7 dummy-slot beluga62)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga63)
		(next_load typeC slot0 slot1 beluga63)
		(next_load dummy-type slot1 dummy-slot beluga63)
		; 0: typeA
		(to_load typeA slot0 beluga64)
		(next_load dummy-type slot0 dummy-slot beluga64)
		; 0: typeD
		(to_load typeD slot0 beluga65)
		(next_load dummy-type slot0 dummy-slot beluga65)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga66)
		(next_load typeA slot0 slot1 beluga66)
		(next_load dummy-type slot1 dummy-slot beluga66)
		; 0: typeC
		(to_load typeC slot0 beluga67)
		(next_load dummy-type slot0 dummy-slot beluga67)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga68)
		(next_load typeA slot0 slot1 beluga68)
		(next_load typeA slot1 slot2 beluga68)
		(next_load dummy-type slot2 dummy-slot beluga68)
		; 0: typeD
		(to_load typeD slot0 beluga69)
		(next_load dummy-type slot0 dummy-slot beluga69)
		; 0: typeC
		(to_load typeC slot0 beluga70)
		(next_load dummy-type slot0 dummy-slot beluga70)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga71)
		(next_load typeB slot0 slot1 beluga71)
		(next_load typeB slot1 slot2 beluga71)
		(next_load dummy-type slot2 dummy-slot beluga71)
		; 0: typeB
		(to_load typeB slot0 beluga72)
		(next_load dummy-type slot0 dummy-slot beluga72)
		; 0: typeD
		(to_load typeD slot0 beluga73)
		(next_load dummy-type slot0 dummy-slot beluga73)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga74)
		(next_load typeA slot0 slot1 beluga74)
		(next_load dummy-type slot1 dummy-slot beluga74)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga75)
		(next_load typeB slot0 slot1 beluga75)
		(next_load dummy-type slot1 dummy-slot beluga75)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga76)
		(next_load typeD slot0 slot1 beluga76)
		(next_load dummy-type slot1 dummy-slot beluga76)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga77)
		(next_load typeB slot0 slot1 beluga77)
		(next_load dummy-type slot1 dummy-slot beluga77)
		; 0: typeA 1: typeA 2: typeA 3: typeA
		(to_load typeA slot0 beluga78)
		(next_load typeA slot0 slot1 beluga78)
		(next_load typeA slot1 slot2 beluga78)
		(next_load typeA slot2 slot3 beluga78)
		(next_load dummy-type slot3 dummy-slot beluga78)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga79)
		(next_load typeB slot0 slot1 beluga79)
		(next_load dummy-type slot1 dummy-slot beluga79)
		; 0: typeA
		(to_load typeA slot0 beluga80)
		(next_load dummy-type slot0 dummy-slot beluga80)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga81)
		(next_load typeD slot0 slot1 beluga81)
		(next_load dummy-type slot1 dummy-slot beluga81)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga82)
		(next_load typeB slot0 slot1 beluga82)
		(next_load dummy-type slot1 dummy-slot beluga82)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga83)
		(next_load typeA slot0 slot1 beluga83)
		(next_load typeA slot1 slot2 beluga83)
		(next_load dummy-type slot2 dummy-slot beluga83)
		; 0: typeC
		(to_load typeC slot0 beluga84)
		(next_load dummy-type slot0 dummy-slot beluga84)
		; 0: typeD
		(to_load typeD slot0 beluga85)
		(next_load dummy-type slot0 dummy-slot beluga85)
		; 0: typeE
		(to_load typeE slot0 beluga86)
		(next_load dummy-type slot0 dummy-slot beluga86)
		; 0: typeE
		(to_load typeE slot0 beluga87)
		(next_load dummy-type slot0 dummy-slot beluga87)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga88)
		(next_load typeA slot0 slot1 beluga88)
		(next_load dummy-type slot1 dummy-slot beluga88)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga89)
		(next_load typeC slot0 slot1 beluga89)
		(next_load typeC slot1 slot2 beluga89)
		(next_load dummy-type slot2 dummy-slot beluga89)
		; 0: typeB
		(to_load typeB slot0 beluga90)
		(next_load dummy-type slot0 dummy-slot beluga90)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga91)
		(next_load typeD slot0 slot1 beluga91)
		(next_load dummy-type slot1 dummy-slot beluga91)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga92)
		(next_load typeB slot0 slot1 beluga92)
		(next_load typeB slot1 slot2 beluga92)
		(next_load typeB slot2 slot3 beluga92)
		(next_load dummy-type slot3 dummy-slot beluga92)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga93)
		(next_load typeB slot0 slot1 beluga93)
		(next_load dummy-type slot1 dummy-slot beluga93)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga94)
		(next_load typeC slot0 slot1 beluga94)
		(next_load typeC slot1 slot2 beluga94)
		(next_load dummy-type slot2 dummy-slot beluga94)
		; 0: typeB
		(to_load typeB slot0 beluga95)
		(next_load dummy-type slot0 dummy-slot beluga95)
		; 0: typeA
		(to_load typeA slot0 beluga96)
		(next_load dummy-type slot0 dummy-slot beluga96)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga97)
		(next_load typeC slot0 slot1 beluga97)
		(next_load dummy-type slot1 dummy-slot beluga97)
		; 0: typeD
		(to_load typeD slot0 beluga98)
		(next_load dummy-type slot0 dummy-slot beluga98)
		; 0: typeD
		(to_load typeD slot0 beluga99)
		(next_load dummy-type slot0 dummy-slot beluga99)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga100)
		(next_load typeA slot0 slot1 beluga100)
		(next_load dummy-type slot1 dummy-slot beluga100)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga101)
		(next_load typeA slot0 slot1 beluga101)
		(next_load dummy-type slot1 dummy-slot beluga101)
		; 0: typeB
		(to_load typeB slot0 beluga102)
		(next_load dummy-type slot0 dummy-slot beluga102)
		; 0: typeD
		(to_load typeD slot0 beluga103)
		(next_load dummy-type slot0 dummy-slot beluga103)
		; 0: typeC
		(to_load typeC slot0 beluga104)
		(next_load dummy-type slot0 dummy-slot beluga104)
		; 0: typeB
		(to_load typeB slot0 beluga105)
		(next_load dummy-type slot0 dummy-slot beluga105)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga106)
		(next_load typeD slot0 slot1 beluga106)
		(next_load dummy-type slot1 dummy-slot beluga106)
		; 0: typeB
		(to_load typeB slot0 beluga107)
		(next_load dummy-type slot0 dummy-slot beluga107)
		; 0: typeB
		(to_load typeB slot0 beluga108)
		(next_load dummy-type slot0 dummy-slot beluga108)
		; 0: typeB
		(to_load typeB slot0 beluga109)
		(next_load dummy-type slot0 dummy-slot beluga109)
		; 0: typeA
		(to_load typeA slot0 beluga110)
		(next_load dummy-type slot0 dummy-slot beluga110)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga111)
		(next_load typeD slot0 slot1 beluga111)
		(next_load dummy-type slot1 dummy-slot beluga111)
		; 0: typeB
		(to_load typeB slot0 beluga112)
		(next_load dummy-type slot0 dummy-slot beluga112)
		; 0: typeC
		(to_load typeC slot0 beluga113)
		(next_load dummy-type slot0 dummy-slot beluga113)
		; 0: typeC
		(to_load typeC slot0 beluga114)
		(next_load dummy-type slot0 dummy-slot beluga114)
		; 0: typeE
		(to_load typeE slot0 beluga115)
		(next_load dummy-type slot0 dummy-slot beluga115)
		; 0: typeE
		(to_load typeE slot0 beluga116)
		(next_load dummy-type slot0 dummy-slot beluga116)
		; 0: typeC
		(to_load typeC slot0 beluga117)
		(next_load dummy-type slot0 dummy-slot beluga117)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga118)
		(next_load typeB slot0 slot1 beluga118)
		(next_load typeB slot1 slot2 beluga118)
		(next_load typeB slot2 slot3 beluga118)
		(next_load dummy-type slot3 dummy-slot beluga118)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga119)
		(next_load typeB slot0 slot1 beluga119)
		(next_load dummy-type slot1 dummy-slot beluga119)
		; 0: typeC
		(to_load typeC slot0 beluga120)
		(next_load dummy-type slot0 dummy-slot beluga120)
		; 0: typeC
		(to_load typeC slot0 beluga121)
		(next_load dummy-type slot0 dummy-slot beluga121)
		; 0: typeB
		(to_load typeB slot0 beluga122)
		(next_load dummy-type slot0 dummy-slot beluga122)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga123)
		(next_load typeA slot0 slot1 beluga123)
		(next_load dummy-type slot1 dummy-slot beluga123)
		; 0: typeB
		(to_load typeB slot0 beluga124)
		(next_load dummy-type slot0 dummy-slot beluga124)
		; 0: typeD
		(to_load typeD slot0 beluga125)
		(next_load dummy-type slot0 dummy-slot beluga125)
		; 0: typeA
		(to_load typeA slot0 beluga126)
		(next_load dummy-type slot0 dummy-slot beluga126)
		; 0: typeD
		(to_load typeD slot0 beluga127)
		(next_load dummy-type slot0 dummy-slot beluga127)
		; 0: typeA
		(to_load typeA slot0 beluga128)
		(next_load dummy-type slot0 dummy-slot beluga128)
		; 0: typeD
		(to_load typeD slot0 beluga129)
		(next_load dummy-type slot0 dummy-slot beluga129)
		; 0: typeB
		(to_load typeB slot0 beluga130)
		(next_load dummy-type slot0 dummy-slot beluga130)
		; 0: typeB
		(to_load typeB slot0 beluga131)
		(next_load dummy-type slot0 dummy-slot beluga131)
		; 0: typeB
		(to_load typeB slot0 beluga132)
		(next_load dummy-type slot0 dummy-slot beluga132)
		; 0: typeC
		(to_load typeC slot0 beluga133)
		(next_load dummy-type slot0 dummy-slot beluga133)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga134)
		(next_load typeA slot0 slot1 beluga134)
		(next_load dummy-type slot1 dummy-slot beluga134)
		; 0: typeB
		(to_load typeB slot0 beluga135)
		(next_load dummy-type slot0 dummy-slot beluga135)
		; 0: typeA
		(to_load typeA slot0 beluga136)
		(next_load dummy-type slot0 dummy-slot beluga136)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga137)
		(next_load typeC slot0 slot1 beluga137)
		(next_load typeC slot1 slot2 beluga137)
		(next_load dummy-type slot2 dummy-slot beluga137)
		; 0: typeB
		(to_load typeB slot0 beluga138)
		(next_load dummy-type slot0 dummy-slot beluga138)
		; 0: typeA
		(to_load typeA slot0 beluga139)
		(next_load dummy-type slot0 dummy-slot beluga139)
		; 0: typeE
		(to_load typeE slot0 beluga140)
		(next_load dummy-type slot0 dummy-slot beluga140)
		; 0: typeD
		(to_load typeD slot0 beluga141)
		(next_load dummy-type slot0 dummy-slot beluga141)
		; 0: typeA
		(to_load typeA slot0 beluga142)
		(next_load dummy-type slot0 dummy-slot beluga142)
		; 0: typeB
		(to_load typeB slot0 beluga143)
		(next_load dummy-type slot0 dummy-slot beluga143)
		; 0: typeC
		(to_load typeC slot0 beluga144)
		(next_load dummy-type slot0 dummy-slot beluga144)
		; 0: typeB
		(to_load typeB slot0 beluga145)
		(next_load dummy-type slot0 dummy-slot beluga145)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga146)
		(next_load typeD slot0 slot1 beluga146)
		(next_load dummy-type slot1 dummy-slot beluga146)
		; 0: typeB
		(to_load typeB slot0 beluga147)
		(next_load dummy-type slot0 dummy-slot beluga147)
		; 0: typeD
		(to_load typeD slot0 beluga148)
		(next_load dummy-type slot0 dummy-slot beluga148)
		; 0: typeA
		(to_load typeA slot0 beluga149)
		(next_load dummy-type slot0 dummy-slot beluga149)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga150)
		(next_load typeC slot0 slot1 beluga150)
		(next_load dummy-type slot1 dummy-slot beluga150)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga151)
		(next_load typeB slot0 slot1 beluga151)
		(next_load dummy-type slot1 dummy-slot beluga151)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga152)
		(next_load typeC slot0 slot1 beluga152)
		(next_load dummy-type slot1 dummy-slot beluga152)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga153)
		(next_load typeD slot0 slot1 beluga153)
		(next_load dummy-type slot1 dummy-slot beluga153)
		; 0: typeB 1: typeB 2: typeB
		(to_load typeB slot0 beluga154)
		(next_load typeB slot0 slot1 beluga154)
		(next_load typeB slot1 slot2 beluga154)
		(next_load dummy-type slot2 dummy-slot beluga154)
		; 0: typeD
		(to_load typeD slot0 beluga155)
		(next_load dummy-type slot0 dummy-slot beluga155)
		; 0: typeB 1: typeB
		(to_load typeB slot0 beluga156)
		(next_load typeB slot0 slot1 beluga156)
		(next_load dummy-type slot1 dummy-slot beluga156)
		; 0: typeA
		(to_load typeA slot0 beluga157)
		(next_load dummy-type slot0 dummy-slot beluga157)
		; 0: typeB
		(to_load typeB slot0 beluga158)
		(next_load dummy-type slot0 dummy-slot beluga158)
		; 0: typeC
		(to_load typeC slot0 beluga159)
		(next_load dummy-type slot0 dummy-slot beluga159)
		; 0: typeD
		(to_load typeD slot0 beluga160)
		(next_load dummy-type slot0 dummy-slot beluga160)
		; 0: typeD
		(to_load typeD slot0 beluga161)
		(next_load dummy-type slot0 dummy-slot beluga161)
		; 0: typeB
		(to_load typeB slot0 beluga162)
		(next_load dummy-type slot0 dummy-slot beluga162)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga163)
		(next_load typeA slot0 slot1 beluga163)
		(next_load typeA slot1 slot2 beluga163)
		(next_load typeA slot2 slot3 beluga163)
		(next_load typeA slot3 slot4 beluga163)
		(next_load dummy-type slot4 dummy-slot beluga163)
		; 0: typeE
		(to_load typeE slot0 beluga164)
		(next_load dummy-type slot0 dummy-slot beluga164)
		; 0: typeA
		(to_load typeA slot0 beluga165)
		(next_load dummy-type slot0 dummy-slot beluga165)
		; 0: typeA
		(to_load typeA slot0 beluga166)
		(next_load dummy-type slot0 dummy-slot beluga166)
		; 0: typeE
		(to_load typeE slot0 beluga167)
		(next_load dummy-type slot0 dummy-slot beluga167)
		; 0: typeE
		(to_load typeE slot0 beluga168)
		(next_load dummy-type slot0 dummy-slot beluga168)
		; 0: typeE
		(to_load typeE slot0 beluga169)
		(next_load dummy-type slot0 dummy-slot beluga169)
		; 0: typeE
		(to_load typeE slot0 beluga170)
		(next_load dummy-type slot0 dummy-slot beluga170)
		; No jigs
		(to_load dummy-type dummy-slot beluga171)
		; 0: typeC
		(to_load typeC slot0 beluga172)
		(next_load dummy-type slot0 dummy-slot beluga172)
		; 0: typeA
		(to_load typeA slot0 beluga173)
		(next_load dummy-type slot0 dummy-slot beluga173)
		; 0: typeD
		(to_load typeD slot0 beluga174)
		(next_load dummy-type slot0 dummy-slot beluga174)
		; 0: typeE
		(to_load typeE slot0 beluga175)
		(next_load dummy-type slot0 dummy-slot beluga175)
		; 0: typeB 1: typeB 2: typeB 3: typeB
		(to_load typeB slot0 beluga176)
		(next_load typeB slot0 slot1 beluga176)
		(next_load typeB slot1 slot2 beluga176)
		(next_load typeB slot2 slot3 beluga176)
		(next_load dummy-type slot3 dummy-slot beluga176)
		; 0: typeA
		(to_load typeA slot0 beluga177)
		(next_load dummy-type slot0 dummy-slot beluga177)
		; 0: typeC 1: typeC 2: typeC
		(to_load typeC slot0 beluga178)
		(next_load typeC slot0 slot1 beluga178)
		(next_load typeC slot1 slot2 beluga178)
		(next_load dummy-type slot2 dummy-slot beluga178)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga179)
		(next_load typeC slot0 slot1 beluga179)
		(next_load dummy-type slot1 dummy-slot beluga179)
		; 0: typeB
		(to_load typeB slot0 beluga180)
		(next_load dummy-type slot0 dummy-slot beluga180)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga181)
		(next_load typeD slot0 slot1 beluga181)
		(next_load dummy-type slot1 dummy-slot beluga181)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga182)
		(next_load typeD slot0 slot1 beluga182)
		(next_load dummy-type slot1 dummy-slot beluga182)
		; 0: typeA
		(to_load typeA slot0 beluga183)
		(next_load dummy-type slot0 dummy-slot beluga183)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga184)
		(next_load typeC slot0 slot1 beluga184)
		(next_load dummy-type slot1 dummy-slot beluga184)
		; 0: typeD 1: typeD
		(to_load typeD slot0 beluga185)
		(next_load typeD slot0 slot1 beluga185)
		(next_load dummy-type slot1 dummy-slot beluga185)
		; 0: typeD
		(to_load typeD slot0 beluga186)
		(next_load dummy-type slot0 dummy-slot beluga186)
		; 0: typeA 1: typeA 2: typeA
		(to_load typeA slot0 beluga187)
		(next_load typeA slot0 slot1 beluga187)
		(next_load typeA slot1 slot2 beluga187)
		(next_load dummy-type slot2 dummy-slot beluga187)
		; 0: typeD
		(to_load typeD slot0 beluga188)
		(next_load dummy-type slot0 dummy-slot beluga188)
		; 0: typeC 1: typeC
		(to_load typeC slot0 beluga189)
		(next_load typeC slot0 slot1 beluga189)
		(next_load dummy-type slot1 dummy-slot beluga189)
		; No jigs
		(to_load dummy-type dummy-slot beluga190)
		; No jigs
		(to_load dummy-type dummy-slot beluga191)
		; 0: typeE
		(to_load typeE slot0 beluga192)
		(next_load dummy-type slot0 dummy-slot beluga192)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA
		(to_load typeA slot0 beluga193)
		(next_load typeA slot0 slot1 beluga193)
		(next_load typeA slot1 slot2 beluga193)
		(next_load typeA slot2 slot3 beluga193)
		(next_load typeA slot3 slot4 beluga193)
		(next_load dummy-type slot4 dummy-slot beluga193)
		; 0: typeA
		(to_load typeA slot0 beluga194)
		(next_load dummy-type slot0 dummy-slot beluga194)
		; 0: typeC
		(to_load typeC slot0 beluga195)
		(next_load dummy-type slot0 dummy-slot beluga195)
		; 0: typeC
		(to_load typeC slot0 beluga196)
		(next_load dummy-type slot0 dummy-slot beluga196)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA 6: typeA
		(to_load typeA slot0 beluga197)
		(next_load typeA slot0 slot1 beluga197)
		(next_load typeA slot1 slot2 beluga197)
		(next_load typeA slot2 slot3 beluga197)
		(next_load typeA slot3 slot4 beluga197)
		(next_load typeA slot4 slot5 beluga197)
		(next_load typeA slot5 slot6 beluga197)
		(next_load dummy-type slot6 dummy-slot beluga197)
		; 0: typeA 1: typeA
		(to_load typeA slot0 beluga198)
		(next_load typeA slot0 slot1 beluga198)
		(next_load dummy-type slot1 dummy-slot beluga198)
		; 0: typeA 1: typeA 2: typeA 3: typeA 4: typeA 5: typeA
		(to_load typeA slot0 beluga199)
		(next_load typeA slot0 slot1 beluga199)
		(next_load typeA slot1 slot2 beluga199)
		(next_load typeA slot2 slot3 beluga199)
		(next_load typeA slot3 slot4 beluga199)
		(next_load typeA slot4 slot5 beluga199)
		(next_load dummy-type slot5 dummy-slot beluga199)
		; Production schedule:
		; Production line: pl0
		; 0: jig0011 1: jig0012 2: jig0010 3: jig0005 4: jig0021 5: jig0013 6: jig0028 7: jig0037 8: jig0020 9: jig0042 10: jig0015 11: jig0040 12: jig0027 13: jig0003 14: jig0022 15: jig0025 16: jig0038 17: jig0030 18: jig0043 19: jig0014 20: jig0050 21: jig0044 22: jig0048 23: jig0059 24: jig0046 25: jig0051 26: jig0068 27: jig0053 28: jig0060 29: jig0063 30: jig0075 31: jig0080 32: jig0067 33: jig0073 34: jig0052 35: jig0077 36: jig0088 37: jig0066 38: jig0078 39: jig0083 40: jig0090 41: jig0076 42: jig0101 43: jig0084 44: jig0104 45: jig0082 46: jig0115 47: jig0092 48: jig0109 49: jig0102 50: jig0110 51: jig0071 52: jig0098 53: jig0117 54: jig0105 55: jig0112 56: jig0134 57: jig0118 58: jig0132 59: jig0125 60: jig0099 61: jig0144 62: jig0124 63: jig0147 64: jig0131 65: jig0127 66: jig0143 67: jig0119 68: jig0146 69: jig0129 70: jig0137 71: jig0161 72: jig0159 73: jig0164 74: jig0140 75: jig0169 76: jig0142 77: jig0150 78: jig0168 79: jig0151 80: jig0176 81: jig0174 82: jig0149 83: jig0157 84: jig0155 85: jig0171 86: jig0162 87: jig0187 88: jig0189 89: jig0192 90: jig0172 91: jig0186 92: jig0191 93: jig0194 94: jig0198 95: jig0196 96: jig0190 97: jig0184 98: jig0193 99: jig0217 100: jig0205 101: jig0220 102: jig0211 103: jig0212 104: jig0223 105: jig0207 106: jig0222 107: jig0208 108: jig0203 109: jig0204 110: jig0219 111: jig0236 112: jig0234 113: jig0221 114: jig0229 115: jig0239 116: jig0242 117: jig0233 118: jig0227 119: jig0241 120: jig0248 121: jig0237 122: jig0235 123: jig0255 124: jig0261 125: jig0266 126: jig0240 127: jig0257 128: jig0256 129: jig0265 130: jig0274 131: jig0264 132: jig0268 133: jig0253 134: jig0267 135: jig0278 136: jig0279 137: jig0275 138: jig0283 139: jig0280 140: jig0281 141: jig0296 142: jig0293 143: jig0310 144: jig0297 145: jig0289 146: jig0295 147: jig0309 148: jig0282 149: jig0291 150: jig0326 151: jig0305 152: jig0308 153: jig0287 154: jig0286 155: jig0325 156: jig0328 157: jig0299 158: jig0315 159: jig0341
		(to_deliver jig0011 pl0)
		(next_deliver jig0011 jig0012)
		(next_deliver jig0012 jig0010)
		(next_deliver jig0010 jig0005)
		(next_deliver jig0005 jig0021)
		(next_deliver jig0021 jig0013)
		(next_deliver jig0013 jig0028)
		(next_deliver jig0028 jig0037)
		(next_deliver jig0037 jig0020)
		(next_deliver jig0020 jig0042)
		(next_deliver jig0042 jig0015)
		(next_deliver jig0015 jig0040)
		(next_deliver jig0040 jig0027)
		(next_deliver jig0027 jig0003)
		(next_deliver jig0003 jig0022)
		(next_deliver jig0022 jig0025)
		(next_deliver jig0025 jig0038)
		(next_deliver jig0038 jig0030)
		(next_deliver jig0030 jig0043)
		(next_deliver jig0043 jig0014)
		(next_deliver jig0014 jig0050)
		(next_deliver jig0050 jig0044)
		(next_deliver jig0044 jig0048)
		(next_deliver jig0048 jig0059)
		(next_deliver jig0059 jig0046)
		(next_deliver jig0046 jig0051)
		(next_deliver jig0051 jig0068)
		(next_deliver jig0068 jig0053)
		(next_deliver jig0053 jig0060)
		(next_deliver jig0060 jig0063)
		(next_deliver jig0063 jig0075)
		(next_deliver jig0075 jig0080)
		(next_deliver jig0080 jig0067)
		(next_deliver jig0067 jig0073)
		(next_deliver jig0073 jig0052)
		(next_deliver jig0052 jig0077)
		(next_deliver jig0077 jig0088)
		(next_deliver jig0088 jig0066)
		(next_deliver jig0066 jig0078)
		(next_deliver jig0078 jig0083)
		(next_deliver jig0083 jig0090)
		(next_deliver jig0090 jig0076)
		(next_deliver jig0076 jig0101)
		(next_deliver jig0101 jig0084)
		(next_deliver jig0084 jig0104)
		(next_deliver jig0104 jig0082)
		(next_deliver jig0082 jig0115)
		(next_deliver jig0115 jig0092)
		(next_deliver jig0092 jig0109)
		(next_deliver jig0109 jig0102)
		(next_deliver jig0102 jig0110)
		(next_deliver jig0110 jig0071)
		(next_deliver jig0071 jig0098)
		(next_deliver jig0098 jig0117)
		(next_deliver jig0117 jig0105)
		(next_deliver jig0105 jig0112)
		(next_deliver jig0112 jig0134)
		(next_deliver jig0134 jig0118)
		(next_deliver jig0118 jig0132)
		(next_deliver jig0132 jig0125)
		(next_deliver jig0125 jig0099)
		(next_deliver jig0099 jig0144)
		(next_deliver jig0144 jig0124)
		(next_deliver jig0124 jig0147)
		(next_deliver jig0147 jig0131)
		(next_deliver jig0131 jig0127)
		(next_deliver jig0127 jig0143)
		(next_deliver jig0143 jig0119)
		(next_deliver jig0119 jig0146)
		(next_deliver jig0146 jig0129)
		(next_deliver jig0129 jig0137)
		(next_deliver jig0137 jig0161)
		(next_deliver jig0161 jig0159)
		(next_deliver jig0159 jig0164)
		(next_deliver jig0164 jig0140)
		(next_deliver jig0140 jig0169)
		(next_deliver jig0169 jig0142)
		(next_deliver jig0142 jig0150)
		(next_deliver jig0150 jig0168)
		(next_deliver jig0168 jig0151)
		(next_deliver jig0151 jig0176)
		(next_deliver jig0176 jig0174)
		(next_deliver jig0174 jig0149)
		(next_deliver jig0149 jig0157)
		(next_deliver jig0157 jig0155)
		(next_deliver jig0155 jig0171)
		(next_deliver jig0171 jig0162)
		(next_deliver jig0162 jig0187)
		(next_deliver jig0187 jig0189)
		(next_deliver jig0189 jig0192)
		(next_deliver jig0192 jig0172)
		(next_deliver jig0172 jig0186)
		(next_deliver jig0186 jig0191)
		(next_deliver jig0191 jig0194)
		(next_deliver jig0194 jig0198)
		(next_deliver jig0198 jig0196)
		(next_deliver jig0196 jig0190)
		(next_deliver jig0190 jig0184)
		(next_deliver jig0184 jig0193)
		(next_deliver jig0193 jig0217)
		(next_deliver jig0217 jig0205)
		(next_deliver jig0205 jig0220)
		(next_deliver jig0220 jig0211)
		(next_deliver jig0211 jig0212)
		(next_deliver jig0212 jig0223)
		(next_deliver jig0223 jig0207)
		(next_deliver jig0207 jig0222)
		(next_deliver jig0222 jig0208)
		(next_deliver jig0208 jig0203)
		(next_deliver jig0203 jig0204)
		(next_deliver jig0204 jig0219)
		(next_deliver jig0219 jig0236)
		(next_deliver jig0236 jig0234)
		(next_deliver jig0234 jig0221)
		(next_deliver jig0221 jig0229)
		(next_deliver jig0229 jig0239)
		(next_deliver jig0239 jig0242)
		(next_deliver jig0242 jig0233)
		(next_deliver jig0233 jig0227)
		(next_deliver jig0227 jig0241)
		(next_deliver jig0241 jig0248)
		(next_deliver jig0248 jig0237)
		(next_deliver jig0237 jig0235)
		(next_deliver jig0235 jig0255)
		(next_deliver jig0255 jig0261)
		(next_deliver jig0261 jig0266)
		(next_deliver jig0266 jig0240)
		(next_deliver jig0240 jig0257)
		(next_deliver jig0257 jig0256)
		(next_deliver jig0256 jig0265)
		(next_deliver jig0265 jig0274)
		(next_deliver jig0274 jig0264)
		(next_deliver jig0264 jig0268)
		(next_deliver jig0268 jig0253)
		(next_deliver jig0253 jig0267)
		(next_deliver jig0267 jig0278)
		(next_deliver jig0278 jig0279)
		(next_deliver jig0279 jig0275)
		(next_deliver jig0275 jig0283)
		(next_deliver jig0283 jig0280)
		(next_deliver jig0280 jig0281)
		(next_deliver jig0281 jig0296)
		(next_deliver jig0296 jig0293)
		(next_deliver jig0293 jig0310)
		(next_deliver jig0310 jig0297)
		(next_deliver jig0297 jig0289)
		(next_deliver jig0289 jig0295)
		(next_deliver jig0295 jig0309)
		(next_deliver jig0309 jig0282)
		(next_deliver jig0282 jig0291)
		(next_deliver jig0291 jig0326)
		(next_deliver jig0326 jig0305)
		(next_deliver jig0305 jig0308)
		(next_deliver jig0308 jig0287)
		(next_deliver jig0287 jig0286)
		(next_deliver jig0286 jig0325)
		(next_deliver jig0325 jig0328)
		(next_deliver jig0328 jig0299)
		(next_deliver jig0299 jig0315)
		(next_deliver jig0315 jig0341)
		(next_deliver jig0341 dummy-jig)
		; Production line: pl1
		; 0: jig0009 1: jig0007 2: jig0002 3: jig0017 4: jig0032 5: jig0034 6: jig0036 7: jig0004 8: jig0039 9: jig0016 10: jig0033 11: jig0026 12: jig0023 13: jig0008 14: jig0024 15: jig0029 16: jig0019 17: jig0035 18: jig0049 19: jig0047 20: jig0054 21: jig0018 22: jig0031 23: jig0045 24: jig0041 25: jig0065 26: jig0069 27: jig0055 28: jig0061 29: jig0064 30: jig0056 31: jig0081 32: jig0062 33: jig0085 34: jig0058 35: jig0087 36: jig0091 37: jig0072 38: jig0079 39: jig0070 40: jig0097 41: jig0089 42: jig0074 43: jig0093 44: jig0057 45: jig0108 46: jig0086 47: jig0096 48: jig0113 49: jig0107 50: jig0111 51: jig0100 52: jig0122 53: jig0095 54: jig0121 55: jig0123 56: jig0106 57: jig0094 58: jig0128 59: jig0130 60: jig0135 61: jig0103 62: jig0139 63: jig0120 64: jig0141 65: jig0136 66: jig0114 67: jig0126 68: jig0116 69: jig0133 70: jig0156 71: jig0148 72: jig0160 73: jig0138 74: jig0167 75: jig0170 76: jig0145 77: jig0152 78: jig0175 79: jig0165 80: jig0153 81: jig0179 82: jig0154 83: jig0166 84: jig0158 85: jig0163 86: jig0177 87: jig0183 88: jig0180 89: jig0173 90: jig0181 91: jig0195 92: jig0178 93: jig0182 94: jig0188 95: jig0200 96: jig0199 97: jig0185 98: jig0210 99: jig0201 100: jig0218 101: jig0197 102: jig0206 103: jig0213 104: jig0224 105: jig0225 106: jig0202 107: jig0216 108: jig0232 109: jig0209 110: jig0214 111: jig0226 112: jig0215 113: jig0228 114: jig0231 115: jig0238 116: jig0243 117: jig0246 118: jig0230 119: jig0245 120: jig0250 121: jig0247 122: jig0249 123: jig0244 124: jig0262 125: jig0254 126: jig0259 127: jig0263 128: jig0258 129: jig0251 130: jig0252 131: jig0270 132: jig0276 133: jig0260 134: jig0271 135: jig0285 136: jig0272 137: jig0277 138: jig0269 139: jig0284 140: jig0292 141: jig0294 142: jig0273 143: jig0298 144: jig0301 145: jig0302 146: jig0306 147: jig0311 148: jig0304 149: jig0303 150: jig0332 151: jig0307 152: jig0334 153: jig0290 154: jig0312 155: jig0327 156: jig0338 157: jig0300 158: jig0333
		(to_deliver jig0009 pl1)
		(next_deliver jig0009 jig0007)
		(next_deliver jig0007 jig0002)
		(next_deliver jig0002 jig0017)
		(next_deliver jig0017 jig0032)
		(next_deliver jig0032 jig0034)
		(next_deliver jig0034 jig0036)
		(next_deliver jig0036 jig0004)
		(next_deliver jig0004 jig0039)
		(next_deliver jig0039 jig0016)
		(next_deliver jig0016 jig0033)
		(next_deliver jig0033 jig0026)
		(next_deliver jig0026 jig0023)
		(next_deliver jig0023 jig0008)
		(next_deliver jig0008 jig0024)
		(next_deliver jig0024 jig0029)
		(next_deliver jig0029 jig0019)
		(next_deliver jig0019 jig0035)
		(next_deliver jig0035 jig0049)
		(next_deliver jig0049 jig0047)
		(next_deliver jig0047 jig0054)
		(next_deliver jig0054 jig0018)
		(next_deliver jig0018 jig0031)
		(next_deliver jig0031 jig0045)
		(next_deliver jig0045 jig0041)
		(next_deliver jig0041 jig0065)
		(next_deliver jig0065 jig0069)
		(next_deliver jig0069 jig0055)
		(next_deliver jig0055 jig0061)
		(next_deliver jig0061 jig0064)
		(next_deliver jig0064 jig0056)
		(next_deliver jig0056 jig0081)
		(next_deliver jig0081 jig0062)
		(next_deliver jig0062 jig0085)
		(next_deliver jig0085 jig0058)
		(next_deliver jig0058 jig0087)
		(next_deliver jig0087 jig0091)
		(next_deliver jig0091 jig0072)
		(next_deliver jig0072 jig0079)
		(next_deliver jig0079 jig0070)
		(next_deliver jig0070 jig0097)
		(next_deliver jig0097 jig0089)
		(next_deliver jig0089 jig0074)
		(next_deliver jig0074 jig0093)
		(next_deliver jig0093 jig0057)
		(next_deliver jig0057 jig0108)
		(next_deliver jig0108 jig0086)
		(next_deliver jig0086 jig0096)
		(next_deliver jig0096 jig0113)
		(next_deliver jig0113 jig0107)
		(next_deliver jig0107 jig0111)
		(next_deliver jig0111 jig0100)
		(next_deliver jig0100 jig0122)
		(next_deliver jig0122 jig0095)
		(next_deliver jig0095 jig0121)
		(next_deliver jig0121 jig0123)
		(next_deliver jig0123 jig0106)
		(next_deliver jig0106 jig0094)
		(next_deliver jig0094 jig0128)
		(next_deliver jig0128 jig0130)
		(next_deliver jig0130 jig0135)
		(next_deliver jig0135 jig0103)
		(next_deliver jig0103 jig0139)
		(next_deliver jig0139 jig0120)
		(next_deliver jig0120 jig0141)
		(next_deliver jig0141 jig0136)
		(next_deliver jig0136 jig0114)
		(next_deliver jig0114 jig0126)
		(next_deliver jig0126 jig0116)
		(next_deliver jig0116 jig0133)
		(next_deliver jig0133 jig0156)
		(next_deliver jig0156 jig0148)
		(next_deliver jig0148 jig0160)
		(next_deliver jig0160 jig0138)
		(next_deliver jig0138 jig0167)
		(next_deliver jig0167 jig0170)
		(next_deliver jig0170 jig0145)
		(next_deliver jig0145 jig0152)
		(next_deliver jig0152 jig0175)
		(next_deliver jig0175 jig0165)
		(next_deliver jig0165 jig0153)
		(next_deliver jig0153 jig0179)
		(next_deliver jig0179 jig0154)
		(next_deliver jig0154 jig0166)
		(next_deliver jig0166 jig0158)
		(next_deliver jig0158 jig0163)
		(next_deliver jig0163 jig0177)
		(next_deliver jig0177 jig0183)
		(next_deliver jig0183 jig0180)
		(next_deliver jig0180 jig0173)
		(next_deliver jig0173 jig0181)
		(next_deliver jig0181 jig0195)
		(next_deliver jig0195 jig0178)
		(next_deliver jig0178 jig0182)
		(next_deliver jig0182 jig0188)
		(next_deliver jig0188 jig0200)
		(next_deliver jig0200 jig0199)
		(next_deliver jig0199 jig0185)
		(next_deliver jig0185 jig0210)
		(next_deliver jig0210 jig0201)
		(next_deliver jig0201 jig0218)
		(next_deliver jig0218 jig0197)
		(next_deliver jig0197 jig0206)
		(next_deliver jig0206 jig0213)
		(next_deliver jig0213 jig0224)
		(next_deliver jig0224 jig0225)
		(next_deliver jig0225 jig0202)
		(next_deliver jig0202 jig0216)
		(next_deliver jig0216 jig0232)
		(next_deliver jig0232 jig0209)
		(next_deliver jig0209 jig0214)
		(next_deliver jig0214 jig0226)
		(next_deliver jig0226 jig0215)
		(next_deliver jig0215 jig0228)
		(next_deliver jig0228 jig0231)
		(next_deliver jig0231 jig0238)
		(next_deliver jig0238 jig0243)
		(next_deliver jig0243 jig0246)
		(next_deliver jig0246 jig0230)
		(next_deliver jig0230 jig0245)
		(next_deliver jig0245 jig0250)
		(next_deliver jig0250 jig0247)
		(next_deliver jig0247 jig0249)
		(next_deliver jig0249 jig0244)
		(next_deliver jig0244 jig0262)
		(next_deliver jig0262 jig0254)
		(next_deliver jig0254 jig0259)
		(next_deliver jig0259 jig0263)
		(next_deliver jig0263 jig0258)
		(next_deliver jig0258 jig0251)
		(next_deliver jig0251 jig0252)
		(next_deliver jig0252 jig0270)
		(next_deliver jig0270 jig0276)
		(next_deliver jig0276 jig0260)
		(next_deliver jig0260 jig0271)
		(next_deliver jig0271 jig0285)
		(next_deliver jig0285 jig0272)
		(next_deliver jig0272 jig0277)
		(next_deliver jig0277 jig0269)
		(next_deliver jig0269 jig0284)
		(next_deliver jig0284 jig0292)
		(next_deliver jig0292 jig0294)
		(next_deliver jig0294 jig0273)
		(next_deliver jig0273 jig0298)
		(next_deliver jig0298 jig0301)
		(next_deliver jig0301 jig0302)
		(next_deliver jig0302 jig0306)
		(next_deliver jig0306 jig0311)
		(next_deliver jig0311 jig0304)
		(next_deliver jig0304 jig0303)
		(next_deliver jig0303 jig0332)
		(next_deliver jig0332 jig0307)
		(next_deliver jig0307 jig0334)
		(next_deliver jig0334 jig0290)
		(next_deliver jig0290 jig0312)
		(next_deliver jig0312 jig0327)
		(next_deliver jig0327 jig0338)
		(next_deliver jig0338 jig0300)
		(next_deliver jig0300 jig0333)
		(next_deliver jig0333 dummy-jig)
		; Action cost:
		(= (total-cost ) 0)
	)
  (:goal (and
		; All jigs empty (order defined by production schedule)
		(empty jig0011)
		(empty jig0012)
		(empty jig0010)
		(empty jig0005)
		(empty jig0021)
		(empty jig0013)
		(empty jig0028)
		(empty jig0037)
		(empty jig0020)
		(empty jig0042)
		(empty jig0015)
		(empty jig0040)
		(empty jig0027)
		(empty jig0003)
		(empty jig0022)
		(empty jig0025)
		(empty jig0038)
		(empty jig0030)
		(empty jig0043)
		(empty jig0014)
		(empty jig0050)
		(empty jig0044)
		(empty jig0048)
		(empty jig0059)
		(empty jig0046)
		(empty jig0051)
		(empty jig0068)
		(empty jig0053)
		(empty jig0060)
		(empty jig0063)
		(empty jig0075)
		(empty jig0080)
		(empty jig0067)
		(empty jig0073)
		(empty jig0052)
		(empty jig0077)
		(empty jig0088)
		(empty jig0066)
		(empty jig0078)
		(empty jig0083)
		(empty jig0090)
		(empty jig0076)
		(empty jig0101)
		(empty jig0084)
		(empty jig0104)
		(empty jig0082)
		(empty jig0115)
		(empty jig0092)
		(empty jig0109)
		(empty jig0102)
		(empty jig0110)
		(empty jig0071)
		(empty jig0098)
		(empty jig0117)
		(empty jig0105)
		(empty jig0112)
		(empty jig0134)
		(empty jig0118)
		(empty jig0132)
		(empty jig0125)
		(empty jig0099)
		(empty jig0144)
		(empty jig0124)
		(empty jig0147)
		(empty jig0131)
		(empty jig0127)
		(empty jig0143)
		(empty jig0119)
		(empty jig0146)
		(empty jig0129)
		(empty jig0137)
		(empty jig0161)
		(empty jig0159)
		(empty jig0164)
		(empty jig0140)
		(empty jig0169)
		(empty jig0142)
		(empty jig0150)
		(empty jig0168)
		(empty jig0151)
		(empty jig0176)
		(empty jig0174)
		(empty jig0149)
		(empty jig0157)
		(empty jig0155)
		(empty jig0171)
		(empty jig0162)
		(empty jig0187)
		(empty jig0189)
		(empty jig0192)
		(empty jig0172)
		(empty jig0186)
		(empty jig0191)
		(empty jig0194)
		(empty jig0198)
		(empty jig0196)
		(empty jig0190)
		(empty jig0184)
		(empty jig0193)
		(empty jig0217)
		(empty jig0205)
		(empty jig0220)
		(empty jig0211)
		(empty jig0212)
		(empty jig0223)
		(empty jig0207)
		(empty jig0222)
		(empty jig0208)
		(empty jig0203)
		(empty jig0204)
		(empty jig0219)
		(empty jig0236)
		(empty jig0234)
		(empty jig0221)
		(empty jig0229)
		(empty jig0239)
		(empty jig0242)
		(empty jig0233)
		(empty jig0227)
		(empty jig0241)
		(empty jig0248)
		(empty jig0237)
		(empty jig0235)
		(empty jig0255)
		(empty jig0261)
		(empty jig0266)
		(empty jig0240)
		(empty jig0257)
		(empty jig0256)
		(empty jig0265)
		(empty jig0274)
		(empty jig0264)
		(empty jig0268)
		(empty jig0253)
		(empty jig0267)
		(empty jig0278)
		(empty jig0279)
		(empty jig0275)
		(empty jig0283)
		(empty jig0280)
		(empty jig0281)
		(empty jig0296)
		(empty jig0293)
		(empty jig0310)
		(empty jig0297)
		(empty jig0289)
		(empty jig0295)
		(empty jig0309)
		(empty jig0282)
		(empty jig0291)
		(empty jig0326)
		(empty jig0305)
		(empty jig0308)
		(empty jig0287)
		(empty jig0286)
		(empty jig0325)
		(empty jig0328)
		(empty jig0299)
		(empty jig0315)
		(empty jig0341)
		(empty jig0009)
		(empty jig0007)
		(empty jig0002)
		(empty jig0017)
		(empty jig0032)
		(empty jig0034)
		(empty jig0036)
		(empty jig0004)
		(empty jig0039)
		(empty jig0016)
		(empty jig0033)
		(empty jig0026)
		(empty jig0023)
		(empty jig0008)
		(empty jig0024)
		(empty jig0029)
		(empty jig0019)
		(empty jig0035)
		(empty jig0049)
		(empty jig0047)
		(empty jig0054)
		(empty jig0018)
		(empty jig0031)
		(empty jig0045)
		(empty jig0041)
		(empty jig0065)
		(empty jig0069)
		(empty jig0055)
		(empty jig0061)
		(empty jig0064)
		(empty jig0056)
		(empty jig0081)
		(empty jig0062)
		(empty jig0085)
		(empty jig0058)
		(empty jig0087)
		(empty jig0091)
		(empty jig0072)
		(empty jig0079)
		(empty jig0070)
		(empty jig0097)
		(empty jig0089)
		(empty jig0074)
		(empty jig0093)
		(empty jig0057)
		(empty jig0108)
		(empty jig0086)
		(empty jig0096)
		(empty jig0113)
		(empty jig0107)
		(empty jig0111)
		(empty jig0100)
		(empty jig0122)
		(empty jig0095)
		(empty jig0121)
		(empty jig0123)
		(empty jig0106)
		(empty jig0094)
		(empty jig0128)
		(empty jig0130)
		(empty jig0135)
		(empty jig0103)
		(empty jig0139)
		(empty jig0120)
		(empty jig0141)
		(empty jig0136)
		(empty jig0114)
		(empty jig0126)
		(empty jig0116)
		(empty jig0133)
		(empty jig0156)
		(empty jig0148)
		(empty jig0160)
		(empty jig0138)
		(empty jig0167)
		(empty jig0170)
		(empty jig0145)
		(empty jig0152)
		(empty jig0175)
		(empty jig0165)
		(empty jig0153)
		(empty jig0179)
		(empty jig0154)
		(empty jig0166)
		(empty jig0158)
		(empty jig0163)
		(empty jig0177)
		(empty jig0183)
		(empty jig0180)
		(empty jig0173)
		(empty jig0181)
		(empty jig0195)
		(empty jig0178)
		(empty jig0182)
		(empty jig0188)
		(empty jig0200)
		(empty jig0199)
		(empty jig0185)
		(empty jig0210)
		(empty jig0201)
		(empty jig0218)
		(empty jig0197)
		(empty jig0206)
		(empty jig0213)
		(empty jig0224)
		(empty jig0225)
		(empty jig0202)
		(empty jig0216)
		(empty jig0232)
		(empty jig0209)
		(empty jig0214)
		(empty jig0226)
		(empty jig0215)
		(empty jig0228)
		(empty jig0231)
		(empty jig0238)
		(empty jig0243)
		(empty jig0246)
		(empty jig0230)
		(empty jig0245)
		(empty jig0250)
		(empty jig0247)
		(empty jig0249)
		(empty jig0244)
		(empty jig0262)
		(empty jig0254)
		(empty jig0259)
		(empty jig0263)
		(empty jig0258)
		(empty jig0251)
		(empty jig0252)
		(empty jig0270)
		(empty jig0276)
		(empty jig0260)
		(empty jig0271)
		(empty jig0285)
		(empty jig0272)
		(empty jig0277)
		(empty jig0269)
		(empty jig0284)
		(empty jig0292)
		(empty jig0294)
		(empty jig0273)
		(empty jig0298)
		(empty jig0301)
		(empty jig0302)
		(empty jig0306)
		(empty jig0311)
		(empty jig0304)
		(empty jig0303)
		(empty jig0332)
		(empty jig0307)
		(empty jig0334)
		(empty jig0290)
		(empty jig0312)
		(empty jig0327)
		(empty jig0338)
		(empty jig0300)
		(empty jig0333)
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
		(to_unload dummy-jig beluga193)
		(to_unload dummy-jig beluga194)
		(to_unload dummy-jig beluga195)
		(to_unload dummy-jig beluga196)
		(to_unload dummy-jig beluga197)
		(to_unload dummy-jig beluga198)
		(to_unload dummy-jig beluga199)
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
		(to_load dummy-type dummy-slot beluga193)
		(to_load dummy-type dummy-slot beluga194)
		(to_load dummy-type dummy-slot beluga195)
		(to_load dummy-type dummy-slot beluga196)
		(to_load dummy-type dummy-slot beluga197)
		(to_load dummy-type dummy-slot beluga198)
		(to_load dummy-type dummy-slot beluga199)
	))
  (:metric minimize (total-cost))
)