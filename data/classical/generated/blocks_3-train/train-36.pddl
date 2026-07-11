(define (problem blocks-3-4)
  (:domain blocksworld-3ops)
  (:objects b1 b2 b3 b4)
  (:init
    (on-table b2)
    (on b1 b2)
    (on b3 b1)
    (on b4 b3)
    (clear b4)
  )
  (:goal
    (and
      (on b4 b2)
    )
  )
)
