import random

word_bank = ['California', 'Ohio', 'Colorado', 'Arizona', 'Delaware', 'Florida']

word = random.choice(word_bank)

guessedWord = ['_'] * len(word)  

attempts = 10

