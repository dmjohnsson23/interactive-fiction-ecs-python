from .__common__ import Component
from collections import defaultdict

class Actor(Component):
    """
    A component describing how the player can use an entity to perform an action. The direct object in a command sentence.
    """

    lookup = defaultdict(list)

    def __init__(self, *verbs):
        self.verbs = verbs
    
    def assign(self, entity):
        for name in self.verbs:
            self.lookup[name].append(entity)
    