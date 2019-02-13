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


#selected_word = get_secret_word()
#print(selected_word)

# Make a fuction to mask selected word
def mask_selected_word(selected_word):
    word_len = len(selected_word)
    masked_word = ((word_len) * "*")  
    return masked_word

#masked_word = mask_selected_word(selected_word)
#guessed_char = 'n'

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

#posi = chek_gussed_char(guessed_char, selected_word)
#print(posi)

def add_gussed_char_masked_word(posi ,guessed_char, masked_word):
    mask_w = masked_word
    list_mask_w = list(mask_w)
   #print(list_mask_w)
    for i in posi:
        list_mask_w[i] = guessed_char
    unmasked_word = list_mask_w
    return unmasked_word

#print(add_gussed_char_masked_word(posi ,guessed_char, masked_word) )


#def chance_left(usre_input):
   # chance = 10
    #while chance:
            
            

def user_input():
    user_input = input("Guess a character: ")
    if len(user_input)  != 1:
        print("Sorry,only one char allowed at a time")
    else:
        return user_input

    
def chances(count):
    selected_word = get_secret_word()
    masked_word =  mask_selected_word(selected_word)
    while (count > 0):
        user_input1 = user_input()
       
        posi = chek_gussed_char(user_input1, selected_word)
        
        if len(posi) == 0:
            messag1=("Your guess is wrong")
            print('\n'.join('{:^80}'.format(s) for s in messag1.split('\n')))
        else:
            unmask =(add_gussed_char_masked_word(posi , user_input1, masked_word))
            unmask_str = ''.join(unmask)
            print(unmask_str)
            masked_word = add_gussed_char_masked_word(posi , user_input1, masked_word)
            if unmask_str == selected_word:
                print("\n\n")
                print(26 * u"\u2668")
                print("Congratulations! You WON.")
                print(26 * u"\u2663")
                print("\n\n")
                break
        count = count - 1
        print("remining chances: ", count,"\n")
        if count == 0:
            print("Sorry! you lose")
            print("The word was: ", selected_word)
            break
    return count




def main():
    Message = "welcome to Hangman_Game\nYou have 10 chances!"       
    print('\n'.join('{:^80}'.format(s) for s in Message.split('\n')))
    selected_word = get_secret_word()
   #print(selected_word)
    print(mask_selected_word(selected_word))
    chances(10)
    

       
   #print("remining chances:", chances(10) ,'\n')
        
        

        


if __name__ == '__main__':
    main()
