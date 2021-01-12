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
    
    def can_act_on(self, entity, intent):
        """
        Returns true if this entity can perform this action on the given entity.
        This is called as a confirmation after it has already been verified that 
        the verbs match.

        Override this for custom behavior.
        """
        return True