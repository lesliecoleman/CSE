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
        if

player_inv = []