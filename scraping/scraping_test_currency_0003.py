from bs4 import BeautifulSoup
import requests

def toFloat(s):
    return float(s.text.strip().replace(',', ''))

url = "https://finance.naver.com/marketindex/exchangeList.nhn"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

trs = soup.select('table > tbody > tr')

for tr in trs:
    tds = tr.select('td')
    print(">>>>>>>>>>>>>>>",tr)
    print("=================",tds)
    print("+++++++++++++++++++++")
    if (len(tds) < 4):
        continue

    tit = tds[0]
    rate = tds[1]
    diff = toFloat(tds[2]) - toFloat(tds[3])
    print(")))))))))))))))))))))))))))))",type(tit))
    print("{}, {}, {}".format(tit.text.strip(), rate.text, diff))
    