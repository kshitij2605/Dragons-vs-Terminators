from ..fighter import Fighter

class Terminator(Fighter):
    """A Terminator moves from place to place, following exits and stinging dragons."""

    name = 'Terminator'
    damage = 1
    is_watersafe = True
    is_scared = False
    once_scared = False
    # OVERRIDE CLASS ATTRIBUTES HERE

    def sting(self, dragon):
        """Attack a Dragon, reducing its armor by 1."""
        dragon.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Terminator's current Place to a new PLACE."""
        self.place.remove_fighter(self)
        place.add_fighter(self)

    def blocked(self):
        """Return True if this Terminator cannot advance to the next Place."""
        # BEGIN 2.4
        if self.place.dragon is None or self.place.dragon.blocks_path == False:
            return False
        else:
            return True
        #return self.place.dragon is not None
        # END 2.4

    def action(self, colony):
        """A Terminator's action stings the Dragon that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        colony -- The DragonColony, used to access game state information.
        """
        ahead = self.place.exit
        behind = self.place.entrance
        # BEGIN 4.4
        if self.is_scared == False:
            if self.blocked():
                self.sting(self.place.dragon)
            elif self.armor > 0 and ahead is not None:
                self.move_to(ahead)
        elif self.is_scared == True:
            if self.blocked():
                self.sting(self.place.dragon)
            elif self.armor > 0 and behind.name is not "Skynet":
                self.move_to(behind)
        # END 4.4
