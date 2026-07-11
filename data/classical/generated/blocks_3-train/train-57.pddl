(define (problem blocks-3-4)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4)
  (:init
    (on-table b2)
    (on b3 b2)
    (on b1 b3)
    (on-table b4)
    (clear b1)
    (clear b4)
  )
  (:goal
    (and
      (on b4 b3)
      (on b1 b4)
    )
  )
)
