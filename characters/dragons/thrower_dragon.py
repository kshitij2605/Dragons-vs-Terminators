from .dragon import Dragon
from utils import random_or_none
import random


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost = 3

    # ADD/OVERRIDE CLASS ATTRIBUTES HERE

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        place = self.place
        count = 0
        max = self.max_range
        if self.min_range != float('inf'):
            for _ in range(self.min_range):
                place = place.entrance
                max -= 1
        while place!=skynet and count != max+1:
            if place.terminators != []:
                return random.choice(place.terminators)
            place = place.entrance
            count += 1
        else:
            return None
        #return random_or_none(self.place.terminators)  # REPLACE THIS LINE
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
