from .thrower_dragon import ThrowerDragon
from utils import make_scare, apply_effect

class ScaryThrower(ThrowerDragon):
    """ThrowerDragon that intimidates Terminators, making them back away instead of advancing."""

    name = 'Scary'
    # BEGIN 4.4
    implemented = True  # Change to True to view in the GUI
    food_cost = 6
    # END 4.4

    def throw_at(self, target):
        # BEGIN 4.4
        if target:
            apply_effect(make_scare, target, 2)
        # END 4.4
