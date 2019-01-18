## 멜론 top 100 앨범재킷 scraping

import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

selector = ".wrap a img"
images = soup.select(selector)

for i, image in enumerate(images):
    image_url = image.get('src')
    img = requests.get(image_url).content

    saveFile = "./results/images/"+str(i+1)+".jpg"
    with open(saveFile, mode="wb") as file:
        file.write(img)
        print("----------"+saveFile+"----------")
