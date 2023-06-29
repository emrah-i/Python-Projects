import random

print('\nWelcome to Rock Paper Scissors!This is best out of 3. You will be facing the most decorated rock paper scissors player, my computer. \n')

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_points = 0
computer_points = 0
winner = False

def main():
    while winner == False:
        battle()

def battle():
    choices = [rock, paper, scissors]

    computer = random.choice(choices)

    player = input("\nChoose either rock, paper, or scissors. Type 'rock', 'paper', or 'scissors'. ")

    while player.strip() != 'rock' and player.strip() != 'paper' and player.strip() != 'scissors':
        print('Invalid response. Try again!')
        player = input("You will be facing the computer. Chooce either rock, paper, or scissors. Type 'rock', 'paper', or 'scissors'. ")

    if player == 'rock':
        player = rock
    elif player == 'scissors':
        player = scissors
    else:
        player = paper

    print('\nYou chose:', player)
    print('\nComputer chose:', computer)

    global computer_points 
    global user_points
    global winner

    if player == paper and computer == scissors:
        print("You lost")
        computer_points += 1
    elif player == paper and computer == rock:
        print("You won")
        user_points += 1
    elif player == paper and computer == paper:
        print("You tied")

    elif player == rock and computer == scissors:
        print("You won")
        user_points += 1
    elif player == rock and computer == rock:
        print("You tied")
    elif player == rock and computer == paper:
        print("You lost")
        computer_points += 1

    elif player == scissors and computer == scissors:
        print("You tied")
    elif player == scissors and computer == rock:
        print("You lost")
        computer_points += 1
    elif player == scissors and computer == paper:
        print("You won")
        user_points += 1

    print(f'\nCurrent score is: User {user_points}:{computer_points} Computer')

    if user_points == 3:
        print(f'You won {user_points}:{computer_points}!\n')
        winner = True
    
    elif computer_points == 3:
        print(f'You lost {user_points}:{computer_points}!\n')
        winner = True
    
    elif user_points == 2 and computer_points == 2:
        print('I am on the edge of my seat.')

main()