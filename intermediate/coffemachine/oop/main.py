from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
item = menu.find_drink('latte')
drink = item.name

machine = CoffeeMaker()

money = MoneyMachine()

def main():

    #Choose drink
    choice = input(f'\nWhat would you like? {menu.get_items()}: ')

    avbl = ''

    if choice == 'report':
        machine.report()
        money.report()
        main()
        return
    elif choice == '':
        return
    else:
        avbl = menu.find_drink(choice)

    if avbl != None:
        purchase(choice)
    else:
        main()


def purchase(item):

    drink = menu.find_drink(item)

    #Check to make sure there are enough ingredients
    resources = machine.is_resource_sufficient(drink)
    
    if resources == False:
        print('We cannot make that right now. Please order something else.')
        main()
        return

    #Give price and take coins
    print(f"\nThe price of your {drink.name} is ${drink.cost}. Please insert coins: ")
    paid = money.make_payment(drink.cost)

    if paid == True:
        machine.make_coffee(drink)

    #Ask if they'd like to order again
    goon = input("Would you like another drink. Type 'y' for yes or hit enter for no: ")

    while goon not in ['y', '']:
        goon = input("Type 'y' for yes or hit enter for no: ")
    
    if goon == 'y':
        main()

    return


main()

