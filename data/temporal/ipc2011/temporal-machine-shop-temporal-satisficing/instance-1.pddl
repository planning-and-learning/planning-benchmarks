(define (problem pfile0)
 (:domain domain-tms-2-3-light)
 (:objects
    kiln0 - (either kiln8 kiln20)
    pone0 - piecetype1
    pone1 - piecetype1
    pone2 - piecetype1
    pone3 - piecetype1
    pone4 - piecetype1
    pone5 - piecetype1
    pone6 - piecetype1
    pone7 - piecetype1
    pone8 - piecetype1
    pone9 - piecetype1
    ptwo0 - piecetype2
    ptwo1 - piecetype2
    ptwo2 - piecetype2
    ptwo3 - piecetype2
    ptwo4 - piecetype2
    ptwo5 - piecetype2
    ptwo6 - piecetype2
    ptwo7 - piecetype2
    ptwo8 - piecetype2
    ptwo9 - piecetype2
    ptwo10 - piecetype2
    ptwo11 - piecetype2
    ptwo12 - piecetype2
    ptwo13 - piecetype2
    ptwo14 - piecetype2
    pthree0 - piecetype3
    pthree1 - piecetype3
    pthree2 - piecetype3
    pthree3 - piecetype3
    pthree4 - piecetype3
    pthree5 - piecetype3
    pthree6 - piecetype3
    pthree7 - piecetype3
    pthree8 - piecetype3
    pthree9 - piecetype3
    pthree10 - piecetype3
    pthree11 - piecetype3
    pthree12 - piecetype3
    pthree13 - piecetype3
    pthree14 - piecetype3
    pthree15 - piecetype3
    pthree16 - piecetype3
    pthree17 - piecetype3
    pthree18 - piecetype3
    pthree19 - piecetype3
    pthree20 - piecetype3
    pthree21 - piecetype3
    pthree22 - piecetype3
    pthree23 - piecetype3
    pthree24 - piecetype3)
 (:init 
  (energy)
)
 (:goal
  (and
     (baked-structure pthree8 ptwo13)
     (baked-structure pthree10 ptwo10)
     (baked-structure pone6 pthree2)
     (baked-structure pone8 ptwo7)
     (baked-structure ptwo9 pthree24)
     (baked-structure pone0 ptwo2)
     (baked-structure pthree15 pthree23)
     (baked-structure pthree0 ptwo8)
     (baked-structure pthree21 pone4)
     (baked-structure pthree22 pthree17)
     (baked-structure pone9 ptwo14)
     (baked-structure pthree1 ptwo4)
     (baked-structure pthree7 pthree16)
     (baked-structure pthree4 pthree19)
     (baked-structure pthree20 pone3)
     (baked-structure pthree6 ptwo6)
     (baked-structure ptwo11 pthree13)
     (baked-structure ptwo1 pone5)
     (baked-structure pthree11 pone7)
     (baked-structure pthree18 ptwo12)
     (baked-structure pthree3 ptwo3)
     (baked-structure ptwo5 ptwo0)
     (baked-structure pthree12 pthree14)
     (baked-structure pthree9 pone2)
     (baked-structure pthree5 pone1)
))
 (:metric minimize (total-time))
)
