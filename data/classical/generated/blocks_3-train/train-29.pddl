(define (problem blocks-3-4)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4)
  (:init
    (on-table b4)
    (on b2 b4)
    (on b3 b2)
    (on-table b1)
    (clear b1)
    (clear b3)
  )
  (:goal
    (and
      (on b4 b1)
      (on b3 b4)
      (on b2 b3)
    )
  )
)
