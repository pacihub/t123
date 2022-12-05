import random

wordz = ['Hangover', 'Bridgerton', 'Friends', 'Crown', 'Memento', 'Alone', 'Inception',
         'Interstellar', 'Argo']

def get_valid_word(word_list):
    picked_word = random.choice(word_list)      # randomly chooses a word from a list

    return picked_word.upper()

#print(get_valid_word(wordz))

def hangman():
    lives = 6

    guess_word = get_valid_word(wordz)
    dash_representation = (len(guess_word) * '_')   # rep the word with dashes on the screen

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    user_guesses = set()                    # store all letters the user has already guessed
    guess_word_letters = set(guess_word)    # All letters contained in the word

    # prompt until the word has been guessed or game is over
    while len(guess_word_letters) > 0:
        print("Until now you've guessed the letters: ", ''.join(user_guesses))
        on_screen = [i if i in user_guesses else '_' for i in guess_word]
        print(''.join(on_screen))

        guessed_letter = input("Guess a letter: ").upper()

        if guessed_letter in alphabet:
            alphabet.remove(guessed_letter)
        else:
            print("this letter already used")
            continue        # return to the beginning of the while loop

        if guessed_letter in guess_word_letters:      # if the guessed letter is correct
            guess_word_letters.remove(guessed_letter)     #remove it from remaining guess letters

            if len(guess_word_letters) == 0:
                print("you won fucker. The word was,", guess_word)
                exit()
        else:
            lives -= 1
            if lives == 0:
                print("game over, dude. The word was,", guess_word)
                exit()

        user_guesses.add(guessed_letter)
 #       print("the word is with these letters: ",guess_word_letters)
 #       print("choose from letters: ", alphabet)
 #       print("Letters remaining: ", len(guess_word_letters))
        print(f"wrong attempts left: {lives}")

# program start
hangman()







