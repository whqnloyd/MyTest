import random


def chat_robot():
    answers = [
        'i do not understand what you just said',
        'it does not mean anything to me',
        'i do not know, whatever',
    ]

    while 1:
        user_input = input('please talk with me:')
        if user_input.lower() == 'hi':
            print('hello')
        elif user_input.lower() == 'stop':
            break
        else:
            print(random.choice(answers))


if __name__ == '__main__':
    chat_robot()
