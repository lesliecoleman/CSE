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
HOLE_1 = 'You fall down a deep hole and land on a mattress. There is a path to the south.'
CAVE_1 = 'You enter a dirt cave with one torch on the floor. There is two paths to the east and north.'
BATH_1 = 'You enter the bathroom. On the shelf there is a half-eaten sandwich. There is three paths: ' \
         'East, West, and South.'
HOLE_2 = 'You fall down another deep hole and there is a path to the north-west.'
CAVE_2 = 'You are in another dirt cave. There is two paths to the south-west and south-east.'
STORAGE = 'You walk into a dim lighted storage room. In the bottom right corner, there is a cardboard box. ' \
          'It seems to be partially open.'
S_BOX = 'You are now in a steel box. There is a path to the north and one to the west.'
GRASS = 'You leave the bathroom and you are now in a grassy field. To the north and to the east there ' \
        'is a brick wall. There are two paths to the west and south.'
BARN = 'You walk through two open doors into a barn. There is two paths leading west and north. ' \
       'It appears that nothing is in the barn but you feel like there is something watching you.'
FANBATH = 'You enter a fancy bathroom. On the wall there is a mirror that is partially broken. ' \
          'There are two paths to the west and to the east.'
POOL = 'You leave the bathroom and walk onto a pool deck. Floating in the pool is another rubber duck ' \
       'wearing a fedora. There are two paths to the east and to the north-west.'
LIBRARY = 'You walk into a library full of dusty books. You look around and find 600 rubber ducks wearing ' \
          'fedoras all over the room. You need to get out either to the west or south-east.'
CLASS = 'You walk into what look likes an old classroom. Books are left all over the desks and there is ' \
        'a staircase in the back. \nThere are two paths leading out, down the staircase and to the east.'
MARSTORAGE = 'You enter a room full of seafoam green colored whiteboard markers. There is two paths up the ' \
             'staircase and down the staircase.'
LARSTORAGE = 'You enter a dim lighted storage room. You see over 3,000 tiny rubber ducks in the room ' \
             'surrounding a the largest rubber duck in the world. You see that your armor has been upgraded ' \
             'and \nyou now have a sword to fight the ducks. There is a path to the east but it is shut, and ' \
             'a path up the stairs. Defeat the duck to open the door.'
PARTY = 'You had just defeated the ducks. You walk into a party room to celebrate the win ' \
        'with all the people who live in the house. Congrats on beating the game. You did a nice job.'

m_box = Room('Metal Box', M_BOX, 'bedroom', '', '', '', '', '', '', '', '', '')
bedroom = Room('Empty Bedroom', BEDROOM, '', '', 'kitchen', 'hole', '', '', '', '', '', '')
kitchen = Room('Kitchen', KITCHEN, 'hole_2', 's_box', 'bathroom_1', 'bedroom', '', '', '', '', '', '')
hole = Room('Hole', HOLE_1, '', 'cave_1', '', '', '', '', '', '', '', '')
cave_1 = Room('Cave', CAVE_1, 'hole', '', 'm_box', '', '', '', '', '', '', '')
bathroom_1 = Room('Bathroom', BATH_1, '', 'storage_room', 'grass_field', 'kitchen', '', '', '', '', '', '')
hole_2 = Room('Hole', HOLE_2, '', '', '', '', 'cave_2', '', '', '', '', '')
cave_2 = Room('Cave', CAVE_2, '', '', '', '', '', 'hole_2', 'bedroom', '', '', '')
storage_room = Room('Storage Room', STORAGE, 'bathroom_1', '', '', '', '', '', '', '', '', '')
s_box = Room('Box', S_BOX, 'kitchen', '', '', 'm_box', '', '', '', '', '', '')
grass_field = Room('Grass Field', GRASS, '', 'barn', '', 'bathroom_1', '', '', '', '', '', '')
barn = Room('Barn', BARN, 'grass_field', '', '', 'fancy_bath', '', '', '', '', '', '')
fancy_bath = Room('Fancy Bathroom', FANBATH, '', '', 'barn', 'pool', '', '', '', '', '', '')
pool = Room('Pool', POOL, '', '', 'fancy_bath', '', 'library', '', '', '', '', '')
library = Room('Library', LIBRARY, '', '', '', 'classroom', '', 'pool', '', '', '', '')
classroom = Room('Classroom', CLASS, '', '', 'library', '', '', '', '', '', 'marker_storage', '')
marker_storage = Room('Whiteboard Marker Storage', MARSTORAGE, '', '', '', '', '', '', '', 'classroom', 'large_storage',
                      '')
large_storage = Room('Large Storage Room', LARSTORAGE, '', '', 'party', '', '', '', '', 'marker_storage', '', '')
party = Room('Party Central 101', PARTY, '', '', '', '', '', '', '', '', '' ,'')


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
