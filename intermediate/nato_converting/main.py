import pandas

nato = pandas.read_csv('intermediate/nato_converting/nato_phonetic_alphabet.csv')
locate = nato.loc[nato['letter'] == 'A'].iloc[0]['code']

# alpha = {letter:code for (letter, code) in nato.itertuples(index=False)}

text = input("What word would you like to convert? ")

new_words = [nato.loc[nato['letter'] == letter.upper(), 'code'].to_string(index=False) for letter in text if letter.isalpha()]
print(new_words)

# same as nato[nato['letter'] == letter.upper()].iloc[0]['code']

