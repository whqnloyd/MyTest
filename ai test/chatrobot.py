import random
answers=['i did not understand what you just said',
         'it does not look like anything to me',
         'i do not know, whatever']
while 1:
    user_input=input('please input to me:')
    if user_input.lower()=='hi':
        print('hello')
    else:
        print(random.choice(answers))