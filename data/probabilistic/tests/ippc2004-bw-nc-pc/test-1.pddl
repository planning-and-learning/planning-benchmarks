(define (problem bw-nc-pc-5)
 (:domain bw-nc-pc-5)
 (:objects block0 block1 block2 block3 block4 - block)
 (:init
  (on-top-of block0 table)
  (on-top-of block1 table)
  (on-top-of block2 block3)
  (on-top-of block3 table)
  (on-top-of block4 table)
 )
 (:goal
  (and
   (on-top-of block0 table)
   (on-top-of block3 block2)
   (on-top-of block2 block1)
   (on-top-of block1 block4)
   (on-top-of block4 table)

  )
 )
 (:goal-reward 500)
)
