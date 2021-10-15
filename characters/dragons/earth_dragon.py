from .dragon import Dragon

class EarthDragon(Dragon):
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    name = "Earth"
    implemented = True
    food_cost = 4

    def __init__(self, armour = 4):
        Dragon.__init__(self, armour)
