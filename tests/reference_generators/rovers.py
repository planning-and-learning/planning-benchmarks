"""Rovers tasks with connected Bernoulli visibility and movement graphs.

Sample visibility first, then each connected movement subset conditional on it.
Equipment/modes use uniform nonempty subsets; camera ownership is uniform with
extra cameras for unequipped imaging rovers. Objective visibility uses repeated
uniform draws. Sample goals retain multiplicity weighting; image goal attempts
may duplicate and undershoot the density target. Graph exhaustion propagates.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from pypddl_datasets.generators.runtime import (
    Atom, Object, Problem, RandomSource, atom, objects,
)

from pypddl_datasets.generators.classical.rovers.parameters import Parameters
from .graphs import connected_edges

Edge = tuple[int, int]
MODES = ("colour", "high_res", "low_res")


@dataclass
class Rover:
    """Mutable construction state; sampling publishes an immutable Problem."""
    location: int
    equipment: tuple[bool, bool, bool]
    traversals: tuple[Edge, ...]
    cameras: list[int] = field(default_factory=list[int])


@dataclass(frozen=True)
class Camera:
    """A camera's calibration target, carrier and supported modes."""
    target: int
    onboard: int
    modes: tuple[str, ...]


@dataclass
class World:
    """Construction stages shared by initial and goal generation."""
    parameters: Parameters
    visibility: set[Edge]
    lander: int
    rovers: list[Rover]
    cameras: list[Camera] = field(default_factory=list[Camera])
    objectives: list[frozenset[int]] = field(default_factory=list[frozenset[int]])
    samples: list[tuple[bool, bool]] = field(default_factory=list[tuple[bool, bool]])


def _flags(rng: RandomSource) -> tuple[bool, bool, bool]:
    value = rng.randrange(7)
    return value & 1 == 0, value & 2 == 0, value & 4 == 0


def _bidirectional(edges: set[Edge]) -> tuple[Edge, ...]:
    return tuple(edge for left, right in sorted(edges) for edge in ((left, right), (right, left)))


def _world(parameters: Parameters, rng: RandomSource) -> World:
    visibility = connected_edges(parameters.num_waypoints, rng, parameters.edge_probability)
    lander = rng.randrange(parameters.num_waypoints)
    rovers: list[Rover] = []
    for _ in range(parameters.num_rovers):
        location = rng.randrange(parameters.num_waypoints)
        equipment = _flags(rng)
        movement = connected_edges(parameters.num_waypoints, rng, parameters.edge_probability,
                                   allowed_edges=visibility)
        rovers.append(Rover(location, equipment, _bidirectional(movement)))
    return World(parameters, visibility, lander, rovers)


def _add_camera(world: World, rng: RandomSource, onboard: int | None = None) -> None:
    target = rng.randrange(world.parameters.num_objectives)
    onboard = rng.randrange(len(world.rovers)) if onboard is None else onboard
    modes = tuple(mode for mode, supported in zip(MODES, _flags(rng)) if supported)
    rover = world.rovers[onboard]
    rover.equipment = (rover.equipment[0], rover.equipment[1], True)
    rover.cameras.append(len(world.cameras))
    world.cameras.append(Camera(target, onboard, modes))


def _equipment_and_sites(world: World, rng: RandomSource) -> None:
    for _ in range(world.parameters.num_cameras):
        _add_camera(world, rng)
    for rover_id, rover in enumerate(world.rovers):
        if rover.equipment[2] and not rover.cameras:
            _add_camera(world, rng, rover_id)
    count = world.parameters.num_waypoints
    world.objectives = [frozenset(rng.randrange(count) for _ in range(rng.randrange(1, count + 1)))
                        for _ in range(world.parameters.num_objectives)]
    world.samples = [(rng.randrange(count) % 2 == 0, rng.randrange(count) % 2 == 0)
                     for _ in range(count)]


def _sample_goals(world: World, rng: RandomSource, kind: int, count: int) -> list[Atom]:
    sites = [waypoint for rover in world.rovers if rover.equipment[kind] and rover.traversals
             for waypoint, samples in enumerate(world.samples) if samples[kind]]
    selected: set[int] = set()
    goals: list[Atom] = []
    while len(selected) < min(count, len(set(sites))):
        # Collapsing duplicate retries retains their conditional weighted law.
        waypoint = rng.choice([site for site in sites if site not in selected])
        selected.add(waypoint)
        goals.append(atom(f"communicated_{('soil', 'rock')[kind]}_data", f"waypoint{waypoint}"))
    return goals


def _image_goals(world: World, rng: RandomSource, count: int) -> list[Atom]:
    suitable = [(objective, rover_id)
                for rover_id, rover in enumerate(world.rovers) if rover.cameras
                for objective, visible in enumerate(world.objectives)
                for waypoint in sorted(visible)
                for left, right in rover.traversals if waypoint in (left, right)]
    requests: set[tuple[int, str]] = set()
    goals: list[Atom] = []
    for _ in range(min(count, len(suitable))):
        objective, rover_id = rng.choice(suitable)
        camera = world.cameras[rng.choice(world.rovers[rover_id].cameras)]
        mode = rng.choice(camera.modes)
        if (objective, mode) not in requests:
            requests.add((objective, mode))
            goals.append(atom("communicated_image_data", f"objective{objective}", mode))
    return goals


def _goals(world: World, rng: RandomSource) -> tuple[Atom, ...]:
    density = world.parameters.num_goals
    counts = [rng.randrange(1, density + 1) + density // 3 for _ in range(3)]
    return (*_sample_goals(world, rng, 0, counts[0]), *_sample_goals(world, rng, 1, counts[1]),
            *_image_goals(world, rng, counts[2]))


def _rover_facts(index: int, rover: Rover) -> tuple[Atom, ...]:
    name = f"rover{index}"
    facts = [atom("at", name, f"waypoint{rover.location}"), atom("available", name),
             atom("store_of", f"{name}store", name), atom("empty", f"{name}store")]
    # The domain declares store_of(store, rover).
    for kind, equipped in zip(("soil_analysis", "rock_analysis", "imaging"), rover.equipment):
        if equipped:
            facts.append(atom(f"equipped_for_{kind}", name))
    facts.extend(atom("can_traverse", name, f"waypoint{left}", f"waypoint{right}")
                 for left, right in rover.traversals)
    return tuple(facts)


def _camera_facts(index: int, camera: Camera) -> tuple[Atom, ...]:
    name = f"camera{index}"
    return (atom("on_board", name, f"rover{camera.onboard}"),
            atom("calibration_target", name, f"objective{camera.target}"),
            *(atom("supports", name, mode) for mode in camera.modes))


def _initial(world: World) -> tuple[Atom, ...]:
    facts = [atom("visible", f"waypoint{left}", f"waypoint{right}")
             for left, right in _bidirectional(world.visibility)]
    facts.extend(atom(f"at_{kind}_sample", f"waypoint{waypoint}")
                 for waypoint, samples in enumerate(world.samples)
                 for kind, present in zip(("soil", "rock"), samples) if present)
    facts.extend((atom("at_lander", "general", f"waypoint{world.lander}"),
                  atom("channel_free", "general")))
    facts.extend(fact for index, rover in enumerate(world.rovers) for fact in _rover_facts(index, rover))
    facts.extend(fact for index, camera in enumerate(world.cameras) for fact in _camera_facts(index, camera))
    facts.extend(atom("visible_from", f"objective{objective}", f"waypoint{waypoint}")
                 for objective, visible in enumerate(world.objectives) for waypoint in sorted(visible))
    return tuple(facts)


def _objects(world: World) -> tuple[Object, ...]:
    return (*objects(("general",), "lander"), *objects(MODES, "mode"),
            *objects((f"rover{i}" for i in range(len(world.rovers))), "rover"),
            *objects((f"rover{i}store" for i in range(len(world.rovers))), "store"),
            *objects((f"waypoint{i}" for i in range(world.parameters.num_waypoints)), "waypoint"),
            *objects((f"camera{i}" for i in range(len(world.cameras))), "camera"),
            *objects((f"objective{i}" for i in range(len(world.objectives))), "objective"))


def sample(parameters: Parameters, rng: RandomSource) -> Problem:
    """Sample visibility, connected movement subsets, capabilities and eligible goals."""
    world = _world(parameters, rng)
    _equipment_and_sites(world, rng)
    goals = _goals(world, rng)
    return Problem(name="roverprob", domain="rover", objects=_objects(world),
                   initial=_initial(world), goal=goals)
