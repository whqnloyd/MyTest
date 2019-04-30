import random

def chat_robot():
    answers = [                                                             #list of answers
        'i do not understand what you just said',
        'it does not mean anything to me',
        'i do not know, whatever',
    ]

    while 1:                                                                #loop
        user_input = input('please talk with me:')                          #get input
        if user_input.lower() == 'hi':                                      #condition
            print('hello')
        elif user_input.lower() == 'stop':
            break
        else:
            print(random.choice(answers))

if __name__ == '__main__':                                                   #self test
    chat_robot()