# create a new file Warmups.py

# 12.4.17
# Write a Python Function
# which accepts the user's
# first and last name
# and prints them in reverse order
# with a space between them.


def reverse_order(first_name, last_name):
    # print("%s, %s"  % (last_name, first_name))
    print(last_name + " " + first_name)  # Concatenation

first = input("What is your first name?")
last = input("What is your last name?")

reverse_order(first, last)