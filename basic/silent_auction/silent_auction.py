from auctioning_items import items
import os

print("\n***Welcome to Silent Auction***\n")

winners = []
products = items

def main():
    print('We will be auctioning the following items:')

    for i in range(len(products)):
        print(i, products[i]['name'])

    item = int(input('\nSelect the number of the product you would like to auction now: '))

    while item > (len(products) - 1) or item < 0:
        item = int(input('Select a valid item index: '))

    auction(item)

    next = input('Would you like to auction any more items? Type "yes" for yes and hit enter for no: ')

    while next != 'yes' and next != '':
        next = input('Type "yes" for yes and hit enter for no: ')
    
    if next == 'yes':
        main()
    else:
        print('\nWinners:')  
        for i in range(len(winners)): 
            print('    ', 'Item:', winners[i]['name'])
            print('    ', 'Bid:', winners[i]['current bid'])
            print('    ', 'Bidder:', winners[i]['bidder'])
            print('\n')

        exit()

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def auction(item):
    print(f'\nThe auction for the {products[item]["name"]} will now start! The starting bid is ${products[item]["current bid"]}.\n')

    over = False

    while over != True:
        name = input('Enter your name: ').strip()

        while name == '' or name.isdigit():
            name = input('Enter a valid name: ').strip()

        bid = float(input('What is your bid: $'))

        while bid == '' or bid == ' ':
            bid = float(input('Please enter valid bid: $'))

        if bid > products[item]['current bid']:
            products[item]['current bid'] = bid
            products[item]['bidder'] = name

        more = input('Is there any more bidders? Type "yes" for yes or hit enter for no: ')
    
        while more != 'yes' and more != '':
            more = input('Type "yes" for yes and hit enter for no: ')
        
        if more == "yes":
            clear_terminal()
            auction(item)
        else: 
            clear_terminal()
            winners.append(products[item])
            print(f"The winner of the {products[item]['name']} is {products[item]['bidder']}")
            return

main()
