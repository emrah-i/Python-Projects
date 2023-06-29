from items import options

machine = {
    'water': 500,
    'milk': 500,
    'coffee': 100,
    'money': 0
}

''' 
    water (ml)
    milk (ml)
    coffee (g)
    money ($)
'''

def main():
    #Choose drink
    choice = input('\nWhat would you like? (Espresso / Americano / Cappuccino / Latte / Macchiato / Flat White): ').title()

    while choice not in ["Espresso", "Americano", "Cappuccino", "Latte", "Macchiato", "Flat White", "Report"]:
        choice = input('Type in Espresso / Americano / Cappuccino / Latte / Macchiato / Flat White: ')

    #Gives a receipt of the ingredients available
    if choice == 'Report':
        print('\nWater:', machine['water'], '\nCoffee:', machine['coffee'], '\nMilk:', machine['milk'], '\nMoney:', machine['money'], '\n' )
        main()
    else:
        purchase(choice)

def purchase(item):

    #Access global variable
    global machine
    
    drink = options[item]

    #Check to make sure there are enough ingredients
    if machine['water'] < drink['water']:
        print('Not enough water in the machine. Sorry!')
        exit()
    elif machine['coffee'] < drink['coffee']:
        print('Not enough coffee in the machine. Sorry!')
        exit()
    elif machine['milk'] < drink['milk']:
        print('Not enough milk in the machine. Sorry!')
        exit()

    #Give price and take coins
    print(f"\nThe price of your {item} is ${drink['price']:.2f}. Please insert coins: ")

    try:
        q = int(input("How many quarters: "))
    except ValueError:
        q = 0

    try:
        d = int(input("How many dimes: "))
    except ValueError:
        d = 0

    try:
        n = int(input("How many nickles: "))
    except ValueError:
        n = 0

    try:
        p = int(input("How many pennies: "))
    except ValueError:
        p = 0

    #Calculate price and refunds
    total = (q*.25) + (d*.1) + (n*.05) + (p*.01)
    price = drink['price']
    refund = round(total - price, 2)

    #Make sure they have enough money
    if refund < 0:
        print('\nNot enough money. Money refunded.')
        exit()
    elif refund > 0:
        print(f'\nThank you for your purchase. Your refund is ${refund}')
    else:
        print("\nThank you for your purchase. ")
    
    #Remove ingredients used and add money
    machine['water'] = machine['water'] - drink['water']
    machine['coffee'] = machine['coffee'] - drink['coffee']
    machine['milk'] = machine['milk'] - drink['milk']
    machine['money'] = machine['money'] + drink['price']

    print(f"Here is your {item}. Enjoy!\n")

    #Ask if they'd like to order again
    goon = input("Would you like another drink. Type 'y' for yes or hit enter for no: ")

    while goon not in ['y', '']:
        goon = input("Type 'y' for yes or hit enter for no: ")
    
    if goon == 'y':
        main()

    return



main()
