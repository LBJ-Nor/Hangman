from hangman_art import models
import random

with open('wordlist.txt') as f:
    secret_word = (random.choice(f.readlines())).upper()[:-1]

already_guessed = []
wrong_guess_counter = 0
placeholder = ['_' for _ in range(len(secret_word))]


def guess_validator():
    global wrong_guess_counter
    player_guess = input('Guess a letter: ').upper()
    
    # Validate input
    if player_guess.isalpha():
        if len(player_guess) == 1:
            if player_guess in already_guessed:
                print('That letter has already been guessed. Try again.')
            else:
                already_guessed.append(player_guess)
                if player_guess not in secret_word:
                    wrong_guess_counter += 1
            # fill placeholder by index
            for slot in range(len(secret_word)):
                if secret_word[slot] == player_guess:
                    placeholder[slot] = player_guess

        else:
            print('Guess one letter at a time. Try again.')

    else:
        print('That was not a letter. Try again.')


# Game loop
while '_' in placeholder:
    print(f"""{models[wrong_guess_counter]}
Guess the word:  {' '.join(placeholder)}
Already guessed: {', '.join(already_guessed)}
""")
    guess_validator()
    if wrong_guess_counter == 6:
        print(f'The word was {secret_word}')
        print('You died!')
        break

if '_' not in placeholder:
    print(f' The word was {secret_word}')
    print('You win!')
