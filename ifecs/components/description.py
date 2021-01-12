from .__common__ import Component
from collections import defaultdict


class Description(Component):
    """
    A component describing how entities are descried to the player.
    """

    def __init__(self, short_description, long_description):
        self.short_description = short_description
        self.long_description = long_description

