from .dragon import Dragon


class HarvesterDragon(Dragon):
    """HarvesterDragon produces 1 additional food per turn for the colony."""

    name = 'Harvester'
    implemented = True
    food_cost = 2

    # OVERRIDE CLASS ATTRIBUTES HERE

    def action(self, colony):
        """Produce 1 additional food for the colony.

        colony -- The DragonColony, used to access game state information.
        """
        # BEGIN 1.1
        colony.food += 1
