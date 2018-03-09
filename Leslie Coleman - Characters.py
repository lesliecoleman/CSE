# Name
# Health
# Pick up items
# Move?
# Attack
# Death
# Dialogue
# Perform Actions (Use, Push, etc.)
# Description
# Status Effect (paralyze, poison, burn, etc.)
# Take Damage


class Character(object):
    def __init__(self, name, description, dialogue, holding):
        self.name = name
        self.health = 6
        self.description = description
        self.dialogue = dialogue
        self.holding = holding
        self.dead = False

    def pick_up(self):
        if self.holding:
            print("You can not pick up this item at this time. Please try again later. Thank you.")
        else:
            print("You pick up the item.")

    def attack(self, target):
        print("%s attacks %s" % (self.name, target.name))
        target.damage()

    def death(self):
        if self.health <= 0:
            self.dead = True
            print("%s is dead." % self.name)

    def damage(self):
        self.health -= 1
        if self.health >= 1:
            print("%s has %s health" % (self.name, self.health))
        else:
            self.death()


print("I present to you Civil War")
cap_america = Character('Steve Rogers', 'Large man in a colorful suit holding a round shield.', None, None)
iron_man = Character('Tony Stark', "Rich man in a suit. (Might also be Batman in disguise.)", None, None)
print(cap_america.description)
print(iron_man.description)
iron_man.attack(cap_america)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
cap_america.attack(iron_man)
iron_man.attack(cap_america)
