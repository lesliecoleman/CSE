class Item(object):
    def __init__(self, name):
        self.name = name

    def take(self):
        if len(player_inv) < 15:
            print("You grab the %s" % self.name)
            player_inv.append(self)

        elif len(player_inv) == 15:
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


sword = Weapons('Duck Sword', None, 20, 5, None, None, None)
shrink_ray = Weapons('Shrink Ray', None, 15, 7, True, None, None)
chestplate = Armor('Chestplate', True, None, None, None)
helmet = Armor('Helmet', None, True, None, None)
boots = Armor('Boots', None, None, True, None)
pants = Armor('Pants', None, None, None, True)


class Map(Item):
    def __init__(self, name, description, location):
        super(Map, self).__init__(name)
        
    def fast_travel(self):
        print("You open the map and see some rooms that are different. There are 3 rooms that you can travel to from "
              "certain rooms, Movie Set, Basement and Pretty Garden.")
        print()
        print('The rooms that you can travel to the Movie Set, Basement, and Pretty Garden from are Metal Box, '
              'Empty Bedroom, Kitchen, Bathroom 1, Grass Field, Barn, \nFancy Bathroom, Pool, Library and Classroom. '
              'Remember that you can travel back to the room that you came from.')
        print()
        print("Where would you like to travel?")
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
            print("You are now in(at) the %s" % teleport)
            global current_node
            current_node = room_dictionary[teleport]
        else:
            print('Sadly that room does not exist on the map.')


class Character(object):
    def __init__(self, name, description, dialogue, dialogue_2, dialogue_3, holding):
        self.name = name
        self.health = 60
        self.description = description
        self.dialogue = dialogue
        self.dialogue = dialogue_2
        self.dialogue = dialogue_3
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


Giant_Duck = Character('Giant Duck', 'A giant duck that you need to defeat. (Might also be someone you know)', '', '',
                       '', '')
Mr_Wybe = Character('Mr. Wybe', 'HYDRA Agent, Your Father, and a completely horrible parent.', '', '', '', '')
Sam = Character('Sam Wilson', 'AKA "Falcon"', '"Look at the wall... Don\'t trust the ducks!" says Sam.', '', '', '')
player = Character('Mister Sir Man', 'Loving kid, smart, and adventurous.', '', '', '', '')


class Room(object):
    def __init__(self, name, description, description2, north, south, east, west, northwest, southeast, southwest, up,
                 down, walls):
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
        self.visited = False

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


BACKSTORY = 'You are heading over to your Uncle Wiebe\'s house with your dad, Mr. Wybe, and your older brother, ' \
            'Wiebe "The Duck" Wybe. "How ya doing sis?" said Wiebe. \n"Good. Dad\'s music is annoying tho." you said. '\
            '"It is not!" yelled. Mr. Wybe. You pull up to your Uncle\'s house and enter in. A hour later your dad ' \
            'and uncle get into a fight. \nYour dad left and took your brother with him and you never saw them again.'
LISTOFCOMMANDS = 'North, South, East, West, Northwest, Southeast, Southwest, Up, Down, Look, Quit, Party, Travel, ' \
                 'Inventory, Commands'
GARDEN = 'You step into a garden just outside of the mansion, but fenced into its own secluded area. \n' \
         'The air is filled with the sweet smell of nectar and despite the apparent age of the garden, the flowers ' \
         'are thriving with splashed of magnificent, vibrant, glorious colors.'
M_BOX = 'You wake up in a metal box. There is one path to the north. \nYou are wearing leather armor.'
M_BOX2 = 'You are back in the metal box. Remember there is a path to the north'
BEDROOM = 'You enter what looks like a bedroom. \nIn the upper right corner you see Sam Wilson trapped in a ' \
          'cage. In another corner you see a rubber duck wearing a fedora. \nThere is a path to the west and a ' \
          'path to the east.'
BEDROOM2 = 'You are back in the bedroom. Remember "Don’t Trust The Ducks!" \nThere is a path to the east and west'
KITCHEN = 'You are now in the kitchen. On the table in the upper left corner there is a pocket knife. ' \
          '\nThere is four paths: West, North, South, and East. Also you see a very familiar person in the corner.'
KITCHEN2 = 'Welcome back to the kitchen. Go either north, south, east, or west'
HOLE_1 = 'You fall down a deep hole and land on a mattress. There is a path to the south.'
HOLE_1_2 = 'You are back in the hole. There is a path to the south'
CAVE_1 = 'You enter a dirt cave with one torch on the floor. There is two paths to the east and north.'
CAVE_1_2 = 'You re-enter a dirt cave with one torch on the floor. There is two paths to the east and north.'
BATH_1 = 'You enter the bathroom. On the shelf there is a half-eaten sandwich. There is also a bar of soap that ' \
         'looks like someone took a bite of, courtesy of Thor \nThere is three paths: East, West, and South.'
BATH_1_2 = 'Welcome to bathroom. Paths to the west, east, and south'
HOLE_2 = 'You fall down another deep hole and there is a path to the northwest.'
HOLE_2_2 = 'You are back in the deep hole and there is a path to the northwest.'
CAVE_2 = 'You are in another dirt cave. There is two paths to the southwest and southeast.'
CAVE_2_2 = 'You re-enter the dirt cave. There is two paths to the southwest and southeast.'
STORAGE = 'You walk into a dim lighted storage room. In the bottom right corner, \nthere is a cardboard box. ' \
          'It seems to be partially open. There is a path to the north.'
STORAGE2 = 'There is still a box in the corner of the room. There is a path to the north.'
S_BOX = 'You are now in a steel box. There is a path to the north and one to the west.'
GRASS = 'You leave the bathroom and you are now in a grassy field. To the north and to the east \nthere ' \
        'is a brick wall. There are two paths to the west and south. Also you see Tony Stark working on something in ' \
        'the corner'
GRASS2 = 'You are now back in the grass field. Paths to the west and south.'
BARN = 'You walk through two open doors into a barn. There is two paths leading west and north. ' \
       '\nIt appears that nothing is in the barn but you feel like there is something watching you. It\'s probably ' \
       'just Clint Barton'
BARN2 = 'There is still something watching you. " You need to get out, ASAP!" yelled Natasha Romanoff. Hurry to the ' \
        'west or north!!'
FANBATH = 'You enter a fancy bathroom. On the wall there is a mirror that is partially broken. ' \
          '\nThere are two paths to the west and to the east.'
FANBATH2 = 'Welcome back to the fancy bathroom. Please exit to the west or east.'
POOL = 'You leave the bathroom and walk onto a pool deck. Floating in the pool is another rubber duck ' \
       '\nwearing a fedora. There are two paths to the east and to the northwest.'
POOL2 = 'Welcome back. Sadly the pool is closed. *From a distance* "No it\'s not!" yelled Bucky Barnes Please leave ' \
        'to the east or northwest.'
LIBRARY = 'You walk into a library full of dusty books. You look around and find 600 rubber ducks \nwearing ' \
          'fedoras all over the room. You need to get out either to the west, southeast, or north.'
LIBRARY2 = 'AHCHOO! The ducks are moving! Get out to the west, southeast, or north!'
CLASS = 'You walk into what look likes an old classroom. Books are left all over the desks and there is ' \
        'a staircase in the back. \nThere are two paths leading out, down the staircase and to the east.'
CLASS2 = 'Welcome to class. Please leave before Steve Rogers comes back. Head out to the east or go downstairs.'
MARSTORAGE = 'You enter a room full of seafoam green colored whiteboard markers. \nThere is two paths up the ' \
             'staircase and down the staircase.'
MARSTORAGE2 = 'The markers are still there. Go upstairs or downstairs.'
LARSTORAGE = 'You enter a dim lighted storage room. You see over 3,000 tiny rubber ducks in the room ' \
             '\nsurrounding a the largest rubber duck in the world. You see that your armor has been upgraded ' \
             '\nand you now have a sword to fight the ducks. There is a path to the east but it is shut, and ' \
             'a path up the stairs. \nDefeat the duck to open the door.'
LARSTORAGE2 = 'You are back. Not quite sure if you have defeated the ducks yet. Have fun I guess... :('
PARTY = 'You had just defeated the ducks. You walk into a party room to celebrate the win ' \
        '\nwith all the people who live in the house and Bruce Banner. Congrats on beating the game. You did a nice ' \
        'job.'
MOVIESET = 'You enter what looks like a movie set. You close your eyes and see the filming of your favorite movie.'
BASEMENT = 'Hey!!! It\'s a basement!!!! And Loki is here!!!! Go up and discover a secret.'
TOWER = 'WOW! It\'s the Avengers Tower. That\'s where they came from. Go down to head back to the basement. Pepper ' \
        'Pots is walking around trying to figure out where everyone went.'


m_box = Room('Metal Box', M_BOX, M_BOX2, 'bedroom', '', '', '', '', '', '', '', '', '')
bedroom = Room('Empty Bedroom', BEDROOM, BEDROOM2, '', '', 'kitchen', 'hole', '', '', '', '', '', '')
kitchen = Room('Kitchen', KITCHEN, KITCHEN2, 'hole_2', 's_box', 'bathroom_1', 'bedroom', '', '', '', '', '', '')
hole = Room('Hole', HOLE_1, '', '', 'cave_1', '', '', '', '', '', '', '', '')
cave_1 = Room('Cave', CAVE_1, '', 'hole', '', 'm_box', '', '', '', '', '', '', '')
bathroom_1 = Room('Bathroom', BATH_1, BATH_1_2, '', 'storage_room', 'grass_field', 'kitchen', '', '', '', '', '', '')
hole_2 = Room('Hole', HOLE_2, '', '', '', '', '', 'cave_2', '', '', '', '', '')
cave_2 = Room('Cave', CAVE_2, '', '', '', '', '', '', 'hole_2', 'bedroom', '', '', '')
storage_room = Room('Storage Room', STORAGE, STORAGE2, 'bathroom_1', '', '', '', '', '', '', '', '', '')
s_box = Room('Box', S_BOX, '', 'kitchen', '', '', 'm_box', '', '', '', '', '', '')
grass_field = Room('Grass Field', GRASS, GRASS2, '', 'barn', '', 'bathroom_1', '', '', '', '', '', '')
barn = Room('Barn', BARN, BARN2, 'grass_field', '', '', 'fancy_bath', '', '', '', '', '', '')
fancy_bath = Room('Fancy Bathroom', FANBATH, FANBATH2, '', '', 'barn', 'pool', '', '', '', '', '', '')
pool = Room('Pool', POOL, POOL2, '', '', 'fancy_bath', '', 'library', '', '', '', '', '')
library = Room('Library', LIBRARY, LIBRARY2, 'm_box', '', '', 'classroom', '', 'pool', '', '', '', '')
classroom = Room('Classroom', CLASS, CLASS2, '', '', 'library', '', '', '', '', '', 'marker_storage', '')
marker_storage = Room('Whiteboard Marker Storage', MARSTORAGE, MARSTORAGE2, '', '', '', '', '', '', '', 'classroom',
                      'large_storage', '')
large_storage = Room('Large Storage Room', LARSTORAGE, LARSTORAGE2, '', '', 'party', '', '', '', '', 'marker_storage',
                     '', '')
party = Room('Party Central 101', PARTY, '', '', '', '', '', '', '', '', '', '', '')
movieset = Room('Movie Set', MOVIESET, '', '', '', '', '', '', '', '', '', '', '')
basement = Room('Basement', BASEMENT, '', '', '', '', '', '', '', '', 'avengers_tower', '', '')
avengers_tower = Room('Avengers Tower', TOWER, '', '', '', '', '', '', '', '', '', 'basement', '')
garden = Room('Pretty Garden', GARDEN, '', '', '', '', '', '', '', '', '', '', '')


travel_map = Map('Travel Map', 'You find a map and rooms that you have not seen are on there. You can travel to the '
                               'rooms by saying travel and then where you want to go.', '')
info = 'I do not own any Marvel Characters mentioned.'

current_node = m_box
directions = ['north', 'south', 'west', 'east', 'northwest', 'southeast', 'southwest', 'up', 'down']
short_directions = ['n', 's', 'w', 'e', 'nw', 'se', 'sw', 'u', 'd']
is_playing = True
print(LISTOFCOMMANDS)
print()
print(BACKSTORY)
print()
print(info)

player_inv = [travel_map]


while is_playing:
    # Rom information
    print()
    print(current_node.name)
    if not current_node.visited:
        print(current_node.description)

    # Input
    command = input('>_').lower().strip()

    # Pre-processing
    if command == 'quit':
        print('I am sorry this was hard. I wish you would continue.')
        exit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    # Process input
    if command == 'party':
        print('Sorry you can not party yet. Beat the ducks and then you can celebrate brave adventurer.')
    elif command == 'inventory':
        for item in player_inv:
            print()
            print(item.name)
    elif command in directions:
        try:
            current_node.visited = True
            current_node.move(command)
        except KeyError:
            print("This way is not available. Please try again. Thank You")
    elif command == 'travel':
        travel_map.fast_travel()
    elif command == 'look':
        print(current_node.name)
        print(current_node.description2)
    elif command == 'commands':
        print(LISTOFCOMMANDS)
    else:
        print("That command is not available. Please try again. Thank You.")
    if current_node == bedroom:
        print(Sam.dialogue)

    # Handling win conditions
    if current_node == party:
        print(current_node.name)
        print(current_node.description)
        is_playing = False
