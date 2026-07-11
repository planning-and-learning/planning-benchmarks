(define (problem tpp-g2-t1-m3-d1-l2)
  (:domain TPP-Propositional)
  (:objects
    market0 market1 market2 - market
    depot0 - depot
    truck0 - truck
    goods0 goods1 - goods
    level0 level1 level2 - level
  )
  (:init
    (next level1 level0)
    (next level2 level1)
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
    (on-sale goods0 market0 level2)
    (ready-to-load goods0 market0 level0)
    (on-sale goods0 market1 level1)
    (ready-to-load goods0 market1 level0)
    (on-sale goods0 market2 level1)
    (ready-to-load goods0 market2 level0)
    (stored goods1 level0)
    (loaded goods1 truck0 level0)
    (on-sale goods1 market0 level2)
    (ready-to-load goods1 market0 level0)
    (on-sale goods1 market1 level2)
    (ready-to-load goods1 market1 level0)
    (on-sale goods1 market2 level1)
    (ready-to-load goods1 market2 level0)
  )
  (:goal
    (and
      (stored goods0 level2)
      (stored goods1 level2)
    )
  )
)
