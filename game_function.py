import output_string
from main import files

from output_string import Outputs


def check_win(secret_word, old_letters_guessed):
    for i in  secret_word:
        if  i not in old_letters_guessed:
            # print(i+'++ ')
            return  False
        # print(i)
    # print('TRUE')
    return True

def show_hidden_word(secret_word, old_letters_guessed):
    s=[]
    for i in secret_word:
        if i in old_letters_guessed:
            s.append(i)
        else:
            s.append('_')
        s.append(' ')
    return ''.join(s[:-1])

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed)!= 1 :
        return False
    if letter_guessed  not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input (letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        s=[]
        for i in old_letters_guessed:
            s.append(i)
            s.append(' > ')
        print(''.join(s[:-1]))
        return False

def choose_word(file_path, index):
    if index < 1 :
        return  None
    else:
        words = []
        f = open(file_path ,'r')
        for  i in f:
            words.append(f.readline())
        if index > len(words):
            return None
        list(set (words))

        f.close()


        return  words [index].strip()
def is_letter_correct(letter_guessed,secret_word,old_letters_guessed):
    if check_valid_input (letter_guessed,old_letters_guessed):
        if letter_guessed in secret_word:
            return True
        return False



def num_of_word(file_path):

    words = []
    f = open(file_path, 'r')
    for i in f:
        words.append(f.readline())


    f.close()

    return len(words)


def print_hangman(num_of_tries):
    o =Outputs()
    print(o.PICTURE[num_of_tries+1])



def main():
    # secret_word = "friends"
    # old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    # print_hangman(5)
    # print(show_hidden_word('seretword',['s','w']))
    print(check_win('win',['w','n','i']))

if __name__ == '__main__':
    main()
