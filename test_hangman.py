# test_hangman.py

import hangman
import pytest

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun
def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))

# 4. Mask the selected word
    
def test_mask_selected_word():
    assert (hangman.mask_selected_word("words") == "🔒🔒🔒🔒🔒")


def test_chek_gussed_char_psition():
    assert (hangman.chek_gussed_char('a', 'mankind')) == [1]
    assert (hangman.chek_gussed_char('w', 'mankind')) == []

def test_add_gussed_char_masked_word():
    assert(hangman.add_gussed_char_masked_word([1,5,6], 'n','********')) == ['*', '🅝 ', '*', '*', '*', '🅝 ', '🅝 ', '*']

def test_user_input_multiple_char():
    def fake_input(_):
        return 'aa'
    assert hangman.user_input(fake_input) == None
def test_user_input_normal():
    def fake_input(_):
        return 'a'
    assert hangman.user_input(fake_input) == 'a'

def test_check_allReady():
    assert hangman.check_allReady('a' ,['a' ,'b','c']) == True


