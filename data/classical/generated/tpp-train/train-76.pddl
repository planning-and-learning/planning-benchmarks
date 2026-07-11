(define (problem tpp-g1-t1-m3-d1-l4)
  (:domain TPP-Propositional)
  (:objects
    market0 market1 market2 - market
    depot0 - depot
    truck0 - truck
    goods0 - goods
    level0 level1 level2 level3 level4 - level
  )
  (:init
    (next level1 level0)
    (next level2 level1)
    (next level3 level2)
    (next level4 level3)
    (connected depot0 market0)
    (connected depot0 market1)
    (connected depot0 market2)
    (connected market0 depot0)
    (connected market0 market1)
    (connected market0 market2)
    (connected market1 depot0)
    (connected market1 market0)
    (connected market1 market2)
    (connected market2 depot0)
    (connected market2 market0)
    (connected market2 market1)
    (at truck0 depot0)
    (stored goods0 level0)
    (loaded goods0 truck0 level0)
    (on-sale goods0 market0 level1)
    (ready-to-load goods0 market0 level0)
    (on-sale goods0 market1 level2)
    (ready-to-load goods0 market1 level0)
    (on-sale goods0 market2 level1)
    (ready-to-load goods0 market2 level0)
  )
  (:goal
    (and
      (stored goods0 level4)
    )
  )
)
