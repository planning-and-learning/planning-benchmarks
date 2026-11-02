language 1;
distribution schedule;
revision "2";
metadata {
    probability "Independent categorical properties and parameterized integer-percent Bernoulli choices; partial goals including possibly empty conjunctions.";
    solvability "not asserted";
    scope "membership and structural corner cases";
    cases ["num_parts=1; all property probabilities at 0, 1, 99, 100 percent"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_parts: int;
param num_shapes: int = 0;
param num_colours: int = 2;
param num_widths: int = 2;
param num_orientations: int = 2;
param cylindrical_goal_probability: int = 80;
param initial_colour_probability: int = 50;
param goal_colour_probability: int = 80;
param initial_hole_probability: int = 50;
param goal_hole_probability: int = 80;
param goal_surface_probability: int = 50;

require valid_counts: num_parts >= 1 and num_shapes >= 0 and num_shapes <= 2 and num_colours >= 1 and num_colours <= 4 and num_widths >= 1 and num_widths <= 3 and num_orientations >= 1 and num_orientations <= 2;
require valid_probabilities: cylindrical_goal_probability >= 0 and cylindrical_goal_probability <= 100 and initial_colour_probability >= 0 and initial_colour_probability <= 100 and goal_colour_probability >= 0 and goal_colour_probability <= 100 and initial_hole_probability >= 0 and initial_hole_probability <= 100 and goal_hole_probability >= 0 and goal_hole_probability <= 100 and goal_surface_probability >= 0 and goal_surface_probability <= 100;
let Parts = names("p", num_parts);
let ShapeLabels = ["circular", "oblong"];
let Shape[i in range(num_shapes)] = ShapeLabels[i];
let ExtraShapes = values(Shape);
let Shapes = ["cylindrical"] + ExtraShapes;
let ColorLabels = ["blue", "yellow", "red", "black"];
let Color[i in range(num_colours)] = ColorLabels[i];
let Colors = values(Color);
let WidthLabels = ["one", "two", "three"];
let Width[i in range(num_widths)] = WidthLabels[i];
let Widths = values(Width);
let OrientationLabels = ["front", "back"];
let Orientation[i in range(num_orientations)] = OrientationLabels[i];
let Orientations = values(Orientation);
let Surfaces = ["polished", "rough", "smooth"];
let Painters = ["immersion-painter", "spray-painter"];
let Drillers = ["drill-press", "punch"];
objects Parts: part;
objects ExtraShapes: ashape;
objects Colors: colour;
objects Widths: width;
objects Orientations: anorient;
constants ["cylindrical"]: ashape;
constants Surfaces: surface;
constants ["cold", "hot"]: "temperature-type";
constants Painters + Drillers + ["polisher", "roller", "lathe", "grinder"]: machine;
relation initial.has_paint(Painters, Colors) as "has-paint";
relation initial.has_bit(Drillers, Widths) as "has-bit";
relation initial.can_orient(Drillers, Orientations) as "can-orient";
relation initial.shape(Parts, Shapes);
relation initial.surface_condition(Parts, Surfaces) as "surface-condition";
relation initial.temperature(Parts, ["cold", "hot"]);
relation initial.painted(Parts, Colors);
relation initial.has_hole(Parts, Widths, Orientations) as "has-hole";
relation goal.shape(Parts, Shapes);
relation goal.surface_condition(Parts, Surfaces) as "surface-condition";
relation goal.painted(Parts, Colors);
relation goal.has_hole(Parts, Widths, Orientations) as "has-hole";
initial {
 rule paint_supplies: forall m in Painters, c in Colors: initial.has_paint(m,c);
 rule drill_bits: forall m in Drillers, w in Widths: initial.has_bit(m,w);
 rule drill_orientations: forall m in Drillers, o in Orientations: initial.can_orient(m,o);
 rule shape_choice: forall p in Parts: count(s in Shapes: initial.shape(p,s)) == 1;
 rule surface_choice: forall p in Parts: count(s in Surfaces: initial.surface_condition(p,s)) == 1;
 rule cold_parts: forall p in Parts, t in ["cold", "hot"]: initial.temperature(p,t) iff t == "cold";
 rule optional_color: forall p in Parts: count(c in Colors: initial.painted(p,c)) <= 1;
 rule color_endpoints: forall p in Parts: if initial_colour_probability == 0 then count(c in Colors: initial.painted(p,c)) == 0 else if initial_colour_probability == 100 then count(c in Colors: initial.painted(p,c)) == 1 else true;
 rule optional_hole: forall p in Parts: count(w in Widths, o in Orientations: initial.has_hole(p,w,o)) <= 1;
 rule hole_endpoints: forall p in Parts: if initial_hole_probability == 0 then count(w in Widths, o in Orientations: initial.has_hole(p,w,o)) == 0 else if initial_hole_probability == 100 then count(w in Widths, o in Orientations: initial.has_hole(p,w,o)) == 1 else true;
}
goal {
 rule cylindrical_only: forall p in Parts, s in Shapes where s != "cylindrical": not goal.shape(p,s);
 rule shape_endpoints: forall p in Parts: if cylindrical_goal_probability == 0 then not goal.shape(p,"cylindrical") else if cylindrical_goal_probability == 100 then goal.shape(p,"cylindrical") else true;
 rule optional_surface: forall p in Parts: count(s in Surfaces: goal.surface_condition(p,s)) <= 1;
 rule surface_endpoints: forall p in Parts: if goal_surface_probability == 0 then count(s in Surfaces: goal.surface_condition(p,s)) == 0 else if goal_surface_probability == 100 then count(s in Surfaces: goal.surface_condition(p,s)) == 1 else true;
 rule optional_color: forall p in Parts: count(c in Colors: goal.painted(p,c)) <= 1;
 rule color_endpoints: forall p in Parts: if goal_colour_probability == 0 then count(c in Colors: goal.painted(p,c)) == 0 else if goal_colour_probability == 100 then count(c in Colors: goal.painted(p,c)) == 1 else true;
 rule optional_hole: forall p in Parts: count(w in Widths, o in Orientations: goal.has_hole(p,w,o)) <= 1;
 rule hole_endpoints: forall p in Parts: if goal_hole_probability == 0 then count(w in Widths, o in Orientations: goal.has_hole(p,w,o)) == 0 else if goal_hole_probability == 100 then count(w in Widths, o in Orientations: goal.has_hole(p,w,o)) == 1 else true;
}
joint {}
