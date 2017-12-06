# REMEMBER, INPUTS FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!

# 1. Generate a number
# 2. Ask the user for an input(Number)
# 3. Does the guess match the number?
# 4. Add "Higher" and "Lower"
# 5. Add 5 guesses

import random


winning_number = random.randint(1,50)
guesses = 5
correct_guess = False

number = int(input("Choose a number between one and fifty:"))

while guesses != 0 and correct_guess == False:
    if number == winning_number:
        guesses -= 1
        print("Yay! You deserve a cake! You had %s guesses left." % guesses)
        correct_guess = True
    elif number > winning_number:
        guesses -= 1
        print("Sorry! Your number was too high. You have %s guesses left." % guesses)
        number = int(input("Try again:"))
    elif number < winning_number:
        guesses -= 1
        print("Sorry! Your number was too low. You have %s guesses left." % guesses)
        number = int(input("Try again:"))
if guesses == 0:
    print("You lose! The correct number was %s. Go home and eat away your sorrows... loser." % winning_number)
