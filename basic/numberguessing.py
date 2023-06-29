import random
import os

#Allow them to guess and take away from guess count each time
#If the guess is less than the number, print 'higher'
#If higher, print 'lower'

def guess(total):

    if total != guesses:
        print('Guess again!')

    print(f'You have {total} attempt(s) left.')

    try:
        choice = int(input("What's your guess? "))
    except ValueError:
        print('Please enter a valid input. ')
        choice = int(input("What's your guess? "))

    if choice == numb:
        print(f'\nYou won! Out of {guesses} guesses, you used {guesses - total}!\n')
        return
    elif choice < numb:
        print("Go higher.")
    elif choice > numb:
        print("Go lower.")

    new_total = total - 1

    if new_total == 0:
        print(f"\nYou've used all of your guesses. The number was {numb}. Game over!\n")
        return

    guess(new_total)


print('\n***Welcome to the Number Guessing Game***\n')
print("I am think of a number between 1 and 100. I'll let you know if you're higher or lower than my number.")

numb = random.randint(1, 100)

#Ask how hard they want the game and set the variabel
#Easy - 10, Medium - 7, Hard - 5, Impossible - 3

diff = input("\nWhat difficulty would you like to play on? The options are: easy ('e'), medium ('m'), hard ('h'), impossible ('i'). Type 'e', 'm', 'h', or 'i': ")

while diff not in ['e', 'm', 'h', 'i']:
    diff = input("Type 'e' for easy, 'm' for medium, 'h' for hard, and 'i' for impossible: ")

if diff == 'e':
    guesses = 10
elif diff == 'm':
    guesses = 7
elif diff == 'h':
    guesses = 5
else:
    guesses = 3

print(f'\nYou have {guesses} guesses to guess my number. Good luck!\n')
guess(guesses)