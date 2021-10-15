from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from utils import terminators_win


class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    food_cost = 7
    instantiated = False
    count = 0
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        Dragon.__init__(self, armor)
        if DragonKing.count == 0:
            self.instantiated = True
            DragonKing.count = 1
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        if self.instantiated is False:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            place = self.place.exit
            while place is not None:
                if place.dragon is not None:
                    if place.dragon.is_container:
                        if place.dragon.buffed is False:
                            place.dragon.damage *= 2
                            place.dragon.buffed = True
                        if place.dragon.contained_dragon and place.dragon.contained_dragon.buffed == False:
                            place.dragon.contained_dragon.damage *= 2
                            place.dragon.contained_dragon.buffed = True
                    else:
                        if place.dragon.buffed is False:
                            place.dragon.damage *= 2
                            place.dragon.buffed = True
                place = place.exit
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        if self.instantiated is False:
            super().reduce_armor(amount)
        else:
            self.armor -= amount
            if self.armor <= 0:
                terminators_win()
