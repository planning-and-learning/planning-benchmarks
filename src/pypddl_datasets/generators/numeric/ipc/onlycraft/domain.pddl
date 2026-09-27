;;
;; Domain inspired by the model provided in the paper  
;; "Crafting a Pogo Stick in Minecraft with Heuristic Search (Extended Abstract)",
;; authored by Yarin Benyamin, Argaman Mordoch, Shahaf Shperberg, Wiktor Piotrowski, Roni Stern
;;

(define (domain polycraft)
  (:requirements :strips :numeric-fluents :typing)

  (:types
    cell - object
  )

  (:predicates
    (position ?c - cell)
    (tree_cell ?c - cell)
    (low_tree_cell ?c - cell)
    (air_cell ?c - cell)
    (dead_tree_cell ?c - cell)
    (crafting_table_cell ?c - cell)
    (connected ?from - cell ?to - cell)
  )

  (:functions
    (count_log_in_inventory)
    (count_planks_in_inventory)
    (count_stick_in_inventory)
    (count_sack_polyisoprene_pellets_in_inventory)
    (count_tree_tap_in_inventory)
    (count_pogo_stick)
    (toxicity)
  )

  (:action break
    :parameters (?pos - cell)
    :precondition (and
      (tree_cell ?pos)
    )
    :effect (and
      (not (tree_cell ?pos))
      (air_cell ?pos)
      (increase (count_log_in_inventory) 1)
    )
  )

  (:action break_low
    :parameters (?pos - cell)
    :precondition (and
      (low_tree_cell ?pos)
    )
    :effect (and
      (not (low_tree_cell ?pos))
      (air_cell ?pos)
      (increase (count_log_in_inventory) 0.5)
    )
  )

  (:action break_brutal
    :parameters (?pos - cell)
    :precondition (and
      (tree_cell ?pos)
    )
    :effect (and
      (not (tree_cell ?pos))
      (dead_tree_cell ?pos)
      (increase (count_log_in_inventory) 2)
    )
  )

  (:action craft_plank
    :parameters ()
    :precondition (and
      (>= (count_log_in_inventory) 1)
    )
    :effect (and
      (decrease (count_log_in_inventory) 1)
      (increase (count_planks_in_inventory) 4)
    )
  )

  (:action craft_stick
    :parameters ()
    :precondition (and
      (>= (count_planks_in_inventory) 2)
    )
    :effect (and
      (decrease (count_planks_in_inventory) 2)
      (increase (count_stick_in_inventory) 4)
    )
  )

  (:action craft_tree_tap
    :parameters (?pos - cell)
    :precondition (and
      (crafting_table_cell ?pos)
      (>= (count_planks_in_inventory) 5)
      (>= (count_stick_in_inventory) 1)
    )
    :effect (and
      (decrease (count_planks_in_inventory) 5)
      (decrease (count_stick_in_inventory) 1)
      (increase (count_tree_tap_in_inventory) 1)
    )
  )

  (:action place_tree_tap
    :parameters (?pos - cell)
    :precondition (and
      (tree_cell ?pos)
      (>= (count_tree_tap_in_inventory) 1)
    )
    :effect (and
      (not (tree_cell ?pos))
      (air_cell ?pos)
      (decrease (count_tree_tap_in_inventory) 1)
      (increase (count_sack_polyisoprene_pellets_in_inventory) 1)
    )
  )

  (:action smelt_pellets_raw
    :parameters ()
    :precondition (and
      (>= (count_log_in_inventory) 2)
    )
    :effect (and
      (decrease (count_log_in_inventory) 2)
      (increase (count_sack_polyisoprene_pellets_in_inventory) 0.5)
    )
  )

  (:action craft_synthetic_pellets
    :parameters ()
    :precondition (and
      (>= (count_log_in_inventory) 1)
    )
    :effect (and
      (decrease (count_log_in_inventory) 1)
      (increase (count_sack_polyisoprene_pellets_in_inventory) 1)
      (increase (toxicity) 1)
    )
  )

  (:action craft_wooden_pogo
    :parameters (?pos - cell)
    :precondition (and
      (crafting_table_cell ?pos)
      (>= (count_planks_in_inventory) 2)
      (>= (count_stick_in_inventory) 4)
      (>= (count_sack_polyisoprene_pellets_in_inventory) 1)
      (<= (toxicity) 1)
    )
    :effect (and
      (decrease (count_planks_in_inventory) 2)
      (decrease (count_stick_in_inventory) 4)
      (decrease (count_sack_polyisoprene_pellets_in_inventory) 1)
      (increase (count_pogo_stick) 1)
    )
  )
)
