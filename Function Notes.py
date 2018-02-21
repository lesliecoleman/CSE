# Defining functions
def hello_world():
    print("Hello World")


hello_world()


def square_it(number):
    return number**2


print(square_it(3))


def tip_calc(bill):
    tax_amt = bill * 0.18
    total_bill = bill + tax_amt
    return total_bill


print(tip_calc(0.50))


def distance_calc(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y2 - y1) ** 2
    answer = inside ** 0.5
    return answer


print(distance_calc(0, 0, 3, 4))


def theorem_calc(a, b):
    inside = (a) ** 2 + (b) ** 2
    answer = inside ** 0.5
    return answer


print(theorem_calc(5, 12))