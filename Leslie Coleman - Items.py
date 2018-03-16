class item(object):
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def take(self):
        