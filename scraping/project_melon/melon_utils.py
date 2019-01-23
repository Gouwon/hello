def get_conn(db):
    import pymysql

    return pymysql.connect(
    host='localhost',
    user='dooo',
    password='root1!',
    port=3306,
    db=db,
    charset='utf8')

def get_html(url, method, params = ""):
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    if params != "":
        params = params

    if method == 'get':
        res = requests.get(url, headers=headers, params=params)
    elif method == 'post':
        res = requests.post(url, headers=headers, params=params)
    else:
        print("Wrong Method!! Check your request method!")
        exit()

    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def get_json(url, method, params = ""):
    import requests
    import json

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    if params != "":
        params = params    

    if method == 'get':
        res = requests.get(url, headers=headers, params=params)
    elif method == 'post':
        res = requests.post(url, headers=headers, params=params)
    else:
        print("Wrong Method!! Check your request method!")
        exit()

    html = requests.post(url, params=params, headers=headers).text

    jsonData = json.loads(html)
    return jsonData


def write_csv(location, contents = ""):
    ## location is file location to read or save
    ## mode only 'w' or 'a'
    import codecs
    import csv

    with codecs.open(location, 'w', 'utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"')
        writer.writerow(contents)



def insert_data_to_db(db, sql, lst):
    import pymysql

    conn = get_conn(db)

    with conn:
        cursor = conn.cursor()
        cursor.execute(sql, lst)
    

def get_top100list():
    import re
    import datetime
    import codecs
    import csv

    now = datetime.datetime.now()
    n = now.strftime('%Y%m%d')

    url = "https://www.melon.com/chart/"
    method = 'get'
    html = get_html(url, method)

    selector = 'tbody tr'
    html_tags = html.select(selector)
    pattern = re.compile("'(.*)'")

    saveFile = './results/melon_top_100_list({}).csv'.format(n)
    print(saveFile)
    with codecs.open(saveFile, 'w', 'utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"')
        for html_tag in html_tags:
            rank = html_tag.select_one("span.rank").text
            songId = html_tag.get('data-song-no')
            title = html_tag.select_one('div.ellipsis.rank01').text.strip()
            artist = ",".join([artist_name.text for artist_name in html_tag.select('div.ellipsis.rank02 span a')])
            albumId = re.findall(pattern, html_tag.select_one('div.wrap a').get('href'))[0]
            albumTitle = html_tag.select_one('div.wrap a').get('title')

            result = [rank, songId, title, artist, albumId, albumTitle]
            print(rank, songId, title, artist, albumId, albumTitle)
            print("===================")
            writer.writerow(result)
    print("+++++++++++++++++++++++++", saveFile, " saved +++++++++++++++++++++++++")


if __name__ == "__main__":

    # url = "https://www.melon.com/song/detail.htm"
    # params = { "songId" : "31113240" }
    # html = get_html(url, 'get', params=params)
    # print(html)

    url2 = "https://www.melon.com/album/detail.htm"
    params2 = {"albumId" : "10223837" }
    html2 = get_html(url2, 'get', params=params2)
    print(html2)