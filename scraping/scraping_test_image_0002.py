import urllib.request

url = "http://www.weather.go.kr/repositary/image/rdr/img/RDR_CMP_WRC_201901081250.png"

saveFile = "d:/workspace/hello/scraping/results/scraping_test_image_0002.png"
mem = urllib.request.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")