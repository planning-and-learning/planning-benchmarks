(define (problem blocks-3-4)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4)
  (:init
    (on-table b3)
    (on-table b1)
    (on-table b2)
    (on b4 b2)
    (clear b1)
    (clear b3)
    (clear b4)
  )
  (:goal
    (and
      (on b3 b1)
      (on b4 b3)
    )
  )
)
