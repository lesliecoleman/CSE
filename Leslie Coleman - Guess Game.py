# REMEMBER, INPUTS FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!

import random


winning_number = random.randint(1,50)
guesses = 5

number = int(input("Choose a number between one and fifty"))
if number == winning_number:
    print("Yay! You guessed the number! You had %s guesses left" % guesses)
elif number > winning_number:
    print("Sorry! Your number was too high. Try again. You have %s guesses left." % guesses)
elif number < winning_number:
    print("Sorry! Your number was too low. Try again. You have %s guesses left." % guesses)
