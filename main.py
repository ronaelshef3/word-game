from game_function import *
from output_string import Outputs
import random
from colorama import Fore,  Style

# Const Definition
class Outputs:
    def __init__(self):
        self.NUM_OF_TRIES = 7
        self.WELCOME = '''
           _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/        



        '''
        self.COISE_FILE = '''
        Plase coise file of words or insert file path : 

        > Animals  <A>
        > Foods  <B>
        > Color <C>
        > Other file  <?>

        '''

        self.WIN = 'YOU ARE WINNER !!!'
        self.GAME_OVER = '''

        *****************************************************
        ^^^^^^^^^^^^^^^^                   ^^^^^^^^^^^^^^^^^^
                            GAME OVER
        ^^^^^^^^^^^^^^^^                   ^^^^^^^^^^^^^^^^^^

        ******************************************************                    
        '''

        self.PICTURE = ['x - ------x\n\n'
            , ''''x - ------x
|
|
|
|
|'''
            , '''x - ------x
|   |
|   0
|
|
|'''
            , '''x - ------x
|   |
|   0
|   #
|
|'''

            , '''x - ------x
|   |
|   0
|  / #\\
|
|'''

            , '''x - ------x
|   |
|   0
|  / # \\
|  /
|
'''
            , '''x - ------x
|   |
|   0
|  / # \\
|  /  \\
|
''']




# Checking if all word found
def check_win(secret_word, old_letters_guessed):
    for i in  secret_word:
        if  i not in old_letters_guessed:
            # print(i+'++ ')
            return  False
        # print(i)
    # print('TRUE')
    return True

# When  Letter is  correct,  to discover it
def show_hidden_word(secret_word, old_letters_guessed):
    s=[]
    for i in secret_word:
        if i in old_letters_guessed:
            s.append(i)
        else:
            s.append('_')
        s.append(' ')
    return ''.join(s[:-1])

# Input  validation
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed)!= 1 :
        return False
    if letter_guessed  not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True
# Input ////////
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

# Selection random word from file
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

    # Checking one letter
def is_letter_correct(letter_guessed,secret_word,old_letters_guessed):
    if check_valid_input (letter_guessed,old_letters_guessed):
        if letter_guessed in secret_word:
            return True
        return False


# count word in file
def num_of_word(file_path):

    words = []
    f = open(file_path, 'r')
    for i in f:
        words.append(f.readline())


    f.close()

    return len(words)

# Output message for incorrect letter (drow the hangman by leval
def print_hangman(num_of_tries):
    o =Outputs()
    print(o.PICTURE[num_of_tries+1])



# list of words file (key:value )
files= {
    'A': 'animals.dat',
    'B':'food.dat',
    'C':'Colors.dat'



}

# Global variable definition
secret_word = None
letter_guessed =[]
old_letters_guessed=[]
# num_of_try=0


# The game
def main():
    # file_path = None

    # variable definition and init them
    num_of_try = 0
    o = Outputs()


    # Start message
    print(Fore.LIGHTYELLOW_EX+o.WELCOME)

    # request input from user
    f=  input(Fore.BLUE+o.COISE_FILE)

    # from file word or other files
    if f  in files.keys():
        file_path=files[f]
    else :
        file_path = input (Fore.BLUE+"please enter path of file ! ")
        try:
            open(file_path)
        except FileExistsError as  e :
            print( Fore.RED+" file is not valid {} {}".format(file_path,e))

    # select ramdom word
    index = random.randint(0,num_of_word(file_path) )
    secret_word =choose_word(file_path,index+1)

    # print ("DEBUG {}".format(secret_word))
    if secret_word is not None:

        # Game loop
        # print (f"DEBUG {num_of_try}:{o.NUM_OF_TRIES}= {num_of_try < o.NUM_OF_TRIES}")
        while num_of_try < o.NUM_OF_TRIES:

            l = input("try letter ")

            if try_update_letter_guessed(l, old_letters_guessed):

                # When letter corrct
                if l in secret_word:
                    print(show_hidden_word(secret_word,old_letters_guessed))
                    if check_win(secret_word, old_letters_guessed):
                        print(Fore.GREEN+o.WIN)

                        return 0
                else:
                    print(Fore.LIGHTMAGENTA_EX+o.PICTURE[num_of_try])
                    num_of_try +=1
        # When 7 tries
        print(Fore.RED+o.GAME_OVER)




if __name__=="__main__":
    main()
