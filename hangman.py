# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)


selected_word = get_secret_word()

#make a function to mask selected word
def mask_selected_word(selected_word):
    x = len(selected_word)
    a = ((x-1) * "*") 
    return a
print (mask_selected_word(selected_word))
print(selected_word)
