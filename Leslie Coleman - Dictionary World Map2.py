world_map = {
    'M_BOX': {
        'NAME': 'Metal Box',
        'DESCRIPTION': 'You wake up in a metal box. There is one path to the north. You are wearing leather armor.',
        'PATHS': {
            'NORTH': 'BEDROOM'
        }
    },
    'BEDROOM': {
        'NAME': 'Empty Bedroom',
        'DESCRIPTION': 'You enter what looks like a bedroom. In the upper right corner you see a person trapped in a '
                    'cage pointing to writing on the wall saying “Don’t Trust The Ducks!” \nIn another corner you see '
                    'a rubber duck wearing a fedora. There is a path to the west and a path to the east.',
        'PATHS': {
            'WEST': 'HOLE_1',
            'EAST': 'KITCHEN'
        }
    },
    'HOLE_1': {
        'NAME': 'Hole',
        'DESCRIPTION': 'You fall down a deep hole and land on a mattress. There is a path to the south.',
        'PATHS': {
            'SOUTH': 'CAVE_1'
        }
    },
    'CAVE_1': {
        'NAME': 'Cave',
        'DESCRIPTION': 'You enter a dirt cave with one torch on the floor. There is two paths to the east and north.',
        'PATHS': {
            'EAST': 'M_BOX',
            'NORTH': 'HOLE_1'
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'You are now in the kitchen. On the table in the upper left corner there is a pocket knife. '
                       'There is four paths: West, North, South, and East.',
        'PATHS': {
            'WEST': 'BEDROOM',
            'NORTH': 'HOLE_2',
            'SOUTH': 'S_BOX',
            'EAST': 'BATHROOM_1'
        }
    },
    'HOLE_2': {
        'NAME': 'Hole',
        'DESCRIPTION': 'You fall down another deep hole and there is a path to the north-west.',
        'PATHS': {
            'NORTHWEST': 'CAVE_2'
        }
    },
    'CAVE_2': {
        'NAME': 'Cave',
        'DESCRIPTION': 'You are in another dirt cave. There is two paths to the south-west and south-east.',
        'PATHS': {
            'SOUTHWEST': 'BEDROOM',
            'SOUTHEAST': 'HOLE_2'
        }
    },
    'S_BOX': {
        'NAME': 'Steel Box',
        'DESCRIPTION': 'You are now in a steel box. There is a path to the north and one to the west.',
        'PATHS': {
            'NORTH': 'KITCHEN',
            'WEST': 'M_BOX'
        }
    },
    'BATHROOM_1': {
        'NAME': 'Bathroom',
        'DESCRIPTION': 'You enter the bathroom. On the shelf there is a half-eaten sandwich. There is three paths: '
                       'East, West, and South.',
        'PATHS': {
            'EAST': 'GRASS',
            'WEST': 'KITCHEN',
            'SOUTH': 'STORAGE'
        }
    },
    'STORAGE': {
        'NAME': 'Storage Room',
        'DESCRIPTION': 'You walk into a dim lighted storage room. In the bottom right corner, there is a cardboard '
                       'box. It seems to be partially open.',
        'PATHS': {

        }
    },
    'GRASS': {
        'NAME': 'Grass Field',
        'DESCRIPTION': 'You leave the bathroom and you are now in a grassy field. To the north and to the east there '
                       'is a brick wall. There are two paths to the west and south.',
        'PATHS': {
            'WEST': 'BATHROOM_1',
            'SOUTH': 'BARN'
        }
    },
    'BARN': {
        'NAME': 'Barn',
        'DESCRIPTION': 'You walk through two open doors into a barn. There is two paths leading west and north. '
                       'It appears that nothing is in the barn but you feel like there is something watching you.',
        'PATHS': {
            'NORTH': 'GRASS',
            'WEST': 'BATHROOM_2'
        }
    },
    'BATHROOM_2': {
        'NAME': 'Fancy Bathroom',
        'DESCRIPTION': 'You enter a fancy bathroom. On the wall there is a mirror that is partially broken. '
                       'There are two paths to the west and to the east.',
        'PATHS': {
            'EAST': 'BARN',
            'WEST': 'POOL'
        }
    },
    'POOL': {
        'NAME': 'Pool',
        'DESCRIPTION': 'You leave the bathroom and walk onto a pool deck. Floating in the pool is another rubber duck '
                       'wearing a fedora. There are two paths to the east and to the north-west.',
        'PATHS': {
            'NORTHWEST': 'LIBRARY',
            'EAST': 'BATHROOM_2'
        }
    },
    'LIBRARY': {
        'NAME': 'Library',
        'DESCRIPTION': 'You walk into a library full of dusty books. You look around and find 600 rubber ducks wearing '
                       'fedoras all over the room. You need to get out either to the west or south-east.',
        'PATHS': {
            'WEST': 'CLASS',
            'SOUTHEAST': 'POOL'
        }
    },
    'CLASS': {
        'NAME': 'Classroom',
        'DESCRIPTION': 'You walk into what look likes an old classroom. Books are left all over the desks and there is '
                       'a staircase in the back. \nThere are two paths leading out, down the staircase and to the east',
        'PATHS': {
            'EAST': 'LIBRARY',
            'DOWN': 'STORAGE_2'
        }
    },
    'STORAGE_2': {
        'NAME': 'Whiteboard Marker Storage',
        'DESCRIPTION': 'You enter a room full of seafoam green colored whiteboard markers. There is two paths up the '
                       'staircase and down the staircase.',
        'PATHS': {
            'UP': 'CLASS',
            'DOWN': 'STORAGE_3'
        }
    },
    'STORAGE_3': {
        'NAME': 'Large Storage Room (Boss Area)',
        'DESCRIPTION': 'You enter a dim lighted storage room. You see over 3,000 tiny rubber ducks in the room '
                    'surrounding a the largest rubber duck in the world. You see that your armor has been upgraded '
                    'and \nyou now have a sword to fight the ducks. There is a path to the east but it is shut, and '
                    'a path up the stairs. Defeat the duck to open the door.',
        'PATHS': {
            'UP': 'STORAGE_2',
            'EAST': 'PARTY'
        }
    },
    'PARTY': {
        'NAME': 'Party Central 101',
        'DESCRIPTION': 'You had just defeated the ducks. You walk into a party room to celebrate the win '
                       'with all the people who live in the house. Congrats on beating the game. You did a nice job',
        'PATHS': {

        }
    },
}

current_node = world_map['M_BOX']
directions = ['NORTH', 'SOUTH', 'WEST', 'EAST', 'NORTHWEST', 'SOUTHEAST', 'UP', 'DOWN', 'SOUTHWEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print("Command not recognized")
