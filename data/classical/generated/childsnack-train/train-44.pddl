(define (problem childsnack-c2-t2)
  (:domain child-snack)
  (:objects
      child1 child2 - child
      bread1 bread2 - bread-portion
      content1 content2 - content-portion
      sandw1 sandw2 sandw3 - sandwich
      tray1 tray2 - tray
      table1 table2 table3 - place
  )
  (:init
    (at tray1 kitchen)
    (at tray2 kitchen)
    (at_kitchen_bread bread1)
    (at_kitchen_bread bread2)
    (at_kitchen_content content1)
    (at_kitchen_content content2)
    (not_allergic_gluten child1)
    (not_allergic_gluten child2)
    (waiting child1 table2)
    (waiting child2 table1)
    (notexist sandw1)
    (notexist sandw2)
    (notexist sandw3)
  )
  (:goal
    (and
      (served child1)
      (served child2)
    )
  )
)
