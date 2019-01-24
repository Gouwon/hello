import melon_utils as mu 
import codecs
import csv

## 멜론 Top100 list를 csv 파일로 저장하고, 읽은 뒤, MelList에 입력
# mu.get_top100list()

csvFile = codecs.open('./results/melon_top_100_list(20190123).csv', 'r', 'utf-8')
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

sql = 'insert into MelList(SongId, AlbumId) values(%s, %s)'

for row in reader:
    lst = (row[1], row[5])
    mu.insert_data_to_db("dooodb", sql, lst)

print("=============== MelList Insert Completed! =================")

## MelList에 입력된 노래들을 읽어서 크롤링할 준비
sql_select_mellist = "select albumId, songId from MelList where crawl = 0"
conn = mu.get_conn('dooodb')
with conn:
    cur = conn.cursor()
    cur.execute(sql_select_mellist)
    lis = cur.fetchall()

print("================ MelList Read Completed! ==================")

## lis에 저장된 노래들을 하나씩 Album, Song 테이블에 입력 후, MelList에 크롤링 여부 체크
for numbers in lis:
    lst = mu.get_albuinfo(numbers[0])
    sql_insert_album = "insert into Album(albumId, title, score, releaseDate, publisher, label) values(%s, %s, %s, %s, %s, %s) on duplicate key update score = values(score)"
    mu.insert_data_to_db("dooodb", sql_insert_album, lst)
    lst2 = mu.get_songinfo(numbers[1], numbers[0])
    sql_insert_song = "insert ignore into Song(songId, title, artist, genre, albumId) values(%s, %s, %s, %s, %s)"
    mu.insert_data_to_db("dooodb", sql_insert_song, lst2)

    ## sql_update_mellist 실행
    sql_update_mellist = "update MelList set crawl = 1 where crawl = 0 and albumId = {} and songId = {}".format(numbers[0], numbers[1])
    conn_melList = mu.get_conn('dooodb')
    with conn_melList:
        cur_melList = conn_melList.cursor()
        cur_melList.execute(sql_update_mellist)

    print("<<<<<<<<<<<<<< {} - {} Insert Completed! >>>>>>>>>>>>>>>".format(lst2[2], lst2[1]))

print("=============== Song & Album Insert Completed! =================")

## 마지막으로 SongRank에 노래들의 순위 정보를 csv 파일을 읽어서 저장
sql2 = 'insert into SongRank(SongId, rank, rankDate, likecnt) values(%s, %s, %s, %s)'
reader2 = csv.reader(csvFile, delimiter=',', quotechar='"')

import datetime
now = datetime.datetime.now()
n = now.strftime('%Y%m%d')

for row in reader2:
    lst = (row[1], row[0], n, row[4])
    mu.insert_data_to_db("dooodb", sql2, lst)

print("=============== SongRank Insert Completed! =================")

