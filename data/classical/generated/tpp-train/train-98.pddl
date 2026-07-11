(define (problem tpp-g3-t1-m1-d1-l2)
  (:domain TPP-Propositional)
  (:objects
    market0 - market
    depot0 - depot
    truck0 - truck
    goods0 goods1 goods2 - goods
    level0 level1 level2 - level
  )
  (:init
    (next level1 level0)
    (next level2 level1)
    (connected depot0 market0)
    (connected market0 depot0)
    (at truck0 depot0)
    (stored goods0 level0)
    (loaded goods0 truck0 level0)
    (on-sale goods0 market0 level2)
    (ready-to-load goods0 market0 level0)
    (stored goods1 level0)
    (loaded goods1 truck0 level0)
    (on-sale goods1 market0 level1)
    (ready-to-load goods1 market0 level0)
    (stored goods2 level0)
    (loaded goods2 truck0 level0)
    (on-sale goods2 market0 level2)
    (ready-to-load goods2 market0 level0)
  )
  (:goal
    (and
      (stored goods0 level2)
      (stored goods1 level2)
      (stored goods2 level2)
    )
  )
)
