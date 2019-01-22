## 멜론 탑100 상세페이지 링크를 크롤대상테이블(MeltopList)에 저장하시오.(단, 크롤여부 컬럼을 추가하시오)

import pymysql
import requests
from bs4 import BeautifulSoup
import re

target_url = "https://www.melon.com/chart/"

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" }

res = requests.get(target_url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

selector1 = "div.rank03 a"
js_urls = soup.select(selector1)


# pattern = re.compile("\:(.*)건")
# case_cnt = re.findall(pattern, case_cnt_tag)

pattern = re.compile("\('(.*)'\)")

urls = []
for href in js_urls:
    url = href.get('href')
    url_no = re.findall(pattern, url)    
    urls.append(url_no)

print(len(urls))
print(type(urls[0]))
print(urls)