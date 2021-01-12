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
    
    def can_be_acted_on_by(self, entity, intent):
        """
        Returns true if this entity can be acted on by the given entity.
        This is called as a confirmation if the actor's verbs already match.

        Override this for custom behavior.
        """
        return True