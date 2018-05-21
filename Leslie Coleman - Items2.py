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
    def __init__(self, name, eat, attack, damage, shrink, splash, spread):
        self.attack = attack
        self.damage = damage
        self.shrink = shrink
        self.splash = splash
        self.spread = spread
        super(Weapons, self).__init__(name)


class Ranged(Weapons):
    def __init__(self, name, attack, damage):
        super(Ranged, self).__init__(name, None, 20, 2, None, None, None)


class Armor(Item):
    def __init__(self, name, chestplate, helmet, boots, pants):
        self.chestplate = chestplate
        self.helmet = helmet
        self.boots = boots
        self.pants = pants
        super(Armor, self).__init__(name)


class key_items(Item):
    def __init__(self):
        super(key_items, self).__init__(key_items)

        def take(self):
            if player_inv < 15:
                print("You grab the %s" % self.name)
                player_inv.append(self)

            elif player_inv == 15:
                print("You don't have space to pick up the %s" % self.name)


class Archery(key_items):
    def __init__(self, name, attack, damage):
        super(Archery, self).__init__()
        self.attack = attack
        self.damage = damage

        def attack(self, target):
            print("%s attacks %s" % (self.name, target.name))
            target.damage()

        def damage(self):
            self.health -= 1
            if self.health >= 1:
                print("%s has %s health" % (self.name, self.health))
            else:
                self.death()


class Bow(Archery):
    def __init__(self):
        super(Bow, self).__init__('Jeffery', 40, 1)


class Sword(Weapons):
    def __init__(self):
        super(Sword, self).__init__('Thanos', False, 100, 100, False, False, False)

class Knife(Weapons):
    def __init__(self):
        super(Knife, self).__init__('Hero', False, 20, 20, False, False, False)


class Drink(Item):
    def __init__(self):
        super(Drink, self).__init__('Water')

    def drink(self):
        if self.drink:
            print("You drink the %s" % self.name)
            player_inv.remove(self)



class Other_wearables(key_items):
    def __init__(self):
        super(Other_wearables, self).__init__()


class Map(Item):
    def __init__(self, name, description):
        super(Map, self).__init__(name)

    def fast_travel(self):
        print('*******************************************************************************************************')
        print("You open the map and see some rooms that are different. There are 3 rooms that you can travel to from "
              "certain rooms, Movie Set, Basement and Pretty Garden.")
        print()
        print('The rooms that you can travel to the Movie Set, Basement, and Pretty Garden from are Metal Box, '
              'Empty Bedroom, Kitchen, Bathroom 1, Grass Field, Barn, \nFancy Bathroom, Pool, Library and Classroom. '
              'Remember that you can travel back to the room that you came from.')
        print()
        print("Where would you like to travel?")
        print('*******************************************************************************************************')
    room_dictionary = {
        'Movie Set': movieset,
        'Pretty Garden': garden,
        'Basement': basement,
                }
    teleport = input(">_")
    if teleport in room_dictionary:
        print('***************************************************************************************************')
        print("You are now in(at) the %s" % teleport)
        print('***************************************************************************************************')
        global current_node
        current_node = room_dictionary[teleport]
    else:
        print('***************************************************************************************************')
        print('Sadly that room does not exist on the map.')
        print('***************************************************************************************************')


sword = Weapons('Duck Sword', None, 20, 5, None, None, None)
shrink_ray = Weapons('Shrink Ray', None, 15, 7, True, None, None)
chestplate = Armor('Chestplate', True, None, None, None)
helmet = Armor('Helmet', None, True, None, None)
boots = Armor('Boots', None, None, True, None)
pants = Armor('Pants', None, None, None, True)
toast = Food('Jo', True)
avocado = Food('Chip', True)
plums = Food('Plums from Romania', True)
mac_n_burger = Food('Mac n\' Burger', True)

movieset = ()
garden = ()
basement = ()


player_inv = []