import melon_utils as mu 
import codecs
import csv
mu.get_top100list()

csvFile = codecs.open('./results/melon_top_100_list(20190123).csv', 'r', 'utf-8')
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

sql = 'insert into MelList(SongId, AlbumId) values(%s, %s)'
lst = []
for row in reader:
    # lst = [str(row[1]), str(row[4])]
    # mu.insert_data_to_db("dooodb", sql, lst)
    lst.append((row[1], row[4]))
    print(lst)

import pymysql

conn = mu.get_conn('dooodb')

with conn:
    cur = conn.cursor()
    cur.executemany(sql, lst)
print("=============== MelList Insert Completed! =================")
