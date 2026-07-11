(define (problem blocks-3-6)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4 b5 b6)
  (:init
    (on-table b5)
    (on b3 b5)
    (on b1 b3)
    (on b6 b1)
    (on b2 b6)
    (on b4 b2)
    (clear b4)
  )
  (:goal
    (and
      (on b5 b2)
      (on b4 b5)
    )
  )
)
