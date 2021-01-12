from .components import Actor, Reactor, Reference

class Intent:
    def __init__(self, action, method, actor, reactor):
        """
        action: The verb in the command sentence; what the player wants to do.
        method: A modifier on the verb, such as "up". Not used often outside of directions.
        actor: The object to act with; the direct object of the command sentence.
        reactor: The object to act on; the indirect object of the command sentence
        """
        self.action = action
        self.method = method
        self.actor = actor
        self.reactor = reactor

command_shortcuts = {
    'u': 'go up',
    'up': 'go up',
    'd': 'go down',
    'down': 'go down',
    'n': 'go north',
    'north': 'go north',
    's': 'go south',
    'south': 'go south',
    'e': 'go east',
    'east': 'go east',
    'w': 'go west',
    'west': 'go west',
    'i': 'check inventory',
    'inventory': 'check inventory',
}


class InterpreterContext:
    def __init__(self):
        self.nouns = set(Reference.lookup.keys())
        self.verbs = set(Actor.lookup.keys()).union(Reactor.lookup.keys())

    def interpret(self, command_string):
        """
        Convert an arbitrary command string to an Intent
        """

        # Should work with a variety of different command structures, such as:
        #
        # * "go up stairs" -> action='go', method='up', reactor='stairs'
        # * "attack monster" -> action='attack', reactor='monster'
        # * "attack with sword" -> action='attack', actor='sword'
        # * "attack monster with sword" -> action='attack', actor='sword', reactor='monster'
        # * "use key to open gate" -> action='open', actor='key', reactor='gate'
        # * "put card in slot" -> action='put', actor='card', reactor='slot'
        # * "look at runestone" -> action='look', reactor='runestone'
        # * "using hammer, break rock" -> action='break', actor='hammer', reactor='rock'

        command_string = command_string.lower()
        if command_string in command_shortcuts:
            command_string = command_shortcuts[command_string]
        words = command_string.split()
        # TODO parse words into Intent

