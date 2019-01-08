from bs4 import BeautifulSoup
import requests

url = "https://s.pstatic.net/static/www/mobile/edit/2019/0108/mobile_114723757849.jpg"
img = requests.get(url).content

saveFile = "d:/workspace/hello/scraping/results/scraping_test_image_0003.jpg"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")
