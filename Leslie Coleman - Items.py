class item(object):
    def __init__(self, weapons, consumable, armor):
        self.weapons = weapons
        self.consumable = consumable
        self.armor = armor

    def pick_up(self):
        