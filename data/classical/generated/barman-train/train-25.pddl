(define (problem barman-c2-i2-s6-g5-ig0)
  (:domain barman)
  (:objects
      left right - hand
      shaker1 - shaker
      shot1 shot2 shot3 shot4 shot5 shot6 - shot
      ingredient1 ingredient2 - ingredient
      cocktail1 cocktail2 - cocktail
      dispenser1 dispenser2 - dispenser
      l0 l1 l2 - level
  )
  (:init
    (= (total-cost) 0)
    (handempty left)
    (handempty right)
    (ontable shaker1)
    (clean shaker1)
    (empty shaker1)
    (shaker-empty-level shaker1 l0)
    (shaker-level shaker1 l0)
    (ontable shot1)
    (ontable shot2)
    (ontable shot3)
    (ontable shot4)
    (ontable shot5)
    (ontable shot6)
    (clean shot1)
    (clean shot2)
    (clean shot3)
    (clean shot4)
    (clean shot5)
    (clean shot6)
    (empty shot1)
    (empty shot2)
    (empty shot3)
    (empty shot4)
    (empty shot5)
    (empty shot6)
    (dispenses dispenser1 ingredient1)
    (dispenses dispenser2 ingredient2)
    (next l0 l1)
    (next l1 l2)
    (cocktail-part1 cocktail1 ingredient1)
    (cocktail-part2 cocktail1 ingredient2)
    (cocktail-part1 cocktail2 ingredient2)
    (cocktail-part2 cocktail2 ingredient1)
  )
  (:goal
    (and
      (contains shot1 cocktail2)
      (contains shot2 cocktail1)
      (contains shot3 cocktail1)
      (contains shot4 cocktail2)
      (contains shot5 cocktail2)
    )
  )
  (:metric minimize (total-cost))
)
