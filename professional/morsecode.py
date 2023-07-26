morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': ''
}

choice = input('Would you like to convert text to morse code or decode morse code? Type "t" for text or "d" for decode: ')

while choice not in ['t', 'd']:
    choice = input('Type "t" for text or "d" for decode: ')

output = []

if choice == 't':
    text = input('What is your text? ')
    for i in text:
        output.append(morse_code_dict[i.upper()])

    print(' '.join(output))

else:
    code = input('What is your code? ')
    code = code.strip().split(' ')
    
    for char in code:
        for i in morse_code_dict:
            if morse_code_dict[i] == char:
                output.append(i)
                break
    
    print(''.join(output))