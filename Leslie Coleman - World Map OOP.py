class Room(object):
    def __init__(self, name, description, north, walls, south, east, west, northwest, southeast, southwest, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.walls = walls
        self.south = south
        self.east = east
        self.west = west
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


m_box = Room()


current_node = m_box
directions = ['north', 'south', 'west', 'east', 'northwest', 'southeast', 'up', 'down', 'southwest']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = m_box[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
