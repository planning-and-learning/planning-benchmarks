(define (problem blocks-3-5)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4 b5)
  (:init
    (on-table b5)
    (on b4 b5)
    (on b1 b4)
    (on b2 b1)
    (on-table b3)
    (clear b2)
    (clear b3)
  )
  (:goal
    (and
      (on b3 b2)
      (on b5 b1)
    )
  )
)
