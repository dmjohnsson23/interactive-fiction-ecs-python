from .__common__ import Component
from collections import defaultdict

class Reference(Component):
    """
    A component describing how the player can reference the associated entity
    """

    lookup = defaultdict(list)

    def __init__(self, *names):
        self.names = names
    
    def assign(self, entity):
        for name in self.names:
            self.lookup[name].append(entity)