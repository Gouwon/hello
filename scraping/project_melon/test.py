import melon_utils as mu 
import codecs
import csv
import datetime

now = datetime.datetime.now()
n = now.strftime('%Y%m%d')
db = "melondb"

file_location = "./results/melon_top_100_list({}).csv".format(n)


sql2 = 'insert into SongRank(songId, rank, likecnt, rankDate) values(%s, %s, %s, date_format(now(), "%%Y%%m%%d"))'
# sql2 = 'insert into SongRank(songId, rank, likecnt, rankDate) values(%s, %s, %s, "20190125")'

csvFile2 = codecs.open(file_location, 'r', 'utf-8')
reader2 = csv.reader(csvFile2, delimiter=',', quotechar='"')

for row in reader2:
    lst = (row[1], row[0], row[4])
    mu.insert_data_to_db(db, sql2, lst)

print("=============== SongRank Insert Completed! =================")