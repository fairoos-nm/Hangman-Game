3# hangman.py

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


def add_gussed_char_masked_word(posi ,guessed_char,m_word):
    mask_w = m_word
    list_mask_w = list(mask_w)
    print(list_mask_w)
    a =[]
    for i in posi:
        list_mask_w[i] = guessed_char
    unmasked_word = list_mask_w
    return unmasked_word

def main(selected_word = get_secret_word()):
    chance = 10
    wrong_guess = ''
    word=list(selected_word)

    m_word = mask_selected_word(selected_word)
    posi = chek_gussed_char(guessed_char,selected_word)
    un_masked_word = add_gussed_char_masked_word(posi ,guessed_char,m_word)
    str_unmasked_word =''.join(un_masked_word)
    

    
    while chance:
        
        print(f"\n {str_unmasked_word} \n")
        print(f"Number of tries left: {chance}")
        print(f"Wrong guesses so far: {wrong_guess}")


        guessed_char=input("Enter your guess:  ")
        
        if len(guessed_char)!=1:
            print("Enter one Char. only!")
            continue
        if usr_input in word:
             m_word = mask_selected_word(selected_word)
             posi = chek_gussed_char(guessed_char,selected_word)
             un_masked_word = add_gussed_char_masked_word(posi ,guessed_char,m_word)
             
             str_unmasked_word =''.join(un_masked_word)
             print(str_unmasked_word)


        else:
            print("Wrong Guess:")


            wrong_guess = wrong_guess + guessed_char



            chance = chance - 1

            
        if selected_word == str_unmasked_word:
            
            print("Congratulations! You WON.")
            break
            
        if chance == 0:
            
            print(f"Too bad! The secret word was {selected_word}")
                
                
if __name__=='__main__':
    main()
            
            
           
        
    
#def gussed_char():
 #   guess = input("guess a charecter:  ")
  #  return guess
