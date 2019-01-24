import melon_utils as mu 
import codecs
import csv

sql2 = 'insert into SongRank(SongId, rank, rankDate, likecnt) values(%s, %s, %s, %s)'
csvFile2 = codecs.open('./results/melon_top_100_list(20190124).csv', 'r', 'utf-8')
reader2 = csv.reader(csvFile2, delimiter=',', quotechar='"')

import datetime
now = datetime.datetime.now()
n = now.strftime('%Y%m%d')

for row in reader2:
    lst = (row[1], row[0], '20190124', row[4])
    mu.insert_data_to_db("dooodb", sql2, lst)

print("=============== SongRank Insert Completed! =================")