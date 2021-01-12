from .__common__ import Component
from collections import defaultdict

class Placement(Component):
    """
    A component describing an entity being placed in or on another
    """

    lookup = defaultdict(set)

    def __init__(self, parent_entity, weight = None, size = None):
        self._parent = parent_entity
        self._entity = None
        self.weight = weight
        self.size = size
    
    def assign(self, entity):
        self._entity = entity
        self.lookup[self._parent].add(entity)
    
    @property
    def parent(self):
        return self.parent
    
    @parent.setter
    def parent(self, new_parent):
        self.lookup[self._parent].remove(self._entity)
        self._parent = new_parent
        self.lookup[new_parent].add(self._entity)
    
    @classmethod
    def lookup_tree(cls, root_entity):
        found = cls.lookup[root_entity]
        for entity in found:
            found.union(cls.lookup_tree(entity))
