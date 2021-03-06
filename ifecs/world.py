from collections import defaultdict
from .entity import Entity
from .components import Component
from .systems import System, SystemRunner, RootRunner
from .interpreter import Intent
from .game import Game

class World:
    """
    Represents the ECS game world. Tracks all the entities, components, and
    systems in the game.

    You should only create one world instance. Having more than one world at 
    a time may confuse any component classesthat provide their own lookup 
    registry, as these do not track which world entities belong to. Fully 
    destroy the existing world before you create a new one.
    """
    def __init__(self):
        self._entity_to_component = defaultdict(list)
        self._component_to_entity = defaultdict(set)
        self._root_runner = RootRunner()


    def destroy_world(self):
        """
        Removes and deregisters all entities from the world. Call this to fully 
        delete this world so you can be free to create a new one.
        """
        pass #TODO actually do this
    

    def create_entity(self, *components: Component):
        """
        Create and return a new entity will all the give components
        """
        entity = Entity()
        self._entity_to_component[entity] = components
        for component in components:
            self._component_to_entity[type(component)].add(entity)
            component.assign(entity)
    

    def remove_entity(self, entity: Entity):
        """
        Remove an entity and all associated components from the game.
        """
        del self._entity_to_component[entity]
        # TODO we need to call an unassign hook in each destroyed component
        for entity_set in self._component_to_entity:
            entity_set.remove(entity)
    

    def add_component(self, entity: Entity, component: Component):
        """
        Add a component to an existing entity.
        """
        self._entity_to_component[entity].append(component)
        self._component_to_entity[type(component)].add(entity)
        component.assign(entity)
    

    def remove_component(self, entity: Entity, component: Component):
        """
        Remove a specific component from a given entity.
        """
        if component in self._entity_to_component[entity]:
            self._entity_to_component[entity].remove(component)
            # TODO we need to call an unassign hook in each destroyed component
            component_type = type(component)
            if not any([isinstance(comp, component_type) for comp in self._entity_to_component[entity]]):
                self._component_to_entity[component_type].remove(entity)
    

    def components_for_entity(self, entity: Entity, filter_component=None):
        """
        Get a list of all components for an entity, optionally filtering by type
        """
        components = self._entity_to_component[entity]
        if filter_component:
            return list(filter(lambda item: isinstance(item, filter_component), components))
        else:
            return components


    def entities_with_components(self, *components):
        """
        Get a set of all entities that have all the given components
        """
        final = None
        for component in components:
            if final is None:
                final = self._component_to_entity[component]
            else:
                final = final.intersection(self._component_to_entity[component])
        return final


    def add_default_systems(self):
        """
        Adds all the default built-in systems. Returns a dictionary of the 
        SystemRunners for each system.
        """
        # TODO actually add systems
        return {}


    def add_system(self, system: System, before=None, after=None):
        pass #TODO add system


    def process_intent(self, intent: Intent, game: Game):
        self._root_runner.begin_execution_frame(game)
        self._root_runner.complete(intent)

