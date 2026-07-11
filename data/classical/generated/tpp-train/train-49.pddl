(define (problem tpp-g4-t1-m1-d1-l1)
  (:domain TPP-Propositional)
  (:objects
    market0 - market
    depot0 - depot
    truck0 - truck
    goods0 goods1 goods2 goods3 - goods
    level0 level1 - level
  )
  (:init
    (next level1 level0)
    (connected depot0 market0)
    (connected market0 depot0)
    (at truck0 depot0)
    (stored goods0 level0)
    (loaded goods0 truck0 level0)
    (on-sale goods0 market0 level1)
    (ready-to-load goods0 market0 level0)
    (stored goods1 level0)
    (loaded goods1 truck0 level0)
    (on-sale goods1 market0 level1)
    (ready-to-load goods1 market0 level0)
    (stored goods2 level0)
    (loaded goods2 truck0 level0)
    (on-sale goods2 market0 level1)
    (ready-to-load goods2 market0 level0)
    (stored goods3 level0)
    (loaded goods3 truck0 level0)
    (on-sale goods3 market0 level1)
    (ready-to-load goods3 market0 level0)
  )
  (:goal
    (and
      (stored goods0 level1)
      (stored goods1 level1)
      (stored goods2 level1)
      (stored goods3 level1)
    )
  )
)
