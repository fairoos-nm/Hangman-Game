# hangman.py

import random
import emoji

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

def mask_selected_word(selected_word):
    word_len = len(selected_word)
    masked_word = ((word_len) * "*")  
    return masked_word

def chek_gussed_char(guessed_char, selected_word):
    list_of_word = list(selected_word)
    a = ''
    for i in range(len(list_of_word)):
        a = list_of_word[i]
        if guessed_char == a :
            position1 = [i for i, s in enumerate(list_of_word) if guessed_char  in s]
            return position1
        else:
            position2 = []
    return position2;

def add_gussed_char_masked_word(posi ,guessed_char, masked_word):
    mask_w = masked_word
    list_mask_w = list(mask_w)
   #print(list_mask_w)
    for i in posi:
        list_mask_w[i] = guessed_char
    unmasked_word = list_mask_w
    return unmasked_word

def user_input():
    user_input = input("Guess a character: ")
    if len(user_input)  != 1:
        print("\u26a0 sorry,only one char allowed at a time\n")
    else:
        return user_input
    
def check_allReady(user_ip, char_list):
    if user_ip in char_list:
        return print ("""\n\u274E You already guessed it\n""")
    
def chances(count):
    selected_word = get_secret_word()
    masked_word =  mask_selected_word(selected_word)
    print(masked_word)
    char_list = []
    while (count > 0):
        user_input1 = user_input()
        check_allReady(user_input1, char_list)
        char_list.append(user_input1)
        posi = chek_gussed_char(user_input1, selected_word)
        
        if len(posi) == 0:
            print(emoji.emojize(':thumbs_down:'), "Your guess is wrong")
        else:
            unmask =(add_gussed_char_masked_word(posi , user_input1, masked_word))
            unmask_str = ''.join(unmask)
            print(emoji.emojize(':thumbs_up:'), unmask_str)
            masked_word = add_gussed_char_masked_word(posi , user_input1, masked_word)
            if unmask_str == selected_word:
                print("\n\n")
                print(26 * u"\u2668")
                print("Congratulations! You WON.")
                print(26 * u"\u2663")
                print("\n\n")
                break
        count = count - 1
        print("\n\u23F3 remining chances: ", count,"\n")
        if count == 0:
            print("\u26F5  Sorry! you lose")
            print("The word was: ", selected_word)
            break
    return count

def main():
    Message = "welcome to Hangman_Game\nYou have 10 chances!"       
    print('\n'.join('{:^80}'.format(s) for s in Message.split('\n')))
    chances(10)
 
if __name__ == '__main__':
    main()
