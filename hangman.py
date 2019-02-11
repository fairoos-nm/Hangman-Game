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

# Make a fuction to mask selected word
def mask_selected_word(selected_word):
    word_len = len(selected_word)
    masked_word = ((word_len) * "*") #  (x - 1) to avoid newline char 
    return masked_word


def chek_gussed_char(guessed_char,selected_word):
    list_of_word = list(selected_word)
    a = ''
    for i in range(len(list_of_word)):
        a = list_of_word[i]
        if guessed_char == a :
            position = [i for i, s in enumerate(list_of_word) if guessed_char  in s]      
    return position
    
