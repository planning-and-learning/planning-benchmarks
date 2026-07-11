(define (problem blocks-3-5)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4 b5)
  (:init
    (on-table b1)
    (on b3 b1)
    (on b2 b3)
    (on b4 b2)
    (on-table b5)
    (clear b4)
    (clear b5)
  )
  (:goal
    (and
      (on b3 b2)
      (on b5 b3)
    )
  )
)
