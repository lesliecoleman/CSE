class Vehicle(object):
    def __init__(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.max_speed = speed
        self.passengers = passengers

    def move(self):
        print("You move forward")

    def change_directions(self):
        print("You change directions")


class Car(Vehicle):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Car, self).__init__('engine', material, seat, speed, passengers)
        self.windows = windows

    def roll_down_windows(self):
        print("You roll the windows down")

    def turn_on(self):
        print("You turn the key and the engine starts")


test_car = Car('Plastic', 'Driver side', 653324104025, 1210712057927947395872395739579375203741957902137593755902, True)
test_car.change_directions()


class KeylessCar(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(KeylessCar, self).__init__(material, seat, speed, passengers,windows)

    def turn_on(self):
        print("You push the button and the car turns on")


test_car.turn_on()
cool_car = KeylessCar('Plastic', 'Driver side', 653324104025, 121071205792794739587239573957937520374195793755902, True)
cool_car.turn_on()
