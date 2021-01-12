from .__common__ import Component
from collections import defaultdict
from .placement import Placement

class Container(Component):
    """
    A component describing how entities can be placed in or on this entity in the game world.
    """

    def __init__(self, weight_limit = None, size_limit = None):
        self.weight_limit = weight_limit
        self.size_limit = size_limit

    def assign(self, entity):
        self._entity = entity

    @property
    def children(self):
        return Placement.lookup(self._entity)
    