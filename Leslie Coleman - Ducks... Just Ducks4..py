class Item(object):
    def __init__(self, name):
        self.name = name

    def take(self, player, room):
        if len(player.inventory) < 15:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("You grab the %s" % self.name)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            player.inventory.append(self)
            room.inventory.remove(self)

        elif len(player.inventory) == 15:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("You don't have space to pick up the %s" % self.name)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def dropped(self, player, room):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You drop the item')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        player.inventory.remove(self)
        room.inventory.append(self)

class Food(Item):
    def __init__(self, name, eat):
        self.eat = eat
        super(Food, self).__init__(name)

    def eat(self):
        if self.eat:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("You eat the %s. Weird." % self.name)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            player.inventory.remove(self)
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("You can not eat that. That's weird.")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


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
            if player.inventory < 15:
                print("You grab the %s" % self.name)
                player.inventory.append(self)

            elif player.inventory == 15:
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
            player.inventory.remove(self)


class Other_wearables(key_items):
    def __init__(self):
        super(Other_wearables, self).__init__()


class Map(Item):
    def __init__(self, name, description):
        super(Map, self).__init__(name)
        
    def fast_travel(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("You open the map and see some rooms that are different. \nThere are 3 rooms that you can travel to from "
              "certain rooms, Movie Set, Basement and Pretty Garden.")
        print()
        print('The rooms that you can travel to the Movie Set, Basement, and Pretty Garden from are Metal Box, '
              '\nEmpty Bedroom, Kitchen, Bathroom 1, Grass Field, Barn, Fancy Bathroom, Pool, Library and Classroom. '
              '\nRemember that you can travel back to the room that you came from.')
        print()
        print("Where would you like to travel?")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        room_dictionary = {
            'Movie Set': movieset,
            'Pretty Garden': garden,
            'Basement': basement,
            'Metal Box': m_box,
            'Empty Bedroom': bedroom,
            'Kitchen': kitchen,
            'Bathroom 1': bathroom_1,
            'Grass Field': grass_field,
            'Barn': barn,
            'Fancy Bathroom': fancy_bath,
            'Pool': pool,
            'Library': library,
            'Classroom': classroom
        }
        teleport = input(">_")
        if teleport in room_dictionary:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("You are now in(at) the %s" % teleport)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            global current_node
            current_node = room_dictionary[teleport]
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Sadly that room does not exist on the map.')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


sword = Sword()
shrink_ray = Weapons('Shrink Ray', None, 15, 7, True, None, None)
chestplate = Armor('Chestplate', True, None, None, None)
helmet = Armor('Helmet', None, True, None, None)
boots = Armor('Boots', None, None, True, None)
pants = Armor('Pants', None, None, None, True)
toast = Food('Jo', True)
avocado = Food('Chip', True)
avocado2 = Food('Another Avocado', True)
plums = Food('Plums from Romania', True)
mac_n_burger = Food('Mac n\' Burger', True)
half_eaten_sandwich = Food('Old sandwich', True)


class Character(object):
    def __init__(self, name, description, dialogue, damage, attack,  holding, items=None):
        self.name = name
        self.health = 60
        self.description = description
        self.dialogue = dialogue
        self.holding = holding
        self.inventory = items
        self.dead = False
        self.damage = damage
        self.attack = attack

    def pick_up(self, item, room):
        if self.pick_up(stuff, current_node):
            print("You can not pick up this item at this time. Please try again later. Thank you.")
        else:
            item.take(self, room)

    def drop(self, item, room):
        if not self.pick_up(stuff, current_node):
            print("You can't drop the item.")
        else:
            item.dropped(self, room)

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


Giant_Duck = Character('Giant Duck', 'A giant duck that you need to defeat. (Might also be someone you know)', '', '',
                       '', '', [])
Mr_Wybe = Character('Mr. Wybe', 'HYDRA Agent, Your Father, and a completely horrible parent.', '', '', '',
                    '', [])
player = Character('Mister Sir Man', 'Loving kid, smart, and adventurous.', '', '', '', '', [])
bucky = Character('Bucky Barnes', 'Your best friend and would protect you from anything.', '"Would you like some '
                                                                                           'plums. I don\'t mind it '
                                                                                           'you take some."', '', '',
                                                                                           '', [plums])


class Room(object):
    def __init__(self, name, description, description2, north, south, east, west, northwest, southeast, southwest, up,
                 down, walls, items=None):
        self.name = name
        self.description = description
        self.description2 = description2
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.up = up
        self.down = down
        self.walls = walls
        self.inventory = items
        self.visited = False

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


BACKSTORY = 'You are heading over to your Uncle Wiebe\'s house with your dad, Mr. Wybe, and your older brother, ' \
            'Wiebe "The Duck" Wybe. "How ya doing sis?" said Wiebe. \n"Good. Dad\'s music is annoying tho." you said. '\
            '"It is not!" yelled. Mr. Wybe. You pull up to your Uncle\'s house and enter in. A hour later your dad ' \
            'and uncle get into a fight. \nYour dad left and took your brother with him and you never saw them again.'
LISTOFCOMMANDS = 'North, South, East, West, Northwest, Southeast, Southwest, Up, Down, \nLook, Quit, Party, Travel, ' \
                 'Inventory, Commands'
SHORTDIRECTIONS = 'n, s, w, e, nw, se, sw, u, d'
GARDEN = 'You step into a garden just outside of the mansion, but fenced into its own secluded area. \n' \
         'The air is filled with the sweet smell of nectar and despite the apparent age of the garden, \nthe flowers ' \
         'are thriving with splashed of magnificent, vibrant, glorious colors.'
M_BOX = 'You wake up in a metal box. There is one path to the north. \nYou are wearing leather armor.'
M_BOX2 = 'You are back in the metal box. Remember there is a path to the north'
BEDROOM = 'You enter what looks like a bedroom. \nIn the upper right corner you see Sam Wilson trapped in a ' \
          'cage, muttering something about ducks. \nIn another corner you see a rubber duck wearing a fedora. ' \
          '\nThere is a path to the west and a path to the east.'
BEDROOM2 = 'You are back in the bedroom. Remember "Don’t Trust The Ducks!" \nThere is a path to the east and west'
KITCHEN = 'You are now in the kitchen. On the table in the upper left corner there is a pocket knife. ' \
          '\nThere is four paths: West, North, South, and East. Also you see a very familiar person in the corner.'
KITCHEN2 = 'Welcome back to the kitchen. You see Wanda Maximoff cooking with Vision. Go either north, south, east, ' \
           'or west'
HOLE_1 = 'You fall down a deep hole and land on a mattress. There is a path to the south.'
HOLE_1_2 = 'You are back in the hole. There is a path to the south'
CAVE_1 = 'You enter a dirt cave with one torch on the floor. There is two paths to the east and north.'
CAVE_1_2 = 'You re-enter a dirt cave with one torch on the floor. There is two paths to the east and north.'
BATH_1 = 'You enter the bathroom. On the shelf there is a half-eaten sandwich. \nThor has been here because you see ' \
         'the damage of his fight with Loki. \nThere is three paths: East, West, and South.'
BATH_1_2 = 'Welcome to bathroom. Paths to the west, east, and south'
HOLE_2 = 'You fall down another deep hole and there is a path to the northwest.'
HOLE_2_2 = 'You are back in the deep hole and there is a path to the northwest.'
CAVE_2 = 'You are in another dirt cave. There is two paths to the southwest and southeast.'
CAVE_2_2 = 'You re-enter the dirt cave. There is two paths to the southwest and southeast.'
STORAGE = 'You walk into a dim lighted storage room. In the bottom right corner, \nthere is a cardboard box. ' \
          'It seems to be partially open. There is a path to the north. There is an avocado here.'
STORAGE2 = 'There is still a box in the corner of the room. There is a path to the north.'
S_BOX = 'You are now in a steel box. There is a path to the north and one to the west.'
GRASS = 'You leave the bathroom and you are now in a grassy field. To the north and to the east \nthere ' \
        'is a brick wall. There are two paths to the west and south. \nAlso you see Tony Stark working on something ' \
        'in the corner'
GRASS2 = 'You are now back in the grass field. Paths to the west and south.'
BARN = 'You walk through two open doors into a barn. There is two paths leading west and north. ' \
       '\nIt appears that nothing is in the barn but you feel like there is something watching you. \nIt\'s probably ' \
       'just Clint Barton'
BARN2 = 'There is still something watching you. " You need to get out, ASAP!" yelled Natasha Romanoff. \nHurry to ' \
        'the west or north!!'
FANBATH = 'You enter a fancy bathroom. On the wall there is a mirror that is partially broken. ' \
          '\nThere are two paths to the west and to the east.'
FANBATH2 = 'Welcome back to the fancy bathroom. Please exit to the west or east.'
POOL = 'You leave the bathroom and walk onto a pool deck. Floating in the pool is another rubber duck ' \
       '\nwearing a fedora. There are two paths to the east and to the northwest.'
POOL2 = 'Welcome back. Sadly the pool is closed. Please leave to the east or northwest.'
LIBRARY = 'You walk into a library full of dusty books. You look around and find 600 rubber ducks \nwearing ' \
          'fedoras all over the room. You need to get out either to the west, southeast, or north.'
LIBRARY2 = 'AHCHOO! The ducks are moving! Get out to the west, southeast, or north!'
CLASS = 'You walk into what look likes an old classroom. \nBooks are left all over the desks and there is ' \
        'a staircase in the back. \nThere are two paths leading out, down the staircase and to the east.'
CLASS2 = 'Welcome to class. Please leave before Steve Rogers comes back. Head out to the east or go downstairs.'
MARSTORAGE = 'You enter a room full of seafoam green colored whiteboard markers. \nThere is two paths up the ' \
             'staircase and down the staircase.'
MARSTORAGE2 = 'The markers are still there. Go upstairs or downstairs.'
LARSTORAGE = 'You enter a dim lighted storage room. You see over 3,000 tiny rubber ducks in the room ' \
             '\nsurrounding a the largest rubber duck in the world. You see that your armor has been upgraded ' \
             '\nand you now have a sword to fight the ducks. \nThere is a path to the east but it is shut, and ' \
             'a path up the stairs. \nDefeat the duck to open the door.'
LARSTORAGE2 = 'You are back. Not quite sure if you have defeated the ducks yet. Have fun I guess... :('
PARTY = 'You had just defeated the ducks. You walk into a party room to celebrate the win ' \
        '\nwith all the people who live in the house and Bruce Banner. Congrats on beating the game. You did a nice ' \
        'job.'
MOVIESET = 'You enter what looks like a movie set. You close your eyes and see the filming of your favorite movie.'
BASEMENT = 'Hey!!! It\'s a basement!!!! And Loki is here!!!! Probably hiding from Thor. Go up and discover a secret. ' \
           '\nLike Bucky said, he doesn\'t mind sharing his plums. Take some if you want.'
COMPOUND = 'WOW! It\'s the Avengers Compound. That\'s where they came from. Go down to head back to the basement. ' \
           '\nPepper Pots is walking around trying to figure out where everyone went.'


m_box = Room('Metal Box', M_BOX, M_BOX2, 'bedroom', '', '', '', '', '', '', '', '', '')
bedroom = Room('Empty Bedroom', BEDROOM, BEDROOM2, '', '', 'kitchen', 'hole', '', '', '', '', '', '', [chestplate,
                                                                                                       boots, pants,
                                                                                                       helmet])
kitchen = Room('Kitchen', KITCHEN, KITCHEN2, 'hole_2', 's_box', 'bathroom_1', 'bedroom', '', '', '', '', '', '')
hole = Room('Hole', HOLE_1, '', '', 'cave_1', '', '', '', '', '', '', '', '')
cave_1 = Room('Cave', CAVE_1, '', 'hole', '', 'm_box', '', '', '', '', '', '', '')
bathroom_1 = Room('Bathroom', BATH_1, BATH_1_2, '', 'storage_room', 'grass_field', 'kitchen', '', '', '', '', '', '')
hole_2 = Room('Hole', HOLE_2, '', '', '', '', '', 'cave_2', '', '', '', '', '')
cave_2 = Room('Cave', CAVE_2, '', '', '', '', '', '', 'hole_2', 'bedroom', '', '', '')
storage_room = Room('Storage Room', STORAGE, STORAGE2, 'bathroom_1', '', '', '', '', '', '', '', '', '', [avocado])
s_box = Room('Box', S_BOX, '', 'kitchen', '', '', 'm_box', '', '', '', '', '', '')
grass_field = Room('Grass Field', GRASS, GRASS2, '', 'barn', '', 'bathroom_1', '', '', '', '', '', '')
barn = Room('Barn', BARN, BARN2, 'grass_field', '', '', 'fancy_bath', '', '', '', '', '', '')
fancy_bath = Room('Fancy Bathroom', FANBATH, FANBATH2, '', '', 'barn', 'pool', '', '', '', '', '', '', [mac_n_burger])
pool = Room('Pool', POOL, POOL2, '', '', 'fancy_bath', '', 'library', '', '', '', '', '', [avocado2])
library = Room('Library', LIBRARY, LIBRARY2, 'm_box', '', '', 'classroom', '', 'pool', '', '', '', '')
classroom = Room('Classroom', CLASS, CLASS2, '', '', 'library', '', '', '', '', '', 'marker_storage', '')
marker_storage = Room('Whiteboard Marker Storage', MARSTORAGE, MARSTORAGE2, '', '', '', '', '', '', '', 'classroom',
                      'large_storage', '', [sword])
large_storage = Room('Large Storage Room', LARSTORAGE, LARSTORAGE2, '', '', 'party', '', '', '', '', 'marker_storage',
                     '', '')
party = Room('Party Central 101', PARTY, '', '', '', '', '', '', '', '', '', '', '')
movieset = Room('Movie Set', MOVIESET, '', '', '', '', '', '', '', '', '', '', '')
basement = Room('Basement', BASEMENT, '', '', '', '', '', '', '', '', 'avengers_compound', '', '', [plums])
avengers_compound = Room('Avengers compound', COMPOUND, '', '', '', '', '', '', '', '', '', 'basement', '')
garden = Room('Pretty Garden', GARDEN, '', '', '', '', '', '', '', '', '', '', '', [toast])


travel_map = Map('Travel Map', 'You find a map and rooms that you have not seen are on there. You can travel to the '
                               'rooms by saying travel and then where you want to go.')
info = 'I do not own any Marvel Characters mentioned.'

current_node = m_box
directions = ['north', 'south', 'west', 'east', 'northwest', 'southeast', 'southwest', 'up', 'down']
short_directions = ['n', 's', 'w', 'e', 'nw', 'se', 'sw', 'u', 'd']
is_playing = True

response = 'Leslie likes eating Blueberries'
while response not in ['yes', 'no']:
    response = input('Would you like instructions? yes/no')
    if response.lower() == 'yes':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
              '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("Welcome. Here is some basic information."
              "\nBelow is a list of commands and directions. You also have short directions."
              "\nCommands:"
              "\nLook, Quit, Party, Travel, Inventory, Commands, Help."
              "\nDirections:"
              "\nNorth, South, East, West, Northwest, Southeast, Southwest, Up, Down."
              "\nShort Directions:"
              "\nn, s, e, w, nw, se, sw, u, d."
              "\nLook allows you to see a description for a room if you have already visited it."
              "\nQuit allows you to end the game."
              "\nParty gives you a sentence."
              "\nTravel allows you to travel to different rooms, some that are special."
              "'\nInventory allows you to see your inventory."
              "\nCommands allows you to see the commands at any point in the game."
              "\nHelp allows you to get certain information during the game."
              "\nHave a grand adventure. Be warned, what lies ahead is something you didn't expect.")
    elif response.lower() == 'no':
        print("Have a grand adventure. Be warned, what lies ahead is something you didn't expect.")
    else:
        print('Thanos demands you to answer the question.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(BACKSTORY)
print()
print('If you want to travel, make sure the room you are traveling to starts with a capital letter. For example: '
      '"Where would you like to travel?" ">_Basement"')
print()
print(info)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Let\'s begin our adventure...')
player.inventory = [travel_map]


while is_playing:
    # Rom information
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(current_node.name)
    if not current_node.visited:
        print(current_node.description)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # Input
    print("If you need a list of commands, you can type 'Commands'")
    print("If you need help, just type 'help'")
    command = input('>_').lower().strip()

    # Pre-processing
    if command == 'quit':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('I am sorry this was hard. I wish you would continue.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        exit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Process input
    if command == 'party':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Sorry you can not party yet. Beat the ducks and then you can celebrate adventurer.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    elif command[:7] == 'pick up':
        item = command[8:]
        for stuff in current_node.inventory:
            if item == stuff.name:
                player.pick_up(stuff, current_node)
    elif command[:4] == 'drop':
        item = command[5:]
        for stuff in current_node.inventory:
            if item == stuff.name:
                player.drop(stuff, current_node)
    elif command == 'inventory':
        for item in player.inventory:
            print(item.name)
    elif command in directions:
        try:
            current_node.visited = True
            current_node.move(command)
        except KeyError:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("This way is not available. Please try again. Thank You")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    elif command == 'travel':
        travel_map.fast_travel()
    elif command == 'look':
        print(current_node.name)
        print(current_node.description2)
    elif command == 'commands':
        print(LISTOFCOMMANDS)
    elif command == 'help':
        print('If you want to travel, make sure the room you are traveling to starts with a capital letter. '
              '\nFor example: "Where would you like to travel?" ">_Basement"')
        print('If you need a description for your room, you can always type "look"')
        print('Quit allows you to end the game where you are.')
    else:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("That command is not available. Please try again. Thank You.")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if current_node == basement:
        print(bucky.name)
        print(bucky.dialogue)
    # Handling win conditions
    if current_node == party:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(current_node.name)
        print(current_node.description)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        is_playing = False
