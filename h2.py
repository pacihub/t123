
# load a random word from a dictionary

# draw a _ for each letter they have

# user guesses a letter
    # if letter does not match - draw a line
    # if letter matches, reveal the letter

import random
import h3

dict = ['honey', 'crackers', 'bread', 'nuts', 'fruits', 'chocolate', 'rice', 'cereal']
pc_word = random.choice(dict)   # randomly generated word

print(pc_word)  # check

# dash representation
for i in pc_word:
    print('_', end="")
print()


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


lives = 7

aa = []

correct_letters = set(pc_word)


while lives > 0:
    guess = input("Guess a letter: ")
    if guess in pc_word:
        aa.append(guess)
        correct_letters.remove(guess)
        if len(correct_letters) == 0:
            print(f"You won. The word was {pc_word}")
            exit()
    else:
        lives -= 1

        if lives == 0:
            print(f"game over, dude. The word was, {pc_word}")
            exit()

    for i in pc_word:
        if i in aa:
            print(i, end="")
        else:
            print('_', end="")
    print()
    print(lives)
    print(correct_letters)
















