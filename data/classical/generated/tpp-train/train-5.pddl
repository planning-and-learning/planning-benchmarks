(define (problem tpp-g1-t1-m2-d1-l1)
  (:domain TPP-Propositional)
  (:objects
    market0 market1 - market
    depot0 - depot
    truck0 - truck
    goods0 - goods
    level0 level1 - level
  )
  (:init
    (next level1 level0)
    (connected depot0 market0)
    (connected depot0 market1)
    (connected market0 depot0)
    (connected market0 market1)
    (connected market1 depot0)
    (connected market1 market0)
    (at truck0 depot0)
    (stored goods0 level0)
    (loaded goods0 truck0 level0)
    (on-sale goods0 market0 level1)
    (ready-to-load goods0 market0 level0)
    (on-sale goods0 market1 level1)
    (ready-to-load goods0 market1 level0)
  )
  (:goal
    (and
      (stored goods0 level1)
    )
  )
)
