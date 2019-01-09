from bs4 import BeautifulSoup
import requests
import platform

os = platform.system()

url = "https://s.pstatic.net/static/www/mobile/edit/2019/0108/mobile_114723757849.jpg"
img = requests.get(url).content

if os == "Windows":
    saveFile = "d:/workspace/hello/scraping/results/scraping_test_image_0003.jpg"
elif os == "Darwin": 
    saveFile = "./results/scraping_test_image_0003.jpg"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("OK!")
