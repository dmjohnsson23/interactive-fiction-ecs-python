from .components import Actor, Reactor, Reference
import re

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
    'q': 'quit'
}

basic_words = {
    'the',
    'a',
    'with',
    'to',
    'it',
    'at',
}

built_in_commands = {
    'look',
    'look at',
    'check',
    'go',
    'go to',
    'quit'
}


class InterpreterContext:
    def __init__(self):
        self.recompile_lexicon()
    
    def recompile_lexicon(self):
        self.nouns = set(Reference.lookup.keys())
        self.verbs = set(Actor.lookup.keys()).union(Reactor.lookup.keys()).union(built_in_commands)
        self.pattern = self._compile_lexicon_pattern(self.nouns.union(self.verbs).union(basic_words))
    
    def _compile_lexicon_pattern(self, word_list):
        # Produce a pattern that looks like this:
        # \b(?:dog house)|(?:house)|(?:dog)\b
        return re.compile(r'\b(?:{})\b'.format('|'.join(
            map(
                # Escape all passed words in case they contain regex metacharacters
                re.escape,
                # There may be overlapping word matches in the lexicon. For example, "north", "west", 
                # "north west", "west corridor", and "north west corridor" might all be valid 
                # lexicon entries. In the event of a lexical overlap, the longer entry should always
                # win. Thus, longer entries need to be sorted first in the compiled pattern.
                sorted(word_list, key=len, reverse=True)
            )
        )))

    def interpret(self, command_string) -> Intent:
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
        words = self._split_command(self.pattern, command_string)
        # TODO detect part of speech and convert to Intent
        
    
    def _split_command(self, lexicon_pattern, command_string):
        """
        Parse the command string into lexicon entries. (Some entries might be multi-word, 
        hence why we can't just use string.split())
        """
        last_index = 0
        words = []
        unmatched_pattern = re.compile(r"\b[-'\w\s]+\b")
        # TODO in the event there is unmatched text, try to determine if it is a noun or verb, 
        # and adjust the error message accordingly
        for match in lexicon_pattern.finditer(command_string):
            # make sure there are no unmatched words
            unmatched = unmatched_pattern.search(command_string, last_index, match.start())
            if unmatched:
                raise InterpreterError('Sorry, I do not know about this "{}" you speak of'.format(command_string[unmatched.start():unmatched.end()]))
            # Add the matched lexicon entry to the list
            words.append(command_string[match.start():match.end()])
            last_index = match.end()
        # Also check for unmatched words at the end of the string
        unmatched = unmatched_pattern.search(command_string, last_index)
        if unmatched:
            raise InterpreterError('Sorry, I do not know about this "{}" you speak of'.format(command_string[unmatched.start():unmatched.end()]))
        return words


class InterpreterError(RuntimeError):
    pass