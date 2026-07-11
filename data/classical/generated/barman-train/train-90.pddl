(define (problem barman-c2-i4-s5-g4-ig100)
  (:domain barman)
  (:objects
      left right - hand
      shaker1 - shaker
      shot1 shot2 shot3 shot4 shot5 - shot
      ingredient1 ingredient2 ingredient3 ingredient4 - ingredient
      cocktail1 cocktail2 - cocktail
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
    (ontable shot4)
    (ontable shot5)
    (clean shot1)
    (clean shot2)
    (clean shot3)
    (clean shot4)
    (clean shot5)
    (empty shot1)
    (empty shot2)
    (empty shot3)
    (empty shot4)
    (empty shot5)
    (dispenses dispenser1 ingredient1)
    (dispenses dispenser2 ingredient2)
    (dispenses dispenser3 ingredient3)
    (dispenses dispenser4 ingredient4)
    (next l0 l1)
    (next l1 l2)
    (cocktail-part1 cocktail1 ingredient1)
    (cocktail-part2 cocktail1 ingredient4)
    (cocktail-part1 cocktail2 ingredient3)
    (cocktail-part2 cocktail2 ingredient2)
  )
  (:goal
    (and
      (contains shot1 ingredient4)
      (contains shot2 ingredient1)
      (contains shot3 ingredient1)
      (contains shot4 ingredient1)
    )
  )
  (:metric minimize (total-cost))
)
