import random
import os

deck = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
user = []
comp = []
done = False

def main():

    global done

    print('\n***Welcome to Blackjack***\n')

    for _ in range(2):
        user.append(random.choice(deck))
        comp.append(random.choice(deck))

    user_score = fscore(user)
    comp_score = fscore(comp)

    if comp_score != 21 and user_score != 21:
        print(f"Your cards are: {user}\nYour current score is: {user_score}\nComputer's first card is {comp[0]}")
    elif user_score == 21 and comp_score == 21:
        print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nYou both got blackjack! It's a tie!\n")
        exit()
    elif comp_score == 21:
        print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nComputer got blackjack! You lost!\n")
        exit()
    elif user_score == 21:
        print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nYou got blackjack! You won!\n")
        exit()

    next = input("\nWould you like to hit or stand. Type 'h' for hit and 's' for stand. ")
    while next not in ['h', 's']:
        next = input("Type 'h' for hit and 's' for stand. ")
    
    done = False

    while next == 'h':
        user.append(random.choice(deck))
        user_score = n_score(user_score, user[len(user) - 1])

        if done == False:
            if comp_score <= 16:
                comp.append(random.choice(deck))
                comp_score = n_score(comp_score, comp[len(comp) - 1])

            if comp_score > 16 and comp_score <= 19:
                choice = random.randint(1, 1000) % 2
                
                if choice == 1:
                    comp.append(random.choice(deck))
                    comp_score = n_score(comp_score, comp[len(comp) - 1])
                else:
                    done = True

        if comp_score != 21 and user_score != 21:
            print(f"Your cards are: {user}\nYour current score is: {user_score}\nComputer's first card is {comp[0]}")
        elif user_score == 21 and comp_score == 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nYou both got blackjack! It's a tie!\n")
            exit()
        elif comp_score == 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nComputer got blackjack! You lost!\n")
            exit()
        elif user_score == 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nYou got blackjack! You won!\n")
            exit()

        if user_score > 21 and comp_score > 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nYou both busted! It's a tie!\n")
            exit()
        elif comp_score > 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nComputer busted! You won!\n")
            exit()
        elif user_score > 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nYou busted! You lost!\n")
            exit()
            
        next = input("\nWould you like to hit or stand. Type 'h' for hit and 's' for stand. ")
        while next not in ['h', 's']:
            next = input("Type 'h' for hit and 's' for stand. ")
    
    else:
        while comp_score <= 16:
            comp.append(random.choice(deck))
            comp_score = n_score(comp_score, comp[len(comp) - 1])

        while comp_score > 16 and comp_score <= 19:
            choice = random.randint(1, 1000) % 2
            
            if choice == 1:
                comp.append(random.choice(deck))
                comp_score = n_score(comp_score, comp[len(comp) - 1])
            else: 
                break
        
        if comp_score > 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nComputer busted! You won!\n")
            exit()
        elif comp_score == 21:
            print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}\n\nComputer got blackjack! You lost!\n")
            exit()

        print(f"\nFinal:\n\n{user} -- Score: {user_score}\n{comp} -- Score: {comp_score}")

        if comp_score > user_score:
            print('\nYou lost!\n')   
        elif user_score > comp_score:
            print('\nYou won!\n')   
        else:
            print('\nYou tied!\n')   

def fscore(hand: list):

    score = 0

    for i in range(len(hand)):
        if hand[i] in ['J', 'Q', 'K']: 
            score += 10

        elif hand[i] == 'A' and hand == user:
            ace = input(f"Your current hand is: {hand}. Would you like your ace to count as 1 or 11. Type either '1' or '11'. ")
            while ace not in ['1', '11']:
                ace = input("Type either '1' or '11'. ")
            if ace == '1':
                score += 1
            else:
                score += 11
        
        elif hand[i] == 'A' and hand == comp:
            if score != 11:
                score += 11
            else:
                score += 1
        
        else:
            score += hand[i]

    return score

def n_score(score, card):

    new_score = score

    if card in ['J', 'Q', 'K']: 
        new_score += 10
    elif card == 'A' and score > 10:
        new_score += 1
    elif card == 'A' and score <= 10:
        new_score += 11
    else:
        new_score += card
    
    return new_score

main()