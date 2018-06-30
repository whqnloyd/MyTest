import image_description_copy

list_animal = ['dog', 'cat', 'bear', 'monkey', 'tiger', 'bird', 'pig', 'cow', 'deer', 'duck', 'turtle', 'rabbit', 'sheep']
list_color = ['yellow', 'blue', 'red', 'black', 'green', 'white']
list_action = ['sitting', 'eating']

img = 'http://www.lazerhorse.org/wp-content/uploads/2013/09/Sheep-Vs-Cow.jpg'
description, tags = image_description_copy.recognize_image(img)

capture_animal = []

def L1():
    with open('data/L1.txt', 'r') as f:
        text = f.readlines()
    for i in text:
        temp = i.replace('animal_1', capture_animal[0])
        temp = temp.replace('\n', '')
        print(temp)

def L2():
    with open('data/L2.txt', 'r') as f:
        text = f.readlines()
    for i in text:
        temp = i.replace('animal_1', capture_animal[0])
        temp = temp.replace('animal_2', capture_animal[1])
        temp = temp.replace('\n', '')
        print(temp)

for i in tags:
    for ii in list_animal:
        if i == ii:
            capture_animal.append(ii)

if len(capture_animal) == 0:
    print('Can not recognize the picture')
elif len(capture_animal) == 1:
    L1()
elif len(capture_animal) == 2:
    L2()
else:
    print('It is not you, it is me.')

#test function

print(description)
print(tags)
