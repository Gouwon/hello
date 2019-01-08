import urllib.request

# 기상청 사이트에서 2018년에 발생한 국내 지진 목록을 다운로드합니다.

url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm=2018-01-01&endTm=2018-12-31"

saveFile = "d:/workspace/hello/scraping/results/earthquake_domain_2018.html"
mem = urllib.request.urlopen(url).read()
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")
