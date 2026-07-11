(define (problem barman-c1-i4-s3-g2-ig100)
  (:domain barman)
  (:objects
      left right - hand
      shaker1 - shaker
      shot1 shot2 shot3 - shot
      ingredient1 ingredient2 ingredient3 ingredient4 - ingredient
      cocktail1 - cocktail
      dispenser1 dispenser2 dispenser3 dispenser4 - dispenser
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
    (clean shot1)
    (clean shot2)
    (clean shot3)
    (empty shot1)
    (empty shot2)
    (empty shot3)
    (dispenses dispenser1 ingredient1)
    (dispenses dispenser2 ingredient2)
    (dispenses dispenser3 ingredient3)
    (dispenses dispenser4 ingredient4)
    (next l0 l1)
    (next l1 l2)
    (cocktail-part1 cocktail1 ingredient4)
    (cocktail-part2 cocktail1 ingredient3)
  )
  (:goal
    (and
      (contains shot1 ingredient3)
      (contains shot2 ingredient4)
    )
  )
  (:metric minimize (total-cost))
)
