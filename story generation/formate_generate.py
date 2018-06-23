import image_description_copy

img = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13001000/Beagle-On-White-01-400x267.jpg'
type, name, description = image_description_copy.recognize_image(img)
#print(name)

with open('data/story.txt', 'r') as f:
    text = f.readlines()

for i in text:
    temp = i.replace('_', name)
    temp = temp.replace('\n', '')
    print(temp)
