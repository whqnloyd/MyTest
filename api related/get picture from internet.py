import requests
from bs4 import BeautifulSoup

url = 'https://images.google.com/'
header = {'User-Agent': 'Chrome/50.0.2661.102'}
html = requests.get(url,headers = header)
soup = BeautifulSoup(html.text,'html.parser')

all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')

for a in all_a:
    title = a.get_text() #提取文本
    print(title)