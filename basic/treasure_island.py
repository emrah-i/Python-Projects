print("Welcome to Treasure Island. You mission is to go down the path that will lead you to treasure.\n")

first = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'? ")

print('\n')

while first.strip() != 'right' and first.strip() != 'left':
    print('Invalid answer. Please try again.\n')
    first = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'? ")

if first == 'right':
    print("There were bandits on that path, and while you were running away, you tripped and hit your head. You're dead. We'll just put that the bandits got you on the headstone. Game over!\n")
    exit()

second = input("As you're walking, you come across a lake. There is an island in the middle of the lake that you could possibly swim to. Would you like to wait for a boat or swim. Type 'boat' or 'swim'? ")

print('\n')

while second.strip() != 'boat' and second.strip() != 'swim':
    print('Invalid answer. Please try again.\n')
    second = input("As you're walking, you come across a lake. There is an island in the middle of the lake that you could possibly swim to. Would you like to wait for a boat or swim. Type 'boat' or 'swim'? ")

if second == 'swim':
    print("You must be blind because those were very obviously shark infested waters. I mean you can literally see their fins. Game over!\n")
    exit()

final = input("You safely arrive at the island on boat. You come across an odd house with three different colored doors. One red, one blue, and one yellow. I guess the owner couldn't decide on a color. Which door do you enter through?. Type 'red', 'blue', 'yellow'? ")

print('\n')

while final.strip() != 'red' and final.strip() != 'blue' and final.strip() != 'yellow':
    print('Invalid answer. Please try again.\n')
    final = input("You safely arrive at the island on boat. You come across an odd house with three different colored doors. One red, one blue, and one yellow. I guess the owner couldn't decide on a color. Which door do you enter through?. Type 'red', 'blue', 'yellow'? ")

if final == 'blue' or final == 'red':
    print("I like your courage, however, those doors had traps behind them and you're dead for sure, like really dead. There were spikes and everything. Game over!\n")
    exit() 

else:
    print("You found a chest with treasure. Congratulations! I recommend you take it but it is someone's house you just barged into so ¯\_(ツ)_/¯")
    print(''' 
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/
    ''')
    exit()




        