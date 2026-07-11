(define (problem blocks-3-4)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4)
  (:init
    (on-table b1)
    (on-table b4)
    (on b3 b4)
    (on-table b2)
    (clear b1)
    (clear b2)
    (clear b3)
  )
  (:goal
    (and
      (on b1 b2)
      (on b4 b3)
    )
  )
)
