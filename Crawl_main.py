from bs4 import BeautifulSoup
import requests
from Crawl_game import Game


url = "https://play.google.com/store/apps/collection/topselling_paid"
res = requests.get(url) ## get은 엽서(간단한 내용과 주소)를 보내는 것, post라는 함수는 편지라고 생각하면 된다. ## 서버에서 정보를 받아오는 것.
# print(res.text) 서버는 응답으로 편지를 보낸다. 그 안에는 text, statuscode 등이 있다. 
soup = BeautifulSoup(res.text, 'html.parser')   ## 정보를 분석하는 부분.
card_list = soup.select('div.card-list')        ## soup.select(selector) ## (태그)(.class)(attribute==element)  ## 셀렉트하면 tag를 찾아서 list로 넘겨준다.
# print(card_list)      

print(">>>>> ", len(card_list), card_list[0].get('class'))      ## card_list에도 html <tag>가 들어가 있으니까 이를 다시 한 번 여과한다. ## tag에서 get은 attribute를 받아오는 함수. 리스트 안에는 지금 tag들이 있다.

games = list()

for i in card_list:
    cards = i.select('.card')
    print("LLL>>> ", len(cards))
    for c in cards:         ## parsing 부분.
        games.append(Game(c))

for i in games:
    print(i)