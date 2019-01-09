def get_earthquake_domain_list(startTm, endTm, filename):

    import urllib.request
    import platform

    os = platform.system()
    url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm={}&endTm={}".format(startTm, endTm)
    
    if os == "Windows":
        saveFile = "d:/workspace/hello/scraping/results/{}".format(filename)
    elif os == "Darwin":
        saveFile = "./results/{}".format(filename)
        
    mem = urllib.request.urlopen(url).read()
    with open(saveFile, mode="wb") as file:
        file.write(mem)

    print("OK!")

get_earthquake_domain_list('2019-01-01', '2019-01-08', 'earthquake_domain_2019.html')