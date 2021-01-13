from __future__ import annotations
from ifecs.interpreter import Intent
from .system import System
from ..game import Game

class SystemRunner:
    def __init__(self, system: System, dependents=None, dependencies=None):
        self.system = system
        self.dependants = dependents or []
        self.dependencies = dependencies or []

    def begin_execution_frame(self, game: Game):
        """
        Begin a new execution frame, resetting the internal state.
        """
        self.intent = None
        self.complete = False
        self.game = game
    
    def trigger(self, triggered_by: SystemRunner = None):
        if all([runner.complete for runner in self.dependencies]):
            # The first dependency is considered the primary dependency, from which we take the intent
            intent = self.dependencies[0].intent
            if intent is None:
                # The primary dependency declined the event, so we decline it by default
                # We still call complete in case this system is a secondary dependency to a dependent
                self.complete(None)
            elif self.system.filter_intent(intent):
                self.complete(self.system.process_intent(intent, game))
            else:
                self.complete(None)
    
    def complete(self, intent: Intent):
        self.intent = intent
        self.complete = True
        for runner in self.dependants:
            runner.trigger(self)
        self.game = None


class RootRunner(SystemRunner):
    def __init__(self, dependents=None):
        super().__init__(None, dependents=dependents)
    
    def trigger(self, triggered_by):
        raise NotImplementedError('The root runner must not be passed as a dependent to any other runner')

