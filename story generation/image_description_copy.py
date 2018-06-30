import requests

def recognize_image(img_path):
    #define the key and url for api, and path for img
    api_key = '0c36327545bf4cf2b51e5f8917245711'
    assert api_key
    api_url = 'https://eastus.api.cognitive.microsoft.com/vision/v2.0/analyze'

    #define request
    headers = {'Ocp-Apim-Subscription-Key': api_key}
    params = {'visualFeatures': 'Description, Categories', 'language': 'en'}
    data = {'url': img_path}

    #get response
    response = requests.post(api_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    results = response.json()

    #print information
    tags = results['description']['tags']
    description = results['description']['captions'][0]['text'].capitalize()
#    categories = results['categories'][0]['name']
#    temp = categories.split('_')
#    type = temp[0]
#    name = temp[1]

    return description, tags
'''
    #save
    with open('data/image.txt', 'w') as f:
        f.write('Tags:\n')
        for i in tags:
            f.write(i + '\n')
        f.write('Description:\n')
        f.write(description)
'''
#self test
if (__name__ == '__main__'):
    img = 'https://s3.amazonaws.com/v2p-prod/db/image/website/74185/f3815050-c58c-46d4-860c-e35b66f09ff5.jpg'
    description, tags = recognize_image(img)
    '''
    with open('data/image.txt', 'r') as img:
        img_text = img.read()
    print(img_text)
    '''
#    print(type)
#    print(name)
    print(description)
    print(tags)
