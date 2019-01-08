import urllib.request

url = "http://www.weather.go.kr/repositary/image/sat/coms/coms_mi_le1b_ir1_k_201901080330.thn.png"

saveFile = "d:/workspace/hello/scraping/results/scraping_test_image_0001.png"
urllib.request.urlretrieve(url, saveFile)
print("OK!")