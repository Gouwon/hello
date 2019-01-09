from bs4 import BeautifulSoup
import requests


selector = "$('iframe').contentDocument"


def get_iframe(url):
    from bs4 import BeautifulSoup
    import requests

    headers = { "referer" : "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND"}

    param = { 'menuGubun': 'A', 'p_apt_code': 20064683, 'p_house_cd': 1, 'p_acc_year': 2018 }

    mem = requests.get(url, params=param, headers=headers).content

    print(mem)
    saveFile = "d:/workspace/hello/scraping/results/test.html"
    with open(saveFile, mode="wb") as file:
        file.write(mem)

url = "http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do"
get_iframe(url)
