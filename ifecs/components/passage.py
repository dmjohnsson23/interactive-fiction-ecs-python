from .reactor import Reactor
from enum import Enum

class Direction(Enum):
    north = 'n'
    south = 's'
    east = 'e'
    west = 'w'
    up = 'u'
    down = 'd'

    @property
    def inverse(self):
        if self is Direction.north: return Direction.south
        if self is Direction.south: return Direction.north
        if self is Direction.east: return Direction.west
        if self is Direction.west: return Direction.east
        if self is Direction.up: return Direction.down
        if self is Direction.down: return Direction.up

class Passage(Reactor):
    def __init__(self, direction, to_entity):
        self.direction = direction
        self.to_entity = to_entity
        super().__init__(
            'go', 
            'climb' if direction in (Direction.up, Direction.down) else 'walk', 
            'enter')