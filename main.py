
import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in data.iterrows() }
print(f'{alphabet}')
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('What word would you like to use?')
real_input = user_word.upper()
new_list = [alphabet[letter] for letter in real_input]
print(f'{new_list}')
