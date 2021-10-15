from .thrower_dragon import ThrowerDragon
import random

class ShortThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at most 3 places away."""

    name = 'Short'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.1
    implemented = True  # Change to True to view in the GUI
    food_cost = 2
    max_range = 3

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        place = self.place
        count = 0
        while place!=skynet and count!=self.max_range+1:
            if place.terminators != []:
                return random.choice(place.terminators)
            place = place.entrance
            count += 1
        else:
            return None
    # END 2.1
