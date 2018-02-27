class Room(object):
    def __init__(self, name, description, north, south, east, west, northwest, southeast, southwest, up, down, walls):
        self.name = name
        self.description = description
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


M_BOX = 'You wake up in a metal box. There is one path to the north. You are wearing leather armor.'
BEDROOM = 'You enter what looks like a bedroom. In the upper right corner you see a person trapped in a ' \
          'cage pointing to writing on the wall saying “Don’t Trust The Ducks!” \nIn another corner you see ' \
          'a rubber duck wearing a fedora. There is a path to the west and a path to the east.'
KITCHEN = 'You are now in the kitchen. On the table in the upper left corner there is a pocket knife. ' \
          'There is four paths: West, North, South, and East.'


m_box = Room('Metal Box', M_BOX, 'bedroom', '', '', '', '', '', '', '', '', '')
bedroom = Room('Empty Bedroom', BEDROOM, '', '', 'kitchen', 'hole', '', '', '', '', '', '')
kitchen = Room('Kitchen', KITCHEN, 'hole_2', 'box', 'bathroom', 'bedroom', '', '', '', '', '', '')
hole = Room('Hole', HOLE_1, '', '', '', '', )



current_node = m_box
directions = ['north', 'south', 'west', 'east', 'northwest', 'southeast', 'up', 'down', 'southwest']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
