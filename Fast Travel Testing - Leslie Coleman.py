class Item(object):
    def __init__(self, name):
        self.name = name

    def take(self):
        if len(player_inv) < 15:
            print("You grab the %s" % self.name)
            player_inv.append(self)

        elif len(player_inv) == 15:
            print("You don't have space to pick up the %s" % self.name)

class KeyItem(Item):
    def __init__(self, name):
        super(KeyItem, self).__init__(name)

    def take(self):
        if len(player_inv) < 15:
            print("You grab the %s" % self.name)
            player_inv.append(self)


class Map(KeyItem):
    def __init__(self, name, description, location):
        super(Map, self).__init__(name)

    def fast_travel(self):
        print("You open the map and see some rooms that are different. There are 2 rooms, Movie Set and Basement"
              "")
        print("Where would you like to travel?")
        room_dictionary = {
            'Movie Set': movieset,
            'Basement': basement
        }
        teleport = input(">_")
        if teleport in room_dictionary:
            print("You are now in(at)the %s " % teleport)
            global current_node
            current_node = room_dictionary[teleport]
        else:
            print('Sadly that room does not exist on the map.')


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


LISTOFCOMMANDS = 'North, South, East, West, Northwest, Southeast, Southwest, Up, Down, Look, Quit, Party, Travel'
M_BOX = 'You wake up in a metal box. There is one path to the north. \nYou are wearing leather armor.'
MOVIESET = 'You enter what looks like a movie set. You close your eyes and see the filming of your favorite movie.'
BASEMENT = 'Hey!!! It\'s a basement!!!!'
PARTY = 'You had just defeated the ducks. You walk into a party room to celebrate the win ' \
        '\nwith all the people who live in the house. Congrats on beating the game. You did a nice job.'
M_BOX2 = 'You are back in the metal box. Remember there is a path to the north'


m_box = Room('Metal Box', M_BOX, M_BOX2, 'bedroom', '', '', '', '', '', '', '', '', '')
party = Room('Party Central 101', PARTY, '', '', '', '', '', '', '', '', '', '', '')
movieset = Room('Movie Set', MOVIESET, '', '', '', '', '', '', '', '', '', '', '')
basement = Room('Basement', BASEMENT, '', '', '', '', '', '', '', '', '', '', '')


travel_map = Map('Piece of paper', 'You find a map and rooms that you have not seen are on there. You can travel '
                                   'to the rooms by saying travel and then where you want to go.', '')

current_node = m_box

directions = ['north', 'south', 'west', 'east', 'northwest', 'southeast', 'southwest', 'up', 'down']
short_directions = ['n', 's', 'w', 'e', 'nw', 'se', 'sw', 'u', 'd']
is_playing = True
print(LISTOFCOMMANDS)


while is_playing:
    # Rom information
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
    else:
        print("That command is not available. Please try again. Thank You.")

    # Handling win conditions
    if current_node == party:
        print(current_node.name)
        print(current_node.description)
        is_playing = False

player_inv = []
key_inv = [travel_map]
