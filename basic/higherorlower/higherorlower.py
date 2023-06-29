from options import celebrities
import random
import os

print('\n***Welcome to Higher or Lower***\n\nThis is a game where you guess which of the two options presented has a higher instagram following count.\n')

score = 0
round = 0
loser = None
choice1 = None
choice2 = None

def main():

    global score
    global round
    global loser
    global choice1
    global choice2

    #If round 0, choose both choices. Else: keep the last winner
    if round == 0:
        choice1 = random.choice(celebrities)
        choice2 = random.choice(celebrities)
    elif loser == choice1:
        choice1 = random.choice(celebrities)
    else:
        choice2 = random.choice(celebrities)
    
    #Choose the winner
    if int(choice1['followers']) > int(choice2['followers']):
        winner = '1'
        loser = choice2
    else:
        winner = '2'
        loser = choice1

    #Make sure the two choices are not the same
    while choice1 == choice2:
        choice2 = random.choice(celebrities)

    #Print both options
    print(f"Choice 1: {choice1['name']}: {choice1['description']}\n\nvs")
    print(f"\nChoice 2: {choice2['name']}: {choice2['description']}\n")

    #Ask for the input
    choose = input("Does choice 1 or choice 2 have a higher instagram following. Type '1' for 1 or '2' for 2: ")

    while choose not in ['1', '2']:
        choose = input("Type '1' for 1 or '2' for 2: ")

    #Path depending on correct or incorrent choice
    if choose == winner:
        score += 1
        round += 1
        clear_terminal()
        print(f"\nThat's correct! Your score is {score}. Round {round + 1}:\n")
        main()
    else:
        print(f"\nThat's wrong! Your final score is {score}\n")
        exit()

def clear_terminal():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


    


main()
