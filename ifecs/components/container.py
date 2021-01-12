from .__common__ import Component
from collections import defaultdict
from .placement import Placement

class Container(Component):
    """
    A component describing how entities can be placed in or on this entity in the game world.
    """

    def __init__(self, *verbs):
        self.verbs = verbs

    def assign(self, entity):
        self._entity = entity

    @property
    def children(self):
        return Placement.lookup(self._entity)
    
    def can_hold(self, entity):
        """
        Returns true if this entity can hold the other entity.

        Override this for custom behavior.
        """
        return True