'''
Name
Health
Pick up items
Move?
Attack
Death
Dialogue
Perform Actions (Use, Push, etc.)
Description
Status Effect (paralyze, poison, burn, etc.)
Take Damage
'''

class Character(object):
    def __init__(self, name, health, description, dialogue, holding):
        self.name = name
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.holding = False

    def pick_up(self):
        if self.holding:
            print("Not available")
        else:
            print("You pick up the item.")
    def attack(self):
        print("You attack.")
    def death(self):
        if self.health < 0
            self.health = True
        else:
            self.health = False
    def damage(self):
        self.damage -= 1

iron_man = Character('Tony Stark', 100, "Rich man in a suit", None)
