import os
class Outputs:
    def __init__(self):

        self.NUM_OF_TRIES=7
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
        self.COISE_FILE ='''
        Plase coise file of words or insert file path : 
        
        > Animals  <A>
        > Foods  <B>
        > Color <C>
        > Other file  <?>
        
        '''

        self.WIN='YOU ARE WINNER !!!'
        self.GAME_OVER='''
        
        *****************************************************
        ^^^^^^^^^^^^^^^^                   ^^^^^^^^^^^^^^^^^^
                            GAME OVER
        ^^^^^^^^^^^^^^^^                   ^^^^^^^^^^^^^^^^^^
        
        ******************************************************                    
        '''

        self.PICTURE=['x - ------x\n\n'
        ,''''x - ------x
|
|
|
|
|'''
       ,'''x - ------x
|   |
|   0
|
|
|'''
       ,'''x - ------x
|   |
|   0
|   #
|
|'''

        ,'''x - ------x
|   |
|   0
|  / #\\
|
|'''


      ,'''x - ------x
|   |
|   0
|  / # \\
|  /
|
'''
     ,'''x - ------x
|   |
|   0
|  / # \\
|  /  \\
|
''']

    def clear(self):
             os.system("cls")

def main():
    c = Outputs()

    print(c.LOCK)
    print(c.GAME_OVER)
if __name__ =='__main__':
    main()