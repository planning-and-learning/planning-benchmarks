(define (problem pfile1)
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
    pone10 - piecetype1
    pone11 - piecetype1
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
    ptwo15 - piecetype2
    ptwo16 - piecetype2
    ptwo17 - piecetype2
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
    pthree24 - piecetype3
    pthree25 - piecetype3
    pthree26 - piecetype3
    pthree27 - piecetype3
    pthree28 - piecetype3
    pthree29 - piecetype3)
 (:init 
  (energy)
)
 (:goal
  (and
     (baked-structure pthree25 ptwo0)
     (baked-structure pone9 pthree27)
     (baked-structure pthree1 pthree15)
     (baked-structure ptwo15 pthree10)
     (baked-structure pone8 pthree4)
     (baked-structure pthree12 pthree20)
     (baked-structure ptwo4 pthree13)
     (baked-structure pthree7 pthree17)
     (baked-structure ptwo12 ptwo5)
     (baked-structure pthree2 ptwo7)
     (baked-structure pthree9 ptwo10)
     (baked-structure pthree6 pone0)
     (baked-structure ptwo9 pthree3)
     (baked-structure pthree11 pthree16)
     (baked-structure ptwo11 ptwo16)
     (baked-structure pthree14 pthree18)
     (baked-structure pone2 pthree0)
     (baked-structure pone11 pone5)
     (baked-structure pone6 ptwo17)
     (baked-structure pthree22 pthree26)
     (baked-structure pthree5 pthree21)
     (baked-structure pthree28 ptwo1)
     (baked-structure pthree8 ptwo8)
     (baked-structure pone7 pone3)
     (baked-structure pone1 pthree23)
     (baked-structure ptwo13 ptwo6)
     (baked-structure pone10 pthree24)
     (baked-structure pthree19 pthree29)
     (baked-structure ptwo3 ptwo2)
     (baked-structure pone4 ptwo14)
))
 (:metric minimize (total-time))
)
