import os

print('\n***Welcome to my Calculator***\n')

cont = False
first = ''

def main():
    
    global first 

    if cont == False: 
        first = float(input('What is your first number? '))

        while first == '':
            first = float(input('What is your first number? '))

    operation = input("Which operation would you like to perform: '+', '-', '*', '/': ").strip()

    while operation != '+' and operation != '-' and operation != '*' and operation != '/':
        operation = input("Please type in one of the following signs: '+', '-', '*', '/': ").strip()

    second = float(input('What is your second number? '))

    while second == '':
        second = float(input('What is your second number? '))

    calculator(first, second, operation)

def calculator(firstn, secondn, operation):

    global cont
    global first

    if operation == '+':
        numb = firstn + secondn

    elif operation == '-':
        numb = firstn - secondn

    elif operation == '*':
        numb = firstn * secondn

    elif (operation == '/'):
        numb = firstn / secondn
    
    numb = round(numb, 2)
    print(firstn, operation, secondn, '=', numb)
    goon = input(f'Would you like to continue with this {numb}, start over, or quit? Type "y" to continue, type "n" to quit, and hit enter to start over. ')

    while goon != 'y' and goon != '' and goon != 'n':
        goon = input(f'Type either "y" or hit enter. ')
    
    if goon == 'y':
        clear_terminal()
        print(f'First number: {numb}')
        cont = True
        first = numb
        main()
    elif goon == '':
        cont = False
        main()
    else:
        return
        
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

main()
