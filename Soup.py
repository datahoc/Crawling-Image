import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://www.glamira.com/rings-home/')
soup = BeautifulSoup(page.content, 'html.parser')
wrapper = soup.find('body')

images = wrapper.find_all('img')
for image in images:
    imgData = image['src']
    downloadPath = './download'
    filename = imgData.split('/')[-1]
    print(imgData)

    response = requests.get(imgData)

    file = open(downloadPath + filename, "wb")
    file.write(response.content)
    file.close()