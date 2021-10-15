from .dragon import Dragon
import random


class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    implemented = True  # Change to True to view in the GUI
    time_to_digest = 3
    food_cost = 4
    # END 2.3

    def __init__(self, armor=1, digesting = 0):
        # BEGIN 2.3
        self.digesting = digesting
        Dragon.__init__(self, armor)
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        amount = terminator.armor
        terminator.reduce_armor(amount)
        # END 2.3

    def action(self, colony):
        # BEGIN 2.3
        if self.digesting != 0:
            self.digesting -= 1
        elif self.place.terminators:
            self.eat_terminator(random.choice(self.place.terminators))
            self.digesting = self.time_to_digest
        else:
            return None
