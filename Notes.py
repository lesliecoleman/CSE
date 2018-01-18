# print("Hello world")
#
# # Leslie
#
# a = 4
# b = 3
#
# print(3+5)
# print(5-3)
# print(3*5)
# print(6/2)
# print(3 ** 2)
#
# print("try to figure out how this works")
# print(11 % 5)
#
# # the "%" sign is a modulus. It finds a remainder.
#
# car_name = "The Cheese Mobile"
# car_type = "Porsche"
# car_cylinders = 10
# car_mpg = 6000
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s."% (car_name, car_type)) #watch the order
#
# # here is where we get a little fancy
# print("What is your name?")
# name= input(">_")
# print("Hi %s." %name)
#
# age = input("How old are you?")
# print("%s?! That's really old. You belong in a retirement home." %age)
#
# print("I wish I had a cheeseburger at the moment and that I was sharing it with my friend Jeffery")
#
# print("What is your best friend's name?")
# name= input(">_")
# print("I wish I could meet %s" %name)

# Functions


# def print_hw():
#     print("Hello World.")
#     print("Enjoy the day.")
#
#
# # Indent is exactly 4 spaces for python, everything should be lowercase
#
# print_hw()
#
#
# def say_hi(name):  # Name is a "parameter"
#     print("Hello %s" % name)
#     print("Coding is great!")
#
#
# say_hi("Jeffery")
#
#
# def print_age(name, age):
#     print("%s is %d years old" % (name, age)) # There can only be one item after the percent, more than 1 use (, )
#     age += 1  # age = age + 1
#     print("Next year, %s will be %d years old" % (name, age))
#
#
# print_age("Jeffery", 17)
#
#
# def algebra_hw(x):
#     return x**3 + 4*x**2 + 7 * x - 4
#
# print(algebra_hw(3))
# print(algebra_hw(4))
# print(algebra_hw(5))
# print(algebra_hw(6))
# print(algebra_hw(7))
#
#
# # if statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:  # else if
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
#
# print(grade_calc(99))

# def happy_bday(name):
#     print("Happy birthday to you,")
#     print("Happy birthday to you,")
#     print("Happy birthday dear %s," %name)  # also works as "Happy Birthday dear" + name
#     print("Happy birthday to you.")
#
#
#
# (happy_bday("Jeffery"))

# Loops

# for num in range(10):
#     print(num + 1)
#
# # While Loops will break your computer
#
# a = 1
# while a < 10:  # This is the condition
#                 # it must be true to execute
#     print(a)
#     a += 1  # This iterate so that we can break the loop

# Random Numbers

# import random  # This should be on line 1
# print(random.randint(0, 10))



# c = '1'
# print(c == 1)  # we have a string and an integer
# print(int(c) == 1)
# print(c == str(1))


# # Comparisons

# print(1 == 1)  # Use a double equal sign
# print(1 != 2) # 1 is not equal to 2
# print(not False)



# Lists

the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', "beef", "crushed chips", "sesame seed bun", "add on:avocado", "bacon", "mac and cheese",
                            "ranch", "add on:extra cheese of any choice"]
print(cheeseburger_ingredients[0])
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))

# print(len(the_count))

# Going through lists
for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for the_count in the_count:
    print(the_count * 2)

length = len(cheeseburger_ingredients)
range(5)  # A list of the numbers 0 through 4
range(len(cheeseburger_ingredients))  # Generates a list of all indices

for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num, item))

# Lines 161 - 167 are the MOST IMPORTANT LINES EVER!!!!!!!
