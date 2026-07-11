(define (problem blocks-4-4)
  (:domain blocksworld)
  (:objects b1 b2 b3 b4)
  (:init
    (arm-empty)
    (on-table b4)
    (on b3 b4)
    (on b1 b3)
    (on b2 b1)
    (clear b2)
  )
  (:goal
    (and
      (on b3 b2)
    )
  )
)
