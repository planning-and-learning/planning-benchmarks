(define (problem tpp-g1-t1-m1-d1-l3)
  (:domain TPP-Propositional)
  (:objects
    market0 - market
    depot0 - depot
    truck0 - truck
    goods0 - goods
    level0 level1 level2 level3 - level
  )
  (:init
    (next level1 level0)
    (next level2 level1)
    (next level3 level2)
    (connected depot0 market0)
    (connected market0 depot0)
    (at truck0 depot0)
    (stored goods0 level0)
    (loaded goods0 truck0 level0)
    (on-sale goods0 market0 level1)
    (ready-to-load goods0 market0 level0)
  )
  (:goal
    (and
      (stored goods0 level3)
    )
  )
)
