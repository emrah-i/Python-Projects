print('\n***Welcome to Caesar Cipher***\n')

def main():
    decision = input("Type 'code' to make a cipher and 'decode' to decode one. ").strip()

    while decision != 'decode' and decision != 'code':
        decision = input("You must type either 'code' or 'decode'. ").strip()
        print('\n')

    if decision == 'code':
        message = input('What is the message you want to code? ').strip()
    else:
        message = input('What is the message you want to decode? ').strip()
        
    shift = int(input('What is your shift amount? '))
    cipher(message, shift, decision)
    
    again = input("Would you like to go again? Type 'yes' for yes or hit enter for no. ").strip()

    print('\n')

    while again != 'yes' and again != '':
        again = input("Type 'yes' for yes or hit enter for no. ").strip()
    
    if again == 'yes':
        main()
    else:
        exit()

def cipher(message, shift, decision):

    length = len(message)
    cipher = list(range(length))
    new_message = message.lower()

    for i in range(length):

        ascii = ord(new_message[i])
        
        if decision == 'code':
            if ascii >= 97 and ascii <= 122:
                shift_char = ascii + (shift % 26)

                if shift_char > 122:
                    cipher[i] = shift_char - 26
                else: 
                    cipher[i] = shift_char
            else:
                cipher[i] = ascii

        elif decision == 'decode':
            if ascii >= 97 and ascii <= 122:
                shift_char = ascii - (shift % 26)
                
                if shift_char <= 96 and shift_char != 32:
                    cipher[i] = shift_char + 26
                else:
                    cipher[i] = shift_char
            else:
                cipher[i] = ascii

        cipher[i] = chr(cipher[i])

        if ord(message[i]) > 64 and ord(message[i]) < 91:
            cipher[i] = cipher[i].upper()

    print('\nHere is your text:', (''.join(cipher)), '\n')

main()