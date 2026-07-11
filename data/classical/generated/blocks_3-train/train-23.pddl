(define (problem blocks-3-5)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4 b5)
  (:init
    (on-table b4)
    (on b2 b4)
    (on b5 b2)
    (on b3 b5)
    (on b1 b3)
    (clear b1)
  )
  (:goal
    (and
      (on b1 b2)
      (on b5 b1)
    )
  )
)
