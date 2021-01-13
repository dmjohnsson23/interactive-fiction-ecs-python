from ..interpreter import Intent
from ..game import Game

class System:
    def filter_intent(self, intent: Intent):
        """
        Determine if this system cares about the given intent. This
        will be called to determine if process_intent should be called.
        """
        return True
    
    def process_intent(self, intent: Intent, game: Game):
        """
        Perform actions based on the passed intent. Override this to
        define the behavior of your new system.

        Should return the passed intent, optionally modified for other
        systems down the pipe.
        """
        return intent