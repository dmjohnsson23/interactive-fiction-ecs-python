from .__common__ import Component
from collections import defaultdict

class Reactor(Component):
    """
    A component describing how the entity reacts to a certain action. The indirect object in a command sentence.
    """

    lookup = defaultdict(list)

    def __init__(self, *verbs):
        self.verbs = verbs
    
    def assign(self, entity):
        for name in self.verbs:
            self.lookup[name].append(entity)
    