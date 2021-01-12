from collections import defaultdict
from .entity import Entity
from .components import Component

class World:
    def __init__(self):
        self._entity_to_component = defaultdict(list)
        self._component_to_entity = defaultdict(set)
    
    def create_entity(self, *components: Component):
        """
        Create and return a new entity will all the give components
        """
        entity = Entity()
        self._entity_to_component[entity] = components
        for component in components:
            self._component_to_entity[type(component)].add(entity)
            component.assign(entity)
    
    def add_component(self, entity: Entity, component: Component):
        """
        Add a component to an existing entity
        """
        self._entity_to_component[entity].append(component)
        self._component_to_entity[type(component)].add(entity)
        component.assign(entity)
    

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
