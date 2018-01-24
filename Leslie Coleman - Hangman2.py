# This is a guide of how to make hangman
# 1. Make a word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed
# 4. Hide and reveal letters
# 5. Create win and lose conditions
import random
import string

alphabet = string.ascii_lowercase
words_phrases = ['high school musical', 'onion rings', 'wittle wunny', 'jeffery', 'boy meets world', 'home improvement',
                 'harry potter', 'star wars', 'cheeseburger', 'farkle minkus']
word = list(random.choice(words_phrases))
print(word)
player_guess = ''
hidden_word = list('*' * len(word))
print(player_guess)
guesses_left = 10


while:
    