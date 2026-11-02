language 1;
distribution woodworking;
revision "2";
metadata {
    probability "Uniform fixed-size color and wood subsets. Latent part treatment is uniform varnished/glazed, surface uniform smooth/verysmooth, color uniform palette plus natural, and wood uniform palette. Select 2/3/4 goal properties with probabilities 3/5,1/5,1/5 and uniform subsets of that size. Parts are unused with probability 4/5; otherwise initial treatment and surface each have three uniform values, wood matches latent goal, and color is uniform excluding latent goal color; resample properties and same-size goal subset while the selected goal initially holds. Part sizes are uniform 1..3. Extra wood chunks use uniform 1..3 draws while remainder exceeds 3, then include the remainder, shuffle per wood and group fours. Board labels follow first-seen unused-part wood groups, with only the final board of each group allowed fewer than four chunks; board surface is rough/smooth with probabilities 3/4 and 1/4. Each needed varnish/glaze color uses uniform machine subsets of size ceil(.6*n); unspecified treatment uses ceil(.3*n) of each relevant type. Empty machine color sets receive one uniform palette color. Preprocessing budgets can yield an explicit failure outcome.";
    solvability "not asserted";
    scope "membership and structural corner cases";
    cases ["1..6 parts, 1..2 machines, wood factors 1, 1.1, 1.25, 1.5, 2: membership and resource counterexamples"];
    limitations ["Arbitrary-size sampler completeness is not machine-proved.", "Exact whole-task probability weights are established only for explicitly stated bounded cases."];
}
param num_parts: int;
param num_machines: int;
param wood_factor: float = 1.0;

require positive_counts: num_parts >= 1 and num_machines >= 1;
require resource_factor: wood_factor >= 1;

let Colors = ["black", "white", "red", "green", "blue", "mauve"];
let ColorValues = Colors + ["natural"];
let Woods = ["oak", "pine", "cherry", "teak", "mahogany", "beech", "walnut"];
let Surfaces = ["rough", "smooth", "verysmooth"];
let Treatments = ["varnished", "glazed", "colourfragments"];
let AllTreatments = Treatments + ["untreated"];
let GoalTreatments = ["varnished", "glazed"];
let GoalSurfaces = ["smooth", "verysmooth"];
let PartSizes = ["small", "medium", "large"];
let PartIndices = range(num_parts);
let WoodIndices = range(len(Woods));
let ColorIndices = range(len(ColorValues));
let PaletteColorIndices = range(len(Colors));
let TreatmentIndices = range(len(Treatments));
let GoalTreatmentIndices = range(len(GoalTreatments));
let SurfaceIndices = range(len(Surfaces));
let GoalSurfaceIndices = range(1, len(Surfaces));
let MachineIndices = range(num_machines);
let Parts = names("p", num_parts);
let ExtraBound = ceil(3 * num_parts * (wood_factor - 1));
let MaximumBoards = num_parts + ExtraBound;
let MaximumChunks = max(1, ExtraBound);
let BoardIndices = range(MaximumBoards);
let ChunkIndices = range(MaximumChunks);
let Boards = names("b", MaximumBoards);
let SizeIndices = range(13);
let BoardSizes = names("s", 13);
let WoodObjects = Parts + Boards;
let RequiredAmounts = range(3 * num_parts + 1);
let ExtraLookup[q in RequiredAmounts] = ceil(q * (wood_factor - 1));
let PaletteColorCount = min(max(round(0.7 * num_parts), 2), len(Colors));
let PaletteWoodCount = min(max(round(0.25 * num_parts), 2), len(Woods));

let HighspeedSaws = names("highspeed-saw", num_machines);
let Glazers = names("glazer", num_machines);
let Grinders = names("grinder", num_machines);
let ImmersionVarnishers = names("immersion-varnisher", num_machines);
let Planers = names("planer", num_machines);
let Saws = names("saw", num_machines);
let SprayVarnishers = names("spray-varnisher", num_machines);
let FinishKinds = ["spray-varnisher", "immersion-varnisher", "glazer"];
let FinishKindIndices = range(3);
let FinishMachines[k in FinishKindIndices, m in MachineIndices] = FinishKinds[k] + str(m);
let Categories = ["varnished", "glazed", "unspecified"];
let CategoryIndices = range(3);
let Relevant[t in CategoryIndices, k in FinishKindIndices] = (t == 0 and k < 2) or (t == 1 and k == 2) or t == 2;
let CoverageCount[t in CategoryIndices] = ceil((if t == 2 then 0.3 else 0.6) * num_machines);

objects Colors: acolour optional;
objects Woods: awood optional;
objects Parts: part;
objects Boards: board optional;
objects BoardSizes: aboardsize optional;
objects HighspeedSaws: highspeed-saw;
objects Glazers: glazer;
objects Grinders: grinder;
objects ImmersionVarnishers: immersion-varnisher;
objects Planers: planer;
objects Saws: saw;
objects SprayVarnishers: spray-varnisher;
constants ["natural"]: acolour;
constants Surfaces: surface;
constants AllTreatments: treatmentstatus;
constants PartSizes: apartsize;

relation initial.unused(Parts);
relation initial.available(WoodObjects);
relation initial.treatment(Parts, Treatments);
relation initial.surface_condition(WoodObjects, Surfaces) as "surface-condition";
relation initial.colour(Parts, ColorValues);
relation initial.wood(WoodObjects, Woods);
relation initial.goalsize(Parts, PartSizes);
relation initial.boardsize(Boards, BoardSizes);
relation initial.boardsize_successor(BoardSizes, BoardSizes) as "boardsize-successor";
relation initial.empty(HighspeedSaws);
relation initial.has_colour(values(FinishMachines), ColorValues) as "has-colour";
relation initial.grind_treatment_change(AllTreatments, AllTreatments) as "grind-treatment-change";
relation initial.is_smooth(Surfaces) as "is-smooth";
relation goal.available(Parts);
relation goal.treatment(Parts, GoalTreatments);
relation goal.surface_condition(Parts, GoalSurfaces) as "surface-condition";
relation goal.colour(Parts, ColorValues);
relation goal.wood(Parts, Woods);
number initial.total_cost(): int(0, 0) as "total-cost";
number initial.spray_varnish_cost(Parts): int(5, 15) as "spray-varnish-cost";
number initial.glaze_cost(Parts): int(10, 20) as "glaze-cost";
number initial.grind_cost(Parts): int(15, 45) as "grind-cost";
number initial.plane_cost(Parts): int(10, 30) as "plane-cost";
metric minimize initial.total_cost();

# Latent goals include attributes omitted by the actual partial goal formula.
aux part_size[p in PartIndices]: int(1, 3);
aux latent_treatment[p in PartIndices]: int(0, 1);
aux latent_surface[p in PartIndices]: int(1, 2);
aux latent_color[p in PartIndices]: int(0, len(ColorValues) - 1);
aux latent_wood[p in PartIndices]: int(0, len(Woods) - 1);
aux selected_properties[p in PartIndices]: int(2, 4);

# Every resource token is either an unused part's required size or one chunk
# of additional wood. Active tokens have exactly one board assignment.
aux required_wood[w in WoodIndices]: int(0, 3 * num_parts);
aux extra_wood[w in WoodIndices]: int(0, ExtraBound);
aux extra_count[w in WoodIndices]: int(0, MaximumChunks);
aux chunk_size[w in WoodIndices, j in ChunkIndices]: int(0, 3);
aux part_board[p in PartIndices]: int(-1, MaximumBoards - 1);
aux chunk_board[w in WoodIndices, j in ChunkIndices]: int(-1, MaximumBoards - 1);
aux board_size[b in BoardIndices]: int(0, 12);
aux board_wood[b in BoardIndices]: int(0, len(Woods) - 1);
aux board_token_count[b in BoardIndices]: int(0, 4);
aux first_unused_wood[w in WoodIndices]: int(0, num_parts);
aux board_group_rank[b in BoardIndices]: int(0, num_parts);

# Separate category witnesses retain the exact fixed-size machine coverage
# law, including unions when a color occurs under several goal categories.
aux needed[t in CategoryIndices, c in ColorIndices]: bool;
aux selected_paint[t in CategoryIndices, k in FinishKindIndices, m in MachineIndices, c in ColorIndices]: bool;
aux assigned_paint[k in FinishKindIndices, m in MachineIndices, c in ColorIndices]: bool;
aux has_assignment[k in FinishKindIndices, m in MachineIndices]: bool;

initial {
    rule palette_colors: count(c in Colors: present(c)) == PaletteColorCount;
    rule palette_woods: count(w in Woods: present(w)) == PaletteWoodCount;
    rule part_availability: forall p in Parts: initial.available(p) iff not initial.unused(p);
    rule initial_treatment_cardinality: forall p in Parts:
        count(t in Treatments: initial.treatment(p, t)) == (if initial.unused(p) then 0 else 1);
    rule initial_surface_cardinality: forall p in Parts:
        count(s in Surfaces: initial.surface_condition(p, s)) == (if initial.unused(p) then 0 else 1);
    rule initial_color_cardinality: forall p in Parts:
        count(c in ColorValues: initial.colour(p, c)) == (if initial.unused(p) then 0 else 1);
    rule initial_wood_cardinality: forall p in Parts:
        count(w in Woods: initial.wood(p, w)) == (if initial.unused(p) then 0 else 1);
    rule initial_color_palette: forall p in Parts, c in Colors: initial.colour(p, c) implies present(c);
    rule initial_wood_palette: forall p in Parts, w in Woods: initial.wood(p, w) implies present(w);
    rule part_size_labels: forall p in PartIndices, s in range(3):
        initial.goalsize(Parts[p], PartSizes[s]) iff part_size[p] == s + 1;
    rule part_spray_cost: forall p in PartIndices: initial.spray_varnish_cost(Parts[p]) == 5 * part_size[p];
    rule part_glaze_cost: forall p in PartIndices: initial.glaze_cost(Parts[p]) == 5 * part_size[p] + 5;
    rule part_grind_cost: forall p in PartIndices: initial.grind_cost(Parts[p]) == 15 * part_size[p];
    rule part_plane_cost: forall p in PartIndices: initial.plane_cost(Parts[p]) == 10 * part_size[p];

    rule board_prefix: forall b in BoardIndices where b > 0: present(Boards[b]) implies present(Boards[b - 1]);
    rule board_availability: forall b in Boards: initial.available(b) iff present(b);
    rule board_size_labels: forall b in BoardIndices, s in SizeIndices:
        initial.boardsize(Boards[b], BoardSizes[s]) iff (present(Boards[b]) and board_size[b] == s);
    rule board_wood_labels: forall b in BoardIndices, w in WoodIndices:
        initial.wood(Boards[b], Woods[w]) iff (present(Boards[b]) and board_wood[b] == w);
    rule board_wood_palette: forall b in Boards, w in Woods: initial.wood(b, w) implies present(w);
    rule board_surface_cardinality: forall b in Boards:
        count(s in Surfaces: initial.surface_condition(b, s)) == (if present(b) then 1 else 0);
    rule board_surface_values: forall b in Boards: not initial.surface_condition(b, "verysmooth");
    rule zero_size_object: present("s0");
    rule size_object_prefix: forall s in SizeIndices where s > 0:
        present(BoardSizes[s]) iff (exists b in BoardIndices: present(Boards[b]) and board_size[b] >= s);
    rule size_successor_table: forall a in SizeIndices, b in SizeIndices:
        initial.boardsize_successor(BoardSizes[a], BoardSizes[b]) iff (b == a + 1 and present(BoardSizes[b]));

    rule highspeed_saws_empty: forall m in HighspeedSaws: initial.empty(m);
    rule machine_color_palette: forall m in values(FinishMachines), c in Colors:
        initial.has_colour(m, c) implies present(c);
    rule grind_treatment_table: forall old in AllTreatments, new in AllTreatments:
        initial.grind_treatment_change(old, new) iff
            ((old == "varnished" and new == "colourfragments") or (old != "varnished" and new == "untreated"));
    rule smooth_surfaces: forall s in Surfaces: initial.is_smooth(s) iff s != "rough";
    rule zero_total_cost: initial.total_cost() == 0;
}

goal {
    rule parts_available: forall p in Parts: goal.available(p);
    rule partial_treatment: forall p in Parts: count(t in GoalTreatments: goal.treatment(p, t)) <= 1;
    rule partial_surface: forall p in Parts: count(s in GoalSurfaces: goal.surface_condition(p, s)) <= 1;
    rule partial_color: forall p in Parts: count(c in ColorValues: goal.colour(p, c)) <= 1;
    rule partial_wood: forall p in Parts: count(w in Woods: goal.wood(p, w)) <= 1;
    rule selected_property_count: forall p in PartIndices:
        selected_properties[p] == count(t in GoalTreatments: goal.treatment(Parts[p], t))
            + count(s in GoalSurfaces: goal.surface_condition(Parts[p], s))
            + count(c in ColorValues: goal.colour(Parts[p], c))
            + count(w in Woods: goal.wood(Parts[p], w));
}

joint {
    rule latent_color_palette: forall p in PartIndices, c in PaletteColorIndices:
        latent_color[p] == c implies present(Colors[c]);
    rule latent_wood_palette: forall p in PartIndices, w in WoodIndices:
        latent_wood[p] == w implies present(Woods[w]);
    rule project_treatment: forall p in PartIndices, t in GoalTreatmentIndices:
        goal.treatment(Parts[p], GoalTreatments[t]) implies latent_treatment[p] == t;
    rule project_surface: forall p in PartIndices, s in GoalSurfaceIndices:
        goal.surface_condition(Parts[p], Surfaces[s]) implies latent_surface[p] == s;
    rule project_color: forall p in PartIndices, c in ColorIndices:
        goal.colour(Parts[p], ColorValues[c]) implies latent_color[p] == c;
    rule project_wood: forall p in PartIndices, w in WoodIndices:
        goal.wood(Parts[p], Woods[w]) implies latent_wood[p] == w;
    rule initial_wood_matches_latent_goal: forall p in PartIndices, w in WoodIndices:
        initial.wood(Parts[p], Woods[w]) implies latent_wood[p] == w;
    rule initial_color_differs_from_latent_goal: forall p in PartIndices, c in ColorIndices:
        initial.colour(Parts[p], ColorValues[c]) implies latent_color[p] != c;
    rule initially_unsatisfied: forall p in Parts:
        initial.unused(p)
        or (exists t in GoalTreatments: goal.treatment(p, t) and not initial.treatment(p, t))
        or (exists s in GoalSurfaces: goal.surface_condition(p, s) and not initial.surface_condition(p, s))
        or (exists c in ColorValues: goal.colour(p, c) and not initial.colour(p, c))
        or (exists w in Woods: goal.wood(p, w) and not initial.wood(p, w));

    rule required_resource_total: forall w in WoodIndices:
        required_wood[w] == sum(p in PartIndices: if initial.unused(Parts[p]) and latent_wood[p] == w then part_size[p] else 0);
    rule exact_extra_resource: forall w in WoodIndices:
        extra_wood[w] == sum(q in RequiredAmounts: if required_wood[w] == q then ExtraLookup[q] else 0);
    rule extra_tokens_iff_unused_wood: forall w in WoodIndices: extra_count[w] == 0 iff required_wood[w] == 0;
    rule final_remainder_only: forall w in WoodIndices:
        (required_wood[w] > 0 and extra_wood[w] <= 3) implies extra_count[w] == 1;
    rule inactive_chunk_zero: forall w in WoodIndices, j in ChunkIndices:
        j >= extra_count[w] implies chunk_size[w, j] == 0;
    rule positive_split_chunks: forall w in WoodIndices, j in ChunkIndices:
        (j < extra_count[w] and extra_wood[w] > 3) implies chunk_size[w, j] >= 1;
    rule chunk_resource_sum: forall w in WoodIndices: sum(j in ChunkIndices: chunk_size[w, j]) == extra_wood[w];
    # After shuffling, an extra-chunk multiset has a legal stopping order iff
    # two active chunks can be the final pair with a combined size above three.
    rule stopping_remainder: forall w in WoodIndices:
        extra_wood[w] > 3 implies (exists a in ChunkIndices, b in ChunkIndices where a < b:
            a < extra_count[w] and b < extra_count[w] and chunk_size[w, a] + chunk_size[w, b] > 3);

    rule part_token_assignment: forall p in PartIndices:
        (if initial.unused(Parts[p]) then part_board[p] >= 0 else part_board[p] == -1);
    rule extra_token_assignment: forall w in WoodIndices, j in ChunkIndices:
        (if j < extra_count[w] then chunk_board[w, j] >= 0 else chunk_board[w, j] == -1);
    rule part_token_wood: forall p in PartIndices, b in BoardIndices:
        part_board[p] == b implies (present(Boards[b]) and latent_wood[p] == board_wood[b]);
    rule extra_token_wood: forall w in WoodIndices, j in ChunkIndices, b in BoardIndices:
        chunk_board[w, j] == b implies (present(Boards[b]) and w == board_wood[b]);
    rule board_chunk_count: forall b in BoardIndices:
        board_token_count[b] == count(p in PartIndices: part_board[p] == b)
            + count(w in WoodIndices, j in ChunkIndices: chunk_board[w, j] == b);
    rule board_packed_size: forall b in BoardIndices:
        board_size[b] == sum(p in PartIndices: if part_board[p] == b then part_size[p] else 0)
            + sum(w in WoodIndices, j in ChunkIndices: if chunk_board[w, j] == b then chunk_size[w, j] else 0);
    rule board_presence_from_tokens: forall b in BoardIndices: present(Boards[b]) iff board_token_count[b] > 0;
    rule one_partial_group: forall w in WoodIndices:
        count(b in BoardIndices: present(Boards[b]) and board_wood[b] == w and board_token_count[b] < 4) <= 1;

    # Legacy labels preserve the order in which unused parts introduce woods.
    rule first_wood_occurrence: forall w in WoodIndices:
        ((not (exists p in PartIndices: initial.unused(Parts[p]) and latent_wood[p] == w)) and first_unused_wood[w] == num_parts)
        or (exists p in PartIndices: initial.unused(Parts[p]) and latent_wood[p] == w and first_unused_wood[w] == p);
    rule earliest_wood_occurrence: forall w in WoodIndices, p in PartIndices:
        (initial.unused(Parts[p]) and latent_wood[p] == w) implies first_unused_wood[w] <= p;
    rule board_wood_group_rank: forall b in BoardIndices:
        board_group_rank[b] == sum(w in WoodIndices: if board_wood[b] == w then first_unused_wood[w] else 0);
    rule wood_group_order: forall b in BoardIndices where b + 1 < MaximumBoards:
        present(Boards[b + 1]) implies board_group_rank[b] <= board_group_rank[b + 1];
    rule full_nonfinal_group: forall b in BoardIndices where b + 1 < MaximumBoards:
        (present(Boards[b + 1]) and board_wood[b] == board_wood[b + 1]) implies board_token_count[b] == 4;

    rule needed_varnish: forall c in ColorIndices:
        needed[0, c] iff (exists p in Parts: goal.colour(p, ColorValues[c]) and goal.treatment(p, "varnished"));
    rule needed_glaze: forall c in ColorIndices:
        needed[1, c] iff (exists p in Parts: goal.colour(p, ColorValues[c]) and goal.treatment(p, "glazed"));
    rule needed_unspecified: forall c in ColorIndices:
        needed[2, c] iff (exists p in Parts: goal.colour(p, ColorValues[c]) and not goal.treatment(p, "varnished") and not goal.treatment(p, "glazed"));
    rule category_machine_coverage: forall t in CategoryIndices, k in FinishKindIndices, c in ColorIndices:
        count(m in MachineIndices: selected_paint[t, k, m, c]) == (if Relevant[t, k] and needed[t, c] then CoverageCount[t] else 0);
    rule assigned_color_union: forall k in FinishKindIndices, m in MachineIndices, c in ColorIndices:
        assigned_paint[k, m, c] iff (exists t in CategoryIndices: selected_paint[t, k, m, c]);
    rule machine_has_assignment: forall k in FinishKindIndices, m in MachineIndices:
        has_assignment[k, m] iff (exists c in ColorIndices: assigned_paint[k, m, c]);
    rule output_color_union: forall k in FinishKindIndices, m in MachineIndices, c in ColorIndices:
        has_assignment[k, m] implies (initial.has_colour(FinishMachines[k, m], ColorValues[c]) iff assigned_paint[k, m, c]);
    rule fallback_color_count: forall k in FinishKindIndices, m in MachineIndices:
        not has_assignment[k, m] implies count(c in ColorValues: initial.has_colour(FinishMachines[k, m], c)) == 1;
    rule fallback_not_natural: forall k in FinishKindIndices, m in MachineIndices:
        not has_assignment[k, m] implies not initial.has_colour(FinishMachines[k, m], "natural");
}
