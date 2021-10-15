from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    food_cost = 10
    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        dict = {}
        place = self.place
        count = 0
        if place.dragon and place.dragon.is_container:
            dict[place.dragon] = count
            count += 1
            place = place.entrance
        elif place.terminators:
            for i in place.terminators:
                dict[i] = count
            count += 1
            place = place.entrance
            
        while place != skynet:
            if place.dragon:
                dict[place.dragon] = count
            elif place.terminators:
                for i in place.terminators:
                    dict[i] = count
            count += 1
            place = place.entrance

        return dict
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        damage = 2 - distance*0.2 - self.fighters_shot*0.05
        if damage < 0:
            damage = 0
        return damage
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
