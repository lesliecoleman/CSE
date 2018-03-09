class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take(self):
        print("You take the %s" % self.name)


class Weapon(Item):
    def __init__(self, name, damage, description):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


sandwich = Item('Half-Eaten Sandwich', 'You find a half-eaten sandwich in the bathroom')
sandwich.take()
