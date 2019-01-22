import pymysql
import requests
from bs4 import BeautifulSoup
import re

## mysql 에 접속해서 MelList 한 코드씩 읽어서 접속을 해야...

def get_albumno(mysql_songno):
    target_url = "https://www.melon.com/song/detail.htm"

    headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" }

    params = { "songId" : mysql_songno }

    res = requests.get(target_url, headers=headers, params=params)
    soup = BeautifulSoup(res.text, 'html.parser')

    selector1 = "dl.list dd a"
    js_urls = soup.select(selector1)

    pattern = re.compile("\('(.*)'\)")
    urls = []
    for href in js_urls:
        url = href.get('href')
        url_no = re.findall(pattern, url)    

    return url_no[0]


if __name__ == '__main__':
    get_albumno("31113240")