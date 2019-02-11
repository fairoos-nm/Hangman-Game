# test_hangman.py

import hangman

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
    assert (hangman.mask_selected_word("words") == "*****")


def test_chek_gussed_char_psition():
    assert (hangman.chek_gussed_char('a', 'mankind')) == [1]

def test_add_gussed_char_masked_word():
    assert(hangman.add_gussed_char_masked_word([1,5,6], 'n','********')) == ['*', 'n', '*', '*', '*', 'n', 'n', '*']


def test_for_Win_main():
    input_values=['e','l', 'p','h','a','n','t']
    output=[]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    hangman.input=mock_input
    hangman.print=lambda s :output.append(s)

    hangman.main("elephant")
            
    assert output[1] == "Number of tries left: 10"
    assert output[3] == "Enter your guess:  "
    assert output[4] == "e*e*****"
    assert output[35] == "Congratulations! You WON."
def test_for_Lose_main():

    input_values=['k','k', 'k','k','k','k','k','k','k','k']
    output=[]

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    hangman.input=mock_input
    hangman.print=lambda s :output.append(s)

    hangman.main("elephant")

    assert output[1] == "Number of tries left: 10"
    assert output[4] == "Wrong Guess:"
    assert output[50] == "Too bad! The secret word was elephant"
