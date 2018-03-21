class Item(object):
    def __init__(self, name):
        self.name = name

    def take(self):
        if player_inv < 15:
            print("You grab the %s" % self.name)
            player_inv.append(self)

        elif player_inv == 15:
            print("You don't have space to pick up the %s" % self.name)


class Food(Item):
    def __init__(self, name, eat):
        self.eat = eat
        super(Food, self).__init__(name)

    def eat(self):
        if self.eat:
            print("You eat the %s. Weird." % self.name)
            player_inv.remove(self)
        else:
            print("You can not eat that. That's weird.")

        
class Weapons(Item):
    def __init__(self, name, eat, attack, damage, shrink, splash):
        self.attack = attack
        self.damage = damage
        self.shrink = shrink
        self.splash = splash
        super(Weapons, self).__init__(name)

    def attack(self):


class Ranged(Weapons):
    def __init__(self, name, attack, damage):
        super(Ranged, self).__init__(name, None, 20, 2, None, None)




player_inv = []