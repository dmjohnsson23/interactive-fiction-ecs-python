from ifecs.components.reference import Reference
from ifecs.components.container import Container
from .world import World
from .entity import Entity
from . import components as comp

def build_player(world: World, starting_location: Entity):
    return world.create_entity(
        comp.Placement(starting_location),
        comp.Container() # Player inventory
    )

class RoomBuilder:
    def __init__(self, world: World, *names: str):
        self.entity = world.create_entity(
            comp.Reference(*names),
            comp.Container()
        )
        self.world = world
        self.passages = {}
        self.return_passages = {}
    
    def add_passage(self, to_room: Entity, direction: comp.Direction, passage_names=None, two_way=True):
        passage_entity = self.world.create_entity(
            comp.Passage(direction, to_room),
            comp.Placement(self.entity)
        )
        self.passages[direction] = passage_entity
        if passage_names:
            self.world.add_component(passage_entity, Reference(*passage_names))
        if two_way:
            return_passage_entity = self.world.create_entity(
                comp.Passage(direction.inverse, self.entity),
                comp.Placement(to_room)
            )
            self.return_passages[direction] = return_passage_entity
            if passage_names:
                self.world.add_component(return_passage_entity, Reference(*passage_names))
        return self
    
    def add_entity(self, entity: Entity):
        self.world.add_component(entity, comp.Placement(self.entity))
        return self