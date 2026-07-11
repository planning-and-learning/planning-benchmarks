(define (problem blocks-4-4)
  (:domain blocksworld)
  (:objects b1 b2 b3 b4)
  (:init
    (arm-empty)
    (on-table b1)
    (on b4 b1)
    (on b3 b4)
    (on b2 b3)
    (clear b2)
  )
  (:goal
    (and
      (on b1 b4)
      (on b2 b1)
      (on b3 b2)
    )
  )
)
