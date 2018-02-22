# Defining a class
class Cheeseburger(object):
    def __init__(self, patty_type, cheese):  # TWO underscores before and after
        self.patty = patty_type
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + "is thankful")

    def cut(self):
        print("You cut the cheeseburger")

    def eat(self):
        print("You eat the cheeseburger")
        self.eaten = True


# Instantiating (the creation of) two cheeseburgers
burger1 = Cheeseburger("Beef", "Cheddar")
burger2 = Cheeseburger("Bacon", "Swiss")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)

# Car can drive, explode, flip, turn


class Car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print("Nothing Happens.")
        else:
            self.running = True
            print("The car starts.")

    def move_forward(self):
        if self.running:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.running:
            self.running = False
            print("You turn the car off")
        else:
            print("The car is already off")

    def go_for_drive(self, passengers):
        print("%d passengers get in." % passengers)
        self.passengers = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print("%d passengers get out." % passengers)
        self.passengers = 0


my_car = Car('Jeffery', 'Neon Yellow', 2000, 999999999999999999999199999999999)

car2 = Car('Yreffej', 'Neon Blue', 4000, 999999999999999999999999999999999999999999999999999999999999999999999999999999)
my_car.go_for_drive(777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777)