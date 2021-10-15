from .thrower_dragon import ThrowerDragon
import random


class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.1
    implemented = True   # Change to True to view in the GUI
    food_cost = 2
    min_range = 5

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        place = self.place
        for _ in range(self.min_range):
            place = place.entrance
        while place!=skynet:
            if place.terminators != []:
                return random.choice(place.terminators)
            place = place.entrance
        else:
            return None
    # END 2.1
