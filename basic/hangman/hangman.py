import random
from hangman_words import word_list

print('\n Welcome to Handman!\n')

score = 0

stages = [
'''
+---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

word = random.choice(word_list).lower()
empty = list(range(len(word)))

for i in range(len(empty)):
    empty[i] = '_'

won = False

letters_guessed = []

while won == False:
    letter = (input('Guess a letter: '))
    while letter in letters_guessed:
        letter = input('You already guessed that. Guess another letter: ')

    while len(letter) > 1:
        letter = input('You must guess a letter: ')

    letters_guessed.append(letter)
    found = False

    for i in range(len(empty)):
        if letter == word[i]:
            empty[i] = letter
            found = True
        elif i == (len(empty) - 1) and found == False:
            score += 1
            if score != 7:
                print('\n', stages[score - 1], '\n')

    if ''.join(empty).lower() == word.lower():
        print('\n**** You won! ****\n')
        print('\nThe word was:', word, '\n')
        exit()
    
    elif score == 7:
        print('\n**** You lost! ****\n', stages[6], '\n')
        print('\nThe word was:', word, '\n')
        exit()
    
    print('\nLetters guessed:', letters_guessed, '\n', ''.join(empty), '\n')
    