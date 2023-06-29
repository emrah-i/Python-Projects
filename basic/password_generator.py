import random

letters = int(input('How many letters would you like in your password? '))
symbols = int(input('How many symbols would you like? '))
numbers = int(input('How many numbers would you like? '))

length = letters + symbols + numbers
password = list(range(length))

for i in range(len(password)):
    password[i] = ''

random_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGIHJKLMNOPQRSTUVWXYZ'
random_symbols = '~`!@#$%^&*()_-+={[}]|\:;<>'
random_number = '1234567890'

for i in range(letters):
    char = random.choice(random_letters)
    place = random.choice(range(length))
    while password[place] != '':
        place = random.choice(range(length))
    else: 
        password[place] = char

for i in range(symbols):
    symbol = random.choice(random_symbols)
    place = random.choice(range(length))
    while password[place] != '':
        place = random.choice(range(length))
    else: 
        password[place] = symbol

for i in range(numbers):
    number = random.choice(random_number)
    place = random.choice(range(length))
    while password[place] != '':
        place = random.choice(range(length))
    else: 
        password[place] = number

print('\nHere is your password', ''.join(password), '\n')

