# hangman.py

import random
import time
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
    print(selected_word)
    word_len = len(selected_word)
    masked_word = ((word_len) * "🔒")  
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
char_dict = {"a":"🅐 ", "b":"🅑 ", "c":"🅒 ", "d":"🅓 ",
             "e":"🅔 ", "f":"🅕 ", "g":"🅖 ", "h":"🅗 ",
             "i":"🅘 ", "j":"🅙 ", "k":"🅚 ", "l":"🅛 ",
             "m":"🅜 ", "n":"🅝 ", "o":"🅞 ", "p":"🅟 ",
             "q":"🅠 ", "r":"🅡 ", "s":"🅢 ", "t":"🅣 ",
             "u":"🅤 ", "v":"🅥 ", "w":"🅦 ", "x":"🅧 ",
             "y":"🅨 ", "z":"🅩 "}  

def get_value(char, char_dict): 
    for key, value in char_dict.items(): 
        if char == key: 
            return value 

def get_unmask_string(unmask_str, char_dict):
    letters_list = unmask_str.split()
    make_list= list()
    for letter in letters_list:
        for key, value in char_dict.items():
            if letter +" " == value:
                make_list.append(key)
    word = ""
    for letters in make_list:
        word += letters
    return word
    
def add_gussed_char_masked_word(posi ,guessed_char, masked_word):
    mask_w = masked_word
    list_mask_w = list(mask_w)
    for i in posi:
        letter_emoji = get_value(guessed_char, char_dict)
        list_mask_w[i] = letter_emoji
    unmasked_word = list_mask_w
    return unmasked_word 

def user_input(input=input):
    user_input = input("Guess a character: ")
    if len(user_input)  != 1:
        print("{: ^80s}".format("🛑sorry,only one char allowed at a time🛑"))
    elif user_input.isupper():
        print("{: ^80s}".format("🛑please enter a lowercase letter🛑"))
    elif user_input.isnumeric():
        print("{: ^80s}".format("🛑numbers not allowde🛑"))
    else:
        return user_input
    
def check_allReady(user_ip, char_list):
    if user_ip in char_list:
        return True
    
def chances(count):
    selected_word = get_secret_word()
    masked_word =  mask_selected_word(selected_word)
    print()
    print("{: ^70s}".format(masked_word))
    char_list = []
    while (count > 0):
        print("\n", "= " * 50)
        user_input1 = user_input()
        if user_input1 == None:
            print("{: ^80s}".format("please enter a valied charector"))
            continue
        if check_allReady(user_input1, char_list) :
            print("{: ^80s}".format("Sorry!-You already guessed it"))
        char_list.append(user_input1)
        posi = chek_gussed_char(user_input1, selected_word)

        if len(posi) == 0:
            print("{: ^80s}".format("Your guess is wrong"))
        else:
            unmask =(add_gussed_char_masked_word(posi , user_input1, masked_word))
            unmask_str = ''.join(unmask)
            print("\n", "{: ^70s}".format(unmask_str))
            masked_word = add_gussed_char_masked_word(posi , user_input1, masked_word)
            unmask_string = get_unmask_string(unmask_str, char_dict)
            if unmask_string == selected_word:
                print("\n\n")
                print(26 * "🏆")
                print("Congratulations! You WON.")
                print(26 * "🏆")
                print("\n\n")
                break
        count = count - 1
        for i in range(count):
            print("💎", sep=' ', end='', flush=True)
            time.sleep(.1)
        if count == 0:
            print()
            print("{: ^80s}".format("Sorry! you lose"))
            print("🡆 The word was: ", selected_word)
            break
    return count

def main():
    Message = "welcome to Hangman_Game\nYou have 10 chances!"       
    print('\n'.join('{:^80}'.format(s) for s in Message.split('\n')))
    chances(10)
 
if __name__ == '__main__':
    main()
