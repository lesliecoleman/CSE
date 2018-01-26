# This is a guide of how to make hangman
# 1. Make a word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed
# 4. Hide and reveal letters
# 5. Create win and lose conditions
import random
import string
import sys

alphabet = string.ascii_lowercase
words_phrases = ['stuart', 'bunny', 'lightsaber', 'jeffery', 'cookies', 'monkey', 'pickles', 'kyber', 'cheeseburger',
                 'farkle']
word = list(random.choice(words_phrases))
print(word)
hidden_word = list('*' * len(word))
guesses_left = 10
regular_word = random.choice(words_phrases)
guesses = []

while guesses_left > 0:
    print(guesses)
    player_guess = input("take a guess >_")
    guesses.append(player_guess)
    if player_guess not in regular_word:
        guesses_left -= 1
    print("You now have %s guesses" % guesses_left)
    output = []
    for letter in regular_word:
        if letter in guesses:
            output.append(letter)
        else:
            output.append('*')
    output = ''.join(output)
    if '*' not in output:
        print('Congrats you win. The word was %s' % regular_word)
        sys.exit()
    print(output)

print("You lose. The word was %s" % regular_word)